# Quality Gate 基準詳細

## 基準一覧

```
┌─────────────────────────────────────────────────────────────────────┐
│                    QUALITY GATE CRITERIA                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ GATE 1: TESTS                                               │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ • Test Pass Rate        : 100%                  [REQUIRED]  │   │
│  │ • Line Coverage         : ≥ 80%                 [REQUIRED]  │   │
│  │ • Branch Coverage       : ≥ 70%                 [OPTIONAL]  │   │
│  │ • Mutation Score        : ≥ 60%                 [OPTIONAL]  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ GATE 2: CODE QUALITY                                        │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ • Lint Errors           : 0                     [REQUIRED]  │   │
│  │ • Format Check          : Pass                  [REQUIRED]  │   │
│  │ • Type Errors           : 0                     [REQUIRED]  │   │
│  │ • Complexity (Cyclomatic): ≤ 10 per function   [OPTIONAL]  │   │
│  │ • Duplication           : ≤ 3%                  [OPTIONAL]  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ GATE 3: SECURITY                                            │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ • SAST Critical Issues  : 0                     [REQUIRED]  │   │
│  │ • SAST High Issues      : 0                     [REQUIRED]  │   │
│  │ • Dependency Vulns (High): 0                    [REQUIRED]  │   │
│  │ • Secret Detection      : 0                     [REQUIRED]  │   │
│  │ • SAST Medium Issues    : ≤ 5                   [OPTIONAL]  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ GATE 4: REVIEW & CI                                         │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ • Approvals             : ≥ 2                   [REQUIRED]  │   │
│  │ • CI Pipeline           : All Jobs Pass         [REQUIRED]  │   │
│  │ • Merge Conflicts       : 0                     [REQUIRED]  │   │
│  │ • Documentation Updated : Yes                   [OPTIONAL]  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Gate 1: Tests（テスト）

### 1.1 Test Pass Rate（テスト通過率）

| 項目 | 値 |
|------|-----|
| 基準 | 100% |
| 必須 | Yes |
| 説明 | 全てのテストが通過している |

```bash
# Python
pytest

# JavaScript
npm test
```

### 1.2 Line Coverage（行カバレッジ）

| 項目 | 値 |
|------|-----|
| 基準 | ≥ 80% |
| 必須 | Yes |
| 説明 | コードの80%以上がテストでカバー |

```bash
# Python
pytest --cov --cov-fail-under=80

# JavaScript
npm test -- --coverage --coverageThreshold='{"global":{"lines":80}}'
```

### 1.3 Branch Coverage（分岐カバレッジ）

| 項目 | 値 |
|------|-----|
| 基準 | ≥ 70% |
| 必須 | No |
| 説明 | 条件分岐の70%以上がテストでカバー |

```bash
# Python
pytest --cov --cov-branch

# JavaScript
npm test -- --coverage --collectCoverageFrom='src/**/*.{js,ts}'
```

### 1.4 Mutation Score（ミューテーションスコア）

| 項目 | 値 |
|------|-----|
| 基準 | ≥ 60% |
| 必須 | No |
| 説明 | テストがバグを検出できる割合 |

```bash
# Python
mutmut run

# JavaScript
npx stryker run
```

---

## Gate 2: Code Quality（コード品質）

### 2.1 Lint Errors（リントエラー）

| 項目 | 値 |
|------|-----|
| 基準 | 0件 |
| 必須 | Yes |
| 説明 | リントエラーがない |

```bash
# Python
ruff check .

# JavaScript
npm run lint
```

### 2.2 Format Check（フォーマットチェック）

| 項目 | 値 |
|------|-----|
| 基準 | Pass |
| 必須 | Yes |
| 説明 | コードフォーマットが統一 |

```bash
# Python
ruff format --check .

# JavaScript
npm run format:check
```

### 2.3 Type Errors（型エラー）

| 項目 | 値 |
|------|-----|
| 基準 | 0件 |
| 必須 | Yes |
| 説明 | 型エラーがない |

```bash
# Python
mypy .

# TypeScript
npm run typecheck
```

### 2.4 Cyclomatic Complexity（循環的複雑度）

| 項目 | 値 |
|------|-----|
| 基準 | ≤ 10 per function |
| 必須 | No |
| 説明 | 関数の複雑さが適切 |

```bash
# Python
radon cc src/ -a -s

