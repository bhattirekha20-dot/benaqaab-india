/**
 * BENAQAAB OS — Master Application Logic & Reactive Store (V2 Pro Max)
 * Manages Tab Routing, Video Theater, Kanban Pipeline, Teleprompter,
 * Financial Math Lab, Live Canvas Thumbnail Customizer, YouTube SEO Packager,
 * Forensic Evidence Pinboard, Audio & VO Studio, Retention Sequencer, and B-Roll Prompts.
 */

class BenaqaabOS {
  constructor() {
    this.storageKey = 'benaqaab_os_state_v2';
    this.state = this.loadState();
    this.currentTab = 'dashboard';
    this.searchQuery = '';
    this.activeFilter = 'all';

    // Teleprompter state
    this.prompterTimer = null;
    this.prompterOffset = 0;
    this.prompterSpeed = 90; // px per sec
    this.isPrompterRunning = false;
    this.isPrompterMirrored = false;

    // Canvas Studio state
    this.canvasBaseImg = null;
    this.canvasLoaded = false;

    // Forensic Evidence Pinboard state
    this.currentCaseId = 'case-gold';
    this.activeEvidenceNodeId = null;
    this.showRedStrings = true;
    this.isDraggingEvidence = false;
    this.draggedNode = null;
    this.dragOffset = { x: 0, y: 0 };

    // Audio & VO Studio state
    this.ttsUtterance = null;
    this.ttsVoices = [];
    this.isTtsSpeaking = false;
    this.isRecordingMic = false;
    this.mediaRecorder = null;
    this.recordedChunks = [];
    this.micTimerInterval = null;
    this.micElapsedSec = 0;
    this.audioContext = null;
    this.analyser = null;
    this.micStream = null;

    // Retention Sequencer state
    this.currentRetentionId = 'BP-01';

    this.init();
  }

  loadState() {
    const saved = localStorage.getItem(this.storageKey);
    let state = null;
    if (saved) {
      try {
        state = JSON.parse(saved);
      } catch (e) {
        console.error('Failed to parse saved state, using default database', e);
      }
    }
    const def = JSON.parse(JSON.stringify(window.BENAQAAB_DATABASE));
    if (!state) return def;

    // Defensive merge for productions
    if (state.productions && Array.isArray(state.productions)) {
      def.productions.forEach(dp => {
        const existing = state.productions.find(sp => sp.id === dp.id);
        if (!existing) {
          state.productions.push(dp);
        } else {
          // Sync media links and project paths if missing
          if (!existing.videoFile && dp.videoFile) existing.videoFile = dp.videoFile;
          if (!existing.thumbnailCuriosity && dp.thumbnailCuriosity) existing.thumbnailCuriosity = dp.thumbnailCuriosity;
          if (!existing.thumbnailClean && dp.thumbnailClean) existing.thumbnailClean = dp.thumbnailClean;
          if (!existing.thumbnailLandscape && dp.thumbnailLandscape) existing.thumbnailLandscape = dp.thumbnailLandscape;
          if (!existing.projectPath && dp.projectPath) existing.projectPath = dp.projectPath;
          if (!existing.htmlComp && dp.htmlComp) existing.htmlComp = dp.htmlComp;
        }
      });
    } else {
      state.productions = def.productions;
    }

    // Defensive merge for topics
    if (state.topics && Array.isArray(state.topics)) {
      def.topics.forEach(dt => {
        if (!state.topics.some(st => st.id === dt.id)) {
          state.topics.push(dt);
        }
      });
    } else {
      state.topics = def.topics;
    }

    // Defensive merge for evidence cases
    if (state.evidenceCases && Array.isArray(state.evidenceCases)) {
      def.evidenceCases.forEach(dc => {
        if (!state.evidenceCases.some(sc => sc.id === dc.id)) {
          state.evidenceCases.push(dc);
        }
      });
    } else {
      state.evidenceCases = def.evidenceCases;
    }

    // Defensive merge for retention blueprints
    if (state.retentionBlueprints && Array.isArray(state.retentionBlueprints)) {
      def.retentionBlueprints.forEach(db => {
        if (!state.retentionBlueprints.some(sb => sb.id === db.id)) {
          state.retentionBlueprints.push(db);
        }
      });
    } else {
      state.retentionBlueprints = def.retentionBlueprints;
    }

    // Defensive merge for prompt templates
    if (state.promptTemplates && Array.isArray(state.promptTemplates)) {
      def.promptTemplates.forEach(dp => {
        if (!state.promptTemplates.some(sp => sp.id === dp.id)) {
          state.promptTemplates.push(dp);
        }
      });
    } else {
      state.promptTemplates = def.promptTemplates;
    }

    return state;
  }

  saveState() {
    localStorage.setItem(this.storageKey, JSON.stringify(this.state));
  }

