"""試作の catalog.json と categories.json を、SharePoint のリストに取り込める CSV にエクスポートする。

使い方（commons-store のフォルダで）:

    python3 tools/export_for_sharepoint.py

出力先は docs/backend/import/。標準ライブラリだけで動く。
会社の PC に Python が無くても使えるよう、エクスポートした CSV はリポジトリに置いておく。

- 列の名前は、リストの列の内部名（半角英字）にそろえる。表示名は日本語に後から変える。
  列の意味と型は docs/backend/data-model.md が正本。
  SharePoint がすでに持つ列と重なる名前（Order・Version）は使わず、
  SortOrder・ItemVersion にする（data-model.md 1 章）。
- 配列（features・environments・references・files・signals、特集の items）は、
  1 つのセルに改行でつないで入れる（リストの「複数行テキスト」の列に 1 行 1 つ）。
- 文字コードは BOM 付きの UTF-8。Excel で開いても日本語が化けないようにするため。
- エクスポートする前に build_store.py の validate() で確かめる。直すところがあれば止まる。
- エクスポートした後、CSV から catalog.json と categories.json の形に組み立て直し、
  元と比べる（元の形に戻せるかの確認）。違ってよいのは、決めてある例外だけ。

サンプルデータは架空。本番のサイトには取り込まない。
"""

from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "backend" / "import"
DATA_MODEL = ROOT / "docs" / "backend" / "data-model.md"
TEMPLATE = ROOT / "store-template.html"

# 設定のリストの既定値。意味は data-model.md の「設定」の表が正本。
# ここに足したキーは、data-model.md にも書くこと（書いていなければ警告を出す）。
SETTINGS: list[tuple[str, str]] = [
    ("IdPrefix", "s"),
    ("DuplicateWindowMinutes", "10"),
    ("ReviewWaitDays", "30"),
    ("ApplyWaitDays", "14"),
    ("RawKeepDays", "90"),
    ("RisingMin30", "5"),
    ("RisingRatio", "2"),
    ("StandardMinDays", "180"),
    ("StandardMinDepts", "5"),
    ("StandardMinMonths", "4"),
    ("SignalAlertShare", "0.2"),
    ("StaleAlertHours", "36"),
    ("ShowDeptNamesToMaker", "no"),
    ("DeptNameMinPeople", "2"),
    ("PriceUnits", "1人あたり月額\n1部門あたり月額\n1人分の買い切り"),
    ("MonthlyUnits", "1人あたり月額\n1部門あたり月額"),
    ("DeptScopeUnits", "1部門あたり月額"),
    ("CostApproval", "other_dept"),
    ("DeptCodeCheck", "list"),
    ("DeptCodePattern", "^[0-9A-Z-]{3,12}$"),
    ("CloseDay", "1"),
    ("AckWaitDays", "5"),
    ("CsvBom", "no"),
    ("TimeZone", "Tokyo Standard Time"),
    ("DetailLinkFormat", ""),
]

ITEM_COLUMNS = [
    "Title",
    "ItemId",
    "Tagline",
    "Summary",
    "Description",
    "Features",
    "Tier",
    "Kind",
    "Shelf",
    "PriceType",
    "PriceAmount",
    "PriceUnit",
    "RevenueDeptCode",
    "MakerId",
    "MakerUpn",
    "MakerName",
    "MakerOrg",
    "ItemVersion",
    "Updated",
    "PublishedAt",
    "Environments",
    "References",
    "Files",
    "ReviewStatus",
    "ReviewAt",
    "ReviewBy",
    "ReviewNote",
    "Signals",
    "State",
]
FEATURE_COLUMNS = [
    "Title",
    "FeatureId",
    "Kind",
    "Tier",
    "Lead",
    "Body",
    "Items",
    "Hue",
    "SortOrder",
    "Show",
]
CATEGORY_COLUMNS = [
    "Title",
    "Type",
    "CatId",
    "Sub",
    "SubShort",
    "Parent",
    "SortOrder",
    "Hue",
    "Active",
]
REVIEW_COLUMNS = ["Title", "ItemId", "Outcome", "ReviewerLabel", "At", "Note", "Source"]
DEPT_COLUMNS = ["Title", "DeptName", "DirectoryDept", "ValidFrom", "ValidTo", "Active"]
SETTING_COLUMNS = ["Title", "Value"]


def load_validate():
    """build_store.py の validate() を借りる（同じ決まりを二か所に書かない）。"""
    spec = importlib.util.spec_from_file_location(
        "build_store", ROOT / "build_store.py"
    )
    if spec is None or spec.loader is None:
        raise SystemExit("build_store.py を読めない")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.validate


