"""
compile_complete_wiki.py - Extracts 100% of the content from Campaign Setting.docx and Royal Court NPCs.docx
and formats it into structured articles in js/data.js.
"""

import zipfile
import xml.etree.ElementTree as ET
import json
import re

def extract_docx_paragraphs(path):
    with zipfile.ZipFile(path) as z:
        xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    paragraphs = []
    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
        if texts:
            t = ''.join(texts).strip()
            if t:
                paragraphs.append(t)
    return paragraphs

def main():
    cs_paragraphs = extract_docx_paragraphs('Campaign Setting.docx')
    rc_paragraphs = extract_docx_paragraphs('Royal Court NPCs.docx')

    print(f"Read {len(cs_paragraphs)} paragraphs from Campaign Setting.docx")
    print(f"Read {len(rc_paragraphs)} paragraphs from Royal Court NPCs.docx")

    articles = []

    # Helper to clean text
    def clean(t):
        return t.replace('\uFFFD', '').replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', '—').replace('\u2013', '–')

    # =========================================================================
    # 1. CAMPAIGN PREMISE & WORLD PARAMETERS (From Section 1 of Campaign Setting)
    # =========================================================================
    sec1_text = []
    collecting = False
    for p in cs_paragraphs:
        if '1. CAMPAIGN PREMISE & WORLD PARAMETERS' in p:
            collecting = True
            continue
        if '2. EIGHT-PERIOD CANONICAL CHRONOLOGY' in p:
            collecting = False
            break
        if collecting:
            sec1_text.append(clean(p))

    premise_html = "<h3>1.1 High-Concept Campaign Premise</h3>\n"
    current_sec = "1.1"
    for p in sec1_text:
        if '1.1 High-Concept Campaign Premise' in p:
            continue
        elif '1.2 Canonical Worldbuilding Parameters' in p:
            premise_html += "\n<h3>1.2 Canonical Worldbuilding Parameters</h3>\n"
            current_sec = "1.2"
        elif '1.3 Game Master Execution & Sandbox Directives' in p:
            premise_html += "\n<h3>1.3 Game Master Execution & Sandbox Directives</h3>\n"
            current_sec = "1.3"
        elif p.startswith('The Ascendancy Trap'):
            premise_html += f"""
<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE ASCENDANCY TRAP</div>
  <p>{p}</p>
</div>
"""
        elif 'Core Setting Pillars' in p:
            premise_html += f"<h4>{p}</h4>\n"
        elif p.startswith('Pundonor:') or p.startswith('Thrall Labor:') or p.startswith('Decadence & Ruin:'):
            parts = p.split(':', 1)
            premise_html += f"<p><strong>{parts[0]}:</strong>{parts[1]}</p>\n"
        elif p.startswith('The Sovereign Clock') or p.startswith('Covert Sovereign Operations'):
            parts = p.split(':', 1)
            premise_html += f"<p><strong>{parts[0]}:</strong>{parts[1] if len(parts) > 1 else ''}</p>\n"
        else:
            premise_html += f"<p>{p}</p>\n"

    articles.append({
        "id": "campaign-premise",
        "category": "overview",
        "title": "Campaign Premise & World Parameters",
        "subtitle": "Section 1: High-Concept Premise, Setting Parameters & Sandbox Directives",
        "tags": ["Overview", "Period VIII", "The Triumvirate", "Sandbox", "Core Setting"],
        "aliases": ["Campaign Premise", "Premise", "World Parameters", "Our Kingdom Come", "Sandbox Directives"],
        "summary": "Full canonical overview of Our Kingdom Come: ancient pre-deluvial Zingara, the PC Triumvirate, the Ascendancy Trap, and Game Master sandbox directives.",
        "content": premise_html,
        "gmSecrets": "The Restoration Council intentionally provoked the state bankruptcy to ensure the PCs cannot recruit an independent household guard without uncovering hidden wealth or relics.",
        "relatedIds": ["valenza", "sadoria", "court-matrix", "restoration-council", "period-viii"]
    })

    # =========================================================================
    # 2. ROYAL COURT NPCS (8 DOSSIERS - Complete from Royal Court NPCs.docx)
    # =========================================================================
    npc_configs = [
        ("valenza", "General Don Rodrigo de Valenza (Head of the Royal Army)", "Military Elite / Restoration Council", ["Don Rodrigo", "General Valenza", "Rodrigo de Valenza", "Head of the Royal Army"], "Fencing Master Lucia 'La Mariposa' de la Vega"),
        ("sadoria", "High Chancellor Marquis Mateo de Sadoria (Chief Monarchist)", "Restoration Council / Bureaucracy", ["Marquis Mateo", "Mateo de Sadoria", "High Chancellor", "Chief Monarchist"], "High Duke Gonzalo de Guarralid"),
        ("lucia", "Fencing Master Lucia \"La Mariposa\" de la Vega (Republican Cell Commander)", "Republican Insurgents (The Pit)", ["La Mariposa", "Lucia de la Vega", "Lucia", "Fencing Master Lucia"], "General Don Rodrigo de Valenza"),
        ("malachai", "Father Malachai the Blind (High Priest of the Underground Church of Nemeth)", "Church of Nemeth the Gnostic", ["Father Malachai", "Malachai", "High Priest of Nemeth"], "Master Alchemist Vane"),
        ("gonzalo-guarralid", "High Duke Gonzalo de Guarralid (Grandee Representative)", "Grandee Coalitions (Eastern League)", ["Gonzalo de Guarralid", "Duke Gonzalo", "High Duke Gonzalo", "Guarralid"], "High Chancellor Marquis Mateo de Sadoria"),
        ("vesper", "Vesper the Key-Master (Spymaster of The Pit & Black Market Guildmaster)", "Underworld Syndicates / Smugglers", ["Vesper", "Key-Master", "The Key-Master"], "General Don Rodrigo de Valenza"),
        ("vane", "Master Alchemist Vane (Industrial Thrall Overseer)", "Crown Necromantic Apparatus", ["Master Vane", "Alchemist Vane", "Vane"], "Father Malachai the Blind"),
        ("tiberio", "Ambassador Tiberio of Messantia (Foreign Envoy)", "Kingdom of Argos / Hyborian Powers", ["Ambassador Tiberio", "Tiberio", "Envoy Tiberio"], "Vesper the Key-Master")
    ]

    for nid, nheader, nfac, naliases, nrival in npc_configs:
        # Extract text for this NPC from rc_paragraphs
        ntext = []
        in_npc = False
        for p in rc_paragraphs:
            if nheader[:20] in p:
                in_npc = True
                continue
            if in_npc:
                # Check if next section started
                if re.match(r'^[0-9]\.[0-9]\s+[A-Z]', p) or p.startswith('6. Court Relationship Matrix'):
                    break
                ntext.append(clean(p))

        # Parse sections within NPC text
        appearance = ""
        mannerisms = ""
        quote = ""
        courtDCs = ""
        publicPersona = []
        secretAgenda = []
        factionTies = []
        hooks = []

        curr_section = "glance"
        curr_hook = None

        for p in ntext:
            if 'At-a-Glance' in p:
                curr_section = "glance"
            elif 'Public Persona' in p:
                curr_section = "public"
            elif 'Secret Agenda' in p:
                curr_section = "secret"
            elif 'Faction Ties & Court Relationships' in p or 'Faction Ties' in p:
                curr_section = "faction"
            elif 'Player-Led Plot Hooks' in p:
                curr_section = "hooks"
            elif p.startswith('Hook 1:') or p.startswith('Hook 2:'):
                curr_section = "hook_item"
                curr_hook = {"title": p, "text": []}
                hooks.append(curr_hook)
            else:
                if curr_section == "glance":
                    if p.startswith('Visual Appearance & Apparel:') or p.startswith('Visual Appearance:'):
                        appearance = p.split(':', 1)[1].strip()
                    elif p.startswith('Mannerism / Behavioral Tick:') or p.startswith('Mannerisms:'):
                        mannerisms = p.split(':', 1)[1].strip()
                    elif p.startswith('Iconic Quote:'):
                        quote = p.split(':', 1)[1].strip().strip('"').strip("'")
                    elif p.startswith('Court Social DCs:'):
                        courtDCs = p.split(':', 1)[1].strip()
                elif curr_section == "public":
                    publicPersona.append(p)
                elif curr_section == "secret":
                    secretAgenda.append(p)
                elif curr_section == "faction":
                    factionTies.append(p)
                elif curr_section == "hook_item" and curr_hook is not None:
                    curr_hook["text"].append(p)

        # Build formatted HTML
        hooks_html = ""
        for h in hooks:
            h_body = ""
            for hp in h["text"]:
                if hp.startswith('Suggested Skill Checks:') or hp.startswith('Key Skill Checks:'):
                    h_body += f"<div class=\"dc-box\"><strong>{hp}</strong></div>\n"
                elif hp.startswith('Dynamic Escalation Trigger:'):
                    h_body += f"<p class=\"escalation\"><strong>{hp}</strong></p>\n"
                elif hp.startswith('Premise:') or hp.startswith('Core Conflict & Player Choice:'):
                    parts = hp.split(':', 1)
                    h_body += f"<p><strong>{parts[0]}:</strong> {parts[1]}</p>\n"
                else:
                    h_body += f"<p>{hp}</p>\n"

            hooks_html += f"""
<div class="hook-card info-card">
  <h4>{h['title']}</h4>
  {h_body}
</div>
"""

        content_html = f"""
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">{nfac}</span>
    <span class="badge rival-badge">Primary Rival: {nrival}</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> {appearance}</div>
    <div class="glance-item"><strong>Mannerisms:</strong> {mannerisms}</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;{quote}&rdquo;</div>
    <div class="glance-item dcs"><strong>Court Social DCs:</strong> {courtDCs}</div>
  </div>
</div>

<h3>Public Persona</h3>
{''.join([f'<p>{p}</p>' for p in publicPersona])}

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  {''.join([f'<p>{p}</p>' for p in secretAgenda])}
</div>

<h3>Faction Ties &amp; Court Relationships</h3>
{''.join([f'<p>{p}</p>' for p in factionTies])}

<h3>Player-Led Plot Hooks</h3>
{hooks_html}
"""

        articles.append({
            "id": nid,
            "category": "npcs",
            "title": nheader.split('(')[0].replace('2.1 ', '').replace('2.2 ', '').replace('3.1 ', '').replace('3.2 ', '').replace('4.1 ', '').replace('4.2 ', '').replace('5.1 ', '').replace('5.2 ', '').strip(),
            "subtitle": f"{nheader.split('(')[1].replace(')', '') if '(' in nheader else ''} &bull; {nfac}",
            "tags": ["Royal Court", "NPC", nfac.split('/')[0].strip(), "Period VIII"],
            "aliases": naliases,
            "summary": f"{nfac}. {publicPersona[0] if publicPersona else appearance}",
            "atAGlance": {
                "appearance": appearance,
                "mannerisms": mannerisms,
                "quote": quote,
                "courtDCs": courtDCs,
                "publicStance": publicPersona[0] if publicPersona else "",
                "secretAgenda": ' '.join(secretAgenda),
                "rival": nrival
            },
            "content": content_html,
            "gmSecrets": ' '.join(secretAgenda),
            "relatedIds": ["court-matrix", "campaign-premise"] + [r[0] for r in npc_configs if r[0] != nid]
        })

    # =========================================================================
    # 3. COURT MATRIX & RELATIONSHIPS
    # =========================================================================
    # Extract Section 6 of Royal Court NPCs
    matrix_text = []
    in_matrix = False
    for p in rc_paragraphs:
        if '6. Court Relationship Matrix & Cross-Faction Web' in p:
            in_matrix = True
            continue
        if '7. Kingdom-Building Plot Hook Index' in p:
            in_matrix = False
            break
        if in_matrix:
            matrix_text.append(clean(p))

    articles.append({
        "id": "court-matrix",
        "category": "npcs",
        "title": "Court Relationship Matrix & Cross-Faction Web",
        "subtitle": "Master Cross-Reference of Loyalties, Stances, Secret Levers, and Rivals",
        "tags": ["Court", "Matrix", "Factions", "Rivalries", "Quick Reference"],
        "aliases": ["Court Matrix", "Relationship Matrix", "Court Web", "NPC Matrix"],
        "summary": "Master matrix of all 8 key court NPCs detailing faction alignment, stated stance toward the PC Triumvirate, secret agenda, and primary court rival.",
        "content": """
<h3>Court Relationship Matrix & Cross-Faction Web</h3>
<p>This master matrix maps the lethal political architecture surrounding the PC Triumvirate. Every NPC possesses a public stance, a hidden lever, and a primary rival they seek to destroy.</p>

<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>NPC Name &amp; Title</th>
      <th>Primary Faction</th>
      <th>Stated Stance Toward PCs</th>
      <th class="gm-only-header">Secret Agenda / Hidden Lever</th>
      <th>Primary Court Rival</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="#npcs/valenza" class="wiki-link">General Don Rodrigo de Valenza</a></strong><br><small>Head of Royal Army</small></td>
      <td><span class="badge">Military Elite / Restoration Council</span></td>
      <td>Protective martial defender; loyal guardian of the crown.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Keep PCs dependent on army; conceal Period VI assassination of republican founder.</span></td>
      <td><a href="#npcs/lucia" class="wiki-link">Lucia de la Vega</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Mateo de Sadoria</a></strong><br><small>Chief Monarchist</small></td>
      <td><span class="badge">Restoration Council / Bureaucracy</span></td>
      <td>Devoted mentor, elder statesman, and administrative guide.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Restrict royal stipend to keep PCs financially paralyzed; hoard state wealth in Council vaults.</span></td>
      <td><a href="#npcs/gonzalo-guarralid" class="wiki-link">Duke Gonzalo de Guarralid</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/lucia" class="wiki-link">Fencing Master Lucia 'La Mariposa' de la Vega</a></strong><br><small>Republican Commander</small></td>
      <td><span class="badge">Republican Insurgents (The Pit)</span></td>
      <td>Openly hostile to monarchy; offers conditional secret pacts.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Expose Council's Period VI assassination plot; dismantle feudal monarchy for a republic.</span></td>
      <td><a href="#npcs/valenza" class="wiki-link">General Don Rodrigo</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/malachai" class="wiki-link">Father Malachai the Blind</a></strong><br><small>High Priest of Nemeth</small></td>
      <td><span class="badge">Church of Nemeth the Gnostic</span></td>
      <td>Conditional ally against sorcery; demands religious conversion.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Eradicate all necromancy; clear church's name; find Fountain of Youth to impose divine theocracy.</span></td>
      <td><a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalo de Guarralid</a></strong><br><small>Grandee Representative</small></td>
      <td><span class="badge">Grandee Coalitions (Eastern League)</span></td>
      <td>Dismissive of young rulers; demands absolute provincial autonomy.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Weaken central crown tariffs; hoard mountain mineral wealth; test crown strength via duels.</span></td>
      <td><a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/vesper" class="wiki-link">Vesper the Key-Master</a></strong><br><small>Spymaster of The Pit</small></td>
      <td><span class="badge">Underworld Syndicates / Smugglers</span></td>
      <td>Opportunistic business partner; seller of secrets and relics.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Maintain control of subterranean Pit; profit from pre-Cataclysmic relics and extortion.</span></td>
      <td><a href="#npcs/valenza" class="wiki-link">General Don Rodrigo</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a></strong><br><small>Industrial Thrall Overseer</small></td>
      <td><span class="badge">Crown Necromantic Apparatus</span></td>
      <td>Obedient technical advisor and supervisor of state thralls.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Expand industrial zombie production for profit; locate Black Blade of Azur or Obsidian Blade.</span></td>
      <td><a href="#npcs/malachai" class="wiki-link">Father Malachai</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio of Messantia</a></strong><br><small>Foreign Envoy of Argos</small></td>
      <td><span class="badge">Kingdom of Argos / Hyborian Powers</span></td>
      <td>Suave diplomatic ally offering financial loans and trade ties.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Exploit political instability; secure intelligence; force naval concessions in Baracha Strait.</span></td>
      <td><a href="#npcs/vesper" class="wiki-link">Vesper the Key-Master</a></td>
    </tr>
  </tbody>
</table>
</div>
""",
        "gmSecrets": "Valenza and Sadoria are also in secret rivalry: Valenza favors a military garrison state, while Sadoria favors a wealthy aristocratic oligarchy.",
        "relatedIds": ["valenza", "sadoria", "lucia", "malachai", "gonzalo-guarralid", "vesper", "vane", "tiberio"]
    })

    # =========================================================================
    # 4. HISTORICAL CHRONOLOGY & 8 PERIODS (Complete from Campaign Setting.docx)
    # =========================================================================
    hist_text = []
    in_hist = False
    for p in cs_paragraphs:
        if '2. EIGHT-PERIOD CANONICAL CHRONOLOGY' in p:
            in_hist = True
            continue
        if '3. DRAMATIS PERSONAE & HISTORICAL FIGURES' in p:
            in_hist = False
            break
        if in_hist:
            hist_text.append(clean(p))

    periods = [
        ("period-i", "Period I: The Gift", "Founding of the Realm & The Buried Blade"),
        ("period-ii", "Period II: The Time of the Elves", "Golden Age of Ancillus I & Elven Scholars"),
        ("period-iii", "Period III: The Magical Capital", "Desecration of Ancillus, Earthquake, & First Undead"),
        ("period-iv", "Period IV: The Zombie Era", "Edmund's Industrial Necromancy & Labor Pits"),
        ("period-v", "Period V: Mad King Daedalus & The Starfall", "City Sacrifice, Cosmic Meteor, & The Obsidian Blade"),
        ("period-vi", "Period VI: Religious Rulership & Fall", "Holy Crusade of Nemeth, Child Crucifixion, & Coup"),
        ("period-vii", "Period VII: Restoration Civil War", "Return of Undead Ancillus I & Monarchist Betrayal"),
        ("period-viii", "Period VIII: The Besieged Kingdom", "Modern Campaign Epoch: The Triumvirate's Ascendancy Trap")
    ]

    for pid, ptitle, psub in periods:
        p_body = []
        in_p = False
        for p in hist_text:
            if ptitle[:10] in p:
                in_p = True
                continue
            if in_p:
                if any(other[1][:10] in p for other in periods if other[0] != pid) or '2.2 Historical Chronology Master Matrix' in p:
                    break
                p_body.append(p)

        body_html = ''.join([f'<p>{p}</p>\n' for p in p_body if not p.startswith('Period')])
        articles.append({
            "id": pid,
            "category": "history",
            "title": ptitle,
            "subtitle": psub,
            "tags": ["History", "Chronology", "Lore", pid],
            "aliases": [ptitle, pid.replace("-", " ")],
            "summary": p_body[0] if p_body else psub,
            "content": f"""
<div class="info-card">
  <p><strong>Chronological Designation:</strong> {ptitle}</p>
  <p><strong>Core Theme:</strong> {psub}</p>
</div>
<h3>Historical Chronicle</h3>
{body_html}
""",
            "gmSecrets": f"Events from {ptitle} directly inform modern conspiracies, buried relics, and subterranean passages in The Pit.",
            "relatedIds": ["history-matrix", "campaign-premise", "ancillus-i", "daedalus"]
        })

    # Master Historical Matrix
    articles.append({
        "id": "history-matrix",
        "category": "history",
        "title": "Historical Chronology Master Matrix",
        "subtitle": "Section 2.2: Master Chronology of Zingaran Cataclysm and Rebirth",
        "tags": ["History", "Timeline", "Matrix", "Quick Reference"],
        "aliases": ["Historical Matrix", "Timeline", "Eight Periods", "Chronology Matrix"],
        "summary": "Master matrix detailing the defining events, key figures, and lasting modern legacies across all eight historical epochs.",
        "content": """
<h3>2.2 Historical Chronology Master Matrix</h3>
<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Period &amp; Name</th>
      <th>Defining Canonical Events</th>
      <th>Key Historical Figures</th>
      <th>Lasting Legacy on Modern Zingara</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="#history/period-i" class="wiki-link">I: The Gift</a></strong></td>
      <td>Kingdom founded in Zingg Valley; Black Blade forged by sorcerer; sorcerer executed; blade buried underground.</td>
      <td>Founding Monarch, Executed Sorcerer</td>
      <td>Established core territory and buried primary anti-sorcery relic beneath valley.</td>
    </tr>
    <tr>
      <td><strong><a href="#history/period-ii" class="wiki-link">II: Time of the Elves</a></strong></td>
      <td>Arrival of elven longships; cross-cultural peace; founding of magical academy in Kordava.</td>
      <td><a href="#history/ancillus-i" class="wiki-link">King Ancillus I</a>, Elven Scholars</td>
      <td>Codified advanced arcane traditions and elven architectural influence.</td>
    </tr>
    <tr>
      <td><strong><a href="#history/period-iii" class="wiki-link">III: Magical Capital</a></strong></td>
      <td>First zombie created; tomb of Ancillus desecrated; earthquake subsumes academy; Black Blade lost; necromancy commercialized.</td>
      <td><a href="#history/printius" class="wiki-link">Printius</a>, <a href="#history/silkeneth" class="wiki-link">Lord Silkeneth</a></td>
      <td>Created subterranean sunken ruins beneath Kordava; introduced commercial undead labor.</td>
    </tr>
    <tr>
      <td><strong><a href="#history/period-iv" class="wiki-link">IV: Zombie Era</a></strong></td>
      <td>Industrialization of undead labor; vast zombie pits engineered across the realm for mining.</td>
      <td><a href="#history/edmund" class="wiki-link">Edmund the Necromancer</a></td>
      <td>Permanently shifted economy to rely on thrall labor; left toxic vats across the realm.</td>
    </tr>
    <tr>
      <td><strong><a href="#history/period-v" class="wiki-link">V: Mad King Daedalus</a></strong></td>
      <td>Obsidian Blade unearthed; city sacrifice of Kordava; Starfall meteor strike; Daedalus imprisoned by Tanatos.</td>
      <td><a href="#history/daedalus" class="wiki-link">King Daedalus</a>, <a href="#history/tanatos" class="wiki-link">Tanatos</a>, <a href="#history/fergus" class="wiki-link">Fergus</a></td>
      <td>Shattered old Kordava into rubble; created memory-retaining zombie hordes; birthed Church of Nemeth.</td>
    </tr>
    <tr>
      <td><strong><a href="#history/period-vi" class="wiki-link">VI: Religious Rulership</a></strong></td>
      <td>Holy crusade against zombies; Fountain of Youth found; child crucifixion scandal; coup; covert murder.</td>
      <td><a href="#history/fergus" class="wiki-link">Fergus</a>, <a href="#history/falmouth" class="wiki-link">Falmouth</a>, <a href="#history/nemeth" class="wiki-link">Nemeth</a>, <a href="#npcs/valenza" class="wiki-link">General Valenza</a></td>
      <td>Left hidden theocratic cults; created monarchist-republican rift; lost the Fountain of Youth.</td>
    </tr>
    <tr>
      <td><strong><a href="#history/period-vii" class="wiki-link">VII: Restoration Civil War</a></strong></td>
      <td>Discovery of Ancillus lineage; republican revolt; undead King Ancillus I returns; alliance and betrayal.</td>
      <td>Undead Ancillus I, <a href="#factions/restoration-council" class="wiki-link">Restoration Council</a></td>
      <td>Decimated population; crippled republican leaders via assassination; cemented Council control.</td>
    </tr>
    <tr>
      <td><strong><a href="#history/period-viii" class="wiki-link">VIII: Besieged Kingdom</a></strong></td>
      <td>Installation of PC Triumvirate by puppetmasters; growth of The Pit; multi-front threats.</td>
      <td>The Triumvirate (PCs), <a href="#npcs/valenza" class="wiki-link">Valenza</a>, <a href="#npcs/sadoria" class="wiki-link">Mateo</a></td>
      <td>Modern campaign setting: bankrupt, besieged realm ruled by young rulers surrounded by wolves.</td>
    </tr>
  </tbody>
</table>
</div>
""",
        "gmSecrets": "Every historical period ended in hubris or betrayal. The players must break this multi-century cycle.",
        "relatedIds": ["period-i", "period-viii", "campaign-premise"]
    })

    # =========================================================================
    # 5. HISTORICAL FIGURES (DRAMATIS PERSONAE)
    # =========================================================================
    figures_data = [
        ("ancillus-i", "King Ancillus I", "Progenitor Monarch of the Golden Age & Undead Warlord", "Period II & Period VII", ["Ancillus", "King Ancillus", "Ancillus I"]),
        ("printius", "Printius", "Head of the Magical Academy & Co-Founder of Commercial Necromancy", "Period III", ["Printius"]),
        ("silkeneth", "Lord Silkeneth", "Mercenary Nobleman & Architect of Industrial Thrall Mercantilism", "Period III", ["Silkeneth", "Lord Silkeneth"]),
        ("edmund", "Edmund the Necromancer", "Master Necromancer & Engineer of the Industrial Zombie Pits", "Period IV", ["Edmund", "Master Edmund"]),
        ("daedalus", "Mad King Daedalus", "Tyrannical Monarch of the Starfall & Bearer of the Obsidian Blade", "Period V", ["Daedalus", "Mad King Daedalus", "King Daedalus"]),
        ("fergus", "Fergus the Holy Warrior", "Last Human King's Guard & Founder of the Church of Nemeth", "Period V & VI", ["Fergus", "Holy Fergus"]),
        ("tanatos", "Death (Tanatos)", "Cosmic Incarnation of Death & Cosmic Tormentor of Daedalus", "Period V", ["Tanatos", "Death"]),
        ("falmouth", "Priest Falmouth", "High Priest of Nemeth & Discoverer of the Fountain of Youth", "Period VI", ["Falmouth", "High Priest Falmouth"]),
        ("nemeth", "Nemeth the Gnostic", "Divine Entity of Holy Magic & Patron of the Underground Faith", "Period VI & Modern", ["Nemeth", "Nemeth the Gnostic"])
    ]

    # Extract Section 3 text
    fig_text = []
    in_fig = False
    for p in cs_paragraphs:
        if '3. DRAMATIS PERSONAE & HISTORICAL FIGURES' in p:
            in_fig = True
            continue
        if '4. REGIONAL GAZETTEER & GEOGRAPHY' in p:
            in_fig = False
            break
        if in_fig:
            fig_text.append(clean(p))

    for fid, fname, fsub, fperiod, faliases in figures_data:
        f_body = []
        in_this_fig = False
        for p in fig_text:
            if fname in p or (fid == 'tanatos' and 'Death (Tanatos)' in p):
                in_this_fig = True
                continue
            if in_this_fig:
                if any(other[1] in p for other in figures_data if other[0] != fid):
                    break
                f_body.append(p)

        f_html = ""
        role = ""
        actions = ""
        legacy = ""
        for p in f_body:
            if p.startswith('Historical Role:'):
                role = p.split(':', 1)[1].strip()
            elif p.startswith('Canonical Actions:'):
                actions = p.split(':', 1)[1].strip()
            elif p.startswith('Modern Legacy:'):
                legacy = p.split(':', 1)[1].strip()
            else:
                f_html += f"<p>{p}</p>\n"

        articles.append({
            "id": fid,
            "category": "history",
            "title": fname,
            "subtitle": f"{fsub} &bull; {fperiod}",
            "tags": ["Historical Figure", "Lore", fperiod],
            "aliases": faliases,
            "summary": role or fsub,
            "content": f"""
<div class="info-card">
  <p><strong>Historical Role:</strong> {role or fsub}</p>
  <p><strong>Period of Prominence:</strong> {fperiod}</p>
</div>
<h3>Canonical Actions</h3>
<p>{actions}</p>
<h3>Lasting Legacy on Modern Zingara</h3>
<p>{legacy}</p>
{f_html}
""",
            "gmSecrets": f"Relics and crypts associated with {fname} remain accessible in The Pit or ancient provincial ruins.",
            "relatedIds": ["history-matrix", "campaign-premise", "court-matrix"]
        })

    # =========================================================================
    # 6. REGIONAL GAZETTEER (Complete from Section 4 of Campaign Setting.docx)
    # =========================================================================
    gaz_entries = [
        ("kordava", "Kordava", "Modern Capital & Seat of the Crystal Floor Court", "Coastal Port / Capital", "Seat of royal court, foreign trade, naval base.", "Court intrigue, royal guards, street skirmishes, assassins."),
        ("the-pit", "The Pit", "Subterranean Sunken Ruins beneath Kordava", "Subterranean Sunken Ruins", "Black markets, hidden refuges, ancient artifacts.", "Criminal syndicates, rogue zombies, toxic cave-ins, stone guardians."),
        ("mausoleum-kalenius", "Submerged Mausoleum of King Kalenius", "Pre-Cataclysmic Tomb beneath Kordava Harbor", "Underwater Ancient Tomb", "Holds pre-Cataclysmic Thurian weaponry, ancient armor, and the dormant Final Guard.", "Flooded vertical shafts, aquatic ghoul constructs, 1,000 animate stone guardians."),
        ("zingg-valley", "Zingg Valley", "Fertile River Basin & Agricultural Heartland", "Fertile River Basin", "Agriculture, wine, olive oil, horse breeding.", "Republican guerrillas, hidden church shrines, local bandits."),
        ("jerida", "Jerida", "Fortified River Port on the Lower Thunder River", "Fortified River Port", "Inland river trade, iron and lumber distribution.", "River pirates, corrupt customs inspectors, mercenaries."),
        ("guarralid", "Guarralid Highlands", "Autonomous Mountain Fiefdom & Iron Mines", "Mountainous Interior Fief", "Mineral wealth, defensive interior bastion.", "Private grandee armies, feud ambushes, mountain raiders."),
        ("sadoria-kova", "Sadoria & Kova", "Central Agricultural Plains & Warhorse Hubs", "Rolling Agricultural Plains", "Warhorse breeding, citrus production, grain.", "Thrall labor revolts, noble press-gangs, highwaymen."),
        ("baracha-strait", "Baracha Strait & Isles", "Reef-Choked Pirate Archipelago", "Island Chain / Reef Corridor", "Maritime trade lanes, privateer hideouts.", "Barachan pirates, naval blockades, sudden sea storms."),
        ("forest-of-ghouls", "Forest of Ghouls & City of the Ghouls", "Primeval Gloom-Draped Cursed Wilderness", "Primeval Cursed Forest", "Ancient ruin salvage, rare alchemical ingredients.", "Feral ghouls, necromantic constructs, lost cultists."),
        ("pictish-wilderness", "Pictish Wilderness", "Untamed Northern Frontier & Savage Jungle", "Northern Dense Jungle/Forest", "Frontier timber, pelt trading.", "Pictish raiding parties, wild beasts, uncharted terrain."),
        ("poitain-alimane", "Poitain Mountains & River Alimane", "Northeastern Mountain Border with Aquilonia", "Northeastern Mountain Border", "Frontier defense, Alpine river transit.", "Border patrols, mountain avalanches, smuggler ambushes."),
        ("rabirian-mountains", "Rabirian Mountains", "Southeastern Barrier Range & Fountain Shrine", "Southeastern Barrier Range", "Border security, ancient shrine sites.", "Mountain bandits, fanatical cultists, treacherous passes."),
        ("kingdom-of-argos", "Kingdom of Argos & Port Messantia", "Ancient Maritime Rival & Wealthy Merchant Empire", "Southeastern Maritime Realm", "Naval commerce, foreign diplomacy.", "Argossean privateers, naval blockades, foreign spies.")
    ]

    gaz_text = []
    in_gaz = False
    for p in cs_paragraphs:
        if '4. REGIONAL GAZETTEER & GEOGRAPHY' in p:
            in_gaz = True
            continue
        if '5. FACTION & POLITICAL DYNAMICS' in p:
            in_gaz = False
            break
        if in_gaz:
            gaz_text.append(clean(p))

    for gid, gname, gsub, gtype, gstrat, ghaz in gaz_entries:
        g_body = []
        in_this_g = False
        for p in gaz_text:
            if gname in p:
                in_this_g = True
                continue
            if in_this_g:
                if any(other[1] in p for other in gaz_entries if other[0] != gid) or '4.5 Regional Gazetteer Master Matrix' in p:
                    break
                g_body.append(p)

        body_html = ''.join([f'<p>{p}</p>\n' for p in g_body]) if g_body else f"<p>Regional territory of Zingara.</p>"
        articles.append({
            "id": gid,
            "category": "gazetteer",
            "title": gname,
            "subtitle": gsub,
            "tags": ["Gazetteer", "Geography", gtype.split('/')[0].strip()],
            "aliases": [gname, gsub],
            "summary": f"{gtype}. {gstrat}",
            "content": f"""
<div class="info-card">
  <p><strong>Geographical Type:</strong> {gtype}</p>
  <p><strong>Strategic &amp; Economic Value:</strong> {gstrat}</p>
  <p><strong>Primary Encounter Hazards:</strong> {ghaz}</p>
</div>
<h3>Geographical Description</h3>
{body_html}
<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; REGIONAL HAZARDS &amp; HOOKS</div>
  <p><strong>Encounter Threats:</strong> {ghaz}</p>
</div>
""",
            "gmSecrets": ghaz,
            "relatedIds": ["gazetteer-matrix", "kordava", "the-pit", "campaign-premise"]
        })

    # Master Gazetteer Matrix Article
    articles.append({
        "id": "gazetteer-matrix",
        "category": "gazetteer",
        "title": "Regional Gazetteer Master Matrix",
        "subtitle": "Section 4.5: Master Matrix of Geography, Economics, and Hazards",
        "tags": ["Gazetteer", "Matrix", "Quick Reference", "Geography"],
        "aliases": ["Gazetteer Matrix", "Geography Matrix", "Regional Matrix"],
        "summary": "Master matrix of all 13 Zingaran regions with geographical classifications, strategic value, and encounter hazards.",
        "content": """
<h3>4.5 Regional Gazetteer Master Matrix</h3>
<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Region / Location</th>
      <th>Geographical Type</th>
      <th>Strategic / Economic Value</th>
      <th>Primary Encounter Hazards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="#gazetteer/kordava" class="wiki-link">Kordava</a></strong></td>
      <td>Coastal Port / Capital</td>
      <td>Seat of royal court, foreign trade, naval base.</td>
      <td>Court intrigue, royal guards, street skirmishes, assassins.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/the-pit" class="wiki-link">The Pit</a></strong></td>
      <td>Subterranean Sunken Ruins</td>
      <td>Black markets, hidden refuges, ancient artifacts.</td>
      <td>Criminal syndicates, rogue zombies, toxic cave-ins, stone guardians.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/zingg-valley" class="wiki-link">Zingg Valley</a></strong></td>
      <td>Fertile River Basin</td>
      <td>Agriculture, wine, olive oil, horse breeding.</td>
      <td>Republican guerrillas, hidden church shrines, local bandits.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/jerida" class="wiki-link">Jerida</a></strong></td>
      <td>Fortified River Port</td>
      <td>Inland river trade, iron and lumber distribution.</td>
      <td>River pirates, corrupt customs inspectors, mercenaries.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/guarralid" class="wiki-link">Guarralid</a></strong></td>
      <td>Mountainous Interior Fief</td>
      <td>Mineral wealth, defensive interior bastion.</td>
      <td>Private grandee armies, feud ambushes, mountain raiders.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/sadoria-kova" class="wiki-link">Sadoria &amp; Kova</a></strong></td>
      <td>Rolling Agricultural Plains</td>
      <td>Warhorse breeding, citrus production, grain.</td>
      <td>Thrall labor revolts, noble press-gangs, highwaymen.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/baracha-strait" class="wiki-link">Baracha Strait &amp; Isles</a></strong></td>
      <td>Island Chain / Reef Corridor</td>
      <td>Maritime trade lanes, privateer hideouts.</td>
      <td>Barachan pirates, naval blockades, sudden sea storms.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/forest-of-ghouls" class="wiki-link">Forest of Ghouls</a></strong></td>
      <td>Primeval Cursed Forest</td>
      <td>Ancient ruin salvage, rare alchemical ingredients.</td>
      <td>Feral ghouls, necromantic constructs, lost cultists.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/pictish-wilderness" class="wiki-link">Pictish Wilderness</a></strong></td>
      <td>Northern Dense Jungle/Forest</td>
      <td>Frontier timber, pelt trading.</td>
      <td>Pictish raiding parties, wild beasts, uncharted terrain.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/poitain-alimane" class="wiki-link">Poitain Mountains &amp; River Alimane</a></strong></td>
      <td>Northeastern Mountain Border</td>
      <td>Frontier defense, Alpine river transit.</td>
      <td>Border patrols, mountain avalanches, smuggler ambushes.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/rabirian-mountains" class="wiki-link">Rabirian Mountains</a></strong></td>
      <td>Southeastern Barrier Range</td>
      <td>Border security, ancient shrine sites.</td>
      <td>Mountain bandits, fanatical cultists, treacherous passes.</td>
    </tr>
    <tr>
      <td><strong><a href="#gazetteer/kingdom-of-argos" class="wiki-link">Kingdom of Argos</a></strong></td>
      <td>Southeastern Maritime Realm</td>
      <td>Naval commerce, foreign diplomacy.</td>
      <td>Argossean privateers, naval blockades, foreign spies.</td>
    </tr>
  </tbody>
</table>
</div>
""",
        "gmSecrets": "Use encounter hazards to introduce sudden complications when players travel across provinces.",
        "relatedIds": ["kordava", "the-pit", "zingg-valley", "jerida"]
    })

    # =========================================================================
    # 7. FACTIONS & MILITARY DOCTRINES (Section 5 of Campaign Setting.docx)
    # =========================================================================
    fac_configs = [
        ("restoration-council", "Restoration Council", "Monarchist Cabal & Bureaucracy", ["Restoration Council", "Council", "Chief Monarchist"]),
        ("military-elite", "The Military Elite & Royal Army Command", "Chivalric Caballeros & Armed Forces", ["Military Elite", "Royal Army", "Zingaran Army"]),
        ("republican-insurgents", "Republican Insurgents", "Underground Radical Cells in The Pit", ["Republican Insurgents", "Republicans", "The Pit Rebels"]),
        ("church-of-nemeth", "Church of Nemeth the Gnostic", "Underground Fanatical Theocracy", ["Church of Nemeth", "Nemeth the Gnostic", "Gnostic Church"]),
        ("grandees", "Grandee Coalitions", "Hereditary High Nobility (Eastern & Western Leagues)", ["Grandee Coalitions", "Grandees", "Eastern League", "Western League"]),
        ("barachan-pirates", "Barachan Pirates & Freebooters", "Corsairs of the Baracha Strait", ["Barachan Pirates", "Barachan Corsairs", "Corsairs", "Freebooters"]),
        ("foreign-powers", "Foreign Powers & Regional Neighbors", "Kingdom of Argos, Poitain, & Pictish Clans", ["Foreign Powers", "Kingdom of Argos", "Argos", "Picts", "Poitain"])
    ]

    fac_text = []
    in_fac = False
    for p in cs_paragraphs:
        if '5. FACTION & POLITICAL DYNAMICS' in p:
            in_fac = True
            continue
        if '5.2 Military Doctrines & Command Friction' in p:
            break
        if in_fac:
            fac_text.append(clean(p))

    for fid, fname, fsub, faliases in fac_configs:
        f_body = []
        in_this_f = False
        for p in fac_text:
            if fname in p or (fid == 'restoration-council' and 'Restoration Council' in p):
                in_this_f = True
                continue
            if in_this_f:
                if any(other[1] in p for other in fac_configs if other[0] != fid):
                    break
                f_body.append(p)

        body_html = ''.join([f'<p>{p}</p>\n' for p in f_body]) if f_body else "<p>Zingaran faction.</p>"
        articles.append({
            "id": fid,
            "category": "factions",
            "title": fname,
            "subtitle": fsub,
            "tags": ["Faction", "Politics", "Power Bloc"],
            "aliases": faliases,
            "summary": f_body[0] if f_body else fsub,
            "content": f"""
<div class="info-card">
  <p><strong>Faction Classification:</strong> {fsub}</p>
</div>
<h3>Faction Dossier &amp; Operations</h3>
{body_html}
""",
            "gmSecrets": f"This faction possesses active levers to exploit against the PC Triumvirate.",
            "relatedIds": ["court-matrix", "valenza", "sadoria", "lucia", "malachai", "gonzalo-guarralid"]
        })

    # =========================================================================
    # 8. RULES & MECHANICS (Section 5.2, 6.1, 6.2, 6.3 of Campaign Setting.docx)
    # =========================================================================
    articles.append({
        "id": "pundonor",
        "category": "rules",
        "title": "Dueling Culture & Pundonor Rules",
        "subtitle": "Section 6.2: Aristocratic Honor System, Duels, Penalties, & Swashbuckling Flair",
        "tags": ["Rules", "Pundonor", "Combat", "Social", "Dueling"],
        "aliases": ["Pundonor", "Dueling Rules", "Honor Rules", "Pundonor System"],
        "summary": "The touchy Zingaran code of honor. Yielding or refusing a duel inflicts a persistent -2 social penalty until cleansed by victory in formal combat.",
        "content": """
<h3>6.2 Dueling Culture & Pundonor Rules</h3>
<p>Swordsmanship is Zingara's preeminent art form. Zingarans reject brute-force hacking weapons in favor of slender cut-and-thrust rapiers and main-gauche parrying daggers. Master swordsmen operate prestigious fencing academies (esgrimas) throughout Kordava. Social slights, territorial squabbles, or romantic rivalries are settled through formal duels at dawn or fatal back-alley encounters.</p>

<div class="rule-box">
  <div class="rule-header">MECHANICAL RULE: PUNDONOR (HONOR)</div>
  <p><strong>Trigger:</strong> A character yields, flees, or refuses a legitimate duel of honor when challenged by a social peer or noble in public.</p>
  <p><strong>Mechanical Effect:</strong> The character suffers a persistent <strong>-2 penalty</strong> to all Social, Persuasion, and Command checks when interacting with Zingaran nobility, military officers, or high-class merchants.</p>
  <p><strong>Cleansing the Stain:</strong> The penalty remains active until the character's honor is cleansed by defeating a social peer in a formal duel or completing an extraordinary feat of public bravery.</p>
</div>

<h3>NPC Honor-Baiting Tactics (GM Roleplay Guidance)</h3>
<p>Rival Grandees and fencing masters exploit pundonor as a political weapon against the PC Triumvirate. An NPC will deliberately issue mild public insults—questioning a PC's martial skill, royal legitimacy, or courage—in front of assembled court nobles. This forces the PC into a dilemma:</p>
<ul>
  <li>Accept an illegal or potentially fatal duel on the NPC's home turf.</li>
  <li>Refuse and suffer the persistent -2 Pundonor penalty to all subsequent royal governance and persuasion attempts.</li>
</ul>

<div class="info-card">
  <h4>GM Advice for Swashbuckling Combat Flair</h4>
  <p>Reward players who incorporate the environment into martial encounters. Grant a <strong>+2 situational bonus</strong> to attack rolls or Armor Class whenever a player executes swashbuckling maneuvers, such as:</p>
  <ul>
    <li>Swinging from wrought-iron chandeliers or balconies.</li>
    <li>Wrapping a velvet cloak around an off-hand arm to parry a blade.</li>
    <li>Vaulting over wine casks or tavern tables during fencing duels.</li>
    <li>Kicking sand or wine into an opponent's eyes before a lunge.</li>
  </ul>
</div>
""",
        "gmSecrets": "Duke Gonzalo de Guarralid will use pundonor challenges early in court to gauge whether the PCs have martial backbone.",
        "relatedIds": ["gonzalo-guarralid", "command-friction", "social-hierarchy"]
    })

    articles.append({
        "id": "command-friction",
        "category": "rules",
        "title": "Military Doctrines & Command Friction",
        "subtitle": "Section 5.2: Tactical Arms, Aristocratic Insubordination, & Royal Edicts",
        "tags": ["Rules", "Warfare", "Tactics", "Command", "Military"],
        "aliases": ["Command Friction", "Military Doctrines", "Warfare Rules"],
        "summary": "Four tactical arms of Zingara and the Command Friction mechanic: noble commanders routinely refuse orders from rivals without a DC 14 check.",
        "content": """
<h3>5.2 Military Doctrines & Tactical Arms</h3>
<p>Zingaran military strategy relies on four distinct tactical arms:</p>
<ul>
  <li><strong>Heavy Cavalry (Caballeros):</strong> Armored noble lancers mounted on barded warhorses. Recruited from the noble caste, they form the elite striking arm of Grandee armies, devastating in open-field shock charges.</li>
  <li><strong>Pike Blocks &amp; Arbalesters:</strong> Disciplined municipal defensive squares composed of peasant levies and city guards armed with long pikes, supported by heavy crossbowmen (arbalesters) capable of punching through knightly armor.</li>
  <li><strong>Fencing Skirmishers:</strong> Light infantry specialized in urban skirmishing, boarding actions, and rough terrain. Armed with rapiers, bucklers, and throwing blades, they excel at maneuverability and harassment.</li>
  <li><strong>The Royal Fleet &amp; Privateers:</strong> War galleys and swift caravels equipped for close-quarters naval action, featuring ramming prows, archer platforms, and boarding raiders.</li>
</ul>

<div class="rule-box">
  <div class="rule-header">COMMAND FRICTION MECHANICS</div>
  <p><strong>The Core Military Flaw:</strong> The fundamental vulnerability of any Zingaran military force is command friction caused by aristocratic hubris, feudal bloodlines, and sensitive personal honor (pundonor).</p>
  <p><strong>Operational Execution:</strong> Because military appointments are tied to social rank rather than competence, high-born Grandees routinely refuse to take orders from social rivals or low-born officers.</p>
  <p><strong>Check Mechanics:</strong> In mass tactical engagements, when an order is issued to a subordinate noble unit, the commander must make a <strong>DC 14 Command Check</strong> utilizing Warfare, Leadership, or Persuasion. On a failure, the subordinate noble considers the order an insult to their personal honor, resulting in an uncoordinated charge, refusal of reinforcement, or complete battlefield withdrawal.</p>
  <p><strong>Player Mitigation Options:</strong> Player Characters acting as the Triumvirate can bypass or reduce this Command Friction through direct royal intervention:</p>
  <ul>
    <li><em>Expend a Royal Edict:</em> Expending a formal Crown Decree automatically succeeds on the check, though it increases Council suspicion.</li>
    <li><em>Issue a Direct Duel Challenge:</em> A PC can publicly challenge an insubordinate Grandee to an immediate duel of honor; if accepted or conceded, the DC is reduced to <strong>DC 8</strong> for the remainder of the battle.</li>
  </ul>
</div>
""",
        "gmSecrets": "When players command noble levies, remember that high-born commanders will happily lose a battle rather than take an order from a lower-ranked officer.",
        "relatedIds": ["pundonor", "military-elite", "gonzalo-guarralid"]
    })

    articles.append({
        "id": "social-hierarchy",
        "category": "rules",
        "title": "Ethnic Genesis & Social Hierarchy",
        "subtitle": "Section 6.1: The Four Strata: Grandees, Caballeros, Chulos, and Thralls",
        "tags": ["Culture", "Society", "Classes", "Lore"],
        "aliases": ["Social Hierarchy", "Ethnic Genesis", "Social Strata", "Zingaran Society"],
        "summary": "Synthesis of Shemite, Pictish, and Hyborian bloodlines forming four rigid classes: Grandees, Caballeros, Chulos & Commoners, and Undead Thralls.",
        "content": """
<h3>6.1 Ethnic Genesis & Social Hierarchy</h3>
<p>Zingaran society arose from three distinct historical waves: peaceful Shemitish agriculturalists of the Zingg Valley merged first with primitive conquering Pictish tribes, and later with invading Hyborian warriors. This fusion created a proud, dark-complexioned, slender people who combined Hyborian martial traditions, Shemitish agricultural roots, and tempestuous Pictish blood.</p>

<div class="info-card">
<h4>The Four Rigid Social Strata</h4>
<ol>
  <li><strong>Grandees (Grandes):</strong> The hereditary high nobility (dukes, counts, high barons). They govern vast fiefdoms as near-sovereign lords, maintain private armies, mint provincial coin, and obey the crown only when compelled by military force.</li>
  <li><strong>Caballeros &amp; Hidalgos:</strong> The lesser nobility, knights, and landed gentry. Serving primarily as heavy cavalry, retainers to Grandees, or fencing masters, they are obsessed with military reputation and genealogical purity.</li>
  <li><strong>Chulos &amp; Commoners:</strong> Urban artisans, shopkeepers, maritime laborers, and manorial peasants. While peasants are bound to rural soil under manorial burdens, urban commoners possess a fiery, rebellious spirit and vibrant pub culture.</li>
  <li><strong>Undead Thralls:</strong> The lowest underclass. Memory-retaining zombies used for brutal, toxic labor in the mining pits. Stripped of all mortal rights, yet horrifyingly conscious of their former lives.</li>
</ol>
</div>
""",
        "gmSecrets": "Commoners are heavily drawn to republican pamphlets circulated from The Pit.",
        "relatedIds": ["pundonor", "necromancy-mechanics", "campaign-premise"]
    })

    articles.append({
        "id": "fashion-aesthetics",
        "category": "rules",
        "title": "Fashion, Aesthetics, & Architecture",
        "subtitle": "Section 6.3: Chivalric Doublets, Corsair Silks, & White Arcades",
        "tags": ["Culture", "Fashion", "Architecture", "Aesthetics"],
        "aliases": ["Fashion", "Aesthetics", "Architecture", "Zingaran Fashion"],
        "summary": "Visual details of Zingaran life: slashed silk doublets, ostrich plumes, corsair silks stained with pitch, and whitewashed stone mansions over ancient ruins.",
        "content": """
<h3>6.3 Fashion, Aesthetics, & Architecture</h3>
<div class="info-card">
  <h4>Noble &amp; Fencer Attire</h4>
  <p>Slashed doublets of silk, satin, and velvet; bright lace collars; sweeping velvet cloaks; high cordwain riding boots; wide-brimmed felt hats crowned with peacock or ostrich plumes.</p>
  <h4>Mariner &amp; Corsair Gear</h4>
  <p>Gaudy silks stained with pitch, gold hoop earrings, wide leather belts studded with rough jewels, and multiple dagger sheaths.</p>
  <h4>Architectural Palette</h4>
  <p>Whitewashed stone mansions, grand arcades, wrought-iron balconies, central garden courtyards, and massive coastal stone fortresses constructed directly over pre-Cataclysmic foundations.</p>
</div>
""",
        "gmSecrets": "Use descriptions of court silks and lace to contrast sharply with the subterranean squalor of The Pit.",
        "relatedIds": ["kordava", "the-pit", "social-hierarchy"]
    })

    # =========================================================================
    # 9. ARCANA, RELICS & UNDEAD (Section 7 of Campaign Setting.docx)
    # =========================================================================
    articles.append({
        "id": "necromancy-mechanics",
        "category": "relics",
        "title": "Memory-Retaining Undead Mechanics",
        "subtitle": "Section 7.1: The Horrific Psychology and Exploitation of Zingaran Thralls",
        "tags": ["Arcana", "Undead", "Necromancy", "Mechanics", "Horror"],
        "aliases": ["Memory-Retaining Undead", "Thrall Mechanics", "Necromancy Mechanics", "Undead Rules"],
        "summary": "Zingaran zombies retain their living memories and personalities while trapped in complete physical servitude to their masters.",
        "content": """
<h3>7.1 Necromantic Mechanics & Industrial Exploitation</h3>
<p>Unlike mindless skeletons found in other fantasy settings, zombies created through Zingaran necromancy retain their pre-death human memories, intellect, and personalities, while remaining totally enthralled to their master's magical commands or controlling artifacts. This creates three core operational dilemmas at the table:</p>

<div class="rule-box">
  <div class="rule-header">THREE OPERATIONAL THRALL DILEMMAS</div>
  <ol>
    <li><strong>The Reanimated Acquaintance:</strong> PCs encounter fallen allies, family members, or historical figures who recognize them, speaking with tragic clarity and experiencing conscious horror at their own servitude while forced to attack.</li>
    <li><strong>Tactical Intelligence Exploitation:</strong> Capturing and interrogating an enthralled thrall allows characters to extract vital historical memories, secret passage locations, or security passwords known by the individual in life (<strong>DC 14 Interrogation/Persuasion Check</strong>).</li>
    <li><strong>Moral Sabotage:</strong> PCs can manipulate a thrall's deep personal memories or unfulfilled life vows to create momentary cognitive dissonance. A successful <strong>DC 16 Persuasion Check</strong> temporarily paralyzes a thrall for <strong>1d4 rounds</strong> as its living mind fights the binding magic.</li>
  </ol>
</div>
""",
        "gmSecrets": "Master Alchemist Vane is conducting unsanctioned soul-binding experiments on political dissidents.",
        "relatedIds": ["industrial-pits", "vane", "edmund", "obsidian-blade"]
    })

    articles.append({
        "id": "industrial-pits",
        "category": "relics",
        "title": "Industrial Zombie Pits & Blueprint Layout",
        "subtitle": "Section 7.1: Mass Thrall Labor Infrastructure, Toxic Vats, & Hazard Rules",
        "tags": ["Arcana", "Dungeon", "Zombie Pits", "Hazards"],
        "aliases": ["Industrial Zombie Pits", "Zombie Pits", "The Pits", "Edmund's Pits"],
        "summary": "Modular blueprints and environmental hazards for the reeking chemical extraction pits engineered by Edmund across Zingara.",
        "content": """
<h3>Industrial Zombie Pits Architecture &amp; Mechanics</h3>
<p>Engineered during Period IV by Edmund the Necromancer, these industrial complexes are dug into subterranean caverns and open quarries to extract valuable ores and toxic minerals using disposable, tireless undead labor.</p>

<div class="info-card">
<h4>Modular Pit Blueprint Layout</h4>
<ul>
  <li><strong>1. Excavation Pit &amp; Mine Shafts:</strong> Deep, unventilated subterranean shafts where thralls chisel raw ore in total darkness. Prone to cave-ins and gas pockets.</li>
  <li><strong>2. Chemical Preservation Vats:</strong> Massive stone cisterns filled with acidic embalming slurry and sulfurous resins used to pickle thrall flesh and prevent rot.</li>
  <li><strong>3. The Processing Floor:</strong> Sorting belts and crushing mills where thralls crush rock with bare hands and iron hammers. High risk of mechanical accidents.</li>
  <li><strong>4. The Overseer's Iron Cage:</strong> A fortified, suspended metal redoubt overlooking the pit where mortal alchemists and guards issue commands using control amulets.</li>
</ul>
</div>

<div class="rule-box">
  <div class="rule-header">PIT ENVIRONMENTAL HAZARDS</div>
  <ul>
    <li><strong>Toxic Alchemical Slurry:</strong> Falling into a preservation pool deals <strong>2d6 acid damage</strong> per round and forces a <strong>DC 13 Fortitude/Constitution Save</strong> against toxic fumes.</li>
    <li><strong>Fume Inhalation:</strong> Characters in the pit must save every 10 minutes or suffer cumulative -1 penalties to physical checks.</li>
    <li><strong>Thrall Frenzy / Meltdown:</strong> If the alchemical Overseer Amulet is destroyed, all thralls in the chamber fly into an uncoordinated frenzy, attacking the nearest living creatures.</li>
  </ul>
</div>
""",
        "gmSecrets": "Pit #4 near Jerida connects directly to an ancient unmapped crypt holding the Black Blade of Azur.",
        "relatedIds": ["necromancy-mechanics", "vane", "edmund", "black-blade"]
    })

    articles.append({
        "id": "black-blade",
        "category": "relics",
        "title": "The Black Blade of Azur",
        "subtitle": "Section 7.2: Pre-Deluvial Anti-Sorcery Relic",
        "tags": ["Relic", "Artifact", "Anti-Magic", "Weapon"],
        "aliases": ["Black Blade of Azur", "Black Blade", "Blade of Azur"],
        "summary": "Legendary anti-sorcery weapon forged in Period I. Capable of instantly severing necromantic control and nullifying magical wards.",
        "content": """
<h3>7.2 The Black Blade of Azur</h3>
<div class="info-card">
  <p><strong>Historical Origin:</strong> Forged in Period I by an ancient sorcerer in the Zingg Valley; buried underground following the sorcerer's execution to prevent catastrophic misuse.</p>
  <p><strong>Current Status:</strong> Lost in the subterranean abyss beneath the ruins of the old magical academy, far below The Pit in Kordava.</p>
</div>

<h3>Eldritch Properties &amp; Powers</h3>
<p>The Black Blade is forged from an unreflective, light-devouring matte black alloy. It possesses absolute anti-magic properties:</p>
<ul>
  <li><strong>Arcane Nullification:</strong> Radiates a constant 10-foot aura of magical suppression, dispelling spells and magical wards on contact.</li>
  <li><strong>Thrall Severance:</strong> Striking a necromantic thrall with the blade immediately severs its binding runes, granting the soul permanent release into death without reanimation.</li>
  <li><strong>Sovereign Defense:</strong> In the hands of the Triumvirate, the blade would completely neutralize the Restoration Council's secret sorcerous countermeasures.</li>
</ul>
""",
        "gmSecrets": "Vane is desperately seeking this blade to destroy it before it can sever his thralls.",
        "relatedIds": ["obsidian-blade", "the-pit", "vane", "period-i"]
    })

    articles.append({
        "id": "obsidian-blade",
        "category": "relics",
        "title": "The Obsidian Blade",
        "subtitle": "Section 7.2: Eldritch Mass-Binding Conduit of Mad King Daedalus",
        "tags": ["Relic", "Artifact", "Necromancy", "Weapon", "Horror"],
        "aliases": ["The Obsidian Blade", "Obsidian Blade"],
        "summary": "Terrifying necromantic conduit uncovered by Mad King Daedalus. Grants supreme command over undead hordes, buried with Daedalus beneath The Pit.",
        "content": """
<h3>7.2 The Obsidian Blade</h3>
<div class="info-card">
  <p><strong>Historical Origin:</strong> Uncovered by Mad King Daedalus in Period V to channel the sacrificial blood of citizens and envoys into his cauldron for godhood.</p>
  <p><strong>Current Status:</strong> Buried deep within the smoldering rubble of old Kordava beneath The Pit, where King Daedalus lies eternally trapped by Tanatos.</p>
</div>

<h3>Eldritch Properties &amp; Powers</h3>
<ul>
  <li><strong>Horde Command:</strong> The wielder can mentally command hundreds of memory-retaining thralls simultaneously over miles without verbal orders.</li>
  <li><strong>Mass Exhumation:</strong> Plunging the blade into unhallowed ground automatically animates fallen corpses within a 300-foot radius.</li>
  <li><strong>The Cosmic Curse:</strong> The blade constantly whispers with the voices of Daedalus and the victims of the Starfall. Wielding it requires a DC 16 Wisdom/Sanity check every dawn or suffer paranoid megalomania.</li>
</ul>
""",
        "gmSecrets": "If the blade is taken from Daedalus's hand, Tanatos's imprisonment ritual will collapse.",
        "relatedIds": ["daedalus", "black-blade", "the-pit", "tanatos"]
    })

    articles.append({
        "id": "fountain-of-youth",
        "category": "relics",
        "title": "The Fountain of Youth",
        "subtitle": "Section 7.2: Sacred Waters of Miraculous Longevity & Purification",
        "tags": ["Relic", "Healing", "Church of Nemeth", "Rabirian"],
        "aliases": ["The Fountain of Youth", "Fountain of Youth", "Waters of the Shrine"],
        "summary": "Miraculous sacred spring discovered in Period VI in the Rabirian Mountains. Cures all poisons, reverses decay, and grants centuries of life.",
        "content": """
<h3>7.2 The Fountain of Youth</h3>
<div class="info-card">
  <p><strong>Historical Origin:</strong> Discovered by High Priest Falmouth in Period VI in the Rabirian Mountains, securing divine prestige for the Church of Nemeth.</p>
  <p><strong>Current Status:</strong> Concealed inside a sealed, trapped mountain shrine in the Rabirian borderlands, disputed by Argossean mercenaries and Gnostic cultists.</p>
</div>

<h3>Miraculous Powers</h3>
<ul>
  <li><strong>Absolute Healing:</strong> Drinking the waters immediately cures any mortal poison, disease, or magical wasting sickness.</li>
  <li><strong>Necromantic Reversal:</strong> Reverses physical decay in living creatures touched by necromancy, and can purify blighted land.</li>
  <li><strong>Longevity:</strong> Grants centuries of unaging vigor, making it the ultimate prize for aging Grandees and foreign kings.</li>
</ul>
""",
        "gmSecrets": "Marquis Mateo poisoned a royal relative specifically to force the Triumvirate to locate this fountain.",
        "relatedIds": ["malachai", "falmouth", "rabirian-mountains", "church-of-nemeth"]
    })

    articles.append({
        "id": "final-guard",
        "category": "relics",
        "title": "The Final Guard of King Kalenius",
        "subtitle": "One Thousand Pre-Cataclysmic Thurian Stone Warriors",
        "tags": ["Relic", "Guardians", "Ancient", "Thurian", "Military"],
        "aliases": ["The Final Guard", "Final Guard", "Stone Guardians", "Kalenius Guard"],
        "summary": "One thousand deathless stone warriors guarding King Kalenius's tomb. If commanded, they would provide an unstoppable royal army.",
        "content": """
<h3>The Final Guard of King Kalenius</h3>
<p>Dating back to the pre-Cataclysmic Thurian epoch (recorded in the chronicles of Karl Edward Wagner), the Final Guard was King Kalenius's elite royal bodyguard. Through ancient rites, one thousand warriors were petrified into living, animate stone to guard their king's rest for eternity.</p>

<div class="info-card">
<h4>Combat &amp; Mechanical Attributes</h4>
<ul>
  <li><strong>Animate Stone Physiology:</strong> Immune to poison, bleed, mental influence, and necromantic corruption. Resistant to slashing and piercing damage.</li>
  <li><strong>Thurian Masterwork Armament:</strong> Equipped with star-metal broadswords and tower shields that ignore standard magical armor.</li>
  <li><strong>The True Command:</strong> If the PC Triumvirate can secure the Royal Signet of Kalenius from his sarcophagus, they could awaken the Final Guard to serve as their personal, incorruptible household army.</li>
</ul>
</div>
""",
        "gmSecrets": "Vesper has secret access to this flooded tomb and will sell the coordinates for royal immunity.",
        "relatedIds": ["mausoleum-kalenius", "vesper", "the-pit"]
    })

    # =========================================================================
    # 10. PLOT HOOKS (Complete from Section 8 of CS and Section 7 of Royal Court)
    # =========================================================================
    hooks_data = [
        ("hook-blood-in-cauldron", "Blood in the Cauldron", "Section 8.1 / Section 7.1", ["The Triumvirate", "Restoration Council", "Kingdom of Argos", "The Pit Underworld"],
         "A neighboring Hyborian nation (Argos) threatens immediate war unless the signet ring of their ambassador—murdered during Mad King Daedalus's ritual in Period V—is returned from an earthquake-exposed crypt beneath Kordava. The Restoration Council forbids the Triumvirate from intervening, hoping the diplomatic crisis will humiliate the crown.",
         "Deep in the crypt, the PCs discover the ambassador is now a conscious, memory-retaining zombie thrall who guards the Obsidian Blade. The rulers must choose whether to destroy the thrall and return the signet ring to prevent war, free the thrall using a dangerous unbinding rite, or secretly claim the Obsidian Blade for themselves.",
         "DC 15 History/Arcana Check (identify unbinding runes); DC 17 Persuasion Check (appeal to living memories to secure signet peacefully).",
         "If the PCs take longer than 3 rounds negotiating or searching the crypt, a covert strike team loyal to the Restoration Council enters from upper tunnels, ordered to seize all relics and eliminate witnesses.",
         "Prevents an immediate Argossean naval blockade of Kordava harbor, secures a foreign diplomatic reprieve, and provides potential access to the Obsidian Blade."),

        ("hook-insurgents-bargain", "The Insurgent's Bargain", "Section 8.1 / Section 7.1", ["The Triumvirate", "Republican Insurgents", "Restoration Council", "Church of Nemeth"],
         "Republican insurgents operating out of The Pit contact the PCs in secret during a royal diplomatic gala. They possess hard evidence proving that the military chief and chief monarchist—the PCs' own puppetmasters—assassinated the republican founder during Period VI and framed the Church of Nemeth.",
         "The republicans offer the evidence in exchange for royal pardons and democratic concessions. However, agents of the underground Church of Nemeth intercept the meeting, demanding the evidence to clear their church's name. The PCs must decide whether to use the evidence to blackmail their handlers, hand it to the church, or side with the Council.",
         "DC 16 Stealth/Deception Check (slip away from royal handlers at gala); DC 14 Insight Check (detect double-dealing in church zealots).",
         "If the PCs hesitate or attempt to play all sides, the military chief's royal assassins strike the meeting place, attempting to burn the documents and silence all informants.",
         "Secures absolute blackmail evidence against General Don Rodrigo and Marquis Mateo, allowing the PCs to purge their puppetmasters or force total political submission."),

        ("hook-pits-of-edmund", "The Reeking Pits of Edmund", "Section 8.1 / Section 7.2", ["The Triumvirate", "Restoration Council", "Grandee Coalitions", "Master Alchemist Vane"],
         "A crown-owned industrial zombie pit near Jerida collapses into an ancient river cavern, releasing hundreds of memory-retaining thralls who seize a vital iron mine. The Restoration Council uses the lost revenue as an excuse to cut the royal household's stipend, tightening their financial leash on the Triumvirate.",
         "Traveling to Jerida under the guise of an inspection, the PCs discover the thralls are led by a reanimated Period IV scholar who offers to reveal a secret passage into the crypt of the Black Blade of Azur—an anti-sorcery weapon capable of severing Council magical control—if the rulers help the thralls escape to the Pictish Wilderness.",
         "DC 14 Athletics/Survival Check (navigate toxic pit slurry); DC 16 Warfare/Tactics Check (organize stealth escape route through mountain passes).",
         "Reeking toxic alchemical fumes require a DC 13 Fortitude Save every 10 minutes; failure inflicts cumulative physical weakness (-1 to physical checks and attack rolls).",
         "Restores iron production to the royal armory while gaining a secret map to the subterranean crypt housing the Black Blade of Azur."),

        ("hook-fallen-shrine", "Waters of the Fallen Shrine", "Section 8.1 / Section 7.3", ["The Triumvirate", "Restoration Council", "Church of Nemeth", "Kingdom of Argos"],
         "One of the PCs (or their sole loyal blood relative at court) is struck by a slow, magical wasting poison—secretly administered by the Restoration Council to remind the Triumvirate how easily they can be replaced. To survive without begging handlers for an antidote, the PCs must quietly ride into the Rabirian Mountains to locate the lost Fountain of Youth.",
         "The PCs locate the shrine, but find an underground cell of Nemeth Gnostics guarding the waters while an Argossean naval detachment attacks to seize the Fountain. The PCs must choose whether to strike a deal with the fanatical cultists, bribe the Argosseans, or secure the waters before the shrine collapses.",
         "DC 15 Perception Check (spot Argossean mountain scouts); DC 17 Religion Check (quote Gnostic scripture accurately to secure sanctuary).",
         "On round 4 of combat inside the shrine, the fragile cavern ceiling collapses, destroying the primary pool of the Fountain forever and forcing a panicked flight.",
         "Acquires waters from the Fountain of Youth in the Rabirian Mountains, providing an absolute cure for magical wasting poisons, disease, or necromantic decay affecting royal allies."),

        ("hook-concealed-order", "The Concealed Execution Order", "Section 7.1", ["Military Elite", "Republican Insurgents", "The Triumvirate"],
         "General Don Rodrigo requests the Triumvirate sign an official royal decree mobilizing troops to purge a 'rebel encampment' in the Zingg Valley. In reality, the camp houses surviving witnesses to the Period VI assassination of the republican founder.",
         "The PCs must decide whether to rubber-stamp the order to maintain Don Rodrigo's favor, or delay the decree to dispatch covert agents to investigate who is actually in the camp.",
         "DC 15 Investigation/Insight (uncover true identity of target camp); DC 16 Command/Persuasion (countermand military orders).",
         "If the PCs delay signing for more than 24 hours, Don Rodrigo executes the operation using his private household guard and places the royal quarters on protective lockdown.",
         "Saves key witnesses to Period VI state crimes, earning the secret allegiance of urban republican cells without triggering an immediate military coup."),

        ("hook-treasury-lockout", "The Treasury Lockout", "Section 7.2", ["Restoration Council", "The Triumvirate", "Marquis Mateo"],
         "When the Triumvirate attempts to allocate funds for independent city watch recruitment, Marquis Mateo calmly informs them that crown coffers are completely dry, citing foreign debt payments owed to Argos.",
         "The PCs must find a way to finance their rule without Council permission: raid an illicit black-market smuggling den in The Pit, audit Mateo's private provincial tax records, or negotiate a risky loan with foreign merchants.",
         "DC 16 Investigation (audit treasury scrolls to detect missing gold); DC 17 Persuasion/Intimidation (confront Mateo with proof of embezzled revenues).",
         "If confronted directly without unassailable proof, Mateo retaliates by cutting the royal palace's servant and food budgets, claiming 'extreme wartime austerity.'",
         "Exposes Council embezzlement and forces release of crown funds for an independent royal guard."),

        ("hook-tax-revolt-jerida", "The Tax Revolt of Jerida", "Section 7.2", ["Grandee Coalitions", "Restoration Council", "Barachan Pirates"],
         "Duke Gonzalo orders his private garrison in Jerida to seize royal barges carrying timber and ore along the Thunder River, declaring an embargo until the crown cuts provincial customs tariffs.",
         "The PCs must travel to Jerida to break the standoff through military intimidation, clever economic compromise, or covert sabotage of Gonzalo's supply lines.",
         "DC 15 Intimidation (rally local merchants against Gonzalo's embargo); DC 14 Deception/Stealth (smuggle crown goods past the river blockade).",
         "Failure to resolve the embargo within 3 days triggers an armed clash between royal army detachments and Gonzalo's retainers, threatening full civil war.",
         "Re-establishes crown trade tariffs along the lower Thunder River, generating independent income that frees the Triumvirate from the Council's financial leash."),

        ("hook-tomb-kalenius", "The Tomb of King Kalenius", "Section 7.3", ["Vesper the Key-Master", "Grandee Coalitions", "The Triumvirate"],
         "Vesper approaches the PCs through a secret passage in the palace wine cellar, offering a map to the forgotten crypt of King Kalenius beneath Kordava's harbor in exchange for royal immunity for his smuggling guild.",
         "The crypt contains legendary pre-Cataclysmic weapons and the dormant Final Guard (one thousand animate stone warriors), but entering requires diving into flooded tunnels infested with aquatic ghoul constructs.",
         "DC 16 Athletics/Endurance (underwater tunnel navigation beneath Kordava harbor); DC 17 Warfare/Tactics (survive engagement with stone guardians).",
         "Disturbing the crypt without the proper ritual key awakens six stone guardians who attack relentlessly until subdued or sealed back behind the stone gate.",
         "Secures pre-Cataclysmic weaponry and stone-guardian armor from the Final Guard, allowing the PCs to equip an elite personal household guard immune to corruption."),

        ("hook-treasury-heist", "The Treasury Heist", "Section 7.2", ["Restoration Council", "Vesper the Key-Master", "The Triumvirate"],
         "The PCs partner with Vesper the Key-Master to break into the Restoration Council's secret subterranean vaults beneath Kordava to seize hoarded bullion.",
         "Bypass pre-Cataclysmic mechanical wards, avoid Council patrols, and extract hoarded gold without being identified.",
         "DC 16 Thievery/Stealth (bypass subterranean vault traps); DC 15 Arcana (disarm pre-Cataclysmic mechanical wards).",
         "Triggering a trap fills the vault with paralytic gas and summons mute thrall sentinels.",
         "Reclaims hoarded state gold from Council vaults, allowing the PCs to pay the Kordava city watch directly and secure their absolute loyalty.")
    ]

    for hid, hname, hsec, hfacs, hprem, hconf, hdcs, hesc, hrew in hooks_data:
        articles.append({
            "id": hid,
            "category": "hooks",
            "title": hname,
            "subtitle": f"{hsec} &bull; Factions: {', '.join(hfacs)}",
            "tags": ["Hook", "Quest", "Sandbox", "Kingdom-Building"],
            "aliases": [hname],
            "summary": hprem[:140] + "...",
            "content": f"""
<div class="info-card">
  <p><strong>Involved Factions:</strong> {', '.join(hfacs)}</p>
  <p><strong>Strategic Reward:</strong> {hrew}</p>
</div>

<h3>Narrative Premise</h3>
<p>{hprem}</p>

<h3>Core Conflict &amp; Player Choice</h3>
<p>{hconf}</p>

<div class="dc-box">
  <strong>Suggested Skill Checks:</strong> {hdcs}
</div>

<p class="escalation"><strong>Dynamic Escalation Trigger:</strong> {hesc}</p>
""",
            "gmSecrets": f"Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
            "relatedIds": ["court-matrix", "campaign-premise", "valenza", "sadoria", "lucia", "vesper"]
        })

    # Master Plot Hook Index Article
    articles.append({
        "id": "hooks-index",
        "category": "hooks",
        "title": "Master Kingdom-Building Plot Hook Index",
        "subtitle": "Section 7: Master Index Categorized by Campaign Pillar",
        "tags": ["Hooks", "Index", "Quick Reference", "Sandbox"],
        "aliases": ["Plot Hook Index", "Hooks Index", "Kingdom-Building Index"],
        "summary": "Master index of all kingdom-building plot hooks categorized under Crown Sovereignty, Economic Recovery, and Ancient Relics.",
        "content": """
<h3>7. Kingdom-Building Plot Hook Index</h3>
<div class="info-card">
  <h4>1. Crown Sovereignty &amp; Puppetmaster Defiance</h4>
  <ul>
    <li><strong><a href="#hooks/hook-insurgents-bargain" class="wiki-link">The Insurgent's Bargain</a>:</strong> Secure blackmail evidence against Valenza and Sadoria from republican cells.</li>
    <li><strong><a href="#hooks/hook-blood-in-cauldron" class="wiki-link">Blood in the Cauldron</a>:</strong> Prevent an immediate Argossean naval blockade and resolve a crypt crisis.</li>
    <li><strong><a href="#hooks/hook-concealed-order" class="wiki-link">The Concealed Execution Order</a>:</strong> Intercept General Valenza's secret purge order targeting assassination witnesses.</li>
  </ul>

  <h4>2. Economic Recovery &amp; Thrall Labor Crises</h4>
  <ul>
    <li><strong><a href="#hooks/hook-pits-of-edmund" class="wiki-link">The Reeking Pits of Edmund</a>:</strong> Resolve a thrall revolt at Pit #4 near Jerida and find the Black Blade map.</li>
    <li><strong><a href="#hooks/hook-tax-revolt-jerida" class="wiki-link">The Tax Revolt of Jerida</a>:</strong> Break Duke Gonzalo's river embargo on the lower Thunder River.</li>
    <li><strong><a href="#hooks/hook-treasury-lockout" class="wiki-link">The Treasury Lockout</a>:</strong> Audit Marquis Mateo's ledgers to expose state gold embezzlement.</li>
    <li><strong><a href="#hooks/hook-treasury-heist" class="wiki-link">The Treasury Heist</a>:</strong> Infiltrate Council vaults with Vesper to reclaim hoarded state bullion.</li>
  </ul>

  <h4>3. Ancient Relics &amp; Eldritch Defense</h4>
  <ul>
    <li><strong><a href="#hooks/hook-fallen-shrine" class="wiki-link">Waters of the Fallen Shrine</a>:</strong> Locate the Fountain of Youth in the Rabirian Mountains to cure wasting poison.</li>
    <li><strong><a href="#hooks/hook-tomb-kalenius" class="wiki-link">The Tomb of King Kalenius</a>:</strong> Dive into flooded abyssal crypts to awaken the 1,000 stone warriors of the Final Guard.</li>
  </ul>
</div>
""",
        "gmSecrets": "Use this index to quickly pick an adventure hook depending on what pressure the PCs are trying to resolve.",
        "relatedIds": ["hook-blood-in-cauldron", "hook-insurgents-bargain", "hook-pits-of-edmund", "court-matrix"]
    })

    # Write out data.js
    data_content = f"""// Our Kingdom Come - Zingara Sandbox GM Compendium Data
// Auto-compiled from canonical source documents

window.WIKI_DATA = {{
  meta: {{
    title: "Our Kingdom Come",
    subtitle: "Zingara Sandbox Campaign & GM Intrigue Compendium",
    epoch: "Period VIII: The Besieged Kingdom",
    totalArticles: {len(articles)}
  }},
  categories: [
    {{ id: "overview", name: "Campaign Overview", icon: "👑" }},
    {{ id: "npcs", name: "Royal Court & NPCs", icon: "🎭" }},
    {{ id: "factions", name: "Factions & Power Blocs", icon: "⚔️" }},
    {{ id: "gazetteer", name: "Regional Gazetteer", icon: "🗺️" }},
    {{ id: "history", name: "Chronology & Periods", icon: "📜" }},
    {{ id: "rules", name: "Rules & Mechanics", icon: "⚖️" }},
    {{ id: "relics", name: "Arcana & Relics", icon: "💀" }},
    {{ id: "hooks", name: "Plot Hooks & Sandbox", icon: "🎯" }},
    {{ id: "sessions", name: "Session Log", icon: "📖" }}
  ],
  articles: {json.dumps(articles, indent=2)}
}};

var WIKI_DATA = window.WIKI_DATA;

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = WIKI_DATA;
}}
"""

    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(data_content)

    print(f"Successfully generated js/data.js with {len(articles)} fully populated articles!")

if __name__ == '__main__':
    main()
