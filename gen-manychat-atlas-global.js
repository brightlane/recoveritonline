// gen-manychat-atlas-global.js
// ManyChat Atlas Runner – Global Edition
// 100k ManyChat affiliate funnels covering global users per run
// 100% ready to deploy

const fs = require("fs/promises");
const path = require("path");

// ── GLOBAL ERROR HANDLING ────────────────────────────────────
process.on("uncaughtException", (err) => {
  console.error("Uncaught Exception:", err);
  process.exit(1);
});
process.on("unhandledRejection", (reason, p) => {
  console.error("Unhandled Rejection at:", p, "reason:", reason);
  process.exit(1);
});

// ── YOUR MANYCHAT AFFILIATE LINKS (as in your snippet) ───────
const AFF = {
  default: "https://manychat.partnerlinks.io/nwkkk7vkps17",
  free: "https://manychat.partnerlinks.io/emwcbue22i01-ogcg6e",
  discount: "https://manychat.partnerlinks.io/t8let4hhqtqg-wki14",
  pricing: "https://manychat.partnerlinks.io/98hj6b3pr28k-4znb59",
  instagram: "https://manychat.partnerlinks.io/8k59yhm0l32j-z7dk2i",
};

// Simple rotation (A/B)
function getPrimaryOffer() {
  const options = [AFF.free, AFF.discount];
  return options[Math.floor(Math.random() * options.length)];
}

// ── GLOBAL CITIES (you can expand this list as needed) ───────
const globalCities = [
  "New York", "Los Angeles", "Chicago", "Houston", "Miami",
  "Toronto", "Vancouver", "Montreal", "Calgary",
  "London", "Manchester", "Birmingham", "Edinburgh",
  "Paris", "Marseille", "Lyon", "Bordeaux",
  "Berlin", "Munich", "Frankfurt", "Hamburg",
  "Rome", "Milan", "Florence", "Venice",
  "Madrid", "Barcelona", "Valencia", "Seville",
  "Amsterdam", "Rotterdam",
  "Stockholm", "Oslo", "Copenhagen",
  "Sydney", "Melbourne", "Brisbane",
  "Tokyo", "Osaka", "Kyoto",
  "Seoul", "Busan",
  "Singapore",
  "Bangkok",
  "Mumbai", "Delhi", "Bangalore",
  "São Paulo", "Rio de Janeiro",
  "Mexico City",
  "Dubai", "Abu Dhabi",
  "Johannesburg", "Cape Town",
  "Lagos",
  "Nairobi",
];

function pickGlobalCity() {
  return globalCities[Math.floor(Math.random() * globalCities.length)];
}

// ── RUN ID + PATH HELPERS ─────────────────────────────────────
function runId() {
  const now = new Date();
  return (
    now.toISOString().replace(/:/g, "").replace(/\.\d+/, "") +
    "-" +
    Math.floor(100000 + Math.random() * 900000)
  );
}

function runOutputDir(baseDir, id) {
  return path.join(baseDir, "runs", id);
}

