# Slack App Directory・Atlassian Marketplace・Salesforce AppExchange — 記憶に基づく観察

**この内容は Claude の学習データ（記憶）に基づく。実物のページは今回読んでいない。数値は記憶であり、実物と違いうる。**確信の度合いは［高］［中］［低］で示す。事実（公式のデザインシステムのトークン、公式に告知されたプログラムの名前）と推測（画面の並びの記憶）を、確信の度合いで区別する。3 つのストアとも 2023〜25 年にデザインが改められており、記憶の中で改修の前後が混ざっている可能性がある。

## 0. 先に押さえておく、3 つのストアの性格

- 3 つのストアとも、**管理者がアプリを導入する、企業向けのストア**である。カードは、楽しさより**だれが作り、だれが保証するか**を前に出す。［高］
- **「ストアに並んでいること自体が、審査済みであることを示す」**点が共通している。Slack では掲載前に Slack が審査し、Atlassian では Cloud アプリの掲載時に審査があり、Salesforce では Security Review が必須である。［高］したがって、審査済みの印は、掲載されたものどうしを区別するものではなく、**ストアの外（自作のもの・掲載されていないもの）との境目**として働く。3 つのストアの「オフィシャル／インディーズ」は、ここで分かれる。［高］
- 星は Atlassian（4 段階）と AppExchange（5 段階）にあり、**Slack には無い**。Slack は、「作成者・一言・審査」だけで成り立つ、星の無いストアの実例である。［中〜高］

## (a) 画面の骨格

**Slack App Directory（slack.com/apps、現在の名前は「Slack Marketplace」）**［中］
- 白い地。全体のナビゲーション（約 64px）の下に、見出しと検索窓（幅約 640px）、右に「Manage」「Build」がある。
- **左のサイドバー（約 240px）に、カテゴリーが縦一列**に並び、右にコンテンツがある。トップページでは、「Featured」「Essential apps」「Brilliant bots」など、**編集部が選んだ一覧**が、横 4 列の固定のグリッドで並ぶ。カルーセルは無い。
- カテゴリーは Analytics／Customer Support／Developer Tools／HR／Productivity／Project Management／Sales／Security など、約 20 個。［中］

**Atlassian Marketplace**［中〜高］
- 上部のナビゲーションは 1 段（白、約 56px）: ロゴ、中央に検索窓、右に「Manage apps」「Sell」。
- ヒーローに、見出しと**製品のチップ（Jira, Confluence, Bitbucket, JSM…）**がある。先に**製品**を選ばせるのが最大の特徴である。［高］
- 一覧は「Trending」「Staff picks」「New」で、それぞれ横 4 列。グリッドの幅は約 1,140px、カードの幅は約 270px。［中］
- 一覧ページは、左に絞り込み（Hosting＝Cloud／Data Center、価格、カテゴリー、Partner）、右に 3〜4 列の結果。［高］

**Salesforce AppExchange**［中］
- 紺〜青の色の帯（約 56px）に、ロゴ、**メガメニュー**（Solutions by Type／Product Collections／Industry Collections／Consultants／Learn）、中央に「Search AppExchange」がある。
- 画像のバナーのカルーセルがあり、その下に「Featured」「Trending」「Top Rated」の**横にスクロールする一覧**（矢印付き、1 段に 4〜5 枚）が並ぶ。［中〜高］
- 一覧ページは、左に絞り込み、右に 3 列の結果。Apps／Components／Bolt／Flow／Consultants と、**種類の違うものが同じ検索結果に混ざる**。［中〜高］

## (b) カード 1 枚の構成

