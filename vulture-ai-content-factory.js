#!/usr/bin/env node
const fs = require('fs-extra');
const path = require('path');
const faker = require('@faker-js/faker');
const { OpenAI } = require('openai');
const cheerio = require('cheerio');

// === CONFIG ===
const config = {
  baseUrl: process.env.SITE_BASEURL || 'https://yourrepo.github.io/pages',
  pagesDir: './pages',
  aiPagesPerRun: parseInt(process.env.PAGES_PER_RUN) || 50,
  startPage: parseInt(process.argv[2]) || 1,
  endPage: parseInt(process.argv[3]) || config.aiPagesPerRun,
  locales: ['en', 'es', 'fr', 'de', 'it'],
  affiliateNetworks: {
    manychat: 'https://manychat.com/?ref=yourid',
    clickbank: 'https://hop.clickbank.net/?affiliate=yourid',
    warriorplus: 'https://warriorplus.com/?ref=yourid',
    jvzoo: 'https://www.jvzoo.com/?ref=yourid'
  },
  openai: {
    apiKey: process.env.OPENAI_API_KEY || 'your-key-here',
    model: 'gpt-4o-mini',
    temperature: 0.7
  }
};

// === AI CLIENT ===
const openai = new OpenAI({ apiKey: config.openai.apiKey });

// === AFFILIATE PIXELS ===
const MANYCHAT_PIXEL = `
<script>
fbq('track', 'ViewContent');
(function(w,d,s,l,i){
  w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});
  var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';
  j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');
</script>`;

const CLICKBANK_PIXEL = `
<img src="https://your-tracker.com/pixel.gif?aff_id=yourid&product=manychat" width="1" height="1" />`;

// === CONTENT TEMPLATES ===
const manychatTopics = [
  'Instagram DM Automation Strategies',
  'WhatsApp Lead Generation Funnels', 
  'Facebook Messenger Bot Sequences',
  'TikTok Comment Automation Workflows',
  'SMS Follow-up Sequences for Ecom',
  'ManyChat Pro vs Free Comparison',
  'Chatbot A/B Testing Frameworks',
  'Omnichannel Messaging Strategies',
  'Dynamic Content Personalization',
  'Abandoned Cart Recovery Flows'
];

const schemaTemplates = {
  FAQPage: {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: []
  },
  Article: {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: "",
    author: {"@type": "Person", "name": "AI Marketing Expert"},
    datePublished: new Date().toISOString()
  }
};

// === CORE GENERATOR ===
async function generateVulturePage(pageNum, locale = 'en') {
  console.log(`🦅 Generating page ${pageNum} (${locale})...`);
  
  const topic = faker.helpers.arrayElement(manychatTopics);
  const title = `ManyChat ${topic} | Strategy #${pageNum}`;
  const slug = `vulture-page-${pageNum}.html`;
  
  // === AI CONTENT GENERATION ===
  const aiPrompt = `Write a comprehensive 1800-word ManyChat automation guide titled "${title}". 
  Target: affiliate marketers scaling Instagram/WhatsApp leads. Include:
  1. Problem (manual DMs killing conversions)
  2. ManyChat solution (specific flows)
  3. Step-by-step implementation
  4. 5 real templates with screenshots
  5. A/B test results
  6. ROI calculator
  7. Affiliate CTA (sign up via my link)
  Make it E-E-A-T optimized. Conversational tone.`;

  try {
    const aiResponse = await openai.chat.completions.create({
      model: config.openai.model,
      messages: [{ role: 'user', content: aiPrompt }],
      temperature: config.openai.temperature,
      max_tokens: 3000
    });
    
    const content = aiResponse.choices[0].message.content;
    
    // === BUILD HTML ===
    const html = buildPageHTML({
      title,
      content,
      pageNum,
      locale,
      topic,
      canonical: `${config.baseUrl}/${slug}`
    });
    
    // === WRITE FILE ===
    const filePath = path.join(config.pagesDir, slug);
    await fs.writeFile(filePath, html);
    
    console.log(`✅ Page ${pageNum} saved: ${filePath}`);
    
    return { success: true, path: filePath, pageNum };
    
  } catch (error) {
    console.error(`❌ Page ${pageNum} failed:`, error.message);
    return { success: false, pageNum, error: error.message };
  }
}

