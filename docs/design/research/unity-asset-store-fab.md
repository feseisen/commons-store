# Unity Asset Store と Epic Fab（デスクトップ Web）の観察メモ

**この内容は Claude の学習済みの知識に基づく。実物のページは今回読んでいない。数値は記憶によるもので、実物と違いうる。**

確信の度合い: ［高］＝公式の仕様（画像の規格・ライセンス制度）や広く知られた事実、［中］＝観察の記憶で、おおむね確か、［低］＝推測。対象とする時期は、Unity Asset Store が 2020 年の改修以降、Fab が 2024 年 10 月の公開（UE Marketplace・Sketchfab Store・Quixel・ArtStation Marketplace を統合したもの）以降。**Fab は記憶が少なく、確信の度合いは Unity より一段低い。**

両ストアの性格: Unity は、白い地で文字が中心の、情報の詰まった「部品カタログ」［高］。Fab は、黒い地で画像が中心の、「見て選ぶ」ストア［中］。どちらも、大カテゴリー→中カテゴリーの階層・左の絞り込みの列・星・割引率のバッジ・カードに載る作成者名を持ち、**星を除けば、社内のストアの骨組みに近い**［高］。

## (a) 画面の骨格

**Unity**（上から）
1. **ヘッダー**（黒、約 60px）: ロゴと「Asset Store」、中央に幅の広い検索窓、右に「Sell Assets」、カート、通知、アバター。［中］
2. **カテゴリーのバー**（1 段）: 3D / 2D / Add-Ons / Audio / AI / Decentralization / Essentials / Templates / Tools / VFX、末尾に**目立つ色の「Sale」**。ポインターを合わせると、中カテゴリーのメガメニュー（複数列）が開く。［高。AI・Decentralization の有無は中］
3. **ヒーロー**（幅いっぱいのカルーセル。ほぼ常にセールか特集）［高］→ **横並びの一覧**（「Top new assets」「Popular assets」「Publisher of the week」と「See all」。1 行に 4〜5 枚）［中］
4. **一覧ページ**: 左に絞り込みの列（240〜260px）、右にカードが **4 列**（幅 1280 前後のとき）。上に件数と並べ替え。ページ送り式。最大幅は 1,300〜1,440px で、ダークモードは無い。［中。幅は低］
5. **詳細ページ**: パンくずリスト → タイトルの行 → 左の 2/3 にメディア、右の 1/3 に購入パネル → 説明・技術情報・中身・バージョンの履歴・レビュー・作成者・関連。［高］

**Fab**（上から）
1. **ヘッダー**（黒、約 64px）: ワードマーク（文字のロゴ）、幅の広い検索窓、右に「Sell on Fab」、ウィッシュリスト、カート、アバター。［中］
2. **カテゴリーのバー**: 3D Models / Environments / Game Systems / Game Templates / VFX / Materials / Textures / Animations / Audio / 2D Assets / Tools & Plugins / Education & Tutorials / Smart Assets / UI と、**14 個前後もある**。［中］
3. **ヒーロー** → **横並びの一覧**: **「Limited-Time Free」**（毎月の無料の枠。期間内に入手すれば、その後も持ち続けられる）、Featured、New releases、Trending、Quixel Megascans。行ごとに「View all」があり、1 行に 5〜6 枚。［中］
4. **一覧ページ**: 左に絞り込みの列、右にカードが **5〜6 列**。カードは Unity より小さく、画像が大半を占める。［低］
5. **詳細ページ**: 左の 2/3 にメディア、右の 1/3 に「ライセンスの選択・価格・Add to cart」 → Description / Technical details / License / Reviews / Questions。［中］

## (b) カード 1 枚の構成

**Unity**（上から）
- **サムネイルは 3:2**。規格は「Card image 420×280」（ほかに Icon 160×160・Cover 1950×1300・Social 1200×630）。［高］
- サムネイルの**左上に割引のバッジ**（「-50%」の塗りのタグ）、右上には、ポインターを合わせると♡が出る。［中］
- **作成者名**（12〜13px、灰色。タイトルより上）→ **タイトル**（14〜15px、太字。2 行を超えると省略）。［中］
- **星 5 つと (件数)**。評価が無いと、空の星がそのまま出る。［高］
- **価格**: 太字。無料なら **「FREE」の文字**。割引中は、元の価格に灰色の取り消し線を引き、新しい価格を並べる。［高］
- 幅 260〜300px、内側の余白 12〜16px、角丸 4px 前後（四角い印象）、薄い境界線。ポインターを合わせると薄い影が出る。所有済みのものには「Purchased」にあたるラベルが付く。［中。ラベルは低］

**Fab**（上から）
- **サムネイルは 16:9** に近い（推奨は 1920×1080 だった記憶がある）。角丸 6〜8px。上に「Limited-Time Free」「-XX%」のピル。［中］
- **タイトル**（白、14px、1〜2 行）→ **販売者名**（灰色、12px）→ **星と件数**、**価格**（Free／$。割引中は取り消し線と割引率）。所有済みなら「In library」。［中］
- 対応する形式を示す小さなロゴ（UE / UEFN / Unity）。詳細ページにだけ出るのかもしれない。［低］