| | Slack | Atlassian | AppExchange |
|---|---|---|---|
| 形 | 白、枠線 1px、角丸約 8px、高さ約 120px［中］ | 白、枠線 1px（N30）、角丸 3px、高さ約 200px［中］ | 白、薄い影、角丸 4px、高さ約 220px［中］ |
| 左上 | アイコン 48〜64px、角丸 12px［中］ | アイコン 48px、角丸 3px［中〜高］ | ロゴ 60px、角丸 4px［中］ |
| 1 行目 | 名前（16px、太字） | 名前（16px、太字）と、右に **Cloud Fortified の盾** | 名前（16px、太字） |
| 2 行目 | 一言（2 行を超えると省略） | 「by ベンダー」（12〜13px）、Partner なら金／銀の印 | 「by 会社」 |
| 3 行目 | 無し | 一言（2 行を超えると省略） | 一言（2 行を超えると省略） |
| 下段 | 無し（**価格も星も無い**）［中〜高］ | ★（4 段階）と件数、installs の数、**Free／Paid via Atlassian**、Cloud／DC のチップ［高］ | ★（5 段階）と件数、**Free／Paid／Discounted**、Labs の印［中〜高］ |

- 3 つのストアとも、サムネイルは無い。**身元を示すのは、アイコンと作成者名だけ**である。画像で選ばせない。［高］
- 無料は「Free」、有料は「Paid」と文字で示す。金額はカードに出さず、詳細ページで「Starts at」として示す。［中〜高］

## (c) 詳細ページの構成

**Slack**［中］: 左に大きなアイコン（96px）、名前、一言、作成者、**緑の「Add to Slack」**（作成者が自分で配布するアプリでは「Visit site to install」）。右の列に、カテゴリー、Website／Privacy／Support、審査済みの印。その下に、スクリーンショット、説明、**「Permissions」**（アプリが見られるもの／できることを、scope ごとに平易な文で列挙する）。［中〜高］

**Atlassian**［中〜高］: 左に大きなアイコン（72px）、名前、「by ベンダー」、Partner／Cloud Fortified の印、★と件数、インストール数。右に**青の「Try it free」**（無料なら「Get it now」）と、Hosting の切り替え。**タブ: Overview／Reviews／Pricing／Privacy & Security／Support／Versions／Installation**。Overview は、3 枚のハイライト画像にそれぞれ 1 文を添え、その下に長い説明が続く。右の列に、価格表（per-user の月額）と Compatibility。

**AppExchange**［中］: 上にメディアのカルーセル。左に、ロゴ、名前、「by 会社」、★と件数、Listed／Latest Release の日付。**青の「Get It Now」**と「Test Drive」（デモ用の組織で試せる）と「Watch Demo」。タブ: Overview／Details／Reviews／Provider。**Details の情報表**: Pricing、Supported Editions、Package Type、Languages、Lightning Ready、Data Residency、Compliance。

## (d) 文字

- Slack: 本文の書体は **Lato**、見出しは Larsseit。本文は 15〜16px、行間 1.5。［中〜高］
- Atlassian: ADS のシステム書体（-apple-system／Segoe UI／Roboto）で、見出しは Charlie Display。本文 14px、小さい文字 12px、見出し 20／24／29px、行間 20px。［高］
- AppExchange: 書体は **Salesforce Sans**。本文 14〜16px、小さい文字 12px、見出し 24〜28px、行間 1.5。［高］

## (e) 色

- Slack: 茄子色（aubergine）**#4A154B**、緑 #2EB67D／ボタン #007A5A、青 #36C5F0、黄 #ECB22E、赤 #E01E5A。地は白。ダークモードは無い。［高（色）／中（ボタン）］
- Atlassian: 青 **#0052CC**、押したときの色 #0747A6、文字 **#172B4D**、補助の文字 #6B778C、面 #F4F5F7、枠線 #EBECF0。盾は青。Marketplace は白い画面だけ。［高］
- AppExchange: 青 **#0176D3**（以前は #0070D2）、紺 #032D60、地 #F3F3F3、文字 #181818、枠線 #C9C9C9。ダークモードは無い。［高（色）／中（紺）］

## (f) 余白・角丸・グリッド・影

