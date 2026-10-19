# VS Code Marketplace と JetBrains Marketplace — 記憶に基づく観察

**この内容は Claude の学習済みの知識に基づく。実物のページは今回読んでいない。数値は記憶によるもので、実物と違いうる**。確信の度合いは［高］［中］［低］で示す。事実（公式ドキュメント・package.json の仕様・VS Code のソースコードにある色のトークン）と推測（こうだったはず）は、確信の度合いで区別する。対象は、両ストアの Web 版と、アプリ内の画面（VS Code の拡張機能のビュー、JetBrains IDE の Settings › Plugins）である。

## 0. 先に押さえておく、2 つのストアの性格

- どちらも**検索が中心で、文字が主体**である。カードにスクリーンショットは無く、アイコン・名前・発行者・数字で選ばせる。［高］信頼の作り方は逆である。VS Code は**発行者（人）の検証**が主軸で、拡張機能そのものは自動のスキャンだけ。JetBrains では、新しいプラグインは公開前に**人による審査（Plugin Approval、通常 2 営業日**）を通る。［高］
- 価格: VS Code の拡張機能はすべて無料で、「Free」の文字が出るだけ。JetBrains には Paid／Freemium がある。［高］

## (a) 画面の骨格

**VS Code Web**［中］
- 濃い灰色のヘッダーが 1 段（約 48px。製品のタブとサインイン）。ヒーローは、見出し「Extensions for Visual Studio Code」と、幅いっぱいの検索窓 1 つだけ。バナーやカルーセルは無い。
- 一覧: 「Featured／Trending／Most Popular／Recently Added」を見出しで切り替え、同じ形のカードを 4〜5 列のグリッドで並べる。
- 検索結果: 左に約 250px の絞り込みの列（Category のチェックボックスが約 20 個、1 段）、右にグリッド。並べ替えは右上のドロップダウンで行う。

**VS Code アプリ内**［高］
- 幅 300px 前後のサイドバー。上に検索窓「Search Extensions in Marketplace」と漏斗のアイコンがある。
- **検索語が空でも一覧が出る**: 「INSTALLED／POPULAR／RECOMMENDED」の、折りたためる節が並ぶ。一覧は縦 1 列で、クリックするとエディター領域に詳細が開く。

**JetBrains Web**［中］
- ほぼ黒のヘッダー（約 64px）: ロゴ、「Plugins」（IDE ごとのメガメニュー）、「Themes」。
- ヒーロー: 大きな検索窓「Search plugins in Marketplace」。その下に**製品のチップ**（IntelliJ IDEA、PyCharm、…。ロゴ付き）が並び、まず IDE で絞り込む入り口になっている。
- 一覧: 「Staff Picks／New and Updated／Top Downloads／Top Rated」を縦に積み、それぞれ 3〜4 列で、「See all」が付く。その下に**カテゴリーのタイル**（約 20 個）。
- 検索結果: 左に絞り込み（製品・カテゴリー・**価格 Free/Paid/Freemium**・タグ）、右に結果の一覧。

**JetBrains IDE 内**［高］
- 「Marketplace | Installed」の 2 つのタブ。検索窓には「Type / to see options」と表示され、`/tag:` `/vendor:` `/sortBy:` の接頭辞が使える。検索語が空のときは、Web と同じ一覧が出る。左が一覧、右が詳細。

## (b) カード 1 枚の構成

**VS Code アプリ内のリストの行**［構成は高、寸法は中］
- 高さ 62px。左に 42×42px のアイコン、右に 3 行の文字。
- 1 行目: **名前（太字**）と、導入済みなら薄い文字のバージョン番号。右端にインストール数（雲と下矢印のアイコンに「1.2M」）と評価（★「4.5」）。
- 2 行目: 1 行の説明（はみ出す分は省略記号）。
- 3 行目: 発行者名と**青い盾のチェック**。右端に小さな青い「Install」（角丸 2px）。導入後は歯車のアイコンに変わる。
- ラベル（アイコンの隅か名前の横）: Extension Pack は同梱する拡張機能の数、Pre-Release は緑、Preview は黄色、Deprecated は警告、Sponsor はピンクのハート。［中］サムネイルは無い。

**VS Code Web のカード**［中、寸法は低］
- 白い面で、正方形に近い（260px 前後）。角丸 2〜4px、薄い影が 1 段。左上に約 80px のアイコン、右に名前（太字、16px）と発行者（灰色）、下に 2〜3 行の説明、最下段にインストール数・★ 5 個と件数、右端に「Free」。並びは「絵→名前→誰が→何→数字→価格」。

