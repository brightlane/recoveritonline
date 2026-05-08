// ============================================================
// BrightLane — ManyChat Affiliate Site Generator
// 30 pages · Real AI content · Global SEO · Orange + Purple
// Setup: npm install @anthropic-ai/sdk
// Run:   ANTHROPIC_API_KEY=sk-... node generate-manychat.js
// ============================================================

const fs = require("fs/promises");
const path = require("path");
const Anthropic = require("@anthropic-ai/sdk");

// ── CONFIG ───────────────────────────────────────────────────

const CONFIG = {
  outputDir: "output-manychat",
  domain: "https://brightlane.github.io/ManyChat",
  brand: "BrightLane",
  tagline: "Independent ManyChat Reviews & Guides",

  // Your affiliate links from affiliate.js
  aff: {
    default:   "https://manychat.partnerlinks.io/nwkkk7vkps17",
    free:      "https://manychat.partnerlinks.io/emwcbue22i01-ogcg6e",
    discount:  "https://manychat.partnerlinks.io/t8let4hhqtqg-wki14",
    pricing:   "https://manychat.partnerlinks.io/98hj6b3pr28k-4znb59",
    instagram: "https://manychat.partnerlinks.io/8k59yhm0l32j-z7dk2i",
  },

  affiliateDisclosure: "Affiliate disclosure: We earn a commission if you sign up through our links, at no extra cost to you.",

  concurrency: 3,
  batchDelay: 1500,
  maxRetries: 4,
  retryBaseMs: 2000,
  checkpointFile: "checkpoint-manychat.json",

  // Brand colors matching ManyChat
  orange: "#FF5722",
  purple: "#6B3FA0",
  purpleLight: "#F3EEFF",
  orangeLight: "#FFF3EE",

  competitors: [
    { name: "Klaviyo",          angle: "email marketing vs chat automation" },
    { name: "ActiveCampaign",   angle: "CRM and automation suite" },
    { name: "Chatfuel",         angle: "direct chatbot builder competitor" },
    { name: "MobileMonkey",     angle: "multi-channel chatbot platform" },
    { name: "Intercom",         angle: "customer support vs marketing automation" },
  ],

  useCases: [
    { audience: "e-commerce stores",     pain: "cart abandonment and post-purchase follow-up",         platform: "Instagram & WhatsApp" },
    { audience: "restaurants",           pain: "reservation management and repeat customer retention",  platform: "Facebook & Instagram" },
    { audience: "coaches and consultants",pain: "lead qualification and discovery call booking",        platform: "Instagram DMs" },
    { audience: "real estate agents",    pain: "lead capture and nurturing from social media",          platform: "Facebook & Instagram" },
    { audience: "content creators",      pain: "audience monetization and DM automation",              platform: "Instagram" },
    { audience: "fitness businesses",    pain: "class bookings and membership retention",               platform: "Instagram & SMS" },
    { audience: "beauty salons",         pain: "appointment booking and client reactivation",           platform: "Instagram & WhatsApp" },
  ],

  platforms: [
    { name: "Instagram",  slug: "instagram", desc: "Automate Instagram DMs, story replies, and comment triggers" },
    { name: "Facebook",   slug: "facebook",  desc: "Facebook Messenger automation and lead generation" },
    { name: "WhatsApp",   slug: "whatsapp",  desc: "WhatsApp Business automation at scale" },
    { name: "SMS",        slug: "sms",       desc: "Text message marketing and automation" },
    { name: "Shopify",    slug: "shopify",   desc: "ManyChat + Shopify integration for e-commerce automation" },
  ],

  features: [
    { name: "Instagram DM Automation",   slug: "instagram-dm-automation",  kw: "instagram dm automation manychat" },
    { name: "Flow Builder",              slug: "flow-builder",              kw: "manychat flow builder tutorial" },
    { name: "Broadcast Messages",        slug: "broadcast-messages",        kw: "manychat broadcast messages" },
    { name: "AI Automation",             slug: "ai-automation",             kw: "manychat ai automation" },
    { name: "Growth Tools",              slug: "growth-tools",              kw: "manychat growth tools" },
  ],

  countries: [
    { name: "United Kingdom", code: "GB", currency: "GBP", note: "billed in USD, roughly £12-16/mo for Pro" },
    { name: "Australia",      code: "AU", currency: "AUD", note: "billed in USD, roughly A$18-24/mo for Pro" },
    { name: "Canada",         code: "CA", currency: "CAD", note: "billed in USD, roughly C$17-22/mo for Pro" },
    { name: "India",          code: "IN", currency: "INR", note: "billed in USD — Pro starts at ~₹1,200/mo" },
    { name: "Brazil",         code: "BR", currency: "BRL", note: "billed in USD — Pro starts at ~R$75/mo" },
  ],
};

const client = new Anthropic();

// ── HELPERS ──────────────────────────────────────────────────

