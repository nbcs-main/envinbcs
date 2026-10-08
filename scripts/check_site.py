#!/usr/bin/env python3
"""Static checks for the NBCS site. Run from the repo root:  python3 scripts/check_site.py
Exit code 1 if any ERROR is found (CI uses this). Needs: pip install beautifulsoup4
"""
import os, re, sys, json
from urllib.parse import unquote
from bs4 import BeautifulSoup

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
os.chdir(ROOT)
MAX_IMAGE_BYTES = 1_000_000
errors, warnings = [], []
def err(p, m): errors.append(f"{p}: {m}")
def warn(p, m): warnings.append(f"{p}: {m}")

pages = sorted(os.path.join(d, f)[2:] for d, _, fs in os.walk(".") for f in fs
               if f.endswith(".html") and not d.startswith(("./.git", "./includes", "./node_modules")))
sitemap = open("sitemap.xml", encoding="utf-8").read() if os.path.exists("sitemap.xml") else ""
in_sitemap = {u.replace("https://nbcs-envi.com/", "") or "index.html"
              for u in re.findall(r"<loc>([^<]+)</loc>", sitemap)}

for p in pages:
    src = open(p, encoding="utf-8", errors="replace").read()
    s = BeautifulSoup(src, "html.parser")
    is_redirect = bool(s.find("meta", attrs={"http-equiv": re.compile("refresh", re.I)}))
    if re.search(r"lorem ipsum|ipsum dolor", src, re.I): err(p, "contains placeholder (Lorem ipsum) text")
    if "user-scalable=no" in src: err(p, "viewport blocks zoom (user-scalable=no)")
    if not (s.html and s.html.get("lang")): err(p, "missing <html lang>")
    if not (s.title and s.title.get_text(strip=True)): err(p, "missing <title>")
    if not is_redirect:
        if len(s.find_all("h1")) > 1: err(p, "more than one <h1>")
        if p in in_sitemap and not s.find("meta", attrs={"name": "description"}): err(p, "missing meta description")
        if p in in_sitemap and not s.find("link", rel="canonical"): warn(p, "missing canonical link")
    ids = [e["id"] for e in s.find_all(id=True)]
    for x in sorted({i for i in ids if ids.count(i) > 1}): err(p, f"duplicate id '{x}'")
    for i in s.find_all("img"):
        if i.get("alt") is None: err(p, f"<img src={i.get('src')}> has no alt attribute")
    for t in s.find_all("iframe"):
        if not t.get("title"): err(p, "iframe without title")
    for t in s.find_all("script", type="application/ld+json"):
        try: json.loads(t.string)
        except Exception as e: err(p, f"invalid JSON-LD: {e}")
    base = os.path.dirname(p)
    for tag, attr in (("a", "href"), ("img", "src"), ("link", "href"), ("script", "src"), ("source", "src"), ("video", "poster")):
        for e in s.find_all(tag):
            v = e.get(attr)
            if not v or v.startswith(("http", "//", "mailto:", "tel:", "data:", "javascript:")) or "${" in v: continue
            path, _, frag = v.partition("#"); path = path.split("?")[0]
            if path == "":
                if frag and frag not in ids: err(p, f"anchor #{frag} not found on this page")
                continue
            target = os.path.normpath(path[1:] if path.startswith("/") else os.path.join(base, unquote(path)))
            if not os.path.exists(target): err(p, f"<{tag} {attr}={v}> -> missing file {target}")
            elif frag and target.endswith(".html"):
                t2 = BeautifulSoup(open(target, encoding="utf-8", errors="replace").read(), "html.parser")
                if not t2.find(id=frag): err(p, f"anchor {v} not found in {target}")

for u in sorted(in_sitemap):
    if not os.path.exists(u): err("sitemap.xml", f"lists {u} but the file does not exist")

for css in sorted(f for f in os.listdir("assets/css") if f.endswith(".css") and f not in ("fontawesome-all.min.css",)):
    cpath = os.path.join("assets/css", css)
    for u in re.findall(r"url\(['\"]?([^)'\"]+)['\"]?\)", open(cpath, encoding="utf-8", errors="replace").read()):
        if u.startswith(("data:", "http", "#")): continue
        target = os.path.normpath(os.path.join("assets/css", u.split("?")[0].split("#")[0]))
        if not os.path.exists(target):
            (warn if target.startswith("assets/fonts") else err)(cpath, f"url({u}) -> missing file {target}" + (" (see assets/fonts/README.md)" if target.startswith("assets/fonts") else ""))

total = 0
for d, _, fs in os.walk("images"):
    for f in fs:
        sz = os.path.getsize(os.path.join(d, f)); total += sz
        if sz > MAX_IMAGE_BYTES: err(os.path.join(d, f), f"image is {sz/1e6:.1f} MB (limit {MAX_IMAGE_BYTES/1e6:.0f} MB) - resize/compress it")
print(f"Checked {len(pages)} pages; images total {total/1e6:.1f} MB")
for w in warnings: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
