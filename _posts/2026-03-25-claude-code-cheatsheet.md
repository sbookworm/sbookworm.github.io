---
layout: page
title: Claude Code 速查表
date: 2026-03-25 08:00:00
categories: [工具]
tags: [Claude Code, 速查表, AI工具]
---

<style>
.cheatsheet {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 14px;
  line-height: 1.6;
}
.cheatsheet .section {
  margin-bottom: 24px;
}
.cheatsheet .section-header {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  padding-bottom: 4px;
  border-bottom: 1px solid #e5e7eb;
}
.cheatsheet .sub-header {
  font-size: 12px;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 12px 0 6px 0;
}
.cheatsheet .row {
  display: flex;
  gap: 12px;
  padding: 2px 0;
}
.cheatsheet .key {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 13px;
  color: #0369a1;
  min-width: 160px;
  flex-shrink: 0;
}
.cheatsheet .desc {
  color: #374151;
}
.cheatsheet .keycap {
  display: inline-block;
  background: #f3f4f6;
  border: 1px solid #d1d5db;
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 12px;
  margin-right: 2px;
}
.cheatsheet .badge-new {
  display: inline-block;
  background: #dbeafe;
  color: #1d4ed8;
  font-size: 10px;
  font-weight: 600;
  padding: 1px 4px;
  border-radius: 3px;
  margin-left: 4px;
}
.cheatsheet-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
}
@media (max-width: 768px) {
  .cheatsheet-grid {
    grid-template-columns: 1fr;
  }
}
.cheatsheet-source {
  margin-top: 32px;
  padding-top: 16px;
  border-top: 1px solid #e5e7eb;
  font-size: 13px;
  color: #6b7280;
}
</style>

<div class="cheatsheet">
<div class="cheatsheet-grid">

<!-- 键盘快捷键 -->
<section class="section">
  <div class="section-header">⌨️ 键盘快捷键</div>
  <div class="sub-header">常规控制</div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">C</span></span> <span class="desc">取消输入/生成</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">D</span></span> <span class="desc">退出会话</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">L</span></span> <span class="desc">清屏</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">O</span></span> <span class="desc">切换详细输出</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">R</span></span> <span class="desc">反向搜索历史</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">G</span></span> <span class="desc">在编辑器中打开提示</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">B</span></span> <span class="desc">后台运行任务</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">T</span></span> <span class="desc">切换任务列表</span></div>
  <div class="row"><span class="key"><span class="keycap">Alt</span><span class="keycap">V</span></span> <span class="desc">粘贴图片</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">F</span></span> <span class="desc">终止后台代理（按两次）</span></div>
  <div class="row"><span class="key"><span class="keycap">Esc</span><span class="keycap">Esc</span></span> <span class="desc">回退 / 撤销</span></div>
  
  <div class="sub-header">模式切换</div>
  <div class="row"><span class="key"><span class="keycap">Shift</span><span class="keycap">Tab</span></span> <span class="desc">循环切换权限模式</span></div>
  <div class="row"><span class="key"><span class="keycap">Alt</span><span class="keycap">P</span></span> <span class="desc">切换模型</span></div>
  <div class="row"><span class="key"><span class="keycap">Alt</span><span class="keycap">T</span></span> <span class="desc">切换思考模式</span></div>
  
  <div class="sub-header">输入</div>
  <div class="row"><span class="key"><span class="keycap">\</span><span class="keycap">Enter</span></span> <span class="desc">换行（快捷）</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">J</span></span> <span class="desc">换行（控制序列）</span></div>
  
  <div class="sub-header">前缀</div>
  <div class="row"><span class="key">/</span> <span class="desc">斜杠命令</span></div>
  <div class="row"><span class="key">!</span> <span class="desc">直接执行 bash</span></div>
  <div class="row"><span class="key">@</span> <span class="desc">文件引用 + 自动补全</span></div>
  
  <div class="sub-header">会话选择器</div>
  <div class="row"><span class="key">↑↓</span> <span class="desc">导航</span></div>
  <div class="row"><span class="key">←→</span> <span class="desc">展开/折叠</span></div>
  <div class="row"><span class="key">P</span> <span class="desc">预览</span></div>
  <div class="row"><span class="key">R</span> <span class="desc">重命名</span></div>
  <div class="row"><span class="key">/</span> <span class="desc">搜索</span></div>
  <div class="row"><span class="key">A</span> <span class="desc">所有项目</span></div>
  <div class="row"><span class="key">B</span> <span class="desc">当前分支</span></div>