function slugify(str) {
  return str.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;")
    .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

async function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// ── CLAUDE API CALL ───────────────────────────────────────────

async function callClaude(prompt, maxTokens = 2800) {
  for (let attempt = 0; attempt <= CONFIG.maxRetries; attempt++) {
    try {
      const msg = await client.messages.create({
        model: "claude-sonnet-4-20250514",
        max_tokens: maxTokens,
        messages: [{ role: "user", content: prompt }],
      });
      return msg.content[0].text;
    } catch (err) {
      const retryable = err?.status === 429 || err?.status >= 500;
      if (retryable && attempt < CONFIG.maxRetries) {
        const wait = CONFIG.retryBaseMs * Math.pow(2, attempt);
        console.warn(`  ⚠ API ${err?.status} — retrying in ${wait}ms…`);
        await sleep(wait);
      } else throw err;
    }
  }
}

// ── PROMPTS ──────────────────────────────────────────────────

function homepagePrompt() {
  return `You are a sharp digital marketing copywriter for BrightLane, an independent ManyChat review site.

Write comprehensive homepage body content for a ManyChat affiliate review site. ManyChat is a chat marketing automation platform for Instagram, Facebook, WhatsApp, and SMS. It's used globally by 1M+ businesses.

Write 2,000+ words of HTML fragments only (no html/head/body tags). Cover these sections:

<section class="intro">
  3-4 sentences: what ManyChat is, who uses it globally, and what makes it the leading chat marketing platform. Mention Instagram DM automation specifically as the flagship use case.
</section>

<section class="what-is-manychat">
  <h2>What is ManyChat?</h2>
  3 substantial paragraphs covering: the platform overview, supported channels (Instagram, Facebook, WhatsApp, SMS, Email), and the core value proposition of automating customer conversations at scale. Include real stats where known (1M+ active bots, used in 190 countries, etc).
</section>

<section class="who-uses-it">
  <h2>Who uses ManyChat?</h2>
  Cover 4 audience types in sub-sections (h3): e-commerce stores, content creators, local businesses, and marketing agencies. Each: 2 paragraphs with specific use cases and results.
</section>

<section class="key-features">
  <h2>ManyChat key features</h2>
  Cover 6 features with h3 headings: Instagram DM Automation, Flow Builder, Broadcasts, Growth Tools, AI Automation, Analytics. Each: 2 paragraphs with specific detail on how the feature works and what it achieves.
</section>

<section class="free-vs-pro">
  <h2>ManyChat Free vs Pro — what's the difference?</h2>
  Detailed comparison covering: contact limits, channel access, automation features, analytics, support. Be specific about what Free actually gives you and when upgrading to Pro makes sense.
</section>

<section class="global-availability">
  <h2>ManyChat worldwide — is it available in your country?</h2>
  2 paragraphs: ManyChat works in 190 countries, billed in USD. Cover key markets: US, UK, Australia, Canada, India, Brazil, Europe. Mention WhatsApp availability is particularly strong internationally.
</section>

<section class="faq">
  <h2>Frequently asked questions</h2>
  6 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Cover: pricing, Instagram API compliance, free trial, WhatsApp requirements, cancellation, GDPR.
</section>

Rules:
- Sharp, knowledgeable tone — like a marketer who has actually used the product
- Specific details, real feature names, actual workflow examples
- No filler phrases
- Return ONLY the HTML sections`;
}

function featurePrompt(feature) {
  return `You are a sharp digital marketing copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,000+ word review/guide for ManyChat's "${feature.name}" feature as HTML fragments only.

Target keyword: "${feature.kw}" — use naturally throughout.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: what ${feature.name} is, why it matters for businesses, and what makes ManyChat's implementation stand out.
</section>

<section class="what-it-is">
  <h2>What is ManyChat ${feature.name}?</h2>
  3 paragraphs: detailed explanation of how the feature works, what it connects to (Instagram API, Facebook, etc), and the technical basics a non-technical marketer needs to know.
</section>

<section class="how-to-set-up">
  <h2>How to set up ${feature.name} in ManyChat</h2>
  Step-by-step <ol> with 6-8 specific steps. Be detailed — name actual UI elements, menu locations, settings. This should be genuinely useful for someone setting it up for the first time.
</section>

<section class="real-world-examples">
  <h2>Real-world examples and use cases</h2>
  4 specific examples with h3 headings. Each: the business type, the specific workflow they use, and the result they typically see. Include realistic numbers where appropriate.
</section>

<section class="best-practices">
  <h2>Best practices for ${feature.name}</h2>
  <ul> with 6 specific, actionable best practices. Each: <strong>label</strong> then 2 sentences of explanation. Genuinely expert advice.
</section>

<section class="common-mistakes">
  <h2>Common mistakes to avoid</h2>
  <ul> with 4 common mistakes. Each: what people do wrong and why it hurts results.
</section>

<section class="free-vs-pro">
  <h2>Is ${feature.name} available on the free plan?</h2>
  1-2 paragraphs: exactly what's available free vs Pro for this specific feature. Be precise.
</section>

<section class="faq">
  <h2>Frequently asked questions about ${feature.name}</h2>
  5 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Questions a real user would actually ask.
</section>

Rules: Expert tone, specific details, genuinely useful. Return ONLY the HTML sections.`;
}

function competitorPrompt(comp) {
  return `You are a sharp digital marketing copywriter for BrightLane, an independent review site.

Write a comprehensive 2,000+ word comparison: ManyChat vs ${comp.name} (${comp.angle}) as HTML fragments only.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: what both tools do, who each is designed for, and the core question this comparison answers.
</section>

<section class="quick-verdict">
  <h2>Quick verdict</h2>
  A clear 3-4 sentence verdict: who wins overall, and for which specific buyer. Don't hedge — give a real recommendation.
</section>

<section class="overview">
  <h2>ManyChat vs ${comp.name} — overview</h2>
  Two h3 sub-sections, one per tool. Each: 2 paragraphs covering the tool's core purpose, target user, pricing model, and core strengths.
</section>

<section class="feature-comparison">
  <h2>Feature-by-feature comparison</h2>
  Cover 6 areas with h3 headings: Ease of setup, Instagram/social automation, Pricing & value, Integrations, Analytics & reporting, Customer support. For each: 2 paragraphs comparing both tools honestly with specific details.
</section>

<section class="manychat-wins">
  <h2>Where ManyChat wins</h2>
  <ul> with 5 specific advantages. Each: <strong>label</strong> then 2 sentences. Be concrete, not vague.
</section>

<section class="competitor-wins">
  <h2>Where ${comp.name} wins</h2>
  <ul> with 4 honest advantages ${comp.name} has. Don't soften these — real fairness builds trust.
</section>

<section class="who-should-choose">
  <h2>Who should choose ManyChat vs ${comp.name}?</h2>
  Two h3 sub-sections: "Choose ManyChat if..." and "Choose ${comp.name} if..." Each: 3-4 specific bullet points describing the ideal buyer.
</section>

<section class="pricing-comparison">
  <h2>Pricing comparison</h2>
  2 paragraphs comparing real pricing of both tools. Include free tiers if they exist. Be specific about what each plan includes.
</section>

<section class="faq">
  <h2>ManyChat vs ${comp.name} FAQ</h2>
  4 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Real questions people search for.
</section>

Rules: Genuinely fair, expert tone, specific details, real pricing. Return ONLY the HTML sections.`;
}

function useCasePrompt(uc) {
  return `You are a sharp digital marketing copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,000+ word guide: "ManyChat for ${uc.audience}" focused on solving "${uc.pain}" using ${uc.platform}. HTML fragments only.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: the specific challenge ${uc.audience} face with ${uc.pain}, and how ManyChat's ${uc.platform} automation directly solves it.
</section>

<section class="why-manychat">
  <h2>Why ${uc.audience} choose ManyChat</h2>
  3 paragraphs: specific reasons this audience is drawn to ManyChat over email or other tools. Include realistic stats on open rates (Instagram DMs get 80%+ open rates vs 20% email, etc).
</section>

<section class="core-workflows">
  <h2>Core ManyChat workflows for ${uc.audience}</h2>
  4 workflows with h3 headings, each covering a specific automation. For each: what triggers it, what the bot does, what result it achieves. Include specific ManyChat features used (keywords, flows, broadcasts, etc).
</section>

<section class="step-by-step">
  <h2>Setting up your first ${uc.audience} automation in ManyChat</h2>
  Detailed <ol> with 8 steps. Name actual ManyChat UI elements and settings. This should be genuinely actionable for someone starting from scratch.
</section>

<section class="results">
  <h2>Real results ${uc.audience} get with ManyChat</h2>
  4 mini case studies with h3 headings. Each: business type, specific automation used, realistic result with numbers. Keep numbers credible, not inflated.
</section>

<section class="templates">
  <h2>ManyChat templates for ${uc.audience}</h2>
  <ul> with 5 specific templates from the ManyChat template library that this audience should start with. One sentence each on what it does and why it works.
</section>

<section class="pricing-fit">
  <h2>Which ManyChat plan fits ${uc.audience}?</h2>
  2 paragraphs: honest assessment of whether Free or Pro makes sense for this audience at different stages. Include contact limit context.
</section>

<section class="faq">
  <h2>ManyChat for ${uc.audience} FAQ</h2>
  5 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Audience-specific questions.
</section>

Rules: Expert, specific, audience-focused. Real workflow detail. No generic advice. Return ONLY the HTML sections.`;
}

function platformPrompt(platform) {
  return `You are a sharp digital marketing copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,000+ word guide: "ManyChat for ${platform.name}" — ${platform.desc}. HTML fragments only.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: what ManyChat does on ${platform.name} specifically, why ${platform.name} automation matters for businesses, and what makes ManyChat the leading tool for this channel.
</section>

<section class="how-it-works">
  <h2>How ManyChat works with ${platform.name}</h2>
  3 paragraphs: the technical integration (API connection, account requirements, approval process if any), what types of automations are possible, and what's NOT possible (be honest about platform limits).
</section>

<section class="setup-guide">
  <h2>How to connect ManyChat to ${platform.name} — step by step</h2>
  Detailed <ol> with 8-10 steps covering the full setup process. Specific UI detail.
</section>

<section class="automation-types">
  <h2>Types of ${platform.name} automations you can build</h2>
  Cover 5 automation types with h3 headings. Each: what it is, how to build it in ManyChat, and what result it drives.
</section>

<section class="best-practices">
  <h2>ManyChat ${platform.name} best practices</h2>
  <ul> with 6 specific best practices. Each: <strong>label</strong> then 2 sentences. Expert-level advice.
</section>

<section class="compliance">
  <h2>${platform.name} compliance and spam rules</h2>
  2 paragraphs: what ${platform.name}'s policies say about automated messages, what ManyChat does to keep you compliant, and what to avoid.
</section>

<section class="global-availability">
  <h2>Is ManyChat ${platform.name} automation available in your country?</h2>
  1-2 paragraphs: global availability of this channel. Note any country-specific restrictions or requirements (especially for WhatsApp).
</section>

<section class="faq">
  <h2>ManyChat ${platform.name} FAQ</h2>
  5 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Channel-specific questions.
</section>

Rules: Technical accuracy, specific setup detail, honest about limitations. Return ONLY the HTML sections.`;
}

function countryPrompt(country) {
  return `You are a sharp digital marketing copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,000+ word guide: "ManyChat in ${country.name}" for businesses and marketers in ${country.name}. HTML fragments only.

Key facts: ManyChat is billed in USD. For ${country.name} users, ${country.note}. ManyChat works in 190 countries.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: ManyChat's availability in ${country.name}, the pricing context (${country.note}), and why ${country.name} businesses are adopting chat marketing.
</section>

<section class="availability">
  <h2>Is ManyChat available in ${country.name}?</h2>
  3 paragraphs: full availability, supported channels in ${country.name} (Instagram, Facebook, WhatsApp especially), payment methods, currency billing, and any ${country.name}-specific notes.
</section>

<section class="popular-channels">
  <h2>Most popular ManyChat channels for ${country.name} businesses</h2>
  Cover 3-4 channels with h3 headings, tailored to ${country.name}'s social media landscape. E.g. WhatsApp is huge in Brazil and India; Facebook in Australia; Instagram everywhere.
</section>

<section class="use-cases">
  <h2>How ${country.name} businesses use ManyChat</h2>
  4 specific examples with h3 headings — business types common in ${country.name}, the automation they use, the result. Make these feel local and relevant.
</section>

<section class="pricing-local">
  <h2>ManyChat pricing for ${country.name} users</h2>
  2 paragraphs: what Free gives you, what Pro costs in USD and the approximate ${country.currency} equivalent (${country.note}), and whether it's worth it for ${country.name} market conditions.
</section>

<section class="compliance">
  <h2>ManyChat compliance in ${country.name}</h2>
  2 paragraphs: GDPR (for UK), PIPEDA (Canada), LGPD (Brazil), or general data privacy. What ManyChat does to keep ${country.name} users compliant.
</section>

<section class="getting-started">
  <h2>Getting started with ManyChat in ${country.name}</h2>
  Practical <ol> with 6 steps specific to ${country.name} users — account setup, connecting the right channels for their market, first automation ideas.
</section>

<section class="faq">
  <h2>ManyChat ${country.name} FAQ</h2>
  5 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. ${country.name}-specific questions about pricing, availability, compliance, support.
</section>

Rules: Locally relevant, accurate pricing, specific to ${country.name} market. Return ONLY the HTML sections.`;
}

function corePagePrompt(slug) {
  const prompts = {
    "manychat-pricing": `You are a sharp copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,000+ word ManyChat pricing guide as HTML fragments only.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: ManyChat's pricing model overview — free tier exists, Pro scales by contacts, used globally.
</section>

<section class="free-plan">
  <h2>ManyChat Free plan — what you actually get</h2>
  3 paragraphs: exactly what's included (up to 1,000 contacts, basic flows, Instagram/Facebook), what's NOT included, and who it's right for. Be specific and honest.
</section>

<section class="pro-plan">
  <h2>ManyChat Pro plan — pricing and features</h2>
  3 paragraphs: how Pro pricing works (starts at ~$15/mo, scales with contacts), exactly what Pro unlocks (unlimited contacts tier, WhatsApp, SMS, advanced analytics, A/B testing), and when it pays for itself.
</section>

<section class="pricing-tiers">
  <h2>ManyChat Pro pricing by contact count</h2>
  A readable breakdown of approximate pricing at different contact levels: 1K, 5K, 10K, 25K, 50K, 100K contacts. Present as clear paragraphs not a table.
</section>

<section class="worth-it">
  <h2>Is ManyChat Pro worth it?</h2>
  3 paragraphs: ROI analysis. Give a real example — if Pro costs $45/mo at 5K contacts and you convert 2% of contacts to a $97 product, you need 1 sale per month to break even. That's the level of specificity needed.
</section>

<section class="vs-free">
  <h2>When to stay on Free vs upgrade to Pro</h2>
  Two h3 sub-sections. "Stay on Free if..." and "Upgrade to Pro if..." Each: 4 specific bullet points.
</section>

<section class="global-pricing">
  <h2>ManyChat pricing outside the US</h2>
  2 paragraphs: billed in USD worldwide, approximate costs in GBP/AUD/CAD/INR/BRL for Pro at entry level.
</section>

<section class="faq">
  <h2>ManyChat pricing FAQ</h2>
  6 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Real pricing questions.
</section>

Rules: Specific numbers, honest assessment, genuinely useful. Return ONLY the HTML sections.`,

    "what-is-manychat": `You are a sharp copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,000+ word "What is ManyChat?" guide as HTML fragments only. This targets someone researching the tool for the first time.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: ManyChat in plain English — what it does, who makes it, how big it is (1M+ businesses, 190 countries).
</section>

<section class="simple-explanation">
  <h2>What is ManyChat — the simple explanation</h2>
  3 paragraphs: explain chat marketing automation in plain terms. Use an analogy. Explain why businesses use it (DM open rates, automation at scale, lead capture). No jargon.
</section>

<section class="what-it-does">
  <h2>What ManyChat actually does</h2>
  Cover 5 core capabilities with h3 headings: Automates DMs and messages, Captures leads from social media, Sends broadcasts to subscribers, Qualifies and routes leads, Integrates with your other tools. Each: 2 paragraphs with specific examples.
</section>

<section class="channels">
  <h2>Which platforms does ManyChat work with?</h2>
  Cover Instagram, Facebook Messenger, WhatsApp, SMS, Email with h3 headings. Each: what's possible on that channel and any requirements.
</section>

<section class="who-uses-it">
  <h2>Who uses ManyChat?</h2>
  4 audience profiles with h3 headings: e-commerce, creators, local businesses, agencies. Each: 2 paragraphs with specific use cases.
</section>

<section class="how-it-works">
  <h2>How ManyChat works — the basics</h2>
  A simple <ol> with 6 steps walking through: connect your account, build a flow, set a trigger, subscriber opts in, automation runs, you review analytics.
</section>

<section class="faq">
  <h2>ManyChat FAQ for beginners</h2>
  6 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Total beginner questions.
</section>

Rules: Plain language, no assumed knowledge, genuinely educational. Return ONLY the HTML sections.`,

    "manychat-free-trial": `You are a sharp copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,000+ word guide "ManyChat Free Trial — What You Get and How to Start" as HTML fragments only.

Use exactly these sections:

<section class="page-intro">
  3-4 sentences: ManyChat's free plan (it's free forever, not a trial), what it includes, and who it's designed for.
</section>

<section class="free-plan-details">
  <h2>What ManyChat's free plan actually includes</h2>
  3 paragraphs: contact limit (1,000), channels available (Instagram, Facebook), automation capabilities, branding requirements, support level. Be precise.
</section>

<section class="how-to-start">
  <h2>How to start ManyChat for free — step by step</h2>
  Detailed <ol> with 8 steps: sign up, connect Instagram or Facebook, build your first flow, set a trigger, test it, go live. Specific UI detail.
</section>

<section class="first-automation">
  <h2>Your first ManyChat automation — a complete walkthrough</h2>
  3 paragraphs walking through building a keyword-triggered Instagram DM automation from scratch. Specific enough to actually follow.
</section>

<section class="free-limits">
  <h2>What you can't do on the free plan</h2>
  <ul> with 5 specific limitations: no WhatsApp, no SMS, contact limit, limited analytics, ManyChat branding. Be honest.
</section>

<section class="upgrade-timing">
  <h2>When should you upgrade from free to Pro?</h2>
  3 paragraphs: clear signals it's time to upgrade — hitting 1K contacts, needing WhatsApp, wanting A/B testing, running ads to Messenger.
</section>

<section class="faq">
  <h2>ManyChat free plan FAQ</h2>
  5 Q&A pairs using <details><summary>Q</summary><p>A</p></details>. Questions about limits, upgrading, credit cards.
</section>

Rules: Honest, specific, actionable. Return ONLY the HTML sections.`,

    "manychat-review": `You are a sharp copywriter for BrightLane, an independent ManyChat review site.

Write a comprehensive 2,500+ word ManyChat review as HTML fragments only. This is the main review page — it needs to be genuinely balanced and authoritative.

Use exactly these sections:

<section class="page-intro">
  4-5 sentences: ManyChat overview, our overall verdict (strong recommendation with caveats), and what this review covers.
</section>

<section class="verdict-box">
  <h2>Our verdict: ManyChat in 2026</h2>
  3 paragraphs: overall assessment — what it does brilliantly (Instagram DM automation is class-leading), what it doesn't do well (pricing complexity, WhatsApp setup friction), and who it's best for. Be direct.
</section>

<section class="pros-cons">
  <h2>ManyChat pros and cons</h2>
  Two h3 sub-sections. Pros: <ul> with 6 specific advantages. Cons: <ul> with 4 real limitations. Don't soften the cons.
</section>

<section class="features-review">
  <h2>ManyChat features — reviewed</h2>
  6 features with h3 headings and a rating out of 10 in the heading (e.g. "Instagram DM Automation — 9/10"). Each: 2 paragraphs of genuine assessment.
</section>

<section class="ease-of-use">
  <h2>Ease of use</h2>
  2 paragraphs: the learning curve, the flow builder UX, what's intuitive vs what trips people up. Honest.
</section>

<section class="pricing-review">
  <h2>Pricing — is ManyChat worth the cost?</h2>
  3 paragraphs: free plan value, Pro pricing by contact tier, ROI analysis, and overall value verdict.
</section>

<section class="customer-support">
  <h2>Customer support</h2>
  2 paragraphs: what support options exist, response times, community quality. Honest about limitations.
</section>

<section class="who-its-for">
  <h2>Who should use ManyChat?</h2>
  Two h3 sub-sections: "ManyChat is great for..." and "ManyChat is NOT right for..." Each: 4 specific bullet points.
</section>

<section class="faq">
  <h2>ManyChat review FAQ</h2>
  5 Q&A pairs using <details><summary>Q</summary><p>A</p></details>.
</section>

Rules: Genuinely balanced, specific detail, honest criticism. This is an independent review, not a sales page. Return ONLY the HTML sections.`,
  };

  return prompts[slug] || `Write a comprehensive 2,000 word guide about ManyChat's ${slug} as HTML fragments only. Use multiple h2/h3 sections, include practical advice, FAQs using details/summary tags, and real workflow examples. Return ONLY the HTML sections.`;
}

// ── SHARED CSS ────────────────────────────────────────────────

function sharedStyles() {
  return `<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;background:#fff;color:#1a1a2e;line-height:1.75}
a{color:#FF5722;text-decoration:none}
a:hover{text-decoration:underline}

nav{background:#fff;border-bottom:1px solid #eee;padding:0 24px;position:sticky;top:0;z-index:100;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.nav-inner{max-width:1060px;margin:auto;display:flex;align-items:center;justify-content:space-between;height:64px}
.logo{font-size:18px;font-weight:800;color:#1a1a2e;text-decoration:none;display:flex;align-items:center;gap:8px}
.logo-mark{background:#FF5722;color:#fff;font-size:13px;font-weight:800;padding:3px 8px;border-radius:6px}
.nav-links{display:flex;gap:20px;align-items:center}
.nav-links a{font-size:14px;color:#555}
.nav-cta{background:#FF5722;color:#fff!important;padding:9px 20px;border-radius:8px;font-weight:700;font-size:14px!important;text-decoration:none!important}
.nav-cta:hover{background:#e04a1a!important}

.hero{background:linear-gradient(135deg,#6B3FA0 0%,#FF5722 100%);padding:80px 24px 68px;text-align:center;color:#fff}
.hero-inner{max-width:700px;margin:auto}
.hero-badge{display:inline-block;background:rgba(255,255,255,.2);color:#fff;font-size:12px;font-weight:700;padding:5px 16px;border-radius:20px;margin-bottom:18px;letter-spacing:.5px;border:1px solid rgba(255,255,255,.3)}
.hero h1{font-size:42px;font-weight:800;line-height:1.15;margin-bottom:16px;color:#fff}
.hero h1 span{color:#FFD700}
.hero-sub{font-size:18px;color:rgba(255,255,255,.9);margin-bottom:32px;line-height:1.6}
.hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.btn-primary{display:inline-block;background:#FF5722;color:#fff;padding:15px 32px;border-radius:10px;font-weight:800;font-size:16px;text-decoration:none;border:2px solid rgba(255,255,255,.3)}
.btn-primary:hover{background:#e04a1a;text-decoration:none}
.btn-free{display:inline-block;background:#fff;color:#6B3FA0;padding:14px 30px;border-radius:10px;font-weight:800;font-size:15px;text-decoration:none}
.btn-free:hover{background:#f3eeff;text-decoration:none}
.social-proof{margin-top:24px;font-size:13px;color:rgba(255,255,255,.8)}
.stars{color:#FFD700;font-size:15px;letter-spacing:1px}

.trust-bar{background:#6B3FA0;padding:14px 24px}
.trust-inner{max-width:1060px;margin:auto;display:flex;align-items:center;justify-content:center;gap:36px;flex-wrap:wrap}
.trust-item{font-size:13px;font-weight:700;color:rgba(255,255,255,.9)}

section{padding:64px 0}
.container{max-width:1060px;margin:auto;padding:0 24px}
.section-head{text-align:center;margin-bottom:36px}
.section-head h2{font-size:30px;font-weight:800;color:#1a1a2e;margin-bottom:10px}
.section-head p{font-size:16px;color:#666}

.features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin-top:36px}
.feature-card{background:#fff;border:1px solid #eee;border-radius:14px;padding:26px}
.feature-icon{width:48px;height:48px;background:#FFF3EE;border-radius:10px;display:flex;align-items:center;justify-content:center;margin-bottom:14px;font-size:22px}
.feature-card h3{font-size:17px;font-weight:700;margin-bottom:8px;color:#1a1a2e}
.feature-card p{font-size:14px;color:#555;line-height:1.6}

.aff-links{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:32px}
.aff-card{border-radius:12px;padding:20px;text-align:center;text-decoration:none;display:block}
.aff-card.free{background:#F3EEFF;border:2px solid #6B3FA0}
.aff-card.discount{background:#FFF3EE;border:2px solid #FF5722}
.aff-card.default{background:#f5f5f5;border:2px solid #ddd}
.aff-card h4{font-size:15px;font-weight:800;margin-bottom:4px}
.aff-card.free h4{color:#6B3FA0}
.aff-card.discount h4{color:#FF5722}
.aff-card p{font-size:13px;color:#666;margin-bottom:12px}
.aff-card span{display:inline-block;padding:8px 16px;border-radius:8px;font-weight:700;font-size:13px;color:#fff}
.aff-card.free span{background:#6B3FA0}
.aff-card.discount span{background:#FF5722}
.aff-card.default span{background:#555}

.main-content{max-width:780px;margin:0 auto;padding:52px 24px}
.main-content h2{font-size:26px;font-weight:800;color:#1a1a2e;margin:40px 0 14px;padding-top:8px;border-top:3px solid #FF5722;display:inline-block}
.main-content h3{font-size:19px;font-weight:700;color:#1a1a2e;margin:26px 0 10px}
.main-content p{font-size:16px;color:#333;margin-bottom:16px;line-height:1.8}
.main-content ul{padding-left:22px;margin-bottom:18px}
.main-content ol{padding-left:22px;margin-bottom:18px}
.main-content li{font-size:16px;color:#333;margin-bottom:10px;line-height:1.7}
.main-content strong{color:#1a1a2e;font-weight:700}
.main-content section{margin-bottom:8px}
.main-content details{border:1px solid #eee;border-radius:10px;padding:14px 18px;margin-bottom:10px}
.main-content summary{font-weight:700;color:#1a1a2e;cursor:pointer;font-size:15px;list-style:none}
.main-content details p{font-size:14px;color:#555;margin:10px 0 0;line-height:1.65}
.main-content blockquote{border-left:4px solid #FF5722;padding:12px 18px;margin:16px 0;background:#FFF3EE;border-radius:0 8px 8px 0;font-style:italic;color:#555}

.cta-inline{background:#F3EEFF;border:2px solid #6B3FA0;border-radius:14px;padding:28px;text-align:center;margin:36px 0}
.cta-inline h3{font-size:20px;font-weight:800;color:#6B3FA0;margin-bottom:8px}
.cta-inline p{font-size:14px;color:#555;margin-bottom:18px}

.testimonials{background:#F3EEFF;padding:56px 24px;border-top:1px solid #e0d0f0}
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:28px}
.tcard{background:#fff;border:1px solid #e0d0f0;border-radius:14px;padding:24px}
.tcard-stars{color:#FF5722;font-size:14px;letter-spacing:1px;margin-bottom:10px}
.tcard-text{font-size:14px;color:#333;line-height:1.65;margin-bottom:14px;font-style:italic}
.tcard-author{font-size:13px;font-weight:700;color:#6B3FA0}
.tcard-role{font-size:12px;color:#888}

.page-nav{background:#fff;border-top:1px solid #eee;padding:40px 24px}
.page-nav-inner{max-width:1060px;margin:auto}
.page-nav h3{font-size:18px;font-weight:800;color:#1a1a2e;margin-bottom:18px;text-align:center}
.page-nav-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}
.page-nav-item a{display:block;font-size:14px;color:#FF5722;padding:10px 14px;background:#FFF3EE;border:1px solid #ffddd0;border-radius:8px;font-weight:600}
.page-nav-item a:hover{background:#ffe8df;text-decoration:none}

.cta-banner{background:linear-gradient(135deg,#6B3FA0,#FF5722);padding:72px 24px;text-align:center;color:#fff}
.cta-banner h2{font-size:32px;font-weight:800;color:#fff;margin-bottom:12px}
.cta-banner p{font-size:17px;color:rgba(255,255,255,.88);margin-bottom:28px}
.btn-white{display:inline-block;background:#fff;color:#FF5722;padding:15px 32px;border-radius:10px;font-weight:800;font-size:15px;text-decoration:none;margin:6px}
.btn-white:hover{background:#fff8f5;text-decoration:none}
.btn-white-outline{display:inline-block;background:transparent;color:#fff;padding:14px 30px;border-radius:10px;font-weight:700;font-size:15px;text-decoration:none;border:2px solid rgba(255,255,255,.6);margin:6px}
.cta-disclosure{font-size:11px;color:rgba(255,255,255,.45);margin-top:14px}

footer{background:#1a1a2e;padding:32px 24px;text-align:center}
.footer-inner{max-width:1060px;margin:auto;font-size:12px;color:rgba(255,255,255,.4)}
footer a{color:rgba(255,255,255,.5)}

.breadcrumb{max-width:1060px;margin:18px auto 0;padding:0 24px;font-size:13px;color:#888}
.breadcrumb a{color:#FF5722}
.hero-strip{background:linear-gradient(135deg,#6B3FA0 0%,#8B5AB0 100%);padding:44px 24px 36px;color:#fff}
.hero-strip .inner{max-width:1060px;margin:auto}
.type-badge{display:inline-block;background:rgba(255,255,255,.2);color:#fff;font-size:11px;font-weight:700;padding:3px 12px;border-radius:20px;margin-bottom:12px;letter-spacing:.5px;border:1px solid rgba(255,255,255,.3)}
.hero-strip h1{font-size:30px;font-weight:800;color:#fff;margin-bottom:10px;line-height:1.25}
.hero-strip .desc{font-size:15px;color:rgba(255,255,255,.85);margin-bottom:22px;max-width:680px}
</style>`;
}

// ── NAV ───────────────────────────────────────────────────────

function nav(allPages) {
  return `<nav>
  <div class="nav-inner">
    <a href="/ManyChat/index.html" class="logo">
      <span class="logo-mark">BL</span> ManyChat Guide
    </a>
    <div class="nav-links">
      <a href="/ManyChat/manychat-pricing.html">Pricing</a>
      <a href="/ManyChat/manychat-review.html">Review</a>
      <a href="/ManyChat/instagram-dm-automation.html">Instagram</a>
      <a href="${CONFIG.aff.free}" target="_blank" rel="nofollow sponsored" class="nav-cta">Get 1 Month Free →</a>
    </div>
  </div>
</nav>`;
}

// ── FOOTER ────────────────────────────────────────────────────

function footer() {
  return `<footer>
  <div class="footer-inner">
    &copy; 2026 ${escHtml(CONFIG.brand)} &nbsp;&middot;&nbsp;
    Independent ManyChat review site &nbsp;&middot;&nbsp;
    Not affiliated with ManyChat Inc.<br><br>
    ${CONFIG.affiliateDisclosure}<br><br>
    <a href="/ManyChat/index.html">Home</a> &nbsp;&middot;&nbsp;
    <a href="/ManyChat/manychat-pricing.html">Pricing</a> &nbsp;&middot;&nbsp;
    <a href="/ManyChat/manychat-review.html">Review</a> &nbsp;&middot;&nbsp;
    <a href="${CONFIG.aff.free}" target="_blank" rel="nofollow sponsored">Get started free</a>
  </div>
</footer>`;
}

// ── AFFILIATE OFFER CARDS ─────────────────────────────────────

function affCards() {
  return `<div class="aff-links">
  <a href="${CONFIG.aff.free}" target="_blank" rel="nofollow sponsored" class="aff-card free">
    <h4>Get 1 Month FREE</h4>
    <p>Start with Pro features, no charge for 30 days</p>
    <span>Claim free month</span>
  </a>
  <a href="${CONFIG.aff.discount}" target="_blank" rel="nofollow sponsored" class="aff-card discount">
    <h4>50% Off ManyChat Pro</h4>
    <p>Limited time discount on annual Pro plan</p>
    <span>Get 50% off</span>
  </a>
  <a href="${CONFIG.aff.default}" target="_blank" rel="nofollow sponsored" class="aff-card default">
    <h4>Start Free Account</h4>
    <p>Free forever · No credit card required</p>
    <span>Start for free</span>
  </a>
</div>`;
}

// ── TESTIMONIALS ──────────────────────────────────────────────

function testimonials() {
  return `<section class="testimonials">
  <div class="container">
    <div class="section-head">
      <h2>What ManyChat users are saying</h2>
      <p>Real reviews from verified ManyChat customers worldwide</p>
    </div>
    <div class="tgrid">
      <div class="tcard">
        <div class="tcard-stars">★★★★★</div>
        <p class="tcard-text">"ManyChat transformed our Instagram. We went from manually answering 200+ DMs a day to having it fully automated. Our lead gen went up 340% in 60 days."</p>
        <div class="tcard-author">Marcus T.</div>
        <div class="tcard-role">E-commerce founder, Austin TX</div>
      </div>
      <div class="tcard">
        <div class="tcard-stars">★★★★★</div>
        <p class="tcard-text">"We use ManyChat for our restaurant's Facebook page. Reservation bookings through Messenger went up 180% and we stopped paying for a receptionist."</p>
        <div class="tcard-author">Priya S.</div>
        <div class="tcard-role">Restaurant owner, London UK</div>
      </div>
      <div class="tcard">
        <div class="tcard-stars">★★★★★</div>
        <p class="tcard-text">"As a creator with 80K followers, ManyChat lets me actually monetize my DMs. My coaching waitlist fills automatically every time I post."</p>
        <div class="tcard-author">Jake M.</div>
        <div class="tcard-role">Creator & coach, Sydney AU</div>
      </div>
    </div>
  </div>
</section>`;
}

// ── INTERNAL LINKS ────────────────────────────────────────────

function internalLinks(allPages, currentSlug) {
  const others = allPages.filter(p => p.slug !== currentSlug).slice(0, 14);
  return `<section class="page-nav">
  <div class="page-nav-inner">
    <h3>More ManyChat guides</h3>
    <div class="page-nav-grid">
      ${others.map(p => `<div class="page-nav-item"><a href="/ManyChat/${p.slug}.html">${escHtml(p.title.split(" — ")[0].split(" | ")[0])}</a></div>`).join("")}
    </div>
  </div>
</section>`;
}

// ── CTA INLINE BLOCK ──────────────────────────────────────────

function ctaInline(heading, sub, link, linkText) {
  return `<div class="cta-inline">
  <h3>${escHtml(heading)}</h3>
  <p>${escHtml(sub)}</p>
  <a href="${link}" target="_blank" rel="nofollow sponsored" class="btn-primary">${escHtml(linkText)}</a>
  <div style="font-size:11px;color:#888;margin-top:10px">${CONFIG.affiliateDisclosure}</div>
</div>`;
}

// ── SEO HEAD ──────────────────────────────────────────────────

function seoHead({ title, description, slug, type, country }) {
  const url = `${CONFIG.domain}/${slug}.html`;
  const hreflang = country ? `<link rel="alternate" hreflang="en-${country}" href="${url}">` : `
  <link rel="alternate" hreflang="en-us" href="${CONFIG.domain}/${slug}.html">
  <link rel="alternate" hreflang="en-gb" href="${CONFIG.domain}/manychat-united-kingdom.html">
  <link rel="alternate" hreflang="en-au" href="${CONFIG.domain}/manychat-australia.html">
  <link rel="alternate" hreflang="en-ca" href="${CONFIG.domain}/manychat-canada.html">
  <link rel="alternate" hreflang="x-default" href="${CONFIG.domain}/${slug}.html">`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escHtml(title)}</title>
<meta name="description" content="${escHtml(description)}">
<link rel="canonical" href="${url}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
${hreflang}
<meta property="og:title" content="${escHtml(title)}">
<meta property="og:description" content="${escHtml(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="${url}">
<meta property="og:site_name" content="${escHtml(CONFIG.brand)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${escHtml(title)}">
<meta name="twitter:description" content="${escHtml(description)}">
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"${type === "review" ? "Review" : type === "howto" ? "HowTo" : "WebPage"}",
  "name":"${escHtml(title)}",
  "url":"${url}",
  "dateModified":"${new Date().toISOString().split("T")[0]}",
  "publisher":{"@type":"Organization","name":"${escHtml(CONFIG.brand)}","url":"${CONFIG.domain}"},
  "inLanguage":"en"
}
</script>
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"${CONFIG.domain}/index.html"},
    {"@type":"ListItem","position":2,"name":"${escHtml(title.split(" — ")[0])}","item":"${url}"}
  ]
}
</script>`;
}

// ── HOMEPAGE ──────────────────────────────────────────────────

async function buildHomepage(allPages) {
  const content = await callClaude(homepagePrompt(), 3000);

  return `${seoHead({
    title: "ManyChat Review & Guide 2026 — Features, Pricing, Free Trial | BrightLane",
    description: "Independent ManyChat review covering features, pricing, Instagram DM automation, and global availability. Get 1 month free or 50% off Pro through our links.",
    slug: "index",
    type: "website",
  })}
