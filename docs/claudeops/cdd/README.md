# CDD - Claude Delegated Development

**Cherny Method**

> Origin: Boris Cherny (@bcherny) - Anthropic Claude Code Team
>
> Source: https://x.com/bcherny (2025)

## 概要

CDD (Claude Delegated Development) は、Claude Codeチームが実践する開発手法です。

**核心: 「Don't micromanage how」— 信頼して委任する**

```
従来の開発:     人間が「考えて」「作業する」
CDD:           人間が「指示して」「確認する」
```

## 4つの原則

| 原則 | 内容 |
|------|------|
| **委任** | URLを渡して "fix" だけ言う |
| **並列** | 複数セッション/サブエージェントで分散 |
| **蓄積** | CLAUDE.md, Skills で知識を資産化 |
| **監督** | 人間はレビュアーに徹する |

## 10のプラクティス

## クイックリファレンス

| # | Tip | キーワード |
|---|-----|-----------|
| 1 | [並列作業](#1-並列作業do-more-in-parallel) | git worktree, 複数セッション |
| 2 | [Plan Mode](#2-plan-modeで開始) | 設計先行, レビュー |
| 3 | [CLAUDE.md投資](#3-claudemdに投資) | 学習蓄積, ルール自己記述 |
| 4 | [スキル作成](#4-スキルを作成してgitにコミット) | 再利用, /techdebt |
| 5 | [自律バグ修正](#5-自律バグ修正) | Slack MCP, "fix" |
| 6 | [プロンプト技法](#6-プロンプト技法) | レビュアー, 証明 |
| 7 | [環境設定](#7-環境設定) | Ghostty, /statusline |
| 8 | [サブエージェント](#8-サブエージェント活用) | 並列探索, hook |
| 9 | [データ分析](#9-データ分析) | BigQuery, bq CLI |
| 10 | [学習モード](#10-claudeで学習) | Explanatory, HTML |

---

## 1. 並列作業（Do more in parallel）

**最大の生産性向上ポイント**

```bash
# 3-5個のgit worktreeを作成し、各々でClaudeセッションを実行
$ git worktree add .claude/worktrees/feature-a origin/main
$ cd .claude/worktrees/feature-a && claude
```

- Claudeチームの多くがworktreeを使用
- 複数のgit checkoutでも可
- 1つのタスクを待つ間に別タスクを進行

📄 [詳細: scaling.md](detailed/scaling.md)

---

## 2. Plan Modeで開始

**複雑なタスクは設計から**

```
> Try "refactor cli.tsx"
■ plan mode on (shift+Tab to cycle)
```

- Plan Modeで設計 → 実装を1-shotで完了
- 「Second Claudeにstaff engineerとしてレビューさせる」パターン
- 問題発生時はPlan Modeに戻る

📄 [詳細: workflow.md](detailed/workflow.md)

---

## 3. CLAUDE.mdに投資

**学習する設定ファイル**

```
修正のたびに:
"Update your CLAUDE.md so you don't make that mistake again."
```

- Claudeは自分用のルールを書くのが得意
- 継続的に編集・改善
- Memory files: ~/.claude/CLAUDE.md + プロジェクトのCLAUDE.md

📄 [詳細: knowledge.md](detailed/knowledge.md)

---

## 4. スキルを作成してgitにコミット

**再利用可能な自動化**

- 1日1回以上行う作業 → スキルまたはコマンド化
- `/techdebt` コマンドを作成し、セッション終了時に実行
- プロジェクト間で共有

📄 [詳細: knowledge.md](detailed/knowledge.md)

---

## 5. 自律バグ修正

**「fix」の一言で完結**

```bash
# Slack MCPを有効化して
> fix this https://slack.com/archives/C07.../p1234...

# または
> Go fix the failing CI tests

# Docker logsを渡して
> fix based on these logs [URL]
```

**ポイント: "How"をマイクロマネジメントしない**

📄 [詳細: workflow.md](detailed/workflow.md)

---

## 6. プロンプト技法

**Claudeを協働者として使う**

| 目的 | プロンプト例 |
|-----|-------------|
| 厳格レビュー | "Grill me on these changes and don't make a PR until I pass your test" |
| 動作証明 | "Prove to me this works" → mainとfeature branchの差分比較 |
| 品質向上 | 期待以下の結果後に "you can do better, try again" |

📄 [詳細: interaction.md](detailed/interaction.md)

---

## 7. 環境設定

**ターミナル環境の最適化**

- **Ghostty** - チーム推奨ターミナル
  - 同期レンダリング
  - 24-bit color
  - 適切なUnicodeサポート
- **/statusline** - ステータスバーカスタマイズ
  - コンテキスト使用量表示
  - 現在のgit branch表示

📄 [詳細: tooling.md](detailed/tooling.md)

---

## 8. サブエージェント活用

**計算リソースのスケーリング**

```bash
> use 5 subagents to explore the codebase
```

**3つの活用法:**
- a. "use subagents" で計算リソースを投入
- b. 個別タスクをオフロードしてコンテキスト維持
- c. Permission requestをOpus 4.5にhook経由でルーティング → 自動承認

📄 [詳細: scaling.md](detailed/scaling.md)

---

## 9. データ分析

**BigQuery等をClaude経由で**

```bash
> What were our error rates last week?
# → Claude が bq CLI でクエリ実行・分析
```

- BigQuery skillをコードベースにコミット
- チーム全員がClaude経由でanalytics実行
- SQLを手書きしない

📄 [詳細: tooling.md](detailed/tooling.md)

---

## 10. Claudeで学習

**実行者ではなく教師として**

- a. `/config` で "Explanatory" または "Learning" 出力スタイルを有効化
  - 変更の「なぜ」を説明
- b. 馴染みのない概念をHTMLプレゼンテーションで視覚化

📄 [詳細: interaction.md](detailed/interaction.md)

---

## 全体像: 哲学とパターン

```
┌─────────────────────────────────────────────────────────┐
│              Claude Code 活用の4原則                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. 水平スケーリング                                   │
│     - 複数セッション並列実行 (Tips 1, 8)               │
│     - サブエージェントで分散処理                       │
│                                                         │
│  2. 知識への投資                                        │
│     - CLAUDE.mdの継続的改善 (Tip 3)                    │
│     - スキルのgit管理 (Tip 4)                          │
│                                                         │
│  3. 信頼と委任                                          │
│     - Howをマイクロマネジメントしない (Tip 5)          │
│     - 権限を適切に委譲 (Tip 8c)                        │
│                                                         │
│  4. 役割の再定義                                        │
│     - 実行者 → レビュアー (Tip 6)                      │
│     - 作業者 → 学習者 (Tip 10)                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 関連リンク

- [Claude Code Docs](https://docs.anthropic.com/claude-code)
- [Slack MCP Integration](https://github.com/korotovsky/slack-mcp-server)
- [Ghostty Terminal](https://ghostty.org/)

## Credits

- Boris Cherny (@bcherny) - Anthropic
- Bob Sheth (@bobsheth) - セッション自動評価のアイデア