</section>

<!-- MCP 服务器 -->
<section class="section">
  <div class="section-header">🔌 MCP 服务器</div>
  <div class="sub-header">添加服务器</div>
  <div class="row"><span class="key">--transport http</span> <span class="desc">远程 HTTP（推荐）</span></div>
  <div class="row"><span class="key">--transport stdio</span> <span class="desc">本地进程</span></div>
  <div class="row"><span class="key">--transport sse</span> <span class="desc">远程 SSE</span></div>
  <div class="sub-header">作用域</div>
  <div class="row"><span class="key">Local</span> <span class="desc">~/.claude.json（每个项目）</span></div>
  <div class="row"><span class="key">Project</span> <span class="desc">.mcp.json（共享/VCS）</span></div>
  <div class="row"><span class="key">User</span> <span class="desc">~/.claude.json（全局）</span></div>
  <div class="sub-header">管理</div>
  <div class="row"><span class="key">/mcp</span> <span class="desc">交互式界面</span></div>
  <div class="row"><span class="key">claude mcp list</span> <span class="desc">列出所有服务器</span></div>
  <div class="row"><span class="key">claude mcp serve</span> <span class="desc">CC 作为 MCP 服务器</span></div>
  <div class="row"><span class="key">Elicitation</span> <span class="desc">服务器在任务中请求输入<span class="badge-new">NEW</span></span></div>
</section>

