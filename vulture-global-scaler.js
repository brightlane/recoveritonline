#!/usr/bin/env node
const fs = require('fs-extra');
const path = require('path');
const cheerio = require('cheerio');

const MANYCHAT_CTA = "https://manychat.partnerlinks.io/nwkkk7vkps17";
const SOURCE_DIR = './pages';
const TARGET_BASE = './pages-global';
const LOCALES = ['en', 'es', 'fr', 'de', 'it'];
const GEOS = ['us', 'uk', 'ca', 'au', 'eu', 'mx', 'br', 'ar', 'de', 'fr', 'it', 'es'];

const GEO_AFFILIATES = {
  us: `${MANYCHAT_CTA}?geo=us`,
  uk: `${MANYCHAT_CTA}?geo=uk`,
  ca: `${MANYCHAT_CTA}?geo=ca`,
  au: `${MANYCHAT_CTA}?geo=au`,
  eu: `${MANYCHAT_CTA}?geo=eu`,
  mx: `${MANYCHAT_CTA}?geo=mx`,
  br: `${MANYCHAT_CTA}?geo=br`,
  ar: `${MANYCHAT_CTA}?geo=ar`
};

const CURRENCY_MAP = {
  us: { symbol: '$', leadsCost: 2.50 },
  uk: { symbol: '£', leadsCost: 2.00 },
  ca: { symbol: 'CAD$', leadsCost: 3.20 },
  au: { symbol: 'AUD$', leadsCost: 3.80 },
  eu: { symbol: '€', leadsCost: 2.30 }
};

const LOCALE_TRANSLATORS = {
  es: { 
    title: 'Guía de Automatización ManyChat',
    cta: '¡Empieza Gratis Ahora!',
    roi: 'Calculadora ROI'
  },
  fr: {
    title: 'Guide Automatisation ManyChat',
    cta: 'Démarrer Gratuitement!',
    roi: 'Calculateur ROI'
  },
  de: {
    title: 'ManyChat Automatisierungs-Guide',
    cta: 'Kostenlos Starten!',
    roi: 'ROI Rechner'
  },
  it: {
    title: 'Guida Automazione ManyChat',
    cta: 'Inizia Gratis!',
    roi: 'Calcolatore ROI'
  }
};

// === MAIN SCALER ===
async function scaleGlobal() {
  console.log('🌍 Vulture Global Scaler v1.0 | 833 → 4,165 pages');
  
  await fs.ensureDir(TARGET_BASE);
  
  const sourceFiles = await fs.readdir(SOURCE_DIR);
  const vulturePages = sourceFiles.filter(f => /^vulture-page-\d+\.html$/.test(f));
  
  console.log(`📊 Source: ${vulturePages.length} English pages found`);
  
  let totalGenerated = 0;
  
  for (const sourceFile of vulturePages) {
    const pageNum = parseInt(sourceFile.match(/\d+/)[0]);
    
    // Scale to locales
    for (const locale of LOCALES) {
      const scaled = await scaleToLocale(sourceFile, pageNum, locale);
      totalGenerated += scaled;
    }
    
    // Scale to geos (English base)
    for (const geo of GEOS) {
      await geoTargetPage(sourceFile, pageNum, geo);
      totalGenerated++;
    }
    
    console.log(`✅ Scaled page ${pageNum} (${totalGenerated} total)`);
  }
  
  console.log(`🎉 GLOBAL COMPLETE: ${totalGenerated} pages deployed`);
  
  await generateGlobalSitemap();
  await updateRobotsTxt();
}

async function scaleToLocale(sourceFile, pageNum, locale) {
  const sourcePath = path.join(SOURCE_DIR, sourceFile);
  const sourceHTML = await fs.readFile(sourcePath, 'utf8');
  const $ = cheerio.load(sourceHTML);
  
  const targetFile = `vulture-page-${pageNum}-${locale}.html`;
  const targetPath = path.join(TARGET_BASE, targetFile);
  
  // Translate key elements
  if (locale !== 'en') {
    $('h1').text($('h1').text().replace('ManyChat', LOCALE_TRANSLATORS[locale].title));
    $('.cta-button').text(LOCALE_TRANSLATORS[locale].cta);
    $('.roi-calculator h2').text(LOCALE_TRANSLATORS[locale].roi);
  }
  
  // Hreflang cluster
  $('head').append(`<link rel="alternate" hreflang="${locale}" href="${config.baseUrl}/${targetFile}">`);
  
  // Canonical to English
  $('head').append(`<link rel="canonical" href="${config.baseUrl}/vulture-page-${pageNum}.html">`);
  
  await fs.writeFile(targetPath, $.html());
  return 1;
}

async function geoTargetPage(sourceFile, pageNum, geo) {
  const sourcePath = path.join(SOURCE_DIR, sourceFile);
  const sourceHTML = await fs.readFile(sourcePath, 'utf8');
  const $ = cheerio.load(sourceHTML);
  
  const targetFile = `vulture-page-${pageNum}-${geo}.html`;
  const targetPath = path.join(TARGET_BASE, targetFile);
  
  // Geo-specific affiliate
  const geoCta = GEO_AFFILIATES[geo] || MANYCHAT_CTA;
  $('.cta-button').attr('href', geoCta);
  $('.cta-button').text(`Start ManyChat ${geo.toUpperCase()} Trial`);
  
  // Currency conversion
  if (CURRENCY_MAP[geo]) {
    const currency = CURRENCY_MAP[geo];
    $('table td:nth-child(2)').each((i, el) => {
      const text = $(el).text().replace('$', '');
      $(el).text(`${currency.symbol}${parseFloat(text).toLocaleString()}`);
    });
  }
  
  // Geo meta tags
  $('head').append(`
    <meta name="geo.region" content="${geo.toUpperCase()}">
    <meta name="geo.placename" content="${geo.toUpperCase()}">
  `);
  
  await fs.writeFile(targetPath, $.html());
}

async function generateGlobalSitemap() {
  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  
  ${LOCALES.map(locale => 
    `<xhtml:link rel="alternate" hreflang="${locale}" href="${config.baseUrl}/sitemap-${locale}.xml"/>`
  ).join('\n  ')}
  
</urlset>`;
  
  await fs.writeFile(path.join(TARGET_BASE, 'sitemap-global.xml'), sitemap);
}

async function updateRobotsTxt() {
  const robots = `User-agent: *
Allow: /
Sitemap: https://yourrepo.github.io/pages-global/sitemap-global.xml

# Multilingual sitemaps
Sitemap: https://yourrepo.github.io/pages/sitemap-en.xml
Sitemap: https://yourrepo.github.io/pages/sitemap-es.xml
Sitemap: https://yourrepo.github.io/pages/sitemap-fr.xml`;

  await fs.writeFile(path.join(TARGET_BASE, 'robots.txt'), robots);
}

// === EXECUTE ===
scaleGlobal().catch(console.error);
