# スクラムセレモニー

## 概要

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SPRINT CEREMONIES                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Sprint        Daily         Sprint        Sprint                   │
│  Planning  →  Standup   →   Review    →  Retrospective             │
│                                                                     │
│  スプリント    毎日         スプリント    スプリント                │
│  開始時       15分         終了時        終了後                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 1. Sprint Planning（スプリント計画）

### 目的
スプリントで何を達成するかを決定する。

### タイミング
スプリント開始時

### 時間
2〜4時間（2週間スプリントの場合）

### 参加者
- Product Owner
- Development Team
- Scrum Master

### アジェンダ

```markdown
1. 【30分】スプリントゴール設定
   - Product Ownerが優先事項を説明
   - チームでゴールを合意

2. 【1時間】What - 何を作るか
   - Product Backlogからストーリー選択
   - Acceptance Criteria確認

3. 【1.5時間】How - どう作るか
   - タスク分解
   - 見積もり
   - Sprint Backlog作成

4. 【30分】コミットメント
   - チームがスプリントにコミット
   - 質問・懸念の解消
```

### アウトプット
- Sprint Goal
- Sprint Backlog

---

## 2. Daily Standup（デイリースタンドアップ）

### 目的
進捗を共有し、障害を早期発見する。

### タイミング
毎日同じ時間

### 時間
15分以内

### 参加者
- Development Team（必須）
- Scrum Master（任意）
- Product Owner（任意）

### 形式

各メンバーが3つの質問に答える：

```markdown
1. 昨日やったこと
   「US-1のバリデーションテストを作成し、実装を完了した」

2. 今日やること
   「US-1の登録APIのテストと実装に取り組む」

3. 障害・課題
   「メール送信のライブラリ選定で悩んでいる」
```

### ルール
- 15分厳守
- 立って行う（長引き防止）
- 詳細な議論は後で個別に

---

## 3. Sprint Review（スプリントレビュー）

### 目的
成果物をデモし、フィードバックを得る。

### タイミング
スプリント終了時

### 時間
1〜2時間

### 参加者
- Scrum Team全員
- ステークホルダー

### アジェンダ

```markdown
1. 【10分】スプリント概要
   - スプリントゴールの振り返り
   - 完了/未完了ストーリー

2. 【45分】デモ
   - 動作する成果物のデモ
   - 各機能の説明

3. 【30分】フィードバック
   - ステークホルダーからの意見
   - 改善提案

4. 【15分】バックログ更新
   - 新しいストーリーの追加
   - 優先度の見直し
```

### Quality Gate確認

Sprint Review前にQuality Gateを通過していること：

```markdown
## Quality Gate Status

| Gate | 項目 | 結果 |
|------|------|------|
| 1 | テストカバレッジ ≥80% | ✅ 85% |
| 2 | リントエラー 0件 | ✅ Pass |
| 3 | セキュリティスキャン | ✅ No Critical |
| 4 | コードレビュー承認 | ✅ 2/2 |

**Status: ALL GATES PASSED** ✅
```

---

## 4. Sprint Retrospective（スプリントレトロスペクティブ）

### 目的
プロセスを振り返り、改善する。

### タイミング
Sprint Review後

### 時間
1〜1.5時間

### 参加者
- Development Team
- Scrum Master
- Product Owner（任意）

### 形式：KPT

```markdown
## Keep（続けること）
- TDDで進めたことでバグが少なかった
- 毎日のスタンドアップで障害を早期発見できた
- Quality Gateのおかげで品質が安定した

## Problem（問題点）
- 見積もりが甘く、2ストーリー残った
- テスト作成に時間がかかりすぎた
- ドキュメントの更新が遅れた

## Try（試すこと）
- 見積もり時にバッファを20%追加
- テストのテンプレートを作成
- ストーリー完了時にドキュメントも更新
```

### 形式：Start/Stop/Continue

```markdown
## Start（始めること）
- ペアプログラミングを週1回実施
- 技術的負債の棚卸しを毎スプリント実施

## Stop（やめること）
- 完璧を求めすぎてリリースが遅れること
- スタンドアップでの長い議論

## Continue（続けること）
- TDDによる開発
- Quality Gate運用
```

### アクションアイテム

```markdown
## Action Items for Sprint 4

| # | アクション | 担当 | 期限 |
|---|-----------|------|------|
| 1 | テストテンプレート作成 | Alice | Sprint 4 Day 2 |
| 2 | 見積もりガイドライン更新 | Bob | Sprint 4 Day 1 |
| 3 | ペアプロスケジュール設定 | Charlie | Sprint 4 Day 1 |
```

---

## Claude Codeとのセレモニー

### Claude Codeとの「Sprint Planning」

```markdown
User: 「来週のスプリントで、検索機能とお気に入り機能を実装したい」

Claude:
1. 各機能のAcceptance Criteria確認
2. タスク分解提案
3. 優先順位の確認
4. TodoWriteでSprintBacklog作成
```

### Claude Codeとの「Daily Standup」

```markdown
User: 「今日の進捗は？」

Claude:
1. 完了タスクの報告
2. 現在取り組み中のタスク
3. 障害・課題があれば報告
```

### Claude Codeとの「Sprint Review」

```markdown
User: 「今週の成果を見せて」

Claude:
1. 完了した機能のリスト
2. コード変更の概要
3. テストカバレッジ報告
4. Quality Gate通過状況
```

### Claude Codeとの「Retrospective」

```markdown
User: 「今回のスプリントの振り返りをしよう」

Claude:
1. うまくいったことの分析
2. 問題点の特定
3. 改善提案
```
