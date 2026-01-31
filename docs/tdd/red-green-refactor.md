# Red-Green-Refactor サイクル

## 概要

TDDの核心となる3つのフェーズ。

```
┌─────────────────────────────────────────────────────────────────────┐
│                  RED - GREEN - REFACTOR                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │         ┌─────────┐                                    │     │
│    │         │   RED   │                                    │     │
│    │         │ テスト  │                                    │     │
│    │         │  失敗   │                                    │     │
│    │         └────┬────┘                                    │     │
│    │              │                                         │     │
│    │              ↓                                         │     │
│    │         ┌─────────┐                                    │     │
│    │         │  GREEN  │                                    │     │
│    │         │ テスト  │                                    │     │
│    │         │  成功   │                                    │     │
│    │         └────┬────┘                                    │     │
│    │              │                                         │     │
│    │              ↓                                         │     │
│    │         ┌──────────┐                                   │     │
│    │         │ REFACTOR │                                   │     │
│    │         │  改善    │                                   │     │
│    │         └────┬─────┘                                   │     │
│    │              │                                         │     │
│    │              └──────────────→ 次のテストへ             │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Phase 1: RED（赤）

### 目的
失敗するテストを書く。

### 手順

1. **1つの振る舞いに対するテストを書く**
2. **テストを実行して失敗を確認**
3. **失敗メッセージが意味のあるものか確認**

### 例：パスワードバリデーション

```python
# test_password_validator.py

import pytest
from password_validator import validate_password

class TestPasswordValidator:

    def test_valid_password_returns_true(self):
        """8文字以上のパスワードは有効"""
        result = validate_password("securepass123")
        assert result.is_valid is True

    def test_short_password_returns_error(self):
        """8文字未満のパスワードはエラー"""
        result = validate_password("short")
        assert result.is_valid is False
        assert result.error == "Password must be at least 8 characters"
```

### 実行結果（RED）

```
$ pytest test_password_validator.py

E   ModuleNotFoundError: No module named 'password_validator'

FAILED - 2 tests
```

### REDフェーズのルール

- テストは**1つの振る舞い**のみをテスト
- テスト名は**何をテストしているか明確に**
- **最小限のコード**で失敗を確認

---

## Phase 2: GREEN（緑）

### 目的
テストを通す最小限の実装を書く。

### 手順

1. **テストを通すための最小限のコードを書く**
2. **テストを実行して成功を確認**
3. **他のテストが壊れていないか確認**

### 例：最小限の実装

```python
# password_validator.py

from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    error: str | None = None

def validate_password(password: str) -> ValidationResult:
    if len(password) < 8:
        return ValidationResult(
            is_valid=False,
            error="Password must be at least 8 characters"
        )
    return ValidationResult(is_valid=True)
```

### 実行結果（GREEN）

```
$ pytest test_password_validator.py

test_password_validator.py::TestPasswordValidator::test_valid_password_returns_true PASSED
test_password_validator.py::TestPasswordValidator::test_short_password_returns_error PASSED

2 passed
```

### GREENフェーズのルール

- **最小限の実装**に留める（完璧を求めない）
- **ハードコード**でもOK（後でリファクタリング）
- **テストが通ることだけ**に集中

### 「最小限」の例

```python
# 極端な例：ハードコードで通す
def validate_password(password: str) -> ValidationResult:
    if password == "short":
        return ValidationResult(is_valid=False, error="...")
    return ValidationResult(is_valid=True)
```

これは技術的にはテストを通すが、次のテストを追加すると失敗する。
その時に一般化する。

---

## Phase 3: REFACTOR（リファクタリング）

### 目的
テストを通したまま、コードを改善する。

### 手順

1. **コードの重複を除去**
2. **命名の改善**
3. **構造の改善**
4. **テストを実行して緑のまま確認**

### 例：リファクタリング

```python
# password_validator.py

from dataclasses import dataclass
from typing import Final

MIN_PASSWORD_LENGTH: Final[int] = 8

@dataclass(frozen=True)
class ValidationResult:
    """パスワードバリデーションの結果"""
    is_valid: bool
    error: str | None = None

    @classmethod
    def success(cls) -> "ValidationResult":
        return cls(is_valid=True)

    @classmethod
    def failure(cls, error: str) -> "ValidationResult":
        return cls(is_valid=False, error=error)


def validate_password(password: str) -> ValidationResult:
    """
    パスワードをバリデーションする。

    Args:
        password: バリデーション対象のパスワード

    Returns:
        ValidationResult: バリデーション結果
    """
    if len(password) < MIN_PASSWORD_LENGTH:
        return ValidationResult.failure(
            f"Password must be at least {MIN_PASSWORD_LENGTH} characters"
        )
    return ValidationResult.success()
