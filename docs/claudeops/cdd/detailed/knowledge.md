# 知識管理: CLAUDE.mdとスキル

> Tips #3, #4 の詳細

## 1. CLAUDE.mdへの投資

### 概要

CLAUDE.mdは「消耗品」ではなく「資産」。継続的に改善することで、Claudeの精度が向上する。

### ファイル階層

```
~/.claude/CLAUDE.md          # グローバル設定 (76 tokens程度)
project/CLAUDE.md            # プロジェクト固有 (4k tokens程度)
project/src/CLAUDE.md        # ディレクトリ固有 (オプション)
```

### 更新のトリガー

```bash
# Claudeが間違えたとき
> Update your CLAUDE.md so you don't make that mistake again

# 新しいパターンを学んだとき
> Add this pattern to CLAUDE.md for future reference

# プロジェクト固有のルールができたとき
> Document this convention in CLAUDE.md
```

### CLAUDE.mdの構成例

```markdown
# Project Guidelines

## Architecture
- Use repository pattern for data access
- All API endpoints go through src/api/

## Conventions
- Use camelCase for variables
- Prefix interfaces with I (IUser, IProduct)
- Tests must be colocated with source files

## Common Mistakes (学習済み)
- Don't import from @internal packages
- Always check for null before accessing user.profile
- Use dayjs instead of moment (moment is deprecated)

## Commands
- Build: npm run build
- Test: npm test
- Lint: npm run lint
```

### 自己記述の活用

Claudeは自分用のルールを書くのが得意。

```bash
> You just made a mistake with X. Write a rule for yourself
> in CLAUDE.md to prevent this in the future.

# Claudeが自分でルールを追加:
## Common Mistakes
- When modifying auth.ts, always update the corresponding test file
```

---

## 2. スキルの作成とgit管理

### スキルとは

繰り返し行う操作をカプセル化したもの。

### 作成基準

**1日1回以上行う作業 → スキル化**

例:
- テスト実行 + カバレッジ確認
- リント + フォーマット
- 技術的負債の検出
- デプロイ前チェック

### スキルの配置

```
project/
├── .claude/
│   └── skills/
│       ├── techdebt.md
│       ├── deploy-check.md
│       └── coverage-report.md
└── ...
```

### スキル例: /techdebt

```markdown
# /techdebt

セッション終了時に技術的負債を検出・報告する

## 実行内容

1. 重複コードの検出
   - jscpd または類似ツールで検出

2. TODO/FIXME コメントの一覧
   - grep で収集
   - 優先度付け

3. 未使用コード/依存関係
   - depcheck で検出

4. テストカバレッジの低いファイル
   - カバレッジレポートから抽出

## 出力形式

| カテゴリ | ファイル | 詳細 | 優先度 |
|---------|---------|------|--------|
| 重複 | src/utils.ts | 3箇所で同一ロジック | High |
| TODO | src/api.ts:45 | "Refactor this" | Medium |
```

### スキル例: /deploy-check

```markdown
# /deploy-check

デプロイ前の最終チェック

## チェックリスト

1. [ ] 全テストがパス
2. [ ] リントエラーなし
3. [ ] 型エラーなし
4. [ ] 未コミットの変更なし
5. [ ] mainブランチとの差分確認
6. [ ] マイグレーションの確認
7. [ ] 環境変数の確認

## 実行コマンド

\`\`\`bash
npm test && npm run lint && npm run typecheck
git status
git diff main...HEAD --stat
\`\`\`
```

### プロジェクト間での共有

```bash
# 共通スキルリポジトリを作成
git clone https://github.com/org/claude-skills ~/.claude/shared-skills

# プロジェクトでシンボリックリンク
ln -s ~/.claude/shared-skills/techdebt.md .claude/skills/techdebt.md
```

---

## 3. 知識の蓄積サイクル

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│    作業中にパターン発見                                │
│           ↓                                             │
│    CLAUDE.mdに記録                                     │
│           ↓                                             │
│    繰り返し使う場合はスキル化                          │
│           ↓                                             │
│    gitにコミット                                        │
│           ↓                                             │
│    チーム/プロジェクト間で共有                         │
│           ↓                                             │
│    継続的に改善                                         │
│           ↓                                             │
│    (ループ)                                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 関連

- [Claude Code Memory Files](https://docs.anthropic.com/claude-code/memory)
- [Claude Code Skills](https://docs.anthropic.com/claude-code/skills)
