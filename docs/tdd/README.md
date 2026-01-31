# TDD（テスト駆動開発）ワークフロー

## 概要

TDD（Test-Driven Development）は、テストを先に書いてから実装を行う開発手法です。

```
┌─────────────────────────────────────────────────────────────────────┐
│                         TDD CYCLE                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│         ┌─────────┐                                                │
│         │   RED   │ ← 失敗するテストを書く                         │
│         └────┬────┘                                                │
│              ↓                                                      │
│         ┌─────────┐                                                │
│         │  GREEN  │ ← テストを通す最小限の実装                     │
│         └────┬────┘                                                │
│              ↓                                                      │
│         ┌──────────┐                                               │
│         │ REFACTOR │ ← コードを改善（テストは通ったまま）          │
│         └────┬─────┘                                               │
│              ↓                                                      │
│         次のテストへ                                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## TDDの原則

### Three Laws of TDD

1. **失敗するテストを書くまで、プロダクションコードを書いてはいけない**
2. **失敗させるのに必要な分だけテストを書く（コンパイルエラーも失敗）**
3. **現在失敗しているテストを通すのに必要な分だけプロダクションコードを書く**

### Red-Green-Refactorサイクル

詳細は [red-green-refactor.md](red-green-refactor.md) を参照。

## TDDのメリット

| メリット | 説明 |
|---------|------|
| バグの早期発見 | テストが先にあるため、実装時にバグを発見しやすい |
| 設計の改善 | テスタブルなコードを書く必要があり、結果として良い設計になる |
| 仕様の明確化 | テストが仕様書として機能する |
| リファクタリングの安全性 | テストがあるため、安心してリファクタリングできる |
| ドキュメント | テストがコードの使い方を示す |

## TDDの実践

### ステップ1: テストリスト作成

実装する機能に対して、必要なテストケースをリストアップ。

```markdown
## ユーザー登録機能のテストリスト

1. 正常系
   - [ ] 有効なメールとパスワードで登録できる
   - [ ] 登録後にユーザーIDが返される

2. バリデーション
   - [ ] メールが空の場合エラー
   - [ ] メール形式が不正な場合エラー
   - [ ] パスワードが8文字未満の場合エラー
   - [ ] パスワードが空の場合エラー

3. 重複チェック
   - [ ] 既存メールで登録しようとするとエラー
```

### ステップ2: 最初のテストを書く（RED）

```python
# test_user_registration.py

def test_register_user_with_valid_email_and_password():
    """有効なメールとパスワードで登録できる"""
    # Arrange
    email = "test@example.com"
    password = "securepass123"

    # Act
    result = register_user(email, password)

    # Assert
    assert result.success is True
    assert result.user_id is not None
```

実行すると失敗する（`register_user`が存在しない）。

### ステップ3: テストを通す実装（GREEN）

```python
# user_service.py

from dataclasses import dataclass

@dataclass
class RegistrationResult:
    success: bool
    user_id: str | None = None

def register_user(email: str, password: str) -> RegistrationResult:
    # 最小限の実装
    return RegistrationResult(success=True, user_id="user_123")
```

テストが通る。

### ステップ4: リファクタリング（REFACTOR）

```python
# user_service.py

from dataclasses import dataclass
from uuid import uuid4

@dataclass
class RegistrationResult:
    success: bool
    user_id: str | None = None
    error: str | None = None

def register_user(email: str, password: str) -> RegistrationResult:
    """ユーザーを登録する"""
    user_id = str(uuid4())
    return RegistrationResult(success=True, user_id=user_id)
```

テストは引き続き通る。

### ステップ5: 次のテストへ

```python
def test_register_user_with_empty_email_fails():
    """メールが空の場合エラー"""
    result = register_user("", "securepass123")

    assert result.success is False
    assert result.error == "Email is required"
```

このサイクルを繰り返す。

## テストの種類

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TEST PYRAMID                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                          /\                                         │
│                         /  \                                        │
│                        / E2E \      ← 少数（遅い、高コスト）        │
│                       /      \                                      │
│                      /────────\                                     │
│                     /Integration\   ← 中程度                        │
│                    /            \                                   │
│                   /──────────────\                                  │
│                  /    Unit Tests   \  ← 多数（速い、低コスト）      │
│                 /                    \                              │
│                /______________________\                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Unit Test（単体テスト）

- 1つの関数/クラスをテスト
- 外部依存はモック化
- 高速で多数実行

```python
def test_validate_email_with_valid_email():
    assert validate_email("test@example.com") is True

def test_validate_email_with_invalid_email():
    assert validate_email("invalid") is False
```

### Integration Test（統合テスト）

- 複数のコンポーネントを組み合わせてテスト
- データベースやAPIとの連携を確認

```python
def test_user_registration_saves_to_database():
    # Arrange
    db = get_test_database()
    service = UserService(db)

    # Act
    result = service.register("test@example.com", "password123")

    # Assert
    user = db.find_user_by_email("test@example.com")
    assert user is not None
    assert user.id == result.user_id
```

### E2E Test（End-to-Endテスト）

- システム全体をユーザー視点でテスト
- 実際のブラウザや環境を使用

```python
def test_user_can_register_via_ui():
    # Arrange
    browser.navigate("/register")

    # Act
    browser.fill("email", "test@example.com")
    browser.fill("password", "password123")
    browser.click("submit")

    # Assert
    assert browser.current_url == "/dashboard"
    assert browser.contains_text("Welcome, test@example.com")
```

## Claude CodeでのTDD

### 基本フロー

```markdown
1. ユーザーストーリーを受け取る
2. テストリストを作成
3. TodoWriteでタスク管理
4. RED-GREEN-REFACTORサイクル実行
5. Quality Gateチェック
6. コミット
```

### 例

```markdown
User: 「メールアドレスのバリデーション機能を追加して」

Claude:
1. テストリスト作成
   - 正常なメールアドレスの検証
   - 空文字のエラー
   - @なしのエラー
   - ドメインなしのエラー

2. RED: 最初のテストを書く
   ```python
   def test_valid_email():
       assert validate_email("test@example.com") is True
   ```

3. GREEN: 最小限の実装
   ```python
   def validate_email(email: str) -> bool:
       return "@" in email and "." in email
   ```

4. REFACTOR: コード改善
   ```python
   import re

   EMAIL_PATTERN = re.compile(r'^[^@]+@[^@]+\.[^@]+$')

   def validate_email(email: str) -> bool:
       return bool(EMAIL_PATTERN.match(email))
   ```

5. 次のテストへ...
```

## テスト品質の指標

| 指標 | 目標 | 説明 |
|------|------|------|
| カバレッジ | ≥ 80% | コードのテストされている割合 |
| ミューテーションスコア | ≥ 70% | テストがバグを検出できる割合 |
| テスト実行時間 | < 5分 | 高速なフィードバックループ |

## アンチパターン

### 避けるべきこと

1. **テストなしの実装** - 必ずテストを先に
2. **複数機能を一度にテスト** - 1テスト1機能
3. **実装詳細のテスト** - 振る舞いをテスト
4. **脆いテスト** - 実装変更で壊れないテスト
5. **遅いテスト** - モックを活用して高速化

## 関連ドキュメント

- [Red-Green-Refactor詳細](red-green-refactor.md)
- [スクラムとの統合](../scrum/README.md)
- [Quality Gate基準](../quality-gate/README.md)
