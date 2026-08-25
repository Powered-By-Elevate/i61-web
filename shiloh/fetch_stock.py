#!/usr/bin/env python3
"""Temp stock via Openverse (CC commercial-use). Attribution recorded — required for CC-BY/SA.
Stand-ins until Shiloh's own photography exists."""
import json, subprocess, pathlib, time
from PIL import Image

WANT = [
 ("hero",      ["event venue interior", "banquet hall interior"]),
 ("gal1",      ["wedding reception barn", "wedding tables"]),
 ("gal2",      ["dinner long table", "banquet dinner"]),
 ("gal3",      ["warehouse interior brick", "loft interior"]),
 ("gal4",      ["woodworking workshop", "carpentry workshop"]),
 ("gal5",      ["patio string lights", "outdoor terrace evening"]),
 ("mission",   ["youth group volunteers", "students workshop"]),
 ("gather",    ["reception hall event", "event hall tables"]),
 ("buildwide", ["building renovation interior", "construction interior"]),
 ("visitwide", ["georgia countryside", "country road trees"]),
 ("givehero",  ["community dinner", "shared meal table"]),
]
out = pathlib.Path("assets/stock"); out.mkdir(parents=True, exist_ok=True)
credits = []
def try_query(key, q):
    r = subprocess.run(["curl","-sS","--max-time","25",
        f"https://api.openverse.org/v1/images/?q={q.replace(' ','%20')}"
        "&license_type=commercial&page_size=10"], capture_output=True, text=True)
    try: results = json.loads(r.stdout).get("results", [])
    except Exception: return False
    for res in results:
        url = res.get("url") or ""
        if not url: continue
        w = res.get("width") or 0
        if w and w < 900: continue
        dst = out / f"{key}.jpg"
        dl = subprocess.run(["curl","-sSL","--max-time","45","-A","Mozilla/5.0",
                             "-o",str(dst),url], capture_output=True)
        if dl.returncode == 0 and dst.exists() and dst.stat().st_size > 30000:
            try:
                im = Image.open(dst); im.verify()
            except Exception:
                dst.unlink(missing_ok=True); continue
            credits.append(f"| `{key}.jpg` | {(res.get('title') or '?')[:60]} | "
                f"{res.get('creator') or '?'} | CC {(res.get('license') or '?').upper()} "
                f"{res.get('license_version') or ''} | {res.get('foreign_landing_url') or url} |")
            print(key, "OK", dst.stat().st_size//1024, "KB —", res.get('license'), "—", (res.get('title') or '')[:40])
            return True
        dst.unlink(missing_ok=True)
    return False

for key, queries in WANT:
    if (out / f"{key}.jpg").exists():
        print(key, "already have"); continue
    for q in queries:
        if try_query(key, q): break
        time.sleep(3)
    else:
        print(key, "STILL MISSING")
    time.sleep(3)

hdr = ("# Stock photo credits — TEMPORARY\n\n"
 "Creative Commons images via Openverse, stand-ins until Shiloh's own photography exists.\n"
 "**CC-BY / CC-BY-SA require this attribution wherever published.** Replace before launch.\n\n"
 "| File | Title | Creator | License | Source |\n|---|---|---|---|---|\n")
old = pathlib.Path("assets/stock/CREDITS.md")
prev = [l for l in old.read_text().splitlines() if l.startswith("| `")] if old.exists() else []
seen = set(); rows = []
for l in prev + credits:
    k = l.split("|")[1].strip()
    if k not in seen: seen.add(k); rows.append(l)
old.write_text(hdr + "\n".join(rows) + "\n")
print(f"\ntotal on disk: {len(list(out.glob('*.jpg')))} images; credits rows: {len(rows)}")
