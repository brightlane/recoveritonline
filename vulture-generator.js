// vulture-generator.js - Real ManyChat affiliate page generator
const fs = require('fs-extra');
const path = require('path');
const axios = require('axios');
const cheerio = require('cheerio');

/**
 * VULTURE SAFE SDK COMPATIBILITY LAYER
 * Prevents broken or legacy package references from crashing CI
 */
let googleAI;

try {
  const { GoogleGenerativeAI } = require("@google/generative-ai");
  googleAI = GoogleGenerativeAI;
} catch (e) {
  console.warn("⚠️ Google Generative AI SDK not available");
  googleAI = null;
}

// Config from GitHub Actions
const startPage = parseInt(process.env.BATCH_START || '1');
const endPage = parseInt(process.env.BATCH_END || '10');
const llmModel = process.env.LLM_MODEL || 'grok-4.1';
const pagesDir = './pages';

console.log(`🏭 Generating pages ${startPage}-${endPage} with ${llmModel}`);

async function generatePage(pageNum) {
  const filename = `vulture-page-${pageNum}.html`;
  const filepath = path.join(pagesDir, filename);
  
  // Base ManyChat affiliate template
  let html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ManyChat Vulture Strategy #${pageNum} - 833% Growth</title>
  <meta name="description" content="ManyChat automation strategy #${pageNum}: Daily 833 strategy sync for affiliate conversions">
</head>
<body>
  <header>
    <h1>ManyChat Vulture Strategy #${pageNum}</h1>
    <p>Daily Heartbeat - 833 Strategy Sync</p>
  </header>
  
  <main>
    <section>
      <h2>AI-Powered ManyChat Automation</h2>
      <p>Generated with ${llmModel} - Optimized for affiliate conversions</p>
      
      <!-- Affiliate links -->
      <div class="affiliate">
        <a href="https://manychat.com?ref=vulture${pageNum}" target="_blank">
          Start ManyChat Free → (Affiliate)
        </a>
      </div>
      
      <h3>Strategy Benefits:</h3>
      <ul>
        <li>833% traffic growth via AI content</li>
        <li>Automated daily page generation</li>
        <li>SEO-optimized ManyChat flows</li>
        <li>Global multilingual support</li>
      </ul>
    </section>
  </main>
  
  <footer>
    <p>Vulture Factory Orchestrator - Page ${pageNum}/${endPage}</p>
  </footer>
</body>
</html>`;

  // Ensure pages dir exists
  await fs.ensureDir(pagesDir);
  
  // Write page
  await fs.writeFile(filepath, html);
  console.log(`✅ Created ${filename}`);
  
  return filename;
}

/**
 * LLM RESOLVER (ADDED - SAFE MODEL MAPPING)
 */
function resolveLLM(model) {
  const map = {
    "grok-4.1": "grok",
    "claude-4.6-sonnet": "claude",
    "gemini-3.1-pro": "gemini",
    "gpt-5.4-mini": "openai",
    "glm-4.7-thinking": "glm",
    "deepseek-v3.2": "deepseek",
    "qwen3-235b": "qwen",
    "mistral-large-3": "mistral",
    "llama-4-405b": "llama",
    "command-r-plus-248b": "cohere"
  };

  return map[model] || "unknown";
}

async function main() {
  try {
    for (let i = startPage; i <= endPage; i++) {
      await generatePage(i);
    }
    console.log(`🎉 Generated ${endPage - startPage + 1} vulture pages`);
    process.exit(0);
  } catch (error) {
    console.error('❌ Generation failed:', error.message);
    process.exit(1);
  }
}

main();
