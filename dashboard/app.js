// ═══════════════════════════════════════════════════════════════════════
// BENAQAAB INDIA — STUDIO COMMAND CENTER INTERACTION LOGIC
// ═══════════════════════════════════════════════════════════════════════

let activeFilter = 'ALL';
let activeSearch = '';
let activeView = 'GRID'; // 'GRID' | 'TABLE' | 'KANBAN'
let currentHeroCode = 'EP-17'; // Default featured flagship

// DOM Cache
const heroStageEl = document.getElementById('heroStage');
const bentoGridEl = document.getElementById('bentoGrid');
const tableViewWrapEl = document.getElementById('tableViewWrap');
const tableBodyEl = document.getElementById('tableBody');
const kanbanViewWrapEl = document.getElementById('kanbanViewWrap');
const searchInputEl = document.getElementById('searchInput');
const clearSearchBtnEl = document.getElementById('clearSearchBtn');
const filterChipsEl = document.querySelectorAll('.filter-chip');
const viewBtnsEl = document.querySelectorAll('.view-btn');

// Modal DOM
const theaterModalEl = document.getElementById('theaterModal');
const theaterTitleEl = document.getElementById('theaterTitle');
const sandboxFrameEl = document.getElementById('sandboxFrame');
const toggleFrameAspectBtn = document.getElementById('toggleFrameAspectBtn');
const openNewWindowBtn = document.getElementById('openNewWindowBtn');
const theaterCloseBtn = document.getElementById('theaterCloseBtn');

let currentSandboxUrl = '';
let currentSandboxFormat = '16:9';

// Bootstrap
function init() {
  renderHero(currentHeroCode);
  updateStatsRibbon();
  renderActiveView();
  bindEvents();
}

// ─── HERO CINEMATIC SHOWCASE ──────────────────────────────────────────
function renderHero(code) {
  const item = window.PRODUCTIONS_DATA.find(p => p.code === code) || window.PRODUCTIONS_DATA[0];
  currentHeroCode = item.code;

  let mediaMarkup = '';
  if (item.thumbUrl) {
    mediaMarkup = `<img src="${item.thumbUrl}" alt="${item.title}" class="hero-media-img">`;
  } else {
    mediaMarkup = `
      <div class="procedural-poster" style="height: 100%;">
        <div class="procedural-grid-bg"></div>
        <div class="procedural-code">${item.code}</div>
        <div class="procedural-badge">${item.category}</div>
      </div>
    `;
  }

  let launchBtn = '';
  if (item.hasComp && item.previewUrl) {
    launchBtn = `
      <button class="btn-hero-primary" onclick="launchSandbox('${item.code}', '${escapeStr(item.title)}', '${item.previewUrl}', '${item.format}')">
        <span>⚡ Launch comp.html Live</span>
      </button>
    `;
  } else {
    launchBtn = `
      <span class="btn-hero-secondary" style="cursor: default; opacity: 0.8;">
        <span>✓ Broadcast Archived</span>
      </span>
    `;
  }

  heroStageEl.innerHTML = `
    <div class="hero-backdrop-glow"></div>
    <div class="hero-content">
      <div class="hero-tag-row">
        <span class="hero-pill-badge feat">★ FEATURED FLAGSHIP</span>
        <span class="hero-pill-badge cat">${item.category}</span>
        <span class="hero-pill-badge" style="background: rgba(255,255,255,0.06); border: 1px solid var(--border-subtle); color: #fff;">${item.code} · ${item.format}</span>
      </div>
      <h2 class="hero-title">${item.title}</h2>
      <div class="hero-hindi">${item.hindiTitle}</div>
      <p class="hero-quote">${item.heroQuote}</p>
      
      <div class="hero-stats-strip">
        <div class="hero-mini-stat">
          <div class="hero-mini-label">Duration</div>
          <div class="hero-mini-val">⏱️ ${item.duration}</div>
        </div>
        <div class="hero-mini-stat">
          <div class="hero-mini-label">Fact Ledger</div>
          <div class="hero-mini-val">${item.factsCount}</div>
        </div>
        <div class="hero-mini-stat">
          <div class="hero-mini-label">Master Audio</div>
          <div class="hero-mini-val">🎙️ -14.0 LUFS</div>
        </div>
      </div>

      <div class="hero-actions">
        ${launchBtn}
        <button class="btn-hero-secondary" onclick="scrollToRegistry()">
          <span>Explore All 34 Topics ↓</span>
        </button>
      </div>
    </div>

    <div class="hero-media-wrap">
      ${mediaMarkup}
      <div class="hero-media-overlay">
        <span class="hero-overlay-tag">GRADE: ${item.gradeProfile}</span>
      </div>
    </div>
  `;
}

