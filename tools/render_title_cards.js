#!/usr/bin/env node
/**
 * tools/render_title_cards.js
 * CLI helper to run the Title-Card Deterministic Video Renderer from anywhere in the workspace.
 */

import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectDir = path.resolve(__dirname, '..', 'projects', 'title_cards');
const script = path.join(projectDir, 'render.mjs');

const child = spawn(process.execPath, [script, ...process.argv.slice(2)], {
  cwd: projectDir,
  stdio: 'inherit'
});

child.on('exit', (code) => {
  process.exit(code ?? 0);
});
