# PRD スキーマ詳細

## 概要

PRD (Product Requirements Document) は、プロダクトのビジネス要件とユーザー要件を定義するドキュメントです。

## 構造

```
PRD
├── metadata              # ドキュメントメタデータ
├── executive_summary     # エグゼクティブサマリー
├── problem_statement     # 課題定義
├── goals                 # 目標
├── user_personas         # ユーザーペルソナ
├── requirements          # 要件
│   ├── functional        # 機能要件
│   └── non_functional    # 非機能要件
├── user_stories          # ユーザーストーリー
├── success_metrics       # 成功指標
├── timeline              # タイムライン
├── risks                 # リスク（オプション）
├── dependencies          # 依存関係（オプション）
└── appendix              # 付録（オプション）
```

## 必須フィールド

### metadata

```json
{
  "metadata": {
    "document_id": "PRD-2024-001",
    "title": "ユーザー認証機能",
    "version": "1.0.0",
    "status": "draft",
    "created_date": "2024-01-15",
    "author": "Product Manager"
  }
}
```

| フィールド | 型 | 必須 | 説明 |
|-----------|-----|------|------|
| document_id | string | ✅ | PRD-YYYY-NNN形式 |
| title | string | ✅ | 5-200文字 |
| version | string | ✅ | SemVer形式 |
| status | enum | ✅ | draft/review/approved/deprecated |
| created_date | date | ✅ | ISO 8601形式 |
| author | string | ✅ | 作成者名 |
| last_updated | date | - | 最終更新日 |
| reviewers | array | - | レビュアーリスト |
| approvers | array | - | 承認者リスト |

### requirements

```json
{
  "requirements": {
    "functional": [
      {
        "id": "FR-001",
        "description": "ユーザーはメールアドレスとパスワードで登録できる",
        "priority": "must-have",
        "status": "proposed",
        "rationale": "新規ユーザー獲得のため",
        "verification_method": "test"
      }
    ],
    "non_functional": [
      {
        "id": "NFR-001",
        "description": "登録APIは99.9%の可用性を維持する",
        "priority": "must-have",
        "status": "proposed"
      }
    ]
  }
}
```

| フィールド | 型 | 必須 | 説明 |
|-----------|-----|------|------|
| id | string | ✅ | FR-NNN または NFR-NNN形式 |
| description | string | ✅ | 10文字以上 |
| priority | enum | ✅ | must-have/should-have/nice-to-have |
| status | enum | ✅ | proposed/approved/implemented/verified/deferred |
| rationale | string | - | 理由・根拠 |
| source | string | - | 要件の出典 |
| verification_method | enum | - | test/inspection/demonstration/analysis |
| related_user_stories | array | - | 関連ユーザーストーリーID |

### user_stories

```json
{
  "user_stories": [
    {
      "id": "US-001",
      "persona": "新規ユーザー",
      "want": "メールアドレスとパスワードで登録したい",
      "so_that": "サービスを利用できるようになる",
      "acceptance_criteria": [
        {
          "given": "登録ページにアクセスしている",
          "when": "有効なメールとパスワードを入力して送信",
          "then": "登録が成功し確認メールが送信される"
        }
      ],
      "priority": "must-have",
      "story_points": 5,
      "related_requirements": ["FR-001", "FR-002"]
    }
  ]
}
```

## サンプルドキュメント

