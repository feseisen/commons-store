# Hugging Face Hub と npm・PyPI — 記憶に基づく観察

**この内容は Claude の学習済みの知識に基づく。実物のページは今回読んでいない。数値は記憶によるもので、実物と違いうる**。確信の度合いは［高］［中］［低］で示す。事実（公式の仕様・広く知られた作り）と推測（こうだったはず）は、確信の度合いで区別する。対象は3つのストアの Web 版。

## 0. 先に押さえておく、3つのストアの性格

- 3つのストアとも、**検索が中心で文字が主体であり、レビューの星が無い**。HF にはハート（いいね）だけがあり、npm・PyPI には評価の仕組み自体が無い。すべて無料で、価格の表示も無い。［高］
- 「公式」であることをストアが認定するバッジは、**どこにも無い**。作成者がだれなのかは、**名前空間**（`meta-llama/…`、`@angular/…`）で示す。［高］

## (a) 画面の骨格

**Hugging Face**［高］
- ヘッダーは1段（約64px）: 絵文字のロゴ、左寄りの検索窓「Search models, datasets, users...」、右に Models / Datasets / Spaces / Docs / Pricing / Log In / **Sign Up**。
- 一覧 `/models`: **左が絞り込みの列（幅約1/4）、右が結果の列**。結果の先頭に「Models」と総数、「Sort: Trending」があり、その下にカードが並ぶ。**広い画面では2段組**になる［中］。特集の一覧は無く、Trending がその代わりになっている。
- Spaces の一覧だけは、**4列のカラフルなカードのグリッド**で、アプリストアに最も近い［中］。

**npm**［高］
- 上に黒い細いバー（Pro / Teams / Pricing / Documentation）があり、その下の白いヘッダーに、赤いロゴと**幅いっぱいの検索窓**と赤い「Search」ボタンが並ぶ。
- トップページは製品の宣伝ページで、**パッケージを並べた一覧が無い**（2019年の作り直しで、以前の一覧が消えた）［中］。
- 検索結果: 左に「Sort Packages」（Optimal / Popularity / Quality / Maintenance のラジオボタン）、右に**1段**の結果のリストがあり、先頭に「N packages found」と出る。

**PyPI**［高］
- 濃い青のヘッダー: 白いロゴ、検索窓「Search projects」、Help / Sponsors / Log in / Register。トップページには、大きな検索窓と「Or browse projects」、4つの統計の数（projects / releases / files / users）がある。
- 検索結果: **左が Trove 分類による絞り込み**（Framework / Topic / Development Status / License / Programming Language / OS … を折りたたんで並べる）、右が「N projects for "q"」と「Order by: Relevance / Date last updated / Trending」、1段で並ぶ結果の枠。

## (b) カード1枚の構成

**HF のモデルのカード**［中］: 高さ約60px、白い面、1px の薄い灰色の枠線、角丸約8px、内側の余白12〜16px。サムネイルは無い。1行目は、種別のアイコンと`org/model-name`（半太字。長いと末尾を省略）。2行目は、灰色12〜13px のメタ情報の列「タスク名（色付きアイコン）• Updated 3 days ago • ⤓1.2M • ♥3.5k」。ポインターを合わせると枠線が濃くなる。最近は「8B」のような、規模を示す小さなラベルも付く［低］。

**HF の Space のカード**［中］: 横長の角丸のカードの全面に、**README の冒頭で作成者が指定した2色のグラデーション**と絵文字、白抜きのタイトル。下に、所有者・「Running」を示す緑の点・♥の数。**画像を用意させずに、にぎやかに見せる**仕組みである。

**npm の検索結果**［中］: 名前（約20px、太字）。完全に一致したものには緑の「exact match」ラベル。1行の説明。灰色の丸い**キーワードのラベル**（自由に付けるタグ）。メタ情報の行には、公開者の正方形のアバター、ユーザー名、「published 18.2.0 • 2 months ago」。右端に p / q / m を示す小さな棒が3本［低］。

**PyPI の検索結果**［高］: 白い枠線の付いた横長の枠。左上に名前（約18px、太字）、右上にバージョン、右の2行目にリリース日、下に1行の説明。画像もアイコンも無い。

## (c) 詳細ページの構成

