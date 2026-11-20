"""Switch the website to its real domain in one step.

    python tools/set_domain.py sharplinerenovation.co.za

- replaces the current domain in every page, the sitemap, robots.txt and the area-page generator
- writes site/CNAME so GitHub Pages serves the site on that domain
Commit and push afterwards; GitHub redeploys automatically.
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SITE = os.path.join(ROOT, "site")

if len(sys.argv) != 2:
    sys.exit("usage: python tools/set_domain.py example.co.za")
new = sys.argv[1].strip().lower()
new = re.sub(r"^https?://", "", new).strip("/")
if new.startswith("www."):
    new = new[4:]

gen = os.path.join(HERE, "build_areas.py")
old = re.search(r'DOMAIN = "https://([^"]+)"', open(gen, encoding="utf-8").read()).group(1)
if old == new:
    print(f"already set to {new}")
files = glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True) + \
        [os.path.join(SITE, "sitemap.xml"), os.path.join(SITE, "robots.txt"), gen]
changed = 0
for f in files:
    t = open(f, encoding="utf-8").read()
    n = t.replace(f"https://{old}", f"https://{new}").replace(f"@{old}", f"@{new}")
    if n != t:
        open(f, "w", encoding="utf-8").write(n)
        changed += 1
open(os.path.join(SITE, "CNAME"), "w").write(new + "\n")
print(f"{old} -> {new}: updated {changed} files and wrote site/CNAME")