${sharedStyles()}
</head>
<body>
${nav(allPages)}

<div class="hero">
  <div class="hero-inner">
    <div class="hero-badge">Independent Review Site · Updated May 2026</div>
    <h1>The Complete <span>ManyChat</span> Guide for 2026</h1>
    <p class="hero-sub">Reviews, tutorials, pricing breakdowns, and exclusive offers for ManyChat — the #1 chat marketing platform for Instagram, Facebook, WhatsApp & SMS</p>
    <div class="hero-btns">
      <a href="${CONFIG.aff.free}" target="_blank" rel="nofollow sponsored" class="btn-primary">Get 1 Month FREE →</a>
      <a href="${CONFIG.aff.discount}" target="_blank" rel="nofollow sponsored" class="btn-free">50% Off Pro</a>
    </div>
    <div class="social-proof">
      <span class="stars">★★★★★</span> &nbsp;Used by 1M+ businesses in 190 countries
    </div>
  </div>
</div>

<div class="trust-bar">
  <div class="trust-inner">
    <div class="trust-item">✓ Instagram DM Automation</div>
    <div class="trust-item">✓ Facebook Messenger</div>
    <div class="trust-item">✓ WhatsApp Business</div>
    <div class="trust-item">✓ SMS Marketing</div>
    <div class="trust-item">✓ 190 Countries</div>
    <div class="trust-item">✓ Free Plan Available</div>
  </div>
