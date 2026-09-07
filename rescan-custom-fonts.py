# -*- coding: utf-8 -*-
"""扫描 fonts/custom，刷新 index.html 里的 CUSTOM_DIR_FONTS。"""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parent
html = root / "index.html"
custom_dir = root / "fonts" / "custom"
t = html.read_text(encoding="utf-8")

exts = {".ttf", ".otf", ".woff", ".woff2"}
bundled = []
for f in sorted(custom_dir.iterdir()):
    if f.suffix.lower() not in exts:
        continue
    fid = "customfile_" + re.sub(r"[^a-zA-Z0-9_-]", "_", f.stem)
    bundled.append(
        {
            "id": fid,
            "label": f.stem,
            "cssClass": "font-" + fid,
            "loadName": "customfile-" + fid,
            "group": "fonts/custom",
            "url": "./fonts/custom/" + f.name,
        }
    )

lines = ",\n".join(
    "        { id: %r, label: %r, cssClass: %r, loadName: %r, group: %r, url: %r }"
    % (b["id"], b["label"], b["cssClass"], b["loadName"], b["group"], b["url"])
    for b in bundled
)
inner = ("\n" + lines + "\n      ") if lines else ""
new_arr = f"      const CUSTOM_DIR_FONTS = [{inner}];"

pat = re.compile(r"      const CUSTOM_DIR_FONTS = \[.*?\];", re.S)
if not pat.search(t):
    raise SystemExit("CUSTOM_DIR_FONTS not found")
t = pat.sub(new_arr, t, count=1)
html.write_text(t, encoding="utf-8")

(custom_dir / "manifest.json").write_text(
    json.dumps({"fonts": [{"file": Path(b["url"]).name, "id": b["id"], "label": b["label"]} for b in bundled]}, ensure_ascii=False, indent=2)
    + "\n",
    encoding="utf-8",
)
print("updated", len(bundled), [b["label"] for b in bundled])
