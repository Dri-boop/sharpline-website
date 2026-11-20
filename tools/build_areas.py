"""Builds one SEO page per suburb (site/areas/<slug>/index.html), the areas hub (site/areas/index.html),
the area links on the home page and sitemap.xml.

Run from the project folder:   python tools/build_areas.py
Edit suburb content in tools/areas_data.py. When Charles confirms a real project in a suburb, add
real_photos=["kitchen-07", ...] to that suburb's entry: those photos are then captioned with the suburb.
"""
import html, json, math, os, re, sys
from datetime import date
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from areas_data import AREAS, REGIONS, WORKSHOP  # noqa: E402

SITE = os.path.join(HERE, "..", "site")
DOMAIN = "https://sharplinerenovation.co.za"   # TODO: real domain
BRAND = "Sharpline Renovation & Woodworks"
PHONE = "+27 67 617 7735"
TEL = "+27676177735"
E = html.escape

PHOTO_POOLS = {
    "pool":      ["outdoor-01", "outdoor-02"],
    "heritage":  ["doors-03", "doors-21", "doors-11", "doors-04", "doors-12", "kitchen-20", "doors-16", "wardrobe-03"],
    "compact":   ["kitchen-27", "kitchen-09", "kitchen-31", "kitchen-11", "kitchen-28", "kitchen-13", "kitchen-19", "wardrobe-06"],
    "family":    ["kitchen-01", "kitchen-25", "kitchen-02", "kitchen-26", "kitchen-04", "kitchen-30", "kitchen-07", "kitchen-29",
                  "kitchen-14", "kitchen-05", "doors-02", "wardrobe-02", "wardrobe-04", "doors-10"],
    "coastal":   ["doors-01", "doors-19", "kitchen-24", "doors-06", "doors-08"],
    "rental":    ["kitchen-21", "kitchen-17", "wardrobe-09", "kitchen-12", "furniture-13", "kitchen-27"],
    "apartment": ["kitchen-15", "kitchen-24", "wardrobe-05", "kitchen-10", "wardrobe-11", "tv-04"],
}


