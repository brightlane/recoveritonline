#!/usr/bin/env node
const fs = require('fs-extra');
const path = require('path');
const dayjs = require('dayjs');

const BASE_URL = 'https://brightlane.github.io/manychat.com/';
const PAGES_DIR = 'pages';
const SITEMAP_FILE
