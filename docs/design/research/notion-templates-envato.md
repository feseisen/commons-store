# Notion のテンプレートギャラリーと Envato Elements / ThemeForest（デスクトップ Web）の観察メモ

**この内容は Claude の学習データ（記憶）に基づく。実物のページは今回読んでいない。数値は記憶であり、実物と違いうる。**

確信の度合い: ［高］＝公開されている仕様や広く知られた事実、［中］＝観察の記憶で、おおむね確か、［低］＝推測。対象は、Notion が 2023 年の改版から、2024 年 8 月に「Notion Marketplace」になった後まで。Elements は 2020〜2025 年、ThemeForest は旧 Envato Market のデザイン。

**前提となる見方**: 3 つのストアとも「複製して使う素材」のストアで、作成者が前面に出る。価格の見せ方が 3 通りそろっている——Notion は「Free／$価格」を同じ扱いで並べ、Elements は定額制なので**価格を出さず**、ThemeForest は個別の価格を大きく出す。星は ThemeForest にだけある。

## (a) 画面の骨格

**Notion（notion.so/templates）**［中］
1. 上部のバー: Notion 本体のマーケティング用のナビゲーション（白、高さ約 64px）。その下に、見出し「Notion Marketplace」と幅の広い検索欄。
2. **左のサイドバー**（幅約 240〜260px）: カテゴリーの階層。**Work／Life／School** の大カテゴリーの下に、Project management／Meetings／Planning／Notes…の中カテゴリーがある。その上に「Notion Picks」「New & notable」［低］。
3. 本文: 横長の特集バナー 1 枚 → 横並びの一覧（Featured／Popular／New。1 行に 4 枚と See all）→ 4 列のグリッド（幅が狭いと 3 列、さらに狭いと 2 列になる）。
4. 詳細は別のページ `/templates/<slug>`［高］。作成者のページ `/templates/creators/<handle>` には、アバター・自己紹介・SNS・テンプレートの一覧がある［中］。

**Envato Elements**［中］
1. 上部のバー: 黒に近い濃い色（約 60px）。緑の葉のロゴ、種別のメガメニュー（Video／Music／Graphic Templates／Photos／Fonts…）、右に緑で塗りつぶしたボタン「Get Unlimited Downloads」。
2. 検索欄の左端に、種別のドロップダウン（既定は All Items）［高］。
3. ホーム: 見出しと検索欄 → 種別のタイル → 「Trending」「Free files of the month」の横並びの一覧。
4. 一覧: 左のサイドバー（約 260px）に**種別ごとに変わるファセット**（Orientation／Resolution／Applications Supported…）、右に 4〜5 列のグリッド（写真は masonry）。

**ThemeForest**［中］
1. 上部のバー: 濃い灰色〜黒の帯（約 55px）に緑のロゴ。その下に白いカテゴリーのバー（WordPress／eCommerce／Site Templates…と、Popular Items／Free Files／Top Authors）。
2. ホーム: 検索欄を置いたヒーロー → 「Weekly bestsellers」「Featured Items」「New Items」の横並びの一覧。
3. 一覧: 左にカテゴリーの階層（中・小）と Price のスライダー、右に 3〜4 列のグリッドか list（切り替えられる）。Sort は Best sellers／Newest／Best rated／Trending／Price。本文の幅は約 1170px で固定。

## (b) カード 1 枚の構成

**Notion**（上から）
- **カバー画像**: 縦横比はおおむね 16:10〜3:2、角丸 8px、1px の薄い枠［中］。作成者が用意する画像で、これが商品の説明の大半を担う。
- **タイトル**: 1 行で、はみ出す分は省略する。15〜16px の semi-bold、文字色 #37352F［中］。
- **作成者の行**: 直径約 20px の丸いアバターと名前（13px、灰色）。**公式のものは、Notion のロゴのアバターと「Notion」**で示し、それ以上の印は無い［中］。
- **価格**: 作成者の行の右端か下に、「Free」または「$12」と文字で出す（13〜14px）。バッジにはせず、無料と有料を同じ扱いで並べる［中］。「Featured」はカードのラベルではなく、横並びの一覧の見出しで表す［低］。

**Elements**（上から）
- **サムネイル**: 種別によって比率が違う（動画 16:9、グラフィック 4:3、音楽は波形）。角丸は 4px 前後［中］。**動画はホバーすると自動で再生される**［高］。
- ホバーすると、サムネイルの上に「＋（Add to collection）」と緑の「Download」が浮かび上がる［中］。
- **タイトル**（14px、最大 2 行）と「By <author>」（12px、灰色、リンク）［中］。
- **価格は出ない**。無料枠のものにだけ、左上に緑の「Free」の小さなラベルが付く［低］。星も件数も無い［高］。

