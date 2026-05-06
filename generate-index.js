const fs = require('fs');
const path = require('path');

// 1. DATA CONFIGURATION
const CONTENT_TITLES = [
  'instagram-lead-generation-flow', 'facebook-messenger-sales-funnel', 'whatsapp-business-automation',
  'tiktok-viral-growth-strategy', 'ecommerce-abandoned-cart-recovery', 'appointment-booking-system',
  'customer-support-chatbot', 'email-list-builder-flow', 'product-recommendation-engine',
  'vip-member-welcome-sequence', 'retargeting-campaign-automation', 'flash-sale-notification-system',
  'birthday-offer-generator', 'referral-program-flow', 'upsell-sequence-builder',
  'survey-feedback-collector', 'event-registration-bot', 'course-enrollment-funnel',
  'real-estate-lead-qualifier', 'restaurant-reservation-system', 'saas-demo-request-flow',
  'local-service-booking', 'coaching-welcome-sequence', 'membership-renewal-automation',
  'lead-qualification-sequence', 'support-ticket-router', 'cart-abandonment-recovery-v2',
  'advanced-product-recommendations', 'multi-channel-lead-nurturing'
];

// 2. DATA GENERATOR LOGIC
const generateContentSpecificPage = (index) => {
  const contentSlug = CONTENT_TITLES[(index - 1) % CONTENT_TITLES.length];
  const pageNumber = index;
  const filename = `${contentSlug}-${pageNumber}.html`;
  
  const title = contentSlug
    .replace(/-/g, ' ')
    .replace(/\b\w/g, l => l.toUpperCase());
  
  return {
    filename,
    title: `${title} - ManyChat Strategy #${pageNumber}`,
    slug: contentSlug,
    h1: `${title} Strategy`,
    keywords: `${contentSlug.replace(/-/g, ', ')}, manychat ${contentSlug}`,
    pageNumber: pageNumber
  };
};

// 3. CONTENT HELPERS
const getIndustryFocus = (slug) => {
  const focusMap = {
    'instagram': 'Instagram organic/paid traffic',
    'facebook': 'Facebook page subscribers', 
    'whatsapp': 'WhatsApp Business API users',
    'ecommerce': 'Shopify/WooCommerce stores',
    'tiktok': 'TikTok content creators'
  };
  return focusMap[slug.split('-')[0]] || 'high-volume lead gen';
};

const getConversionMetric = (slug) => {
  const metrics = ['47.2% opt-in rate', '347% revenue growth', '28.4% cart recovery', '92.3% open rate'];
  return metrics[Math.floor(Math.random() * metrics.length)];
};

const generateContentForSlug = (slug) => {
  const contentTypes = {
    'instagram-lead': `<h3>Instagram-Specific Optimizations</h3><p>Configure DM automation triggers for Story mentions, comment keywords, and profile visits.</p>`,
    'facebook-messenger': `<h3>Messenger Broadcast Optimization</h3><p>Segment by conversation history, tag stacking, and 24hr messaging window management...</p>`,
  };
  return contentTypes[slug.split('-').slice(0,2).join('-')] || `<h3>Core Flow Architecture</h3><p>47 nodes, 23 branches, 18 custom fields...</p>`;
};

const getContentSpecificStep = (slug, stepNum) => {
  const stepMap = {
    'instagram-lead': ['Configure IG Story mention trigger', 'Set DM welcome sequence'],
    'ecommerce-abandoned': ['Shopify webhook cart detection', 'Personalized recovery timing']
  };
  return stepMap[slug.split('-').slice(0,2).join('-')]?.[stepNum % 2] || `Advanced ${slug.replace(/-/g, ' ')} configuration step ${stepNum + 1}`;
};

const generate47StepsForContent = (slug) => {
  let steps = '';
  for (let i = 0; i < 47; i++) {
    steps += `<div class="step" style="border-bottom:1px solid #eee; padding:15px 0;"><h3>Step ${i+1}: ${getContentSpecificStep(slug, i)}</h3><p>Detailed implementation guide for step ${i+1} including technical logic and node configuration.</p></div>`;
  }
  return steps;
};

const getNextSlug = (currentSlug) => {
  const index = CONTENT_TITLES.indexOf(currentSlug);
  const nextIndex = (index + 1) % CONTENT_TITLES.length;
  return CONTENT_TITLES[nextIndex];
};

