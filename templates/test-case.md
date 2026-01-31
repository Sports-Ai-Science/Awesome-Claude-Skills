# Test Case Template

## テストケース基本構造

### AAA パターン（Arrange-Act-Assert）

```python
def test_[機能]_[条件]_[期待結果]():
    """[テストの説明]"""
    # Arrange: 前提条件のセットアップ
    input_data = create_test_data()

    # Act: テスト対象の実行
    result = function_under_test(input_data)

    # Assert: 結果の検証
    assert result == expected_value
```

---

## 命名規則

```
test_[テスト対象]_[条件/状況]_[期待される結果]

例：
- test_validate_email_with_valid_email_returns_true
- test_register_user_with_duplicate_email_raises_error
- test_calculate_total_with_discount_applies_correctly
```

---

## テストケーステンプレート

### 単体テスト（Unit Test）

```python
import pytest
from module import function_to_test

class TestFunctionName:
    """function_to_testのテスト"""

    # ========== 正常系 ==========

    def test_normal_case_returns_expected_result(self):
        """正常なケースで期待通りの結果を返す"""
        # Arrange
        input_value = "valid_input"

        # Act
        result = function_to_test(input_value)

        # Assert
        assert result.success is True
        assert result.value == "expected_output"

    # ========== 異常系 ==========

    def test_empty_input_raises_validation_error(self):
        """空の入力でValidationErrorが発生する"""
        # Arrange
        input_value = ""

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            function_to_test(input_value)

        assert "Input cannot be empty" in str(exc_info.value)

    def test_invalid_format_returns_error_result(self):
        """不正なフォーマットでエラー結果を返す"""
        # Arrange
        input_value = "invalid_format"

        # Act
        result = function_to_test(input_value)

        # Assert
        assert result.success is False
        assert result.error == "Invalid format"

    # ========== 境界値 ==========

    def test_minimum_valid_length_is_accepted(self):
        """最小有効長が受け入れられる"""
        # Arrange
        input_value = "abc"  # 最小長: 3

        # Act
        result = function_to_test(input_value)

        # Assert
        assert result.success is True

    def test_below_minimum_length_is_rejected(self):
        """最小長未満は拒否される"""
        # Arrange
        input_value = "ab"  # 最小長 - 1

        # Act
        result = function_to_test(input_value)

        # Assert
        assert result.success is False
```

### 統合テスト（Integration Test）

```python
import pytest
from database import Database
from service import UserService

class TestUserServiceIntegration:
    """UserServiceの統合テスト"""

    @pytest.fixture
    def db(self):
        """テスト用データベース"""
        database = Database.create_test_instance()
        yield database
        database.cleanup()

    @pytest.fixture
    def service(self, db):
        """テスト用サービス"""
        return UserService(db)

    def test_register_user_saves_to_database(self, service, db):
        """ユーザー登録がデータベースに保存される"""
        # Arrange
        email = "test@example.com"
        password = "securepass123"

        # Act
        result = service.register(email, password)

        # Assert
        assert result.success is True
        saved_user = db.find_by_email(email)
        assert saved_user is not None
        assert saved_user.email == email
```

### パラメータ化テスト

```python
import pytest

class TestEmailValidation:

    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("user.name@domain.org", True),
        ("user+tag@example.com", True),
        ("", False),
        ("invalid", False),
        ("@example.com", False),
        ("user@", False),
        ("user@.com", False),
    ])
    def test_validate_email(self, email, expected):
        """様々なメールアドレスのバリデーション"""
        result = validate_email(email)
        assert result == expected
```

---

## テストチェックリスト

### 実装前に確認

- [ ] テスト対象の機能を理解しているか
- [ ] Acceptance Criteriaを確認したか
- [ ] 正常系・異常系・境界値を考慮したか

### テスト作成時

- [ ] テスト名は何をテストしているか明確か
- [ ] AAAパターンに従っているか
- [ ] 1テスト1アサーション（または関連アサーション）か
- [ ] テストは独立しているか（他のテストに依存しない）

### テスト作成後

- [ ] テストが失敗することを確認したか（RED）
- [ ] 最小限の実装でテストが通るか（GREEN）
- [ ] リファクタリング後もテストが通るか（REFACTOR）

---

## JavaScript/TypeScript版

```typescript
import { describe, it, expect, beforeEach } from 'vitest';
import { validateEmail } from './validator';

describe('validateEmail', () => {
  describe('正常系', () => {
    it('有効なメールアドレスでtrueを返す', () => {
      // Arrange
      const email = 'user@example.com';

      // Act
      const result = validateEmail(email);

      // Assert
      expect(result).toBe(true);
    });
  });

  describe('異常系', () => {
    it('空文字でfalseを返す', () => {
      expect(validateEmail('')).toBe(false);
    });

    it('@がない場合falseを返す', () => {
      expect(validateEmail('invalid')).toBe(false);
    });
  });

  describe('境界値', () => {
    it.each([
      ['user@example.com', true],
      ['a@b.co', true],
      ['', false],
      ['@', false],
    ])('"%s" の結果は %s', (email, expected) => {
      expect(validateEmail(email)).toBe(expected);
    });
  });
});
```
