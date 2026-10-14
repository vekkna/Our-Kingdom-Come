/**
 * OUR KINGDOM COME - ZINGARA GM WIKI APPLICATION ENGINE
 * Vanilla JavaScript (ES6+), Zero External Dependencies
 * Fast Loading, Tablet-Optimized, Instant Client-Side Search & Hyperlinking
 */

(function () {
  'use strict';

  // Safe Storage Wrapper (never throws even if cookies/storage blocked)
  const safeStorage = {
    getItem: (key, fallback = null) => {
      try {
        const val = localStorage.getItem(key);
        return val !== null ? val : fallback;
      } catch (e) {
        return fallback;
      }
    },
    setItem: (key, val) => {
      try {
        localStorage.setItem(key, val);
      } catch (e) {}
    }
  };

  // State Management
  const AppState = {
    currentArticleId: 'campaign-premise',
    currentCategory: 'overview',
    theme: document.documentElement.getAttribute('data-theme') || safeStorage.getItem('okc_theme', 'dark'),
    isPlayerSafe: safeStorage.getItem('okc_player_safe', 'false') === 'true',
    sidebarOpen: window.innerWidth > 900,
    drawerEntityId: null,
    searchQuery: '',
    selectedSearchIdx: 0,
    sessions: []
  };
  window.AppState = AppState;

  const getWikiData = () => window.WIKI_DATA || (typeof WIKI_DATA !== 'undefined' ? WIKI_DATA : null);
  const EntityGlossary = [];

  function initGlossary() {
    const data = getWikiData();
    if (!data || !data.articles) return;

    EntityGlossary.length = 0; // Clear any existing
    data.articles.forEach(article => {
      // Add primary title
      EntityGlossary.push({
        term: article.title,
        id: article.id,
        category: article.category,
        length: article.title.length
      });

      // Add aliases
      if (article.aliases && Array.isArray(article.aliases)) {
        article.aliases.forEach(alias => {
          if (alias && alias.length > 2 && alias !== article.title) {
            EntityGlossary.push({
              term: alias,
              id: article.id,
              category: article.category,
              length: alias.length
            });
          }
        });
      }
    });

    // Sort longest terms first to prevent partial substring collisions
    EntityGlossary.sort((a, b) => b.length - a.length);
  }

  // Get article by ID
  function getArticle(id) {
    const data = getWikiData();
    if (!data || !data.articles) return null;
    return data.articles.find(a => a.id === id || (a.aliases && a.aliases.includes(id)));
  }

  // =========================================================================
  // AUTOMATIC HYPERLINKING ENGINE
  // =========================================================================
  function autoHyperlink(html, currentId) {
    if (!html || EntityGlossary.length === 0) return html;

    // Use a DOM parser to safely process only text nodes outside of existing <a>, <h1-h4>, or <button>
    const parser = new DOMParser();
    const doc = parser.parseFromString(`<div>${html}</div>`, 'text/html');
    const container = doc.body.firstElementChild;

    // Create a Set of already linked entity IDs in this article to avoid over-linking every single repeated word
    const linkedIds = new Set([currentId]);

    function processTextNode(node) {
      const parentTag = node.parentNode.nodeName.toLowerCase();
      if (['a', 'h1', 'h2', 'h3', 'h4', 'button', 'script', 'style'].includes(parentTag)) {
        return;
      }
      if (node.parentNode.classList && node.parentNode.classList.contains('wiki-link')) {
        return;
      }

      let text = node.nodeValue;
      if (!text || text.trim().length === 0) return;

      for (const entry of EntityGlossary) {
        if (entry.id === currentId) continue;
        if (linkedIds.has(entry.id)) continue; // Link each entity at most once per section for clean reading

        // Case-sensitive or word-boundary boundary match
        const escaped = entry.term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const regex = new RegExp(`\\b(${escaped})\\b`, 'i');
        const match = regex.exec(text);

        if (match) {
          const matchIndex = match.index;
          const matchLength = match[0].length;

          const before = text.substring(0, matchIndex);
          const matchedText = text.substring(matchIndex, matchIndex + matchLength);
          const after = text.substring(matchIndex + matchLength);

          const beforeNode = document.createTextNode(before);
          const linkNode = document.createElement('a');
          linkNode.href = `#${entry.category}/${entry.id}`;
          linkNode.className = 'wiki-link';
          linkNode.setAttribute('data-id', entry.id);
          linkNode.setAttribute('data-category', entry.category);
          linkNode.textContent = matchedText;

          const afterNode = document.createTextNode(after);

          const parent = node.parentNode;
          parent.insertBefore(beforeNode, node);
          parent.insertBefore(linkNode, node);
          parent.insertBefore(afterNode, node);
          parent.removeChild(node);

          linkedIds.add(entry.id);

          // Recursively process the remainder of the text
          processTextNode(afterNode);
          return;
        }
      }
    }

    function walkNodes(root) {
      const walker = doc.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
      const nodes = [];
      while (walker.nextNode()) {
        nodes.push(walker.currentNode);
      }
      nodes.forEach(processTextNode);
    }

    walkNodes(container);
    return container.innerHTML;
  }

  // =========================================================================
  // VIEW RENDERING
  // =========================================================================
  function renderSidebar() {
    const navTreeContainer = document.getElementById('sidebar-nav-tree');
    const data = getWikiData();
    if (!navTreeContainer || !data) return;

    let html = '';

    data.categories.forEach(cat => {
      const articlesInCat = data.articles.filter(a => a.category === cat.id);
      const isExpanded = (AppState.currentCategory === cat.id);

      html += `
        <div class="nav-group" data-cat-id="${cat.id}">
          <div class="sidebar-section-header">
            <span>${cat.icon} ${cat.name}</span>
            <span class="nav-count">${cat.id === 'sessions' ? AppState.sessions.length : articlesInCat.length}</span>
          </div>
          <div class="nav-group-items">
      `;

      if (cat.id === 'sessions') {
        const isActive = AppState.currentArticleId === 'sessions';
        html += `
          <div class="nav-item ${isActive ? 'active' : ''}" data-nav="sessions">
            <span class="nav-icon">📖</span>
            <span class="nav-label">Campaign Session Logs</span>
          </div>
        `;
      } else {
        articlesInCat.forEach(art => {
          const isActive = (AppState.currentArticleId === art.id);
          html += `
            <div class="nav-item ${isActive ? 'active' : ''}" data-nav="${cat.id}/${art.id}">
              <span class="nav-icon">&bull;</span>
              <span class="nav-label">${art.title}</span>
            </div>
          `;
        });
      }

      html += `
          </div>
        </div>
      `;
    });

    navTreeContainer.innerHTML = html;

    // Attach click events to nav items
    navTreeContainer.querySelectorAll('.nav-item').forEach(item => {
      item.addEventListener('click', (e) => {
        const route = item.getAttribute('data-nav');
        window.location.hash = route;
        if (window.innerWidth <= 900) {
          closeSidebar();
        }
      });
    });
  }

  function renderArticle(article) {
    const container = document.getElementById('content-area');
    if (!container) return;

    if (!article) {
      container.innerHTML = `
        <div class="content-container">
          <h2>Article Not Found</h2>
          <p>The requested topic could not be located in the Zingara archives.</p>
          <p><a href="#overview/campaign-premise">Return to Campaign Premise</a></p>
        </div>
      `;
      return;
    }

    const data = getWikiData();
    const catObj = (data && data.categories ? data.categories.find(c => c.id === article.category) : null) || { name: article.category, icon: '📜' };

    // Format tags
    let tagsHtml = '';
    if (article.tags && article.tags.length > 0) {
      tagsHtml = `<div class="article-tags">` + article.tags.map(t => `<span class="tag-pill">${t}</span>`).join('') + `</div>`;
    }

    // Process content through auto-hyperlinking
    const hyperlinkedContent = autoHyperlink(article.content, article.id);

    // Cross-references
    let relatedHtml = '';
    if (article.relatedIds && article.relatedIds.length > 0) {
      const relatedLinks = article.relatedIds.map(rid => {
        const relArt = getArticle(rid);
        if (relArt) {
          return `<a href="#${relArt.category}/${relArt.id}" class="wiki-link" data-id="${relArt.id}">${relArt.title}</a>`;
        }
        return '';
      }).filter(Boolean).join(' ');

      if (relatedLinks) {
        relatedHtml = `
          <div class="info-card" style="margin-top: 30px;">
            <h4>Related Dossiers &amp; References</h4>
            <p>${relatedLinks}</p>
          </div>
        `;
      }
    }

    container.innerHTML = `
      <div class="content-container">
        <div class="breadcrumb-trail">
          <a href="#overview/campaign-premise">Our Kingdom Come</a>
          <span class="breadcrumb-separator">&rsaquo;</span>
          <span>${catObj.icon} ${catObj.name}</span>
          <span class="breadcrumb-separator">&rsaquo;</span>
          <span>${article.title}</span>
        </div>

        <div class="article-header">
          <span class="article-category-badge">${catObj.name}</span>
          <h1 class="article-title">${article.title}</h1>
          ${article.subtitle ? `<div class="article-subtitle">${article.subtitle}</div>` : ''}
          ${tagsHtml}
        </div>

        <div class="article-body">
          ${hyperlinkedContent}
        </div>

        ${relatedHtml}
      </div>
    `;

    // Reset scroll position to top
    container.scrollTop = 0;

    // Attach click listeners to all wiki-links in article body
    attachWikiLinkEvents(container);
  }

  // =========================================================================
  // PREVIEW DRAWER (SLIDE-OUT QUICK CARD)
  // =========================================================================
  function openPreviewDrawer(entityId) {
    const article = getArticle(entityId);
    if (!article) return;

    AppState.drawerEntityId = entityId;
    const drawer = document.getElementById('preview-drawer');
    const titleEl = document.getElementById('drawer-title');
    const subEl = document.getElementById('drawer-subtitle');
    const bodyEl = document.getElementById('drawer-body');
    const fullLinkEl = document.getElementById('drawer-open-full-btn');

    titleEl.textContent = article.title;
    subEl.textContent = article.subtitle || article.category;
    fullLinkEl.setAttribute('data-target', `#${article.category}/${article.id}`);

    let glanceHtml = '';
    if (article.atAGlance) {
      const g = article.atAGlance;
      glanceHtml = `
        <div class="at-a-glance-grid" style="margin-top: 0; margin-bottom: 14px;">
          ${g.appearance ? `<div class="glance-item"><strong>Appearance:</strong> ${g.appearance}</div>` : ''}
          ${g.mannerisms ? `<div class="glance-item"><strong>Mannerisms:</strong> ${g.mannerisms}</div>` : ''}
          ${g.quote ? `<div class="glance-item quote"><strong>Quote:</strong> &ldquo;${g.quote}&rdquo;</div>` : ''}
          ${g.courtDCs ? `<div class="glance-item dcs"><strong>Court DCs:</strong> ${g.courtDCs}</div>` : ''}
        </div>
      `;
    }

    bodyEl.innerHTML = `
      ${glanceHtml}
      <h4>Summary</h4>
      <p>${article.summary}</p>
      ${article.gmSecrets ? `
        <div class="gm-callout" style="margin-top: 14px;">
          <div class="gm-badge">GM SECRET LEVER</div>
          <p>${article.gmSecrets}</p>
        </div>
      ` : ''}
      <p style="margin-top: 14px;"><small class="text-dim">Tap "Open Full Article" below to view complete background, plot hooks, and tactical encounters.</small></p>
    `;

    drawer.classList.add('open');
  }

  function closePreviewDrawer() {
    const drawer = document.getElementById('preview-drawer');
    if (drawer) {
      drawer.classList.remove('open');
      AppState.drawerEntityId = null;
    }
  }

  function attachWikiLinkEvents(parentElement) {
    parentElement.querySelectorAll('.wiki-link').forEach(link => {
      link.addEventListener('click', (e) => {
        const id = link.getAttribute('data-id');
        // If holding shift or ctrl, open in full article directly; otherwise open in fast preview drawer
        if (e.shiftKey || e.ctrlKey || e.metaKey) {
          return; // Let default hash navigation proceed
        }
        e.preventDefault();
        openPreviewDrawer(id);
      });
    });
  }

  // =========================================================================
  // LIVE INSTANT SEARCH ENGINE
  // =========================================================================
  function initSearch() {
    const searchInput = document.getElementById('global-search');
    const resultsModal = document.getElementById('search-results-modal');
    const resultsList = document.getElementById('search-results-list');

    if (!searchInput || !resultsModal || !resultsList) return;

    function performSearch(query) {
      query = query.trim().toLowerCase();
      if (query.length === 0) {
        resultsModal.style.display = 'none';
        return;
      }

      const matches = [];

      const data = getWikiData();
      if (!data || !data.articles) return;

      data.articles.forEach(art => {
        let score = 0;
        let matchedSnippet = '';

        // Exact or prefix title match
        if (art.title.toLowerCase().startsWith(query)) score += 50;
        else if (art.title.toLowerCase().includes(query)) score += 30;

        // Subtitle match
        if (art.subtitle && art.subtitle.toLowerCase().includes(query)) score += 15;

        // Alias match
        if (art.aliases && art.aliases.some(al => al.toLowerCase().includes(query))) score += 25;

        // Tag match
        if (art.tags && art.tags.some(t => t.toLowerCase().includes(query))) score += 20;

        // Content match
        const contentLower = (art.content || '').toLowerCase();
        const contentIdx = contentLower.indexOf(query);
        if (contentIdx !== -1) {
          score += 10;
          const start = Math.max(0, contentIdx - 40);
          const end = Math.min(art.content.length, contentIdx + query.length + 60);
          matchedSnippet = '...' + art.content.substring(start, end).replace(/<[^>]+>/g, '') + '...';
        } else if (art.summary) {
          matchedSnippet = art.summary.substring(0, 100) + '...';
        }

        if (score > 0) {
          matches.push({
            article: art,
            score: score,
            snippet: matchedSnippet
          });
        }
      });

      // Sort by score descending
      matches.sort((a, b) => b.score - a.score);

      renderSearchResults(matches.slice(0, 12), query);
    }

    function renderSearchResults(results, query) {
      if (results.length === 0) {
        resultsList.innerHTML = `
          <div style="padding: 16px; color: var(--text-dim); text-align: center;">
            No lore matching &ldquo;<strong>${escapeHtml(query)}</strong>&rdquo;
          </div>
        `;
        resultsModal.style.display = 'block';
        return;
      }

      AppState.selectedSearchIdx = 0;

      let html = '';
      results.forEach((res, idx) => {
        const art = res.article;
        const isSelected = idx === 0;

        // Highlight matched query in title
        const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
        const highlightedTitle = art.title.replace(regex, '<span class="search-highlight">$1</span>');

        html += `
          <div class="search-result-item ${isSelected ? 'selected' : ''}" data-idx="${idx}" data-route="#${art.category}/${art.id}">
            <div class="search-result-top">
              <span class="search-result-title">${highlightedTitle}</span>
              <span class="search-result-category">${art.category}</span>
            </div>
            <div class="search-result-snippet">${res.snippet}</div>
          </div>
        `;
      });

      resultsList.innerHTML = html;
      resultsModal.style.display = 'block';

      // Click event for results
      resultsList.querySelectorAll('.search-result-item').forEach(item => {
        item.addEventListener('click', () => {
          const route = item.getAttribute('data-route');
          window.location.hash = route;
          resultsModal.style.display = 'none';
          searchInput.value = '';
        });
      });
    }

    searchInput.addEventListener('input', (e) => {
      performSearch(e.target.value);
    });

    // Keyboard navigation (Arrow keys, Enter, Escape, Hotkey '/')
    document.addEventListener('keydown', (e) => {
      // Focus search on '/' or Ctrl+K if not in an input
      if ((e.key === '/' || (e.ctrlKey && e.key === 'k')) && document.activeElement !== searchInput && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
        return;
      }

      if (resultsModal.style.display === 'block') {
        const items = resultsList.querySelectorAll('.search-result-item');
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          AppState.selectedSearchIdx = (AppState.selectedSearchIdx + 1) % items.length;
          updateSelectedSearchResult(items);
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          AppState.selectedSearchIdx = (AppState.selectedSearchIdx - 1 + items.length) % items.length;
          updateSelectedSearchResult(items);
        } else if (e.key === 'Enter') {
          e.preventDefault();
          if (items[AppState.selectedSearchIdx]) {
            items[AppState.selectedSearchIdx].click();
          }
        } else if (e.key === 'Escape') {
          resultsModal.style.display = 'none';
        }
      }
    });

    function updateSelectedSearchResult(items) {
      items.forEach((item, idx) => {
        if (idx === AppState.selectedSearchIdx) {
          item.classList.add('selected');
          item.scrollIntoView({ block: 'nearest' });
        } else {
          item.classList.remove('selected');
        }
      });
    }

    // Dismiss search when clicking outside
    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !resultsModal.contains(e.target)) {
        resultsModal.style.display = 'none';
      }
    });
  }

  // =========================================================================
  // SESSION LOG & CAMPAIGN TRACKER
  // =========================================================================
  async function initSessions() {
    const saved = safeStorage.getItem('okc_sessions');
    if (saved) {
      try {
        AppState.sessions = JSON.parse(saved);
      } catch (err) {
        console.error('Failed to parse saved sessions', err);
      }
    }

    // If no saved sessions in storage, load from data/sessions.json or use embedded default
    if (!AppState.sessions || AppState.sessions.length === 0) {
      try {
        const res = await fetch('data/sessions.json');
        if (res.ok) {
          AppState.sessions = await res.json();
          saveSessions();
        }
      } catch (e) {
        // Fallback for file:// protocol or offline use
        AppState.sessions = [
          {
            "sessionNumber": 0,
            "title": "The Coronation on Crystal & The Handlers' Trap",
            "realDate": "Campaign Launch",
            "inGameDate": "Month of the Sun, Period VIII (Year 1 of the Triumvirate)",
            "summary": "The Player Character Triumvirate was crowned in Kordava upon the famed floor of polished crystal. General Don Rodrigo de Valenza stationed his elite caballeros around the palace perimeter, pledging martial protection. High Chancellor Marquis Mateo de Sadoria assumed direct custody of all crown ledgers, officially declaring the state treasury bankrupt due to foreign debt obligations to Argos. The young monarchs received formal bows from the assembled Grandees, though Duke Gonzalo de Guarralid made several cutting remarks testing their martial mettle under pundonor. Underground intelligence confirms that republican cells in The Pit view the coronation as a farce, while the outlawed Church of Nemeth has stepped up nocturnal recruitment.",
            "sovereigntyPoints": 0,
            "pundonorStatus": "Unstained (No penalties active)",
            "activeThreads": [
              "The Empty Vaults: Marquis Mateo has refused royal requests for personal guard stipends.",
              "The Whispering Pit: Republican agitators are circulating pamphlets claiming the Restoration Council murdered the republican founder in Period VI.",
              "The River Embargo: Rumors that Duke Gonzalo's retainers in Jerida are preparing to halt crown timber barges."
            ],
            "npcDispositions": {
              "General Don Rodrigo de Valenza": "Protective / Patronizing (+1 Martial Guard, -1 Freedom)",
              "High Chancellor Marquis Mateo de Sadoria": "Cordial / Financially Restrictive",
              "Fencing Master Lucia 'La Mariposa'": "Hostile / Curious (Awaiting royal action)",
              "Father Malachai the Blind": "Condemnatory (Demands destruction of zombie pits)",
              "High Duke Gonzalo de Guarralid": "Dismissive / Challenging (Testing pundonor)"
            }
          }
        ];
        saveSessions();
      }
    }
  }

  function saveSessions() {
    safeStorage.setItem('okc_sessions', JSON.stringify(AppState.sessions));
  }

  function renderSessionView() {
    const container = document.getElementById('content-area');
    if (!container) return;

    let sessionCardsHtml = '';

    if (AppState.sessions.length === 0) {
      sessionCardsHtml = `<p class="text-dim">No sessions logged yet. Tap "Log New Session" to record your first game session.</p>`;
    } else {
      // Sort sessions descending by sessionNumber
      const sorted = [...AppState.sessions].sort((a, b) => b.sessionNumber - a.sessionNumber);

      sorted.forEach(s => {
        let threadsHtml = '';
        if (s.activeThreads && s.activeThreads.length > 0) {
          threadsHtml = `<ul>` + s.activeThreads.map(t => `<li>${autoHyperlink(t, 'sessions')}</li>`).join('') + `</ul>`;
        }

        let npcHtml = '';
        if (s.npcDispositions) {
          npcHtml = `<div class="session-stats-grid">`;
          for (const [npc, disp] of Object.entries(s.npcDispositions)) {
            npcHtml += `<div><strong>${npc}:</strong> ${disp}</div>`;
          }
          npcHtml += `</div>`;
        }

        sessionCardsHtml += `
          <div class="session-card">
            <div class="session-header">
              <div>
                <span class="session-num-badge">Session ${s.sessionNumber}</span>
                <strong style="font-size: 1.15rem; color: var(--accent-gold);">${s.title}</strong>
              </div>
              <div class="session-dates">
                <div>${s.realDate}</div>
                <div style="font-style: italic; color: var(--text-muted);">${s.inGameDate}</div>
              </div>
            </div>

            <p>${autoHyperlink(s.summary, 'sessions')}</p>

            <div class="session-stats-grid">
              <div><strong>Crown Sovereignty:</strong> ${s.sovereigntyPoints > 0 ? '+' : ''}${s.sovereigntyPoints}</div>
              <div><strong>Pundonor Status:</strong> ${s.pundonorStatus || 'Unstained'}</div>
            </div>

            ${threadsHtml ? `<h4>Active Plot Leads</h4>${threadsHtml}` : ''}
            ${npcHtml ? `<h4>Court NPC Dispositions</h4>${npcHtml}` : ''}
          </div>
        `;
      });
    }

    container.innerHTML = `
      <div class="content-container">
        <div class="breadcrumb-trail">
          <a href="#overview/campaign-premise">Our Kingdom Come</a>
          <span class="breadcrumb-separator">&rsaquo;</span>
          <span>Campaign Session Log</span>
        </div>

        <div class="article-header">
          <span class="article-category-badge">Live Play Tracker</span>
          <h1 class="article-title">Campaign Session Logs</h1>
          <div class="article-subtitle">Chronicle of Royal Triumvirate Edicts, Court Intrigues, and Session Recaps</div>
        </div>

        <div class="session-controls">
          <button id="btn-add-session" class="btn-primary">+ Log New Session</button>
          <div style="display: flex; gap: 8px;">
            <button id="btn-export-sessions-json" class="btn-secondary" title="Export JSON to commit to git">Export JSON</button>
            <button id="btn-export-sessions-md" class="btn-secondary" title="Export Markdown summary">Download Markdown</button>
            <button id="btn-import-sessions" class="btn-secondary" title="Import session file">Import JSON</button>
            <input type="file" id="import-file-input" style="display: none;" accept=".json">
          </div>
        </div>

        <div class="session-timeline">
          ${sessionCardsHtml}
        </div>
      </div>
    `;

    container.scrollTop = 0;

    // Attach Session Log Action Handlers
    document.getElementById('btn-add-session')?.addEventListener('click', openAddSessionModal);
    document.getElementById('btn-export-sessions-json')?.addEventListener('click', exportSessionsJSON);
    document.getElementById('btn-export-sessions-md')?.addEventListener('click', exportSessionsMarkdown);
    document.getElementById('btn-import-sessions')?.addEventListener('click', () => {
      document.getElementById('import-file-input')?.click();
    });
    document.getElementById('import-file-input')?.addEventListener('change', importSessionsJSON);

    attachWikiLinkEvents(container);
  }

  function openAddSessionModal() {
    const nextNum = AppState.sessions.length > 0 ? Math.max(...AppState.sessions.map(s => s.sessionNumber)) + 1 : 1;
    const modal = document.getElementById('session-modal');
    if (!modal) return;

    document.getElementById('modal-session-num').value = nextNum;
    document.getElementById('modal-session-date').value = new Date().toISOString().split('T')[0];
    document.getElementById('modal-session-ingame').value = `Month of the Lion, Year 1 (Period VIII)`;
    document.getElementById('modal-session-title').value = '';
    document.getElementById('modal-session-summary').value = '';
    document.getElementById('modal-session-sovereignty').value = 0;
    document.getElementById('modal-session-pundonor').value = 'Unstained';
    document.getElementById('modal-session-threads').value = '';

    modal.style.display = 'flex';
  }

  function closeAddSessionModal() {
    const modal = document.getElementById('session-modal');
    if (modal) modal.style.display = 'none';
  }

  function saveNewSessionFromModal() {
    const num = parseInt(document.getElementById('modal-session-num').value, 10) || 1;
    const realDate = document.getElementById('modal-session-date').value;
    const inGameDate = document.getElementById('modal-session-ingame').value;
    const title = document.getElementById('modal-session-title').value || `Session ${num}`;
    const summary = document.getElementById('modal-session-summary').value;
    const sovereignty = parseInt(document.getElementById('modal-session-sovereignty').value, 10) || 0;
    const pundonor = document.getElementById('modal-session-pundonor').value;
    const threadsRaw = document.getElementById('modal-session-threads').value;

    const threads = threadsRaw.split('\n').map(t => t.trim()).filter(Boolean);

    const newSession = {
      sessionNumber: num,
      title: title,
      realDate: realDate,
      inGameDate: inGameDate,
      summary: summary,
      sovereigntyPoints: sovereignty,
      pundonorStatus: pundonor,
      activeThreads: threads,
      npcDispositions: {}
    };

    AppState.sessions.push(newSession);
    saveSessions();
    closeAddSessionModal();
    renderSessionView();
    renderSidebar();
  }

  function exportSessionsJSON() {
    const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(AppState.sessions, null, 2));
    const dlAnchor = document.createElement('a');
    dlAnchor.setAttribute('href', dataStr);
    dlAnchor.setAttribute('download', 'sessions.json');
    dlAnchor.click();
  }

  function exportSessionsMarkdown() {
    let md = `# Our Kingdom Come — Campaign Session Recaps\n\n`;
    const sorted = [...AppState.sessions].sort((a, b) => a.sessionNumber - b.sessionNumber);

    sorted.forEach(s => {
      md += `## Session ${s.sessionNumber}: ${s.title}\n`;
      md += `**Date:** ${s.realDate} | **In-Game Date:** ${s.inGameDate}\n\n`;
      md += `**Crown Sovereignty:** ${s.sovereigntyPoints} | **Pundonor:** ${s.pundonorStatus}\n\n`;
      md += `### Summary\n${s.summary}\n\n`;
      if (s.activeThreads && s.activeThreads.length > 0) {
        md += `### Active Plot Threads\n`;
        s.activeThreads.forEach(t => md += `- ${t}\n`);
        md += `\n`;
      }
      md += `---\n\n`;
    });

    const dataStr = 'data:text/markdown;charset=utf-8,' + encodeURIComponent(md);
    const dlAnchor = document.createElement('a');
    dlAnchor.setAttribute('href', dataStr);
    dlAnchor.setAttribute('download', 'campaign_sessions.md');
    dlAnchor.click();
  }

  function importSessionsJSON(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (e) {
      try {
        const imported = JSON.parse(e.target.result);
        if (Array.isArray(imported)) {
          AppState.sessions = imported;
          saveSessions();
          renderSessionView();
          renderSidebar();
          alert('Sessions imported successfully!');
        } else {
          alert('Invalid sessions JSON file format.');
        }
      } catch (err) {
        alert('Error parsing JSON file: ' + err.message);
      }
    };
    reader.readAsText(file);
  }

  // =========================================================================
  // LIGHT / DARK THEME TOGGLE
  // =========================================================================
  function initThemeToggle() {
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (!themeBtn) return;

    function applyTheme() {
      const isLight = AppState.theme === 'light';
      document.documentElement.setAttribute('data-theme', AppState.theme);
      document.documentElement.className = isLight ? 'light-theme' : 'dark-theme';
      if (document.body) {
        document.body.setAttribute('data-theme', AppState.theme);
        document.body.className = (document.body.className.replace(/\b(light|dark)-theme\b/g, '') + ' ' + (isLight ? 'light-theme' : 'dark-theme')).trim();
      }

      if (isLight) {
        themeBtn.innerHTML = `🌙 <span class="mode-text">Dark</span>`;
        themeBtn.title = "Light mode active (High-contrast parchment). Click or press Alt+T for Dark obsidian mode.";
      } else {
        themeBtn.innerHTML = `☀️ <span class="mode-text">Light</span>`;
        themeBtn.title = "Dark mode active (Zingaran obsidian). Click or press Alt+T for Light parchment mode.";
      }
      safeStorage.setItem('okc_theme', AppState.theme);
    }

    themeBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (typeof window.__toggleTheme === 'function') {
        window.__toggleTheme();
        AppState.theme = document.documentElement.getAttribute('data-theme') || 'dark';
      } else {
        AppState.theme = AppState.theme === 'light' ? 'dark' : 'light';
        applyTheme();
      }
    });

    // Keyboard shortcut: Alt+T to toggle theme
    document.addEventListener('keydown', (e) => {
      if (e.altKey && (e.key === 't' || e.key === 'T')) {
        e.preventDefault();
        if (typeof window.__toggleTheme === 'function') {
          window.__toggleTheme();
          AppState.theme = document.documentElement.getAttribute('data-theme') || 'dark';
        } else {
          AppState.theme = AppState.theme === 'light' ? 'dark' : 'light';
          applyTheme();
        }
      }
    });

    applyTheme();
  }

  // =========================================================================
  // GM MODE & PLAYER-SAFE TOGGLE
  // =========================================================================
  function initModeToggle() {
    const modeBtn = document.getElementById('mode-toggle-btn');
    if (!modeBtn) return;

    function applyMode() {
      if (AppState.isPlayerSafe) {
        document.body.classList.add('player-safe-mode');
        modeBtn.classList.remove('gm-active');
        modeBtn.classList.add('player-active');
        modeBtn.innerHTML = `🛡️ <span class="mode-text">Player Safe Mode</span>`;
        modeBtn.title = "Player Safe Mode is active (Confidential GM notes and DCs are blurred). Click to switch to GM Mode.";
      } else {
        document.body.classList.remove('player-safe-mode');
        modeBtn.classList.remove('player-active');
        modeBtn.classList.add('gm-active');
        modeBtn.innerHTML = `👁️ <span class="mode-text">GM Secrets Mode</span>`;
        modeBtn.title = "GM Mode is active (All secret agendas, hidden levers, and DCs are visible). Click to switch to Player Safe Mode.";
      }
      safeStorage.setItem('okc_player_safe', AppState.isPlayerSafe);
    }

    modeBtn.addEventListener('click', () => {
      AppState.isPlayerSafe = !AppState.isPlayerSafe;
      applyMode();
    });

    // Delegated click event to temporarily unmask confidential elements when clicked in Player-Safe Mode
    document.addEventListener('click', (e) => {
      if (!AppState.isPlayerSafe) return;
      const target = e.target.closest('.gm-callout, .gm-only-cell, .dc-box, .escalation, .glance-item.dcs, th.gm-only-header');
      if (target) {
        target.classList.toggle('revealed');
      }
    });

    applyMode();
  }

  // =========================================================================
  // QUICK GM TOOLS: DICE ROLLER & PUNDONOR
  // =========================================================================
  function initTools() {
    const toolsBtn = document.getElementById('btn-tools-toggle');
    const toolsDrawer = document.getElementById('tools-drawer');
    const diceDisplay = document.getElementById('dice-result-display');

    if (!toolsBtn || !toolsDrawer) return;

    toolsBtn.addEventListener('click', () => {
      toolsDrawer.classList.toggle('open');
    });

    document.querySelectorAll('.dice-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const sides = parseInt(btn.getAttribute('data-die'), 10);
        const roll = Math.floor(Math.random() * sides) + 1;
        let flair = '';
        if (sides === 20) {
          if (roll === 20) flair = ' 🌟 CRITICAL!';
          else if (roll === 1) flair = ' 💀 BOTCH!';
        }
        diceDisplay.textContent = `d${sides}: ${roll}${flair}`;
      });
    });
  }

  // =========================================================================
  // ROUTING & NAVIGATION
  // =========================================================================
  function handleRoute() {
    let hash = window.location.hash.slice(1);
    if (!hash) {
      hash = 'overview/campaign-premise';
      window.location.hash = '#' + hash;
    }

    const parts = hash.split('/');
    let cat = parts[0];
    let id = parts[1];

    if (!id) {
      id = cat;
      const art = getArticle(id);
      if (art) cat = art.category;
    }

    AppState.currentCategory = cat;
    AppState.currentArticleId = id;

    if (cat === 'sessions') {
      renderSessionView();
    } else {
      const article = getArticle(id);
      renderArticle(article);
    }

    renderSidebar();
    closePreviewDrawer();
  }

  function closeSidebar() {
    const sb = document.getElementById('sidebar');
    if (sb) sb.classList.add('collapsed');
  }

  function toggleSidebar() {
    const sb = document.getElementById('sidebar');
    if (sb) sb.classList.toggle('collapsed');
  }

  function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // =========================================================================
  // INITIALIZATION
  // =========================================================================
  function boot() {
    initThemeToggle();
    initGlossary();
    initModeToggle();
    initSearch();
    initTools();

    // Sidebar Toggle
    document.getElementById('sidebar-toggle-btn')?.addEventListener('click', toggleSidebar);

    // Preview Drawer Close and Full-View buttons
    document.getElementById('drawer-close-btn')?.addEventListener('click', closePreviewDrawer);
    document.getElementById('drawer-open-full-btn')?.addEventListener('click', () => {
      const fullLink = document.getElementById('drawer-open-full-btn').getAttribute('data-target');
      if (fullLink) {
        window.location.hash = fullLink;
      }
    });

    // Session Modal Cancel & Save buttons
    document.getElementById('modal-session-cancel')?.addEventListener('click', closeAddSessionModal);
    document.getElementById('modal-session-save')?.addEventListener('click', saveNewSessionFromModal);

    // Hash routing & immediate initial render
    window.addEventListener('hashchange', handleRoute);
    handleRoute();

    // Load sessions asynchronously in background
    initSessions().then(() => {
      if (AppState.currentCategory === 'sessions') {
        renderSessionView();
      }
      renderSidebar();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

})();
