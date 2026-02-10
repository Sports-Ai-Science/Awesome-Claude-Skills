# スケーリング: 並列作業とサブエージェント

> Tips #1, #8 の詳細

## 1. Git Worktreeによる並列作業

### なぜWorktreeか

```
従来のブランチ切り替え:
  repo/ (main) → checkout feature-a → checkout feature-b → ...
  問題: 同時に1つしか作業できない

Worktree:
  repo/ (main)
  .claude/worktrees/feature-a/
  .claude/worktrees/feature-b/
  → 同時に複数作業可能
```

### セットアップ

```bash
# worktree用ディレクトリ作成
mkdir -p .claude/worktrees

# 新しいworktreeを追加
git worktree add .claude/worktrees/feature-auth origin/main -b feature-auth
git worktree add .claude/worktrees/feature-api origin/main -b feature-api
git worktree add .claude/worktrees/bugfix-login origin/main -b bugfix-login

# 各worktreeでClaudeセッション起動
cd .claude/worktrees/feature-auth && claude
# 別ターミナルで
cd .claude/worktrees/feature-api && claude
```

### 推奨構成

```
project/
├── .claude/
│   └── worktrees/
│       ├── feature-1/    # Claude session 1
│       ├── feature-2/    # Claude session 2
│       └── bugfix-1/     # Claude session 3
├── src/
└── ...
```

### Worktree管理コマンド

```bash
# 一覧表示
git worktree list

# 削除
git worktree remove .claude/worktrees/feature-auth

# 不要なworktree情報をクリーンアップ
git worktree prune
```

---

## 2. サブエージェント活用

### 基本的な使い方

```bash
# コードベース探索を並列化
> use 5 subagents to explore the codebase

# 結果:
● Running 5 Explore agents...
  ├── Explore entry points and startup
  ├── Explore React components structure
  ├── Explore tools implementation
  ├── Explore state management
  └── Explore testing infrastructure
```

### ユースケース別

#### a. 計算リソースの投入

```bash
# 大規模リファクタリング
> refactor all API endpoints to use the new auth system, use subagents

# 複数ファイルの同時調査
> find all usages of deprecated function X, use subagents
```

#### b. コンテキスト維持

```bash
# メインエージェントのコンテキストを汚さずに調査
> have a subagent investigate the payment module while I continue here
```

#### c. Permission Hookによる自動承認

```jsonc
// .claude/hooks/permission.json
{
  "handler": "opus-4.5-judge",
  "rules": [
    {
      "pattern": "Edit src/**/*.ts",
      "action": "auto-approve"
    },
    {
      "pattern": "Bash(npm test*)",
      "action": "auto-approve"
    },
    {
      "pattern": "Bash(rm -rf*)",
      "action": "always-deny"
    }
  ]
}
```

---

## 3. 並列作業のベストプラクティス

### Do's

- タスクの依存関係を明確にしてから並列化
- 各worktreeに明確な目的を持たせる
- `/statusline` でコンテキスト使用量を監視

### Don'ts

- 同じファイルを複数worktreeで編集しない
- 依存関係のあるタスクを無理に並列化しない
- worktreeを放置しない（定期的にprune）

---

## 関連

- [Git Worktree公式ドキュメント](https://git-scm.com/docs/git-worktree)
- [Claude Code Subagents](https://docs.anthropic.com/claude-code/subagents)
