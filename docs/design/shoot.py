"""ストアの画面を Chromium で描画し、画面・幅・テーマごとの PNG を作る。

使い方:

    python3 shoot.py <store.html> <出力フォルダ> [light|dark|both] [desktop|phone|both]

PNG のほかに、JS のエラーと横スクロールの有無を `errors.txt` に、
各画面の高さを `metrics.json` に書く。「審査待ち」の画面を撮るために、
localStorage の役割を審査担当者（reviewer）にして開く。

Chromium は Playwright が入れたものを使う。別の場所のものを使うときは、
環境変数 CHROMIUM_PATH にその実行ファイルのパスを入れる。
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

CHROMIUM = os.environ.get("CHROMIUM_PATH") or None
ROUTES = [
    ("home", "home"),
    ("official", "official"),
    ("indie", "indie"),
    ("list-all", "all/tool/spreadsheet"),
    ("list-indie-material", "indie/material"),
    ("item-official", "item/a-0001"),
    ("item-indie-paid", "item/a-0106"),
    ("item-requested", "item/a-0102"),
    ("feature", "feature/f-1"),
    ("maker", "maker/%E9%88%B4%E6%9C%A8%EF%BC%88%E6%9E%B6%E7%A9%BA%EF%BC%89"),
    ("search-empty", "search"),
    ("search-q", "search?q=%E4%BB%95%E6%A7%98%E6%9B%B8"),
    ("search-0", "search?q=zzz"),
    ("publish", "publish"),
    ("review", "review"),
    ("mine", "mine"),
]


def pick(arg: str | None, both: tuple, one: dict) -> tuple:
    if arg is None or arg == "both":
        return both
    return (one[arg],)


def main() -> None:
    src = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    themes = pick(
        sys.argv[3] if len(sys.argv) > 3 else None,
        ("light", "dark"),
        {"light": "light", "dark": "dark"},
    )
    widths = pick(
        sys.argv[4] if len(sys.argv) > 4 else None,
        ((1280, "desktop"), (400, "phone")),
        {"desktop": (1280, "desktop"), "phone": (400, "phone")},
    )
    errors: list[str] = []
    metrics: dict[str, int] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROMIUM
        )  # None なら Playwright の既定
        for theme in themes:
            for width, tag in widths:
                ctx = browser.new_context(
                    viewport={"width": width, "height": 900}, color_scheme=theme
                )
                ctx.add_init_script(
                    "try{localStorage.setItem('store.role', JSON.stringify('reviewer'))}catch(e){}"
                )
                page = ctx.new_page()
                where = f"{theme}/{tag}"
                page.on(
                    "pageerror", lambda e, w=where: errors.append(f"pageerror {w}: {e}")
                )
                page.on(
                    "console",
                    lambda m, w=where: (
                        errors.append(f"console {w}: {m.text}")
                        if m.type == "error"
                        else None
                    ),
                )
                for name, route in ROUTES:
                    page.goto(src.as_uri() + "#/" + route, wait_until="load")
                    page.wait_for_timeout(500)
                    page.screenshot(
                        path=str(out / f"{name}-{tag}-{theme}.png"), full_page=True
                    )
                    sw = page.evaluate("document.documentElement.scrollWidth")
                    cw = page.evaluate("document.documentElement.clientWidth")
                    if sw > cw + 1:
                        errors.append(
                            f"{name}/{where}: 横スクロール scrollWidth={sw} clientWidth={cw}"
                        )
                    metrics[f"{name}-{tag}-{theme}"] = page.evaluate(
                        "document.documentElement.scrollHeight"
                    )
                # 見出しが縮んだ帯
                page.goto(src.as_uri() + "#/item/a-0001", wait_until="load")
                page.wait_for_timeout(300)
                page.evaluate("window.scrollTo(0, 500)")
                page.wait_for_timeout(400)
                page.screenshot(path=str(out / f"item-scrolled-{tag}-{theme}.png"))
                # 入手の流れ
                page.goto(src.as_uri() + "#/item/a-0001", wait_until="load")
                page.wait_for_timeout(300)
                page.locator("[data-get='a-0001']:visible").first.click()
                page.wait_for_timeout(1200)
                page.screenshot(path=str(out / f"item-got-{tag}-{theme}.png"))
                page.evaluate("localStorage.removeItem('store.got')")
                ctx.close()
        browser.close()
    (out / "errors.txt").write_text("\n".join(errors) or "(なし)", encoding="utf-8")
    (out / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print("shots:", len(list(out.glob("*.png"))), "errors:", len(errors))
    for e in errors:
        print(" -", e)


if __name__ == "__main__":
    main()