// ─── STATS RIBBON ─────────────────────────────────────────────────────
function updateStatsRibbon() {
  const data = window.PRODUCTIONS_DATA;
  const delivered = data.filter(p => p.status === 'DONE').length;
  const docs = data.filter(p => p.status === 'DONE' && p.format.includes('16:9')).length;
  const shorts = data.filter(p => p.status === 'DONE' && p.format.includes('9:16')).length;
  const live = data.filter(p => p.status === 'LIVE_CYCLE').length;
  const backlog = data.filter(p => p.status === 'BACKLOG').length;

  document.getElementById('statTotalDelivered').innerText = delivered;
  document.getElementById('statDocs').innerText = docs;
  document.getElementById('statShorts').innerText = shorts;
  document.getElementById('statLiveCycles').innerText = live;
  document.getElementById('statBacklog').innerText = backlog;

  // Update chip counters
  document.querySelector('[data-filter="ALL"] .chip-counter').innerText = data.length;
  document.querySelector('[data-filter="DONE"] .chip-counter').innerText = delivered;
  document.querySelector('[data-filter="16:9"] .chip-counter').innerText = docs;
  document.querySelector('[data-filter="9:16"] .chip-counter').innerText = shorts;
  document.querySelector('[data-filter="LIVE_CYCLE"] .chip-counter').innerText = live;
  document.querySelector('[data-filter="BACKLOG"] .chip-counter').innerText = backlog;
  document.querySelector('[data-filter="BLACKLIST"] .chip-counter').innerText = data.filter(p => p.status === 'BLACKLIST').length;
}

// ─── FILTERING LOGIC ──────────────────────────────────────────────────
function getFilteredData() {
  const q = activeSearch.toLowerCase().trim();
  return window.PRODUCTIONS_DATA.filter(item => {
    let matchesFilter = true;
    if (activeFilter === 'DONE') matchesFilter = item.status === 'DONE';
    else if (activeFilter === '16:9') matchesFilter = item.format.includes('16:9');
    else if (activeFilter === '9:16') matchesFilter = item.format.includes('9:16');
    else if (activeFilter === 'LIVE_CYCLE') matchesFilter = item.status === 'LIVE_CYCLE';
    else if (activeFilter === 'BACKLOG') matchesFilter = item.status === 'BACKLOG';
    else if (activeFilter === 'BLACKLIST') matchesFilter = item.status === 'BLACKLIST';

    let matchesSearch = true;
    if (q) {
      const matchCode = item.code.toLowerCase().includes(q);
      const matchTitle = item.title.toLowerCase().includes(q);
      const matchHindi = item.hindiTitle.toLowerCase().includes(q);
      const matchCat = item.category.toLowerCase().includes(q);
      const matchEvidence = item.evidence.some(e => e.toLowerCase().includes(q));
      matchesSearch = matchCode || matchTitle || matchHindi || matchCat || matchEvidence;
    }

    return matchesFilter && matchesSearch;
  });
}