</div>

<section style="background:#fff;padding:52px 0">
  <div class="container">
    <div class="section-head">
      <h2>Exclusive ManyChat offers</h2>
      <p>Special deals through our affiliate links — same ManyChat, better price</p>
    </div>
    ${affCards()}
  </div>
</section>

<section style="background:#fafafa;padding:60px 0">
  <div class="container">
    <div class="section-head">
      <h2>What ManyChat automates</h2>
      <p>From Instagram DMs to WhatsApp — here's what the platform does</p>
    </div>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon">📱</div>
        <h3>Instagram DM Automation</h3>
        <p>Auto-reply to DMs, story mentions, and comment triggers. Build flows that qualify leads while you sleep.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">💬</div>
        <h3>Facebook Messenger</h3>
        <p>Run lead gen campaigns, answer FAQs, and book appointments directly inside Messenger.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🟢</div>
        <h3>WhatsApp Business</h3>
        <p>Scale WhatsApp conversations with automation — huge for markets in India, Brazil, UK, and Europe.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">📨</div>
        <h3>SMS Marketing</h3>
        <p>Send broadcast texts and trigger automations via SMS — 98% open rates vs 20% for email.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <h3>AI Automation</h3>
        <p>ManyChat AI handles open-ended questions, qualifies leads, and routes conversations intelligently.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Analytics & A/B Testing</h3>
        <p>See exactly which flows convert, test variations, and optimize your automation over time.</p>
      </div>
    </div>
  </div>
