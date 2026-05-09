---
title: "Transformer知识-位置编码"
date: 2025-05-09
categories: [llm-study]
tags: [LLM学习记录, Transformer, 位置编码, Self-Attention]
toc: true
permalink: /llm-study/transform-knowledge-positional-encoding/
---

## 为什么需要位置编码？

### 从直观例子说起："我爱你" ≠ "你爱我"

在中文里，词语的顺序至关重要：
- **"我爱你"** —— 主语是"我"，表达的是我对你的感情
- **"你爱我"** —— 主语是"你"，表达的是你对我的感情

这两个句子意思完全不同。人类在阅读时，通过词语的**位置**来理解句子结构和含义。

但 Transformer 中的 Self-Attention 机制有个问题：**它天生"看不见"位置**。

---

## Self-Attention 为什么"看不见"位置？

### 核心原因：Attention 的计算逻辑本身不关心顺序

Attention 的核心运算是 `QK^T`（Query 和 Key 的点积）。关键在于：**矩阵乘法是交换对称的**。

举个例子，假设只有两个 token：

```
[q1, q2] · [k1, k2]^T  =  q1·k1 + q2·k2
[q2, q1] · [k2, k1]^T  =  q2·k2 + q1·k1   # 值完全一样！
```

只要 Q 和 K 同时颠倒顺序，点积的和不变。这意味着：**Attention 机制无法区分"谁在第几位"，只能区分"谁和谁有关联"**。

### 与 RNN 的对比

| | RNN / LSTM | Self-Attention |
|---|---|---|
| 处理方式 | 顺序逐步输入，第 t 步用到第 t-1 步的隐藏状态 | 所有 token **同时计算**，像集合运算 |
| 位置感知 | 天生有序（时间步天然编码位置） | 天生无序（需要**额外注入**位置信息） |

Self-Attention 把输入当作一个**集合**来处理，而不是一个**序列**。

### "顺序无关"的真实含义

**Attention 机制本身没有显式编码"第几个位置"这个信息。**

它知道"我"和"你"是不同的 token（因为它们的 embedding 不同），但它**不知道**"我"在句子开头还是结尾。

> 💡 注意：Attention **不会**把"我爱你"和"你爱我"完全等同，因为"我"和"你"的 token embedding 不同。但它不知道"我"在第1位、"你"在第2位——它只知道这些 token 之间的相似度关系。


---

## 位置编码如何解决问题？

既然 Self-Attention 天生缺乏位置感知能力，我们就需要**手动注入位置信息**。这就是位置编码（Position Encoding）的作用。

### 两类位置编码思路

**绝对位置编码**：直接告诉模型"这个 token 在第几个位置"
- Sinusoidal 编码（原版 Transformer）：用正弦/余弦函数生成位置向量
- 可学习位置编码（BERT/GPT-2 早期）：把位置当作可训练参数

**相对位置编码**：告诉模型"这两个 token 相距多远"
- 不关注"A 在哪"，而是关注"A 和 B 的距离"
- 更适合处理变长序列和长距离依赖

---

## 主流位置编码方案详解

### 1. Sinusoidal 位置编码（原版 Transformer）

用最简洁的数学函数给每个位置生成唯一"指纹"：

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d))
```

特点：
- **无需学习参数**，纯函数计算
- **理论上可外推**到训练时未见过的长度
- 实际效果在长序列上一般

---

### 2. RoPE（旋转位置编码）⭐ 当前最主流

被 **LLaMA、ChatGLM、Qwen、DeepSeek** 等几乎所有主流大模型采用。

**核心思想**：将位置信息编码为**旋转矩阵**，直接施加到 Query 和 Key 向量上。

数学形式（简化版）：对 embedding 维度两两配对，每对应用旋转：

```
R(pos, θ) = [cos(pos·θ)  -sin(pos·θ)]
            [sin(pos·θ)   cos(pos·θ)]

Q' = Q · R(pos, θ)
K' = K · R(pos, θ)
```

Attention 计算 `Q' · K'^T` 时，结果只依赖于两个位置的**相对距离** `(pos_i - pos_j)`。

**为什么 RoPE 这么受欢迎？**

1. **可外推**（Long Context）：理论上可以外推到更长序列，配合 NTK-aware Scaling、YaRN 等技术实现 32K/128K 长上下文
2. **无额外参数**：参数效率高
3. **与 Attention 自然融合**：位置信息直接进入 attention 计算

---

### 3. ALiBi（Attention with Linear Biases）

用于 **BLOOM** 等模型。

不添加位置向量，而是直接给 attention score 加一个基于距离的惩罚：

```
score(q_i, k_j) -= |i - j| * m
```

距离越远，注意力分数越低（线性衰减）。

特点：外推能力好、实现简单；但衰减方式是硬编码的，不够灵活。

---

## 关键区别：位置信息什么时候注入？

不同方案注入位置的**时机**和**方式**各不相同：

| 方案 | 注入时机 | 具体操作 | Q/K 本身是否带位置 |
|------|---------|---------|-------------------|
| **Sinusoidal** | 输入层 | 与 token embedding **相加** | ✅ 带位置（先融合再投影） |
| **RoPE** | 生成 Q/K **之后** | 对 Q/K 做**旋转乘法** | ❌ 先生成，再旋转注入 |
| **ALiBi** | Attention 计算时 | 给 score **加减法**偏置 | ❌ 完全不带，只改 logits |

### 代码层面的直观对比

**Sinusoidal（输入层相加）：**
```python
# 第1步：在输入层直接融合位置
X = token_emb + pos_emb

# 第2步：再生成 Q/K（此时已带位置）
Q = X @ W_Q
K = X @ W_K
```

**RoPE（生成后旋转）：**
```python
# 第1步：先生成 Q/K（无位置）
Q = X @ W_Q
K = X @ W_K

# 第2步：逐位置旋转注入
Q = rotate(Q, position_ids)  # 乘以旋转矩阵
K = rotate(K, position_ids)

# 第3步：计算 attention
scores = Q @ K.T
```

**ALiBi（计算时偏置）：**
```python
# 第1步：生成 Q/K（完全无位置）
Q = X @ W_Q
K = X @ W_K

# 第2步：计算 score 后加减位置偏置
scores = Q @ K.T
scores -= m * abs(i - j)  # 距离越远，惩罚越大
```

> 💡 **为什么 RoPE 更优雅？** 位置信息直接进入 attention 计算的核心（Q·K^T），而不是作为外部偏置。同时它保持了对相对位置的不变性——`rotate(Q_i) · rotate(K_j)` 的结果只取决于 `i-j`。

---

## 方案对比总结

| 方案 | 外推能力 | 参数开销 | 计算成本 | 代表模型 |
|------|---------|---------|---------|---------|
| Sinusoidal | 理论可外推，实际一般 | 无 | 低 | 原版 Transformer |
| 可学习绝对位置 | 差（无法外推） | O(N) | 低 | BERT, GPT-2 早期 |
| 相对位置 | 一般 | 较小 | 中等 | XLNet |
| **RoPE** | 较好（需配合扩展技术） | **无** | 中等 | **LLaMA, ChatGLM, Qwen** |
| ALiBi | 好 | 无 | 低 | BLOOM |

---

## 当前工程实践的共识

- **RoPE 是主流**：新训练的大模型基本清一色选 RoPE
- **长上下文是关键战场**：32K+ 场景下，RoPE 的外推能力是核心挑战
- **RoPE 缩放技术**：NTK-by-parts、YaRN、LongRoPE 等成为标配
- **中文模型**：ChatGLM、Qwen 等在 RoPE 基础上做了各自的扩展优化
