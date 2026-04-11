# ASCENT LP SKILL — デザイン＆コピー完全仕様書
> このファイルを読めば、LPの更新・新セクション追加・コピー生成が即座にできる。

---

## 1. デザイントークン

### 1-1. カラーパレット

| 用途 | 変数名 | HEX / RGBA |
|------|--------|------------|
| 背景（メイン） | `--bg` | `#050507` |
| 背景（ライト） | `--bg-light` | `#F5F0E8` |
| ゴールド（メイン） | `--gold` | `#C9A84C` |
| ゴールド（ライト） | `--gold-light` | `#e0c070` |
| ゴールド（ダーク） | `--gold-dark` | `#9a7a2e` |
| テキスト（メイン） | `--text` | `#F5F0E8` |
| テキスト（ダーク面） | `--text-dark` | `#1a1a1a` |
| テキスト（ミュート） | `--text-muted` | `rgba(245,240,232,0.55)` |
| ボーダー | `--border` | `rgba(201,168,76,0.25)` |

**追加で使われる色:**
- カード背景: `#13131F`, `#0A0A14`, `#0F0F19`
- セクションダーク背景上のラベル: `#8a6a20`（ゴールドダーク on ライト面）
- ゴースト文字: `rgba(255,255,255,0.03)` / `rgba(0,0,0,0.025)`
- ポジションカードボーダー: `rgba(99,110,250,0.4)`（インディゴ）
- フッター背景: `#030305`
- 固定CTA背景: `rgba(15,15,25,0.96)`

### 1-2. フォント

| 用途 | ファミリー | ウェイト | サイズ範囲 |
|------|-----------|---------|-----------|
| 本文 | `Noto Serif JP` | 300, 400, 500, 700, 900 | 12–15px |
| 見出し・ラベル・ボタン | `Cinzel` | 400, 600, 700 | 9–18px |
| 数字アクセント | `Cormorant Garamond` | 300, 400, 600 (italic含む) | 14–52px |

**フォントサイズ体系:**
- ゴーストテキスト: `clamp(28px, 9vw, 48px)` — Cinzel 700
- セクション見出し: `clamp(22px, 6vw, 30px)` — 700
- FV価格（¥0）: `clamp(60px, 11vw, 90px)` — 900
- FVラベル: `clamp(22px, 3.5vw, 36px)` — 700
- セクションタイトルv7: `22px` — 700
- カード内タイトル: `15–18px` — 700
- 本文: `13–14px` — 400, line-height: 1.75–2.0
- ラベル・バッジ: `9–11px` — 600/700, letter-spacing: 0.2–0.35em
- 注釈: `11–12px` — 400

### 1-3. 余白ルール

| 要素 | 値 |
|------|-----|
| セクションpadding | `96px 24px`（`--section-pad`） |
| v7セクションpadding | `64px 20px` |
| カード内padding | `20–28px` |
| カード間gap | `2px`（タイト結合） |
| セクション間余白 | 0（セクション同士は隙間なし） |
| ラベル → 見出し | `10–28px` |
| 見出し → コンテンツ | `32–48px` |
| CTA前後 | `padding: 40px 20px 48px` |

### 1-4. 角丸・シャドウ・ボーダー

| 要素 | 値 |
|------|-----|
| ステップカード | `border-radius: 12px` |
| ステップアイコン（丸） | `border-radius: 50%` |
| バッジ | `border-radius: 20px`（FVバッジのみ） |
| その他カード | `border-radius: なし（0）` |
| ボーダー厚 | `1px solid`（基本） / `1.5px`（ポジションカード） / `2px`（アクセント） |
| 固定CTAシャドウ | `box-shadow: 0 -4px 20px rgba(0,0,0,0.5)` |
| ゴールドグロー | `box-shadow: 0 0 8px rgba(201,168,76,0.6)` |

### 1-5. アニメーション

| 名前 | 値 | 用途 |
|------|-----|------|
| fadeUp | `opacity: 0 → 1, translateY(20px → 0)`, 0.7s ease | FV要素の初回表示 |
| fade-up-1〜5 | delay: 0.1s, 0.25s, 0.4s, 0.55s, 0.7s | FV内のスタガー |
| reveal | `opacity: 0 → 1, translateY(16px → 0)`, 0.6s ease | スクロール連動 |
| acc-body | `max-height: 0 → 400px`, 0.3s ease | アコーディオン開閉 |
| acc-icon | `rotate(0 → 45deg)`, 0.25s | ＋アイコン回転 |
| fixed-cta | `translateY(110% → 0)`, 0.3s ease | 固定CTA出現 |
| btn hover | `opacity: 0.85`, 0.2s | ボタンホバー |

---

## 2. セクション構成

