# Pull Request Template

## Summary

<!-- 変更内容の概要を1-3文で説明 -->

## Related Issues

<!-- 関連するIssue/User Story -->
- Closes #XXX
- Related to #YYY

## Changes

<!-- 変更内容のリスト -->
- [ ] 変更点1
- [ ] 変更点2
- [ ] 変更点3

## Type of Change

<!-- 該当するものにチェック -->
- [ ] 🐛 Bug fix（バグ修正）
- [ ] ✨ New feature（新機能）
- [ ] 🔧 Enhancement（機能改善）
- [ ] 📝 Documentation（ドキュメント）
- [ ] ♻️ Refactoring（リファクタリング）
- [ ] 🧪 Test（テスト追加・修正）
- [ ] 🔒 Security（セキュリティ）

## Quality Gate Checklist

### Gate 1: Tests
- [ ] 全てのテストが通過
- [ ] カバレッジ ≥ 80%
- [ ] 新機能にテストを追加

### Gate 2: Code Quality
- [ ] リントエラー 0件
- [ ] フォーマットチェック通過
- [ ] 型エラー 0件

### Gate 3: Security
- [ ] セキュリティスキャン通過
- [ ] 依存関係の脆弱性チェック通過
- [ ] シークレット検出なし

### Gate 4: Review
- [ ] セルフレビュー完了
- [ ] レビュアー指定済み

## Test Plan

<!-- テスト方法を記述 -->

### 手動テスト手順
1. ...
2. ...
3. ...

### 自動テスト
```bash
# テスト実行コマンド
pytest tests/
npm test
```

## Screenshots/Recordings

<!-- UI変更がある場合は添付 -->

## Additional Notes

<!-- その他特記事項 -->

---

# Example

```markdown
## Summary

ユーザー登録機能を実装しました。メールアドレスとパスワードでの新規登録が可能になります。

## Related Issues

- Closes #42
- Related to #38 (認証基盤)

## Changes

- [x] ユーザーモデルの追加 (`models/user.py`)
- [x] バリデーションロジック (`validators/user_validator.py`)
- [x] 登録APIエンドポイント (`api/auth.py`)
- [x] ユニットテスト追加 (`tests/test_user_registration.py`)
- [x] 統合テスト追加 (`tests/integration/test_auth_api.py`)

## Type of Change

- [ ] 🐛 Bug fix
- [x] ✨ New feature
- [ ] 🔧 Enhancement
- [ ] 📝 Documentation
- [ ] ♻️ Refactoring
- [ ] 🧪 Test
- [ ] 🔒 Security

## Quality Gate Checklist

### Gate 1: Tests
- [x] 全てのテストが通過
- [x] カバレッジ 87% (≥ 80%)
- [x] 新機能にテストを追加

### Gate 2: Code Quality
- [x] リントエラー 0件
- [x] フォーマットチェック通過
- [x] 型エラー 0件

### Gate 3: Security
- [x] セキュリティスキャン通過
- [x] 依存関係の脆弱性チェック通過
- [x] シークレット検出なし

### Gate 4: Review
- [x] セルフレビュー完了
- [x] レビュアー指定済み

## Test Plan

### 手動テスト手順
1. POST `/api/auth/register` に有効なデータを送信
2. レスポンスで `user_id` が返ることを確認
3. 同じメールで再度登録しようとしてエラーを確認

### 自動テスト
```bash
pytest tests/test_user_registration.py -v
pytest tests/integration/test_auth_api.py -v
```

## Coverage Report

```
tests/test_user_registration.py   100%
validators/user_validator.py       95%
api/auth.py                        82%
models/user.py                     90%
----------------------------------------
TOTAL                              87%
```

## Additional Notes

- パスワードはbcryptでハッシュ化
- メール送信機能は次のPRで実装予定
```
