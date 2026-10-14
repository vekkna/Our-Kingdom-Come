# Our Kingdom Come — Zingara GM Wiki & Campaign Compendium

An ultra-fast, zero-dependency, tablet-optimized wiki-style web application built for Game Masters running the *Our Kingdom Come* sword-and-sorcery sandbox campaign set in ancient Zingara (Period VIII: The Besieged Kingdom).

Built with pure vanilla **HTML5**, **CSS3**, and **JavaScript** (separate modular files) designed for instantaneous loading, high legibility at the gaming table, and zero build step.

---

## ⚡ Key Features for Live Play

1. **Instant Client-Side Live Search (`/` or `Ctrl+K`):**
   - Sub-millisecond fuzzy search across all 67 articles, NPC dossiers, skill check DCs, secret agendas, and historical periods.
   - Use the arrow keys, `Enter` to jump, or `Escape` to close.

2. **Automatic Dynamic Hyperlinking & Side-Drawer Previews:**
   - Mentions of NPCs, factions, places, relics, and rules are automatically hyperlinked throughout every article.
   - **Zero Context Loss:** Tapping any hyperlinked name opens a slide-out preview drawer on the right with the entity's quick card, court DCs, mannerisms, and secret levers—without losing your reading position on the main screen.
   - Tap *"Open Full Article"* in the drawer to navigate directly to the full entry.

3. **GM Secrets Mode vs. Player Safe Mode:**
   - Easily accessible toggle in the top header (`👁️ GM Secrets Mode` / `🛡️ Player Safe Mode`).
   - In **Player Safe Mode**, confidential GM callouts, secret agendas, betrayal triggers, and DC blocks are blurred with an unobtrusive *"Confidential GM Data (Click to peek)"* indicator. You can safely project or hand your tablet to players to show lore, public bios, or maps!

4. **Session Log & Campaign Tracker:**
   - Dedicated Session Log view to chronicle royal edicts, court intrigues, and session summaries.
   - Tracks **Crown Sovereignty Points**, **Pundonor Status**, **Active Plot Leads**, and **NPC Dispositions**.
   - Auto-saves to browser `localStorage` during play.
   - Includes one-click **"Export JSON"** (to save directly into `data/sessions.json` and commit to Git) and **"Download Markdown"** (for sharing recaps).

5. **Quick Table GM Tools:**
   - Built-in table dice roller (`d4`, `d6`, `d8`, `d10`, `d12`, `d20`, `d100` with critical hit and botch detection).
   - Fast Pundonor & Command Friction rule summaries.

6. **Tablet & Mobile Optimized:**
   - Large touch targets (minimum 44px) for rapid finger navigation.
   - Collapsible slide-out navigation tree (`☰`).
   - High-contrast Decadent Zingaran Gothic theme designed for low-fatigue reading in dim gaming rooms.

---

## 🚀 Hosting on GitHub Pages

This repository is pre-configured for static hosting on GitHub Pages with **zero build step**:

1. Push this repository to GitHub.
2. In your GitHub repository, navigate to **Settings** &rarr; **Pages**.
3. Under **Build and deployment**:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/ (root)`
4. Click **Save**.
5. Within 1–2 minutes, your live site URL will be ready at:
   `https://<your-username>.github.io/<repo-name>/`

---

## 📝 Updating After Play Sessions

To update your campaign records after a game session:

### Method A (Through the Web UI):
1. Open the site and click **📖 Sessions** in the header.
2. Click **+ Log New Session** and fill in your session recap, in-game calendar date, and sovereignty/pundonor shifts.
3. Click **Export JSON** to download the updated `sessions.json` file.
4. Replace the `data/sessions.json` file in this repository.
5. Commit and push to Git:
   ```bash
   git add data/sessions.json
   git commit -m "Log session recap"
   git push
   ```

### Method B (Direct File Edit):
Open `data/sessions.json` in any text editor, add your new session object, and commit directly to Git.

---

## 📂 Project Architecture

```
Our Kingdom Come/
├── index.html                 # Semantic SPA HTML shell
├── css/
│   └── style.css              # Decadent Zingaran Gothic styling (Speed & clarity first)
├── js/
│   ├── app.js                 # Router, auto-linker, live search, drawer & session engine
│   └── data.js                # Structured encyclopedia (67 articles, dossiers & rules)
├── data/
│   └── sessions.json          # Campaign session logs & starting state (Session 0)
├── build_data.py              # Optional Python compilation script for rebuilding data.js
├── Campaign Setting.docx      # Canonical campaign setting guide
├── Royal Court NPCs.docx      # Canonical court dossiers and plot hooks
├── Zingara map.jpg            # High-resolution regional map of Zingara
└── README.md                  # Documentation and hosting guide
```