def shelf_hues() -> dict[str, int]:
    """中カテゴリーの色相は、試作では雛形のコードにある。データへ移すために読む。"""
    text = TEMPLATE.read_text(encoding="utf-8")
    m = re.search(r"const HUE = \{([^}]*)\}", text)
    if not m:
        print(
            "注意: 雛形に const HUE が見つからない。Hue の列は空にする", file=sys.stderr
        )
        return {}
    return {k: int(v) for k, v in re.findall(r"'?([\w-]+)'?\s*:\s*(\d+)", m.group(1))}


def lines(values: list[str] | None) -> str:
    return "\n".join(values or [])


def split_lines(cell: str) -> list[str]:
    return [v for v in cell.split("\n") if v != ""]


def dept_codes(catalog: dict, categories: dict) -> dict[str, str]:
    """部署の名前 → 部署コード。

    categories.json の departments（試作の画面が申し込みと公開で使う一覧）があればそれを使う。
    無ければサンプルとして、作成者の部署の名前に出てきた順で D001 から振る（架空）。
    """
    if categories.get("departments"):
        return {d["name"]: d["code"] for d in categories["departments"]}
    codes: dict[str, str] = {}
    for it in catalog["items"]:
        org = it["maker"]["org"]
        if org not in codes:
            codes[org] = f"D{len(codes) + 1:03d}"
    return codes


def item_row(it: dict, codes: dict[str, str]) -> dict[str, str]:
    price = it.get("price", {})
    review = it.get("review", {"status": "none"})
    status = review.get("status", "none")
    # returned は成果物のリストに持たない（利用者の画面では none と同じ）。
    # 理由の一言は審査の履歴へ移す。
    public_status = "none" if status == "returned" else status
    paid = price.get("type") == "paid"
    return {
        "Title": it["name"],
        "ItemId": it["id"],
        "Tagline": it.get("tagline", ""),
        "Summary": it.get("summary", ""),
        "Description": it.get("description", ""),
        "Features": lines(it.get("features")),
        "Tier": it["tier"],
        "Kind": it["kind"],
        "Shelf": it["shelf"],
        "PriceType": price.get("type", "free"),
        "PriceAmount": str(price.get("amount", "")) if paid else "",
        "PriceUnit": price.get("unit", "") if paid else "",
        # 既定値: 収入を計上する部署は作成者の部署（サンプルデータでは架空のコード）。
        "RevenueDeptCode": price.get("revenue_dept", codes[it["maker"]["org"]])
        if paid
        else "",
        "MakerId": it["maker"].get("id", ""),
        "MakerUpn": "",
        "MakerName": it["maker"]["name"],
        "MakerOrg": it["maker"]["org"],
        "ItemVersion": it.get("version", ""),
        "Updated": it.get("updated", ""),
        "PublishedAt": it.get("published", ""),
        "Environments": lines(it.get("environments")),
        "References": lines(it.get("references")),
        "Files": lines(it.get("files")),
        "ReviewStatus": public_status,
        "ReviewAt": review.get("at", "") if public_status != "none" else "",
        "ReviewBy": review.get("by", "") if public_status == "approved" else "",
        "ReviewNote": review.get("note", "") if public_status != "none" else "",
        "Signals": lines(it.get("signals")),
        "State": it.get("state", "listed"),
    }


def row_to_item(r: dict[str, str]) -> dict:
    """リストの 1 行を catalog.json の 1 件に戻す（エクスポートのフローと同じ対応）。"""
    if r["PriceType"] == "paid":
        price: dict = {
            "type": "paid",
            "amount": int(r["PriceAmount"]),
            "unit": r["PriceUnit"],
        }
        if r["RevenueDeptCode"]:
            price["revenue_dept"] = r["RevenueDeptCode"]
    else:
        price = {"type": "free"}
    maker = {"name": r["MakerName"], "org": r["MakerOrg"]}
    if r["MakerId"]:
        maker["id"] = r["MakerId"]
    status = r["ReviewStatus"]
    if status == "approved":
        review = {
            "status": status,
            "by": r["ReviewBy"],
            "at": r["ReviewAt"],
            "note": r["ReviewNote"],
        }
    elif status == "requested":
        review = {"status": status, "at": r["ReviewAt"], "note": r["ReviewNote"]}
    else:
        review = {"status": "none"}
    item = {
        "id": r["ItemId"],
        "name": r["Title"],
        "summary": r["Summary"],
        "tier": r["Tier"],
        "kind": r["Kind"],
        "shelf": r["Shelf"],
        "price": price,
        "maker": maker,
        "version": r["ItemVersion"],
        "updated": r["Updated"],
        "environments": split_lines(r["Environments"]),
        "references": split_lines(r["References"]),
        "files": split_lines(r["Files"]),
        "review": review,
        "signals": split_lines(r["Signals"]),
        "description": r["Description"],
        "features": split_lines(r["Features"]),
        "tagline": r["Tagline"],
    }
    if r["PublishedAt"]:
        item["published"] = r["PublishedAt"]
    if r["State"] and r["State"] != "listed":
        item["state"] = r["State"]
    return item