def km(a, b):
    (la1, lo1), (la2, lo2) = a, b
    r = 6371
    p1, p2 = math.radians(la1), math.radians(la2)
    d = math.sin(math.radians(la2 - la1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lo2 - lo1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(d))


def road(a):
    k = max(1.0, km(WORKSHOP, (a["lat"], a["lon"])) * 1.35)
    mins = max(5, int(round((k / 28 * 60 + 3) / 5.0) * 5))
    return round(k), mins


def captions_from_home():
    t = open(os.path.join(SITE, "index.html"), encoding="utf-8").read()
    caps = {}
    for name, cap in re.findall(r'img/([a-z]+-\d+)-sm\.jpg".*?<figcaption class="mono">(.*?) <span>', t):
        caps[name] = html.unescape(cap)
    return caps


def pick_photos(area, i):
    if area.get("real_photos"):
        return area["real_photos"][:6], True
    chosen, pools = [], [PHOTO_POOLS[p] for p in area["profile"]]
    k = 0
    while len(chosen) < 6 and k < 60:
        pool = pools[k % len(pools)]
        cand = pool[(i + k // len(pools)) % len(pool)] if pool is not PHOTO_POOLS["pool"] else pool[(k // len(pools)) % len(pool)]
        if cand not in chosen:
            chosen.append(cand)
        k += 1
    return chosen, False


def header(root):
    return f'''<a class="sr-only" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{root}" aria-label="{E(BRAND)} home">
      <span class="logo-word">SHARPLINE</span>
      <span class="saw" aria-hidden="true"></span>
      <small>RENOVATION &amp; WOODWORKS</small>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Open menu"><span></span><span></span><span></span></button>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="{root}#services">Services</a>
      <a href="{root}#prices">Pricing</a>
      <a href="{root}#work">Our work</a>
      <a href="{root}areas/">Areas</a>
      <a href="{root}#about">Who we are</a>
      <a class="nav-cta" href="#" data-wa-area>Quote 24/7</a>
    </nav>
  </div>
</header>'''


def footer(root):
    return f'''<footer class="site-footer">
  <div class="wrap">
    <p class="footer-big" aria-hidden="true">Sharpline</p>
    <span class="saw" aria-hidden="true"></span>
    <div class="footer-grid mono">
      <span>© <span id="year">{date.today().year}</span> {E(BRAND)} · Unit 4, 7th Avenue Business Park, Maitland, Cape Town</span>
      <span><a href="{root}areas/">Areas we serve</a> · Anywhere in South Africa</span>
      <span><a href="#" data-wa>WhatsApp {PHONE}</a> · <a href="#top">Back to top ↑</a></span>
    </div>
  </div>
</footer>
<nav class="mobile-bar" aria-label="Quick contact">
  <a href="tel:{TEL}">Call</a>
  <a href="#" data-wa-area class="mb-wa">WhatsApp</a>
  <a href="{root}#contact">Quote</a>
</nav>
<a class="wa-float" href="#" data-wa-area aria-label="Chat on WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Z"/></svg></a>
<script src="{root}area.js"></script>'''


def head(title, desc, canonical, root, ld):
    return f'''<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#1b1a18">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_ZA">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Unbounded:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}styles.css">
<script type="application/ld+json">
{json.dumps(ld, indent=1, ensure_ascii=False)}
</script>
</head>'''


def business_ld(area_name=None):
    d = {
        "@type": "HomeAndConstructionBusiness", "@id": f"{DOMAIN}/#business", "name": BRAND,
        "url": f"{DOMAIN}/", "telephone": TEL, "image": f"{DOMAIN}/img/kitchen-01.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": "Unit 4, 7th Avenue Business Park",
                    "addressLocality": "Maitland, Cape Town", "postalCode": "7405", "addressRegion": "Western Cape", "addressCountry": "ZA"},
    }
    if area_name:
        d["areaServed"] = {"@type": "Place", "name": f"{area_name}, Cape Town"}
    return d


def area_page(a, i, caps, nearby):
    root = "../../"
    name, slug = a["name"], a["slug"]
    dist, mins = road(a)
    photos, real = pick_photos(a, i)
    title = f"Carpenter & Renovations in {name} | {BRAND}"
    desc = (f"Renovation and woodwork in {name}, Cape Town: kitchens, built-in cupboards, doors, garage doors"
            f"{', pool decks' if 'pool' in a['profile'] else ''} and furniture. Workshop {mins} min away in Maitland. Quotes 24/7, fixed prices.")
    canonical = f"{DOMAIN}/areas/{slug}/"
    faqs = [
        (f"Do you work in {name}?", f"Yes. Our workshop is in Maitland, about {dist} km from {name} (roughly {mins} minutes' drive), so we can come out to measure and quote quickly."),
        (f"How much does a renovation or carpentry job in {name} cost?", "Every job is priced for your space, materials and finishes. After a free site visit you get a written, itemised quote, and once you accept it the price is fixed: we never come back to ask for more."),
        (f"How do I get a quote in {name}?", "WhatsApp us photos and rough measurements, any time, 24/7. We'll reply with next steps and arrange a free site visit."),
        a["faq"],
    ]
    ld = {"@context": "https://schema.org", "@graph": [
        business_ld(name),
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": "Areas", "item": f"{DOMAIN}/areas/"},
            {"@type": "ListItem", "position": 3, "name": name, "item": canonical}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in faqs]},
    ]}
    services = [
        ("Kitchen renovations", f"New kitchens and kitchen refits in {name}: cabinets, islands, sculleries and worktops, designed around how you cook."),
        ("Built-in cupboards", f"Built-in cupboards and wardrobes for {name} homes, from single alcoves to full walls with sliding doors."),
        ("Doors, garage doors & gates", "Front doors, stable doors, security doors, aluminium and glass garage doors, and gates."),
        ("Woodwork & custom furniture", "Beds, drawers, counters, tables and commercial furniture, made in our Maitland workshop."),
        ("Pool decks & outdoor timber" if "pool" in a["profile"] or "coastal" in a["profile"] else "Home renovations",
         "Hardwood decks, pool decks and hot-tub surrounds built for sun, water and salt air." if "pool" in a["profile"] or "coastal" in a["profile"]
         else "Flooring, vanities and general home improvements, done properly and left clean."),
        ("Fixed-price quotes, 24/7", "Send your request day or night. Once you accept the written quote, the price doesn't change."),
    ]
    figs = []
    for p in photos:
        w, h = Image.open(os.path.join(SITE, "img", f"{p}-sm.jpg")).size
        cap = caps.get(p, "Our work")
        label = f"{cap} · {name}" if real else cap
        alt = f"{cap}, {'in ' + name + ', ' if real else ''}by {BRAND}"
        figs.append(f'<figure><img src="{root}img/{p}-sm.jpg" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{E(alt)}"><figcaption class="mono">{E(label)}</figcaption></figure>')
    gallery_title = f"Our work in {name}" if real else "Examples of our work"
    gallery_note = "" if real else f"<p class=\"area-note\">A selection from our projects across Cape Town. We're adding more {E(name)} projects soon.</p>"
    nb = "".join(f'<li><a href="../{n["slug"]}/">{E(n["name"])}</a></li>' for n in nearby)
    jobs = "".join(f"<li>{E(j)}</li>" for j in a["jobs"])
    svc = "".join(f'<li><h3>{E(t)} <span>in {E(name)}</span></h3><p>{E(d)}</p></li>' for t, d in services)
    faq_html = "".join(f"<details><summary>{E(q)}</summary><p>{E(ans)}</p></details>" for q, ans in faqs)

    return f'''{head(title, desc, canonical, root, ld)}
<body data-area="{E(name)}">
{header(root)}
<main id="main">
<section class="area-hero">
  <div class="wrap">
    <nav class="crumbs mono" aria-label="Breadcrumb"><a href="{root}">Home</a> / <a href="../">Areas</a> / <span>{E(name)}</span></nav>
    <span class="hero-kicker mono">Carpenter · Joiner · Renovations — {E(name)}, Cape Town</span>
    <h1>Renovation &amp; woodworks in <span class="hl">{E(name)}</span></h1>
    <p class="area-lede">{E(a["intro"])} Kitchens, built-in cupboards, doors and renovations, quoted at a fixed price.</p>
    <div class="hero-actions">
      <a class="btn btn--wa" href="#" data-wa-area>Get a quote in {E(name)}</a>
      <a class="btn btn--ghost" href="tel:{TEL}">Call {PHONE}</a>
    </div>
    <ul class="area-facts mono">
      <li><b>~{dist} km</b> from our Maitland workshop</li>
      <li><b>~{mins} min</b> drive</li>
      <li><b>24/7</b> quote requests</li>
      <li><b>Fixed</b> price, no surprises</li>
    </ul>
  </div>
</section>
<div class="saw saw--band" aria-hidden="true"></div>

<section class="sec area-homes">
  <div class="wrap area-two">
    <div>
      <h2 class="sec-title">Homes in {E(name)}</h2>
      <p>{E(a["homes"])}</p>
    </div>
    <div class="area-jobs">
      <h3 class="mono">What we're often asked to do in {E(name)}</h3>
      <ul>{jobs}</ul>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="sec-title">Carpentry &amp; renovation services in {E(name)}</h2>
    <ul class="area-services">{svc}</ul>
  </div>
</section>

<section class="sec work">
  <div class="wrap">
    <h2 class="sec-title">{gallery_title}</h2>
    {gallery_note}
    <div class="area-gallery">{"".join(figs)}</div>
    <p style="margin-top:22px"><a class="btn" href="{root}#work" style="background:var(--sawdust);color:var(--ink)">See all our projects</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="firm-price">
      <span class="firm-stamp" aria-hidden="true">Fixed<br>price</span>
      <div>
        <h3>Our price is our price.</h3>
        <p>Once you accept your quote in {E(name)}, the price is fixed. No surprise extras.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap area-two">
    <div>
      <h2 class="sec-title">Questions from {E(name)}</h2>
      <div class="faq">{faq_html}</div>
    </div>
    <div>
      <div class="advice">
        <h3>Not sure what you need? Ask Charles.</h3>
        <p>Send a photo of your space and Charles Zeka, with 15+ years in carpentry and renovation, will give you his honest recommendation.</p>
        <a class="btn btn--wa" href="#" data-wa-area>Ask Charles on WhatsApp</a>
      </div>
      <div class="areas" style="margin-top:28px">
        <h3 class="mono">Also near {E(name)}</h3>
        <ul class="mono">{nb}</ul>
        <p class="areas-all">Examples of recent work areas. We work anywhere in South Africa. <a href="../">All areas →</a></p>
      </div>
    </div>
  </div>
</section>
</main>
{footer(root)}
</body>
</html>
'''


