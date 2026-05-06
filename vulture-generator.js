// FIXED vulture-generator.js - Corrected regex escapes and CLI parsing
const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://manychat.com';
const AFFILIATE_LINKS = [
  'https://manychat.com/signup?ref=youraffiliateid',
  'https://manychat.pro?ref=youraffiliateid',
  'https://manychat.com/pricing?ref=youraffiliateid'
];

// ... [all functions remain identical - generatePageContent, generateSteps, getRandom* functions unchanged]

const generatePages = (count, outputDir = 'pages') => {
  console.log(`🦅 Generating ${count} Vulture Pages...`);
  
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  for (let i = 1; i <= count; i++) {
    const filename = `vulture-page-${i}.html`;
    const filepath = path.join(outputDir, filename);
    const content = generatePageContent(i);
    fs.writeFileSync(filepath, content);
    console.log(`Generated: ${filename}`);
  }
  console.log(`✅ Complete! Generated ${count} pages in ${path.resolve(outputDir)}`);
};

const generateIndex = (pagesDir = 'pages') => {
  const files = fs.readdirSync(pagesDir)
    .filter(f => /vulture-page-\d+\.html$/.test(f))  // ✅ FIXED: Proper regex without double \\
    .sort((a,b) => {
      const numA = parseInt(a.match(/vulture-page-(\d+)/)?.[1] || 0);
      const numB = parseInt(b.match(/vulture-page-(\d+)/)?.[1] || 0);
      return numA - numB;
    })
    .slice(0, 500);
  
  let links = files.map(file => {
    const pageNum = file.match(/vulture-page-(\d+)/)?.[1] || '0';
    return `<li><a href="pages/${file}">ManyChat Strategy #${pageNum}</a></li>`;
  }).join('\n');
  
  const indexContent = `<!DOCTYPE html>
<html><head>
<title>ManyChat Directory - ${files.length}+ Strategies</title>
<style>/* [CSS unchanged] */</style>
</head><body>
<h1>🚀 ManyChat Strategies</h1>
<ul class="grid">${links}</ul>
</body></html>`;
  
  fs.writeFileSync('index.html', indexContent);
  console.log('✅ index.html generated');
};

// ✅ FIXED CLI parsing
const args = process.argv.slice(2);
let pages = 833;
let output = 'pages';

if (args.length >= 1) {
  const firstArg = args[0];
  if (!isNaN(parseInt(firstArg))) {
    pages = parseInt(firstArg);
    if (args.length > 1) output = args[1];
  } else {
    output = firstArg;
  }
}

generatePages(pages, output);
generateIndex(output);

console.log('\n🦅 Vulture Complete! Ready for GitHub Pages deploy.');