// ─── RENDER ACTIVE VIEW ───────────────────────────────────────────────
function renderActiveView() {
  const filtered = getFilteredData();

  if (activeView === 'GRID') {
    bentoGridEl.style.display = 'grid';
    tableViewWrapEl.style.display = 'none';
    kanbanViewWrapEl.style.display = 'none';
    renderBentoGrid(filtered);
  } else if (activeView === 'TABLE') {
    bentoGridEl.style.display = 'none';
    tableViewWrapEl.style.display = 'block';
    kanbanViewWrapEl.style.display = 'none';
    renderTableView(filtered);
  } else if (activeView === 'KANBAN') {
    bentoGridEl.style.display = 'none';
    tableViewWrapEl.style.display = 'none';
    kanbanViewWrapEl.style.display = 'grid';
    renderKanbanView(filtered);
  }
}

// ─── VIEW 1: BENTO GRID ───────────────────────────────────────────────
function renderBentoGrid(items) {
  bentoGridEl.innerHTML = '';

  if (items.length === 0) {
    bentoGridEl.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 80px 20px; text-align: center; color: var(--text-muted);">
        <p style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 8px;">No matching productions found</p>
        <p style="font-size: 14px; font-family: var(--font-mono);">Clear search query or pick a different category chip.</p>
      </div>
    `;
    return;
  }

  items.forEach(item => {
    const card = document.createElement('div');
    const statusClass = item.status === 'DONE' ? 'status-done' :
                        item.status === 'LIVE_CYCLE' ? 'status-live' :
                        item.status === 'BACKLOG' ? 'status-backlog' : 'status-blacklist';
    card.className = `cinema-card ${statusClass}`;

    // Tag Status
    let statusTag = '';
    if (item.status === 'DONE') statusTag = `<span class="tag-status tag-done">✓ Delivered</span>`;
    else if (item.status === 'LIVE_CYCLE') statusTag = `<span class="tag-status tag-live">⏳ Active Cycle</span>`;
    else if (item.status === 'BACKLOG') statusTag = `<span class="tag-status tag-backlog">🟢 Researched</span>`;
    else statusTag = `<span class="tag-status tag-blacklist">🚫 Blacklist</span>`;

    // Poster Media
    let posterMedia = '';
    if (item.thumbUrl) {
      posterMedia = `<img src="${item.thumbUrl}" alt="${item.title}" loading="lazy" onerror="this.onerror=null; this.parentElement.innerHTML='<div class=\\'procedural-poster\\'><div class=\\'procedural-grid-bg\\'></div><div class=\\'procedural-code\\'>${item.code}</div><div class=\\'procedural-badge\\'>${item.category}</div></div>'">`;
    } else {
      posterMedia = `
        <div class="procedural-poster">
          <div class="procedural-grid-bg"></div>
          <div class="procedural-code">${item.code}</div>
          <div class="procedural-badge">${item.category}</div>
        </div>
      `;
    }

    // Launch Button
    let launchBtn = '';
    if (item.hasComp && item.previewUrl) {
      launchBtn = `
        <button class="btn-card-launch" onclick="launchSandbox('${item.code}', '${escapeStr(item.title)}', '${item.previewUrl}', '${item.format}')">
          <span>⚡ Launch comp.html</span>
        </button>
      `;
    } else if (item.status === 'LIVE_CYCLE') {
      launchBtn = `<span style="font-family: var(--font-mono); font-size: 11px; color: var(--accent-gold); font-weight: 700;">⚡ Ready to Produce</span>`;
    } else if (item.status === 'BACKLOG') {
      launchBtn = `<span style="font-family: var(--font-mono); font-size: 11px; color: var(--accent-cyan); font-weight: 700;">📁 Data Locked</span>`;
    } else if (item.status === 'BLACKLIST') {
      launchBtn = `<span style="font-family: var(--font-mono); font-size: 11px; color: var(--accent-rose); font-weight: 700;">❌ Blocked</span>`;
    } else {
      launchBtn = `<span style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted);">Archive Saved</span>`;
    }

    const factsList = item.evidence.map(e => `<li>${e}</li>`).join('');

    card.innerHTML = `
      <div class="card-poster" onclick="renderHero('${item.code}')" style="cursor: pointer;" title="Click to spotlight in Hero">
        ${posterMedia}
        <div class="card-floating-badges">
          <span class="tag-code">${item.code}</span>
          ${statusTag}
        </div>
      </div>
      <div class="card-body">
        <div class="card-spec-row">
          <span>${item.category}</span>
          <span class="sep">•</span>
          <span>${item.format}</span>
          <span class="sep">•</span>
          <span>⏱️ ${item.duration}</span>
        </div>
        <h3 class="card-heading" onclick="renderHero('${item.code}')" style="cursor: pointer;">${item.title}</h3>
        <div class="card-hindi-sub">${item.hindiTitle}</div>
        <ul class="card-fact-list">
          ${factsList}
        </ul>
        <div class="card-bottom-bar">
          <div class="card-audio-stamp">
            <span>🎙️</span>
            <span>${item.audioClock}</span>
          </div>
          ${launchBtn}
        </div>
      </div>
    `;

    bentoGridEl.appendChild(card);
  });
}

