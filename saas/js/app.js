/**
 * BENAQAAB OS — Master Application Logic & Reactive Store
 * Manages Tab Routing, Video Theater, Topic Intelligence, Thumbnails, and LocalStorage.
 */

class BenaqaabOS {
  constructor() {
    this.storageKey = 'benaqaab_os_state_v1';
    this.state = this.loadState();
    this.currentTab = 'dashboard';
    this.searchQuery = '';
    this.activeFilter = 'all';
    this.selectedVideo = null;
    this.selectedTopic = null;

    this.init();
  }

  loadState() {
    const saved = localStorage.getItem(this.storageKey);
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        console.error('Failed to parse saved state, using default database', e);
      }
    }
    return JSON.parse(JSON.stringify(window.BENAQAAB_DATABASE));
  }

  saveState() {
    localStorage.setItem(this.storageKey, JSON.stringify(this.state));
  }

  init() {
    this.bindEvents();
    this.render();
  }

  bindEvents() {
    // Navigation items
    document.querySelectorAll('.nav-item').forEach(item => {
      item.addEventListener('click', (e) => {
        const tab = e.currentTarget.getAttribute('data-tab');
        this.switchTab(tab);
      });
    });

    // Global Search
    const searchInput = document.getElementById('globalSearch');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.searchQuery = e.target.value.toLowerCase().trim();
        this.renderCurrentView();
      });
    }

    // Modal Close buttons
    document.querySelectorAll('.modal-close, .modal-backdrop').forEach(el => {
      el.addEventListener('click', (e) => {
        if (e.target === el) {
          this.closeModals();
        }
      });
    });

    // New Topic Form Submit
    const newTopicForm = document.getElementById('newTopicForm');
    if (newTopicForm) {
      newTopicForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.handleCreateTopic(e.target);
      });
    }
  }

  switchTab(tabName) {
    this.currentTab = tabName;
    document.querySelectorAll('.nav-item').forEach(el => {
      if (el.getAttribute('data-tab') === tabName) el.classList.add('active');
      else el.classList.remove('active');
    });

    document.querySelectorAll('.view-container').forEach(el => {
      if (el.id === `view-${tabName}`) el.classList.add('active');
      else el.classList.remove('active');
    });

    this.renderCurrentView();
  }

  showToast(message, type = 'success') {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<span>${type === 'success' ? '⚡' : 'ℹ️'}</span> <span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      setTimeout(() => toast.remove(), 200);
    }, 3200);
  }

  render() {
    this.updateCounts();
    this.renderDashboard();
    this.renderProductions();
    this.renderTopics();
    this.renderVault();
    this.renderThumbnails();
    this.renderAuditor();
  }

  renderCurrentView() {
    if (this.currentTab === 'dashboard') this.renderDashboard();
    else if (this.currentTab === 'productions') this.renderProductions();
    else if (this.currentTab === 'topics') this.renderTopics();
    else if (this.currentTab === 'vault') this.renderVault();
    else if (this.currentTab === 'thumbnails') this.renderThumbnails();
    else if (this.currentTab === 'auditor') this.renderAuditor();
  }

  updateCounts() {
    const prodCount = this.state.productions.length;
    const topicCount = this.state.topics.length;
    const videoCount = this.state.productions.filter(p => p.videoFile).length;

    const elProd = document.getElementById('countProductions');
    if (elProd) elProd.innerText = prodCount;
    const elTopic = document.getElementById('countTopics');
    if (elTopic) elTopic.innerText = topicCount;
    const elVault = document.getElementById('countVault');
    if (elVault) elVault.innerText = videoCount;
  }

  // --- TAB 1: DASHBOARD ---
  renderDashboard() {
    const totalProd = this.state.productions.length;
    const vettedTopics = this.state.topics.length;
    const deliveredCount = this.state.productions.filter(p => p.status === 'Delivered').length;

    const elTotal = document.getElementById('dashTotalProd');
    if (elTotal) elTotal.innerText = totalProd;
    const elVetted = document.getElementById('dashVettedTopics');
    if (elVetted) elVetted.innerText = vettedTopics;
    const elDelivered = document.getElementById('dashDelivered');
    if (elDelivered) elDelivered.innerText = deliveredCount;

    // Render Recent Productions Table / List
    const list = document.getElementById('dashRecentList');
    if (list) {
      list.innerHTML = this.state.productions.slice(0, 5).map(p => `
        <div class="prod-card" style="margin-bottom: 12px; flex-direction: row; align-items: center; padding: 14px 18px;">
          <div style="font-family: var(--font-mono); font-weight: 800; color: var(--gold); width: 65px;">${p.serial}</div>
          <div style="flex: 1; padding: 0 16px;">
            <div style="font-weight: 800; color: #fff; font-size: 15px;">${p.title}</div>
            <div style="font-size: 12px; color: var(--text-muted);">${p.format} • ${p.duration} • ${p.category}</div>
          </div>
          <div class="status-tag status-delivered">${p.status}</div>
          <button class="btn btn-secondary" style="margin-left: 14px; padding: 6px 12px;" onclick="window.os.openVideoModal('${p.id}')">
            ▶ Play
          </button>
        </div>
      `).join('');
    }
  }

  // --- TAB 2: PRODUCTIONS ---
  renderProductions() {
    const grid = document.getElementById('productionsGrid');
    if (!grid) return;

    let items = this.state.productions;

    // Apply Filter
    if (this.activeFilter === 'shorts') items = items.filter(p => p.format.toLowerCase().includes('short'));
    else if (this.activeFilter === 'docu') items = items.filter(p => p.format.toLowerCase().includes('docu') || p.format.toLowerCase().includes('film'));
    else if (this.activeFilter === 'delivered') items = items.filter(p => p.status === 'Delivered');

    // Apply Search
    if (this.searchQuery) {
      items = items.filter(p => 
        p.title.toLowerCase().includes(this.searchQuery) ||
        p.serial.toLowerCase().includes(this.searchQuery) ||
        p.category.toLowerCase().includes(this.searchQuery)
      );
    }

    grid.innerHTML = items.map(p => {
      const thumb = p.thumbnailCuriosity || p.thumbnailClean || '../brand/ref_investigative_1.png';
      return `
        <div class="prod-card">
          <div class="prod-thumb-wrap">
            <img src="${thumb}" alt="${p.title}" class="prod-thumb-img" onerror="this.src='../brand/ref_investigative_1.png'">
            <div class="format-badge">${p.format}</div>
            <div class="duration-tag">${p.duration}</div>
          </div>
          <div class="prod-body">
            <div class="prod-serial">${p.serial} • ${p.category}</div>
            <h3 class="prod-title">${p.title}</h3>
            <p class="prod-desc">${p.description}</p>
            <div class="prod-footer">
              <span class="status-tag status-delivered">${p.status}</span>
              <div style="display: flex; gap: 8px;">
                ${p.videoFile ? `<button class="btn btn-primary" style="padding: 6px 12px; font-size: 11px;" onclick="window.os.openVideoModal('${p.id}')">▶ Watch MP4</button>` : ''}
                ${p.htmlComp ? `<a href="${p.htmlComp}" target="_blank" class="btn btn-secondary" style="padding: 6px 10px; font-size: 11px; text-decoration: none;">🌐 HTML Preview</a>` : ''}
              </div>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  setProductionFilter(filter, el) {
    this.activeFilter = filter;
    document.querySelectorAll('#view-productions .filter-pill').forEach(p => p.classList.remove('active'));
    if (el) el.classList.add('active');
    this.renderProductions();
  }

  // --- TAB 3: TOPICS ---
  renderTopics() {
    const grid = document.getElementById('topicsGrid');
    if (!grid) return;

    let items = this.state.topics;
    if (this.searchQuery) {
      items = items.filter(t => 
        t.title.toLowerCase().includes(this.searchQuery) ||
        t.category.toLowerCase().includes(this.searchQuery) ||
        t.hook.toLowerCase().includes(this.searchQuery)
      );
    }

    grid.innerHTML = items.map(t => `
      <div class="bento-card col-6" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <span class="radar-badge" style="background: rgba(56, 189, 248, 0.15); border-color: rgba(56, 189, 248, 0.3); color: var(--sky);">
              ${t.priority} • ${t.urgencyBadge}
            </span>
            <span style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted); font-weight: 700;">${t.certainty}</span>
          </div>
          <h2 style="font-size: 20px; margin-bottom: 10px; color: #fff;">${t.title}</h2>
          <div style="padding: 10px 14px; background: rgba(0, 0, 0, 0.4); border-left: 3px solid var(--gold); border-radius: 4px; margin-bottom: 14px;">
            <div style="font-family: var(--font-mono); font-size: 10px; font-weight: 800; color: var(--gold); margin-bottom: 4px;">FIRST-SECOND RETENTION HOOK:</div>
            <div style="font-style: italic; color: #e2e8f0; font-size: 13px;">"${t.hook}"</div>
          </div>
          <div style="font-size: 13px; color: var(--text-secondary); margin-bottom: 14px; line-height: 1.5;">
            <strong>Investigation Angle:</strong> ${t.angle}
          </div>
          <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted); margin-bottom: 14px;">
            <div style="font-weight: 700; color: #fff; margin-bottom: 4px;">Verified Ledger:</div>
            ${t.verifiedData.map(d => `• ${d}`).join('<br>')}
          </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-subtle); padding-top: 14px; margin-top: 10px;">
          <span class="status-tag status-ideation">${t.status}</span>
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-secondary" onclick="window.os.advanceTopicStatus('${t.id}')">Advance State ➔</button>
          </div>
        </div>
      </div>
    `).join('');
  }

  advanceTopicStatus(topicId) {
    const t = this.state.topics.find(x => x.id === topicId);
    if (!t) return;
    if (t.status === 'Ideation') t.status = 'Research Completed';
    else if (t.status === 'Research Completed') t.status = 'Ready to Build';
    else if (t.status === 'Ready to Build') t.status = 'In Scripting';
    else if (t.status === 'In Scripting') t.status = 'Ready for Preview';
    else t.status = 'Ready to Build';
    this.saveState();
    this.renderTopics();
    this.showToast(`Updated "${t.title}" status to ${t.status}`);
  }

  handleCreateTopic(form) {
    const title = form.topicTitle.value.trim();
    const category = form.topicCategory.value.trim();
    const hook = form.topicHook.value.trim();
    const angle = form.topicAngle.value.trim();
    const dataLedger = form.topicData.value.trim();

    if (!title || !hook) {
      alert('Please provide a title and hook.');
      return;
    }

    const newTopic = {
      id: `TOPIC-${Date.now()}`,
      title,
      category: category || 'General Explainer',
      priority: 'HIGH PRIORITY',
      urgencyBadge: 'User Created',
      certainty: 'Confirmed / Pending Audit',
      hook,
      angle: angle || 'Mechanism investigation.',
      verifiedData: dataLedger.split('\n').filter(Boolean),
      sources: ['Custom Research Ledger'],
      formatTarget: 'Short (9:16) or Docu (16:9)',
      status: 'Ready to Build'
    };

    this.state.topics.unshift(newTopic);
    this.saveState();
    this.render();
    this.closeModals();
    form.reset();
    this.showToast(`New topic "${title}" successfully registered in master ledger!`);
  }

  // --- TAB 4: VIDEO VAULT ---
  renderVault() {
    const grid = document.getElementById('vaultGrid');
    if (!grid) return;

    const vids = this.state.productions.filter(p => p.videoFile);

    grid.innerHTML = vids.map(v => `
      <div class="prod-card" style="background: rgba(10, 14, 22, 0.75);">
        <div class="prod-thumb-wrap" style="cursor: pointer;" onclick="window.os.openVideoModal('${v.id}')">
          <img src="${v.thumbnailCuriosity || v.thumbnailClean || '../brand/ref_investigative_1.png'}" class="prod-thumb-img">
          <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center;">
            <div style="width: 54px; height: 54px; border-radius: 50%; background: rgba(251, 191, 36, 0.9); display: flex; align-items: center; justify-content: center; font-size: 20px; color: #000; box-shadow: 0 0 25px var(--gold-glow);">
              ▶
            </div>
          </div>
          <div class="duration-tag">${v.duration}</div>
        </div>
        <div class="prod-body">
          <div class="prod-serial">${v.serial} • LUFS: ${v.lufs} dB</div>
          <h3 class="prod-title">${v.title}</h3>
          <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted); margin-bottom: 12px;">
            Target: ${v.format} • Score: ${v.qaScore}%
          </div>
          <div class="prod-footer">
            <a href="${v.videoFile}" download class="btn btn-secondary" style="text-decoration: none; font-size: 12px;">
              ⬇ Download MP4
            </a>
            <button class="btn btn-primary" onclick="window.os.openVideoModal('${v.id}')">
              Cinema Player
            </button>
          </div>
        </div>
      </div>
    `).join('');
  }

  // --- TAB 5: THUMBNAILS & CTR LAB ---
  renderThumbnails() {
    const list = document.getElementById('thumbSelectionList');
    if (!list) return;

    const gold = this.state.productions.find(p => p.id === 'SH-08');
    if (!gold) return;

    // Set simulator images
    const simImg = document.getElementById('simShortsImg');
    if (simImg) simImg.src = gold.thumbnailCuriosity;
    const deskImg = document.getElementById('simDeskImg');
    if (deskImg) deskImg.src = gold.thumbnailLandscape;
  }

  setSimulatorImage(src, isVertical = true) {
    if (isVertical) {
      const el = document.getElementById('simShortsImg');
      if (el) el.src = src;
    } else {
      const el = document.getElementById('simDeskImg');
      if (el) el.src = src;
    }
  }

  // --- TAB 6: FORENSIC QA AUDITOR ---
  renderAuditor() {
    const tableBody = document.getElementById('qaTableBody');
    if (!tableBody) return;

    tableBody.innerHTML = this.state.qaMatrix.map(q => `
      <tr>
        <td style="font-family: var(--font-mono); font-weight: 800; color: var(--gold);">${q.id}</td>
        <td>
          <div style="font-weight: 800; color: #fff;">${q.title}</div>
          <div style="font-size: 11px; color: var(--text-muted);">${q.check}</div>
        </td>
        <td style="font-family: var(--font-mono); font-size: 12px; color: var(--sky);">${q.standard}</td>
        <td>
          <span class="check-pill">✓ PASS</span>
        </td>
      </tr>
    `).join('');
  }

  // Modal Controls
  openVideoModal(prodId) {
    const p = this.state.productions.find(x => x.id === prodId);
    if (!p || !p.videoFile) {
      alert('This production does not have a rendered MP4 file attached yet.');
      return;
    }

    const modal = document.getElementById('videoCinemaModal');
    const player = document.getElementById('cinemaVideoPlayer');
    const title = document.getElementById('cinemaModalTitle');
    const meta = document.getElementById('cinemaModalMeta');

    title.innerText = `${p.serial}: ${p.title}`;
    meta.innerHTML = `
      <div><strong>Format:</strong> ${p.format}</div>
      <div><strong>Duration:</strong> ${p.duration}</div>
      <div><strong>Audio Loudness:</strong> ${p.lufs} LUFS</div>
      <div><strong>Category:</strong> ${p.category}</div>
      <div style="margin-top: 10px;"><strong>Hook:</strong> "${p.hook}"</div>
      <div style="margin-top: 6px;"><strong>Sources:</strong> ${p.sources.join(', ')}</div>
    `;

    player.src = p.videoFile;
    if (p.format.toLowerCase().includes('short')) {
      player.style.aspectRatio = '9/16';
      player.style.width = '320px';
    } else {
      player.style.aspectRatio = '16/9';
      player.style.width = '100%';
    }

    modal.classList.add('open');
    player.play().catch(e => console.log('Autoplay handled', e));
  }

  closeModals() {
    document.querySelectorAll('.modal-backdrop').forEach(el => el.classList.remove('open'));
    const player = document.getElementById('cinemaVideoPlayer');
    if (player) {
      player.pause();
      player.src = '';
    }
  }

  openNewTopicModal() {
    const modal = document.getElementById('newTopicModal');
    if (modal) modal.classList.add('open');
  }

  exportData() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.state, null, 2));
    const dlAnchor = document.createElement('a');
    dlAnchor.setAttribute("href", dataStr);
    dlAnchor.setAttribute("download", `benaqaab_os_backup_${Date.now()}.json`);
    document.body.appendChild(dlAnchor);
    dlAnchor.click();
    dlAnchor.remove();
    this.showToast('Full channel database exported successfully!');
  }

  resetData() {
    if (confirm('Reset channel database to default repository state?')) {
      localStorage.removeItem(this.storageKey);
      this.state = JSON.parse(JSON.stringify(window.BENAQAAB_DATABASE));
      this.render();
      this.showToast('Database reset to defaults.');
    }
  }
}

// Instantiate on DOM load
document.addEventListener('DOMContentLoaded', () => {
  window.os = new BenaqaabOS();
});