**JetBrains Web のカード**［中、寸法は低］
- 白い面、角丸 4〜8px、1px の薄い枠線で、ポインターを合わせると影が出る。左上に 40〜48px のアイコンと名前（太字）、その下に **vendor 名**、2 行の説明、最下段に「★4.7」（数値だけ）・下矢印と「22.5M」・価格のラベル「Free／Paid／Freemium」。価格そのものはカードに出さない。

## (c) 詳細ページの構成

**VS Code（Web 版とアプリ内は、ほぼ同じ形）**［高］
- 最初の 1 画面はヘッダー。左に 128×128px のアイコン、右に名前（約 26px）、識別子 `publisher.name`、発行者名と青いチェック（Web 版では、横に検証済みのドメイン「microsoft.com」）、インストール数、★と件数、Web 版では「Free」。
- 主ボタンは **「Install」**（青、白い文字、角丸 2px）。Web 版では、横の「Trouble Installing?」を開くと、`ext install ms-python.python` とコピーのボタンが出る。
- タブ: アプリ内は「DETAILS／FEATURE CONTRIBUTIONS／CHANGELOG／DEPENDENCIES／RUNTIME STATUS」（大文字）。Web 版は「Overview／Version History／Q & A／Rating & Review」。
- 本文: 左の 2/3 に **README をそのまま描画する**。右の 1/3（約 300px）は情報欄で、Categories・Tags（チップ）／Resources（Repository・License・Issues・Homepage・Changelog）／More Info（Version・Released on・Last updated・Publisher・Unique Identifier・Report Abuse）が並ぶ。

**JetBrains**［中］
- ヘッダー: 約 80px のアイコン、名前（約 32px）、vendor 名（リンク。JetBrains 製ならロゴのラベル）、互換性を示す行「Compatible with IntelliJ IDEA, …」、価格のタグ「Paid」と「Free 30-day trial」。
- 主ボタンは **「Get」**（塗りのボタン。押すと、起動中の IDE を検出してインストールする「Install to IDE」か、各バージョンの Download を選べる）。有料なら「Buy」「Try Free」。
- タブは「Overview／What's New／Reviews／Versions／Pricing（有料のみ）」。Overview では**先頭にスクリーンショットの並び**、その下に HTML の説明がある。右の列に、Rating の要約、Downloads、Version、Compatibility Range、Tags、Vendor、Resources、Last updated が並ぶ。

## (d) 文字

- VS Code のアプリ内: OS の UI 書体（Segoe UI／SF／system-ui）。基本は 13px、説明 12px、節の見出し 11px の大文字、詳細ページの名前 26px。太字は名前だけ。［高］
- VS Code の Web 版: Segoe UI 系で、基本は 14px、見出しは 24〜26px。［中］
- JetBrains: 自社の書体 **JetBrains Sans**。基本は 15〜16px、カードの名前 16〜18px、詳細ページの名前 28〜32px、見出しの太さ 600〜700、行間 1.5。［書体は高、数値は低］

## (e) 色

- VS Code のアプリ内は、**テーマに完全に追従する**（色はすべてトークンで指定）。Dark Modern: 背景 #1f1f1f、サイドバー #181818、境界線 #2b2b2b、文字 #cccccc、説明 #9d9d9d、ボタン #0078d4。旧来の Dark+ は、ボタン #0e639c、リンク #3794ff。Light Modern: 背景 #ffffff、サイドバー #f8f8f8、ボタン #005fb8。［中〜高］
- 拡張機能の画面専用のトークン: 星 #ff8e00、Sponsor #ea4aaa、Pre-Release #1d9271（緑）、Verified はリンクの色。［中］
- VS Code の Web 版: ヘッダーは濃い灰色、面は白、アクセント色は #0078d4。ダークモードは無い。［中］
- JetBrains: ヘッダーは #27282c、アクセント色は #087cfa、面は白、地は薄い灰色（#f4f4f4 系）、枠線は #d1d1d2 系。ダークテーマに切り替えられる。［hex は中、切替は低］

## (f) 余白・角丸・グリッド・影

- VS Code のアプリ内: 行の左の余白 16〜20px、アイコンと文字の間 14px、角丸 2px、影は無い。区切り線を引かず、行の高さで区切る。詳細ページは、ヘッダーの内側の余白が 20px、右の列は 300px に固定。［中］
- VS Code の Web 版: カードの間隔 16〜20px、角丸 2〜4px、影は 1 段。［低］
- JetBrains の Web 版: カードの内側の余白 24px、角丸 4〜8px、枠線 1px で、ポインターを合わせると影が出る。コンテナの幅は 1200〜1280px。［低］

