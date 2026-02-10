# ワークフロー: Plan Modeと自律修正

> Tips #2, #5 の詳細

## 1. Plan Mode

### 概要

複雑なタスクは実装前に設計を固める。Plan Modeを使うことで、Claudeが実装を1-shotで完了できる。

### 有効化

```
shift+Tab でモード切り替え
または
> /plan
```

```
┌─────────────────────────────────────────────────────────┐
│ Claude Code v2.1.29                                     │
│ Opus 4.5 · Claude Enterprise                           │
│                                                         │
│ > Try "refactor cli.tsx"                               │
│                                                         │
│ ■ plan mode on (shift+Tab to cycle)                    │
└─────────────────────────────────────────────────────────┘
```

### Plan Modeでの作業フロー

```
1. Plan Mode ON
   ↓
2. タスクを説明
   ↓
3. Claudeが計画を提案
   ↓
4. 計画をレビュー・修正
   ↓
5. 計画確定
   ↓
6. Plan Mode OFF → 実装開始
   ↓
7. 計画通りに1-shot実装
```

### Second Claudeパターン

```bash
# Terminal 1: 計画作成
> /plan
> Design a caching layer for our API

# Terminal 2: 別のClaudeでレビュー
> Review this plan as a staff engineer: [計画をペースト]
> What are the potential issues? What would you change?
```

### いつPlan Modeに戻るか

- 実装中に想定外の問題が発生
- 要件の理解が不十分だと気づいた
- アーキテクチャの再検討が必要

---

## 2. 自律バグ修正

### 基本原則

**「What」を指示し、「How」は任せる**

```bash
# Good: 何を直すか指示
> fix this bug https://slack.com/archives/...

# Bad: どう直すか指示
> open src/auth.ts, find the login function,
> change line 45 to check for null...
```

### Slack連携

#### セットアップ

```jsonc
// claude_desktop_config.json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["@anthropic/slack-mcp-server"],
      "env": {
        "SLACK_TOKEN": "xoxb-..."
      }
    }
  }
}
```

#### 使用例

```bash
# SlackスレッドURLを渡す
> fix this https://slack.com/archives/C07VBSH.../p1234567890

# Claudeの動作:
# 1. Slack MCPでスレッド内容を取得
# 2. バグの内容を理解
# 3. 関連コードを探索
# 4. 修正を実装
# 5. テスト実行
# 6. PR作成
```

### CI/CD連携

```bash
# CIの失敗を修正
> Go fix the failing CI tests

# Dockerログから調査
> investigate this error from docker logs: [URL or paste]

# Sentryエラーを修正
> fix the top error in Sentry this week
```

### 自動化の範囲

```
┌─────────────────────────────────────────────────────────┐
│         手動              │         自動                │
├─────────────────────────────────────────────────────────┤
│ URL/問題の特定            │ コンテキスト取得           │
│ "fix" コマンド入力        │ 原因調査                   │
│                           │ 修正実装                   │
│                           │ テスト実行                 │
│                           │ PR作成                     │
│ PRレビュー・承認          │                            │
│ マージ                    │                            │
└─────────────────────────────────────────────────────────┘
```

---

## 3. ワークフロー統合

### 推奨フロー

```
バグ報告 (Slack/GitHub/Sentry)
    ↓
URLをClaudeに渡す + "fix"
    ↓
[自動] 調査・修正・PR作成
    ↓
PRレビュー (人間 or Second Claude)
    ↓
マージ・デプロイ
```

### 複雑なバグの場合

```
バグ報告
    ↓
Plan Mode ON
    ↓
調査計画を立てる
    ↓
計画に沿って調査
    ↓
修正計画を立てる
    ↓
Plan Mode OFF
    ↓
実装
```

---

## 関連

- [Claude Code Plan Mode](https://docs.anthropic.com/claude-code/plan-mode)
- [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)