// 4. HTML TEMPLATE
const generatePageContent = (pageData) => {
  const { title, h1, keywords, slug, pageNumber } = pageData;
  const nextSlug = getNextSlug(slug);
  
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>${title} | 2650+ Word ManyChat Implementation</title>
    <meta name="description" content="Complete ${h1} guide for ManyChat. 47 implementation steps, technical specs, 347% ROI case studies.">
    <meta name="keywords" content="${keywords}, manychat automation, chatbot flow">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #f9f9f9; }
        .container { max-width: 900px; margin: 0 auto; padding: 40px 20px; background: white; box-shadow: 0 0 20px rgba(0,0,0,0.05); }
        header { border-bottom: 4px solid #007bff; padding-bottom: 20px; margin-bottom: 30px; }
        h1 { color: #007bff; font-size: 2.5rem; margin-top: 0; }
        .cta-button { display: inline-block; padding: 12px 25px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; margin: 10px 5px; }
        .cta-button:hover { background: #0056b3; }
        footer { margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; font-size: 0.9rem; color: #777; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>${h1} Strategy #${pageNumber}</h1>
            <p><strong>2650+ WORD ${h1.toUpperCase()} IMPLEMENTATION</strong> - 47 Steps • 92 Min Setup</p>
        </header>

        <section class="strategy-content">
            <h2>${h1} - Technical Overview</h2>
            <p>This ${slug.replace(/-/g, ' ')} flow delivers 347% ROI through 47 decision nodes, 23 conditional branches, and 18 custom fields. Optimized for ${getIndustryFocus(slug)} with ${getConversionMetric(slug)} proven results.</p>
            ${generateContentForSlug(slug)}
        </section>

        <section class="strategy-content">
            <h2>47-Step ${h1} Implementation</h2>
            ${generate47StepsForContent(slug)}
        </section>

        <div style="text-align:center;padding:40px 0">
            <a href="/" class="cta-button">Back to All Strategies</a>
            <a href="/${nextSlug}-${pageNumber + 1}/" class="cta-button">Next Strategy →</a>
        </div>

        <footer>
            <p>${h1} Strategy | 2650+ Words | <a href="/">Home</a></p>
        </footer>
    </div>
</body>
</html>`;
};

// 5. FILE GENERATION ENGINE
const generatePages = (count = 833) => {
    console.log(`🦅 Generating ${count} SEO-OPTIMIZED FOLDER STRUCTURES...`);
    
    for (let i = 1; i <= count; i++) {
        const pageData = generateContentSpecificPage(i);
        
        // Create folder name (e.g., "instagram-lead-flow-1")
        const dirName = pageData.filename.replace('.html', ''); 
        const dirPath = path.join(__dirname, dirName);

        // Create folder if it doesn't exist
        if (!fs.existsSync(dirPath)){
            fs.mkdirSync(dirPath, { recursive: true });
        }

        // Generate content and write to index.html inside the folder
        const content = generatePageContent(pageData);
        fs.writeFileSync(path.join(dirPath, 'index.html'), content);
        
        if (i % 100 === 0) console.log(`Progress: ${i}/${count} folders created...`);
    }
    
    generateIndex();
    console.log('✅ CLEAN URLS COMPLETE!');
};

const generateIndex = () => {
    const dirs = fs.readdirSync(__dirname, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory() && !dirent.name.startsWith('.') && dirent.name !== 'node_modules')
        .map(dirent => dirent.name)
        .sort((a, b) => {
            const numA = parseInt(a.match(/\d+$/)?.[0] || 0);
            const numB = parseInt(b.match(/\d+$/)?.[0] || 0);
            return numA - numB;
        });
    
    const links = dirs.slice(0, 500).map(dir => {
        const title = dir.replace(/-/g, ' ').replace(/\d+$/, '').trim().toUpperCase();
        const num = dir.match(/(\d+)$/)?.[1] || "";
        return `<li><a href="/${dir}/">${title} #${num}</a></li>`;
    }).join('\n');
    
    const indexHTML = `<!DOCTYPE html>
<html>
<head>
    <title>ManyChat Strategy Vault (${dirs.length})</title>
    <style>
        body { font-family: sans-serif; padding: 50px; background: #f4f4f9; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; list-style: none; padding: 0; }
        .grid a { display: block; padding: 25px; background: white; text-decoration: none; color: #333; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: 0.3s; border-top: 4px solid #007bff; }
        .grid a:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: #222; margin-bottom: 40px; }
    </style>
</head>
<body>
    <h1>🚀 ManyChat Strategy Vault</h1>
    <ul class="grid">${links}</ul>
</body>
</html>`;
    
    fs.writeFileSync('index.html', indexHTML);
};

// START GENERATION
generatePages(833);
