# Quality Gate

## 概要

Quality Gateは、コードがプロダクションにデプロイされる前に満たすべき品質基準のチェックポイントです。

```
┌─────────────────────────────────────────────────────────────────────┐
│                        QUALITY GATE                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  コード変更                                                         │
│       ↓                                                             │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    GATE 1: Tests                            │   │
│  │  • 全テスト通過                                             │   │
│  │  • カバレッジ ≥ 80%                                         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│       ↓ PASS                                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    GATE 2: Code Quality                     │   │
│  │  • リントエラー 0件                                         │   │
│  │  • フォーマットチェック通過                                 │   │
│  │  • 型チェック通過                                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│       ↓ PASS                                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    GATE 3: Security                         │   │
│  │  • セキュリティスキャン通過                                 │   │
│  │  • 依存関係の脆弱性チェック                                 │   │
│  │  • シークレット検出なし                                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
│       ↓ PASS                                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    GATE 4: Review                           │   │
│  │  • コードレビュー承認（2名以上）                            │   │
│  │  • CI/CDパイプライン成功                                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│       ↓ ALL PASS                                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    ✅ MERGE ALLOWED                         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Quality Gate 基準

詳細は [criteria.md](criteria.md) を参照。

| Gate | カテゴリ | 項目 | 基準 | 必須 |
|------|---------|------|------|------|
| 1 | テスト | 全テスト通過 | 100% | ✅ |
| 1 | テスト | カバレッジ | ≥ 80% | ✅ |
| 2 | コード品質 | リントエラー | 0件 | ✅ |
| 2 | コード品質 | フォーマット | チェック通過 | ✅ |
| 2 | コード品質 | 型チェック | エラー 0件 | ✅ |
| 3 | セキュリティ | SAST スキャン | Critical 0件 | ✅ |
| 3 | セキュリティ | 依存関係脆弱性 | High以上 0件 | ✅ |
| 3 | セキュリティ | シークレット検出 | 検出 0件 | ✅ |
| 4 | レビュー | 承認者数 | ≥ 2名 | ✅ |
| 4 | レビュー | CI通過 | 全ジョブ成功 | ✅ |

## Gate詳細

### Gate 1: Tests（テスト）

```yaml
# チェック項目
- 全てのユニットテストが通過
- 全ての統合テストが通過
- コードカバレッジが80%以上

# コマンド例（Python）
pytest --cov --cov-report=term-missing --cov-fail-under=80

# コマンド例（JavaScript）
npm test -- --coverage --coverageThreshold='{"global":{"lines":80}}'
```

### Gate 2: Code Quality（コード品質）

```yaml
# チェック項目
- リントエラーがない
- コードフォーマットが統一されている
- 型エラーがない

# コマンド例（Python）
ruff check .
ruff format --check .
mypy .

# コマンド例（JavaScript/TypeScript）
npm run lint
npm run format:check
npm run typecheck
```

### Gate 3: Security（セキュリティ）

```yaml
# チェック項目
- 静的解析でセキュリティ問題がない
- 依存関係に既知の脆弱性がない
- ハードコードされたシークレットがない

# コマンド例（Python）
bandit -r src/
pip-audit
detect-secrets scan

# コマンド例（JavaScript）
npm audit
snyk test
```

### Gate 4: Review（レビュー）

```yaml
# チェック項目
- 2名以上のレビュアーが承認
- 全てのCIジョブが成功
- コンフリクトがない

# GitHub設定
Branch Protection Rules:
  - Require pull request reviews: 2
  - Require status checks to pass
  - Require branches to be up to date
```

## CI/CD統合

GitHub Actionsでの実装例：

```yaml
# .github/workflows/quality-gate.yml

name: Quality Gate

on:
  pull_request:
    branches: [main, develop]

jobs:
  test:
    name: "Gate 1: Tests"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests with coverage
        run: |
          pytest --cov --cov-report=xml --cov-fail-under=80

  quality:
    name: "Gate 2: Code Quality"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint & Format
        run: |
          ruff check .
          ruff format --check .
          mypy .

  security:
    name: "Gate 3: Security"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Security scan
        run: |
          bandit -r src/
          pip-audit
```

## ローカルでのQuality Gate

コミット前にローカルで確認：

```bash
# Python プロジェクト
#!/bin/bash
# scripts/quality-gate.sh

echo "🔍 Running Quality Gate..."

echo "📋 Gate 1: Tests"
pytest --cov --cov-fail-under=80 || exit 1

echo "📋 Gate 2: Code Quality"
ruff check . || exit 1
ruff format --check . || exit 1
mypy . || exit 1

echo "📋 Gate 3: Security"
bandit -r src/ || exit 1
pip-audit || exit 1

echo "✅ All Quality Gates Passed!"
```

## Quality Gateが失敗した場合

### Gate 1 失敗（テスト）

```markdown
原因: テストが失敗 / カバレッジ不足

対応:
1. 失敗したテストを確認
2. テストまたは実装を修正
3. カバレッジが足りない場合はテストを追加
4. 再実行して確認
```

### Gate 2 失敗（コード品質）

```markdown
原因: リント/フォーマット/型エラー

対応:
1. エラーメッセージを確認
2. ruff format . で自動修正（フォーマット）
3. リント・型エラーは手動修正
4. 再実行して確認
```

### Gate 3 失敗（セキュリティ）

```markdown
原因: セキュリティ脆弱性検出

対応:
1. 検出された脆弱性を確認
2. 依存関係の場合はアップデート
3. コードの場合は修正
4. 再実行して確認
```

### Gate 4 失敗（レビュー）

```markdown
原因: 承認不足 / CI失敗

対応:
1. レビュアーにレビュー依頼
2. フィードバックに対応
3. CI失敗の場合は該当ジョブを確認
4. 修正して再実行
```

## Claude CodeでのQuality Gate

```markdown
## 開発時のフロー

1. TDDで機能実装
2. 実装完了後にQuality Gateチェック
   - pytest --cov
   - ruff check .
   - ruff format --check .
   - mypy .
3. 全てパスしたらコミット
4. 失敗した場合は修正して再チェック

## コマンド例

```bash
# テスト & カバレッジ
pytest --cov --cov-report=term-missing

# リント
ruff check .

# フォーマット確認
ruff format --check .

# 型チェック
mypy .
```
```

## 関連ドキュメント

- [Quality Gate基準詳細](criteria.md)
- [TDDワークフロー](../tdd/README.md)
- [スクラムとの統合](../scrum/README.md)