def feature_rows(catalog: dict) -> list[dict[str, str]]:
    return [
        {
            "Title": f["title"],
            "FeatureId": f["id"],
            "Kind": f["kind"],
            "Tier": f["tier"],
            "Lead": f.get("lead", ""),
            "Body": f.get("body", ""),
            "Items": lines(f.get("items")),
            "Hue": str(f["hue"]),
            "SortOrder": str(n),
            "Show": "yes",
        }
        for n, f in enumerate(catalog.get("features", []), start=1)
    ]


def row_to_feature(r: dict[str, str]) -> dict:
    return {
        "id": r["FeatureId"],
        "kind": r["Kind"],
        "tier": r["Tier"],
        "title": r["Title"],
        "lead": r["Lead"],
        "body": r["Body"],
        "items": split_lines(r["Items"]),
        "hue": int(r["Hue"]),
    }


def category_rows(categories: dict, hues: dict[str, int]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def add(**kw: str) -> None:
        row = {c: "" for c in CATEGORY_COLUMNS}
        row.update(kw)
        row["Active"] = "yes"
        rows.append(row)

    for n, t in enumerate(categories["tiers"], start=1):
        add(
            Title=t["name"],
            Type="tier",
            CatId=t["id"],
            Sub=t.get("sub", ""),
            SortOrder=str(n),
        )
    for n, k in enumerate(categories["kinds"], start=1):
        add(Title=k["name"], Type="kind", CatId=k["id"], SortOrder=str(n))
        for m, s in enumerate(k["shelves"], start=1):
            hue = hues.get(s["id"])
            add(
                Title=s["name"],
                Type="shelf",
                CatId=s["id"],
                Parent=k["id"],
                SortOrder=str(m),
                Hue="" if hue is None else str(hue),
            )
    for n, s in enumerate(categories.get("signals", []), start=1):
        add(
            Title=s["name"],
            Type="signal",
            CatId=s["id"],
            Sub=s.get("why", ""),
            SubShort=s.get("sub", ""),
            SortOrder=str(n),
        )
    return rows


def rows_to_categories(rows: list[dict[str, str]]) -> dict:
    def of(kind: str) -> list[dict[str, str]]:
        return sorted(
            (r for r in rows if r["Type"] == kind), key=lambda r: int(r["SortOrder"])
        )

    return {
        "tiers": [
            {"id": r["CatId"], "name": r["Title"], "sub": r["Sub"]} for r in of("tier")
        ],
        "kinds": [
            {
                "id": k["CatId"],
                "name": k["Title"],
                "shelves": [
                    {"id": s["CatId"], "name": s["Title"]}
                    for s in of("shelf")
                    if s["Parent"] == k["CatId"]
                ],
            }
            for k in of("kind")
        ],
        "signals": [
            {
                "id": r["CatId"],
                "name": r["Title"],
                "why": r["Sub"],
                "sub": r["SubShort"],
            }
            for r in of("signal")
        ],
    }


def review_rows(catalog: dict) -> list[dict[str, str]]:
    """決まった審査（approved と returned）を、審査の履歴の行にする。"""
    rows = []
    for it in catalog["items"]:
        rv = it.get("review", {})
        if rv.get("status") in ("approved", "returned"):
            rows.append(
                {
                    "Title": f"{it['id']}-{rv.get('at', '')}",
                    "ItemId": it["id"],
                    "Outcome": rv["status"],
                    "ReviewerLabel": rv.get("by", ""),
                    "At": rv.get("at", ""),
                    "Note": rv.get("note", ""),
                    "Source": "migrated",
                }
            )
    return rows


def dept_rows(codes: dict[str, str]) -> list[dict[str, str]]:
    return [
        {
            "Title": code,
            "DeptName": org,
            "DirectoryDept": org,
            "ValidFrom": "2026-04-01",
            "ValidTo": "",
            "Active": "yes",
        }
        for org, code in codes.items()
    ]


def write_csv(name: str, columns: list[str], rows: list[dict[str, str]]) -> Path:
    path = OUT / name
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns)
        w.writeheader()
        w.writerows(rows)
    return path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def round_trip(catalog: dict, categories: dict) -> list[str]:
    """CSV から組み立て直して元と比べる。決めてある例外以外の違いを返す。"""
    unexpected: list[str] = []
    expected: list[str] = []
    back = {r["ItemId"]: row_to_item(r) for r in read_csv(OUT / "items.csv")}
    for it in catalog["items"]:
        got = back.pop(it["id"], None)
        if got is None:
            unexpected.append(f"{it['id']}: 組み立て直した中に無い")
            continue
        want = json.loads(json.dumps(it))
        # 例外 1: returned は成果物のリストに持たないので none に戻る
        if want["review"].get("status") == "returned":
            want["review"] = {"status": "none"}
            expected.append(
                f"{it['id']}: review.status returned → none（理由は審査の履歴へ）"
            )
        # 例外 2: 有償の成果物に収入を計上する部署のコードが無ければ、作成者の部署のコードが足される
        if got["price"].get("revenue_dept") and "revenue_dept" not in want["price"]:
            want["price"]["revenue_dept"] = got["price"]["revenue_dept"]
            expected.append(
                f"{it['id']}: price.revenue_dept を足した（{got['price']['revenue_dept']}、架空）"
            )
        if want != got:
            for key in sorted(set(want) | set(got)):
                if want.get(key) != got.get(key):
                    unexpected.append(
                        f"{it['id']}.{key}: {want.get(key)!r} → {got.get(key)!r}"
                    )
    for extra in back:
        unexpected.append(f"{extra}: 元に無い行")
    feats = [row_to_feature(r) for r in read_csv(OUT / "features.csv")]
    if feats != catalog.get("features", []):
        unexpected.append("特集: 元と違う")
    # 部署の一覧は categories.csv ではなく departments.csv に入る
    tree = {k: v for k, v in categories.items() if k != "departments"}
    if rows_to_categories(read_csv(OUT / "categories.csv")) != tree:
        unexpected.append("カテゴリー: 元と違う")
    if categories.get("departments"):
        back_depts = [
            {"code": r["Title"], "name": r["DeptName"]}
            for r in read_csv(OUT / "departments.csv")
        ]
        if back_depts != categories["departments"]:
            unexpected.append("部署の一覧: categories.json の departments と違う")
    for line in expected:
        print("  想定どおりの違い:", line)
    return unexpected


