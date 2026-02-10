# ツーリング: 環境設定とデータ分析

> Tips #7, #9 の詳細

## 1. ターミナル環境

### Ghostty（チーム推奨）

Claude Codeチームが愛用するターミナルエミュレータ。

**特徴:**
- 同期レンダリング（ちらつきなし）
- 24-bit color サポート
- 適切なUnicodeサポート
- 高速

**インストール:**
```bash
# macOS
brew install ghostty

# Linux
# https://ghostty.org/download
```

**設定例 (~/.config/ghostty/config):**
```ini
font-family = "JetBrains Mono"
font-size = 14
theme = "catppuccin-mocha"
window-padding-x = 10
window-padding-y = 10
```

### 他の選択肢

| ターミナル | 特徴 |
|-----------|------|
| Ghostty | Claude Code チーム推奨 |
| iTerm2 | macOS定番、高機能 |
| Warp | AI統合、モダンUI |
| Alacritty | GPU加速、高速 |

---

## 2. /statusline カスタマイズ

### 概要

Claude Codeのステータスバーをカスタマイズして、重要な情報を常に表示。

```bash
> /statusline
```

### 表示できる情報

- **コンテキスト使用量** - 残りトークン数
- **現在のgit branch** - 作業中のブランチ
- **モード** - Normal / Plan / Auto
- **セッション時間** - 経過時間

### 設定例

```jsonc
// .claude/settings.json
{
  "statusline": {
    "left": ["mode", "branch"],
    "right": ["context-usage", "session-time"]
  }
}
```

**表示イメージ:**
```
┌─────────────────────────────────────────────────────────┐
│ ■ normal │ feature/auth        Context: 45% │ 1h 23m  │
└─────────────────────────────────────────────────────────┘
```

### 複数セッション管理

複数のworktreeでClaudeを実行する場合、statuslineでどのセッションがどのブランチか一目でわかる。

---

## 3. データ分析（BigQuery連携）

### 概要

BigQuery skillをコードベースにコミットし、チーム全員がClaude経由でanalytics実行。

### スキル設定

```markdown
# .claude/skills/bigquery.md

# BigQuery Analytics

## 認証
GCP認証が必要。`gcloud auth login` を事前に実行。

## 使用可能なデータセット
- `project.analytics.events` - ユーザーイベント
- `project.analytics.errors` - エラーログ
- `project.analytics.performance` - パフォーマンスメトリクス

## クエリ例

### 日次アクティブユーザー
\`\`\`sql
SELECT DATE(timestamp) as date, COUNT(DISTINCT user_id) as dau
FROM \`project.analytics.events\`
WHERE timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY date
ORDER BY date
\`\`\`

## 実行方法
bq query --use_legacy_sql=false '[クエリ]'
```

### 使用例

```bash
# 自然言語で質問
> What were our error rates last week?

# Claudeの動作:
# 1. BigQuery skillを参照
# 2. 適切なSQLを生成
# 3. bq CLI で実行
# 4. 結果を解釈して報告

# 出力例:
Last week's error rates:
- Monday: 0.12%
- Tuesday: 0.15%
- Wednesday: 0.45% (spike due to deployment at 14:00)
- Thursday: 0.11%
- Friday: 0.10%

The Wednesday spike correlates with deployment #1234.
```

### 他のデータソース

同様のパターンで他のデータソースも統合可能:

```bash
# Snowflake
> Query our Snowflake warehouse for monthly revenue

# PostgreSQL
> How many users signed up this month?

# Elasticsearch
> Show me the top 10 error messages today
```

---

## 4. MCP統合

### 利用可能なMCP

| MCP | 用途 |
|-----|------|
| Slack | メッセージ読み取り、投稿 |
| GitHub | Issue/PR操作 |
| Sentry | エラートラッキング |
| Linear | タスク管理 |
| Notion | ドキュメント |

### 設定例

```jsonc
// claude_desktop_config.json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["@anthropic/slack-mcp-server"]
    },
    "github": {
      "command": "npx",
      "args": ["@anthropic/github-mcp-server"]
    },
    "sentry": {
      "command": "npx",
      "args": ["sentry-mcp-server"]
    }
  }
}
```

### ワークフロー例

```bash
# Sentryのエラーを見て修正
> Fix the top error in Sentry this week

# LinearのタスクをPRにリンク
> Create a PR for LINEAR-123

# Notionのドキュメントを参照して実装
> Implement the API according to the spec in Notion
```

---

## 5. 開発環境テンプレート

### 推奨セットアップ

```bash
# ターミナル
brew install ghostty

# CLI tools
brew install gh bq jq

# MCPサーバー
npm install -g @anthropic/slack-mcp-server
npm install -g @anthropic/github-mcp-server

# Claude Code
npm install -g @anthropic/claude-code
```

### ディレクトリ構成

```
~/.claude/
├── CLAUDE.md              # グローバル設定
├── settings.json          # ステータスライン等
├── skills/                # 共通スキル
│   ├── bigquery.md
│   └── techdebt.md
└── worktrees/             # 並列作業用

project/
├── .claude/
│   ├── skills/            # プロジェクト固有スキル
│   └── hooks/             # Permission hooks
├── CLAUDE.md              # プロジェクト設定
└── ...
```

---

## 関連

- [Ghostty](https://ghostty.org/)
- [BigQuery CLI](https://cloud.google.com/bigquery/docs/bq-command-line-tool)
- [MCP Servers](https://github.com/anthropics/mcp-servers)
