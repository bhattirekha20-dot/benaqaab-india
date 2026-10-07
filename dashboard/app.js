// Benaqaab India — Studio Localhost Command Center Script

let currentFilter = 'ALL';
let searchQuery = '';

// DOM Elements
const gridEl = document.getElementById('productionsGrid');
const searchInputEl = document.getElementById('searchInput');
const filterPillsEl = document.querySelectorAll('.filter-pill');
const modalOverlayEl = document.getElementById('modalOverlay');
const modalTitleEl = document.getElementById('modalTitle');
const modalIframeEl = document.getElementById('modalIframe');
const modalCloseBtn = document.getElementById('modalCloseBtn');
const frameAspectBtn = document.getElementById('frameAspectBtn');
const openNewTabBtn = document.getElementById('openNewTabBtn');

let currentActiveUrl = '';
let currentFormat = '16:9';

// Initialize
function init() {
  updateStatsRibbon();
  renderGrid();
  bindEvents();
}

// Compute counts and update top stats
function updateStatsRibbon() {
  const totalDelivered = PRODUCTIONS_DATA.filter(p => p.status === 'DONE').length;
  const docsCount = PRODUCTIONS_DATA.filter(p => p.status === 'DONE' && p.format.includes('16:9')).length;
  const shortsCount = PRODUCTIONS_DATA.filter(p => p.status === 'DONE' && p.format.includes('9:16')).length;
  const liveCount = PRODUCTIONS_DATA.filter(p => p.status === 'LIVE_CYCLE').length;
  const backlogCount = PRODUCTIONS_DATA.filter(p => p.status === 'BACKLOG').length;

  document.getElementById('statTotalDelivered').innerText = totalDelivered;
  document.getElementById('statDocs').innerText = docsCount;
  document.getElementById('statShorts').innerText = shortsCount;
  document.getElementById('statLiveCycles').innerText = liveCount;
  document.getElementById('statBacklog').innerText = backlogCount;

  // Update badge counts on pills
  document.querySelector('[data-filter="ALL"] .pill-count').innerText = PRODUCTIONS_DATA.length;
  document.querySelector('[data-filter="DONE"] .pill-count').innerText = totalDelivered;
  document.querySelector('[data-filter="16:9"] .pill-count').innerText = docsCount;
  document.querySelector('[data-filter="9:16"] .pill-count').innerText = shortsCount;
  document.querySelector('[data-filter="LIVE_CYCLE"] .pill-count').innerText = liveCount;
  document.querySelector('[data-filter="BACKLOG"] .pill-count').innerText = backlogCount;
  document.querySelector('[data-filter="BLACKLIST"] .pill-count').innerText = PRODUCTIONS_DATA.filter(p => p.status === 'BLACKLIST').length;
}