// === HTML BUILDER ===
function buildPageHTML(data) {
  const $ = cheerio.load(`
<!DOCTYPE html>
<html lang="${data.locale}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${data.title} - ManyChat Automation Guide</title>
  <meta name="description" content="Step-by-step ${data.topic} using ManyChat. Scale Instagram DMs to 10k/month. Free templates + ROI calculator.">
  
  <!-- Open Graph -->
  <meta property="og:title" content="${data.title}">
  <meta property="og:description" content="ManyChat automation strategy #${data.pageNum}">
  <meta property="og:type" content="article">
  
  <!-- Schema.org -->
  <script type="application/ld+json">
  ${JSON.stringify(schemaTemplates.Article, null, 2)}
  </script>
  
  <!-- Hreflang -->
  ${config.locales.map(l => 
    `<link rel="alternate" hreflang="${l}" href="${data.canonical.replace('.html', `-${l}.html`)}">`
  ).join('\n  ')}
  
  <!-- Preload critical CSS -->
  <style>
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; line-height:1.6; color:#333; max-width:900px; margin:0 auto; padding:40px 20px; }
    h1,h2,h3 { color:#1a1a1a; margin:2rem 0 1rem; }
    h1 { font-size:2.5rem; border-bottom:3px solid #007cba; padding-bottom:1rem; }
    .cta-button { background:#007cba; color:white; padding:15px 30px; text-decoration:none; border-radius:8px; font-weight:600; display:inline-block; margin:2rem 0; }
    .cta-button:hover { background:#005a87; }
    .affiliate-box { background:#f8f9fa; border:2px solid #007cba; border-radius:12px; padding:2rem; margin:3rem 0; }
    .roi-calculator { background:#e7f3ff; padding:2rem; border-radius:12px; margin:2rem 0; }
    pre { background:#f4f4f4; padding:1.5rem; border-radius:8px; overflow-x:auto; }
    table { width:100%; border-collapse:collapse; margin:2rem 0; }
    th,td { border:1px solid #ddd; padding:12px; text-align:left; }
    th { background:#f8f9fa; }
    .faq { margin:3rem 0; }
    .faq details { margin-bottom:1rem; border:1px solid #eee; border-radius:8px; padding:1rem; }
    .timestamp { color:#666; font-size:0.9rem; }
  </style>
</head>
<body>
  <header>
    <h1>${data.title}</h1>
    <p class="timestamp">Published: ${new Date().toLocaleDateString()} | ManyChat Strategy #${data.pageNum}</p>
  </header>
  
  <main>
    ${data.content}
    
    <!-- ROI Calculator -->
    <div class="roi-calculator">
      <h2>ROI Calculator</h2>
      <p>Lead cost: $2.50 → ManyChat automation: <strong>$0.15/lead</strong></p>
      <table>
        <tr><th>Monthly Leads</th><th>Manual Cost</th><th>ManyChat Cost</th><th>Savings</th></tr>
        <tr><td>1,000</td><td>$2,500</td><td>$150</td><td><strong>$2,350</strong></td></tr>
        <tr><td>5,000</td><td>$12,500</td><td>$750</td><td><strong>$11,750</strong></td></tr>
        <tr><td>10,000</td><td>$25,000</td><td>$1,500</td><td><strong>$23,500</strong></td></tr>
      </table>
    </div>
    
    <!-- Affiliate CTA -->
    <div class="affiliate-box">
      <h2>⚡ Get ManyChat Pro (30% OFF)</h2>
      <p>Used by 1M+ businesses. Start your free trial:</p>
      <a href="${config.affiliateNetworks.manychat}" class="cta-button" onclick="trackAffiliate('manychat-pro')">
        🚀 Start ManyChat Trial
      </a>
      <p><small>Affiliate disclosure: We earn commission at no extra cost to you.</small></p>
    </div>
    
    <!-- FAQ Schema -->
    <section class="faq">
      <h2>Frequently Asked Questions</h2>
      <details>
        <summary>How long to setup ManyChat automation?</summary>
        <p>15 minutes with our templates. No coding required.</p>
      </details>
      <details>
        <summary>Works with Instagram DMs?</summary>
        <p>Yes! Full Instagram, WhatsApp, FB Messenger support.</p>
      </details>
    </section>
  </main>
  
  <!-- Affiliate Pixels -->
  ${MANYCHAT_PIXEL}
  ${CLICKBANK_PIXEL}
  
  <!-- Internal Links Cluster -->
  <footer>
    <h3>Related ManyChat Strategies</h3>
    <ul>
      ${generateInternalLinks(data.pageNum)}
    </ul>
  </footer>
  
  <script>
    function trackAffiliate(network) {
      gtag('event', 'affiliate_click', {
        'network': network,
        'page_num': ${data.pageNum}
      });
      fbq('track', 'InitiateCheckout');
    }
  </script>
</body>
</html>`);
  
  // Inject AI content
  $('main').prepend(`<div class="hero">${data.content.substring(0, 300)}...</div>`);
  
  return $.html();
}

// === INTERNAL LINKING MATRIX ===
function generateInternalLinks(pageNum) {
  const links = [];
  const nearbyPages = [
    Math.max(1, pageNum - 5), pageNum - 2, pageNum + 2, pageNum + 5,
    pageNum - 10, pageNum + 10
  ];
  
  nearbyPages.forEach(offset => {
    if (offset > 0 && offset <= 833) {
      links.push(
        `<li><a href="vulture-page-${offset}.html">Strategy #${offset}</a></li>`
      );
    }
  });
  
  return links.join('') + 
    '<li><a href="../index.html">← All Strategies</a></li>';
}

// === MAIN EXECUTION ===
async function main() {
  console.log(`🦅 Vulture Factory v2.0 | Generating pages ${config.startPage}-${config.endPage}`);
  
  // Ensure pages directory
  await fs.ensureDir(config.pagesDir);
  
  const results = [];
  
  for (let i = config.startPage; i <= config.endPage; i++) {
    const result = await generateVulturePage(i);
    results.push(result);
    
    // Rate limiting
    await new Promise(resolve => setTimeout(resolve, 1000));
  }
  
  // Summary
  const success = results.filter(r => r.success).length;
  console.log(`✅ COMPLETE: ${success}/${config.endPage - config.startPage + 1} pages generated`);
  
  // Generate sitemap reference
  await fs.writeJson('./sitemap-recent.json', results, { spaces: 2 });
  
  process.exit(0);
}

// === ERROR HANDLING ===
process.on('unhandledRejection', (reason) => {
  console.error('❌ Factory error:', reason);
  process.exit(1);
});

main();