// ─── VIEW 2: TABLE MATRIX ─────────────────────────────────────────────
function renderTableView(items) {
  tableBodyEl.innerHTML = '';

  items.forEach(item => {
    const tr = document.createElement('tr');

    let statusPill = '';
    if (item.status === 'DONE') statusPill = `<span class="tag-status tag-done">Delivered</span>`;
    else if (item.status === 'LIVE_CYCLE') statusPill = `<span class="tag-status tag-live">Active</span>`;
    else if (item.status === 'BACKLOG') statusPill = `<span class="tag-status tag-backlog">Backlog</span>`;
    else statusPill = `<span class="tag-status tag-blacklist">Blocked</span>`;

    let actionBtn = '';
    if (item.hasComp && item.previewUrl) {
      actionBtn = `
        <button class="btn-card-launch" style="padding: 6px 12px; font-size: 11px;" onclick="launchSandbox('${item.code}', '${escapeStr(item.title)}', '${item.previewUrl}', '${item.format}')">
          ⚡ Launch
        </button>
      `;
    } else {
      actionBtn = `<span style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted);">-</span>`;
    }

    tr.innerHTML = `
      <td><span class="table-code">${item.code}</span></td>
      <td>
        <div class="table-title">${item.title}</div>
        <div class="table-hindi">${item.hindiTitle}</div>
      </td>
      <td><span style="font-family: var(--font-mono); font-size: 11px;">${item.format}</span></td>
      <td><span style="font-family: var(--font-mono); font-size: 12px; color: #fff;">${item.duration}</span></td>
      <td><span style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted);">${item.gradeProfile}</span></td>
      <td><span style="font-size: 12px; color: var(--text-secondary);">${item.sourceAgencies || item.evidence[0]}</span></td>
      <td><span style="font-family: var(--font-mono); font-size: 11px;">${item.audioClock}</span></td>
      <td>${statusPill}</td>
      <td>${actionBtn}</td>
    `;
    tableBodyEl.appendChild(tr);
  });
}