<!-- 斜杠命令 -->
<section class="section">
  <div class="section-header">⚡ 斜杠命令</div>
  <div class="sub-header">会话</div>
  <div class="row"><span class="key">/clear</span> <span class="desc">清除对话</span></div>
  <div class="row"><span class="key">/compact [focus]</span> <span class="desc">压缩上下文</span></div>
  <div class="row"><span class="key">/resume</span> <span class="desc">恢复/切换会话</span></div>
  <div class="row"><span class="key">/rename [name]</span> <span class="desc">命名当前会话</span></div>
  <div class="row"><span class="key">/branch [name]</span> <span class="desc">分支对话（/fork 别名）</span></div>
  <div class="row"><span class="key">/cost</span> <span class="desc">Token 用量统计</span></div>
  <div class="row"><span class="key">/context</span> <span class="desc">可视化上下文（网格）</span></div>
  <div class="row"><span class="key">/diff</span> <span class="desc">交互式差异查看器</span></div>
  <div class="row"><span class="key">/copy</span> <span class="desc">复制上次回复</span></div>
  <div class="row"><span class="key">/export</span> <span class="desc">导出对话</span></div>
  
  <div class="sub-header">配置</div>
  <div class="row"><span class="key">/config</span> <span class="desc">打开设置</span></div>
  <div class="row"><span class="key">/model [model]</span> <span class="desc">切换模型（←→ 努力度）</span></div>
  <div class="row"><span class="key">/fast [on|off]</span> <span class="desc">切换快速模式</span></div>
  <div class="row"><span class="key">/vim</span> <span class="desc">切换 vim 模式</span></div>
  <div class="row"><span class="key">/theme</span> <span class="desc">更改颜色主题</span></div>
  <div class="row"><span class="key">/permissions</span> <span class="desc">查看/更新权限</span></div>
  <div class="row"><span class="key">/effort [level]</span> <span class="desc">设置努力度（low/med/high）<span class="badge-new">NEW</span></span></div>
  <div class="row"><span class="key">/color [color]</span> <span class="desc">设置提示栏颜色</span></div>
  
  <div class="sub-header">工具</div>
  <div class="row"><span class="key">/init</span> <span class="desc">创建 CLAUDE.md</span></div>
  <div class="row"><span class="key">/memory</span> <span class="desc">编辑 CLAUDE.md 文件</span></div>
  <div class="row"><span class="key">/mcp</span> <span class="desc">管理 MCP 服务器</span></div>
  <div class="row"><span class="key">/hooks</span> <span class="desc">管理钩子</span></div>
  <div class="row"><span class="key">/skills</span> <span class="desc">列出可用技能</span></div>
  <div class="row"><span class="key">/agents</span> <span class="desc">管理代理</span></div>
  <div class="row"><span class="key">/chrome</span> <span class="desc">Chrome 集成</span></div>
  <div class="row"><span class="key">/reload-plugins</span> <span class="desc">热重载插件</span></div>
  
  <div class="sub-header">特殊</div>
  <div class="row"><span class="key">/btw &lt;question&gt;</span> <span class="desc">附带提问（无上下文）</span></div>
  <div class="row"><span class="key">/plan [desc]</span> <span class="desc">计划模式（+ 自动启动）</span></div>
  <div class="row"><span class="key">/loop [interval]</span> <span class="desc">调度周期性任务</span></div>
  <div class="row"><span class="key">/voice</span> <span class="desc">按键说话语音（20 种语言）</span></div>
  <div class="row"><span class="key">/doctor</span> <span class="desc">诊断安装问题</span></div>
  <div class="row"><span class="key">/rc</span> <span class="desc">启用远程控制</span></div>
  <div class="row"><span class="key">/pr-comments [PR]</span> <span class="desc">获取 GitHub PR 评论</span></div>
  <div class="row"><span class="key">/stats</span> <span class="desc">使用连续记录和偏好</span></div>
  <div class="row"><span class="key">/insights</span> <span class="desc">分析会话报告</span></div>
  <div class="row"><span class="key">/desktop</span> <span class="desc">在桌面应用中继续</span></div>
  <div class="row"><span class="key">/remote-control</span> <span class="desc">桥接终端到 claude.ai/code<span class="badge-new">NEW</span></span></div>
  <div class="row"><span class="key">/stickers</span> <span class="desc">订购贴纸！🎉</span></div>
</section>