**HF のモデル**［高］
- 最初の1画面: 所有者のアバターと`org / name`（大きな文字で、コピーのボタン付き）、♥のいいねボタン（数付き）、org の Follow。その下に**タグのラベルの並び**（Transformers / Safetensors、タスク、言語、`License: apache-2.0`、arXiv）。
- **タブ「Model card / Files and versions (n) / Community (n)**」があり、同じ行の右端に、灰色の「Train」「Deploy」と、**黒地に白い文字の「Use this model」**（標準の操作）がある。
- 本文は、**左の2/3が README、右の1/3が事実を並べる列**: Downloads last month と折れ線グラフ、Model size / Tensor type、Inference の欄、Model tree（派生・量子化の系図）、Spaces using、Collections including。Gated のモデルでは、README の上に同意を求める枠が出る［中］。

**npm**［高］
- 名前（h2、約32px、太字）と青い「TS」ラベル、その下に「18.2.0 • Public • Published 2 years ago」。非推奨のパッケージには赤いバナーが出る。
- タブ「Readme / Code / Dependencies (n) / Dependents (n) / Versions (n)」（タブごとに下線の色が違う）［低］。
- 右の列: 「Install」の `npm i react` をコピーできる枠、Repository、**Weekly Downloads の大きな数と折れ線グラフ**、Version / License、Unpacked Size / Total Files、Collaborators のアバターの列、灰色の枠の「Report malware」。2023年以降は、「Provenance: Built and signed on GitHub Actions」と緑のチェックを示す節がある［中］。

**PyPI**［高］
- 薄い色のヘッダーに `requests 2.32.3`（約30px）、黒地の `pip install requests` をコピーできる枠、緑の「Latest version」ラベル、「Released: 日付」、一行の説明。
- その下は、**左の1/4が縦のタブ（Project description / Release history / Download files）と事実、右の3/4が README**。
- 左の事実は、**「Verified details」（緑のチェック。PyPI が確認したもの: Maintainers・確認済みの Project links）と「Unverified details」（Project links、Meta＝License / Author / Requires Python、Classifiers）に二分される**［中〜高、2023〜24年導入］。Release history は縦の時系列で、yanked（取り下げ）は警告の色で示す［中〜高］。

## (d) 文字

- HF: **Source Sans Pro** と IBM Plex Mono（等幅）を、Tailwind の設定で指定している［中〜高］。本文16px、カードのタイトル15〜16px（半太字）、メタ情報12〜14px（灰色）、詳細ページのタイトル24〜30px、行間1.5前後［中］。
- npm: システムのサンセリフ書体（-apple-system / Segoe UI / Roboto）で、等幅は Fira Mono あたり［低］。名前32px、本文15〜16px。
- PyPI: **こちらも Source Sans Pro**（自前のサーバーから配信）で、等幅は Source Code Pro［中〜高］。名前30px前後、検索結果18px。

## (e) 色

- HF: 背景は白、面は白に灰色100/200の枠線、アクセント色は黄 `#FFD21E` と橙 `#FF9D00`、主ボタンは黒。**ダークモードに対応している**（設定で切り替える。面は gray-950 系）［中〜高］。タスクの大分類ごとにアイコンの色が違う（NLP は藍、Audio は黄、Tabular は緑、RL は赤）［中］。
- npm: 赤 `#CB3837`［高］、文字は `#231F20` 系［中］、ラベルは灰色 `#f2f2f2`。ダークモードは無い［中］。
- PyPI: ヘッダーは濃い青（`#0073B7` 前後）、リンクは青、成功は緑、警告は黄・赤（yanked / deprecated）［低〜中］。ダークモードは無い［中］。

## (f) 余白・角丸・グリッド・影

- HF: 4px 刻み（Tailwind）。角丸はカード8px、ラベル6〜8px、主ボタン8px。カードの間隔は横24px・縦8〜12px。**影はほとんど使わず、ポインターを合わせると枠線の色が変わる**［中］。最大幅は約1400px［低］。
- npm: 最大幅は1200px前後。詳細ページは2列で、幅の比は 2:1。区切り線1px、角丸2〜4px、影は無い［中〜低］。
- PyPI: 検索結果の枠は角丸2〜4px、枠線1px、縦の間隔は約16px、影は無い［中〜低］。

## (g) 信頼を示す要素