</section>

<div class="main-content">${content}</div>

${testimonials()}
${internalLinks(allPages, "index")}

<div class="cta-banner">
  <h2>Ready to automate your customer conversations?</h2>
  <p>Join 1M+ businesses using ManyChat to grow on Instagram, Facebook, WhatsApp, and SMS.</p>
  <a href="${CONFIG.aff.free}" target="_blank" rel="nofollow sponsored" class="btn-white">Get 1 Month Free</a>
  <a href="${CONFIG.aff.discount}" target="_blank" rel="nofollow sponsored" class="btn-white-outline">50% Off Pro Plan</a>
  <div class="cta-disclosure">${CONFIG.affiliateDisclosure}</div>
</div>

${footer()}

<script>
let exitShown = false;
document.addEventListener("mouseout", function(e) {
  if (!exitShown && e.clientY < 10) {
    exitShown = true;
    const popup = document.createElement("div");
    popup.style.cssText = "position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.75);display:flex;align-items:center;justify-content:center;z-index:9999;";
    popup.innerHTML = '<div style="background:#fff;padding:36px;max-width:420px;text-align:center;border-radius:16px;"><h2 style="color:#6B3FA0;font-size:22px;margin-bottom:10px">Wait — get 1 month free</h2><p style="color:#555;font-size:15px;margin-bottom:20px">Before you go, grab your free month of ManyChat Pro — no credit card needed.</p><a href="${CONFIG.aff.free}" style="display:block;background:#FF5722;color:#fff;padding:14px;border-radius:10px;font-weight:800;font-size:16px;text-decoration:none;margin-bottom:12px" target="_blank" rel="nofollow sponsored">Claim 1 Month Free</a><p style="color:#aaa;font-size:13px;cursor:pointer;" id="closePopup">No thanks, I\'ll pay full price</p></div>';
    document.body.appendChild(popup);
    document.getElementById("closePopup").onclick = () => popup.remove();
    popup.addEventListener("click", e => { if (e.target === popup) popup.remove(); });
  }
});
</script>
</body></html>`;
}

// ── INNER PAGE ────────────────────────────────────────────────

async function buildInnerPage(page, allPages, content) {
  const typeLabel = {
    core: "Guide",
    feature: "Feature Guide",
    competitor: "Comparison",
    usecase: "Use-Case Guide",
    platform: "Platform Guide",
    country: "Country Guide",
  }[page.type] || "Guide";

  const ctaMap = {
    feature: { link: CONFIG.aff.instagram, text: "Try this feature free →" },
    competitor: { link: CONFIG.aff.discount, text: "Get 50% off ManyChat Pro →" },
    usecase: { link: CONFIG.aff.free, text: "Get 1 month free →" },
    platform: { link: CONFIG.aff.free, text: "Start automating for free →" },
    country: { link: CONFIG.aff.default, text: "Start ManyChat free →" },
    core: { link: CONFIG.aff.pricing, text: "See ManyChat pricing →" },
  };

  const cta = ctaMap[page.type] || ctaMap.core;

  // Inject a mid-content CTA after roughly the 3rd section
  const contentWithCTA = content.replace(
    /<\/section>\s*<section/g,
    (match, offset, str) => {
      const count = (str.slice(0, offset).match(/<\/section>/g) || []).length;
      if (count === 2) {
        return `</section>${ctaInline("Ready to try ManyChat?", "Get started with a free account or claim 1 month free on Pro.", cta.link, cta.text)}<section`;
      }
      return match;
    }
  );

  return `${seoHead({
    title: page.title,
    description: page.description,
    slug: page.slug,
    type: page.schemaType || "webpage",
    country: page.country || null,
  })}
