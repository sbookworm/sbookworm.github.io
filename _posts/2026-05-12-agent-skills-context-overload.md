---
title: "你的 Agent 正在被 Skills 淹没：为什么'装越多越好'是个危险的误区"
date: 2026-05-12
categories: [llm-study]
tags: [LLM学习记录, Agent, Skills, Context, Claude Code, 上下文]
toc: true
permalink: /llm-study/agent-skills-context-overload/
---

# 你的 Agent 正在被 Skills 淹没：为什么"装越多越好"是个危险的误区

> Context 是珍贵资源，不是垃圾桶。

---

## 一、从 OpenClaw 爆火说起

Claude Code、OpenClaw、Hermes 等 AI Agent 工具的崛起点燃了整个 Agent 生态。一夜之间，"Agent" 成了科技圈最热的关键词，GitHub 上涌现出数以千计的 Agent 框架、Skill 库、Plugin 仓库。

开发者们兴奋地给自己的 Agent 装上各种"能力"：
- 代码审查 Skill
- 文档生成 Skill
- 数据分析 Skill
- API 调用 Skill
- 浏览器操作 Skill
- ...

**装得越多，能力越强，对吧？**

这是一个看似合理却极其危险的假设。

我在社区中看到有人一次性给自己的 Claude Code 安装了 **81 个 Skills**。81 个！这就像给一个员工塞了 81 份不同的工作手册，然后期望他能高效工作。

但问题远不止"手册太多"这么简单。Agent 的工作方式与传统软件完全不同——它的"手册"不是躺在文件夹里等着查阅，而是**时刻占据着它的"大脑"**。

---

## 二、Agent 中 Skill 的加载机制：以 Claude Code 为例

要理解为什么 Skill 过多是个问题，我们需要先理解 Agent 是如何"记住"这些 Skill 的。

### 2.1 两种加载方式

Claude Code（Anthropic 官方的 Agent CLI）采用了一套优雅的 Skill 管理机制，主要有两种加载方式：

**方式一：通过 Hook 自动注入**

Superpowers 插件通过 `SessionStart` Hook 在每次会话启动时自动注入其核心指导内容：

```
~/.claude/plugins/cache/claude-plugins-official/superpowers/5.1.0/
├── hooks/
│   ├── hooks.json        ← Hook 配置
│   └── session-start     ← 执行脚本
└── skills/
    └── using-superpowers/SKILL.md  ← 被注入的内容
```

当用户执行 `/startup`、`/clear` 或 `/compact` 时，Hook 触发，将 SKILL.md 的内容包装成 `<EXTREMELY_IMPORTANT>` 标签注入到 System Prompt 中。

**方式二：通过 system-reminder 加载 Skills 列表**

每次对话开始时，Claude Code 会扫描 Skills 目录，将所有可用 Skills 的描述（description）汇总成 system-reminder：

```
<system-reminder>
The following skills are available for use with the Skill tool:
- review: Pre-landing PR review...
- browse: Fast headless browser for QA testing...
- brainstorming: You MUST use this before any creative work...
- ship: Complete release workflow...
...（81 个 Skills）
</system-reminder>
```

### 2.2 Skill 的自动调用机制

关键点来了：**AI 如何决定调用哪个 Skill？**

这不是代码层面的自动匹配，而是 **AI 根据 prompt 指导自行判断**。

流程如下：

```
用户消息
    ↓
"Might any skill apply?" ← AI 自问
    ↓
扫描 system-reminder 中所有 skills 的 description
    ↓
如果 > 1% 可能匹配 → Invoke Skill tool
    ↓
加载 skill 内容，follow skill 指令
```

Superpowers 的指导中明确规定：

> "If you think there is even a **1% chance** a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill."

这意味着 AI 在每次收到用户消息后，都要扫描**全部 Skills 的描述**来判断是否需要调用。

### 2.3 真正的问题：固定上下文占用

有人可能会说："没关系，有 Prompt Caching，这些 system-reminder 的 token 消耗几乎为零。"

这是一个常见的误解。