// ─── VIEW 3: KANBAN PIPELINE ──────────────────────────────────────────
function renderKanbanView(items) {
  kanbanViewWrapEl.innerHTML = '';

  const columns = [
    { title: "Delivered (100% Done)", status: "DONE", color: "var(--accent-emerald)" },
    { title: "Active Live Cycles", status: "LIVE_CYCLE", color: "var(--accent-gold)" },
    { title: "Researched Backlog", status: "BACKLOG", color: "var(--accent-cyan)" },
    { title: "Blacklist (Blocked)", status: "BLACKLIST", color: "var(--accent-rose)" }
  ];

  columns.forEach(col => {
    const colItems = items.filter(it => it.status === col.status);
    const colEl = document.createElement('div');
    colEl.className = 'kanban-column';

    let cardsHtml = '';
    colItems.forEach(it => {
      cardsHtml += `
        <div class="kanban-card" onclick="renderHero('${it.code}')">
          <div class="kanban-card-top">
            <span class="kanban-card-code">${it.code}</span>
            <span class="kanban-card-duration">${it.duration}</span>
          </div>
          <div class="kanban-card-title">${it.title}</div>
          <div style="font-size: 11px; color: var(--text-muted); margin-top: 6px;">${it.category}</div>
        </div>
      `;
    });

    colEl.innerHTML = `
      <div class="kanban-col-header">
        <span class="kanban-col-title" style="color: ${col.color};">${col.title}</span>
        <span class="chip-counter">${colItems.length}</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 10px; overflow-y: auto; max-height: 700px;">
        ${cardsHtml || '<div style="color: var(--text-muted); font-size: 12px; padding: 12px 0;">No items</div>'}
      </div>
    `;

    kanbanViewWrapEl.appendChild(colEl);
  });
}

// ─── INTERACTIVE SANDBOX LAUNCHER ─────────────────────────────────────
window.launchSandbox = function(code, title, url, format) {
  currentSandboxUrl = url;
  currentSandboxFormat = format.includes('9:16') ? '9:16' : '16:9';

  theaterTitleEl.innerText = `${code} — ${title}`;
  sandboxFrameEl.src = url;

  syncSandboxAspect();
  theaterModalEl.classList.add('active');
  document.body.style.overflow = 'hidden';
};

function syncSandboxAspect() {
  if (currentSandboxFormat === '9:16') {
    sandboxFrameEl.className = 'sandbox-frame aspect-phone';
    toggleFrameAspectBtn.innerText = '📱 Phone (9:16) — Click to Toggle';
  } else {
    sandboxFrameEl.className = 'sandbox-frame';
    toggleFrameAspectBtn.innerText = '🖥️ Widescreen (16:9) — Click to Toggle';
  }
}

function closeSandbox() {
  theaterModalEl.classList.remove('active');
  sandboxFrameEl.src = 'about:blank';
  document.body.style.overflow = '';
}

function scrollToRegistry() {
  const el = document.getElementById('toolbarSection');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

function escapeStr(s) {
  return (s || '').replace(/'/g, "\\'");
}

// ─── EVENT HANDLERS ───────────────────────────────────────────────────
function bindEvents() {
  // Search typing
  searchInputEl.addEventListener('input', (e) => {
    activeSearch = e.target.value;
    clearSearchBtnEl.style.display = activeSearch ? 'flex' : 'none';
    renderActiveView();
  });

  // Clear search
  clearSearchBtnEl.addEventListener('click', () => {
    searchInputEl.value = '';
    activeSearch = '';
    clearSearchBtnEl.style.display = 'none';
    renderActiveView();
  });

  // Filter chips
  filterChipsEl.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChipsEl.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeFilter = chip.getAttribute('data-filter');
      renderActiveView();
    });
  });

  // View Switcher Buttons
  viewBtnsEl.forEach(btn => {
    btn.addEventListener('click', () => {
      viewBtnsEl.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeView = btn.getAttribute('data-view');
      renderActiveView();
    });
  });

  // Sandbox Modal Controls
  theaterCloseBtn.addEventListener('click', closeSandbox);
  theaterModalEl.addEventListener('click', (e) => {
    if (e.target === theaterModalEl) closeSandbox();
  });

  toggleFrameAspectBtn.addEventListener('click', () => {
    currentSandboxFormat = currentSandboxFormat === '9:16' ? '16:9' : '9:16';
    syncSandboxAspect();
  });

  openNewWindowBtn.addEventListener('click', () => {
    if (currentSandboxUrl) window.open(currentSandboxUrl, '_blank');
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && theaterModalEl.classList.contains('active')) {
      closeSandbox();
    }
  });
}

document.addEventListener('DOMContentLoaded', init);