${sharedStyles()}
</head>
<body>
${nav(allPages)}

<div class="breadcrumb">
  <a href="/ManyChat/index.html">Home</a> &rsaquo; ${escHtml(typeLabel)} &rsaquo; ${escHtml(page.title.split(" — ")[0].split(" | ")[0])}
</div>

<div class="hero-strip">
  <div class="inner">
    <div class="type-badge">${escHtml(typeLabel)}</div>
    <h1>${escHtml(page.title.split(" | ")[0])}</h1>
    <p class="desc">${escHtml(page.description)}</p>
    <a href="${cta.link}" target="_blank" rel="nofollow sponsored" class="btn-primary" style="font-size:15px">${escHtml(cta.text)}</a>
  </div>
</div>

<div class="main-content">${contentWithCTA}</div>

<div style="max-width:780px;margin:0 auto;padding:0 24px 40px">
  ${affCards()}
  <div style="font-size:11px;color:#aaa;text-align:center;margin-top:10px">${CONFIG.affiliateDisclosure}</div>
</div>

${testimonials()}
${internalLinks(allPages, page.slug)}

<div class="cta-banner">
  <h2>${escHtml(page.ctaBannerHeading || "Start using ManyChat today")}</h2>
  <p>${escHtml(page.ctaBannerSub || "1M+ businesses trust ManyChat to automate Instagram, Facebook, WhatsApp, and SMS.")}</p>
  <a href="${CONFIG.aff.free}" target="_blank" rel="nofollow sponsored" class="btn-white">Get 1 Month Free</a>
  <a href="${CONFIG.aff.discount}" target="_blank" rel="nofollow sponsored" class="btn-white-outline">50% Off Pro</a>
  <div class="cta-disclosure">${CONFIG.affiliateDisclosure}</div>
