---
layout: post
title: Claude Code 速查表
date: 2026-03-25 08:00:00
categories: [工具]
tags: [Claude Code, 速查表, AI工具]
---

> 本文整理自 [banwagong1.com/claude-code.html](https://banwagong1.com/claude-code.html)，方便查阅使用。

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+C` | 取消输入/生成 |
| `Ctrl+D` | 退出会话 |
| `Ctrl+L` | 清屏 |
| `Ctrl+O` | 切换详细输出 |
| `Ctrl+R` | 反向搜索历史 |
| `Ctrl+G` | 在编辑器中打开提示 |
| `Ctrl+B` | 后台运行任务 |
| `Ctrl+T` | 切换任务列表 |
| `Ctrl+V` | 粘贴图片 |
| `Ctrl+F` (按两次) | 终止后台代理 |
| `Esc+Esc` | 回退/撤销 |
| `Shift+Tab` | 循环切换权限模式 |
| `Alt+P` | 切换模型 |
| `Alt+T` | 切换思考模式 |
| `\Enter` | 换行（快捷） |
| `Ctrl+J` | 换行（控制序列） |

## 命令速查

### 基础命令

| 命令 | 说明 |
|------|------|
| `/` | 斜杠命令 |
| `!` | 直接执行 bash |
| `@` | 文件引用 + 自动补全 |

### 导航与操作

| 按键 | 功能 |
|------|------|
| `↑↓` | 导航 |
| `←→` | 展开/折叠 |
| `P` | 预览 |
| `R` | 重命名 |
| `/` | 搜索 |
| `A` | 所有项目 |
| `B` | 当前分支 |

## MCP 服务器

```bash
--transport http    # 远程 HTTP（推荐）
--transport stdio   # 本地进程
--transport sse     # 远程 SSE
```

### MCP 配置位置

- `Local ~/.claude.json`（每个项目）
- `Project .mcp.json`（共享/VCS）
- `User ~/.claude.json`（全局）

### MCP 命令

```bash
/mcp                    # 交互式界面
claude mcp list         # 列出所有服务器
claude mcp serve CC     # 作为 MCP 服务器
```

## 斜杠命令

### 会话管理

| 命令 | 说明 |
|------|------|
| `/clear` | 清除对话 |
| `/compact [focus]` | 压缩上下文 |
| `/resume` | 恢复/切换会话 |
| `/rename [name]` | 命名当前会话 |
| `/branch [name]` | 分支对话（/fork 别名） |
| `/cost` | Token 用量统计 |

### 上下文与查看

| 命令 | 说明 |
|------|------|
| `/context` | 可视化上下文（网格） |
| `/diff` | 交互式差异查看器 |
| `/copy` | 复制上次回复 |
| `/export` | 导出对话 |

### 设置与配置

| 命令 | 说明 |
|------|------|
| `/config` | 打开设置 |
| `/model [model]` | 切换模型（←→ 努力度） |
| `/fast [on\|off]` | 切换快速模式 |
| `/vim` | 切换 vim 模式 |
| `/theme` | 更改颜色主题 |
| `/permissions` | 查看/更新权限 |
| `/effort [level]` | 设置努力度（low/med/high） |
| `/color [color]` | 设置提示栏颜色 |

### 项目与记忆

| 命令 | 说明 |
|------|------|
| `/init` | 创建 CLAUDE.md |
| `/memory` | 编辑 CLAUDE.md 文件 |

### 扩展功能

| 命令 | 说明 |
|------|------|
| `/mcp` | 管理 MCP 服务器 |
| `/hooks` | 管理钩子 |
| `/skills` | 列出可用技能 |
| `/agents` | 管理代理 |
| `/chrome` | Chrome 集成 |
| `/reload-plugins` | 热重载插件 |

### 特殊模式

| 命令 | 说明 |
|------|------|
| `/btw <question>` | 附带提问（无上下文） |
| `/plan [desc]` | 计划模式（+ 自动启动） |
| `/loop [interval]` | 调度周期性任务 |
| `/voice` | 按键说话语音（20 种语言） |

### 诊断与工具

| 命令 | 说明 |
|------|------|
| `/doctor` | 诊断安装问题 |
| `/rc` | 启用远程控制 |
| `/pr-comments [PR]` | 获取 GitHub PR 评论 |
| `/stats` | 使用连续记录和偏好 |
| `/insights` | 分析会话报告 |
| `/desktop` | 在桌面应用中继续 |
| `/remote-control` | 桥接终端到 claude.ai/code |

### 高级功能

| 命令 | 说明 |
|------|------|
| `/simplify` | 代码审查（3 个并行代理） |
| `/batch` | 大规模并行修改（5-30 worktrees） |
| `/debug [desc]` | 从调试日志排查问题 |
| `/claude-api` | 加载 API + SDK 参考 |

## CLAUDE.md 配置

### 文件位置

```
./CLAUDE.md                 # 项目（团队共享）
~/.claude/CLAUDE.md         # 个人（所有项目）
/etc/claude-code/           # 管理（组织级）
.claude/rules/*.md          # 项目规则
~/.claude/rules/*.md        # 用户规则
```

### 记忆目录

```
~/.claude/projects/<proj>/memory/
MEMORY.md + 主题文件，自动加载
```

## 权限模式

```
Shift+Tab: Normal → Auto → Plan
```

| 模式 | 说明 |
|------|------|
| `--permission-mode plan` | 以计划模式启动 |
| `default` | 默认权限 |
| `acceptEdits` | 自动接受编辑 |
| `dontAsk` | 不询问 |
| `plan` | 计划模式 |

## 思考模式

| 操作 | 说明 |
|------|------|
| `Alt+T` | 切换思考开/关 |
| `"ultrathink"` | 当前轮次最大努力度 |
| `Ctrl+O` | 查看思考（详细模式） |
| `/effort ○ low · ◐ med · ● high` | 设置努力度 |

## Git Worktree

```bash
--worktree name          # 每个功能独立分支
/batch                   # 自动创建 worktrees
```

- `isolation: worktree` - 代理在独立 worktree 中运行
- `sparsePaths` - 仅检出所需目录

## 语音功能

```bash
/voice          # 启用按键说话
```

- `Space (hold)` - 录音，释放发送
- 支持 20 种语言：EN, ES, FR, DE, CZ, PL…

## 上下文管理

| 命令 | 说明 |
|------|------|
| `/context` | 用量 + 优化建议 |
| `/compact [focus]` | 带焦点压缩 |
| `Auto-compact` | 约 95% 容量时触发 |
| `1M context` | Opus 4.6 (Max/Team/Ent) |

> CLAUDE.md 压缩后保留！

## CLI 启动选项

```bash
claude                      # 交互式
claude "q"                  # 带提示
claude -p "q"               # 无头模式
claude -c                   # 继续上次对话
claude -r "n"               # 按名称恢复
claude update               # 更新
```

### 常用参数

| 参数 | 说明 |
|------|------|
| `--model` | 设置模型 |
| `-w` | Git worktree |
| `-n, --name` | 会话名称 |
| `--add-dir` | 添加目录 |
| `--agent` | 使用代理 |
| `--allowedTools` | 预批准工具 |
| `--output-format json/stream` | 输出格式 |
| `--json-schema` | 结构化输出 |
| `--max-turns` | 限制轮次 |
| `--max-budget-usd` | 费用上限 |
| `--console` | 通过 Anthropic Console 认证 |
| `--verbose` | 详细模式 |
| `--bare` | 最小化无头（无 hooks/LSP） |
| `--channels` | 权限中继 / MCP 推送 |
| `--remote` | Web 会话 |
| `--chrome` | Chrome 集成 |

## 配置文件

```
~/.claude/settings.json         # 用户设置
.claude/settings.json           # 项目（共享）
.claude/settings.local.json     # 仅本地
~/.claude.json                  # OAuth, MCP, 状态
.mcp.json                       # 项目 MCP 服务器
```

### 配置项

- `modelOverrides` - 模型选择器映射自定义 ID
- `autoMemoryDirectory` - 自定义记忆目录
- `worktree.sparsePaths` - 稀疏检出目录

## 环境变量

| 变量 | 说明 |
|------|------|
| `ANTHROPIC_API_KEY` | API 密钥 |
| `ANTHROPIC_MODEL` | 默认模型 |
| `CLAUDE_CODE_EFFORT_LEVEL` | low/med/high |
| `MAX_THINKING_TOKENS` | 0=关闭 |
| `ANTHROPIC_CUSTOM_MODEL_OPTION` | 自定义 /model 条目 |
| `CLAUDE_CODE_PLUGIN_SEED_DIR` | 多个插件种子目录 |

## 代理配置

### 代理模式

| 模式 | 说明 |
|------|------|
| `Explore` | 快速只读 (Haiku) |
| `Plan` | 计划模式研究 |
| `General` | 全工具，复杂任务 |
| `Bash` | 终端独立上下文 |

### 代理选项

```yaml
permissionMode: default/acceptEdits/dontAsk/plan
isolation: worktree      # 在 git worktree 中运行
memory: user|project     # 持久化记忆
background: true         # 后台任务
maxTurns: N              # 限制代理轮次
```

## 技能系统

### 技能目录

```
.claude/skills/<name>/      # 项目技能
~/.claude/skills/<name>/    # 个人技能
```

### 技能配置

```yaml
description: "自动调用触发器"
allowed-tools: []          # 跳过权限提示
model: "模型名称"           # 覆盖技能模型
effort: "low/med/high"     # 覆盖努力度
context: fork              # 在子代理中运行
```

### 变量

- `$ARGUMENTS` - 用户输入占位符
- `${CLAUDE_SKILL_DIR}` - 技能自身目录
- ``!`cmd` `` - 动态上下文注入

## 其他功能

- `--bare` 标志 — 最小化无头模式（无 hooks/LSP/插件）
- `--channels` — 权限中继 & MCP 推送消息（预览）
- `effort` 前置元数据用于技能和斜杠命令
- `/fork` 重命名为 `/branch`（别名保留）
- `SendMessage` 自动恢复已停止的代理
- `Elicitation` 服务器在任务中请求输入

---

*最后更新：2026-03-25*
