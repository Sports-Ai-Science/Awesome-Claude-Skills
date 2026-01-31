# SRS (IEEE 830) スキーマ詳細

## 概要

SRS (Software Requirements Specification) は、IEEE 830規格に準拠したソフトウェア要求仕様書です。

## IEEE 830 構造

```
SRS (IEEE 830)
├── 1. Introduction                    # はじめに
│   ├── 1.1 Purpose                    # 目的
│   ├── 1.2 Scope                      # スコープ
│   ├── 1.3 Definitions                # 定義・略語
│   ├── 1.4 References                 # 参考文献
│   └── 1.5 Overview                   # 概要
├── 2. Overall Description             # 全体説明
│   ├── 2.1 Product Perspective        # 製品の位置づけ
│   ├── 2.2 Product Functions          # 製品機能
│   ├── 2.3 User Characteristics       # ユーザー特性
│   ├── 2.4 Constraints                # 制約条件
│   ├── 2.5 Assumptions & Dependencies # 前提条件・依存関係
│   └── 2.6 Apportioning Requirements  # 要件の配分
├── 3. Specific Requirements           # 詳細要件
│   ├── 3.1 External Interfaces        # 外部インターフェース
│   ├── 3.2 Functional Requirements    # 機能要件
│   ├── 3.3 Performance Requirements   # 性能要件
│   ├── 3.4 Database Requirements      # データベース要件
│   ├── 3.5 Design Constraints         # 設計制約
│   ├── 3.6 System Attributes          # システム属性
│   └── 3.7 Other Requirements         # その他の要件
└── Appendices                         # 付録
    ├── Analysis Models                # 分析モデル
    ├── TBD List                       # 未決定事項
    └── Revision History               # 改訂履歴
```

## 必須フィールド

### introduction

```json
{
  "introduction": {
    "purpose": {
      "description": "本ドキュメントは、ユーザー認証システムのソフトウェア要件を定義する。開発チーム、テストチーム、ステークホルダーに対して、システムの機能的・非機能的要件を明確にする。",
      "intended_audience": ["開発チーム", "テストチーム", "プロジェクトマネージャー"]
    },
    "scope": {
      "product_name": "AuthService",
      "product_description": "Webアプリケーション向けの認証・認可サービス。メール/パスワード認証、ソーシャルログイン、セッション管理を提供する。",
      "benefits": [
        "セキュアなユーザー認証",
        "スケーラブルな設計",
        "複数の認証方式対応"
      ],
      "objectives": [
        "99.9%の可用性を実現",
        "OWASP Top 10に対応したセキュリティ"
      ],
      "exclusions": [
        "二要素認証（次期バージョン）",
        "生体認証"
      ]
    },
    "definitions": [
      {
        "term": "JWT",
        "definition": "JSON Web Token - 認証トークンの形式",
        "acronym": "JWT"
      }
    ],
    "references": [
      {
        "id": "REF-001",
        "title": "PRD-2024-001",
        "version": "1.0.0",
        "date": "2024-01-15"
      }
    ],
    "overview": "本ドキュメントは、Section 2で製品の全体像を説明し、Section 3で詳細な機能要件・非機能要件を定義する。各要件はPRDからトレース可能であり、テスト仕様書へのトレーサビリティも確保されている。"
  }
}
```

### functional_requirements

```json
{
  "specific_requirements": {
    "functional_requirements": [
      {
        "id": "SRS-FR-001",
        "name": "ユーザー登録",
        "description": "システムは、メールアドレスとパスワードを使用した新規ユーザー登録機能を提供する。",
        "rationale": "PRD FR-001の実装要件",
        "source": "FR-001",
        "priority": "essential",
        "status": "approved",
        "stability": "stable",
        "verification_method": "test",
        "inputs": [
          {
            "name": "email",
            "type": "string",
            "constraints": "有効なメール形式"
          },
          {
            "name": "password",
            "type": "string",
            "constraints": "8文字以上、英数字含む"
          }
        ],
        "outputs": [
          {
            "name": "user_id",
            "type": "string (UUID)",
            "description": "作成されたユーザーのID"
          }
        ],
        "processing": "1. 入力バリデーション 2. 重複チェック 3. パスワードハッシュ化 4. DB保存 5. 確認メール送信",
        "preconditions": [
          "メールアドレスが未登録である"
        ],
        "postconditions": [
          "ユーザーレコードがDBに作成される",
          "確認メールが送信される"
        ],
        "exceptions": [
          {
            "condition": "メールアドレスが既に登録済み",
            "action": "409 Conflict エラーを返す"
          }
        ]
      }
    ]
  }
}
```

### non_functional_requirement