# JavaScript
npx eslint --rule 'complexity: [error, 10]' src/
```

### 2.5 Code Duplication（コード重複）

| 項目 | 値 |
|------|-----|
| 基準 | ≤ 3% |
| 必須 | No |
| 説明 | 重複コードが少ない |

```bash
# Python
pylint --disable=all --enable=duplicate-code src/

# JavaScript
npx jscpd src/
```

---

## Gate 3: Security（セキュリティ）

### 3.1 SAST Critical/High Issues

| 項目 | 値 |
|------|-----|
| 基準 | 0件 |
| 必須 | Yes |
| 説明 | Critical/Highレベルの脆弱性なし |

```bash
# Python
bandit -r src/ -ll  # Low以下を無視

# JavaScript
npm audit --audit-level=high
```

### 3.2 Dependency Vulnerabilities（依存関係脆弱性）

| 項目 | 値 |
|------|-----|
| 基準 | High以上 0件 |
| 必須 | Yes |
| 説明 | 依存パッケージに重大な脆弱性なし |

```bash
# Python
pip-audit

# JavaScript
npm audit
snyk test
```

### 3.3 Secret Detection（シークレット検出）

| 項目 | 値 |
|------|-----|
| 基準 | 0件 |
| 必須 | Yes |
| 説明 | ハードコードされた秘密情報なし |

```bash
# 共通
detect-secrets scan
gitleaks detect
```

---

## Gate 4: Review & CI

### 4.1 Approvals（承認）

| 項目 | 値 |
|------|-----|
| 基準 | ≥ 2名 |
| 必須 | Yes |
| 説明 | 2名以上のレビュアーが承認 |

GitHub Branch Protection設定：
```yaml
Require pull request reviews before merging: true
Required approving reviews: 2
```

### 4.2 CI Pipeline

| 項目 | 値 |
|------|-----|
| 基準 | All Jobs Pass |
| 必須 | Yes |
| 説明 | 全CIジョブが成功 |

### 4.3 Merge Conflicts

| 項目 | 値 |
|------|-----|
| 基準 | 0件 |
| 必須 | Yes |
| 説明 | マージコンフリクトがない |

---

## スコアカード例

```markdown
## Quality Gate Report

### Sprint 3 - Feature: User Registration

| Gate | Criteria | Target | Actual | Status |
|------|----------|--------|--------|--------|
| 1 | Test Pass Rate | 100% | 100% | ✅ |
| 1 | Line Coverage | ≥80% | 87% | ✅ |
| 1 | Branch Coverage | ≥70% | 75% | ✅ |
| 2 | Lint Errors | 0 | 0 | ✅ |
| 2 | Format Check | Pass | Pass | ✅ |
| 2 | Type Errors | 0 | 0 | ✅ |
| 2 | Complexity | ≤10 | 6 | ✅ |
| 3 | SAST Critical | 0 | 0 | ✅ |
| 3 | SAST High | 0 | 0 | ✅ |
| 3 | Dependency Vulns | 0 | 0 | ✅ |
| 3 | Secrets | 0 | 0 | ✅ |
| 4 | Approvals | ≥2 | 2 | ✅ |
| 4 | CI Pipeline | Pass | Pass | ✅ |

### Overall: ✅ ALL GATES PASSED

Merge approved at: 2024-01-15 14:30 UTC
Approved by: @alice, @bob
```

---

## 基準のカスタマイズ

プロジェクトの状況に応じて基準を調整可能：

### 新規プロジェクト（立ち上げ期）

```yaml
tests:
  coverage: 60%  # 低めに設定
quality:
  complexity: 15  # 緩めに設定
security:
  medium_issues: 10  # 許容を増やす
```

### 成熟プロジェクト

```yaml
tests:
  coverage: 90%  # 高めに設定
  mutation_score: 80%  # ミューテーションテスト追加
quality:
  complexity: 8  # 厳しく設定
  duplication: 1%  # 厳しく設定
security:
  all_issues: 0  # 全レベルで0
```

### クリティカルシステム（金融・医療等）

```yaml
tests:
  coverage: 95%
  mutation_score: 90%
quality:
  complexity: 5
security:
  all_issues: 0
  manual_review: required
review:
  approvals: 3
  senior_approval: required
```