def hub_page():
    root = "../"
    title = f"Areas we serve | {BRAND}"
    desc = "Carpentry and renovation from our workshop in Maitland, Cape Town, for projects anywhere in South Africa. Examples of recent work areas: Woodstock, Observatory, Gardens, Sea Point, Rondebosch, Pinelands, Milnerton and more."
    groups = ""
    for ri, rname in enumerate(REGIONS):
        items = "".join(f'<li><a href="{x["slug"]}/"><b>{E(x["name"])}</b><span>~{road(x)[1]} min from the workshop</span></a></li>'
                        for x in AREAS if x["region"] == ri)
        groups += f'<h2 class="sec-title hub-region">{E(rname)}</h2><ul class="hub-list">{items}</ul>'
    ld = {"@context": "https://schema.org", "@graph": [business_ld()]}
    return f'''{head(title, desc, f"{DOMAIN}/areas/", root, ld)}
<body data-area="Cape Town">
{header(root)}
<main id="main">
<section class="area-hero">
  <div class="wrap">
    <nav class="crumbs mono" aria-label="Breadcrumb"><a href="{root}">Home</a> / <span>Areas</span></nav>
    <span class="hero-kicker mono">Carpentry &amp; renovations — anywhere in South Africa</span>
    <h1>Areas we <span class="hl">serve</span></h1>
    <p class="area-lede">We're based in Maitland, Cape Town, and we take on projects <b>anywhere in South Africa</b>. The areas below are examples of where we've worked recently, not a complete list. Pick one to see what we do there, or just send us your project wherever you are.</p>
  </div>
</section>
<div class="saw saw--band" aria-hidden="true"></div>
<section class="sec"><div class="wrap">{groups}
<div class="nationwide">
  <h2>Not in Cape Town? We still work with you.</h2>
  <p>These are examples of recent work areas only. We serve clients across the Western Cape and the rest of South Africa. Send us photos and your location on WhatsApp and we'll tell you how we can help.</p>
  <a class="btn btn--wa" href="#" data-wa-area>Ask about your area</a>
</div>
</div></section>
</main>
{footer(root)}
</body>
</html>
'''