| # | セクション名 | クラス/ID | 背景 | 役割 |
|---|-------------|----------|------|------|
| 1 | Announcement Bar | `.announcement-bar` | `#0d0d0d` | リスクリバーサル（返金保証） |
| 2 | Hero / FV | `.hero` | `#000` | ¥0訴求・最初のCTA |
| 3 | あなたのことですか？ | `.empathy-section` | `#0A0A14` | 共感・ターゲット絞り込み |
| 4 | Hero's Journey | `.hero-journey` | `#050507` | 創業者ストーリー・信頼構築 |
| 5 | Problem | `.section-light` | `#F5F0E8` | 痛みの言語化（4つの症状→原因） |
| 6 | Root Cause / 3指標 | `.indicators` #indicators | `#050507` | 01/02/03で根本原因を提示 |
| 7 | Solution | `.section-dark` | `#050507` | 3本柱（AI・PRO・AUTO） |
| 8 | CTA② | `.section-cta` | `#050507` | 「3指標を測ってみますか？」 |
| 9 | How It Works | `.how-it-works-v7` #how-it-works | `#0A0A14` | 3ステップ＋診断の声 |
| 10 | CTA③ | `.section-cta` | — | 「同じ結果を、あなたにも」 |
| 11 | Value Stack | `.value-stack` | `#0A0A14` | 価値の可視化（¥9,920→¥4,980） |
| 12 | Plans | `.section-dark` | `#050507` | 3プラン比較 |
| 13 | CTA④ | `.section-cta` | `#050507` | 「7日間リスクゼロ」 |
| 14 | Stage Design | `.section-light` | `#F5F0E8` | 感情設計の旅（Phase0〜Stage3） |
| 15 | Credibility | `.credibility` | `#050507` | 創業者プロフィール・実績 |
| 16 | For Parents | `.parent-section` | — | 保護者向け反論処理 |
| 17 | Position Select | `.position-select` | `#13131F` | ポジション別LINE誘導 |
| 18 | FAQ | `.faq-section` | — | 5つの反論処理 |
| 19 | CTA⑤ | `.section-cta` | `#0A0A14` | 「不安が消えたなら行動だけ」 |
| 20 | Final CTA | `.narrow-section` | — | 限定オファー＋リスクリバーサル |
| 21 | Footer | `footer` | `#030305` | ロゴ・リンク・著作権 |
| 22 | 特商法 | `.tokushoho` #tokushoho | `#050507` | 法的表示 |
| 23 | 固定CTA | `.fixed-cta` #fixedCta | 半透明 | スクロール追従CTA |

---

## 3. コピールール

### 3-1. トーン＆ボイス

| 場面 | トーン | 語尾 | 一人称 |
|------|--------|------|--------|
| 創業者の声 | 親しみ＋権威 | 〜した。〜だ。 | 俺 |
| サービス説明 | 丁寧・論理的 | 〜です。〜ます。 | — |
| ユーザーの声 | カジュアル | 〜だよ！〜です！ | 自分 |
| CTA周辺 | 寄り添い | 〜してみてください | — |
| FAQ回答 | 丁寧語で統一 | 〜です。〜ます。 | — |

### 3-2. コピーの型

**見出し:** 短く断定。句読点で切る。`感覚じゃなく、構造で直す。`
**サブコピー:** 1文15–25字。2行以内。
**CTA文脈テキスト:** 問いかけ or 共感。13px、ミュートカラー。
**CTAボタン:** 動詞始まり。「今すぐ無料で〜する」形式。

### 3-3. 禁止表現

| 禁止 | 理由 | 代替 |
|------|------|------|
| 命令形（〜してください） | 圧迫感 | 〜できます / 〜してみてください |
| 世界一・絶対・必ず | 景品表示法 | 具体的数値で示す |
| 期限なし限定（今だけ・先着） | 根拠なき緊急性 | 根拠がある場合のみ使用可 |
| Kaitが診断 / Kaitが直接 | 属人的すぎる表現を削除済み | AIが骨格を解析 |
| 〜だよ（FAQ・説明文内） | トーン不統一 | 〜です に統一 |
| 24時間以内 / 48時間以内 | コミットメント不履行リスク | 削除済み |

### 3-4. ターゲット設定

**プライマリ:** 中高生バスケ選手（12–18歳）
- シュートが入らない悩み
- 感覚的指導への不信感
- データ・数値への親和性

**セカンダリ:** 保護者
- 子供の上達への不安
- 費用対効果の判断
- 解約自由度の確認

**ターゲット分離ルール:** 1セクション内で中高生と保護者を同時に狙わない。FOR PARENTSセクションで分離。

---

## 4. コンポーネントパターン

### 4-1. ボタン

| 名前 | クラス | 背景 | 文字色 | フォント | 用途 |
|------|--------|------|--------|---------|------|
| プライマリ | `.btn-primary` | ゴールドグラデ | `#050507` | Cinzel 14px 700 | Stripe決済リンク |
| CTAメイン | `.btn-cta-main` | `#C9A84C` ソリッド | `#050507` | 本文 16px 700 | LINE誘導（主CTA） |
| CTAサブ | `.btn-cta-sub` | 透明 | `#F5F0E8` | 本文 15px 700 | 補助リンク |
| ゴースト | `.btn-ghost` | 透明 | `--gold` | Cinzel 13px | 非推奨プラン用 |
| 固定CTA | `.fixed-cta-btn` | `#C9A84C` | `#050507` | 本文 15px 700 | スクロール追従 |