function slugify(str) {
  return String(str)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

// ── SEO HEAD TEMPLATE (per page) ──────────────────────────────
function seoHead(runId, { slug, title, description, type = "WebPage" }) {
  const runSub = `run=${runId}`;
  const baseUrl = `https://brightlane.github.io/ManyChatAtlasGlobal`;
  const url = `${baseUrl}/${runSub}/${slug}.html`;

  const safeTitle = escHtml(title);
  const safeDesc = escHtml(description);

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${safeTitle}</title>
<meta name="description" content="${safeDesc}">
<link rel="canonical" href="${url}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<meta property="og:title" content="${safeTitle}">
<meta property="og:description" content="${safeDesc}">
<meta property="og:type" content="website">
<meta property="og:url" content="${url}">
<meta property="og:site_name" content="ManyChat Atlas Global">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${safeTitle}">
<meta name="twitter:description" content="${safeDesc}">
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"${type}",
  "name":"${safeTitle}",
  "url":"${url}",
  "publisher":{ 
    "@type":"Organization",
    "name":"ManyChat Atlas Global",
    "url":"https://brightlane.github.io/ManyChatAtlasGlobal"
  },
  "dateModified":"${new Date().toISOString().split("T")[0]}"
}
</script>
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://brightlane.github.io/ManyChatAtlasGlobal/index.html"},
    {"@type":"ListItem","position":2,"name":"${safeTitle.split(" | ")[0]}","item":"${url}"}
  ]
}
</script>`;
}

// ── SIMPLE CCS (SEO‑friendly) ────────────────────────────────
function sharedStyles() {
  return `
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,sans-serif;background:#fff;color:#2d1a22;line-height:1.7}
a{color:#ff5a00;text-decoration:none}
a:hover{text-decoration:underline}
img{max-width:100%}
h2{font-size:1.5rem;color:#2d1a22;margin:1.2em 0 0.6em}
h3{font-size:1.25rem;color:#2d1a22;margin:1em 0 0.5em}
p{margin:0.6em 0;font-size:16px;line-height:1.7}
ul{margin:0.6em 0 0.6em 1.5em;list-style: square}
ol{margin:0.6em 0 0.6em 1.5em;list-style: decimal}
li{margin:0.3em 0}
section{margin-bottom:1em}
.btn-manychat{display:block;background:#ff5a00;color:#fff;padding:0.6em 1.2em;margin:0.6em 0;text-align:center;border-radius:8px;font-weight:bold;font-size:16px;text-decoration:none;box-shadow:0 2px 6px rgba(0,0,0,0.2)}
</style>`;
}

// ── NAV & FOOTER (with ManyChat links) ───────────────────────
function nav(runId) {
  const runSub = `run=${runId}`;
  const baseUrl = `https://brightlane.github.io/ManyChatAtlasGlobal`;
  const primaryOffer = getPrimaryOffer();

  const navHtml = `<nav style="background:#fff;border-bottom:1px solid #f0d0da;padding:0.8em 1.5em">
  <a href="https://brightlane.github.io/ManyChatAtlasGlobal/" style="font-weight:700;color:#2d1a22;text-decoration:none;font-size:15px">
    ManyChat Atlas Global
  </a>
  <a href="${AFF.default}" target="_blank" rel="nofollow sponsored" style="margin-left:1.5em;background:#ff5a00;color:#fff;padding:0.5em 1em;border-radius:20px;font-size:14px;text-decoration:none">
    Start Free ManyChat
  </a>
  <a href="${AFF.pricing}" target="_blank" rel="nofollow sponsored" style="margin-left:1.5em;background:#555;color:#fff;padding:0.5em 1em;border-radius:20px;font-size:14px;text-decoration:none">
    Pricing Plans
  </a>
</nav>`;

  return navHtml;
}

function footer(runId) {
  const runSub = `run=${runId}`;
  const baseUrl = `https://brightlane.github.io/ManyChatAtlasGlobal`;

  return `<footer style="background:#2d1a22;color:#fff;padding:1.2em 1.5em;text-align:center;font-size:12px">
  <div>
    &copy; 2026 ManyChat Atlas Global &nbsp;•&nbsp;
    Independent ManyChat review site serving worldwide users &nbsp;•&nbsp;
    <a href="${AFF.default}" target="_blank" rel="nofollow sponsored" style="color:#fff;text-decoration:underline">
      Sign Up via PartnerLink
    </a>
    <br><br>
    <span style="color:#ccc">Affiliate links may earn commissions at no extra cost to you.</span>
  </div>
</footer>`;
}

// ── PAGE TITLE / DESC (global ManyChat angle) ─────────────────
function pageTitleDesc(wp) {
  const topics = [
    "ManyChat free plan global",
    "ManyChat Pro discount for worldwide users",
    "Instagram DM automation with ManyChat globally",
    "ManyChat for eCommerce worldwide",
    "WhatsApp automation with ManyChat across countries",
    "ManyChat for Shopify merchants worldwide",
    "Facebook Messenger bots with ManyChat – 2026",
    "Kajabi + ManyChat workflows for global creators",
    "TikTok + ManyChat for worldwide audiences",
    "1‑month free ManyChat Pro for everyone",
  ];

  const city = pickGlobalCity();
  const topic = topics[wp % topics.length];
  const adjectives = ["2026", "2027", "step‑by‑step", "complete", "beginner‑friendly"];

  const title = `${topic} Guide ${adjectives[wp % adjectives.length]} in ${city} | ManyChat Atlas Global`;
  const description = `Learn how to use ${topic.toLowerCase()} with ManyChat for global audiences, including free month offers and discounts available to users worldwide. Use our affiliate links to get special pricing.`;

  return { title, description, topic, city };
}

// ── PAGE BUILD (with embedded CTAs like your JS) ─────────────
async function buildPage({ runId, wp, slug, title, description, city }) {
  const primaryOffer = getPrimaryOffer();

  const content = `<section class="intro">
  <p>This page explains how to use ManyChat for ${pageTitleDesc(wp).topic.toLowerCase()} in ${city}, including free and discounted plans available worldwide through our affiliate links.</p>
</section>

<section class="why-manychat">
  <h2>Why use ManyChat globally?</h2>
  <p>ManyChat lets you automate Messenger, WhatsApp, Instagram, SMS, email, and TikTok messaging for customers anywhere in the world. It’s used by creators, agencies, and e‑commerce brands across continents.</p>
</section>

<section class="get-started">
  <h2>Get started with ManyChat</h2>
  <p>Click below to create an account or upgrade to a paid plan with our affiliate offers, available to users worldwide.</p>
  <a href="${AFF.free}" class="btn-manychat" target="_blank" rel="nofollow sponsored">🔥 Get 1 Month FREE ManyChat Pro</a>
  <a href="${AFF.discount}" class="btn-manychat" target="_blank" rel="nofollow sponsored">💸 Get 50% Off ManyChat Pro</a>
  <a href="${primaryOffer}" class="btn-manychat" target="_blank" rel="nofollow sponsored">👉 Start ManyChat Free Plan</a>
</section>

<section class="instagram-automation">
  <h2>Automate Instagram DMs with ManyChat</h2>
  <p>If you want to automate Instagram DM follow‑ups from around the world, use the link below.</p>
  <a href="${AFF.instagram}" class="btn-manychat" target="_blank" rel="nofollow sponsored">🚀 Automate Instagram DMs Now</a>
</section>`;

  const pageHtml = `${seoHead(runId, {
    slug,
    title,
    description,
  })}
${sharedStyles()}
</head>
<body>
${nav(runId)}

<div class="breadcrumb" style="max-width:600px;margin:0.8em 1.5em;font-size:13px;color:#7a4a58">
  <a href="https://brightlane.github.io/ManyChatAtlasGlobal/">Home</a> &rsaquo; ${escHtml(title.split(" | ")[0])}
</div>

<div class="hero" style="background:#fdf0f4;padding:1.5em 1.5em;text-align:center">
  <h1 style="font-size:1.8em;color:#2d1a22;margin-bottom:0.4em">${escHtml(title.split(" | ")[0])}</h1>
  <p style="color:#7a4a58;margin-bottom:1em;font-size:14px">${escHtml(description)}</p>
  <a href="${AFF.default}" target="_blank" rel="nofollow sponsored" class="btn-manychat">Get Started with ManyChat</a>
</div>

<div class="main-content" style="max-width:720px;margin:0 auto 2em;padding:0 1.5em;font-size:16px;color:#2d1a22;line-height:1.7">
  ${content}
</div>

${footer(runId)}
</body>
</html>`;

  return pageHtml;
}

// ── SITEMAP CHUNKS + INDEX + robots.txt (global) ─────────────
async function generateSitemaps(runId, pages, outputDir) {
  const today = new Date().toISOString().split("T")[0];
  const sitemapChunkSize = 50000;
  const chunks = [];
  for (let i = 0; i < pages.length; i += sitemapChunkSize) {
    chunks.push(pages.slice(i, i + sitemapChunkSize));
  }

  const sitemapPaths = [];
  for (let i = 0; i < chunks.length; i++) {
    const urls = chunks[i].map((p) =>
      `https://brightlane.github.io/ManyChatAtlasGlobal/flowerguides/run=${runId}/${p.slug}.html`
    );
    const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((loc) => `  <url>
    <loc>${loc}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>`).join("\n")}
</urlset>`;
    const sitemapFile = `sitemap-${i}.xml`;
    await fs.writeFile(path.join(outputDir, sitemapFile), xml);
    sitemapPaths.push(sitemapFile);
  }

  const indexXml = `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapPaths.map((file) => `  <sitemap>
    <loc>https://brightlane.github.io/ManyChatAtlasGlobal/flowerguides/run=${runId}/${file}</loc>
    <lastmod>${today}</lastmod>
  </sitemap>`).join("\n")}
</sitemapindex>`;
  await fs.writeFile(path.join(outputDir, "sitemap-index.xml"), indexXml);

  const robotsTxt = `User-agent: *
Allow: /

Sitemap: https://brightlane.github.io/ManyChatAtlasGlobal/flowerguides/run=${runId}/sitemap-index.xml`;
  await fs.writeFile(path.join(outputDir, "robots.txt"), robotsTxt);
}

// ── MAIN LOOP (100k pages per run, global cities) ─────────────
async function runManyChatAtlas() {
  const run = runId();
  const outputDir = runOutputDir(".", run);
  await fs.mkdir(outputDir, { recursive: true });

  const pages = [];
  const totalPages = 100000;

  console.log(`\n🌐 Generating ${totalPages} global ManyChat affiliate pages (run '${run}')`);

  for (let wp = 0; wp < totalPages; wp++) {
    const info = pageTitleDesc(wp);
    const slug = `mc-${wp + 1}-${slugify(info.topic)}-${slugify(info.city)}`;

    const html = await buildPage({
      runId: run,
      wp,
      slug,
      title: info.title,
      description: info.description,
      city: info.city,
    });

    const file = path.join(outputDir, `${slug}.html`);
    await fs.writeFile(file, html);

    pages.push({ slug, url: `https://brightlane.github.io
