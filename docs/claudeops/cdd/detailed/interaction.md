# インタラクション: プロンプト技法と学習モード

> Tips #6, #10 の詳細

## 1. プロンプト技法

### 基本姿勢

**Claudeを「実行者」ではなく「協働者」として扱う**

### テクニック一覧

#### a. レビュアーとして使う

```bash
# 厳格なレビュー
> Grill me on these changes and don't make a PR until I pass your test

# コードレビュー
> Review this PR as a senior engineer. Be critical.

# セキュリティレビュー
> Review this code for security vulnerabilities. Assume I'm a junior developer.
```

#### b. 証明を求める

```bash
# 動作の証明
> Prove to me this works
# → Claudeがmainとfeature branchの動作を比較

# 正当性の説明
> Explain why this approach is better than the alternative

# エッジケースの確認
> What edge cases could break this implementation?
```

#### c. 挑戦させる

```bash
# 再試行
> You can do better, try again

# 代替案
> What's another way to solve this?

# 批判的思考
> What are the downsides of this approach?
```

#### d. 役割を与える

```bash
# Staff Engineer
> As a staff engineer, review this architecture decision

# Security Expert
> As a security expert, audit this authentication flow

# Performance Engineer
> As a performance engineer, identify bottlenecks in this code
```

### プロンプトのアンチパターン

```bash
# Bad: 手順を細かく指示
> Open file X, go to line Y, change Z to W, then save

# Good: 目的を伝える
> The login is failing for users with special characters. Fix it.

# Bad: 曖昧な指示
> Make this better

# Good: 具体的な改善点
> Reduce the complexity of this function, it's hard to test
```

---

## 2. 品質向上のループ

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│     最初の結果                                          │
│          ↓                                              │
│     [期待以下?]─────Yes────→ "try again" / フィードバック│
│          │                          ↓                   │
│          No                    改善版を受け取る         │
│          ↓                          ↓                   │
│     レビュー要求              [期待以下?]──Yes──→ (ループ)
│          ↓                          │                   │
│     批判的フィードバック            No                  │
│          ↓                          ↓                   │
│     最終版                     採用                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 3. 学習モード

### Explanatory / Learning 出力スタイル

```bash
> /config
# Output style: Explanatory または Learning を選択
```

**通常モード:**
```
Here's the fix:
[コード変更]
```

**Explanatory モード:**
```
Here's the fix:
[コード変更]

Why this works:
- The original code assumed X, but Y can happen when...
- By adding the null check, we prevent...
- This pattern is called "defensive programming" because...
```

### HTMLプレゼンテーション生成

```bash
> Create an HTML presentation explaining how our authentication system works.
> Include diagrams and make it suitable for a new team member.
```

出力例:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Authentication System Overview</title>
  <style>
    /* インタラクティブなスライド形式 */
  </style>
</head>
<body>
  <section class="slide">
    <h1>Authentication Flow</h1>
    <svg><!-- フロー図 --></svg>
  </section>
  ...
</body>
</html>
```

### 学習目的のプロンプト

```bash
# 概念の説明
> Explain the repository pattern to me like I'm a junior developer

# 比較
> Compare Redux and Zustand. When should I use each?

# ベストプラクティス
> What are the best practices for error handling in this codebase?

# 歴史的経緯
> Why was this architecture chosen? What were the alternatives?
```

---

## 4. Second Claude パターン（応用）

### 計画のレビュー

```bash
# Terminal 1
> /plan
> Design a caching system

# Terminal 2
> Review this plan as a staff engineer: [plan]
> Rate it 1-10 and explain your reasoning
```

### コードのレビュー

```bash
# Terminal 1
> Implement feature X
# → PRを作成

# Terminal 2
> Review this PR: [diff]
> What would you change?
```

### 議論のシミュレーション

```bash
# 異なる視点からの検討
> Terminal 1: Argue for using microservices
> Terminal 2: Argue for using a monolith
> Human: 両方の意見を比較して決定
```

---

## 関連

- [Claude Code Configuration](https://docs.anthropic.com/claude-code/config)
- [Effective Prompting](https://docs.anthropic.com/prompting)