- 3 つのストアとも、**8px を基準**にしている。カードの内側の余白は 16px、カードの間隔は 16〜24px。［高］
- 角丸: Slack は 8〜12px、Atlassian は **3px**、Salesforce は **4px**（0.25rem）。［高］
- 影: Atlassian は枠線が主で、ポインターを合わせたときだけ `0 4px 8px -2px rgba(9,30,66,.25)`。Salesforce は `0 2px 2px rgba(0,0,0,.1)`。Slack は枠線だけ。［中〜高］

## (g) 信頼の印

**Slack**［中〜高］
- 掲載されていれば審査済み。カードに印は無く、詳細ページの右の列に一行で示す。**Built by Slack** は、作成者名の位置に出る。［中］
- ストアの外の「カスタムアプリ」は、管理画面で**「承認待ち」**として別に扱う。**ストアに無いもの＝未審査**という二分である。［高］

**Atlassian**［高］
- **Cloud Fortified**（盾。信頼性・セキュリティ・サポートの基準を満たす）、**Cloud Security Participant**（バグ報奨金制度に参加している）、**Marketplace Partner（Gold／Platinum）**、**Staff pick**、**Supported**（作成者がサポートする）、**Runs on Atlassian**（データが外部に出ない Forge アプリ。2024 年ごろから）［中］。
- 印は**重ねて表示される**。印がまったく無くても掲載される。

**AppExchange**［中〜高］
- **Security Review に合格することが掲載の条件**（印というより前提）。**Salesforce Labs**（社員が作った、無料でサポートの無いもの。**公式だが保証なし**という第 3 の枠）。パートナーの階層は Summit／Crest／Ridge／Base。**Lightning Ready**。「AppExchange Certified」という印は記憶に無い（人の資格と混同しているかもしれない）。［低］

## (h) 探す動線

- **検索窓が最上段**にある。絞り込みの順は、Atlassian が製品→カテゴリー→Hosting（**製品が先**）、AppExchange が種類→価格→Edition→業種。Slack はカテゴリーを縦一列に並べるだけ。［中〜高］
- 並べ替え: Relevance／Trending／Top rated／New（Atlassian）、Relevance／Rating／Newest（AppExchange）。［中］

## (i) 専門家でない利用者が迷わない工夫

- **ボタンの文言が、操作そのものを表す**: 「Add to Slack」「Try it free」「Get It Now」。ボタンは 1 色で、文言は 1 つの語句。［高］
- Slack の、**Permissions を平易な文で列挙する**やり方。［中〜高］
- Atlassian は、Hosting の切り替えで、**自分の環境で動くか**を先に見せる。［高］
- AppExchange の **Test Drive**（導入せずに試せる）。［高］
- 空の状態: Atlassian は「No apps found」と、絞り込みを解除する操作を出す。ほかのストアについては記憶があいまい。［低］

## (j) 取り入れる点と、取り入れない点

**取り入れる**
- 「掲載＝審査済み」とし、**ストアの外にあるものは「未審査」として別の区分に置く**という二分（Slack の承認待ち、Salesforce Labs の「公式だが保証なし」）。社内のストアの、オフィシャル／インディーズの骨格そのものである。［高］
- 印の**重ね方**（Atlassian）。「動作保証」「セキュリティ」「作成者によるサポート」を別々の印にする。［高］
- カードは**アイコン・名前・作成者・一言**だけにする（Slack）。［高］
- 無償／有償は、「Free」「Paid」のように文字で示し、金額の表は詳細ページに置く。［中〜高］
- 使う場所（製品）を先に選ばせる導線（Atlassian）。社内なら「用途」に置き換える。［中］

**取り入れない**
- ★とレビュー。社内では母数が小さく、信頼の印を重ねるだけで足りる。［高］
- AppExchange の、**種類の違うものが混ざる検索**と、メガメニュー・画像のカルーセル。仕掛けばかりが目立つ。［中〜高］
- Atlassian の 3px の角丸と、12px の文字による密度。管理画面向けの作りで、App Store らしさから遠い。［中］
