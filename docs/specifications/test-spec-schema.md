# Test Spec (IEEE 829) スキーマ詳細

## 概要

Test Spec は、IEEE 829規格に準拠したテスト仕様書です。Master Test Plan、Test Design、Test Case、Test Procedure を包含します。

## IEEE 829 構造

```
Test Specification (IEEE 829)
├── Master Test Plan (MTP)           # マスターテスト計画
│   ├── Test Plan Identifier         # 識別子
│   ├── Introduction                 # 概要
│   ├── Test Items                   # テスト対象
│   ├── Features to be Tested        # テスト対象機能
│   ├── Features not to be Tested    # テスト対象外機能
│   ├── Approach                     # アプローチ
│   ├── Pass/Fail Criteria           # 合否基準
│   ├── Deliverables                 # 成果物
│   ├── Environment                  # 環境
│   ├── Responsibilities             # 責任
│   ├── Schedule                     # スケジュール
│   └── Risks                        # リスク
├── Test Design Specification (TDS)  # テスト設計仕様
│   ├── Identifier                   # 識別子
│   ├── Features                     # 対象機能
│   ├── Approach                     # アプローチ
│   └── Test Cases                   # テストケース参照
├── Test Cases (TC)                  # テストケース
│   ├── Identifier                   # 識別子
│   ├── Objective                    # 目的
│   ├── Preconditions                # 前提条件
│   ├── Test Steps                   # テスト手順
│   ├── Expected Results             # 期待結果
│   └── Postconditions               # 事後条件
└── Test Procedures (TP)             # テスト手順
    ├── Identifier                   # 識別子
    ├── Setup                        # セットアップ
    ├── Steps                        # 手順
    └── Teardown                     # 後処理
```

## 必須フィールド

### test_plan

```json
{
  "test_plan": {
    "identifier": "MTP-2024-001",
    "introduction": {
      "purpose": "本テスト計画は、AuthServiceの品質保証を目的とし、機能テスト、性能テスト、セキュリティテストの戦略と計画を定義する。",
      "scope": "ユーザー認証・認可機能の全体テスト。単体テスト、統合テスト、E2Eテストを含む。",
      "objectives": [
        "機能要件の100%カバレッジ",
        "非機能要件の検証",
        "リグレッションの防止"
      ]
    },
    "test_items": [
      {
        "id": "TI-001",
        "name": "AuthService API",
        "version": "1.0.0",
        "description": "認証サービスのREST API"
      }
    ],
    "features_to_be_tested": [
      {
        "id": "FT-001",
        "name": "ユーザー登録",
        "srs_reference": "SRS-FR-001",
        "priority": "critical"
      }
    ],
    "approach": {
      "strategy": "リスクベーステスト戦略を採用。クリティカルな機能から優先的にテストし、自動化率80%を目標とする。",
      "test_levels": ["unit", "integration", "system"],
      "test_types": ["functional", "performance", "security"],
      "automation_scope": {
        "automated": ["単体テスト", "API統合テスト"],
        "manual": ["探索的テスト", "ユーザビリティテスト"],
        "automation_percentage_target": 80
      }
    },
    "pass_fail_criteria": {
      "overall_criteria": [
        {"criterion": "テストケース通過率", "threshold": "95%以上", "mandatory": true},
        {"criterion": "Critical/Highバグ", "threshold": "0件", "mandatory": true},
        {"criterion": "コードカバレッジ", "threshold": "80%以上", "mandatory": true}
      ],
      "exit_criteria": [
        "全Criticalテストケースが通過",
        "未解決のCritical/Highバグが0件",
        "性能基準を満たす"
      ]
    },
    "deliverables": [
      {"name": "テスト結果レポート", "description": "テスト実行結果のサマリー", "format": "HTML/PDF"},
      {"name": "カバレッジレポート", "description": "コードカバレッジ詳細", "format": "HTML"}
    ],
    "schedule": {
      "start_date": "2024-02-01",
      "end_date": "2024-03-15",
      "milestones": [
        {"name": "単体テスト完了", "date": "2024-02-15", "deliverables": ["単体テストレポート"]},
        {"name": "統合テスト完了", "date": "2024-03-01", "deliverables": ["統合テストレポート"]}
      ]
    }
  }
}
```

### test_cases

