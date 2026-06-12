# RecoverIt SEO Site v2

> Affiliate promotional site for Wondershare Recoverit — data recovery software with 99.5% recovery success rate.

**Live site:** https://brightlane.github.io/recoveritonline/

---

## What This Repo Does

A single Python build script (`build.py`) generates a complete data recovery affiliate site into `dist/`. A GitHub Actions workflow cleans old files, then deploys the new site to GitHub Pages — triggered manually.

```
build.py   ←  the only file you need to edit or commit
```

---

## Quick Start

### Repo needs these files:

```
recoveritonline/
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

### Enable GitHub Pages

1. **Settings → Pages**
2. Source: **GitHub Actions**
3. Save

### Run the workflow

**Actions → Build & Deploy RecoverIt → Run workflow**

The workflow automatically:
1. Deletes all old files from the repo root (keeps only `build.py` and `README.md`)
2. Builds 1,687 files into `dist/`
3. Deploys to GitHub Pages

---

## What Gets Built

| Content | Count |
|---|---|
| Essential pages | 11 |
| Keyword-targeted pages | 244 |
| Blog posts | 15 |
| Sitemap URLs | 269 |
| Total files | ~1,687 |
| Total size | ~45 MB |

### Essential Pages

| File | Description |
|---|---|
| `index.html` | Homepage — 12-scenario hub, features, testimonials |
| `features.html` | Full feature list with 5-tool comparison table |
| `how-it-works.html` | 3-step guide + Quick vs Deep Scan explainer |
| `faq.html` | 21 FAQs with FAQPage schema |
| `compare.html` | Recoverit vs Disk Drill, EaseUS, Recuva, Stellar |
| `blog.html` | Blog index — 15 full articles |
| `download.html` | Download CTA with system requirements |
| `keywords.html` | All 244 topics by category |
| `glossary.html` | 25 data recovery terms defined |
| `privacy.html` | Privacy policy + affiliate disclosure |
| `404.html` | Branded 404 with auto-redirect |

### Blog Posts (in `blog/`)

1. How to Recover Deleted Photos in 2025
2. How to Recover Deleted Videos — GoPro, Drone & Camera
3. SD Card Data Recovery — Complete Guide
4. Recover Data From a Computer That Won't Start
5. USB Drive Data Recovery
6. Recover Data After Formatting a Drive
7. How to Prevent Data Loss
8. GoPro Video Recovery
9. NAS Data Recovery — Synology, QNAP & WD
10. Recoverit vs Disk Drill — Which Is Better in 2025?
11. Recover Permanently Deleted Files on Windows
12. How to Repair Corrupted Video Files
13. Best Data Recovery Software in 2025 — Ranked & Reviewed
14. How to Recover Files After a Ransomware Attack
15. Recover Deleted Photos From Any Digital Camera

### Keyword Categories (14)

`brand` · `general` · `device` · `filetype` · `scenario` · `platform` · `camera` · `compare` · `howto` · `global` · `business` · `pricing` · `video-repair` · `nas`

### Support Files

| File | Purpose |
|---|---|
| `sitemap.xml` | 269 URLs for Google Search Console |
| `robots.txt` | Directs crawlers to sitemap |
| `llms.txt` | AI assistant / crawler discovery |
| `_config.yml` | GitHub Pages — disables Jekyll |
| `.nojekyll` | GitHub Pages — serves HTML directly |
| `build-report.json` | Build stats and metadata |

---

## SEO Features

Every page includes:

- Unique `<title>` and `<meta description>`
- `<link rel="canonical">` for `https://brightlane.github.io/recoveritonline/`
- Open Graph + Twitter Card tags
- `SoftwareApplication` schema (Recoverit product + aggregate rating)
- `BreadcrumbList` schema
- `FAQPage` schema per page
- `Article` schema on blog posts with `datePublished` / `dateModified`
- Internal linking mesh — 24 related topics per keyword page
- `robots: index, follow`

---

## Editing the Build Script

Config at the top of `build.py`:

```python
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949095043004532&atid=recoveritwebs"
SITE_DOMAIN   = "https://brightlane.github.io/recoveritonline"
BASE_PATH     = "/recoveritonline"
```

### Adding Keywords

```python
kw("your-slug", "Your Keyword Phrase", "category")
```

Slugs must be unique — duplicates are silently skipped.

### Adding Blog Posts

```python
{
    "slug": "your-post-slug",
    "title": "Your Post Title",
    "excerpt": "One sentence summary.",
    "cat": "Category",
    "read": "5 min",
    "date": "2025-12-01",
    "body": "<h2>Heading</h2><p>Content in HTML...</p>"
}
```

### Adding a New Keyword Category

1. Add keywords with `kw("slug", "keyword", "new-cat")`
2. Add a colour to `COLORS` dict
3. Add a description to `CAT_DESC` dict
4. Optionally add a rich content template to `cat_deep()`

---

## Affiliate Disclosure

All links use:

```
https://www.linkconnector.com/ta.php?lc=007949095043004532&atid=recoveritwebs
```

Links are marked `rel="nofollow sponsored"`. Disclosure in footer and privacy page — FTC and Google compliant.

---

## License

For use on this affiliate project only. Recoverit is a product of Wondershare Technology Co., Ltd.