## (c) 詳細ページの構成

**Unity — 最初の 1 画面**
- パンくずリスト「Home > 3D > Environments > Fantasy」。H1（26〜30px）、作成者名（リンク）、星と件数、お気に入りの数。［高］
- **左**: 動画／スクリーンショットの大きなギャラリーと、サムネイルの並び。［高］
- **右のパネル**（スクロールに追従する）: 大きく示した価格 → **主ボタン**（有料なら「Add to Cart」／無料なら「**Add to My Assets**」／所有済みなら「**Open in Unity**」。青の塗り・幅いっぱい・高さ 40〜44px）→ ♡「Add to favorites」→「Taxes/VAT calculated at checkout」→ **License type**（Single / Multi Entity。Multi は価格が 2 倍）→ **情報欄**（File size / Latest version / Latest release date / Original Unity version / Support）→ 信頼を示す 3 行（Quality assets / Trusted / Knowledge-based）。［文言・情報欄は高、青と 3 行は中］
- **下**: Overview、**Render pipeline compatibility の表**（Built-in / URP / HDRP × Compatible／Not compatible／補足）、Technical details、**Package Content（ファイルのツリー）**、Releases、Reviews（評価の分布のグラフ）、Publisher info、Related assets。［高］

**Fab — 最初の 1 画面**
- H1、販売者のアバターと名前、星と件数。**左**では、動画・画像・Sketchfab 由来の 3D ビューアーを切り替えられる。［中］
- **右のパネル**: **License の選択**（Personal＝年商 10 万ドル未満／Professional。選ぶと価格が変わる）［高］→ 価格 → **「Add to cart」**（無料なら「**Add to My Library**」。青系で、Epic Games Store の #0078F2 に近かった記憶がある）［低］→「Add to wishlist」（枠線のボタン）→ Supported engine versions（例: 5.0–5.5）／Supported platforms／Download type（Asset Pack / Complete Project / Plugin）／Included formats（FBX / OBJ / glTF / USD のチップ）／Last update。［中］
- **下**: Description / Technical details / License / Reviews / Questions と、販売者のほかの商品。［中］

## (d) 文字

- **Unity**: 2020 年のブランド刷新以降は Inter 系（以前は Open Sans／Roboto だった記憶がある）。本文 14px／補助の文字 12px／カードのタイトル 14〜15px（太字）／H1 28px 前後／見出し 20px。行間 1.4〜1.5。太さは 400 と 600 の 2 段階。［中］
- **Fab**: 記憶があいまい。Epic の Web は、見出しが Brutal Type、本文はシステム書体に近いサンセリフ。本文 14px、補助の文字 12px。黒い地なので、太字は控えめ。［低］

## (e) 色

- **Unity**: 背景 #FFFFFF、ヘッダー #000〜#1A1A1A、文字 #1F1F1F〜#222、補助の文字 #6B6B6B、境界線 #E0E0E0 前後。アクセント色は青（#2196F3〜#1E88E5 に近かった記憶がある）。割引のバッジは暖色（赤〜橙）、「Sale」は赤系。［白地・黒ヘッダー・青ボタンは中、hex は低］
- **Fab**: 背景 #121212〜#161616、面 #1E1E1E〜#242424、文字 #FFFFFF／補助の文字 #A0A0A0。境界線をほとんど使わず、**面の明度の差で区切る**。アクセント色は青（#0078F2 系）。ダークモードが既定で、ライトモードに切り替えられるかは不明。［低］

## (f) 余白・角丸・グリッド・影

- **Unity**: カードの間隔 24px、カードの内側の余白 16px、カードの角丸 4px、画像の角丸 0〜4px。影は、ポインターを合わせたときだけ 0 2px 8px rgba(0,0,0,.15) 程度。セクションの間隔 40〜48px。［角張った印象は中、数値は低］
- **Fab**: カードの間隔 16px、カード・画像の角丸 8px、影は無い（黒い地では影が効かない）。パネルの内側の余白 20〜24px。［低］

## (g) 信頼を示す要素

- **Unity**: 公式のものは、**「Unity Technologies」というパブリッシャー名**で示す。専用のバッジではなく、**発行元の名前が手がかりになる**。［高］「Verified Solutions」（Unity が審査した外部ツール）のラベルが一部に付く。［中］「Publisher of the week」などの、**人が選んで並べた一覧**と、累計の評価が、実質的な信頼の指標になっている。［中］**未審査の側にバッジは無い**。空の星・0 件のレビュー・古い日付が、消極的な手がかりになるだけ。［中］
- **Fab**: 公式のものは、**「Epic Games」「Quixel」が販売者**として表示される。Megascans を UE の利用者には無料にする（UE に限ったライセンス）という制度が、信頼の代わりになっている。［高］Featured / Limited-Time Free に載っていれば、Epic が選んだもの、という形。［中］審査のバッジを見た記憶は無い。［低］
- **ここから言えること**: 両ストアとも、審査済みか未審査かを、**バッジではなく、発行元の名前と一覧**で示している。二つの区分を設けるなら、この両ストアより一段はっきり示してよい。