**ThemeForest**（上から）
- **サムネイル**: 横長の **590×300px** の inline preview を縮小したもの（list 表示では 80×80 のアイコン）［高］。ホバーすると「Live Preview」が浮かび上がる［中］。
- **タイトル**（15〜16px、リンクの色）→「by <author>」→ **価格「$59」（太字、16〜18px）**［中］。
- **★の 5 段階評価と評価の件数、「Sales: 12,345」**［高］。バッジは Trending（炎）と Featured（リボン）［低］。

## (c) 詳細ページの構成

**Notion**［中］
- **最初の 1 画面**: 左（約 60%）に大きなカバー画像、右（約 40%）に、タイトル（28〜32px、bold）→ 作成者（アバターと名前）→ 価格 → **主ボタン「Get template」（黒地に白文字、幅いっぱい、角丸 6〜8px）** → 副ボタン「Preview」（枠線だけ）。以前は「Duplicate」だった。有料のものは「Buy for $19」のような文言［低］。
- **その下**: 「About this template」→「Categories」（チップ）→ **Creator のボックス**（アバター・名前・紹介・View all）→「More by this creator」→「Related templates」（4 枚の横並びの一覧）。情報表は無く、更新日も出なかったと記憶している［低］。

**Elements**［中］
- **最初の 1 画面**: 左（約 65〜70%）に大きなプレビュー。右の白いパネルに、タイトル（20px、bold）→「By <author>」→ **緑の「Download」（幅いっぱい、高さ約 44px）** →「Add to collection」（枠線だけ）→「Included with your subscription」という一文。
- **その下**: **Properties の表**（File Type／Applications Supported／File Size／Dimensions…。種別によって項目が変わる）→「Similar items」→「More from <author>」。星・レビュー・ダウンロード数は無い。

**ThemeForest**［中〜高］
- **最初の 1 画面**: 大きなプレビューと、「Live Preview」（緑の塗りつぶし）・「Screenshots」（枠線）のボタン。右のパネルに、**価格「$59」（24〜28px、bold）** → ライセンスの選択（Regular／Extended）→「Add to Cart」（緑の塗りつぶし）→「Buy Now」（濃い色）→ チェックの印が付いた 3 行「**Quality checked by Envato**」「6 months support from <author>」「Future updates」［高］。
- **本文のタブ**: Item Details／Reviews／Comments／Support（それぞれに件数が付く）［高］。**右の情報表**: Last Update／Published／Compatible With／Software Version／Files Included／Documentation／Tags［高］。
- **作成者のボックス**: 約 80px のアバター、名前、**Elite Author の五角形のバッジ**［中］。

## (d) 文字

- **Notion**: Inter。見出し 32〜40 ／ カードの名前 15〜16 ／ 補足 13 ／ 本文 16px、行間 1.5、太さは 400 と 600 の 2 段階［中］。
- **Elements**: ジオメトリック系のサンセリフ［低］。タイトル 14〜15 ／ 補足 12 ／ 見出し 24〜32px［中］。
- **ThemeForest**: Helvetica／Arial 系。本文は 13〜14px と小さめで、行間 1.4［中］。情報の密度が高く、専門家でない利用者には字が小さい。

## (e) 色

- **Notion**: 背景 #FFFFFF、文字 #37352F［高］、灰色の文字 rgba(55,53,47,.65) 相当、枠 #E9E9E7［中］、主ボタンは黒（#000〜#191919）、Notion の青 #0075DE はリンクと一部の CTA に使う［中］。ダークモードには対応していない［中］。
- **Elements／ThemeForest**: ヘッダーは黒に近い濃い色（#1E1E1E〜#2A2A2A）［低］、アクセント色は Envato の緑 **#82B541**［高、ブランド色］。面は白と #F5F5F5。ダークモードは無い［中］。

## (f) 余白・角丸・グリッド・影

- **Notion**: 本文の幅は最大で約 1200〜1280px、サイドバー 240〜260px、4 列で間隔 24px、角丸 8px、枠 1px、影はホバー時だけ（0 2px 8px rgba(0,0,0,.08) 程度）［中／低］。
- **Elements**: ほぼ画面の幅いっぱい（最大 1400〜1600px）、サイドバー 260px、間隔 16〜20px、角丸 4px、影は無い［中／低］。
- **ThemeForest**: 本文の幅は 1170px で固定、間隔 20px、角丸 3〜4px、枠 1px #E0E0E0、影は無い［中／低］。

