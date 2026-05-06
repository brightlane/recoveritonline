#!/usr/bin/env node
const fs = require('fs-extra');
const path = require('path');
const Fuse = require('fuse.js');

const PAGES_DIR = './pages';
const GLOBAL_DIR = './pages-global';
const OUTPUT_FILE = './pages/index.html';

const CATEGORIES = {
  instagram: 'Instagram DM Automation',
  whatsapp: 'WhatsApp Lead Generation', 
  facebook: 'Messenger Bot Strategies',
  ecommerce: 'Abandoned Cart Flows',
  agency: 'Client Scaling Playbooks'
};

async function generateSuperIndex() {
  console.log('🏠 Vulture Super Index | 4,165+ page mega directory');
  
  // Scan all pages
  const pages = await scanAllPages();
  const categorized = categorizePages(pages);
  
  const html = buildIndexHTML(categorized);
  await fs.writeFile(OUTPUT_FILE, html);
  
  // Generate search index
  await fs.writeJson('./pages/search-index.json', pages, { spaces: 2 });
  
  console.log(`✅ Super Index LIVE: ${pages.length} strategies indexed`);
}

async function scanAllPages() {
  const allPages = [];
  
  // Local pages
  const localPages = await fs.readdir(PAGES_DIR);
  localPages
    .filter(f => /^vulture-page-\d+\.html$/.test(f))
    .forEach(file => {
      const num = parseInt(file.match(/\d+/)[0]);
      allPages.push({
        id: num,
        title: `ManyChat Strategy #${num}`,
        url: `vulture-page-${num}.html`,
        category: assignCategory(num),
        words: 8000,
        locale: 'en'
      });
    });
  
  // Global pages
  const globalPages = await fs.readdir(GLOBAL_DIR);
  globalPages
    .filter(f => /^vulture-page-\d+-(en|es|fr|de|it|us|uk|ca|au|eu|mx|br|ar)\.html$/.test(f))
    .forEach(file => {
      const [, num, geo] = file.match(/vulture-page-(\d+)-(.+)\.html/);
      allPages.push({
        id: parseInt(num),
        title: `Strategy #${num} (${geo.toUpperCase()})`,
        url: `../pages-global/${file}`,
        category: assignCategory(parseInt(num)),
        geo,
        locale: geo.includes('-') ? geo.split('-')[1] : 'en'
      });
    });
  
  return allPages.sort((a, b) => a.id - b.id);
}

function assignCategory(pageNum) {
  const catMap = {
    1: 'instagram', 50: 'whatsapp', 100: 'facebook',
    150: 'ecommerce', 200: 'agency'
  };
  return Object.entries(catMap).find(([num]) => pageNum <= parseInt(num))?.[1] || 'instagram';
}

function categorizePages(pages) {
  const categorized = {};
  for (const cat in CATEGORIES) {
    categorized[cat] = pages.filter(p => p.category === cat);
  }
  return categorized;
}

function buildIndexHTML(categorized) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ManyChat Automation Strategies Directory (4,165+ Guides)</title>
  <meta name="description" content="Complete ManyChat playbook. Instagram DMs, WhatsApp flows, FB Messenger bots. 8k-word guides with templates.">
  
  <style>
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui; line-height:1.6; background:#fafafa; }
    .header { background:#007cba; color:white; padding:2rem; text-align:center; }
    .search-box { max-width:600px; margin:2rem auto; padding:1rem; }
    .search-input { width:100%; padding:1rem; font-size:1.2rem; border:2px solid #ddd; border-radius:12px; }
    .categories { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:1rem; padding:2rem; }
    .category { background:white; border-radius:12px; padding:2rem; box-shadow:0 4px 12px rgba(0,0,0,0.1); }
    .category h2 { color:#007cba; margin-bottom:1rem; }
    .strategies { display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:1rem; }
    .strategy-card { background:#f8f9fa; padding:1.5rem; border-radius:8px; border-left:4px solid #007cba; }
    .strategy-card h3 { font-size:1.1rem; margin-bottom:0.5rem; }
    .strategy-card a { text-decoration:none; color:inherit; }
    .strategy-card:hover { background:white; transform:translateY(-2px); box-shadow:0 4px 12px rgba(0,124,186,0.2); }
    .cta { background:#ff6b35; color:white; padding:1rem 2rem; border-radius:8px; text-decoration:none; display:inline-block; margin:2rem auto; }
    .stats { text-align:center; padding:2rem; background:#e7f3ff; }
    .load-more { text-align:center; padding:2rem; }
    .hidden { display:none; }
    @media (max-width:768px) { .strategies { grid-template-columns:1fr; } }
  </style>
</head>
<body>
  <header class="header">
    <h1>🦅 ManyChat Master Directory</h1>
    <p>4,165+ automation strategies | 6.6M words | Live templates</p>
  </header>
  
  <div class="stats">
    <h2>Total Strategies: ${Object.values(categorized).reduce((a,b)=>a+b.length,0)}</h2>
    <a href="${MANYCHAT_CTA}" class="cta">🚀 Start ManyChat Pro Trial</a>
  </div>
  
  <div class="search-box">
    <input type="text" class="search-input" id="search" placeholder="Search strategies (Instagram, WhatsApp, abandoned cart...)">
  </div>
  
  <div class="categories" id="categories">
    ${Object.entries(categorized).map(([cat, pages]) => `
      <section class="category">
        <h2>${CATEGORIES[cat]} (${pages.length})</h2>
        <div class="strategies" data-category="${cat}">
          ${pages.slice(0,12).map(p => strategyCard(p)).join('')}
        </div>
        <button class="load-more" data-category="${cat}">Load More ${CATEGORIES[cat]}</button>
      </section>
    `).join('')}
  </div>
  
  <script>
    // Search index
    const searchIndex = ${JSON.stringify(await fs.readJson('./search-index.json'))};
    const fuse = new Fuse(searchIndex, {
      keys: ['title', 'category'],
      threshold: 0.3
    });
    
    // Search
    document.getElementById('search').addEventListener('input', (e) => {
      const results = fuse.search(e.target.value);
      document.querySelectorAll('.strategy-card').forEach(card => {
        card.classList.toggle('hidden', !e.target.value || 
          !results.some(r => r.item.id == card.dataset.id));
      });
    });
    
    // Infinite scroll per category
    document.querySelectorAll('.load-more').forEach(btn => {
      btn.addEventListener('click', () => {
        const cat = btn.dataset.category;
        const container = btn.previousElementSibling;
        const shown = container.children.length;
        const categoryPages = searchIndex.filter(p => p.category === cat);
        const nextBatch = categoryPages.slice(shown, shown + 12);
        
        nextBatch.forEach(page => {
          container.insertAdjacentHTML('beforeend', strategyCardHTML(page));
        });
      });
    });
    
    function strategyCardHTML(page) {
      return \`
        <div class="strategy-card" data-id="\${page.id}">
          <h3><a href="\${page.url}">\${page.title}</a></h3>
          <small>\${page.category.toUpperCase()} | \${page.geo || 'Global'} | 8k words</small>
        </div>
      \`;
    }
  </script>
</body>
</html>`;
}

function strategyCard(page) {
  return `
    <div class="strategy-card" data-id="${page.id}">
      <h3><a href="${page.url}">${page.title}</a></h3>
      <small>${page.category.toUpperCase()} | ${page.geo || 'EN'} | 8,000 words</small>
    </div>`;
}

// === EXECUTE ===
generateSuperIndex().catch(console.error);
