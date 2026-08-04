---
title: AI学习
icon: fas fa-brain
order: 2
---

> 不做模型，只把模型用好——LLM、Agent 与 AI 安全，一处都看。

我是个搞体系结构的工程师，把 AI 当成"系统"来拆：从 LLM 的架构原理，到 Agent 的工程实践，再到 AI 安全的攻防现实，全部归在这里。

### LLM 基础

从架构到评估，搞懂大模型怎么"想到"答案。

1. [前言：一个体系结构工程师的 LLM 学习之路](/ai-learning/preface-engineers-llm-journey/)
2. [LLM 入门知识 — Ollama](/ai-learning/ollama-local-llm-runner/)
3. [从 Transformer 到 LLM：一场"断臂求生"的架构革命](/ai-learning/transformer-decoder-only-llm/)
4. [Transformer 知识 — 位置编码](/ai-learning/transform-knowledge-positional-encoding/)
5. [LLM 入门知识 — 位置编码外推](/ai-learning/llm-positional-encoding-extrapolation/)
6. [LLM 为什么会有上下文限制？](/ai-learning/llm-context-window-limit/)
7. [预训练与后训练](/ai-learning/pre-training-vs-post-training/)
8. [大模型上下文能力评估方法：NIAH 和 NoLiMa](/ai-learning/niah-nolima-eval/)

### Agent 与工程实践

把模型装进系统——Skills、上下文管理与工具调用。

1. [你的 Agent 正在被 Skills 淹没：为什么"装越多越好"是个危险的误区](/ai-learning/skill-not-the-more-the-better/)

### AI 安全

模型越强，攻击面越大——越狱、对齐伪装、奖励黑客与工程护栏。

1. [€0.02 转账劫持银行 AI 助手：Blue41/Bunq 间接提示注入案例学习](/ai-learning/blue41-bunq-prompt-injection/)
2. [AI 红队攻击图谱：从手工越狱到 Agent 多步攻击](/ai-learning/ai-red-team-attack-map/)
3. [AI 会不会在没有后果时也装乖？——《Do Models Fake Alignment Without Clear Consequences?》通俗拆解](/ai-learning/alignment-faking-without-consequences/)
4. [当 AI 开始"撒谎作弊"：奖励黑客、学术解法与工程护栏 — 一篇学习汇总](/ai-learning/ai-agent-reward-hacking-engineering-guardrails/)

---

> Agent 和 LLM 本来就拆不开——前者是后者的"驾驶舱"，后者是前者的"引擎"。这里把它们当作同一件事来记。