| 维度 | System Prompt + system-reminder | 对话历史 |
|------|----------------------------------|----------|
| **Token 消耗** | 第 1 轮后缓存，后续几乎免费 | 每轮累积消耗 |
| **上下文占用** | ✓ 每轮都占用（**固定量**） | ✓ 每轮都占用（累积量） |

**Prompt Caching 降低了 API 成本，但不会减少上下文窗口的占用。**

Claude 的上下文窗口约 200K tokens。每轮对话时：

```
上下文窗口构成：
├─ System Prompt          ← 固定占用 (~2000-3000 tokens)
├─ system-reminder        ← 固定占用 (~5000-6000 tokens，81 个 Skills)
├─ 对话历史               ← 累积占用（不断增加）
└─ 总占用 = 固定部分 + 累积部分
```

81 个 Skills 的描述信息约 6000 tokens，**每轮对话都占据着这 6000 tokens 的位置**，无论是否被使用。

---

## 三、Skill 过多导致的冲突问题

当多个 Skills 同时匹配用户请求时，会发生什么？

### 3.1 多 Skill 匹配的处理

假设用户说："帮我写一个新功能"。

AI 判断：
```
├─ brainstorming 匹配 ✓ ("creating features, building components")
├─ TDD 匹配 ✓ ("implementing any feature")
├─ frontend-design 匹配？ (如果是前端功能)
├─ mcp-builder 匹配？ (如果涉及 MCP)
└─ 全部 > 1% 可能适用
```

AI 会尝试同时遵循这些 Skills 的指导。Superpowers 定义了优先级规则：

```
1. Process skills first (brainstorming, debugging)
   → 决定 HOW to approach the task

2. Implementation skills second (frontend-design, mcp-builder)
   → Guide execution
```

### 3.2 当 Skills 内容冲突

但不同插件提供的 Skills 可能存在指令冲突：

| 可能的结果 | 说明 |
|------------|------|
| 遵循语气更强的指令 | `<EXTREMELY_IMPORTANT>` 标签的内容优先 |
| 遵循后加载的内容 | LLM 特性：后出现的可能覆盖 |
| AI 行为不一致 | 最糟糕的情况，来回切换 |
| AI 向用户寻求澄清 | 如果冲突足够明显 |

我在实际使用中观察到：当安装了 Gstack 的 `review` skill 和另一个插件的 `code-review` skill 时，两者对"代码审查"的定义略有不同——一个强调 SQL 安全检查，另一个强调代码风格。AI 有时会混合执行，有时又会只选择其中一个，行为难以预测。

### 3.3 解决方案有限

目前的解决方案都有局限：

```
1. 只启用兼容插件 ← 但谁来定义"兼容"？
2. 项目级配置覆盖（CLAUDE.md） ← 需要手动维护
3. 用户在对话中明确指定 ← 每次都要说清楚
```

**用户指令优先级最高**，但这意味着用户需要承担额外的沟通成本。

---

## 四、"Lost in the Middle"：过长上下文的科学证据

即使 Skills 没有冲突，单纯的上下文过长也会严重损害模型表现。

### 4.1 U型性能曲线

Stanford 和 UC Berkeley 的研究团队在论文《Lost in the Middle: How Language Models Use Long Contexts》中发现了一个惊人的现象：

当改变相关信息在输入上下文中的位置时，模型表现呈现**U型曲线**：

```
性能
 ↑    \              /
 │     \            /
 │      \          /
 │       \________/
 └────────────────────→ 信息位置
       开头   中间   结尾
```

- **开头**（首位偏见 primacy bias）：✅ 表现好
- **中间**：❌ 表现显著下降（可下降 20%+）
- **结尾**（近因偏见 recency bias）：✅ 表现好

### 4.2 令人惊讶的结果

| 模型 | 中间位置性能 |
|------|-------------|
| GPT-3.5-Turbo | 低于无文档基线（56.1%） |
| Claude-1.3 | 类似 U 型曲线 |

> **关键洞察**: 更长的上下文窗口 ≠ 更好地使用上下文

当答案文档被放在 20-30 个文档的中间位置时，GPT-3.5-Turbo 的表现甚至**低于完全没有文档**时的表现。

### 4.3 这与 Skills 有什么关系？

