// generate-sitemap.js - Sitemap generator for your ManyChat vulture pages (updated BASE_URL version)
const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://manychat.com';  // Update this to your deployed site URL
const PAGES_DIR = './pages';  // Directory with vulture-page-*.html files
const SITEMAP_PATH = './sitemap.xml';

function generateSitemap() {
  // Collect all HTML files from pages directory
  const files = fs.readdirSync(PAGES_DIR).filter(file => file.endsWith('.html') && !file.includes('index.html'));
  
  // Sort for consistent ordering
  files.sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));

  let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${BASE_URL}/</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>`;

  files.forEach(file => {
    const urlPath = path.join(PAGES_DIR, file).replace('\\', '/');
    const loc = `${BASE_URL}/${file}`;
    const lastmod = new Date().toISOString().split('T')[0];
    
    xml += `
  <url>
    <loc>${loc}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>`;
  });

  xml += `
</urlset>`;

  fs.writeFileSync(SITEMAP_PATH, xml);
  console.log(`Sitemap generated with ${files.length + 1} URLs: ${SITEMAP_PATH}`);
}

generateSitemap();