## (h) 探す動線

- **検索**: ヘッダーの中央に検索窓が 1 つ。Unity では、入力中の候補に、サムネイル付きのアセット名とカテゴリーが出る。［中］
- **カテゴリーの階層**: Unity は、3D → Characters（Humanoids／Robots…）・Environments（Fantasy／Sci-Fi…）・Props・Vegetation・Vehicles、Tools → AI／Animation／GUI／Network…の三段。［高］Fab は 3D Models → Characters／Props／Vehicles／Weapons…。［中］
- **左の絞り込み**: Unity は、カテゴリーの階層（件数付き）、価格のスライダー、星、無料のみ、セール中、パブリッシャー、Unity のバージョン、Render Pipeline、リリース日。［中〜高］Fab は、Format（UE／Unity／UEFN／エンジン以外）、Category、Price、License、Compatibility、Rating、Seller、Sale、Quixel。［中］
- **チップ**: 適用中の絞り込みの条件が、結果の上に「×」付きのチップとして並び、「Clear all」も付く。［中］
- **並べ替え**: Unity は Relevance／Popularity／Rating／Price／Name／Recently updated。Fab は Relevance／Newest／Price／Top rated／Best selling。［中］
- 詳細ページの**パンくずリスト**が、カテゴリーの階層へ戻る道になる。［高］

## (i) 専門家でない利用者が迷わない工夫

- **ボタンの文言が、状態に応じて変わる**: Add to Cart → Add to My Assets（無料）→ Open in Unity（所有済み）。Fab も Add to cart → Add to My Library。次に何が起きるかが読み取れる。［高］
- **最初の 1 画面に、価格・主ボタン・互換性がそろう**（右のパネル）。**互換性は表で示す**（Render Pipeline の表、Supported engine versions）。［高］
- **Package Content** によって、「入手する前に中身が分かる」。［高］
- **空の状態**: 検索結果が 0 件のときは、「No results for …」と、「別の言葉で探す／絞り込みを減らす」という提案を出す。カートが空のときは「Browse assets」へ誘導する。［中］
- **無料のものへの入り口**: Unity の「Free assets」のページ、Fab の「Limited-Time Free」の一覧。専門家でない利用者が最初に触れる導線になる。［中〜高］
- 逆に、Fab の **Personal／Professional の選択は、最初に迷うところ**（自分がどちらに当たるのか分からない）。［中］

## (j) 取り入れる点と、取り入れない点

**取り入れる**
1. **カテゴリーのバーとメガメニュー**で、大カテゴリーから中カテゴリーまで、ポインターを 1 回合わせるだけでたどれるようにする。絞り込みの階層に件数を添える。［高］
2. **カードの並び**: 横長のサムネイル → 作成者名（小さく、灰色）→ 名前（太字、2 行まで）→ 価格（無料なら「FREE」の文字）。割引率はサムネイルの左上のタグで示す。**星の行を消せば、そのまま社内で使える。**［高］
3. **詳細ページの右のパネル**に、価格・主ボタン・互換性・バージョン・更新日・サイズを固定する（スクロールに追従させる）。［高］
4. **状態に応じてボタンの文言を変える**（入手する／持っている→開く）。カードにも「入手済み」のラベルを付ける。［高］
5. **Render Pipeline の表**の形式で「対応環境」を表にし、**Package Content** と **Releases** を置く。［高〜中］
6. Fab の **Limited-Time Free** のような「今月の一覧」を、人が選んだものへの入り口にする。公式のものは**発行元の名前**で示し、社内では**審査済みのバッジも加える**。［中］

**取り入れない**
1. **星の評価とレビュー**（社内のストアには無い。消すと、カードの縦方向の詰まりも軽くなる）。［高］
2. **セールを常に前面に出すこと**（ヒーローが常にセール、「Sale」のタブ、カウントダウン）。社内に値引きは無い。［高］
3. **ライセンスの段階**（Personal／Professional、Single／Multi Entity）と税の注記。［高］
4. **Fab の 14 個の大カテゴリー**。1 段に収まらず、ひと目で見渡せない。6〜8 個に抑える。［中］
5. **Fab の小さすぎるカード**（名前が読めない）と、**Unity の四角く情報の詰まった画面**。依頼者の「しょぼくない」は App Store に近い水準のことで、この二つのストアは、どちらもそこに届かない。［中］
6. 絞り込みに、**開発者にしか分からない軸**（バージョン・パイプライン）を並べること。社内のストアでは「カテゴリー／無償・有償／作成者／区分」で足りる。［中］