## (g) 信頼を示す要素

- **Verified publisher（VS Code）**［高］: 発行者名のすぐ後に、青い盾とチェック。ツールチップは「This publisher has verified ownership of <domain>」。検証するのは、**拡張機能ではなく、発行者がドメインを所有していること**。検証されていないものにはバッジが付かないだけで、「未検証」とは書かない。
- 開発段階を示すラベル: Preview（黄色）、Pre-Release（緑）、Deprecated（警告と、代わりの拡張機能の案内）。「Featured」は、Microsoft の担当者が選ぶ一覧。［中］
- **JetBrains**: すべてが審査済みなので、「審査済み」のバッジは無い。代わりに、vendor が JetBrains 自身かどうかを示すラベル、「Staff Picks」の一覧、バージョンごとに互換性を検証したことを示す緑のチェックが、信頼を担う。有料のものには「Free 30-day trial」を必ず併記する。［中］

## (h) 探す動線

- 検索窓が主役で、一覧は補助。［高］
- カテゴリーは固定の 1 段（VS Code は、package.json で列挙されたものと同じ約 20 種: Debuggers／Formatters／Linters／Snippets／Themes／Other など）。［高］
- 接頭辞による絞り込み: VS Code は `@category:"Themes"` `@sort:installs` `@installed` `@recommended` `@builtin`、JetBrains は `/tag:` `/vendor:` `/sortBy:`。漏斗のメニューから選ぶと検索窓に接頭辞が入るので、覚えていなくても使える。［高］
- 発行者名はリンクになっていて、発行者のページ（その人のすべての拡張機能と、検証済みのドメイン）へ移動できる。作成者の名前が残る形である。［高］

## (i) 専門家でない利用者が迷わない工夫

- ボタンの文言は「Install」「Get」の一語。状態に応じて文言が変わる（Install → Installing… → Reload Required → Uninstall）。［高］
- 検索窓が空でも一覧が出る。Web 版からインストールできないときの逃げ道として、「Trouble Installing?」から、1 回でコピーできるコマンドを示す。［高］
- 空の状態では、「No extensions found.」と、検索語を消すリンクを出す。［中］
- 互換性は文で示す（「Compatible with …」）。数は略記する（1.2M、22.5K）。［高］

## (j) 取り入れる点と、取り入れない点

**取り入れる**
1. 検証のバッジを**作成者の名前のすぐ後**に置き、ツールチップで意味を説明する。バッジの対象を「人」にすると、成果物の審査と分けて扱える（オフィシャルは作成者と成果物の両方にバッジを付け、インディーズは作成者の名前にだけバッジを付ける）。
2. 詳細ページは「上に構造化したヘッダー（絵・名前・作成者・主ボタン）／左に本文／右に情報欄」の形にする。情報欄の項目はそのまま使える。
3. 主ボタンは一語にし、状態に応じて文言を変える。うまくいかないときの逃げ道（手順・コマンド）を、ボタンの横に置く。
4. 検索語が空でも一覧を出す。一覧は、「人が選んだもの（Featured／Staff Picks）」と「数で決まるもの（Popular／New）」を、名前で区別する。
5. Extension Pack の同梱数のバッジは、成果物をまとめたものの表示に使える。識別子 `作成者.名前` を見える所に置く。
6. JetBrains の「先頭にスクリーンショット、次に本文」という並び。無償／有償のラベルは文字（Free／Paid）でカードの最下段に置き、価格は詳細ページのタブに出し、「Free trial」を併記する。

**取り入れない**
1. 星と件数（★4.5 (3)）。件数が少ないと、かえって信頼を損なう。依頼者の方針どおり置かない。
2. Q & A や Reviews の空のタブ。空の画面があると、ストアが寂れて見える。
3. README をそのまま見せること。品質が作成者しだいになるうえ、先頭にバッジの列が来る。「一言・できること 3 つ・インストール方法」を決まった形で上に置き、README はその下に置く。
4. 1 段だけの長いカテゴリーの列（約 20 個）。依頼者の決めた、大カテゴリー→中カテゴリーの 2 段にする。
5. 文字だけのカード。これでは App Store のような画面にならない。サムネイルを持つカードと組み合わせる。
6. インストール数で順位を付けること。社内の母数では「3」のような小さな数が並ぶ。出すなら「○チームが利用」のような言い方にする。ヒーローが検索窓だけ、という点も取り入れない。依頼者の言う「しょぼい」の原因になる。