<!-- 记忆与文件 -->
<section class="section">
  <div class="section-header">📁 记忆与文件</div>
  <div class="sub-header">CLAUDE.md 位置</div>
  <div class="row"><span class="key">./CLAUDE.md</span> <span class="desc">项目（团队共享）</span></div>
  <div class="row"><span class="key">~/.claude/CLAUDE.md</span> <span class="desc">个人（所有项目）</span></div>
  <div class="row"><span class="key">/etc/claude-code/</span> <span class="desc">管理（组织级）</span></div>
  <div class="sub-header">规则与导入</div>
  <div class="row"><span class="key">.claude/rules/*.md</span> <span class="desc">项目规则</span></div>
  <div class="row"><span class="key">~/.claude/rules/*.md</span> <span class="desc">用户规则</span></div>
  <div class="row"><span class="key">paths: frontmatter</span> <span class="desc">路径特定规则</span></div>
  <div class="row"><span class="key">@path/to/file</span> <span class="desc">在 CLAUDE.md 中导入</span></div>
  <div class="sub-header">自动记忆</div>
  <div class="row"><span class="key">~/.claude/projects/&lt;proj&gt;/memory/</span></div>
  <div class="row"><span class="desc">MEMORY.md + 主题文件，自动加载</span></div>
</section>

<!-- 工作流与技巧 -->
<section class="section">
  <div class="section-header">🧠 工作流与技巧</div>
  <div class="sub-header">计划模式</div>
  <div class="row"><span class="key"><span class="keycap">Shift</span><span class="keycap">Tab</span></span> <span class="desc">Normal → Auto → Plan</span></div>
  <div class="row"><span class="key">--permission-mode plan</span> <span class="desc">以计划模式启动</span></div>
  <div class="sub-header">思考与努力度</div>
  <div class="row"><span class="key"><span class="keycap">Alt</span><span class="keycap">T</span></span> <span class="desc">切换思考开/关</span></div>
  <div class="row"><span class="key">"ultrathink"</span> <span class="desc">当前轮次最大努力度</span></div>
  <div class="row"><span class="key"><span class="keycap">Ctrl</span><span class="keycap">O</span></span> <span class="desc">查看思考（详细模式）</span></div>
  <div class="row"><span class="key">/effort</span> <span class="desc">○ low · ◐ med · ● high<span class="badge-new">NEW</span></span></div>
  <div class="sub-header">Git Worktrees</div>
  <div class="row"><span class="key">--worktree name</span> <span class="desc">每个功能独立分支</span></div>
  <div class="row"><span class="key">isolation: worktree</span> <span class="desc">代理在独立 worktree 中</span></div>
  <div class="row"><span class="key">sparsePaths</span> <span class="desc">仅检出所需目录<span class="badge-new">NEW</span></span></div>
  <div class="row"><span class="key">/batch</span> <span class="desc">自动创建 worktrees</span></div>
  <div class="sub-header">语音模式</div>
  <div class="row"><span class="key">/voice</span> <span class="desc">启用按键说话</span></div>
  <div class="row"><span class="key"><span class="keycap">Space</span> (hold)</span> <span class="desc">录音，释放发送</span></div>
  <div class="row"><span class="key">20 种语言</span> <span class="desc">EN, ES, FR, DE, CZ, PL…</span></div>
  <div class="sub-header">上下文管理</div>
  <div class="row"><span class="key">/context</span> <span class="desc">用量 + 优化建议</span></div>
  <div class="row"><span class="key">/compact [focus]</span> <span class="desc">带焦点压缩</span></div>
  <div class="row"><span class="key">Auto-compact</span> <span class="desc">约 95% 容量时触发</span></div>
  <div class="row"><span class="key">1M context</span> <span class="desc">Opus 4.6 (Max/Team/Ent)</span></div>
  <div class="row"><span class="key">CLAUDE.md</span> <span class="desc">压缩后保留！</span></div>
  <div class="sub-header">会话高级操作</div>
  <div class="row"><span class="key">claude -c</span> <span class="desc">继续上次对话</span></div>
  <div class="row"><span class="key">claude -r "name"</span> <span class="desc">按名称恢复</span></div>
  <div class="row"><span class="key">/btw question</span> <span class="desc">附带提问，无上下文开销</span></div>
  <div class="sub-header">SDK / 无头模式</div>
  <div class="row"><span class="key">claude -p "query"</span> <span class="desc">非交互式</span></div>
  <div class="row"><span class="key">--output-format json</span> <span class="desc">结构化输出</span></div>
  <div class="row"><span class="key">--max-budget-usd 5</span> <span class="desc">费用上限</span></div>
  <div class="row"><span class="key">cat file | claude -p</span> <span class="desc">管道输入</span></div>
  <div class="sub-header">调度与远程</div>
  <div class="row"><span class="key">/loop 5m msg</span> <span class="desc">周期性任务</span></div>
  <div class="row"><span class="key">/rc</span> <span class="desc">远程控制</span></div>
  <div class="row"><span class="key">--remote</span> <span class="desc">claude.ai 上的 Web 会话</span></div>
</section>

<!-- 配置与环境 -->
<section class="section">
  <div class="section-header">⚙️ 配置与环境</div>
  <div class="sub-header">配置文件</div>
  <div class="row"><span class="key">~/.claude/settings.json</span> <span class="desc">用户设置</span></div>
  <div class="row"><span class="key">.claude/settings.json</span> <span class="desc">项目（共享）</span></div>
  <div class="row"><span class="key">.claude/settings.local.json</span> <span class="desc">仅本地</span></div>
  <div class="row"><span class="key">~/.claude.json</span> <span class="desc">OAuth, MCP, 状态</span></div>
  <div class="row"><span class="key">.mcp.json</span> <span class="desc">项目 MCP 服务器</span></div>
  <div class="sub-header">重要设置</div>
  <div class="row"><span class="key">modelOverrides</span> <span class="desc">模型选择器映射自定义 ID</span></div>
  <div class="row"><span class="key">autoMemoryDirectory</span> <span class="desc">自定义记忆目录</span></div>
  <div class="row"><span class="key">worktree.sparsePaths</span> <span class="desc">稀疏检出目录<span class="badge-new">NEW</span></span></div>
  <div class="sub-header">重要环境变量</div>
  <div class="row"><span class="key">ANTHROPIC_API_KEY</span></div>
  <div class="row"><span class="key">ANTHROPIC_MODEL</span></div>
  <div class="row"><span class="key">CLAUDE_CODE_EFFORT_LEVEL</span> <span class="desc">low/med/high</span></div>
  <div class="row"><span class="key">MAX_THINKING_TOKENS</span> <span class="desc">0=关闭</span></div>
  <div class="row"><span class="key">ANTHROPIC_CUSTOM_MODEL_OPTION</span> <span class="desc">自定义 /model 条目</span></div>
  <div class="row"><span class="key">CLAUDE_CODE_PLUGIN_SEED_DIR</span> <span class="desc">多个插件种子目录</span></div>
</section>

<!-- 技能与代理 -->
<section class="section">
  <div class="section-header">🔧 技能与代理</div>
  <div class="sub-header">内置技能</div>
  <div class="row"><span class="key">/simplify</span> <span class="desc">代码审查（3 个并行代理）</span></div>
  <div class="row"><span class="key">/batch</span> <span class="desc">大规模并行修改（5-30 worktrees）</span></div>
  <div class="row"><span class="key">/debug [desc]</span> <span class="desc">从调试日志排查问题</span></div>
  <div class="row"><span class="key">/loop [interval]</span> <span class="desc">周期性调度任务</span></div>
  <div class="row"><span class="key">/claude-api</span> <span class="desc">加载 API + SDK 参考</span></div>
  <div class="sub-header">自定义技能位置</div>
  <div class="row"><span class="key">.claude/skills/&lt;name&gt;/</span> <span class="desc">项目技能</span></div>
  <div class="row"><span class="key">~/.claude/skills/&lt;name&gt;/</span> <span class="desc">个人技能</span></div>
  <div class="sub-header">技能前置元数据</div>
  <div class="row"><span class="key">description</span> <span class="desc">自动调用触发器</span></div>
  <div class="row"><span class="key">allowed-tools</span> <span class="desc">跳过权限提示</span></div>
  <div class="row"><span class="key">model</span> <span class="desc">覆盖技能模型</span></div>
  <div class="row"><span class="key">effort</span> <span class="desc">覆盖努力度<span class="badge-new">NEW</span></span></div>
  <div class="row"><span class="key">context: fork</span> <span class="desc">在子代理中运行</span></div>
  <div class="row"><span class="key">$ARGUMENTS</span> <span class="desc">用户输入占位符</span></div>
  <div class="row"><span class="key">${CLAUDE_SKILL_DIR}</span> <span class="desc">技能自身目录</span></div>
  <div class="row"><span class="key">!`cmd`</span> <span class="desc">动态上下文注入</span></div>
  <div class="sub-header">内置代理</div>
  <div class="row"><span class="key">Explore</span> <span class="desc">快速只读 (Haiku)</span></div>
  <div class="row"><span class="key">Plan</span> <span class="desc">计划模式研究</span></div>
  <div class="row"><span class="key">General</span> <span class="desc">全工具，复杂任务</span></div>
  <div class="row"><span class="key">Bash</span> <span class="desc">终端独立上下文</span></div>
  <div class="sub-header">代理前置元数据</div>
  <div class="row"><span class="key">permissionMode</span> <span class="desc">default/acceptEdits/dontAsk/plan</span></div>
  <div class="row"><span class="key">isolation: worktree</span> <span class="desc">在 git worktree 中运行</span></div>
  <div class="row"><span class="key">memory: user|project</span> <span class="desc">持久化记忆</span></div>
  <div class="row"><span class="key">background: true</span> <span class="desc">后台任务</span></div>
  <div class="row"><span class="key">maxTurns</span> <span class="desc">限制代理轮次</span></div>
  <div class="row"><span class="key">SendMessage</span> <span class="desc">恢复代理（替代 resume）<span class="badge-new">NEW</span></span></div>
</section>

<!-- CLI 与标志 -->
<section class="section">
  <div class="section-header">🖥️ CLI 与标志</div>
  <div class="sub-header">核心命令</div>
  <div class="row"><span class="key">claude</span> <span class="desc">交互式</span></div>
  <div class="row"><span class="key">claude "q"</span> <span class="desc">带提示</span></div>
  <div class="row"><span class="key">claude -p "q"</span> <span class="desc">无头模式</span></div>
  <div class="row"><span class="key">claude -c</span> <span class="desc">继续上次</span></div>
  <div class="row"><span class="key">claude -r "n"</span> <span class="desc">恢复</span></div>
  <div class="row"><span class="key">claude update</span> <span class="desc">更新</span></div>
  <div class="sub-header">重要标志</div>
  <div class="row"><span class="key">--model</span> <span class="desc">设置模型</span></div>
  <div class="row"><span class="key">-w</span> <span class="desc">Git worktree</span></div>
  <div class="row"><span class="key">-n / --name</span> <span class="desc">会话名称</span></div>
  <div class="row"><span class="key">--add-dir</span> <span class="desc">添加目录</span></div>
  <div class="row"><span class="key">--agent</span> <span class="desc">使用代理</span></div>
  <div class="row"><span class="key">--allowedTools</span> <span class="desc">预批准</span></div>
  <div class="row"><span class="key">--output-format</span> <span class="desc">json/stream</span></div>
  <div class="row"><span class="key">--json-schema</span> <span class="desc">结构化</span></div>
  <div class="row"><span class="key">--max-turns</span> <span class="desc">限制轮次</span></div>
  <div class="row"><span class="key">--max-budget-usd</span> <span class="desc">费用上限</span></div>
  <div class="row"><span class="key">--console</span> <span class="desc">通过 Anthropic Console 认证</span></div>
  <div class="row"><span class="key">--verbose</span> <span class="desc">详细模式</span></div>
  <div class="row"><span class="key">--bare</span> <span class="desc">最小化无头（无 hooks/LSP）<span class="badge-new">NEW</span></span></div>
  <div class="row"><span class="key">--channels</span> <span class="desc">权限中继 / MCP 推送<span class="badge-new">NEW</span></span></div>
  <div class="row"><span class="key">--remote</span> <span class="desc">Web 会话</span></div>
  <div class="row"><span class="key">--chrome</span> <span class="desc">Chrome</span></div>
  <div class="sub-header">权限模式</div>
  <div class="row"><span class="key">default</span> <span class="desc">提示确认</span></div>
  <div class="row"><span class="key">acceptEdits</span> <span class="desc">自动接受编辑</span></div>
  <div class="row"><span class="key">plan</span> <span class="desc">只读</span></div>
  <div class="row"><span class="key">dontAsk</span> <span class="desc">未允许则拒绝</span></div>
  <div class="row"><span class="key">bypassPermissions</span> <span class="desc">跳过所有</span></div>
</section>

</div>

<div class="cheatsheet-source">
  <p>📝 <strong>引用出处</strong>：本文内容整理自 <a href="https://banwagong1.com/claude-code.html" target="_blank">banwagong1.com/claude-code.html</a>，感谢原作者的整理工作。</p>
</div>
</div>