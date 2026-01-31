# コントリビューションガイド

このプロジェクトへの貢献をありがとうございます！

## 開発フロー

このプロジェクトでは、**Scrum + TDD + Quality Gate** のハイブリッドワークフローを採用しています。

```
1. Issue作成 → 2. ブランチ作成 → 3. TDD開発 → 4. Quality Gate → 5. PR → 6. レビュー → 7. マージ
```

## はじめに

### 環境セットアップ

```bash
# リポジトリをクローン
git clone https://github.com/your-org/awesome-claude-skills.git
cd awesome-claude-skills

# 依存関係をインストール（Python）
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Pre-commitフックをインストール
pip install pre-commit
pre-commit install

# 依存関係をインストール（JavaScript）
npm install
```

### ブランチ戦略

```
main          # 本番リリース用
├── develop   # 開発統合ブランチ
│   ├── feature/xxx   # 機能開発
│   ├── bugfix/xxx    # バグ修正
│   └── hotfix/xxx    # 緊急修正
```

## 貢献の流れ

### 1. Issueを作成または確認

- 新機能: [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) テンプレートを使用
- バグ報告: [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) テンプレートを使用
- ユーザーストーリー: [User Story](.github/ISSUE_TEMPLATE/user_story.md) テンプレートを使用

### 2. ブランチを作成

```bash
# developから最新を取得
git checkout develop
git pull origin develop

# 機能ブランチを作成
git checkout -b feature/your-feature-name
```

### 3. TDDで開発

```
RED → GREEN → REFACTOR
```

1. **RED**: 失敗するテストを先に書く
2. **GREEN**: テストを通す最小限の実装
3. **REFACTOR**: コードを改善（テストは通ったまま）

```bash
# テストを実行
pytest tests/
# または
npm test
```

### 4. Quality Gateを確認

コミット前に以下を確認：

```bash
# Python
pytest --cov --cov-fail-under=80   # テスト＆カバレッジ
ruff check .                        # リント
ruff format --check .               # フォーマット
mypy .                              # 型チェック
bandit -r src/                      # セキュリティ

# JavaScript
npm test -- --coverage
npm run lint
npm run format:check
npm run typecheck
```

または、pre-commitで自動チェック：

```bash
pre-commit run --all-files
```

### 5. コミット

```bash
git add <files>
git commit -m "feat: 機能の説明

- 変更点1
- 変更点2

Quality Gate: PASS"
```

#### コミットメッセージ規約

```
<type>: <description>

[optional body]

[optional footer]
```

**Type:**
- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメント
- `style`: フォーマット
- `refactor`: リファクタリング
- `test`: テスト
- `chore`: その他

### 6. プルリクエスト

```bash
git push origin feature/your-feature-name
```

GitHubでPRを作成し、[PRテンプレート](.github/PULL_REQUEST_TEMPLATE.md)に従って記入。

### 7. レビュー対応

- レビューコメントに対応
- 必要に応じて修正
- 全てのQuality Gateを通過

## Quality Gate 基準

| Gate | 項目 | 基準 |
|------|------|------|
| 1 | テスト | 全て通過、カバレッジ80%以上 |
| 2 | コード品質 | リント/型エラー0件 |
| 3 | セキュリティ | Critical脆弱性0件 |
| 4 | レビュー | 2名以上の承認 |
| 5 | ドキュメント | スキーマ検証通過 |

## 新機能の場合

新機能を追加する場合は、以下のドキュメントも作成/更新してください：

1. **PRD** (`docs/prd.json`) - 要件定義
2. **SRS** (`docs/srs.json`) - 詳細仕様
3. **Test Spec** (`docs/test-spec.json`) - テスト仕様

スキーマ検証：

```bash
python scripts/validate-documents.py \
  --prd docs/prd.json \
  --srs docs/srs.json \
  --test docs/test-spec.json \
  --traceability
```

## ヘルプ

- 質問: Issueで質問を作成
- ドキュメント: [CLAUDE.md](CLAUDE.md)を参照
- ガイドライン:
  - [スクラム](docs/scrum/README.md)
  - [TDD](docs/tdd/README.md)
  - [Quality Gate](docs/quality-gate/README.md)

## 行動規範

- 相互尊重
- 建設的なフィードバック
- インクルーシブなコミュニティ

ありがとうございます！