```json
{
  "test_cases": [
    {
      "id": "TC-0001",
      "title": "正常なメールアドレスとパスワードでユーザー登録が成功する",
      "objective": "有効な入力データでユーザー登録APIが正常に動作することを検証する",
      "srs_reference": "SRS-FR-001",
      "test_design_reference": "TDS-001",
      "priority": "critical",
      "test_type": "positive",
      "automation_status": "automated",
      "preconditions": [
        "テスト用DBが初期化されている",
        "メールサービスがモック化されている"
      ],
      "test_data": {
        "inputs": [
          {"name": "email", "value": "test@example.com", "description": "有効なメールアドレス"},
          {"name": "password", "value": "SecurePass123!", "description": "有効なパスワード"}
        ]
      },
      "test_steps": [
        {"step_number": 1, "action": "POST /api/auth/register を呼び出す", "input": "{email, password}"},
        {"step_number": 2, "action": "レスポンスステータスを確認", "expected_result": "201 Created"},
        {"step_number": 3, "action": "レスポンスボディを確認", "expected_result": "user_id が含まれる"}
      ],
      "expected_results": [
        "HTTPステータス 201 が返される",
        "レスポンスに user_id (UUID形式) が含まれる",
        "DBにユーザーレコードが作成される"
      ],
      "postconditions": [
        "ユーザーレコードがDBに存在する"
      ],
      "cleanup": [
        "作成したテストユーザーを削除"
      ]
    },
    {
      "id": "TC-0002",
      "title": "無効なメール形式でエラーが返される",
      "objective": "無効なメールアドレスでバリデーションエラーが発生することを検証する",
      "srs_reference": "SRS-FR-001",
      "priority": "high",
      "test_type": "negative",
      "automation_status": "automated",
      "preconditions": [
        "テスト用DBが初期化されている"
      ],
      "test_data": {
        "inputs": [
          {"name": "email", "value": "invalid-email", "description": "無効なメール形式"},
          {"name": "password", "value": "SecurePass123!", "description": "有効なパスワード"}
        ]
      },
      "test_steps": [
        {"step_number": 1, "action": "POST /api/auth/register を呼び出す", "input": "{email, password}"},
        {"step_number": 2, "action": "レスポンスステータスを確認", "expected_result": "400 Bad Request"}
      ],
      "expected_results": [
        "HTTPステータス 400 が返される",
        "エラーメッセージに'email'が含まれる"
      ]
    },
    {
      "id": "TC-0010",
      "title": "パスワードが8文字未満でエラーが返される",
      "objective": "短いパスワードでバリデーションエラーが発生することを検証する",
      "srs_reference": "SRS-FR-002",
      "priority": "high",
      "test_type": "boundary",
      "automation_status": "automated",
      "preconditions": ["テスト用DBが初期化されている"],
      "test_data": {
        "inputs": [
          {"name": "email", "value": "test@example.com"},
          {"name": "password", "value": "Short1!", "description": "7文字（境界値-1）"}
        ]
      },
      "test_steps": [
        {"step_number": 1, "action": "POST /api/auth/register を呼び出す"},
        {"step_number": 2, "action": "レスポンスを確認", "expected_result": "400 Bad Request"}
      ],
      "expected_results": [
        "HTTPステータス 400 が返される",
        "エラーメッセージにパスワード長の制約が含まれる"
      ]
    }
  ]
}
```

### traceability_matrix

```json
{
  "traceability_matrix": [
    {
      "requirement_id": "SRS-FR-001",
      "prd_requirement_id": "FR-001",
      "test_case_ids": ["TC-0001", "TC-0002", "TC-0003"],
      "coverage_status": "fully_covered"
    },
    {
      "requirement_id": "SRS-FR-002",
      "prd_requirement_id": "FR-002",
      "test_case_ids": ["TC-0010", "TC-0011"],
      "coverage_status": "fully_covered"
    },
    {
      "requirement_id": "SRS-NFR-001",
      "test_case_ids": ["TC-1001"],
      "coverage_status": "fully_covered"
    }
  ]
}
```

## テスト設計仕様

```json
{
  "test_design_specifications": [
    {
      "id": "TDS-001",
      "feature": "ユーザー登録",
      "srs_references": ["SRS-FR-001", "SRS-FR-002"],
      "approach": "同値分割と境界値分析を使用。正常系、異常系、境界値のテストケースを作成。",
      "test_techniques": [
        "equivalence_partitioning",
        "boundary_value_analysis"
      ],
      "pass_criteria": "全テストケースが期待結果と一致",
      "test_case_ids": ["TC-0001", "TC-0002", "TC-0003", "TC-0010", "TC-0011"]
    }
  ]
}
```

## テスト手順

```json
{
  "test_procedures": [
    {
      "id": "TP-001",
      "purpose": "ユーザー登録機能の手動テスト手順",
      "test_case_ids": ["TC-0001"],
      "special_requirements": [
        "テスト環境へのアクセス権限",
        "メールサービスの確認が可能なこと"
      ],
      "setup": [
        "テスト環境にログイン",
        "DBを初期状態にリセット",
        "メールサービスのモックを起動"
      ],
      "steps": [
        {"step_number": 1, "action": "ブラウザで /register を開く", "expected_result": "登録フォームが表示される"},
        {"step_number": 2, "action": "メールアドレスを入力", "input_data": "test@example.com", "expected_result": "入力が受け付けられる"},
        {"step_number": 3, "action": "パスワードを入力", "input_data": "SecurePass123!", "expected_result": "入力がマスクされて表示"},
        {"step_number": 4, "action": "登録ボタンをクリック", "expected_result": "成功メッセージが表示される"}
      ],
      "teardown": [
        "テストデータを削除",
        "ログアウト"
      ]
    }
  ]
}
```

## 検証

```bash
# Test Spec単体検証
python scripts/validate-documents.py --test path/to/test-spec.json

# トレーサビリティ検証（PRD, SRS, Test Specすべて必要）
python scripts/validate-documents.py \
  --prd path/to/prd.json \
  --srs path/to/srs.json \
  --test path/to/test-spec.json \
  --traceability
```