```

### 実行結果（GREEN維持）

```
$ pytest test_password_validator.py

2 passed
```

### REFACTORフェーズのルール

- **テストが緑のまま**であることを確認しながら
- **小さなステップ**で改善
- **新機能は追加しない**（REDフェーズで）
- **設計の改善に集中**

### リファクタリングのチェックリスト

- [ ] 重複コードがないか
- [ ] 命名は適切か
- [ ] 関数/クラスの責務は単一か
- [ ] マジックナンバーは定数化されているか
- [ ] ネストが深すぎないか
- [ ] テストコードもリファクタリング対象

---

## 完全なサイクル例

### 要件
ユーザー名バリデーション：3-20文字、英数字とアンダースコアのみ

### Iteration 1

**RED:**
```python
def test_valid_username():
    assert validate_username("john_doe").is_valid is True
```

**GREEN:**
```python
def validate_username(username: str) -> ValidationResult:
    return ValidationResult(is_valid=True)
```

**REFACTOR:** なし（シンプルすぎる）

### Iteration 2

**RED:**
```python
def test_username_too_short():
    result = validate_username("ab")
    assert result.is_valid is False
    assert "at least 3 characters" in result.error
```

**GREEN:**
```python
def validate_username(username: str) -> ValidationResult:
    if len(username) < 3:
        return ValidationResult(
            is_valid=False,
            error="Username must be at least 3 characters"
        )
    return ValidationResult(is_valid=True)
```

**REFACTOR:**
```python
MIN_LENGTH = 3

def validate_username(username: str) -> ValidationResult:
    if len(username) < MIN_LENGTH:
        return ValidationResult.failure(
            f"Username must be at least {MIN_LENGTH} characters"
        )
    return ValidationResult.success()
```

### Iteration 3

**RED:**
```python
def test_username_too_long():
    result = validate_username("a" * 21)
    assert result.is_valid is False
```

**GREEN:**
```python
MIN_LENGTH = 3
MAX_LENGTH = 20

def validate_username(username: str) -> ValidationResult:
    if len(username) < MIN_LENGTH:
        return ValidationResult.failure(...)
    if len(username) > MAX_LENGTH:
        return ValidationResult.failure(
            f"Username must be at most {MAX_LENGTH} characters"
        )
    return ValidationResult.success()
```

**REFACTOR:**
```python
def validate_username(username: str) -> ValidationResult:
    if not (MIN_LENGTH <= len(username) <= MAX_LENGTH):
        return ValidationResult.failure(
            f"Username must be between {MIN_LENGTH} and {MAX_LENGTH} characters"
        )
    return ValidationResult.success()
```

### Iteration 4

**RED:**
```python
def test_username_with_invalid_characters():
    result = validate_username("john@doe")
    assert result.is_valid is False
```

**GREEN & REFACTOR:**
```python
import re

USERNAME_PATTERN = re.compile(r'^[a-zA-Z0-9_]+$')

def validate_username(username: str) -> ValidationResult:
    if not (MIN_LENGTH <= len(username) <= MAX_LENGTH):
        return ValidationResult.failure(...)

    if not USERNAME_PATTERN.match(username):
        return ValidationResult.failure(
            "Username can only contain letters, numbers, and underscores"
        )

    return ValidationResult.success()
```

---

## よくある質問

### Q: REDフェーズでどこまでテストを書くべき？

**A:** 1つの振る舞いに対して1つのテスト。複数の失敗するテストを一度に書かない。

### Q: GREENフェーズでどこまで実装すべき？

**A:** テストが通る最小限。「将来必要になるかも」の実装はしない。

### Q: REFACTORはいつスキップしていい？

**A:** コードがすでに十分クリーンな場合。ただし、毎回立ち止まって考える習慣は大切。

### Q: テストコードもリファクタリングする？

**A:** はい。テストも保守対象のコード。重複除去やヘルパー関数の抽出を行う。

---

## Claude Codeでの実践

```markdown
## リクエスト例
「メールアドレスのバリデーション機能を追加して」

## Claude の対応

### 1. テストリスト作成
- 正常なメールアドレス → 有効
- 空文字 → 無効
- @なし → 無効
- ドメインなし → 無効

### 2. Iteration 1 (RED)
テストを書く:
```python
def test_valid_email():
    assert validate_email("user@example.com").is_valid is True
```

実行 → 失敗確認

### 3. Iteration 1 (GREEN)
最小限の実装:
```python
def validate_email(email):
    return ValidationResult(is_valid=True)
```

実行 → 成功確認

### 4. Iteration 2 (RED)
次のテスト:
```python
def test_empty_email():
    result = validate_email("")
    assert result.is_valid is False
```

### 5. 繰り返し...

### 6. Quality Gate
全テスト通過 → カバレッジ確認 → コミット
```
