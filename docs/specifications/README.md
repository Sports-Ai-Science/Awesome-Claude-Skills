# 仕様書スキーマガイド

このドキュメントでは、PRD、SRS (IEEE 830)、Test Spec (IEEE 829) のスキーマ定義と使用方法を説明します。

## 概要

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DOCUMENT HIERARCHY                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────┐                                              │
│  │       PRD        │  ← ビジネス要件・プロダクト要件              │
│  │ (Product Reqs)   │                                              │
│  └────────┬─────────┘                                              │
│           │ traces to                                               │
│           ↓                                                         │
│  ┌──────────────────┐                                              │
│  │       SRS        │  ← ソフトウェア要件 (IEEE 830)               │
│  │ (Software Reqs)  │                                              │
│  └────────┬─────────┘                                              │
│           │ traces to                                               │
│           ↓                                                         │
│  ┌──────────────────┐                                              │
│  │    Test Spec     │  ← テスト仕様 (IEEE 829)                     │
│  │  (Test Design)   │                                              │
│  └──────────────────┘                                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## スキーマファイル

| ドキュメント | スキーマファイル | 説明 |
|-------------|-----------------|------|
| PRD | `schemas/prd.schema.json` | プロダクト要求仕様書 |
| SRS | `schemas/srs-ieee830.schema.json` | IEEE 830準拠ソフトウェア要求仕様書 |
| Test Spec | `schemas/test-spec-ieee829.schema.json` | IEEE 829準拠テスト仕様書 |

## トレーサビリティ

```
PRD Requirements (FR-XXX, NFR-XXX)
         ↓
SRS Requirements (SRS-FR-XXX, SRS-NFR-XXX)
    └─ source: "FR-XXX" (PRD参照)
         ↓
Test Cases (TC-XXXX)
    └─ srs_reference: "SRS-FR-XXX" (SRS参照)
         ↓
Traceability Matrix
    └─ requirement_id → test_case_ids
```

## 検証スクリプト

```bash
# 単一ドキュメントの検証
python scripts/validate-documents.py --prd docs/prd.json
python scripts/validate-documents.py --srs docs/srs.json
python scripts/validate-documents.py --test docs/test-spec.json

# 全ドキュメント + トレーサビリティチェック
python scripts/validate-documents.py \
  --prd docs/prd.json \
  --srs docs/srs.json \
  --test docs/test-spec.json \
  --traceability

# 完成度スコア表示
python scripts/validate-documents.py --prd docs/prd.json --completeness

# JSON出力
python scripts/validate-documents.py --prd docs/prd.json --json-output
```

## Quality Gate統合

ドキュメント検証はQuality Gateの一部として実行されます：

| Gate | チェック項目 | 基準 |
|------|-------------|------|
| 5 | PRDスキーマ検証 | 必須フィールド100% |
| 5 | SRSスキーマ検証 | 必須フィールド100% |
| 5 | Test Specスキーマ検証 | 必須フィールド100% |
| 5 | トレーサビリティ | PRD→SRS→Test 100%カバー |

## ドキュメントガイドライン

### PRD作成時

1. `metadata`セクションを完全に記入
2. 全ての要件にIDを付与（FR-XXX, NFR-XXX形式）
3. ユーザーストーリーにAcceptance Criteriaを記載
4. 成功指標（KPI）を定義

### SRS作成時

1. PRD要件を`source`フィールドで参照
2. IEEE 830の構造に従う
3. 機能要件・非機能要件を明確に分離
4. 検証方法（test/inspection/demonstration/analysis）を指定

### Test Spec作成時

1. SRS要件を`srs_reference`で参照
2. IEEE 829の構造に従う
3. 全SRS要件に対するテストケースを作成
4. トレーサビリティマトリクスを更新

## 詳細ドキュメント

- [PRDスキーマ詳細](prd-schema.md)
- [SRSスキーマ詳細](srs-schema.md)
- [Test Specスキーマ詳細](test-spec-schema.md)