## (g) 信頼の印

- **Notion**［中］: 個々の「審査済み」のバッジは無い。**掲載されていること自体が、審査済みであることを示す**（提出 → 掲載の審査）。公式のものは作成者の行が Notion のロゴになるだけで、格を分ける飾りは無い。編集部が選んだものは、「Notion Picks」「Featured」という**横並びの一覧の名前**で表す。
- **Elements**［中］: すべてが品質の審査を通っているので、個々のバッジは無く、作成者の格付けも出さない。
- **ThemeForest**［高］: 「Quality checked by Envato」のチェックの印。**Elite Author**（累計の売上が $75k 超、Power Elite は $1M 超）の五角形のバッジ、Featured Author／Item（編集部が週替わりで選ぶ）。加えて、星・売上数・レビュー数を前面に出す。
- **印の無いものの見せ方**: Notion は、個人の作成者もアバターと名前だけで、公式と同じ形で並べる。ThemeForest では「バッジが無い＝新人」と消極的に示すことになり、新人が不利に見える。

## (h) 探す動線

- **Notion**［中／低］: 検索、左のカテゴリーの階層（大→中）、Marketplace になってからは「Free／Paid」の価格のフィルター、並べ替え（Popular／Newest）。詳細のカテゴリーのチップから、そのカテゴリーの一覧へたどれる。
- **Elements**［中］: 検索欄での種別の選択 → 左のファセット（何段ものチェックボックス）→ **選択中のフィルターがチップで並び、× で外せる**。Clear filters もある。絞り込みの状態は URL に反映される。
- **ThemeForest**［中］: 上のカテゴリーのバー（大）→ 左のカテゴリーの階層（中・小）→ Price のスライダー → Sort（5 種類）→ grid／list の切り替え。

## (i) 専門家でない利用者が迷わない工夫

- **Notion**［中］: ボタンは「Get template」**だけ**（「複製」という機能の名前を使わない）。「Preview」で、入手する前に中身を見られる。価格が「Free」と文字で分かる。カテゴリーの名前が**用途を表す語**（Meeting notes／Habit tracker）。空の状態では「No templates found」と、おすすめの横並びの一覧を出す［低］。
- **Elements**［中］: ボタンは「Download」だけ。ライセンスの説明は一文で済ませる。Similar items で、行き止まりを作らない。
- **ThemeForest**［中］: 「Live Preview」で実物を触って試せるのが、何よりの強み。ただし、ライセンスの選択、2 種類の購入ボタン、4 つのタブ、長い情報表は**プロ向け**で、専門家でない利用者には負担が大きい。

## (j) 取り入れる点と、取り入れない点

**取り入れる点**
1. **Notion のカードは 4 つの要素だけ**（カバー画像・タイトル・作成者・Free／$）。公式（ロゴ）でも個人（アバター）でも同じ形。このストアの「作成者の名前が残る」「無償／有償」にそのまま当てはまる［中］。
2. **主ボタンは「Get template」だけにし、副ボタンに「Preview」を置く**。「Get」の一語で済ませ、複製・入手・インストールの違いを利用者に考えさせない［中］。
3. **「Quality checked by Envato」のチェックの印**を、「審査済み（オフィシャル）」を示す表現として取り入れる。主ボタンのすぐ下に置く 1 行［高］。
4. **Elements の Properties の表**を、このストアの「形式・動作環境・更新日・提供者」の定型に使う［中］。
5. **選択中のフィルターを示すチップ**（Elements）と、**右のパネルを固定する形**（ThemeForest。スクロールしても購入の欄が画面に残る）［中］。
6. **Notion の「格の違いは一覧の名前で表す」やり方**。区分が 2 つなら、カードに飾りを足さず、区分ごとの入り口と詳細の 1 行で分ける［中］。

**取り入れない点**
1. 星・売上数・レビュー数を並べて出すこと（ThemeForest）。
2. **売上額で作成者を格付けするバッジ**（Elite Author）。社内では、新人を萎縮させる方向に働く。
3. 4 つのタブ、長い情報表、2 種類の購入ボタン。専門家でない利用者が迷う構造そのものである。
4. 「価格を出さない」こと（Elements）。定額制だから成り立つ形である。
5. 有料のものが前面に出た横並びの一覧（Marketplace になってからの Notion）。社内では、有償のものが目立つと使われなくなる。
6. 590×300 という**横長だけ**のプレビューの規格。種類の混ざるこのストアでは、比率を固定してそろえるか、masonry を許すかを**先に決める**。
