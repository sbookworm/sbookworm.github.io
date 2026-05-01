---
title: "LLM 入门知识 — Ollama"
date: 2026-05-01
categories: [llm-study]
tags: [Ollama, 本地部署, 入门]
toc: true
---

# LLM 入门知识 — Ollama

> 一句话概括：**Ollama 是一个让你在本地电脑上轻松运行大语言模型（LLM）的开源工具。**

---

## 本质定位

简单来说，Ollama 就是 **"本地版的大模型应用商店 + 运行环境"**。

- 它帮你解决了模型下载、配置、运行环境搭建的繁琐步骤
- 让你像使用 Docker 一样管理和运行各种开源大模型

---

## 核心特点

| 特点         | 说明                                      |
| ---------- | --------------------------------------- |
| **一键运行**   | `ollama run llama3` 即可下载并启动对话           |
| **本地部署**   | 模型跑在自己机器上，无需联网、数据不外流                    |
| **多模型支持**  | 支持 Llama、Mistral、DeepSeek、Gemma 等主流开源模型 |
| **自带 API** | 启动后自动暴露 REST 接口，方便接入其他应用                |
| **轻量量化**   | 自动处理模型量化和优化，普通电脑也能跑                     |

---

## 主要缺点

| 缺点                                              | 具体说明                                                                          |
| ----------------------------------------------- | ----------------------------------------------------------------------------- |
| **硬件门槛高**                                       | 本地跑大模型需要好 GPU / 大内存，普通电脑跑 7B 模型都卡，更大模型基本跑不动                                   |
| **量化精度损失**       | 为了适配普通硬件自动做量化（4bit/8bit），模型回答质量会比原版下降            |
| **性能天花板低**                                      | 相比 vLLM、TensorRT-LLM 等专业推理框架，吞吐量和并发能力弱很多                                      |
| **闭源模型不支持**                                     | 只能跑开源模型（Llama、Mistral 等），无法直接运行 GPT-4、Claude                                  |
| **缺少高级功能**                                      | 没有内置 RAG、Agent 编排、函数调用管理等，需要你自己搭建                                             |
| **磁盘占用大**                                       | 单个模型动辄 4GB~几十 GB，多装几个很占硬盘                                                     |
| **长上下文吃力**                                      | 本地跑 32K/128K 长上下文非常耗资源，容易爆内存                                                  |

> **一句话总结**：Ollama 的缺点是 **"易用性换性能"** —— 上手简单，但想跑得又快又好、功能又全，还得上更专业的方案。

---

## 运行原理（简单理解）

### 模型像一栋楼

大语言模型由很多**相同结构的层**堆叠而成。比如 Llama3-8B 有 32 层，输入文本从底层进去，逐层加工，顶层输出回答。

### 显存不够怎么办？

Ollama 会自动做**智能分层卸载**：

- **显存充足** → 所有层放 GPU，纯 GPU 推理（最快）
- **显存不足** → 自动将部分层放到 CPU 内存，GPU 和 CPU 接力计算
- **无 GPU** → 全部用 CPU + 内存推理

底层基于 llama.cpp，自动检测硬件后做混合推理，**无需手动配置**。

### 平台差异

| 平台                          | 内存/显存关系                            |
| --------------------------- | ---------------------------------- |
| **Windows / Linux（独显）**     | 显存和内存物理分离，Ollama 智能拆分模型层到两边        |
| **macOS（Apple Silicon）**    | 统一内存架构，CPU/GPU 物理共享同一块内存           |

---

## 安装配置

### 快速安装

对于大多数用户来说，最简便的方法是通过一个简单的命令完成安装：

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 手动安装

如果您需要更精细地控制安装过程，可以选择手动下载并解压包：

```bash
curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
sudo tar -C /usr -xzf ollama-linux-amd64.tgz
```

### 配置服务

Ollama 的端口、模型并行度等可通过配置文件修改。

编辑 `/etc/systemd/system/ollama.service` 文件，添加以下内容：

```ini
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=$PATH"

# Ollama 默认仅绑定 127.0.0.1:11434(只允许本机访问),
# 改成 0.0.0.0 后即可被局域网/远端访问
Environment="OLLAMA_HOST=0.0.0.0"
# 并行处理请求的数量
Environment="OLLAMA_NUM_PARALLEL=4"
# 同时加载的模型数量
Environment="OLLAMA_MAX_LOADED_MODELS=4"

[Install]
WantedBy=default.target
```

修改后需要重新加载并重启服务：

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
sudo systemctl status ollama   # 检查服务状态
```

---

## Troubleshooting

### 手动控制 GPU/CPU 分层

`num_gpu` 表示**缓存在 GPU 显存中的模型 layer 数量**。当显存较小时，可以减小这个值，让更多层落到内存中，用内存替代显存。

#### 临时修改（当前会话生效）

在运行模型的对话中直接设置：

```
/set parameter num_gpu 5   # 设置 5 层使用 GPU
```

#### 永久修改（生成新模型）

**1. 导出原模型的 Modelfile**（以 llama3 为例）：

```bash
ollama show llama3 --modelfile >> llama3.modelfile
```

**2. 编辑 `llama3.modelfile`，添加参数**：

```dockerfile
# 设置使用 GPU 缓存模型层的数量 5
PARAMETER num_gpu 5
```

**3. 重新创建模型**：

```bash
ollama create my-llama3 -f llama3.modelfile
ollama run my-llama3
```

### DeepSeek V2 多轮对话后报错

> **参考**：[llama.cpp issue #8862](https://github.com/ggerganov/llama.cpp/issues/8862)

#### 问题原因

DeepSeek V2 使用了 **MLA（Multi-Head Latent Attention）架构**，这种架构**不支持 KV cache 的 K-shift**（Context Shift / Cache 压缩）。

具体来说：

1. **MLA 架构的限制**：DeepSeek V2 的 MLA 设计把 key/value 压缩成一个低秩的 latent vector（`kv_lora_rank = 512`），这种压缩方式使得 KV cache 中的 token 位置无法通过传统的 RoPE K-shift 来调整。

2. **上下文满了怎么办**：普通模型（如 llama 架构）在 KV cache 快满时可以做 context shift（丢弃旧 token、重新调整剩余 token 的位置编码后继续生成）。但 DeepSeek V2 不能做这个操作，因为 K-shift 会破坏 MLA 的压缩表示。

3. **崩溃触发路径**：
   - 用户设置了 `-c 24600 --parallel 3`，每个 slot 分到的上下文是 `24600 / 3 = 8200` token
   - 当一个 slot 的 prompt + 生成 token 超过 8200 时，llama.cpp 尝试做 context shift（日志里看到 `slot context shift` 和 `kv cache rm`）
   - 代码检测到架构是 DeepSeek V2，触发断言：`GGML_ASSERT(!"Deepseek2 does not support K-shift")` → 程序崩溃

#### 解决方法

按 ggml-org 作者 ggerganov 的说法：**确保每个 slot 的上下文足够大，永远不要触发 context shift**。即：

```
num_predict <= -c / --parallel
```

例如 `-c 24600 --parallel 3` 时，每个 slot 最多 8200 token，限制 `--predict 4096` 就能保证不越界。作者还建议可以把 `-c` 降到 `3 * 4096 = 12288` 来节省 VRAM。

> **本质上这不是一个能"修"的 bug**，而是 MLA 架构的固有约束。llama.cpp 用 `assert` 做了防御性拦截（避免产生错误输出），而不是悄无声息地崩溃或产出垃圾结果。