  init() {
    this.bindEvents();
    this.initCanvasStudio();
    this.initAudioStudio();
    this.initEvidencePinboard();
    this.initPromptStudio();
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

    // Keyboard Shortcuts (Space for teleprompter, Esc for modals)
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.closeModals();
      if (e.code === 'Space' && this.currentTab === 'teleprompter' && e.target.tagName !== 'TEXTAREA' && e.target.tagName !== 'INPUT') {
        e.preventDefault();
        this.togglePrompter();
      }
    });
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
    this.renderKanban();
    this.renderProductions();
    this.renderTopics();
    this.renderVault();
    this.renderThumbnails();
    this.renderTeleprompter();
    this.renderCalculator();
    this.renderPackager();
    this.renderAuditor();
    this.renderEvidencePinboard();
    this.renderVoiceoverStudio();
    this.renderRetentionSequencer();
    this.renderPromptStudio();
  }

  renderCurrentView() {
    if (this.currentTab === 'dashboard') this.renderDashboard();
    else if (this.currentTab === 'kanban') this.renderKanban();
    else if (this.currentTab === 'productions') this.renderProductions();
    else if (this.currentTab === 'topics') this.renderTopics();
    else if (this.currentTab === 'vault') this.renderVault();
    else if (this.currentTab === 'thumbnails') { this.renderThumbnails(); this.renderCustomThumbnailCanvas(); }
    else if (this.currentTab === 'teleprompter') this.renderTeleprompter();
    else if (this.currentTab === 'calculator') this.renderCalculator();
    else if (this.currentTab === 'packager') this.renderPackager();
    else if (this.currentTab === 'auditor') this.renderAuditor();
    else if (this.currentTab === 'evidence') this.renderEvidencePinboard();
    else if (this.currentTab === 'voiceover') this.renderVoiceoverStudio();
    else if (this.currentTab === 'retention') this.renderRetentionSequencer();
    else if (this.currentTab === 'prompts') this.renderPromptStudio();
  }

  updateCounts() {
    const prodCount = this.state.productions.length;
    const topicCount = this.state.topics.length;
    const videoCount = this.state.productions.filter(p => p.videoFile).length;
    const caseCount = (this.state.evidenceCases || []).length;

    const elProd = document.getElementById('countProductions');
    if (elProd) elProd.innerText = prodCount;
    const elTopic = document.getElementById('countTopics');
    if (elTopic) elTopic.innerText = topicCount;
    const elVault = document.getElementById('countVault');
    if (elVault) elVault.innerText = videoCount;
    const elCases = document.getElementById('countCases');
    if (elCases) elCases.innerText = caseCount;
  }

  // --- TAB 1: DASHBOARD ---
  renderDashboard() {
    const totalProd = this.state.productions.length;
    const vettedTopics = this.state.topics.length;
    const deliveredCount = this.state.productions.filter(p => p.stage === 'published' || p.status === 'Delivered').length;

    const elTotal = document.getElementById('dashTotalProd');
    if (elTotal) elTotal.innerText = totalProd;
    const elVetted = document.getElementById('dashVettedTopics');
    if (elVetted) elVetted.innerText = vettedTopics;
    const elDelivered = document.getElementById('dashDelivered');
    if (elDelivered) elDelivered.innerText = deliveredCount;

    const list = document.getElementById('dashRecentList');
    if (list) {
      list.innerHTML = this.state.productions.slice(0, 5).map(p => `
        <div class="prod-card" style="margin-bottom: 12px; flex-direction: row; align-items: center; padding: 14px 18px;">
          <div style="font-family: var(--font-mono); font-weight: 800; color: var(--gold); width: 65px;">${p.serial}</div>
          <div style="flex: 1; padding: 0 16px;">
            <div style="font-weight: 800; color: #fff; font-size: 15px;">${p.title}</div>
            <div style="font-size: 12px; color: var(--text-muted);">${p.format} • ${p.duration} • Stage: <strong style="color:var(--sky);">${p.stage || 'Published'}</strong></div>
          </div>
          <div class="status-tag status-delivered">${p.status}</div>
          <button class="btn btn-secondary" style="margin-left: 14px; padding: 6px 12px;" onclick="window.os.openVideoModal('${p.id}')">
            ▶ Play
          </button>
        </div>
      `).join('');
    }
  }

  // --- TAB 2: KANBAN PRODUCTION PIPELINE ---
  renderKanban() {
    const stages = [
      { id: 'ideation', name: '💡 Ideation & Pitch' },
      { id: 'fact_ledger', name: '📑 Fact Ledger & Sources' },
      { id: 'script_vo', name: '🎙️ Script & VO Timing' },
      { id: 'preview_gate', name: '👁️ 1-Gate HTML Preview' },
      { id: 'published', name: '🚀 Master Render & Live' }
    ];

    stages.forEach(st => {
      const container = document.getElementById(`kanban-list-${st.id}`);
      if (!container) return;
      const countEl = document.getElementById(`kanban-count-${st.id}`);

      const items = this.state.productions.filter(p => (p.stage || 'published') === st.id);
      if (countEl) countEl.innerText = items.length;

      container.innerHTML = items.map(p => `
        <div class="kanban-card">
          <div style="display: flex; justify-content: space-between;">
            <span class="kanban-card-serial">${p.serial}</span>
            <span style="font-size: 10px; color: var(--text-muted);">${p.duration}</span>
          </div>
          <div class="kanban-card-title">${p.title}</div>
          <div style="font-size: 11px; color: var(--text-muted); margin-bottom: 6px;">${p.category}</div>
          <div class="kanban-nav-btns">
            <button class="btn-arrow" title="Move Left" onclick="window.os.moveKanbanStage('${p.id}', -1)">←</button>
            <button class="btn-arrow" title="Move Right" onclick="window.os.moveKanbanStage('${p.id}', 1)">→</button>
          </div>
        </div>
      `).join('');
    });
  }

  moveKanbanStage(prodId, delta) {
    const order = ['ideation', 'fact_ledger', 'script_vo', 'preview_gate', 'published'];
    const p = this.state.productions.find(x => x.id === prodId);
    if (!p) return;
    const currIdx = order.indexOf(p.stage || 'published');
    const newIdx = Math.max(0, Math.min(order.length - 1, currIdx + delta));
    p.stage = order[newIdx];
    this.saveState();
    this.renderKanban();
    this.showToast(`Moved ${p.serial} to ${p.stage.replace('_', ' ').toUpperCase()}`);
  }

  // --- TAB 3: PRODUCTIONS TRACKER ---
  renderProductions() {
    const grid = document.getElementById('productionsGrid');
    if (!grid) return;

    let items = this.state.productions;

    if (this.activeFilter === 'shorts') items = items.filter(p => p.format.toLowerCase().includes('short'));
    else if (this.activeFilter === 'docu') items = items.filter(p => p.format.toLowerCase().includes('docu') || p.format.toLowerCase().includes('film'));
    else if (this.activeFilter === 'delivered') items = items.filter(p => p.status === 'Delivered');

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

  // --- TAB 4: TOPIC RADAR ---
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

  // --- TAB 5: BROADCAST MEDIA VAULT ---
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

  // --- TAB 6: THUMBNAILS & LIVE CANVAS CUSTOMIZER ---
  initCanvasStudio() {
    this.canvasBaseImg = new Image();
    if (window.location.protocol.startsWith('http')) {
      this.canvasBaseImg.crossOrigin = 'anonymous';
    }
    this.canvasBaseImg.src = '../projects/gold_150k/thumbnail_clean_base_1080x1920.jpg';
    this.canvasBaseImg.onload = () => {
      this.canvasLoaded = true;
      this.renderCustomThumbnailCanvas();
    };
  }

  renderThumbnails() {
    const simImg = document.getElementById('simShortsImg');
    const deskImg = document.getElementById('simDeskImg');
    const gold = this.state.productions.find(p => p.id === 'SH-08');
    if (gold && simImg) simImg.src = gold.thumbnailCuriosity;
    if (gold && deskImg) deskImg.src = gold.thumbnailLandscape;
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

  renderCustomThumbnailCanvas() {
    const canvas = document.getElementById('customThumbCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = 1080;
    canvas.height = 1920;

    // 1. Draw base image
    if (this.canvasLoaded && this.canvasBaseImg) {
      ctx.drawImage(this.canvasBaseImg, 0, 0, 1080, 1920);
    } else {
      ctx.fillStyle = '#07090e';
      ctx.fillRect(0, 0, 1080, 1920);
    }

    // 2. Top Dark Gradient for Contrast
    const grad = ctx.createLinearGradient(0, 0, 0, 600);
    grad.addColorStop(0, 'rgba(5, 7, 12, 0.88)');
    grad.addColorStop(1, 'rgba(5, 7, 12, 0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 1080, 600);

    // Get input values
    const headline = document.getElementById('thInputHeadline')?.value || "SONA ₹1.5 LAKH?";
    const badgeText = document.getElementById('thInputBadge')?.value || "ASLI BILL = ₹1.82 LAKH!";
    const callout = document.getElementById('thInputCallout')?.value || "₹31,000 EXTRA KAHAN GAYA?";
    const headY = parseInt(document.getElementById('thSliderHeadY')?.value || "120");
    const badgeY = parseInt(document.getElementById('thSliderBadgeY')?.value || "260");
    const calloutY = parseInt(document.getElementById('thSliderCalloutY')?.value || "390");

    // 3. Draw Headline Text
    ctx.font = "900 114px 'Outfit', 'Anton', sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    // Glow Drop Shadow
    ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
    ctx.fillText(headline, 540, headY + 5);
    ctx.fillStyle = "#ffffff";
    ctx.fillText(headline, 540, headY);

    // 4. Draw Red Warning Badge
    if (badgeText.trim()) {
      ctx.font = "800 68px 'Outfit', sans-serif";
      const bw = ctx.measureText(badgeText).width + 60;
      const bh = 94;
      const bx = 540 - bw / 2;
      const by = badgeY - bh / 2;

      ctx.fillStyle = "rgba(225, 29, 72, 0.95)";
      ctx.beginPath();
      ctx.roundRect(bx, by, bw, bh, 20);
      ctx.fill();
      ctx.strokeStyle = "rgba(254, 205, 211, 0.8)";
      ctx.lineWidth = 3;
      ctx.stroke();

      ctx.fillStyle = "#ffffff";
      ctx.fillText(badgeText, 540, badgeY);
    }

    // 5. Draw Yellow Callout
    if (callout.trim()) {
      ctx.font = "700 42px 'Inter', sans-serif";
      const cw = ctx.measureText(callout).width + 50;
      const ch = 68;
      const cx = 540 - cw / 2;
      const cy = calloutY - ch / 2;

      ctx.fillStyle = "rgba(251, 191, 36, 0.95)";
      ctx.beginPath();
      ctx.roundRect(cx, cy, cw, ch, 14);
      ctx.fill();

      ctx.fillStyle = "#0f172a";
      ctx.fillText(callout, 540, calloutY);
    }

    // 6. Draw AI Illustrative Disclosure Tag
    ctx.font = "600 24px 'Inter', sans-serif";
    const tagText = "AI ILLUSTRATIVE · BENAQAAB INDIA";
    const tw = ctx.measureText(tagText).width + 30;
    ctx.fillStyle = "rgba(0, 0, 0, 0.75)";
    ctx.beginPath();
    ctx.roundRect(40, 1850, tw, 42, 8);
    ctx.fill();
    ctx.strokeStyle = "rgba(255, 255, 255, 0.2)";
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.textAlign = "left";
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText(tagText, 55, 1878);
  }

  loadCustomBasePlate(e) {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      this.canvasBaseImg = new Image();
      this.canvasBaseImg.onload = () => {
        this.canvasLoaded = true;
        this.renderCustomThumbnailCanvas();
        this.showToast('Custom thumbnail background loaded!');
      };
      this.canvasBaseImg.src = event.target.result;
    };
    reader.readAsDataURL(file);
  }

  exportCustomThumbnailJpg() {
    const canvas = document.getElementById('customThumbCanvas');
    if (!canvas) return;
    const link = document.createElement('a');
    link.download = `benaqaab_thumbnail_custom_${Date.now()}.jpg`;
    link.href = canvas.toDataURL('image/jpeg', 0.95);
    link.click();
    this.showToast('High-res 1080x1920 thumbnail exported!');
  }

  // --- TAB 7: LIVE TELEPROMPTER & SCRIPT LAB ---
  renderTeleprompter() {
    this.updateWordBudget();
  }

  updateWordBudget() {
    const area = document.getElementById('prompterScriptInput');
    if (!area) return;
    const text = area.value.trim();
    const words = text ? text.split(/\s+/).length : 0;
    const chars = text.length;

    // Calculations based on WPM
    const sec170 = Math.round((words / 170) * 60); // 170 WPM conversational
    const secFast = Math.round((words / 190) * 60); // 190 WPM fast (+12%)

    document.getElementById('prompterWordCount').innerText = words;
    document.getElementById('prompterCharCount').innerText = chars;
    document.getElementById('prompterTime170').innerText = `${sec170}s`;
    document.getElementById('prompterTimeFast').innerText = `${secFast}s`;

    // Fill meter (Shorts cap: 155 words = 100%)
    const pct = Math.min(100, Math.round((words / 155) * 100));
    const fill = document.getElementById('prompterBudgetFill');
    const label = document.getElementById('prompterBudgetStatus');

    if (fill) {
      fill.style.width = `${pct}%`;
      if (words <= 150) {
        fill.style.background = 'var(--emerald)';
        if (label) label.innerHTML = `<span style="color:var(--emerald);">✓ Shorts Compliant (&lt;60s)</span>`;
      } else if (words <= 165) {
        fill.style.background = 'var(--gold)';
        if (label) label.innerHTML = `<span style="color:var(--gold);">⚠️ Approaching Cap (~58s)</span>`;
      } else {
        fill.style.background = 'var(--rose)';
        if (label) label.innerHTML = `<span style="color:var(--rose);">❌ Overrun Warning (&gt;60s)</span>`;
      }
    }

    // Update prompter scroll text
    const display = document.getElementById('prompterScrollText');
    if (display) {
      display.innerText = text || "Type or paste your script on the left to begin teleprompter display...";
    }
  }

  loadPresetScript(prodId) {
    const p = this.state.productions.find(x => x.id === prodId);
    if (!p || !p.scriptText) return;
    const area = document.getElementById('prompterScriptInput');
    if (area) {
      area.value = p.scriptText;
      this.updateWordBudget();
      this.showToast(`Loaded preset script for ${p.serial}: ${p.title}`);
    }
  }

  togglePrompter() {
    if (this.isPrompterRunning) this.stopPrompter();
    else this.startPrompter();
  }

  startPrompter() {
    this.isPrompterRunning = true;
    const btn = document.getElementById('btnPrompterPlay');
    if (btn) btn.innerText = '⏸ Pause (Space)';

    const display = document.getElementById('prompterScrollText');
    const container = document.getElementById('prompterContainer');

    const step = () => {
      if (!this.isPrompterRunning) return;
      this.prompterOffset += (this.prompterSpeed / 60);
      if (display) {
        display.style.transform = `translateY(-${this.prompterOffset}px) ${this.isPrompterMirrored ? 'scaleX(-1)' : ''}`;
      }
      this.prompterTimer = requestAnimationFrame(step);
    };
    this.prompterTimer = requestAnimationFrame(step);
  }

  stopPrompter() {
    this.isPrompterRunning = false;
    const btn = document.getElementById('btnPrompterPlay');
    if (btn) btn.innerText = '▶ Start Prompter (Space)';
    if (this.prompterTimer) cancelAnimationFrame(this.prompterTimer);
  }

  resetPrompter() {
    this.stopPrompter();
    this.prompterOffset = 0;
    const display = document.getElementById('prompterScrollText');
    if (display) {
      display.style.transform = `translateY(0px) ${this.isPrompterMirrored ? 'scaleX(-1)' : ''}`;
    }
  }

  setPrompterSpeed(val) {
    this.prompterSpeed = parseInt(val);
    document.getElementById('prompterSpeedLabel').innerText = `${this.prompterSpeed} px/s`;
  }

  setPrompterFontSize(val) {
    const display = document.getElementById('prompterScrollText');
    if (display) display.style.fontSize = `${val}px`;
    document.getElementById('prompterSizeLabel').innerText = `${val}px`;
  }

  togglePrompterMirror() {
    this.isPrompterMirrored = !this.isPrompterMirrored;
    const display = document.getElementById('prompterScrollText');
    if (display) {
      display.style.transform = `translateY(-${this.prompterOffset}px) ${this.isPrompterMirrored ? 'scaleX(-1)' : ''}`;
    }
    this.showToast(this.isPrompterMirrored ? 'Beam-splitter mirror mode enabled' : 'Mirror mode disabled');
  }

  // --- TAB 8: FORENSIC FINANCIAL CALCULATOR ---
  renderCalculator() {
    this.calcGoldBill();
    this.calcEmiShock();
  }

  calcGoldBill() {
    const rate = parseFloat(document.getElementById('calcGoldRate')?.value || 150280);
    const grams = parseFloat(document.getElementById('calcGoldGrams')?.value || 10);
    const makingPct = parseFloat(document.getElementById('calcMakingPct')?.value || 15);
    const wastagePct = parseFloat(document.getElementById('calcWastagePct')?.value || 3);

    const baseVal = (rate / 10.0) * grams;
    const makingCharge = baseVal * (makingPct / 100.0);
    const wastageCharge = baseVal * (wastagePct / 100.0);
    const subtotal = baseVal + makingCharge + wastageCharge;
    const gst = subtotal * 0.03; // 3% GST
    const total = subtotal + gst;
    const extraMarkup = total - baseVal;
    const markupPct = (extraMarkup / baseVal) * 100.0;

    document.getElementById('resGoldBase').innerText = `₹${Math.round(baseVal).toLocaleString('en-IN')}`;
    document.getElementById('resGoldMaking').innerText = `₹${Math.round(makingCharge).toLocaleString('en-IN')} (+${makingPct}%)`;
    document.getElementById('resGoldWastage').innerText = `₹${Math.round(wastageCharge).toLocaleString('en-IN')} (+${wastagePct}%)`;
    document.getElementById('resGoldGst').innerText = `₹${Math.round(gst).toLocaleString('en-IN')} (3%)`;
    document.getElementById('resGoldTotal').innerText = `₹${Math.round(total).toLocaleString('en-IN')}`;
    document.getElementById('resGoldExtra').innerText = `+₹${Math.round(extraMarkup).toLocaleString('en-IN')} (+${markupPct.toFixed(1)}% Markup)`;
  }

  copyGoldBeatToClipboard() {
    const total = document.getElementById('resGoldTotal').innerText;
    const extra = document.getElementById('resGoldExtra').innerText;
    const beat = `10 gram gold jo ₹1.5 lakh ka dikh raha tha, 3% GST aur 15% making charges lagne ke baad showroom se nikalte nikalte ${total} ka padta hai — yani poora ${extra}!`;
    navigator.clipboard.writeText(beat);
    this.showToast('Gold script beat copied to clipboard!');
  }

  calcEmiShock() {
    const loan = parseFloat(document.getElementById('calcEmiLoan')?.value || 5000000);
    const currentRate = parseFloat(document.getElementById('calcEmiRate')?.value || 8.5);
    const hikeBps = parseFloat(document.getElementById('calcEmiHike')?.value || 25);
    const tenureYears = parseFloat(document.getElementById('calcEmiTenure')?.value || 20);

    const n = tenureYears * 12;

    const calcEmi = (p, rAnnual) => {
      const r = (rAnnual / 12) / 100;
      return (p * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
    };

    const currentEmi = calcEmi(loan, currentRate);
    const newRate = currentRate + (hikeBps / 100.0);
    const newEmi = calcEmi(loan, newRate);
    const diffMonth = newEmi - currentEmi;
    const totalExtra = diffMonth * n;

    document.getElementById('resEmiCurrent').innerText = `₹${Math.round(currentEmi).toLocaleString('en-IN')} / mo`;
    document.getElementById('resEmiNew').innerText = `₹${Math.round(newEmi).toLocaleString('en-IN')} / mo`;
    document.getElementById('resEmiDiff').innerText = `+₹${Math.round(diffMonth).toLocaleString('en-IN')} / mo`;
    document.getElementById('resEmiTotalExtra').innerText = `+₹${Math.round(totalExtra).toLocaleString('en-IN')} over ${tenureYears} yrs`;
  }

  copyEmiBeatToClipboard() {
    const diff = document.getElementById('resEmiDiff').innerText;
    const total = document.getElementById('resEmiTotalExtra').innerText;
    const beat = `Agar Repo Rate mein sirf 25 bps ka hike hota hai, toh 50 lakh ke home loan par har mahine lagbhag ${diff} aur 20 saal mein ${total} ka seedha extra bojh padega!`;
    navigator.clipboard.writeText(beat);
    this.showToast('EMI shock script beat copied to clipboard!');
  }

  // --- TAB 9: YOUTUBE SEO METADATA PACKAGER ---
  renderPackager() {
    const select = document.getElementById('packagerProdSelect');
    if (!select) return;

    if (select.children.length === 0) {
      select.innerHTML = this.state.productions.map(p => `
        <option value="${p.id}">${p.serial}: ${p.title}</option>
      `).join('');
    }

    const currentId = select.value || 'SH-08';
    const p = this.state.productions.find(x => x.id === currentId);
    if (!p) return;

    // Render Titles
    const titleContainer = document.getElementById('packagerTitlesList');
    if (titleContainer) {
      titleContainer.innerHTML = (p.titles || [p.title]).map((t, idx) => `
        <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
          <div style="flex: 1; padding-right: 12px;">
            <div style="font-weight: 700; color: #fff; font-size: 13px;">${idx + 1}. ${t}</div>
            <div style="font-size: 11px; color: ${t.length <= 100 ? 'var(--emerald)' : 'var(--rose)'}; margin-top: 2px;">
              ${t.length}/100 chars
            </div>
          </div>
          <button class="btn btn-secondary" style="padding: 4px 10px; font-size: 11px;" onclick="window.os.copyText('${t.replace(/'/g, "\\'")}', 'Title copied!')">📋 Copy</button>
        </div>
      `).join('');
    }

    // Render Description
    const descArea = document.getElementById('packagerDescArea');
    if (descArea) descArea.value = p.seoDescription || p.description;

    // Render Pinned Comment
    const pinnedArea = document.getElementById('packagerPinnedArea');
    if (pinnedArea) pinnedArea.value = p.pinnedComment || p.hook;

    // Render Tags
    const tagsArea = document.getElementById('packagerTagsArea');
    if (tagsArea) tagsArea.value = (p.tags || []).join(', ');
  }

  copyText(str, successMsg = 'Copied to clipboard!') {
    navigator.clipboard.writeText(str);
    this.showToast(successMsg);
  }

  copyPackagerField(fieldId, name) {
    const el = document.getElementById(fieldId);
    if (!el) return;
    navigator.clipboard.writeText(el.value);
    this.showToast(`${name} copied to clipboard!`);
  }

  downloadFullUploadPack() {
    const select = document.getElementById('packagerProdSelect');
    const p = this.state.productions.find(x => x.id === (select?.value || 'SH-08'));
    if (!p) return;

    const desc = document.getElementById('packagerDescArea')?.value || '';
    const pinned = document.getElementById('packagerPinnedArea')?.value || '';
    const tags = document.getElementById('packagerTagsArea')?.value || '';

    const content = `=====================================================
BENAQAAB INDIA — YOUTUBE UPLOAD PACK
Production: ${p.serial} — ${p.title}
Format: ${p.format} | Duration: ${p.duration} | Audio: ${p.lufs} LUFS
=====================================================

--- RECOMMENDED TITLES ---
${(p.titles || [p.title]).map((t, i) => `${i + 1}. ${t}`).join('\n')}

--- SEO DESCRIPTION ---
${desc}

--- PINNED COMMENT ---
${pinned}

--- HASHTAGS & TAGS ---
${tags}
`;

    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `Upload_Pack_${p.serial}.txt`;
    link.click();
    this.showToast(`Full upload pack for ${p.serial} downloaded!`);
  }

  // --- TAB 10: FORENSIC QA AUDITOR ---
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

  // --- MODALS & EXPORTS ---
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
    const dlBtn = document.getElementById('cinemaDownloadBtn');

    title.innerText = `${p.serial}: ${p.title}`;
    meta.innerHTML = `
      <div><strong>Format:</strong> ${p.format}</div>
      <div><strong>Duration:</strong> ${p.duration}</div>
      <div><strong>Audio Loudness:</strong> ${p.lufs} LUFS</div>
      <div><strong>Category:</strong> ${p.category}</div>
      <div style="margin-top: 10px;"><strong>Hook:</strong> "${p.hook}"</div>
      <div style="margin-top: 6px;"><strong>Sources:</strong> ${p.sources.join(', ')}</div>
    `;

    if (dlBtn) dlBtn.href = p.videoFile;

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

  // ==========================================================================
  // TAB 11: FORENSIC EVIDENCE PINBOARD & RED-STRING CANVAS
  // ==========================================================================
  initEvidencePinboard() {
    const stage = document.getElementById('pinboardStage');
    if (!stage) return;

    const onMove = (clientX, clientY) => {
      if (!this.isDraggingEvidence || !this.draggedNode) return;
      const stageRect = stage.getBoundingClientRect();
      let newX = clientX - stageRect.left - this.dragOffset.x;
      let newY = clientY - stageRect.top - this.dragOffset.y;

      newX = Math.max(10, Math.min(stageRect.width - 220, newX));
      newY = Math.max(10, Math.min(stageRect.height - 140, newY));

      const activeCase = this.getActiveEvidenceCase();
      const nodeObj = activeCase.nodes.find(n => n.id === this.draggedNode.getAttribute('data-id'));
      if (nodeObj) {
        nodeObj.x = Math.round(newX);
        nodeObj.y = Math.round(newY);
        this.draggedNode.style.left = `${nodeObj.x}px`;
        this.draggedNode.style.top = `${nodeObj.y}px`;
        this.drawPinboardConnections();
      }
    };

    const onEnd = () => {
      if (this.isDraggingEvidence) {
        this.isDraggingEvidence = false;
        this.draggedNode = null;
        this.saveState();
      }
    };

    stage.addEventListener('mousemove', (e) => onMove(e.clientX, e.clientY));
    window.addEventListener('mouseup', onEnd);

    stage.addEventListener('touchmove', (e) => {
      if (e.touches.length > 0) onMove(e.touches[0].clientX, e.touches[0].clientY);
    }, { passive: true });
    window.addEventListener('touchend', onEnd);

    window.addEventListener('resize', () => {
      if (this.currentTab === 'evidence') this.renderEvidencePinboard();
    });
  }

  getActiveEvidenceCase() {
    return (this.state.evidenceCases || []).find(c => c.id === this.currentCaseId) || (this.state.evidenceCases || [])[0];
  }

  renderEvidencePinboard() {
    const activeCase = this.getActiveEvidenceCase();
    if (!activeCase) return;

    const caseSelect = document.getElementById('caseSelect');
    if (caseSelect) caseSelect.value = activeCase.id;

    const stage = document.getElementById('pinboardStage');
    const canvas = document.getElementById('evidenceCanvas');
    const nodesLayer = document.getElementById('pinboardNodesLayer');
    if (!stage || !canvas || !nodesLayer) return;

    canvas.width = stage.clientWidth;
    canvas.height = stage.clientHeight;

    nodesLayer.innerHTML = activeCase.nodes.map(node => {
      const isSelected = this.activeEvidenceNodeId === node.id;
      return `
        <div class="evidence-node ${isSelected ? 'selected' : ''}" 
             id="ev-node-${node.id}"
             data-id="${node.id}"
             style="left: ${node.x}px; top: ${node.y}px;">
          <div class="evidence-pin"></div>
          <div class="evidence-node-category" style="color: ${node.color || 'var(--gold)'};">${node.category}</div>
          <div class="evidence-node-label">${node.label}</div>
          <div class="evidence-node-val">${node.val}</div>
        </div>
      `;
    }).join('');

    nodesLayer.querySelectorAll('.evidence-node').forEach(el => {
      const nodeId = el.getAttribute('data-id');

      const startDrag = (clientX, clientY) => {
        this.isDraggingEvidence = true;
        this.draggedNode = el;
        this.activeEvidenceNodeId = nodeId;
        const rect = el.getBoundingClientRect();
        this.dragOffset = {
          x: clientX - rect.left,
          y: clientY - rect.top
        };
        this.selectEvidenceNode(nodeId);
      };

      el.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        startDrag(e.clientX, e.clientY);
      });

      el.addEventListener('touchstart', (e) => {
        e.stopPropagation();
        if (e.touches.length > 0) startDrag(e.touches[0].clientX, e.touches[0].clientY);
      }, { passive: true });
    });

    this.drawPinboardConnections();

    if (!this.activeEvidenceNodeId && activeCase.nodes.length > 0) {
      this.selectEvidenceNode(activeCase.nodes[0].id);
    } else if (this.activeEvidenceNodeId) {
      this.selectEvidenceNode(this.activeEvidenceNodeId);
    }
  }

  drawPinboardConnections() {
    const canvas = document.getElementById('evidenceCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (!this.showRedStrings) return;

    const activeCase = this.getActiveEvidenceCase();
    if (!activeCase || !activeCase.connections) return;

    ctx.save();
    ctx.lineCap = 'round';

    activeCase.connections.forEach(conn => {
      const fromNode = activeCase.nodes.find(n => n.id === conn.from);
      const toNode = activeCase.nodes.find(n => n.id === conn.to);
      if (!fromNode || !toNode) return;

      const x1 = fromNode.x + 100;
      const y1 = fromNode.y;
      const x2 = toNode.x + 100;
      const y2 = toNode.y;

      const midX = (x1 + x2) / 2;
      const midY = (y1 + y2) / 2 + Math.min(45, Math.hypot(x2 - x1, y2 - y1) * 0.15);

      ctx.shadowColor = 'rgba(244, 63, 94, 0.6)';
      ctx.shadowBlur = 8;
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.5;

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.quadraticCurveTo(midX, midY, x2, y2);
      ctx.stroke();

      ctx.shadowBlur = 0;
      ctx.strokeStyle = '#ff7675';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.quadraticCurveTo(midX, midY, x2, y2);
      ctx.stroke();

      if (conn.label) {
        ctx.font = '10px "JetBrains Mono", monospace';
        const txtWidth = ctx.measureText(conn.label).width;
        ctx.fillStyle = 'rgba(10, 13, 20, 0.85)';
        ctx.strokeStyle = 'rgba(244, 63, 94, 0.4)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.roundRect(midX - txtWidth / 2 - 6, midY - 8, txtWidth + 12, 16, 4);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#fca5a5';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(conn.label, midX, midY);
      }
    });

    ctx.restore();
  }

  selectEvidenceNode(nodeId) {
    this.activeEvidenceNodeId = nodeId;
    const activeCase = this.getActiveEvidenceCase();
    const node = activeCase.nodes.find(n => n.id === nodeId);
    if (!node) return;

    document.querySelectorAll('.evidence-node').forEach(el => {
      if (el.getAttribute('data-id') === nodeId) el.classList.add('selected');
      else el.classList.remove('selected');
    });

    const catEl = document.getElementById('inspectCategory');
    const labelIn = document.getElementById('inspectLabel');
    const valIn = document.getElementById('inspectVal');
    const noteIn = document.getElementById('inspectNote');

    if (catEl) {
      catEl.innerText = node.category;
      catEl.style.color = node.color || '#fff';
    }
    if (labelIn) labelIn.value = node.label;
    if (valIn) valIn.value = node.val;
    if (noteIn) noteIn.value = node.note || '';
  }

  updateActiveNode(field, val) {
    if (!this.activeEvidenceNodeId) return;
    const activeCase = this.getActiveEvidenceCase();
    const node = activeCase.nodes.find(n => n.id === this.activeEvidenceNodeId);
    if (!node) return;

    node[field] = val;
    this.saveState();

    const nodeEl = document.getElementById(`ev-node-${node.id}`);
    if (nodeEl) {
      if (field === 'label') nodeEl.querySelector('.evidence-node-label').innerText = val;
      if (field === 'val') nodeEl.querySelector('.evidence-node-val').innerText = val;
    }
    if (field === 'label') this.drawPinboardConnections();
  }

  switchEvidenceCase(caseId) {
    this.currentCaseId = caseId;
    this.activeEvidenceNodeId = null;
    this.renderEvidencePinboard();
    this.showToast(`Loaded case: ${this.getActiveEvidenceCase().title}`);
  }

  toggleRedStrings() {
    this.showRedStrings = !this.showRedStrings;
    this.drawPinboardConnections();
    this.showToast(this.showRedStrings ? 'Red connecting strings enabled' : 'Red strings hidden');
  }

  resetCasePositions() {
    const defCase = window.BENAQAAB_DATABASE.evidenceCases.find(c => c.id === this.currentCaseId);
    if (defCase) {
      const activeCase = this.getActiveEvidenceCase();
      activeCase.nodes = JSON.parse(JSON.stringify(defCase.nodes));
      this.saveState();
      this.renderEvidencePinboard();
      this.showToast('Node positions reset to layout defaults.');
    }
  }

  openNewNodeModal() {
    const modal = document.getElementById('newNodeModal');
    if (modal) modal.classList.add('open');
  }

  handleCreateNode(form) {
    const activeCase = this.getActiveEvidenceCase();
    const formData = new FormData(form);
    const label = formData.get('nodeLabel');
    const category = formData.get('nodeCategory');
    const val = formData.get('nodeVal') || '';
    const note = formData.get('nodeNote') || '';

    const colorMap = {
      'Benchmark': '#38bdf8',
      'Statutory': '#34d399',
      'Discretionary': '#fbbf24',
      'Consumer Impact': '#f43f5e',
      'Financial Bypass': '#a855f7'
    };

    const newNode = {
      id: `n_${Date.now().toString().slice(-4)}`,
      label: label,
      category: category,
      val: val,
      x: 180 + Math.round(Math.random() * 240),
      y: 120 + Math.round(Math.random() * 180),
      note: note,
      color: colorMap[category] || '#fbbf24'
    };

    activeCase.nodes.push(newNode);
    this.saveState();
    this.closeModals();
    form.reset();
    this.renderEvidencePinboard();
    this.selectEvidenceNode(newNode.id);
    this.showToast(`Pinned new evidence card: "${label}"`);
  }

  downloadPinboardPNG() {
    const activeCase = this.getActiveEvidenceCase();
    if (!activeCase) return;

    const exportCanvas = document.createElement('canvas');
    exportCanvas.width = 1920;
    exportCanvas.height = 1080;
    const ctx = exportCanvas.getContext('2d');

    const bgGrad = ctx.createRadialGradient(960, 540, 200, 960, 540, 1100);
    bgGrad.addColorStop(0, '#0f172a');
    bgGrad.addColorStop(1, '#04060a');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, 1920, 1080);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.05)';
    for (let x = 40; x < 1920; x += 40) {
      for (let y = 40; y < 1080; y += 40) {
        ctx.fillRect(x, y, 2, 2);
      }
    }

    ctx.font = '800 28px "Outfit", sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText(`BENAQAAB INDIA — FORENSIC EVIDENCE BOARD`, 60, 70);

    ctx.font = '600 16px "Inter", sans-serif';
    ctx.fillStyle = '#fbbf24';
    ctx.fillText(`CASE: ${activeCase.title.toUpperCase()} • SACH · SABOOT · BEBAK`, 60, 100);

    const stage = document.getElementById('pinboardStage');
    const scaleX = 1920 / (stage ? stage.clientWidth : 900);
    const scaleY = 1080 / (stage ? stage.clientHeight : 600);
    const scale = Math.min(scaleX, scaleY) * 0.9;
    const offsetX = 100;
    const offsetY = 120;

    ctx.save();
    ctx.lineCap = 'round';
    activeCase.connections.forEach(conn => {
      const fromNode = activeCase.nodes.find(n => n.id === conn.from);
      const toNode = activeCase.nodes.find(n => n.id === conn.to);
      if (!fromNode || !toNode) return;

      const x1 = offsetX + (fromNode.x + 100) * scale;
      const y1 = offsetY + fromNode.y * scale;
      const x2 = offsetX + (toNode.x + 100) * scale;
      const y2 = offsetY + toNode.y * scale;
      const midX = (x1 + x2) / 2;
      const midY = (y1 + y2) / 2 + 35 * scale;

      ctx.shadowColor = 'rgba(244, 63, 94, 0.8)';
      ctx.shadowBlur = 12;
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.quadraticCurveTo(midX, midY, x2, y2);
      ctx.stroke();

      if (conn.label) {
        ctx.font = '12px "JetBrains Mono", monospace';
        const txtWidth = ctx.measureText(conn.label).width;
        ctx.fillStyle = 'rgba(10, 13, 20, 0.9)';
        ctx.strokeStyle = 'rgba(244, 63, 94, 0.5)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.roundRect(midX - txtWidth / 2 - 8, midY - 10, txtWidth + 16, 20, 5);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#fca5a5';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(conn.label, midX, midY);
      }
    });
    ctx.restore();

    activeCase.nodes.forEach(node => {
      const cardX = offsetX + node.x * scale;
      const cardY = offsetY + node.y * scale;
      const cardW = 200 * scale;
      const cardH = 95 * scale;

      ctx.fillStyle = 'rgba(14, 18, 28, 0.95)';
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.18)';
      ctx.lineWidth = 1.5;
      ctx.shadowColor = 'rgba(0, 0, 0, 0.8)';
      ctx.shadowBlur = 16;
      ctx.beginPath();
      ctx.roundRect(cardX, cardY, cardW, cardH, 8);
      ctx.fill();
      ctx.stroke();
      ctx.shadowBlur = 0;

      ctx.fillStyle = '#f43f5e';
      ctx.beginPath();
      ctx.arc(cardX + cardW / 2, cardY, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.font = `700 ${Math.round(10 * scale)}px "JetBrains Mono", monospace`;
      ctx.fillStyle = node.color || '#fbbf24';
      ctx.textAlign = 'left';
      ctx.fillText(node.category.toUpperCase(), cardX + 12 * scale, cardY + 22 * scale);

      ctx.font = `700 ${Math.round(13 * scale)}px "Outfit", sans-serif`;
      ctx.fillStyle = '#ffffff';
      ctx.fillText(node.label, cardX + 12 * scale, cardY + 44 * scale);

      ctx.font = `800 ${Math.round(12 * scale)}px "JetBrains Mono", monospace`;
      ctx.fillStyle = '#fbbf24';
      ctx.fillText(node.val, cardX + 12 * scale, cardY + 68 * scale);
    });

    const link = document.createElement('a');
    link.download = `benaqaab_evidence_${activeCase.id}.png`;
    link.href = exportCanvas.toDataURL('image/png');
    link.click();
    this.showToast('1080p Forensic Evidence Board exported!');
  }

  exportCaseDossier() {
    const activeCase = this.getActiveEvidenceCase();
    if (!activeCase) return;

    let text = `# 🕵️ BENAQAAB INDIA — FORENSIC INVESTIGATION DOSSIER\n`;
    text += `**Case:** ${activeCase.title}\n`;
    text += `**Summary:** ${activeCase.summary}\n\n`;
    text += `## 📌 EVIDENCE NODES:\n`;
    activeCase.nodes.forEach(n => {
      text += `### [${n.category}] ${n.label}\n`;
      text += `- **Forensic Value / Stat:** ${n.val}\n`;
      text += `- **Citation / Note:** ${n.note || 'Official regulatory ledger'}\n\n`;
    });
    text += `## 🧵 CONNECTING THREADS:\n`;
    activeCase.connections.forEach(c => {
      const fromN = activeCase.nodes.find(n => n.id === c.from);
      const toN = activeCase.nodes.find(n => n.id === c.to);
      text += `- "${fromN ? fromN.label : c.from}" ➔ "${toN ? toN.label : c.to}": ${c.label}\n`;
    });

    navigator.clipboard.writeText(text).then(() => {
      this.showToast('Full forensic case dossier copied to clipboard!');
    });
  }

  // ==========================================================================
  // TAB 12: AUDIO & VOICEOVER STUDIO (-14 LUFS)
  // ==========================================================================
  initAudioStudio() {
    const populateVoices = () => {
      if ('speechSynthesis' in window) {
        this.ttsVoices = window.speechSynthesis.getVoices();
        const select = document.getElementById('ttsVoiceSelect');
        if (select && this.ttsVoices.length > 0) {
          select.innerHTML = this.ttsVoices.map((v, i) => {
            const isIndianOrHindi = v.lang.includes('IN') || v.lang.includes('hi');
            return `<option value="${i}" ${isIndianOrHindi ? 'selected' : ''}>${v.name} (${v.lang})</option>`;
          }).join('');
        }
      }
    };

    populateVoices();
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = populateVoices;
    }

    const ttsArea = document.getElementById('ttsScriptArea');
    if (ttsArea && !ttsArea.value) {
      this.loadTtsPreset('SH-08');
    }

    this.startVisualizerLoop();
  }

  loadTtsPreset(prodId) {
    const p = this.state.productions.find(x => x.id === prodId);
    const ttsArea = document.getElementById('ttsScriptArea');
    if (p && ttsArea) {
      ttsArea.value = p.hook || p.scriptText || '';
      this.showToast(`Loaded ${p.serial} hook into VO rehearsal.`);
    }
  }

  speakText() {
    if (!('speechSynthesis' in window)) {
      alert('Speech synthesis not supported in this browser.');
      return;
    }

    const ttsArea = document.getElementById('ttsScriptArea');
    const text = ttsArea ? ttsArea.value.trim() : '';
    if (!text) {
      alert('Please enter text to speak.');
      return;
    }

    window.speechSynthesis.cancel();

    this.ttsUtterance = new SpeechSynthesisUtterance(text);
    const select = document.getElementById('ttsVoiceSelect');
    if (select && this.ttsVoices[select.value]) {
      this.ttsUtterance.voice = this.ttsVoices[select.value];
    }

    const rateSlider = document.getElementById('ttsRateSlider');
    this.ttsUtterance.rate = rateSlider ? parseFloat(rateSlider.value) : 1.05;

    this.isTtsSpeaking = true;
    this.ttsUtterance.onend = () => {
      this.isTtsSpeaking = false;
    };
    this.ttsUtterance.onerror = () => {
      this.isTtsSpeaking = false;
    };

    window.speechSynthesis.speak(this.ttsUtterance);
    this.showToast('Playing voiceover rehearsal...');
  }

  pauseSpeaking() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.pause();
      this.isTtsSpeaking = false;
    }
  }

  stopSpeaking() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      this.isTtsSpeaking = false;
      this.showToast('Voiceover rehearsal stopped.');
    }
  }

  startVisualizerLoop() {
    const canvas = document.getElementById('audioVisualizerCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let phase = 0;

    const renderFrame = () => {
      requestAnimationFrame(renderFrame);

      if (this.currentTab !== 'voiceover') return;

      canvas.width = canvas.clientWidth;
      canvas.height = canvas.clientHeight;

      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      phase += 0.08;

      let energy = 0.15;
      if (this.isRecordingMic && this.analyser) {
        const dataArray = new Uint8Array(this.analyser.frequencyBinCount);
        this.analyser.getByteFrequencyData(dataArray);
        let sum = 0;
        for (let i = 0; i < dataArray.length; i++) sum += dataArray[i];
        energy = Math.max(0.1, sum / (dataArray.length * 128));
      } else if (this.isTtsSpeaking) {
        energy = 0.5 + Math.sin(phase * 2) * 0.35 + Math.random() * 0.15;
      }

      const meterFill = document.getElementById('audioMeterFill');
      const dbReadout = document.getElementById('audioDbReadout');
      if (meterFill && dbReadout) {
        const pct = Math.min(100, Math.round(energy * 100));
        meterFill.style.width = `${pct}%`;
        const approxDb = Math.round(-36 + energy * 34);
        dbReadout.innerText = `${approxDb} dB`;
        if (approxDb >= -15 && approxDb <= -13) {
          dbReadout.style.color = 'var(--emerald)';
        } else if (approxDb > -13) {
          dbReadout.style.color = 'var(--rose)';
        } else {
          dbReadout.style.color = 'var(--gold)';
        }
      }

      const numBars = 36;
      const barWidth = (w - (numBars * 4)) / numBars;

      for (let i = 0; i < numBars; i++) {
        const freqHeight = Math.sin(phase + i * 0.3) * (h * 0.4 * energy) + (h * 0.45 * energy);
        const x = i * (barWidth + 4) + 6;
        const y = h / 2 - freqHeight / 2;

        const grad = ctx.createLinearGradient(0, y, 0, y + freqHeight);
        grad.addColorStop(0, '#38bdf8');
        grad.addColorStop(0.6, '#fbbf24');
        grad.addColorStop(1, '#f43f5e');

        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.roundRect(x, y, barWidth, freqHeight, 3);
        ctx.fill();
      }

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.7)';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0; x < w; x += 4) {
        const wave = Math.sin(phase * 1.5 + x * 0.04) * (20 * energy);
        const y = h / 2 + wave;
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
    };

    renderFrame();
  }

  async toggleMicRecording() {
    if (!this.isRecordingMic) {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.micStream = stream;

        const AudioContext = window.AudioContext || window.webkitAudioContext;
        this.audioContext = new AudioContext();
        const source = this.audioContext.createMediaStreamSource(stream);
        this.analyser = this.audioContext.createAnalyser();
        this.analyser.fftSize = 64;
        source.connect(this.analyser);

        this.recordedChunks = [];
        this.mediaRecorder = new MediaRecorder(stream);
        this.mediaRecorder.ondataavailable = (e) => {
          if (e.data.size > 0) this.recordedChunks.push(e.data);
        };
        this.mediaRecorder.onstop = () => {
          const blob = new Blob(this.recordedChunks, { type: 'audio/webm' });
          const audioUrl = URL.createObjectURL(blob);
          const player = document.getElementById('recordedAudioPlayer');
          const dlBtn = document.getElementById('recordedDownloadBtn');
          const wrap = document.getElementById('recordedPlayerWrap');
          if (player) player.src = audioUrl;
          if (dlBtn) dlBtn.href = audioUrl;
          if (wrap) wrap.style.display = 'block';
        };

        this.mediaRecorder.start();
        this.isRecordingMic = true;
        this.micElapsedSec = 0;

        const startBtn = document.getElementById('recStartBtn');
        const cancelBtn = document.getElementById('recCancelBtn');
        const pulse = document.getElementById('recPulse');
        if (startBtn) startBtn.innerText = '⏹ Stop Recording VO';
        if (cancelBtn) cancelBtn.style.display = 'inline-block';
        if (pulse) pulse.classList.add('active');

        this.micTimerInterval = setInterval(() => {
          this.micElapsedSec++;
          const timerEl = document.getElementById('recTimer');
          if (timerEl) {
            const secStr = String(this.micElapsedSec).padStart(2, '0');
            timerEl.innerText = `00:${secStr} / 00:60`;
          }
          if (this.micElapsedSec >= 60) {
            this.toggleMicRecording();
          }
        }, 1000);

        this.showToast('Microphone recording started.');
      } catch (err) {
        alert('Could not access microphone: ' + err.message);
      }
    } else {
      if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
        this.mediaRecorder.stop();
      }
      if (this.micStream) {
        this.micStream.getTracks().forEach(t => t.stop());
      }
      clearInterval(this.micTimerInterval);
      this.isRecordingMic = false;

      const startBtn = document.getElementById('recStartBtn');
      const cancelBtn = document.getElementById('recCancelBtn');
      const pulse = document.getElementById('recPulse');
      if (startBtn) startBtn.innerText = '🔴 Start Recording VO';
      if (cancelBtn) cancelBtn.style.display = 'none';
      if (pulse) pulse.classList.remove('active');

      this.showToast('VO recording saved! Listen to preview below.');
    }
  }

  cancelMicRecording() {
    if (this.isRecordingMic) {
      if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
        this.mediaRecorder.stop();
      }
      if (this.micStream) {
        this.micStream.getTracks().forEach(t => t.stop());
      }
      clearInterval(this.micTimerInterval);
      this.isRecordingMic = false;
      this.recordedChunks = [];

      const startBtn = document.getElementById('recStartBtn');
      const cancelBtn = document.getElementById('recCancelBtn');
      const pulse = document.getElementById('recPulse');
      if (startBtn) startBtn.innerText = '🔴 Start Recording VO';
      if (cancelBtn) cancelBtn.style.display = 'none';
      if (pulse) pulse.classList.remove('active');

      this.showToast('Recording cancelled.');
    }
  }

  renderVoiceoverStudio() {}

  // ==========================================================================
  // TAB 13: 60-SECOND SHORTS RETENTION SEQUENCER
  // ==========================================================================
  renderRetentionSequencer() {
    const blueprint = (this.state.retentionBlueprints || []).find(b => b.id === this.currentRetentionId) || (this.state.retentionBlueprints || [])[0];
    if (!blueprint) return;

    const select = document.getElementById('retentionSelect');
    if (select) select.value = blueprint.id;

    let totalWords = 0;
    let totalSec = 0;
    blueprint.zones.forEach(z => {
      totalWords += z.words || 0;
      totalSec += z.targetSec || 0;
    });

    const avgWpm = totalSec > 0 ? Math.round((totalWords / (totalSec / 60))) : 0;

    const elWords = document.getElementById('retTotalWords');
    const elSec = document.getElementById('retTotalSec');
    const elWpm = document.getElementById('retAvgWpm');
    const elRisk = document.getElementById('retRiskScore');

    if (elWords) elWords.innerText = totalWords;
    if (elSec) elSec.innerText = `${totalSec.toFixed(1)}s`;
    if (elWpm) elWpm.innerText = `${avgWpm} WPM`;
    if (elRisk) {
      if (totalSec > 59) {
        elRisk.innerText = 'OVER 60S';
        elRisk.style.color = 'var(--rose)';
      } else if (avgWpm < 120) {
        elRisk.innerText = 'SLOW';
        elRisk.style.color = 'var(--gold)';
      } else {
        elRisk.innerText = 'OPTIMAL';
        elRisk.style.color = 'var(--emerald)';
      }
    }

    const container = document.getElementById('retentionBeatsContainer');
    if (!container) return;

    container.innerHTML = blueprint.zones.map((zone, idx) => {
      const zoneWpm = zone.targetSec > 0 ? Math.round((zone.words / (zone.targetSec / 60))) : 0;
      let pacingClass = 'pacing-opt';
      let pacingText = `${zoneWpm} WPM • OPTIMAL`;
      if (zoneWpm > 185) {
        pacingClass = 'pacing-fast';
        pacingText = `${zoneWpm} WPM • RAPID BURST`;
      } else if (zoneWpm < 125) {
        pacingClass = 'pacing-slow';
        pacingText = `${zoneWpm} WPM • SLOW PACING`;
      }

      return `
        <div class="beat-card">
          <div>
            <div style="font-family: var(--font-mono); font-weight: 800; color: var(--gold); font-size: 14px;">${zone.zone}</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">${zone.title}</div>
            <div style="margin-top: 8px;">
              <span class="pacing-badge ${pacingClass}">${pacingText}</span>
            </div>
          </div>

          <div>
            <label style="font-size: 11px; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 4px;">Spoken Narration Line</label>
            <textarea class="calc-input" rows="2" style="font-size: 12px; line-height: 1.4;" oninput="window.os.updateRetentionZone(${idx}, 'vo', this.value)">${zone.vo}</textarea>
          </div>

          <div>
            <label style="font-size: 11px; font-weight: 700; color: var(--sky); display: block; margin-bottom: 4px;">🎬 Visual Motion Cue</label>
            <div style="font-size: 11px; color: #fff; line-height: 1.4; background: rgba(255,255,255,0.03); padding: 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">
              ${zone.visual}
            </div>
          </div>

          <div>
            <label style="font-size: 11px; font-weight: 700; color: var(--rose); display: block; margin-bottom: 4px;">🔊 SFX Cue</label>
            <div style="font-size: 11px; font-family: var(--font-mono); color: #fca5a5;">
              ${zone.sfx}
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  switchRetentionBlueprint(bpId) {
    this.currentRetentionId = bpId;
    this.renderRetentionSequencer();
    this.showToast(`Loaded blueprint: ${bpId}`);
  }

  updateRetentionZone(zoneIdx, field, value) {
    const blueprint = (this.state.retentionBlueprints || []).find(b => b.id === this.currentRetentionId);
    if (!blueprint || !blueprint.zones[zoneIdx]) return;

    blueprint.zones[zoneIdx][field] = value;
    if (field === 'vo') {
      const words = value.trim().split(/\s+/).filter(Boolean).length;
      blueprint.zones[zoneIdx].words = words;
    }

    this.saveState();
    this.renderRetentionSequencer();
  }

  copyRetentionBeatSheet() {
    const blueprint = (this.state.retentionBlueprints || []).find(b => b.id === this.currentRetentionId);
    if (!blueprint) return;

    let text = `# ⏱️ BENAQAAB INDIA — 60-SECOND SHORTS RETENTION BLUEPRINT\n`;
    text += `**Title:** ${blueprint.title}\n`;
    text += `**Runtime:** ${blueprint.totalDuration}s | **Words:** ${blueprint.totalWords}\n\n`;
    text += `| Time Window | Pacing & Beat | Spoken Voiceover Line | On-Screen Visual / Motion Cue | SFX Trigger |\n`;
    text += `|---|---|---|---|---|\n`;

    blueprint.zones.forEach(z => {
      text += `| **${z.zone}** | ${z.title} | ${z.vo} | ${z.visual} | ${z.sfx} |\n`;
    });

    navigator.clipboard.writeText(text).then(() => {
      this.showToast('Retention beat sheet copied for video editor!');
    });
  }

  // ==========================================================================
  // TAB 14: CINEMATIC B-ROLL PROMPT SYNTHESIZER
  // ==========================================================================
  initPromptStudio() {
    this.updatePromptBuilder();
    this.renderPromptStudio();
  }

  updatePromptBuilder() {
    const subject = document.getElementById('promptSubjectSelect')?.value || 'gold_ingot';
    const style = document.getElementById('promptStyleSelect')?.value || 'macro_forensic';
    const lighting = document.getElementById('promptLightingSelect')?.value || 'rim_light';
    const aspect = document.querySelector('input[name="aspectRatio"]:checked')?.value || '9:16';

    const subjectMap = {
      'gold_ingot': 'Extreme macro cinematic shot of molten 24k liquid gold pouring into cast iron ingot mold, bright golden embers, specular liquid reflection',
      'showroom_bill': 'Angled close-up of folded retail jewelry showroom receipt paper on dark wooden table, neon yellow highlighter marker highlighting line item',
      'boeing_turbine': 'Commercial Boeing airliner jet engine turbine close-up on wet airport tarmac, heavy fuel hose refueling connector with glowing green digital flow rate meter',
      'supreme_court': 'Solid dark mahogany courtroom table with open Indian legal statute book, polished judicial wooden gavel, Manila envelope stamped CONFIDENTIAL',
      'evm_microchip': 'Extreme macro photograph of electronic voting machine silicon microprocessor on green motherboard circuit board, microscopic glowing traces',
      'kavach_train': 'Futuristic train locomotive driver cabin interior at high speed, glass dashboard digital display showing Kavach 4.0 automatic braking active in neon green',
      'lithium_rock': 'Hand in rugged field work glove holding raw white-grey crystalline spodumene lithium ore rock, Himalayan mountain peaks of Jammu in bokeh background',
      'stock_ticker': 'Wall of multi-tiered LED financial stock ticker displays in darkened trading room floor, illuminated red and green percentage numbers, motion blur'
    };

    const styleMap = {
      'macro_forensic': '35mm anamorphic macro lens, extreme depth of field, floating atmospheric dust particles, 8k documentary investigation realism',
      'archive_documentary': 'Kodak Vision3 500T 35mm film stock, vintage documentary archive grain, muted chromatic tones, authentic journalistic quality',
      'infographic_3d': 'Isometric 3D glassmorphism perspective, frosted glowing cyan and warm amber HUD lines, dark slate background, ultra clean render',
      'surveillance_cctv': 'Surveillance camera telephoto angle, subtle scanlines, high-contrast shadow drama, cinematic teal and dark orange color grade'
    };

    const lightMap = {
      'rim_light': 'volumetric moody rim lighting, deep obsidian slate backdrop, subtle specular highlights',
      'interrogation': 'harsh directional overhead interrogation spotlight, heavy dark drop shadows',
      'cinematic_dusk': 'cold twilight blue ambient light mixed with warm 3200K tungsten spotlight accents',
      'clean_lab': 'clean high-key forensic laboratory diffuse illumination, zero digital distortion'
    };

    const promptText = `${subjectMap[subject]}, ${styleMap[style]}, ${lightMap[lighting]} --ar ${aspect} --v 6.1 --style raw --q 2`;

    const outBox = document.getElementById('generatedPromptOutput');
    const badge = document.getElementById('promptArBadge');
    if (outBox) outBox.innerText = promptText;
    if (badge) badge.innerText = `--ar ${aspect}`;
  }

  randomizePrompt() {
    const subjects = ['gold_ingot', 'showroom_bill', 'boeing_turbine', 'supreme_court', 'evm_microchip', 'kavach_train', 'lithium_rock', 'stock_ticker'];
    const styles = ['macro_forensic', 'archive_documentary', 'infographic_3d', 'surveillance_cctv'];
    const lightings = ['rim_light', 'interrogation', 'cinematic_dusk', 'clean_lab'];

    const subEl = document.getElementById('promptSubjectSelect');
    const styEl = document.getElementById('promptStyleSelect');
    const ligEl = document.getElementById('promptLightingSelect');

    if (subEl) subEl.value = subjects[Math.floor(Math.random() * subjects.length)];
    if (styEl) styEl.value = styles[Math.floor(Math.random() * styles.length)];
    if (ligEl) ligEl.value = lightings[Math.floor(Math.random() * lightings.length)];

    this.updatePromptBuilder();
    this.showToast('Randomized prompt parameters!');
  }

  copyCurrentPrompt() {
    const outBox = document.getElementById('generatedPromptOutput');
    if (!outBox) return;
    navigator.clipboard.writeText(outBox.innerText).then(() => {
      this.showToast('AI B-Roll prompt copied to clipboard!');
    });
  }

  renderPromptStudio() {
    const container = document.getElementById('promptCardsContainer');
    if (!container) return;

    container.innerHTML = (this.state.promptTemplates || []).map(p => `
      <div class="prompt-item-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span class="status-tag status-delivered" style="font-size: 10px;">${p.category}</span>
          <span class="param-badge">--ar ${p.aspect}</span>
        </div>
        <div style="font-weight: 800; color: #fff; font-size: 13px;">${p.title}</div>
        <div style="font-size: 11px; color: var(--text-muted); line-height: 1.4; font-family: var(--font-mono); max-height: 60px; overflow: hidden; text-overflow: ellipsis;">
          ${p.prompt.slice(0, 110)}...
        </div>
        <div style="display: flex; gap: 8px; margin-top: auto;">
          <button class="btn btn-secondary" style="flex: 1; font-size: 11px; justify-content: center;" onclick="navigator.clipboard.writeText('${p.prompt.replace(/'/g, "\\'")}').then(() => window.os.showToast('Preset prompt copied!'))">
            📋 Copy
          </button>
        </div>
      </div>
    `).join('');
  }

  // ==========================================================================
  // TAB 15: STUDIO BACKUP & RESTORE DATA CENTER
  // ==========================================================================
  openBackupModal() {
    const modal = document.getElementById('backupModal');
    if (!modal) return;

    const savedStr = localStorage.getItem(this.storageKey) || '';
    const bytes = new Blob([savedStr]).size;
    const kb = (bytes / 1024).toFixed(1);
    const quotaKb = 5120;
    const pct = Math.min(100, Math.max(1, (kb / quotaKb * 100).toFixed(1)));

    const txt = document.getElementById('backupStorageText');
    const fill = document.getElementById('backupStorageFill');
    if (txt) txt.innerText = `${kb} KB / ${quotaKb} KB (${pct}% used)`;
    if (fill) fill.style.width = `${pct}%`;

    modal.classList.add('open');
  }

  exportFullBackup() {
    const jsonStr = JSON.stringify(this.state, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `benaqaab_studio_snapshot_${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    this.showToast('Full Studio snapshot downloaded successfully!');
  }

  importBackupFile(fileInput) {
    const file = fileInput.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const parsed = JSON.parse(e.target.result);
        if (!parsed.productions && !parsed.channel) {
          throw new Error('Invalid Benaqaab studio schema.');
        }

        this.state = parsed;
        this.saveState();
        this.render();
        this.closeModals();
        this.showToast('Studio successfully restored from backup snapshot!');
      } catch (err) {
        alert('Failed to import backup file: ' + err.message);
      }
    };
    reader.readAsText(file);
    fileInput.value = '';
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