- **HF**: 公式を示すラベルは無く、**名前空間（`meta-llama/`、`google/`）とアバターのロゴが、公式であることを示す**。org のページには、種別（company / university / non-profit / community）と Enterprise のラベルが出る［中］。個人は `username/` の形で並ぶだけ。Gated（利用に同意が必要）と Private（錠のアイコン）は、別の軸である［中］。
- **npm**: **「TS」ラベル**（型定義がある）、**Provenance**（ビルド元の署名）、公開者のアバター、非推奨を示す赤いバナー、マルウェアを通報するボタン。組織は `@scope/` で示す［高］。
- **PyPI**: **「Verified details / Unverified details」の二分**が最も明快である。**事実ごとに「ストアによる確認」と「作成者からの情報」を分け**、確認した側にだけ緑のチェックを付ける［中〜高］。ほかに、Trusted Publishing による由来の表示と、yanked の警告がある［中］。
- 3つのストアとも、**公開者を審査したことを示すバッジは無い**。バッジは「機械的に検証できた事実」にだけ付く。

## (h) 探す動線

- 共通: **ヘッダーの検索窓が起点**になる。HF では、入力中に、Models / Datasets / Spaces / Users ごとにまとめた候補が下に出る［高］。
- HF: 左の絞り込みは、**大分類（Multimodal / Computer Vision / NLP / Audio / Tabular / RL）→ タスク**の2段で、大分類ごとにアイコンの色が違う［中］。Libraries / Languages / Licenses もチップで選ぶ。選んだ条件は URL に残る。並べ替えは Trending / Most likes / Most downloads / Recently created / updated［高］。
- npm: **分類が無い**。自由に付けるキーワードのラベルと、`keywords:` による検索がある。並べ替えは4つの指標だけ［高］。
- PyPI: Trove 分類（`Topic :: Software Development :: Libraries` のような階層）が唯一の分類。並べ替えは3種類［高］。

## (i) 専門家でない利用者が迷わない工夫

- 最初に押すボタンは1つだけ: HF の「Use this model」、npm / PyPI の**1回のコピーで済むインストールの枠**［高］。
- 「Updated 3 days ago」のような相対的な時刻と、「1.2M」「45.6k」のような省略した数。正確な値は、ポインターを合わせると出る［高］。
- 空の状態: HF は「No models found」と、絞り込みを外す導線。PyPI は「There were no results for "x"」と、綴りの修正や別の語の提案［中］。
- Space では、「Running / Sleeping / Build error」を示す色の点で、「今動くか」が一目で分かる［中］。
- 弱点: HF の絞り込みとラベルの並びは、初めて見る人には重い。npm は、探す語を思いつかない人には入り口が無い。PyPI は結果の見た目が均一で、「どれが良いか」の手がかりが無い［中］。

## (j) 取り入れる点と、取り入れない点

**取り入れる**
1. **大分類→中分類の2段**にし、大分類に色付きのアイコンを付ける（HF のタスク）。中分類はチップで選ばせ、選んだ条件は URL に残す。
2. 左に絞り込み、右に結果を置き、結果の先頭に総数と並べ替えを出す。既定の並びを Trending にすれば、特集の一覧を手で作らなくてよい。
3. 名前と1行のメタ情報だけの薄いカードと、アプリにだけ使う、グラデーションと絵文字のにぎやかなカード（HF Spaces）。**作成者にサムネイルの制作を強いない**。
4. 詳細ページの「タブと、右端の黒い主ボタン」と「右の列の事実の表と折れ線グラフ」。README は事実の表の**後ろ**に置く。
5. **名前空間によって作成者の名前が残る**（`org/name`）。個人は `user/name` となり、それが「個人」の手がかりになる。
6. **「確認した事実／作成者からの情報」の二分**（PyPI）と、由来の署名（npm）を、「審査済み／未審査」のバッジの形に応用する。

**取り入れない**
1. npm の p / q / m の棒。意味が分からず、不信感を生む。
2. HF の黄と橙、npm の赤といったブランドの色。
3. README に任せきりの詳細ページ。構造化した欄を先に置く。
4. HF のような、100を超える絞り込みの項目。社内の規模なら、6前後の大分類と中分類で足りる。
5. 星・レビュー。3つのストアとも、無くても成り立っている。