### 4-2. カードパターン

| パターン | 背景 | ボーダー | 用途 |
|---------|------|---------|------|
| ダークカード | `rgba(255,255,255,0.03)` | `1px solid var(--border)` | Problem, Solution, Stage |
| ステップカード | `#13131F` | `1px solid rgba(201,168,76,0.25)` | HOW IT WORKS |
| プランカード | `rgba(255,255,255,0.03)` | `1px solid var(--border)` | LITE, PRO |
| プランカード(Featured) | `rgba(201,168,76,0.04)` | `rgba(201,168,76,0.6)` | UNLEASH |
| 声カード | `#13131F` | `border-left: 3px solid rgba(201,168,76,0.4)` | Empathy, Testimonial |
| ポジションカード | `#1C1C2E` | `1.5px solid rgba(99,110,250,0.4)` | Position Select |

### 4-3. セクションラベル

2種類:
1. **Cinzel横ライン付き** `.section-label` — 左揃え、右に線。ダーク面で使用。
2. **Eyebrow（中央寄せ）** `.section-eyebrow` — 9px、letter-spacing 0.3em。v7デザインで使用。

### 4-4. アコーディオン

```
.acc-item → .acc-trigger（ボタン）+ .acc-body（コンテンツ）
開閉: .openクラスのtoggle
遷移: max-height 0→400px, padding 0→18px
アイコン: ＋ → 45deg回転
```

### 4-5. CTAブロック

```html
<div class="section-cta" style="background:#050507;">
  <p class="section-cta-context">文脈テキスト</p>
  <a href="https://lin.ee/WGWUFeW" class="btn-cta-main">今すぐ無料でシュート診断を受ける</a>
</div>
```

### 4-6. ゴーストテキスト演出

背景に薄く大文字を重ねる装飾。Cinzel clamp(28px, 9vw, 48px)。
色: `rgba(255,255,255,0.03)`（ダーク面）/ `rgba(0,0,0,0.025)`（ライト面）

---

## 5. 外部リンク一覧

### サービスURL
| 用途 | URL |
|------|-----|
| LP（メイン） | `https://stepbystep-ascent.com` |
| LP（購買） | `https://stepbystep-ascent.com/buy` |
| LP（分析ダッシュボード） | `https://stepbystep-ascent.com/analytics` |
| 受講規約 | `https://stepbystep-ascent.com/terms/` |
| Practice | `https://practice.stepbystep-ascent.com` |
| Trial | `https://practice.stepbystep-ascent.com/trial` |

### LINE
| 用途 | URL |
|------|-----|
| LINE（全CTA統一） | `https://lin.ee/WGWUFeW` |
| LINE（SG/SF） | `https://lin.ee/WGWUFeW?ref=sg` |
| LINE（PG） | `https://lin.ee/WGWUFeW?ref=pg` |
| LINE（PF/C） | `https://lin.ee/WGWUFeW?ref=pf` |
| LINE（保護者） | `https://lin.ee/WGWUFeW?ref=parents` |

### Stripe決済
| 用途 | URL |
|------|-----|
| Stripe LITE | `https://buy.stripe.com/bJecN47bXc1E6xW183f7i0A` |
| Stripe UNLEASH | `https://buy.stripe.com/28EcN47bXbeA8G4bMHf7i0B` |
| Stripe PRO | `https://buy.stripe.com/aFaeVccwhbeAf4seYTf7i0C` |

### その他
| 用途 | URL |
|------|-----|
| メール | `moriki.beaters@gmail.com` |
| GA4 | `G-YDTC8ECY4R` |

---

## 6. 使い方ガイド

### このSKILLを使うべき場面

1. **LPに新セクションを追加するとき** — セクション構成表で挿入位置を決め、デザイントークンでCSS値を取得する
2. **CTAを追加・修正するとき** — CTAブロックのHTMLテンプレートをコピーし、文脈テキストだけ変える
3. **LINE配信文を書くとき** — コピールール§3を参照してトーン・禁止表現を守る
4. **新しいプランカードを追加するとき** — カードパターン§4-2の「Featured」仕様に従う
5. **FAQ・反論処理を追加するとき** — 語尾は丁寧語統一、アコーディオンパターン§4-4を使う
6. **創業者の声を書くとき** — 一人称「俺」、語尾「〜した。〜だ。」、数値を必ず含める
7. **保護者向けコンテンツを追加するとき** — FOR PARENTSセクション内に限定、中高生向けと混ぜない
8. **デザインの一貫性を保ちたいとき** — 全色・全フォント・全余白はこのファイルの値のみ使用する

### CMOへの指示テンプレート

```
セクション追加依頼:
- 挿入位置: [セクション名]の直後
- 背景色: SKILL.md §1-1 参照
- コピートーン: SKILL.md §3-1 参照
- CTAの有無: あり → SKILL.md §4-5 テンプレート使用
```