// Filter and render cards
function renderGrid() {
  gridEl.innerHTML = '';

  const filtered = PRODUCTIONS_DATA.filter(item => {
    // Filter matching
    let matchesFilter = true;
    if (currentFilter === 'DONE') {
      matchesFilter = item.status === 'DONE';
    } else if (currentFilter === '16:9') {
      matchesFilter = item.format.includes('16:9');
    } else if (currentFilter === '9:16') {
      matchesFilter = item.format.includes('9:16');
    } else if (currentFilter === 'LIVE_CYCLE') {
      matchesFilter = item.status === 'LIVE_CYCLE';
    } else if (currentFilter === 'BACKLOG') {
      matchesFilter = item.status === 'BACKLOG';
    } else if (currentFilter === 'BLACKLIST') {
      matchesFilter = item.status === 'BLACKLIST';
    }

    // Search query matching
    const q = searchQuery.toLowerCase().trim();
    let matchesSearch = true;
    if (q) {
      const matchInCode = item.code.toLowerCase().includes(q);
      const matchInTitle = item.title.toLowerCase().includes(q);
      const matchInHindi = item.hindiTitle.toLowerCase().includes(q);
      const matchInCategory = item.category.toLowerCase().includes(q);
      const matchInEvidence = item.evidence.some(e => e.toLowerCase().includes(q));
      matchesSearch = matchInCode || matchInTitle || matchInHindi || matchInCategory || matchInEvidence;
    }

    return matchesFilter && matchesSearch;
  });

  if (filtered.length === 0) {
    gridEl.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 60px 20px; text-align: center; color: var(--text-dim);">
        <p style="font-size: 18px; margin-bottom: 8px;">No matching topics or videos found</p>
        <p style="font-size: 13px; font-family: var(--font-mono);">Try clearing your search query or choosing another filter.</p>
      </div>
    `;
    return;
  }

  filtered.forEach(item => {
    const card = createCardElement(item);
    gridEl.appendChild(card);
  });
}

// Create single card DOM
function createCardElement(item) {
  const card = document.createElement('div');
  const statusClass = item.status === 'DONE' ? 'is-done' :
                      item.status === 'LIVE_CYCLE' ? 'is-live' :
                      item.status === 'BACKLOG' ? 'is-backlog' : 'is-blacklist';
  card.className = `card ${statusClass}`;

  // Status Badge Markup
  let statusBadge = '';
  if (item.status === 'DONE') {
    statusBadge = `<span class="badge badge-done">✓ Delivered</span>`;
  } else if (item.status === 'LIVE_CYCLE') {
    statusBadge = `<span class="badge badge-live">⏳ Active Cycle</span>`;
  } else if (item.status === 'BACKLOG') {
    statusBadge = `<span class="badge badge-backlog">🟢 Researched</span>`;
  } else {
    statusBadge = `<span class="badge badge-blacklist">🚫 Blacklist</span>`;
  }

  // Media Markup
  let mediaMarkup = '';
  if (item.thumbUrl) {
    mediaMarkup = `<img src="${item.thumbUrl}" alt="${item.title}" loading="lazy" onerror="this.onerror=null; this.parentElement.innerHTML='<div class=\\'media-placeholder\\'>${item.code} · ${item.format}</div>'"/>`;
  } else {
    mediaMarkup = `<div class="media-placeholder">${item.code} · ${item.format}</div>`;
  }

  // Action Button Markup
  let actionBtnMarkup = '';
  if (item.hasComp && item.previewUrl) {
    actionBtnMarkup = `
      <button class="btn-launch" onclick="openPreview('${item.code}', '${item.title.replace(/'/g, "\\'")}', '${item.previewUrl}', '${item.format}')">
        ⚡ Launch comp.html
      </button>
    `;
  } else if (item.status === 'LIVE_CYCLE') {
    actionBtnMarkup = `<span style="font-size: 11px; font-family: var(--font-mono); color: var(--accent-gold);">⚡ Ready to Produce</span>`;
  } else if (item.status === 'BACKLOG') {
    actionBtnMarkup = `<span style="font-size: 11px; font-family: var(--font-mono); color: var(--accent-cyan);">📁 Sourced & Verified</span>`;
  } else if (item.status === 'BLACKLIST') {
    actionBtnMarkup = `<span style="font-size: 11px; font-family: var(--font-mono); color: var(--accent-rose);">❌ Do Not Repeat</span>`;
  } else {
    actionBtnMarkup = `<span style="font-size: 11px; font-family: var(--font-mono); color: var(--text-dim);">Archive Delivered</span>`;
  }

  // Evidence Items
  const evidenceList = item.evidence.map(e => `<li>${e}</li>`).join('');

  card.innerHTML = `
    <div class="card-media">
      ${mediaMarkup}
      <div class="card-badge-strip">
        <span class="badge badge-code">${item.code}</span>
        ${statusBadge}
      </div>
    </div>
    <div class="card-content">
      <div class="card-meta">
        <span>${item.category}</span>
        <span>•</span>
        <span>${item.format}</span>
        <span>•</span>
        <span>⏱️ ${item.duration}</span>
      </div>
      <h3 class="card-title">${item.title}</h3>
      <div class="card-hindi">${item.hindiTitle}</div>
      <ul class="card-evidence-list">
        ${evidenceList}
      </ul>
      <div class="card-footer">
        <div class="audio-clock-tag">
          <span>🎙️</span>
          <span>${item.audioClock}</span>
        </div>
        ${actionBtnMarkup}
      </div>
    </div>
  `;

  return card;
}

// Interactive Preview Modal Launcher
window.openPreview = function(code, title, url, format) {
  currentActiveUrl = url;
  currentFormat = format.includes('9:16') ? '9:16' : '16:9';
  
  modalTitleEl.innerText = `${code} — ${title}`;
  modalIframeEl.src = url;

  updateModalFrame();
  modalOverlayEl.classList.add('active');
  document.body.style.overflow = 'hidden';
};

function updateModalFrame() {
  if (currentFormat === '9:16') {
    modalIframeEl.className = 'preview-iframe frame-9x16';
    frameAspectBtn.innerText = '📱 Phone (9:16)';
  } else {
    modalIframeEl.className = 'preview-iframe frame-16x9';
    frameAspectBtn.innerText = '🖥️ Widescreen (16:9)';
  }
}

function closeModal() {
  modalOverlayEl.classList.remove('active');
  modalIframeEl.src = 'about:blank';
  document.body.style.overflow = '';
}

// Bind event listeners
function bindEvents() {
  // Search
  searchInputEl.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    renderGrid();
  });

  // Filter Pills
  filterPillsEl.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPillsEl.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentFilter = pill.getAttribute('data-filter');
      renderGrid();
    });
  });

  // Modal Close
  modalCloseBtn.addEventListener('click', closeModal);
  modalOverlayEl.addEventListener('click', (e) => {
    if (e.target === modalOverlayEl) closeModal();
  });

  // Toggle Aspect Ratio in Preview
  frameAspectBtn.addEventListener('click', () => {
    currentFormat = currentFormat === '9:16' ? '16:9' : '9:16';
    updateModalFrame();
  });

  // Open in new tab
  openNewTabBtn.addEventListener('click', () => {
    if (currentActiveUrl) {
      window.open(currentActiveUrl, '_blank');
    }
  });

  // Keyboard shortcut (Escape to close)
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalOverlayEl.classList.contains('active')) {
      closeModal();
    }
  });
}

// Run on page load
document.addEventListener('DOMContentLoaded', init);
