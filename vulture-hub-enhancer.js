#!/usr/bin/env node
const fs = require('fs-extra');
const path = require('path');
const dayjs = require('dayjs');

const MANYCHAT_CTA = "https://manychat.partnerlinks.io/nwkkk7vkps17";
const VULTURE_PAGES_DIR = 'pages';
const TARGET_PAGES = 1000; // Scale from 833 → 1K+
const OUTPUT_DIR = '.';

fs.ensureDirSync(VULTURE_PAGES_DIR);

// 1. Generate 1,000 vulture pages
function generateVulturePages() {
  console.log('🔥 Generating 1,000 Vulture pages...');
  
  for (let i = 1; i <= TARGET_PAGES; i++) {
    const pageContent = `<!DOCTYPE html>
<html lang="en">
<head>
  <title>ManyChat Strategy #${i} - Advanced Automation</title>
  <meta name="description" content="ManyChat Strategy #${i}: Scale your automation with proven workflows.">
</head>
<body>
  <h1>ManyChat Strategy #${i}</h1>
  <p>Advanced ManyChat automation workflow #${i} for maximum conversions.</p>
  
  <div style="background: #667eea; color: white; padding: 20px; text-align
