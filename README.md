# Awesome Claude Skills - Scrum + TDD Hybrid with Quality Gate

AIアシスタント（Claude）と人間開発者が協働するためのスクラム・TDDハイブリッドワークフローフレームワーク。Quality Gateによる品質保証を統合しています。

## 概要

このリポジトリは、以下の3つの開発手法を統合したハイブリッドワークフローを提供します：

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Scrum + TDD + Quality Gate                       │
├─────────────────────────────────────────────────────────────────────┤
│  Sprint Planning → TDD Cycle → Quality Gate → Sprint Review         │
│       ↓              ↓              ↓              ↓                │
│  バックログ作成   Red→Green→Refactor  品質検証    デモ・振り返り    │
└─────────────────────────────────────────────────────────────────────┘
```

## ワークフロー図

```
                         ┌──────────────────┐
                         │  Product Backlog │
                         └────────┬─────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│                        SPRINT (1-2週間)                             │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────┐                                               │
│  │ Sprint Planning  │ ← ユーザーストーリー選択・タスク分解          │
│  └────────┬─────────┘                                               │
│           ↓                                                         │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                     TDD Cycle (繰り返し)                     │   │
│  │  ┌─────────┐   ┌─────────┐   ┌──────────┐                   │   │
│  │  │  RED    │ → │  GREEN  │ → │ REFACTOR │ ─┐               │   │
│  │  │テスト作成│   │実装作成 │   │リファクタ│  │               │   │
│  │  └─────────┘   └─────────┘   └──────────┘  │               │   │
│  │       ↑                                     │               │   │
│  │       └─────────────────────────────────────┘               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│           ↓                                                         │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                    QUALITY GATE                               │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────┐ │  │
│  │  │ Gate 1     │  │ Gate 2     │  │ Gate 3     │  │ Gate 4 │ │  │
│  │  │ Unit Test  │→ │ Code       │→ │ Security   │→ │ Review │ │  │
│  │  │ Coverage   │  │ Quality    │  │ Scan       │  │ Check  │ │  │
│  │  │ ≥80%       │  │ A/B Rating │  │ No Critical│  │ ≥2人   │ │  │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────┘ │  │
│  └──────────────────────────────────────────────────────────────┘  │
│           ↓ (All Gates Pass)                                        │
│  ┌──────────────────┐                                               │
│  │  Sprint Review   │ ← デモ・フィードバック                        │
│  └────────┬─────────┘                                               │
│           ↓                                                         │
│  ┌──────────────────┐                                               │
│  │ Sprint Retro     │ ← 振り返り・改善                              │
│  └──────────────────┘                                               │
└─────────────────────────────────────────────────────────────────────┘
```

## ディレクトリ構成

```
.
├── CLAUDE.md                    # Claude Code用ガイドライン
├── README.md                    # このファイル
├── docs/
│   ├── scrum/
│   │   ├── README.md           # スクラムワークフロー説明
│   │   ├── sprint-planning.md  # スプリント計画ガイド
│   │   └── ceremonies.md       # セレモニー定義
│   ├── tdd/
│   │   ├── README.md           # TDDワークフロー説明
│   │   └── red-green-refactor.md
│   └── quality-gate/
│       ├── README.md           # Quality Gate概要
│       └── criteria.md         # 品質基準定義
├── templates/
│   ├── user-story.md           # ユーザーストーリーテンプレート
│   ├── test-case.md            # テストケーステンプレート
│   └── pull-request.md         # PRテンプレート
└── .github/
    └── workflows/
        └── quality-gate.yml    # Quality Gate CI/CD
```

## Quality Gate 基準

| Gate | 項目 | 基準 | 必須 |
|------|------|------|------|
| 1 | テストカバレッジ | ≥ 80% | Yes |
| 2 | コード品質 | SonarQube A/B Rating | Yes |
| 3 | セキュリティ | Critical/High 脆弱性 0件 | Yes |
| 4 | コードレビュー | 2名以上の承認 | Yes |
| 5 | ドキュメント | 新規API・機能の文書化 | No |
| 6 | パフォーマンス | レスポンス劣化なし | No |

## クイックスタート

1. **スプリント計画**: [docs/scrum/sprint-planning.md](docs/scrum/sprint-planning.md)
2. **TDD開発**: [docs/tdd/red-green-refactor.md](docs/tdd/red-green-refactor.md)
3. **Quality Gate通過**: [docs/quality-gate/criteria.md](docs/quality-gate/criteria.md)

## Claude Code連携

Claude Codeと連携する際は、[CLAUDE.md](CLAUDE.md)のガイドラインに従ってください。

```bash
# Claude Codeでの開発開始時
claude "新しいユーザーストーリーを実装してください: [ストーリー内容]"
```

## ライセンス

MIT License
