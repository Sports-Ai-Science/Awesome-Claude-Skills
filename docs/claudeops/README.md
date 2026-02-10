# ClaudeOps

**Claude-Assisted Development Framework**

## 概要

ClaudeOpsは、Claude Codeを活用した開発手法の統合フレームワークです。

既存の開発方法論（TDD、Scrum、Kanban等）をClaude Codeで強化する方法と、Claude Code固有のプラクティスを体系化しています。

## 構成

```
ClaudeOps
│
├── CDD (Claude Delegated Development)
│   └── Claude Code固有のプラクティス
│       Origin: Boris Cherny (@bcherny) - Anthropic
│
└── Methodologies (Claude × 既存流派)
    ├── Claude TDD
    ├── Claude Scrum
    ├── Claude Kanban
    └── ...
```

## CDD - Claude Delegated Development

Claude Code チームが実践する開発手法。「信頼して委任する」が核心。

**特徴:**
- 並列作業（複数worktree/セッション）
- 委任主義（Don't micromanage how）
- URL駆動（Slack/GitHub URLを渡して "fix"）
- 知識蓄積（CLAUDE.md, Skills）
- サブエージェント活用

📄 [CDD 詳細](cdd/README.md)

## Methodologies

既存の開発方法論をClaude Codeで強化したバリエーション。

| 流派 | 概要 |
|------|------|
| [Claude TDD](methodologies/claude-tdd/) | テスト駆動開発 + Claude |
| [Claude Scrum](methodologies/claude-scrum/) | Scrum + Claude |
| Claude Kanban | Kanban + Claude |
| Claude XP | エクストリームプログラミング + Claude |
| Claude BDD | 振る舞い駆動開発 + Claude |
| Claude DevOps | DevOps + Claude |

※ 各流派の中身はチーム/プロジェクトで定義

📄 [テンプレート](methodologies/_template/README.md)

## 原則

### 1. 人間は監督者

```
従来:  人間が「考えて」「作業する」
ClaudeOps: 人間が「指示して」「確認する」
```

### 2. Claudeを信頼する

```
× 逐一確認して進める
○ コンテキストを渡して結果を待つ
```

### 3. 知識を蓄積する

```
CLAUDE.md + Skills = チームの資産
修正のたびに更新し、同じミスを防ぐ
```

### 4. 並列で考える

```
1つのClaudeに依存しない
複数セッション、サブエージェントを活用
```

## 始め方

1. **CDD を学ぶ** - [CDD README](cdd/README.md)
2. **既存流派と組み合わせる** - [Methodologies](methodologies/)
3. **チームに合わせてカスタマイズ**

## 関連リンク

- [Claude Code Docs](https://docs.anthropic.com/claude-code)
- [Boris Cherny (@bcherny)](https://x.com/bcherny)