def main():
    caps = captions_from_home()
    for i, a in enumerate(AREAS):
        others = sorted((x for x in AREAS if x is not a), key=lambda x: km((a["lat"], a["lon"]), (x["lat"], x["lon"])))[:5]
        d = os.path.join(SITE, "areas", a["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(area_page(a, i, caps, others))
    open(os.path.join(SITE, "areas", "index.html"), "w", encoding="utf-8").write(hub_page())

    # home page: area links
    hp = os.path.join(SITE, "index.html")
    t = open(hp, encoding="utf-8").read()
    links = "".join(f'<li><a href="areas/{x["slug"]}/">{E(x["name"])}</a></li>' for x in AREAS)
    box = ('<div class="areas">\n        <h3 class="mono">Recent work areas</h3>\n'
           '        <p class="areas-intro">We work anywhere in South Africa. These are examples of areas where we\'ve worked recently.</p>\n'
           f'        <ul class="mono">{links}</ul>\n        <p class="areas-all"><a href="areas/">All areas we serve →</a></p>\n      </div>')
    t, n = re.subn(r'<div class="areas">.*?</ul>\s*(?:<p class="areas-all">.*?</p>\s*)?</div>', lambda m: box, t, count=1, flags=re.S)
    assert n == 1
    if 'href="areas/">Areas</a>' not in t:
        t = t.replace('<a href="#about">Who we are</a>', '<a href="areas/">Areas</a>\n      <a href="#about">Who we are</a>', 1)
    open(hp, "w", encoding="utf-8").write(t)

    # sitemap
    today = date.today().isoformat()
    urls = [f"{DOMAIN}/", f"{DOMAIN}/areas/"] + [f"{DOMAIN}/areas/{a['slug']}/" for a in AREAS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8").write(sm)
    print(f"built {len(AREAS)} area pages + hub; sitemap has {len(urls)} URLs")


if __name__ == "__main__":
    main()