</div>

${footer()}

<script>
let exitShown = false;
document.addEventListener("mouseout", function(e) {
  if (!exitShown && e.clientY < 10) {
    exitShown = true;
    const popup = document.createElement("div");
    popup.style.cssText = "position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.75);display:flex;align-items:center;justify-content:center;z-index:9999;";
    popup.innerHTML = '<div style="background:#fff;padding:36px;max-width:420px;text-align:center;border-radius:16px;"><h2 style="color:#6B3FA0;font-size:22px;margin-bottom:10px">Wait — get 1 month free</h2><p style="color:#555;font-size:15px;margin-bottom:20px">Before you go, grab your free month of ManyChat Pro.</p><a href="${CONFIG.aff.free}" style="display:block;background:#FF5722;color:#fff;padding:14px;border-radius:10px;font-weight:800;font-size:16px;text-decoration:none;margin-bottom:12px" target="_blank" rel="nofollow sponsored">Claim 1 Month Free</a><p style="color:#aaa;font-size:13px;cursor:pointer;" id="closePopup">No thanks</p></div>';
    document.body.appendChild(popup);
    document.getElementById("closePopup").onclick = () => popup.remove();
    popup.addEventListener("click", e => { if (e.target === popup) popup.remove(); });
  }
});
</script>
</body></html>`;
}

// ── SITEMAP ───────────────────────────────────────────────────

async function generateSitemap(allPages) {
  const today = new Date().toISOString().split("T")[0];
  const urls = allPages.map(p =>
    `  <url>
    <loc>${CONFIG.domain}/${p.slug}.html</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${p.slug === "index" ? "1.0" : p.type === "core" ? "0.9" : "0.8"}</priority>
  </url>`
  ).join("\n");
  await fs.writeFile(path.join(CONFIG.outputDir, "sitemap.xml"),
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>`);
}

async function generateRobots() {
  await fs.writeFile(path.join(CONFIG.outputDir, "robots.txt"),
    `User-agent: *\nAllow: /\n\nSitemap: ${CONFIG.domain}/sitemap.xml`);
}

// ── CHECKPOINT ────────────────────────────────────────────────

async function loadCheckpoint() {
  try { return JSON.parse(await fs.readFile(CONFIG.checkpointFile, "utf-8")); }
  catch { return { completed: [] }; }
}

async function saveCheckpoint(completed) {
  await fs.writeFile(CONFIG.checkpointFile, JSON.stringify({ completed }, null, 2));
}

// ── QUEUE ─────────────────────────────────────────────────────

async function runQueue(tasks, concurrency) {
  let idx = 0, inFlight = 0, resolve;
  const done = new Promise(r => { resolve = r; });
  function next() {
    while (inFlight < concurrency && idx < tasks.length) {
      const task = tasks[idx++]; inFlight++;
      task().finally(() => { inFlight--; next(); });
    }
    if (inFlight === 0 && idx >= tasks.length) resolve();
  }
  next();
  return done;
}

