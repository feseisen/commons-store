"""カタログの JSON をストアの画面（1枚の HTML）に埋め込む。

使い方（このフォルダで）:

    python3 build_store.py

`catalog.json` と `categories.json` を `store-template.html` の差し込み位置に入れ、
`store.html` を作る。ストアの画面はブラウザで開くだけで動き、置き場
（共有ドライブ・SharePoint のライブラリ・GitHub）を選ばない。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "store-template.html"
OUT = HERE / "store.html"
MARKS = {
    "/*__CATALOG__*/": HERE / "catalog.json",
    "/*__CATEGORIES__*/": HERE / "categories.json",
}


def embed(text: str) -> str:
    """<script> の中に置くので、閉じタグと解釈される「</」だけをエスケープする。"""
    return text.replace("</", "<\\/")


def validate(catalog: dict, categories: dict) -> list[str]:
    """機械で確かめられる食い違いだけを並べる。"""
    problems: list[str] = []
    tiers = {t["id"] for t in categories["tiers"]}
    shelves = {(k["id"], s["id"]) for k in categories["kinds"] for s in k["shelves"]}
    signals = {s["id"] for s in categories["signals"]}
    depts = {d["code"] for d in categories.get("departments", [])}
    ids: set[str] = set()
    for it in catalog["items"]:
        ident = it.get("id", "?")
        if ident in ids:
            problems.append(f"{ident}: id が重複")
        ids.add(ident)
        if it.get("tier") not in tiers:
            problems.append(
                f"{ident}: tier が categories.json に無い ({it.get('tier')})"
            )
        if (it.get("kind"), it.get("shelf")) not in shelves:
            problems.append(
                f"{ident}: 大カテゴリーと中カテゴリーの組み合わせが categories.json に無い ({it.get('kind')}/{it.get('shelf')})"
            )
        price = it.get("price", {})
        if price.get("type") not in ("free", "paid"):
            problems.append(f"{ident}: price.type は free か paid")
        if price.get("type") == "paid" and not (
            price.get("amount") and price.get("unit")
        ):
            problems.append(f"{ident}: 有償なら amount と unit が要る")
        if price.get("type") == "paid" and price.get("revenue_dept") not in depts:
            problems.append(
                f"{ident}: 有償なら revenue_dept（収入を計上する部署のコード）に"
                f" categories.json の departments にあるコードが要る ({price.get('revenue_dept')})"
            )
        for s in it.get("signals", []):
            if s not in signals:
                problems.append(f"{ident}: 目印が categories.json に無い ({s})")
    for it in catalog["items"]:
        for ref in it.get("references", []):
            if ref not in ids:
                problems.append(f"{it['id']}: 参考にした成果物 {ref} が無い")
        feats = it.get("features", [])
        if not isinstance(feats, list) or not all(isinstance(f, str) for f in feats):
            problems.append(f"{it['id']}: features は文字列の配列")
    for f in catalog.get("features", []):
        fid = f.get("id", "?")
        if f.get("kind") not in ("story", "collection"):
            problems.append(f"{fid}: 特集の kind は story か collection")
        if f.get("tier") not in tiers:
            problems.append(
                f"{fid}: 特集の tier が categories.json に無い ({f.get('tier')})"
            )
        if not isinstance(f.get("hue"), int):
            problems.append(f"{fid}: 特集には hue（0〜359 の整数）が要る")
        for ref in f.get("items", []):
            if ref not in ids:
                problems.append(f"{fid}: 特集に並べる {ref} が無い")
    return problems


def main() -> int:
    html = TEMPLATE.read_text(encoding="utf-8")
    loaded = {mark: path.read_text(encoding="utf-8") for mark, path in MARKS.items()}
    catalog = json.loads(loaded["/*__CATALOG__*/"])
    categories = json.loads(loaded["/*__CATEGORIES__*/"])
    problems = validate(catalog, categories)
    if problems:
        print("カタログに直すところがあります:", file=sys.stderr)
        for p in problems:
            print("  -", p, file=sys.stderr)
        return 1
    for mark, text in loaded.items():
        if mark not in html:
            print(f"雛形に差し込み位置 {mark} が無い", file=sys.stderr)
            return 1
        html = html.replace(mark, embed(text))
    OUT.write_text(html, encoding="utf-8")
    n = len(catalog["items"])
    print(f"{OUT.name} を作った（{n} 件）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