```json
{
  "metadata": {
    "document_id": "PRD-2024-001",
    "title": "ユーザー認証機能",
    "version": "1.0.0",
    "status": "draft",
    "created_date": "2024-01-15",
    "author": "田中太郎",
    "reviewers": ["鈴木花子", "佐藤次郎"]
  },
  "executive_summary": {
    "overview": "本プロダクトは、セキュアで使いやすいユーザー認証機能を提供します。メールアドレスとパスワードによる従来の認証に加え、ソーシャルログインもサポートします。",
    "value_proposition": "ユーザーの登録・ログイン体験を向上させ、コンバージョン率を20%改善",
    "target_release": "2024年Q2"
  },
  "problem_statement": {
    "current_situation": "現在のシステムには認証機能がなく、全てのユーザーが匿名でアクセスしています。これにより、パーソナライズされた体験を提供できず、ユーザーエンゲージメントが低下しています。",
    "problems": [
      {
        "id": "P-001",
        "description": "ユーザーを識別できないため、パーソナライズができない",
        "severity": "high",
        "affected_users": "全ユーザー"
      }
    ],
    "impact": "ユーザーリテンション率が業界平均を30%下回っている"
  },
  "goals": {
    "business_goals": [
      {
        "id": "BG-001",
        "description": "ユーザーリテンション率の向上",
        "metric": "30日リテンション率",
        "target": "40%以上"
      }
    ],
    "product_goals": [
      {
        "id": "PG-001",
        "description": "セキュアな認証システムの構築",
        "priority": "must-have"
      }
    ],
    "non_goals": [
      "二要素認証は次期リリースで対応"
    ]
  },
  "user_personas": [
    {
      "id": "P-001",
      "name": "新規ユーザー",
      "description": "サービスを初めて利用するユーザー",
      "demographics": {
        "age_range": "20-40",
        "occupation": "会社員",
        "tech_savviness": "intermediate"
      },
      "goals": [
        "簡単にアカウントを作成したい",
        "個人情報を安全に管理したい"
      ],
      "pain_points": [
        "複雑な登録フォーム",
        "多すぎる入力項目"
      ]
    }
  ],
  "requirements": {
    "functional": [
      {
        "id": "FR-001",
        "description": "ユーザーはメールアドレスとパスワードで新規登録できる",
        "priority": "must-have",
        "status": "proposed",
        "rationale": "基本的な認証フロー",
        "verification_method": "test"
      },
      {
        "id": "FR-002",
        "description": "パスワードは8文字以上で、英数字を含む必要がある",
        "priority": "must-have",
        "status": "proposed",
        "verification_method": "test"
      }
    ],
    "non_functional": [
      {
        "id": "NFR-001",
        "description": "認証APIのレスポンスタイムは200ms以下",
        "priority": "must-have",
        "status": "proposed",
        "verification_method": "test"
      }
    ]
  },
  "user_stories": [
    {
      "id": "US-001",
      "persona": "新規ユーザー",
      "want": "メールアドレスとパスワードで登録したい",
      "so_that": "サービスの機能を利用できるようになる",
      "acceptance_criteria": [
        {
          "given": "未登録のユーザーが登録ページにいる",
          "when": "有効なメールアドレスと8文字以上のパスワードを入力して送信",
          "then": "アカウントが作成され、確認メールが送信される"
        },
        {
          "given": "未登録のユーザーが登録ページにいる",
          "when": "既に登録済みのメールアドレスを入力",
          "then": "エラーメッセージが表示される"
        }
      ],
      "priority": "must-have",
      "story_points": 5,
      "related_requirements": ["FR-001", "FR-002"]
    }
  ],
  "success_metrics": {
    "kpis": [
      {
        "id": "KPI-001",
        "name": "登録完了率",
        "description": "登録を開始したユーザーのうち完了した割合",
        "baseline": "N/A",
        "target": "80%以上",
        "measurement_method": "Analytics",
        "frequency": "Weekly"
      }
    ]
  },
  "timeline": {
    "milestones": [
      {
        "name": "設計完了",
        "target_date": "2024-02-01",
        "deliverables": ["SRS", "API設計書", "UI/UXデザイン"]
      },
      {
        "name": "開発完了",
        "target_date": "2024-03-15",
        "deliverables": ["実装コード", "ユニットテスト"]
      },
      {
        "name": "リリース",
        "target_date": "2024-04-01",
        "deliverables": ["本番デプロイ"]
      }
    ]
  }
}
```

## 検証

```bash
python scripts/validate-documents.py --prd path/to/prd.json
```