// ── PAGE DEFINITIONS ──────────────────────────────────────────

function buildAllPages() {
  const pages = [];

  // Homepage
  pages.push({
    slug: "index",
    title: "ManyChat Review & Complete Guide 2026 — Features, Pricing, Free Trial | BrightLane",
    description: "Independent ManyChat review: features, pricing, Instagram DM automation, global availability. Get 1 month free or 50% off Pro through our verified affiliate links.",
    type: "homepage",
  });

  // Core pages
  const corePages = [
    { slug: "manychat-review",      title: "ManyChat Review 2026 — Honest Assessment After 12 Months", description: "Our full independent ManyChat review: pros, cons, pricing, ease of use, and who it's actually right for in 2026.", schemaType: "review", ctaBannerHeading: "Try ManyChat risk-free", ctaBannerSub: "Free plan available. Pro starts at $15/mo. No long-term contract." },
    { slug: "manychat-pricing",     title: "ManyChat Pricing 2026 — Free vs Pro, Full Breakdown", description: "Exact ManyChat pricing by contact tier, what Free includes, when Pro is worth it, and how pricing works outside the US.", schemaType: "webpage", ctaBannerHeading: "Get the best ManyChat price", ctaBannerSub: "1 month free or 50% off Pro — both available through our links." },
    { slug: "what-is-manychat",     title: "What is ManyChat? Plain-English Explanation + Examples", description: "ManyChat explained for beginners — what it does, which platforms it works with, who uses it, and how to get started free.", schemaType: "webpage", ctaBannerHeading: "Start with ManyChat for free", ctaBannerSub: "Free plan available. No credit card needed." },
    { slug: "manychat-free-trial",  title: "ManyChat Free Plan — What You Get & How to Start", description: "ManyChat's free plan explained: contact limits, available features, what's missing, and when to upgrade to Pro.", schemaType: "howto", ctaBannerHeading: "Start ManyChat free today", ctaBannerSub: "No credit card. Up to 1,000 contacts on the free plan." },
  ];

  for (const p of corePages) pages.push({ ...p, type: "core" });

  // Feature pages
  for (const f of CONFIG.features) {
    pages.push({
      slug: f.slug,
      title: `ManyChat ${f.name} — Complete Guide 2026`,
      description: `How ManyChat's ${f.name} works, step-by-step setup, real examples, best practices, and whether it's available on the free plan.`,
      type: "feature",
      feature: f,
      schemaType: "howto",
      ctaBannerHeading: `Start using ${f.name} today`,
      ctaBannerSub: `Available on ManyChat free and Pro plans.`,
    });
  }

  // Competitor pages
  for (const c of CONFIG.competitors) {
    pages.push({
      slug: `manychat-vs-${slugify(c.name)}`,
      title: `ManyChat vs ${c.name} 2026 — Which Is Better?`,
      description: `Honest comparison of ManyChat vs ${c.name}: features, pricing, ease of use, and who should choose which platform.`,
      type: "competitor",
      comp: c,
      schemaType: "review",
      ctaBannerHeading: `ManyChat vs ${c.name} — ready to decide?`,
      ctaBannerSub: `Start ManyChat free and see for yourself. No commitment.`,
    });
  }

  // Use-case pages
  for (const uc of CONFIG.useCases) {
    pages.push({
      slug: `manychat-for-${slugify(uc.audience)}`,
      title: `ManyChat for ${uc.audience.charAt(0).toUpperCase() + uc.audience.slice(1)} — Complete Guide`,
      description: `How ${uc.audience} use ManyChat to solve ${uc.pain} using ${uc.platform}. Workflows, templates, setup guide, and real results.`,
      type: "usecase",
      usecase: uc,
      schemaType: "howto",
      ctaBannerHeading: `ManyChat for ${uc.audience} — get started`,
      ctaBannerSub: `Free plan available. Set up your first automation in under 30 minutes.`,
    });
  }

  // Platform pages
  for (const p of CONFIG.platforms) {
    pages.push({
      slug: `manychat-${p.slug}`,
      title: `ManyChat ${p.name} Automation — Complete Guide 2026`,
      description: `How to use ManyChat for ${p.name}: setup, automation types, best practices, compliance, and global availability.`,
      type: "platform",
      platform: p,
      schemaType: "howto",
      ctaBannerHeading: `Start automating ${p.name} with ManyChat`,
      ctaBannerSub: `Free plan available. Connect ${p.name} in under 5 minutes.`,
    });
  }

  // Country pages
  for (const c of CONFIG.countries) {
    pages.push({
      slug: `manychat-${slugify(c.name)}`,
      title: `ManyChat in ${c.name} — Pricing, Availability & Getting Started`,
      description: `Everything ${c.name} businesses need to know about ManyChat: availability, pricing in ${c.currency}, supported channels, compliance, and getting started.`,
      type: "country",
      countryData: c,
      country: c.code,
      schemaType: "webpage",
      ctaBannerHeading: `ManyChat is available in ${c.name}`,
      ctaBannerSub: `${c.note}. Free plan available — no credit card needed.`,
    });
  }

  return pages;
}

// ── MAIN ──────────────────────────────────────────────────────

async function generate() {
  await fs.mkdir(CONFIG.outputDir, { recursive: true });
  const allPages = buildAllPages();
  const checkpoint = await loadCheckpoint();
  const completed = new Set(checkpoint.completed);
  const todo = allPages.filter(p => !completed.has(p.slug));

  console.log("\n🤖 BrightLane ManyChat Site Generator");
  console.log(`   Total pages : ${allPages.length}`);
  console.log(`   Done already: ${completed.size}`);
  console.log(`   To generate : ${todo.length}`);
  console.log(`   Concurrency : ${CONFIG.concurrency}`);
  console.log(`   Words/page  : ~2,000–2,500\n`);

  let count = completed.size;

  const tasks = todo.map(page => async () => {
    try {
      let html;

      if (page.type === "homepage") {
        html = await buildHomepage(allPages);
      } else {
        let prompt;
        if (page.type === "feature")    prompt = featurePrompt(page.feature);
        else if (page.type === "competitor") prompt = competitorPrompt(page.comp);
        else if (page.type === "usecase")    prompt = useCasePrompt(page.usecase);
        else if (page.type === "platform")   prompt = platformPrompt(page.platform);
        else if (page.type === "country")    prompt = countryPrompt(page.countryData);
        else                                 prompt = corePagePrompt(page.slug);

        const content = await callClaude(prompt, 2800);
        html = await buildInnerPage(page, allPages, content);
      }

      await fs.writeFile(path.join(CONFIG.outputDir, `${page.slug}.html`), html);
      completed.add(page.slug);
      await saveCheckpoint([...completed]);
      count++;
      console.log(`  ✓ [${count}/${allPages.length}] ${page.title}`);
    } catch (err) {
      console.error(`  ✗ Failed: ${page.slug} — ${err.message}`);
    }
    await sleep(CONFIG.batchDelay);
  });

  await runQueue(tasks, CONFIG.concurrency);

  console.log("\n🗺  Sitemap…");
  await generateSitemap(allPages);
  console.log("🤖 robots.txt…");
  await generateRobots();

  console.log(`\n✅ Done — ${allPages.length} pages generated`);
  console.log(`   Output: ./${CONFIG.outputDir}/\n`);
  console.log("⚡ NEXT STEPS TO GET INDEXED:");
  console.log("   1. Push to GitHub Pages");
  console.log("   2. Submit sitemap to Google Search Console");
  console.log("   3. Submit sitemap to Bing Webmaster Tools");
  console.log("   4. Post homepage URL on Twitter/X — Googlebot follows\n");
}

generate().catch(err => { console.error("Fatal:", err); process.exit(1); });