def check_settings_documented() -> None:
    if not DATA_MODEL.exists():
        print(
            "注意: data-model.md が無いので、設定のキーの突き合わせをしなかった",
            file=sys.stderr,
        )
        return
    text = DATA_MODEL.read_text(encoding="utf-8")
    missing = [k for k, _ in SETTINGS if f"`{k}`" not in text]
    if missing:
        print(
            "注意: data-model.md に書いていない設定のキー: " + ", ".join(missing),
            file=sys.stderr,
        )


def main() -> int:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    categories = json.loads((ROOT / "categories.json").read_text(encoding="utf-8"))
    problems = load_validate()(catalog, categories)
    if problems:
        print(
            "カタログに直すところがあります（build_store.py と同じ検査）:",
            file=sys.stderr,
        )
        for p in problems:
            print("  -", p, file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    codes = dept_codes(catalog, categories)
    written = [
        write_csv(
            "items.csv", ITEM_COLUMNS, [item_row(it, codes) for it in catalog["items"]]
        ),
        write_csv("features.csv", FEATURE_COLUMNS, feature_rows(catalog)),
        write_csv(
            "categories.csv", CATEGORY_COLUMNS, category_rows(categories, shelf_hues())
        ),
        write_csv("review_history.csv", REVIEW_COLUMNS, review_rows(catalog)),
        write_csv("departments.csv", DEPT_COLUMNS, dept_rows(codes)),
        write_csv(
            "settings.csv",
            SETTING_COLUMNS,
            [{"Title": k, "Value": v} for k, v in SETTINGS],
        ),
    ]
    for p in written:
        n = len(read_csv(p))
        print(f"{p.relative_to(ROOT)} をエクスポートした（{n} 行）")
    print("元の形に戻せるかの確認（CSV → catalog.json・categories.json の形）:")
    unexpected = round_trip(catalog, categories)
    check_settings_documented()
    if unexpected:
        print("想定外の違いがあります:", file=sys.stderr)
        for u in unexpected:
            print("  -", u, file=sys.stderr)
        return 1
    print("  想定外の違いは無い")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