把 81 个 Skills 的描述放在 system-reminder 中，意味着：

1. **真正重要的指令**（如 Superpowers 的核心指导）被放在开头，表现良好
2. **中间的 Skills 描述**很可能被模型"忽略"或弱化处理
3. **最后几个 Skills**可能因为近因偏见获得更多关注

这不是我们想要的行为。我们希望模型能准确判断何时使用哪个 Skill，而不是因为它在列表中间就被"遗忘"。

### 4.4 多轮对话中的"迷失"

Microsoft Research 和 Salesforce Research 的最新论文《LLMs Get Lost In Multi-Turn Conversation》进一步揭示了问题的严重性：

在多轮不完整指定的对话中，所有顶级 LLM 性能平均下降 **39%**。

关键发现：**当 LLM 在对话中走错一步时，它就会迷失，且无法恢复。**

论文识别了四大根因：

1. **过早给出答案**：在信息不完整时做出错误假设
2. **答案膨胀**：后续答案越来越长且混乱
3. **中间轮次遗忘**：只关注第一轮和最后一轮的信息
4. **过度冗长**：长回复包含更多假设，导致后续混乱

这与 Skills 过多的问题直接相关：
- 大量 Skills 描述增加了上下文复杂度
- AI 在判断"是否需要调用 Skill"时可能过早做出决定
- 错误的 Skill 调用会级联放大，导致整个对话迷失

---

## 五、Context 是珍贵资源，请精确控制

### 5.1 核心原则

> **Context 不是垃圾桶，而是 Agent 的"工作记忆"。**

每一个放入 Context 的内容都应该有明确的目的：
- 这条 Skill 真的是我**经常需要**的吗？
- 这条 Skill 与其他 Skills 是否**功能重叠**？
- 这条 Skill 的描述是否**简洁精准**？

### 5.2 我的实践建议

**精简到 15-20 个核心 Skills**

经过实践，我建议保留以下核心 Skills：

```
方法论类（Superpowers 提供）：
├─ brainstorming（创造性工作前先思考）
├─ TDD（先写测试再写代码）
├─ systematic-debugging（系统化调试）
├─ writing-plans（多步骤任务先写计划）
├─ verification-before-completion（完成前验证）

常用工具类：
├─ review（PR 审查）
├─ ship（发布流程）
├─ browse（浏览器测试）
├─ investigate（问题调查）
├─ qa（QA 测试）

按需添加：
├─ 文档类（xlsx, pdf）← 如果经常处理
├─ 开发类（mcp-builder, conda）← 如果有特定需求
```

**其他 Skills 可以删除，需要时再安装。**

### 5.3 定期审视

建议每月审视一次 Skills 配置：

```bash
# 查看已安装的 skills
ls ~/.claude/skills/

# 统计数量
ls ~/.claude/skills/ | wc -l
```

问问自己：
- 这个 Skill 上周用过吗？
- 这个 Skill 是否与其他 Skill 功能重叠？
- 这个 Skill 的描述是否清晰？

### 5.4 项目级 Skills

对于特定项目的 Skills，放在项目目录下：

```
project/.claude/skills/
├─ project-specific-skill-1/
├─ project-specific-skill-2/
```

这样 Skills 只在该项目下可用，不会污染全局 Context。

---

## 六、结语

Agent 开发正处在一个"淘金热"时期。每天都有新的 Skill、新的 Plugin、新的框架涌现。

但请记住：

> **Agent 的能力不是由安装的 Skills 数量决定的，而是由 Agent 能否精准、高效地使用正确的 Skills 决定的。**

就像一个员工，给他 81 份工作手册不会让他更强，只会让他更困惑。同样，给 Agent 装满 Skills 不会让它更智能，只会让它更迷失。

Context 是珍贵资源。请精确控制 Skill 的开关，让 Agent 的"大脑"保持清晰、专注、高效。

---

## 参考资料

1. [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) - Stanford, UC Berkeley, 2023
2. [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120) - Microsoft Research, Salesforce Research, 2025
3. Claude Code Skills 机制分析（个人笔记）

---

*本文基于 Claude Code 的实践经验撰写，观点适用于大多数 Agent 框架。*
