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

  function loadJsonStorage(key, fallback = []) {
    try {
      const val = safeStorage.getItem(key);
      return val ? JSON.parse(val) : fallback;
    } catch (e) {
      return fallback;
    }
  }

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
    sessions: [],
    customArticles: loadJsonStorage('okc_custom_articles', []),
    deletedArticleIds: loadJsonStorage('okc_deleted_articles', [])
  };
  window.AppState = AppState;

  function saveCustomArticles() {
    safeStorage.setItem('okc_custom_articles', JSON.stringify(AppState.customArticles));
  }

  function saveDeletedArticles() {
    safeStorage.setItem('okc_deleted_articles', JSON.stringify(AppState.deletedArticleIds));
  }

  // Dynamic Compendium Data Merge (Canonical + Custom Overrides - Deleted Articles)
  function getWikiData() {
    const base = window.WIKI_DATA || (typeof WIKI_DATA !== 'undefined' ? WIKI_DATA : null);
    if (!base) return null;

    const deletedSet = new Set(AppState.deletedArticleIds || []);
    const customMap = new Map();
    (AppState.customArticles || []).forEach(art => {
      if (art && art.id) customMap.set(art.id, art);
    });

    const mergedArticles = [];
    const handledIds = new Set();

    if (base.articles && Array.isArray(base.articles)) {
      base.articles.forEach(art => {
        if (deletedSet.has(art.id)) return;
        if (customMap.has(art.id)) {
          const custom = customMap.get(art.id);
          mergedArticles.push(Object.assign({}, art, custom, {
            _isCanonical: true,
            _isModified: true
          }));
          handledIds.add(art.id);
        } else {
          mergedArticles.push(art);
          handledIds.add(art.id);
        }
      });
    }

    (AppState.customArticles || []).forEach(art => {
      if (!art || !art.id) return;
      if (deletedSet.has(art.id)) return;
      if (!handledIds.has(art.id)) {
        mergedArticles.push(Object.assign({}, art, {
          _isCustom: true
        }));
        handledIds.add(art.id);
      }
    });

    return {
      meta: Object.assign({}, base.meta, {
        totalArticles: mergedArticles.length
      }),
      categories: base.categories || [],
      articles: mergedArticles
    };
  }
  window.getWikiData = getWikiData;

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

    // Custom or modified badge indicators
    let loreBadgeHtml = '';
    if (article._isCustom) {
      loreBadgeHtml = `<span class="badge-custom-lore">Custom Article</span>`;
    } else if (article._isModified) {
      loreBadgeHtml = `<span class="badge-modified-lore">Locally Modified</span>`;
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
          <div class="article-header-top">
            <span class="article-category-badge">${catObj.name}</span>
            <div class="article-header-actions">
              ${loreBadgeHtml}
              <button id="btn-edit-current-article" class="btn-edit-article" title="Edit this article in the live compendium editor">
                ✏️ Edit Article
              </button>
            </div>
          </div>
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

    // Attach click listener for Edit button
    document.getElementById('btn-edit-current-article')?.addEventListener('click', () => {
      openArticleEditor(article.id);
    });

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
          ${g.classLevel ? `<div class="glance-item" style="grid-column: 1 / -1; background: var(--bg-surface); border-left: 3px solid var(--accent-gold); padding: 8px 12px; border-radius: var(--radius-sm);"><strong>⚔️ Labyrinth Lord:</strong> <span style="color: var(--accent-gold); font-weight: 700;">${g.classLevel}</span>${g.combatStats ? ` &bull; <span style="font-family: var(--font-mono); font-size: 0.85rem;">${g.combatStats}</span>` : ''}</div>` : ''}
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

  function slugify(text) {
    return text.toString().toLowerCase().trim()
      .replace(/\s+/g, '-')
      .replace(/[^\w\-]+/g, '')
      .replace(/\-\-+/g, '-')
      .replace(/^-+/, '')
      .replace(/-+$/, '');
  }

  // =========================================================================
  // TOAST NOTIFICATIONS
  // =========================================================================
  function showToast(message, type = 'info', duration = 3500) {
    const container = document.getElementById('toast-notification');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-message ${type === 'success' ? 'toast-success' : (type === 'error' ? 'toast-error' : '')}`;

    let icon = 'ℹ️';
    if (type === 'success') icon = '✅';
    if (type === 'error') icon = '⚠️';

    toast.innerHTML = `<span>${icon}</span> <span>${escapeHtml(message)}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transition = 'opacity 0.3s ease';
      setTimeout(() => {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }, 300);
    }, duration);
  }

  // =========================================================================
  // IN-BROWSER ARTICLE EDITOR ENGINE
  // =========================================================================
  function initArticleEditor() {
    const editModal = document.getElementById('modal-article-edit');
    const closeBtn = document.getElementById('modal-editor-close-btn');
    const cancelBtn = document.getElementById('modal-editor-cancel-btn');
    const saveBtn = document.getElementById('modal-editor-save-btn');
    const deleteBtn = document.getElementById('modal-editor-delete-btn');
    const titleInput = document.getElementById('editor-article-title');
    const idInput = document.getElementById('editor-article-id');
    const origIdInput = document.getElementById('editor-original-id');
    const contentTextarea = document.getElementById('editor-article-content');
    const quickTagsContainer = document.getElementById('editor-quick-tags');

    if (!editModal) return;

    closeBtn?.addEventListener('click', closeArticleEditor);
    cancelBtn?.addEventListener('click', closeArticleEditor);
    saveBtn?.addEventListener('click', saveArticleFromEditor);
    deleteBtn?.addEventListener('click', deleteOrRevertArticleFromEditor);

    // Auto-generate slug ID when typing title for brand new articles
    titleInput?.addEventListener('input', () => {
      if (!origIdInput.value) {
        idInput.value = slugify(titleInput.value);
      }
    });

    // Allow Tab key inside content textarea for indentation
    contentTextarea?.addEventListener('keydown', (e) => {
      if (e.key === 'Tab') {
        e.preventDefault();
        const start = contentTextarea.selectionStart;
        const end = contentTextarea.selectionEnd;
        contentTextarea.setRangeText('  ', start, end, 'end');
      }
    });

    // Quick tag insertion toolbar
    quickTagsContainer?.querySelectorAll('.tag-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const tag = btn.getAttribute('data-tag');
        insertTagIntoEditor(tag, contentTextarea);
      });
    });

    // Sidebar New Article button
    document.getElementById('btn-new-article-sidebar')?.addEventListener('click', () => {
      openArticleEditor(null);
    });
  }

  function insertTagIntoEditor(tagType, textarea) {
    if (!textarea) return;
    textarea.focus();
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const selectedText = textarea.value.substring(start, end);

    let replacement = '';
    switch (tagType) {
      case 'p':
        replacement = `<p>${selectedText || 'New paragraph text...'}</p>`;
        break;
      case 'h3':
        replacement = `<h3>${selectedText || 'Section Heading'}</h3>`;
        break;
      case 'h4':
        replacement = `<h4>${selectedText || 'Subheading'}</h4>`;
        break;
      case 'strong':
        replacement = `<strong>${selectedText || 'bold text'}</strong>`;
        break;
      case 'em':
        replacement = `<em>${selectedText || 'italic text'}</em>`;
        break;
      case 'ul':
        replacement = `<ul>\n  <li>${selectedText || 'First item'}</li>\n  <li>Second item</li>\n</ul>`;
        break;
      case 'gm-callout':
        replacement = `\n<div class="gm-callout">\n  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET LEVER</div>\n  <p>${selectedText || 'Confidential agendas, blackmail material, or unrevealed truths...'}</p>\n</div>\n`;
        break;
      case 'dc-box':
        replacement = `\n<div class="dc-box">\n  <span class="dc-tag">DC 15 Society</span>\n  <span>${selectedText || 'Skill check description and consequence of success or failure.'}</span>\n</div>\n`;
        break;
      case 'escalation':
        replacement = `\n<div class="escalation">\n  <strong>Escalation / Event:</strong> ${selectedText || 'Sudden complication, ambush, or political deadline.'}\n</div>\n`;
        break;
      case 'rule-box':
        replacement = `\n<div class="rule-box">\n  <div class="rule-header">MECHANICS &bull; TITLE</div>\n  <p>${selectedText || 'Rule mechanics description, modifiers, and tactical applications.'}</p>\n</div>\n`;
        break;
      case 'info-card':
        replacement = `\n<div class="info-card">\n  <h4>${selectedText || 'Card Title'}</h4>\n  <p>Detailed breakdown or quick reference notes.</p>\n</div>\n`;
        break;
      default:
        replacement = selectedText;
    }

    textarea.setRangeText(replacement, start, end, 'select');
    textarea.dispatchEvent(new Event('input'));
  }

  function openArticleEditor(articleId = null) {
    const editModal = document.getElementById('modal-article-edit');
    const deleteBtn = document.getElementById('modal-editor-delete-btn');
    const modeBadge = document.getElementById('editor-mode-badge');
    const modalTitle = document.getElementById('editor-modal-title');
    const idInput = document.getElementById('editor-article-id');

    if (!editModal) return;

    if (articleId) {
      const art = getArticle(articleId);
      if (!art) {
        showToast('Article not found to edit', 'error');
        return;
      }

      document.getElementById('editor-original-id').value = art.id;
      idInput.value = art.id;
      idInput.readOnly = true;
      idInput.style.opacity = '0.7';

      document.getElementById('editor-article-title').value = art.title || '';
      document.getElementById('editor-article-category').value = art.category || 'overview';
      document.getElementById('editor-article-subtitle').value = art.subtitle || '';
      document.getElementById('editor-article-tags').value = (art.tags || []).join(', ');
      document.getElementById('editor-article-aliases').value = (art.aliases || []).join(', ');
      document.getElementById('editor-article-summary').value = art.summary || '';

      document.getElementById('editor-glance-appearance').value = art.atAGlance?.appearance || '';
      document.getElementById('editor-glance-mannerisms').value = art.atAGlance?.mannerisms || '';
      document.getElementById('editor-glance-quote').value = art.atAGlance?.quote || '';
      document.getElementById('editor-glance-dcs').value = art.atAGlance?.courtDCs || '';

      document.getElementById('editor-article-gm-secrets').value = art.gmSecrets || '';
      document.getElementById('editor-article-related').value = (art.relatedIds || []).join(', ');
      document.getElementById('editor-article-content').value = art.content || '';

      modalTitle.textContent = `Edit: ${art.title}`;
      deleteBtn.style.display = 'inline-block';
      if (art._isCustom) {
        deleteBtn.textContent = '🗑️ Delete Custom Article';
        modeBadge.textContent = 'Custom Article';
        modeBadge.className = 'badge-status badge-gold';
      } else if (art._isModified) {
        deleteBtn.textContent = '↺ Revert to Canonical Lore';
        modeBadge.textContent = 'Modified Canonical';
        modeBadge.className = 'badge-status';
      } else {
        deleteBtn.textContent = '🗑️ Hide / Delete from Wiki';
        modeBadge.textContent = 'Canonical Lore';
        modeBadge.className = 'badge-status';
      }
    } else {
      // New Article
      document.getElementById('editor-original-id').value = '';
      idInput.value = '';
      idInput.readOnly = false;
      idInput.style.opacity = '1';

      document.getElementById('editor-article-title').value = '';
      document.getElementById('editor-article-category').value = AppState.currentCategory !== 'sessions' ? AppState.currentCategory : 'overview';
      document.getElementById('editor-article-subtitle').value = '';
      document.getElementById('editor-article-tags').value = '';
      document.getElementById('editor-article-aliases').value = '';
      document.getElementById('editor-article-summary').value = '';

      document.getElementById('editor-glance-appearance').value = '';
      document.getElementById('editor-glance-mannerisms').value = '';
      document.getElementById('editor-glance-quote').value = '';
      document.getElementById('editor-glance-dcs').value = '';

      document.getElementById('editor-article-gm-secrets').value = '';
      document.getElementById('editor-article-related').value = '';
      document.getElementById('editor-article-content').value = '<p>Write article content here...</p>';

      modalTitle.textContent = 'Create New Compendium Article';
      deleteBtn.style.display = 'none';
      modeBadge.textContent = 'New Entry';
      modeBadge.className = 'badge-status badge-gold';
    }

    editModal.style.display = 'flex';
    document.getElementById('editor-article-title').focus();
  }

  function closeArticleEditor() {
    const editModal = document.getElementById('modal-article-edit');
    if (editModal) editModal.style.display = 'none';
  }

  function saveArticleFromEditor() {
    const title = document.getElementById('editor-article-title').value.trim();
    let id = document.getElementById('editor-article-id').value.trim();
    const category = document.getElementById('editor-article-category').value;
    const subtitle = document.getElementById('editor-article-subtitle').value.trim();
    const tagsRaw = document.getElementById('editor-article-tags').value;
    const aliasesRaw = document.getElementById('editor-article-aliases').value;
    const summary = document.getElementById('editor-article-summary').value.trim();
    const content = document.getElementById('editor-article-content').value.trim();
    const gmSecrets = document.getElementById('editor-article-gm-secrets').value.trim();
    const relatedRaw = document.getElementById('editor-article-related').value;

    const appearance = document.getElementById('editor-glance-appearance').value.trim();
    const mannerisms = document.getElementById('editor-glance-mannerisms').value.trim();
    const quote = document.getElementById('editor-glance-quote').value.trim();
    const courtDCs = document.getElementById('editor-glance-dcs').value.trim();

    if (!title) {
      alert('Please provide an article title.');
      document.getElementById('editor-article-title').focus();
      return;
    }

    if (!id) {
      id = slugify(title);
    }

    if (!content) {
      alert('Please write article content.');
      document.getElementById('editor-article-content').focus();
      return;
    }

    const tags = tagsRaw.split(',').map(s => s.trim()).filter(Boolean);
    const aliases = aliasesRaw.split(',').map(s => s.trim()).filter(Boolean);
    const relatedIds = relatedRaw.split(',').map(s => s.trim()).filter(Boolean);

    const articleObj = {
      id: id,
      category: category,
      title: title,
      subtitle: subtitle,
      tags: tags,
      aliases: aliases,
      summary: summary || title,
      content: content,
      gmSecrets: gmSecrets,
      relatedIds: relatedIds
    };

    if (appearance || mannerisms || quote || courtDCs) {
      articleObj.atAGlance = {
        appearance: appearance,
        mannerisms: mannerisms,
        quote: quote,
        courtDCs: courtDCs
      };
    }

    const existingBase = getArticle(id);
    if (existingBase && existingBase.atAGlance) {
      if (existingBase.atAGlance.classLevel || existingBase.atAGlance.combatStats) {
        if (!articleObj.atAGlance) articleObj.atAGlance = {};
        if (existingBase.atAGlance.classLevel) articleObj.atAGlance.classLevel = existingBase.atAGlance.classLevel;
        if (existingBase.atAGlance.combatStats) articleObj.atAGlance.combatStats = existingBase.atAGlance.combatStats;
      }
    }

    // Save into AppState.customArticles
    const existingIdx = AppState.customArticles.findIndex(a => a.id === id);
    if (existingIdx !== -1) {
      AppState.customArticles[existingIdx] = articleObj;
    } else {
      AppState.customArticles.push(articleObj);
    }

    // Ensure it's removed from deleted list if previously deleted
    AppState.deletedArticleIds = AppState.deletedArticleIds.filter(delId => delId !== id);

    saveCustomArticles();
    saveDeletedArticles();

    // Re-initialize dynamic subsystems
    initGlossary();
    closeArticleEditor();

    // Navigate to edited article
    window.location.hash = `#${category}/${id}`;
    handleRoute();

    showToast(`Saved "${title}" to compendium!`, 'success');
  }

  function deleteOrRevertArticleFromEditor() {
    const origId = document.getElementById('editor-original-id').value;
    if (!origId) return;

    const art = getArticle(origId);
    const isCustom = art && art._isCustom;
    const isModified = art && art._isModified;

    const actionName = isCustom ? 'delete this custom article' : (isModified ? 'revert this article to canonical lore' : 'hide this article from the compendium');
    if (!confirm(`Are you sure you want to ${actionName}?`)) {
      return;
    }

    if (isCustom || isModified) {
      AppState.customArticles = AppState.customArticles.filter(a => a.id !== origId);
      saveCustomArticles();
    } else {
      if (!AppState.deletedArticleIds.includes(origId)) {
        AppState.deletedArticleIds.push(origId);
        saveDeletedArticles();
      }
    }

    initGlossary();
    closeArticleEditor();

    if (isModified) {
      showToast(`Reverted "${art.title}" to original lore!`, 'info');
      handleRoute();
    } else {
      showToast(`Article removed from wiki.`, 'info');
      window.location.hash = '#overview/campaign-premise';
    }
  }

  // =========================================================================
  // COMPENDIUM SYNC & CLOUD EXPORT ENGINE
  // =========================================================================
  function initSyncEngine() {
    const syncModal = document.getElementById('modal-sync-export');
    const closeBtn = document.getElementById('modal-sync-close-btn');
    const closeFooterBtn = document.getElementById('modal-sync-close-footer');

    closeBtn?.addEventListener('click', closeSyncModal);
    closeFooterBtn?.addEventListener('click', closeSyncModal);

    // Header & Sidebar sync triggers
    document.getElementById('btn-sync-export-top')?.addEventListener('click', openSyncModal);
    document.getElementById('btn-sync-sidebar')?.addEventListener('click', openSyncModal);

    // Download & Save options
    document.getElementById('btn-download-datajs')?.addEventListener('click', downloadDataJs);
    document.getElementById('btn-direct-save-disk')?.addEventListener('click', directSaveDataJsToDisk);

    // GitHub Sync
    document.getElementById('btn-github-commit')?.addEventListener('click', pushCommitToGitHub);

    // JSON Backup / Restore / Reset
    document.getElementById('btn-export-edits-json')?.addEventListener('click', exportEditsBackupJSON);
    document.getElementById('btn-import-edits-json')?.addEventListener('click', () => {
      document.getElementById('input-import-edits-file')?.click();
    });
    document.getElementById('input-import-edits-file')?.addEventListener('change', importEditsBackupJSON);
    document.getElementById('btn-reset-edits')?.addEventListener('click', resetAllCustomEdits);
  }

  function openSyncModal() {
    const modal = document.getElementById('modal-sync-export');
    if (!modal) return;

    // Load saved GitHub credentials
    const patInput = document.getElementById('github-pat-input');
    const repoInput = document.getElementById('github-repo-input');
    const branchInput = document.getElementById('github-branch-input');

    if (patInput) patInput.value = safeStorage.getItem('okc_github_pat', '');
    if (branchInput) branchInput.value = safeStorage.getItem('okc_github_branch', 'main');

    let savedRepo = safeStorage.getItem('okc_github_repo', '');
    if (!savedRepo && window.location.hostname.endsWith('github.io')) {
      const parts = window.location.pathname.split('/').filter(Boolean);
      const owner = window.location.hostname.split('.')[0];
      const repo = parts[0] || '';
      if (owner && repo) savedRepo = `${owner}/${repo}`;
    }
    if (repoInput) repoInput.value = savedRepo;

    const statusEl = document.getElementById('github-sync-status');
    if (statusEl) statusEl.innerHTML = '';

    modal.style.display = 'flex';
  }

  function closeSyncModal() {
    const modal = document.getElementById('modal-sync-export');
    if (modal) modal.style.display = 'none';
  }

  function generateCompendiumDataJs() {
    const data = getWikiData();
    if (!data) return '';

    // Strip internal runtime flags for pristine data file
    const cleanArticles = data.articles.map(a => {
      const copy = Object.assign({}, a);
      delete copy._isCanonical;
      delete copy._isModified;
      delete copy._isCustom;
      return copy;
    });

    const exportObj = {
      meta: {
        title: data.meta.title || "Our Kingdom Come",
        subtitle: data.meta.subtitle || "Zingara Sandbox Campaign & GM Intrigue Compendium",
        epoch: data.meta.epoch || "Period VIII: The Besieged Kingdom",
        totalArticles: cleanArticles.length,
        lastUpdated: new Date().toISOString()
      },
      categories: data.categories,
      articles: cleanArticles
    };

    const serialized = JSON.stringify(exportObj, null, 2);

    return `// Our Kingdom Come - Zingara Sandbox GM Compendium Data\n// Auto-compiled from canonical source documents and GM in-browser updates\n\nwindow.WIKI_DATA = ${serialized};\n\nvar WIKI_DATA = window.WIKI_DATA;\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = WIKI_DATA;\n}\n`;
  }
  window.generateCompendiumDataJs = generateCompendiumDataJs;
  window.openArticleEditor = openArticleEditor;
  window.openSyncModal = openSyncModal;

  function downloadDataJs() {
    const content = generateCompendiumDataJs();
    downloadBlob(content, 'data.js', 'application/javascript');
    showToast('Downloaded updated data.js!', 'success');
  }

  async function directSaveDataJsToDisk() {
    const content = generateCompendiumDataJs();
    if ('showSaveFilePicker' in window) {
      try {
        const handle = await window.showSaveFilePicker({
          suggestedName: 'data.js',
          types: [{
            description: 'JavaScript Compendium (*.js)',
            accept: { 'application/javascript': ['.js'] }
          }]
        });
        const writable = await handle.createWritable();
        await writable.write(content);
        await writable.close();
        showToast('Directly saved to data.js on disk!', 'success');
        return;
      } catch (err) {
        if (err.name === 'AbortError') return;
        console.warn('showSaveFilePicker error, falling back to download', err);
      }
    }
    // Fallback if browser doesn't support or encountered error
    downloadBlob(content, 'data.js', 'application/javascript');
    showToast('Browser downloaded updated data.js', 'info');
  }

  function downloadBlob(content, filename, mimeType) {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, 100);
  }

  function utf8ToBase64(str) {
    const bytes = new TextEncoder().encode(str);
    let binary = '';
    for (let i = 0; i < bytes.length; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    return btoa(binary);
  }

  async function pushCommitToGitHub() {
    const patInput = document.getElementById('github-pat-input');
    const repoInput = document.getElementById('github-repo-input');
    const branchInput = document.getElementById('github-branch-input');
    const commitMsgInput = document.getElementById('github-commit-msg');
    const statusEl = document.getElementById('github-sync-status');

    const pat = patInput.value.trim();
    const repo = repoInput.value.trim();
    const branch = branchInput.value.trim() || 'main';
    const commitMsg = commitMsgInput.value.trim() || 'Update Zingara compendium lore from GM in-browser editor';

    if (!pat) {
      alert('Please enter your GitHub Personal Access Token (PAT).');
      patInput.focus();
      return;
    }
    if (!repo || !repo.includes('/')) {
      alert('Please enter your repository in owner/repo format (e.g. username/Our-Kingdom-Come).');
      repoInput.focus();
      return;
    }

    // Save config in localStorage
    safeStorage.setItem('okc_github_pat', pat);
    safeStorage.setItem('okc_github_repo', repo);
    safeStorage.setItem('okc_github_branch', branch);

    statusEl.className = 'sync-status-display loading';
    statusEl.innerHTML = '⏳ Contacting GitHub API...';

    try {
      const filePath = 'js/data.js';
      const apiUrl = `https://api.github.com/repos/${repo}/contents/${filePath}?ref=${encodeURIComponent(branch)}`;

      // Step 1: Get current file sha if file exists
      let currentSha = null;
      const getRes = await fetch(apiUrl, {
        headers: {
          'Authorization': `Bearer ${pat}`,
          'Accept': 'application/vnd.github.v3+json'
        }
      });

      if (getRes.ok) {
        const fileInfo = await getRes.json();
        currentSha = fileInfo.sha;
      } else if (getRes.status !== 404) {
        const errData = await getRes.json().catch(() => ({}));
        throw new Error(errData.message || `GitHub error (Status ${getRes.status})`);
      }

      statusEl.innerHTML = '⏳ Committing updated compendium...';

      // Step 2: Push commit with base64 content
      const contentStr = generateCompendiumDataJs();
      const base64Content = utf8ToBase64(contentStr);

      const putBody = {
        message: commitMsg,
        content: base64Content,
        branch: branch
      };
      if (currentSha) {
        putBody.sha = currentSha;
      }

      const putRes = await fetch(`https://api.github.com/repos/${repo}/contents/${filePath}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${pat}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(putBody)
      });

      if (!putRes.ok) {
        const errData = await putRes.json().catch(() => ({}));
        throw new Error(errData.message || `Commit failed with status ${putRes.status}`);
      }

      statusEl.className = 'sync-status-display success';
      statusEl.innerHTML = `✅ Successfully committed to <strong>${escapeHtml(branch)}</strong>!`;
      showToast(`Pushed compendium to GitHub (${branch})!`, 'success');
    } catch (err) {
      console.error('GitHub Sync Error:', err);
      statusEl.className = 'sync-status-display error';
      statusEl.innerHTML = `❌ Error: ${escapeHtml(err.message)}`;
      showToast(`GitHub commit failed: ${err.message}`, 'error');
    }
  }

  function exportEditsBackupJSON() {
    const backup = {
      exportVersion: 1,
      exportedAt: new Date().toISOString(),
      customArticles: AppState.customArticles,
      deletedArticleIds: AppState.deletedArticleIds
    };
    const content = JSON.stringify(backup, null, 2);
    downloadBlob(content, 'okc_compendium_edits.json', 'application/json');
    showToast('Exported custom edits backup JSON', 'success');
  }

  function importEditsBackupJSON(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
      try {
        const data = JSON.parse(e.target.result);
        if (data && Array.isArray(data.customArticles)) {
          AppState.customArticles = data.customArticles;
          AppState.deletedArticleIds = Array.isArray(data.deletedArticleIds) ? data.deletedArticleIds : [];
          saveCustomArticles();
          saveDeletedArticles();
          initGlossary();
          renderSidebar();
          handleRoute();
          closeSyncModal();
          showToast('Custom edits restored successfully!', 'success');
        } else {
          alert('Invalid backup JSON format. Missing customArticles array.');
        }
      } catch (err) {
        alert('Failed to parse JSON file: ' + err.message);
      }
    };
    reader.readAsText(file);
  }

  function resetAllCustomEdits() {
    if (!confirm('Are you sure you want to revert ALL custom and modified articles back to canonical lore? This cannot be undone unless you exported a backup.')) {
      return;
    }
    AppState.customArticles = [];
    AppState.deletedArticleIds = [];
    saveCustomArticles();
    saveDeletedArticles();
    initGlossary();
    renderSidebar();
    handleRoute();
    closeSyncModal();
    showToast('Compendium restored to original canonical lore!', 'info');
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
    initArticleEditor();
    initSyncEngine();

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