```json
{
  "specific_requirements": {
    "performance_requirements": [
      {
        "id": "SRS-NFR-001",
        "category": "performance",
        "description": "ユーザー登録APIのレスポンスタイム",
        "rationale": "ユーザー体験の向上",
        "metric": "95パーセンタイルレスポンスタイム",
        "target": "200ms以下",
        "current_value": "N/A",
        "priority": "essential",
        "verification_method": "test"
      }
    ],
    "software_system_attributes": {
      "reliability": [
        {
          "id": "SRS-NFR-010",
          "category": "reliability",
          "description": "システム可用性",
          "metric": "月間稼働率",
          "target": "99.9%",
          "priority": "essential",
          "verification_method": "analysis"
        }
      ],
      "security": [
        {
          "id": "SRS-NFR-020",
          "category": "security",
          "description": "パスワード保存",
          "metric": "ハッシュアルゴリズム",
          "target": "bcrypt (cost factor 12以上)",
          "priority": "essential",
          "verification_method": "inspection"
        }
      ]
    }
  }
}
```

## トレーサビリティ

```json
{
  "traceability_matrix": [
    {
      "requirement_id": "SRS-FR-001",
      "source": "FR-001",
      "design_element": "UserService.register()",
      "test_case_id": "TC-0001",
      "status": "implemented"
    },
    {
      "requirement_id": "SRS-FR-002",
      "source": "FR-002",
      "design_element": "PasswordValidator",
      "test_case_id": "TC-0010",
      "status": "verified"
    }
  ]
}
```

## サンプルドキュメント（部分）

```json
{
  "metadata": {
    "document_id": "SRS-2024-001",
    "title": "ユーザー認証システム ソフトウェア要求仕様書",
    "version": "1.0.0",
    "status": "approved",
    "created_date": "2024-01-20",
    "author": "開発リーダー",
    "related_prd": "PRD-2024-001"
  },
  "introduction": {
    "purpose": {
      "description": "本ドキュメントは、AuthServiceのソフトウェア要件を定義する。IEEE 830規格に準拠し、機能要件・非機能要件を網羅的に記述する。",
      "intended_audience": ["開発チーム", "テストチーム", "アーキテクト"]
    },
    "scope": {
      "product_name": "AuthService",
      "product_description": "認証・認可マイクロサービス。JWT ベースのトークン認証を提供し、ユーザー管理、セッション管理を担当する。",
      "benefits": [
        "統一された認証基盤",
        "マイクロサービス対応",
        "高いセキュリティ"
      ],
      "objectives": [
        "セキュアな認証フロー",
        "スケーラブルな設計",
        "監査可能なログ"
      ]
    },
    "definitions": [
      {"term": "JWT", "definition": "JSON Web Token", "acronym": "JWT"},
      {"term": "OAuth", "definition": "Open Authorization", "acronym": "OAuth 2.0"}
    ],
    "references": [
      {"id": "REF-001", "title": "PRD-2024-001", "version": "1.0.0", "date": "2024-01-15"}
    ],
    "overview": "本ドキュメントは3部構成。Section 2で全体像、Section 3で詳細要件を定義する。"
  },
  "overall_description": {
    "product_perspective": {
      "system_context": "AuthServiceは、Webアプリケーション全体のマイクロサービスアーキテクチャにおける認証コンポーネントとして機能する。API Gateway経由でリクエストを受け取り、JWTトークンを発行する。"
    },
    "product_functions": [
      {"id": "PF-001", "name": "ユーザー登録", "description": "新規ユーザーの登録", "priority": "essential"},
      {"id": "PF-002", "name": "ログイン", "description": "認証とトークン発行", "priority": "essential"}
    ],
    "user_characteristics": [
      {
        "user_class": "エンドユーザー",
        "description": "Webアプリケーションの利用者",
        "technical_expertise": "novice",
        "frequency_of_use": "日次"
      }
    ],
    "constraints": {
      "regulatory": ["GDPR準拠", "個人情報保護法準拠"],
      "security": ["OWASP Top 10対応", "TLS 1.3必須"]
    },
    "assumptions_dependencies": {
      "assumptions": [
        {"id": "A-001", "description": "PostgreSQL 15以上が利用可能", "risk_if_false": "DBスキーマの互換性問題"}
      ]
    }
  },
  "specific_requirements": {
    "functional_requirements": [
      {
        "id": "SRS-FR-001",
        "name": "ユーザー登録",
        "description": "メールアドレスとパスワードによる新規ユーザー登録機能を提供する",
        "source": "FR-001",
        "priority": "essential",
        "status": "approved",
        "verification_method": "test",
        "preconditions": ["メールアドレスが未登録"],
        "postconditions": ["ユーザーレコードが作成される"]
      }
    ],
    "performance_requirements": [
      {
        "id": "SRS-NFR-001",
        "category": "performance",
        "description": "APIレスポンスタイム",
        "metric": "p95 latency",
        "target": "200ms",
        "priority": "essential",
        "verification_method": "test"
      }
    ]
  }
}
```

## 検証

```bash
python scripts/validate-documents.py --srs path/to/srs.json
```
