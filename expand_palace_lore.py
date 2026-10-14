"""
expand_palace_lore.py
Adds the High Alcazar of Kordava (Gormenghast-inspired palace) and 7 distinct palace staff NPCs
with full Labyrinth Lord stat blocks, B/X mechanics, at-a-glance dossiers, and plot hooks.
"""

import json
import re

def main():
    with open('js/data.js', 'r', encoding='utf-8') as f:
        raw_text = f.read()

    m = re.search(r'window\.WIKI_DATA\s*=\s*(\{.*\});?', raw_text, re.DOTALL)
    if not m:
        print("Error: Could not extract window.WIKI_DATA from js/data.js")
        return

    data = json.loads(m.group(1))
    articles = data['articles']
    article_ids = {a['id']: a for a in articles}

    print(f"Loaded {len(articles)} existing articles.")

    # -------------------------------------------------------------
    # 1. HELPER: Generate Labyrinth Lord Stat Block HTML
    # -------------------------------------------------------------
    def make_stat_block(npc_title, stats):
        # Abilities bar
        ab_boxes = ""
        for ab_name, ab_val, ab_desc in stats["abilities"]:
            ab_boxes += f"""
        <div class="stat-ability-box">
          <div class="stat-ability-label">{ab_name}</div>
          <div class="stat-ability-score">{ab_val}</div>
          <div class="stat-ability-mod">{ab_desc.split(',')[0]}</div>
        </div>
        """

        # Saves bar
        saves_boxes = ""
        for s_name, s_val in stats["saves"]:
            short_name = s_name.split('(')[1].replace(')', '') if '(' in s_name else s_name
            saves_boxes += f"""
        <div class="stat-save-box" title="{s_name}">
          <div class="stat-save-label">{short_name}</div>
          <div class="stat-save-val">{s_val}</div>
        </div>
        """

        # Magic items
        items_html = '<div class="stat-pill-list">' + ''.join([f'<div class="stat-pill">⚔️ {item}</div>' for item in stats["magicItems"]]) + '</div>'

        # Optional Thief Skills
        thief_html = ""
        if "thiefSkills" in stats:
            thief_pills = ''.join([f'<div class="stat-pill"><strong>{sk}:</strong> {pct}</div>' for sk, pct in stats["thiefSkills"]])
            thief_html = f"""
        <div class="stat-section-title">Thief Skills (Labyrinth Lord {stats['classLevel'].split()[0]})</div>
        <div class="stat-pill-list">{thief_pills}</div>
        """

        # Optional Spells
        spells_html = ""
        if "spellsPrepared" in stats:
            spell_rows = ""
            for circle, slist in stats["spellsPrepared"]:
                spell_rows += f'<p style="margin-bottom: 4px;"><strong>{circle}:</strong> {slist}</p>\n'
            spells_html = f"""
        <div class="stat-section-title">Spells Prepared (Labyrinth Lord Divine/Arcane Circles)</div>
        <div style="background: var(--bg-surface); padding: 10px 14px; border-radius: var(--radius-sm); margin: 6px 0;">
          {spell_rows}
        </div>
        """

        return f"""
<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">{npc_title}</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">{stats['station']} &bull; {stats['alignment']}</div>
    </div>
    <span class="stat-class-level">⚔️ {stats['classLevel']}</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> {stats['ac']} <small class="text-dim">({stats['acBreakdown']})</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> {stats['hd']} &bull; <span style="color: #2ecc71; font-weight: 700;">{stats['hp']} HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> {stats['move']}</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> {stats['thaco']}</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> {stats['attacks']}</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    {ab_boxes}
  </div>

  <div class="stat-section-title">Saving Throws (Labyrinth Lord 5-Column)</div>
  <div class="stat-saves-bar">
    {saves_boxes}
  </div>

  {thief_html}
  {spells_html}

  <div class="stat-section-title">Signature Magic Items &amp; Regalia</div>
  {items_html}

  <div class="stat-section-title">Combat Tactics, Retainers &amp; Equipment</div>
  <p>{stats['tactics']}</p>

  <div class="stat-section-title">Power Scale vs. PC Triumvirate (Level 8–9 Rulers)</div>
  <p class="text-muted" style="margin-bottom: 0;">{stats['pcComparison']}</p>
</div>
"""

    # -------------------------------------------------------------
    # 2. DEFINE THE 7 PALACE NPCS
    # -------------------------------------------------------------
    palace_npcs_data = [
        {
            "id": "obregon",
            "category": "npcs",
            "title": "Lord Belisario de Obregon",
            "subtitle": "Grand Seneschal of Precedent & Master of the Royal Hours &bull; Palace Household / Traditionalists",
            "tags": ["Royal Court", "NPC", "Palace Staff", "Period VIII", "Gormenghast", "Court Intrigue"],
            "aliases": ["Lord Belisario", "Belisario de Obregon", "Grand Seneschal", "The Decrepit", "Master of Precedent"],
            "summary": "The ninety-year-old, parchment-skinned Grand Seneschal who rules the daily life of the Alcázar with terrifying ceremonial pedantry. Armed with the 900-page Book of the Royal Hours, he forces the Triumvirate through suffocating ancestral rituals while hoarding forgotten dynastic secrets.",
            "stats": {
                "classLevel": "9th-Level Cleric / Savant",
                "combatStats": "AC 5 (AAC 14) | HP 38 | THAC0 15 | Atk +4 (1d6) | Saves: 13/7/9/10/11",
                "alignment": "Lawful (Obsessive ritualism, ancient ancestral legitimacy, fanatical adherence to precedent)",
                "station": "Grand Seneschal of the Royal Household & Keeper of the Book of Hours",
                "ac": "AC 5 (AAC 14)",
                "acBreakdown": "Stiff Bullion-Embroidered Vestments +2, Ring of Mind Shielding, DEX 8 (-1)",
                "hd": "9d6",
                "hp": 38,
                "move": "30' (10') (hobbles with a gilded ebony cane)",
                "thaco": "15 (Base Attack Bonus +4)",
                "attacks": "Gilded Ebony Cane of Ancillus (+1 light mace, 1d6 damage; sheds golden glow on command)",
                "abilities": [
                    ("STR", 8, "-1 to hit, -1 damage"),
                    ("DEX", 8, "-1 missile to hit, +1 AC penalty"),
                    ("CON", 11, "Normal (0)"),
                    ("INT", 16, "+1 language, encyclopedic recall of 400 years of court law"),
                    ("WIS", 17, "+2 saves vs magic, extra 1st-4th circle divine spells"),
                    ("CHA", 14, "+1 reaction, commanding patriarchal presence")
                ],
                "saves": [
                    ("Breath Weapon (BW)", 13),
                    ("Poison or Death (P/D)", 7),
                    ("Petrify or Paralyze (PP)", 9),
                    ("Wands (W)", 10),
                    ("Spells (S)", 11)  # Base 13 - 2 for WIS 17
                ],
                "spellsPrepared": [
                    ("1st Circle", "Detect Evil, Light, Remove Fear, Sanctuary"),
                    ("2nd Circle", "Hold Person, Know Alignment, Silence 15' Radius"),
                    ("3rd Circle", "Continual Light, Locate Object, Glyph of Warding"),
                    ("4th Circle", "Cure Serious Wounds, Neutralize Poison"),
                    ("5th Circle", "Quest / Geas")
                ],
                "magicItems": [
                    "The Silver Calipers of Ancillus I (Magical regalia-measurer; automatically detects illusions, disguise magic, and counterfeit royal seals upon touch)",
                    "Ring of Mind Shielding (Completely immune to ESP, magical truth-telling, and telepathic intrusion)",
                    "The Libro de las Horas Reales (Indestructible iron-bound calfskin tome containing unredacted genealogies and ancestral edicts)",
                    "Pectoral of Sacred Wardenship (+2 to AC, included in stats)"
                ],
                "tactics": "<strong>Ancestral Invocation:</strong> Belisario never draws a blade himself. If physically confronted, he strikes his cane upon the stone to cast <em>Silence 15' Radius</em> or <em>Hold Person</em> while shrieking for the guard.<br><strong>Guard of the Precedent:</strong> Attended at all times by 4 veteran Palace Halberdiers (Fighters Level 4, AC 3, 22 HP each, Morale 9) and two adolescent herald-pages who carry his lectern.",
                "pcComparison": "Physically frail (38 HP, movement 30'), but an insurmountable legal barrier. If the PCs defy or dismiss him, court protocol grinds to a halt: grandees refuse audience, royal edicts lose legal legitimacy, and the Church of Nemeth accuses the young rulers of apostasy."
            },
            "atAGlance": {
                "appearance": "A withered, ninety-year-old skeleton wrapped in stiff cloth-of-gold robes encrusted with dead jewel-beetles and tarnished bullion. His skin is spotted parchment; his milky eyes glare with terrifying genealogical zeal.",
                "mannerisms": "Sniffs loudly with contempt; taps his gilded ebony cane with rhythmic impatience; quotes sub-clauses of the Edicts of 712 whenever anyone speaks out of turn.",
                "quote": "Your royal grandfather, Sire, would rather have had his spleen removed with a fish-hook than receive an ambassador before the bell of Terce had ceased reverberating. We do not alter the sequence.",
                "courtDCs": "Morale: 10 (Fanatical traditionalist); Initial Reaction: Suspicious (-1 on 2d6 Reaction Rolls). Charisma check (or reciting correct 4th-epoch etiquette) to alter any morning ceremonial without inciting a court scandal.",
                "publicStance": "Strictly neutral toward the Restoration Council and Grandees, claiming allegiance only to the immortal, unchanging Precedent of the Crown.",
                "secretAgenda": "To preserve the absolute purity of ancient Zingaran dynastic ritual against the vulgar militarism of Valenza and the mercantile corruptions of Sadoria. He secretly guards the unredacted Testament of King Daedalus, which proves the Restoration Council's legal charter is an eighty-year-old fraud.",
                "rival": "High Chancellor Marquis Mateo de Sadoria",
                "classLevel": "9th-Level Cleric / Savant",
                "combatStats": "AC 5 (AAC 14) | HP 38 | THAC0 15 | Atk +4 (1d6) | Saves: 13/7/9/10/11"
            },
            "gmSecrets": "Hidden inside the hollow spine of the *Libro de las Horas Reales* is the original Imperial Charter of Period IV, proving that the Triumvirate possess the absolute legal authority to dismiss the Restoration Council without grandee assent. Belisario will only surrender this secret if convinced the PCs intend to restore the true liturgical dignity of the monarchy.",
            "relatedIds": ["palace-of-kordava", "sadoria", "valenza", "court-matrix", "silveira", "ignacio"],
            "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Palace Household &bull; Grand Seneschal</span>
    <span class="badge rival-badge">Primary Rival: High Chancellor Marquis Mateo de Sadoria</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A withered, ninety-year-old skeleton wrapped in stiff cloth-of-gold robes encrusted with dead jewel-beetles and tarnished bullion. His skin is spotted parchment; his milky eyes glare with terrifying genealogical zeal.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Sniffs loudly with contempt; taps his gilded ebony cane with rhythmic impatience; quotes sub-clauses of the Edicts of 712 whenever anyone speaks out of turn.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;Your royal grandfather, Sire, would rather have had his spleen removed with a fish-hook than receive an ambassador before the bell of Terce had ceased reverberating. We do not alter the sequence.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 10 (Fanatical traditionalist); Initial Reaction: Suspicious (-1 on 2d6 Reaction Rolls). Charisma check (roll 1d20 under Cha) to alter any morning ceremonial without inciting a court scandal.</div>
  </div>
</div>

<h3>Public Persona &amp; Palace Duties</h3>
<p>Lord Belisario has held the office of Grand Seneschal through three monarchs, four rebellions, and the ascension of the Triumvirate. He embodies the suffocating, baroque ritualism of the High Alcázar. Every aspect of daily life in the palace—from the exact angle at which a royal cupbearer must tilt a silver ewer, to the mandatory four-hour ceremonial dressing of the sovereigns—is governed by his iron whim and his monstrous calfskin tome, the <em>Libro de las Horas Reales</em>.</p>
<p>To the young PC rulers, he is an infuriating, immovable obstacle: he refuses to allow the PCs to hold emergency midnight war councils because "the Edict of 648 expressly limits sovereign assemblies to daylight hours," and insists that provincial petitions be filed in triplicate upon consecrated sheepskin.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>Belisario despises <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a> and <a href="#npcs/valenza" class="wiki-link">General Don Rodrigo de Valenza</a>, regarding them as vulgar, parvenu usurpers who treat the sacred bloodline of Ancillus I as puppets. Hidden within the hollow binding of his ancient ceremonial volume is the unredacted <em>Testament of King Daedalus</em>, which legally invalidates the Restoration Council's charter. If the PCs demonstrate true reverence for royal dignity and ancestral law, Belisario can become their most formidable constitutional weapon against their handlers.</p>
</div>

<h3>Faction Ties &amp; Palace Relationships</h3>
<ul>
  <li><strong><a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a>:</strong> A venomous mutual hatred. Sadoria repeatedly attempts to retire Belisario to a monastery; Belisario uses ancient procedural points to block Sadoria's financial appropriations.</li>
  <li><strong><a href="#npcs/silveira" class="wiki-link">Don Fernao de Silveira</a>:</strong> An uneasy, prickly alliance of ancient traditionalists. While they squabble over who has precedence when opening royal bedchamber doors, both are fiercely loyal to the Ancillus bloodline.</li>
  <li><strong><a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo</a>:</strong> Belisario considers the kitchen master a disgusting, unwashed swine whose greasy existence defiles the court.</li>
</ul>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Imperial Veto of Ancillus I</h4>
  <p><strong>Premise:</strong> <a href="#npcs/valenza" class="wiki-link">General Valenza</a> demands the Triumvirate sign an edict declaring martial law in Kordava to crush the republican agitators in The Pit. Lord Belisario publicly halts the signing, declaring that under the Edicts of Period IV, no martial decree can take effect without the ceremonial Consecration of the Silver Calipers—which must be conducted at high noon following a three-day fast.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must decide whether to side with Belisario's infuriating procedural stall (buying them 72 hours to investigate The Pit peacefully, while enraging Valenza's officer corps), or overrule the ancient Seneschal (pleasing the army, but triggering a crippling religious strike by the palace heralds and scribes).</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Charisma check (roll 1d20 under Cha) to placate the military without alienating the traditionalist grandees; Intelligence check (roll 1d20 under Int) to uncover an obscure legal loophole in the <em>Libro de las Horas Reales</em>.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the PCs support Belisario, Valenza cuts off royal palace wine rations, stationing cavalry outside the Alcázar gates to starve out the Seneschal's heralds.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Theft of the Golden Hours</h4>
  <p><strong>Premise:</strong> In the dead of night, the 900-page <em>Libro de las Horas Reales</em> is stolen from Belisario's high lectern in the Hall of Precedent. Belisario collapses into hysterical weeping, halting all official royal government until the sacred relic is recovered.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs discover that <a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a> stole the book on behalf of <a href="#npcs/sadoria" class="wiki-link">Marquis Sadoria</a>, who intends to burn the pages containing the royal veto. The PCs must sneak through the palace service flues to recover the tome before sunrise without triggering a public scandal.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Thief Move Silently or Dexterity check (roll 1d20 under Dex) to infiltrate Sadoria's private salon; Wisdom check (roll 1d20 under Wis) to identify the genuine parchment from forged substitutes.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If Sadoria discovers the PCs recovering the book, he accuses them of breaking into state archives, demanding an immediate Council tribunal.</p>
</div>
"""
        },
        {
            "id": "basto",
            "category": "npcs",
            "title": "Maestro Bartolomeo 'El Basto'",
            "subtitle": "Master Cook of the Cavernous Kitchens & Scullery Despot &bull; Palace Household / Domestic Guilds",
            "tags": ["Royal Court", "NPC", "Palace Staff", "Period VIII", "Gormenghast", "The Pit"],
            "aliases": ["Maestro Bartolomeo", "El Basto", "The Cleaver", "Master Cook", "Bartolomeo"],
            "summary": "The gargantuan, sweat-drenched culinary despot who rules the sweltering subterranean kitchens of the Alcázar with an iron cleaver and boiling fat. Beneath his despotic kitchen empire, he controls the dumbwaiters and grease flues connecting the palace directly to the black market of The Pit.",
            "stats": {
                "classLevel": "10th-Level Fighter (Scullery Despot)",
                "combatStats": "AC 3 (AAC 16) | HP 68 | THAC0 12 | Atk +11 (1d10+4) | Saves: 10/8/9/10/11",
                "alignment": "Neutral (Tyrannical glutton, ruthless pragmatist, subterranean smuggler)",
                "station": "Grand Escoffier of the Royal Alcázar & Master of the Roasting Pits",
                "ac": "AC 3 (AAC 16)",
                "acBreakdown": "Greased Boar-Hide Apron +2, Iron Kitchen Gorget, DEX 11",
                "hd": "9d8+8 (+18 CON bonus on first 9 HD)",
                "hp": 68,
                "move": "90' (30')",
                "thaco": "12 (Base Attack Bonus +7)",
                "attacks": "Melee: +11 to hit (The Ox-Cleaver *El Verdugo de las Reses*, 1d10+4 slashing); Off-hand: +9 to hit (Iron Basting Ladle, 1d4+2 bludgeoning + 1d6 fire from boiling tallow)",
                "abilities": [
                    ("STR", 18, "+3 to hit, +3 damage, Open Doors 1-5 on 1d6"),
                    ("DEX", 11, "Normal (0)"),
                    ("CON", 17, "+2 HP per Hit Die up to 9th level"),
                    ("INT", 13, "+1 language, brilliant culinary logistics & alchemy"),
                    ("WIS", 12, "Normal (0)"),
                    ("CHA", 12, "Commanding kitchen tyrant, Morale 9")
                ],
                "saves": [
                    ("Breath Weapon (BW)", 10),
                    ("Poison or Death (P/D)", 8),
                    ("Petrify or Paralyze (PP)", 9),
                    ("Wands (W)", 10),
                    ("Spells (S)", 11)
                ],
                "magicItems": [
                    "El Verdugo de las Reses (+2 Two-Handed Ox Cleaver; severs armor straps or shields on an attack roll of natural 19-20)",
                    "Girdle of the Iron Girth (Immune to all ingested poisons, spoiled food, rotting stenches, and magical nausea)",
                    "Vials of Chef's Nightshade (x3 doses of odorless, tasteless paralytic poison; save vs Poison or paralyzed 2d6 turns)",
                    "The Cauldron Key (Opens the subterranean grease flues and dumbwaiters dropping into The Pit)"
                ],
                "tactics": "<strong>Boiling Tallow Splash:</strong> Once per encounter, Bartolomeo can hurl a copper ladle of boiling fat in a 10' arc (2d6 fire damage; targets must roll 1d20 under Dex or fall prone on the grease-slicked stones).<br><strong>Kitchen Retinue:</strong> In his domain, he is surrounded by 6 burly turnspits (Fighters Level 2, AC 7, 12 HP each) and 4 shambling zombie kitchen thralls who turn spit-roasts without feeling heat.",
                "pcComparison": "A martial powerhouse with 68 HP and STR 18. In melee, he deals damage comparable to High Duke Gonzalo. Fighting him inside his sweltering subterranean kitchens—with boiling cauldrons, iron hooks, and slippery grease—gives him massive environmental advantage."
            },
            "atAGlance": {
                "appearance": "A colossal, mountainously obese brute weighing 340 pounds, glistening with sweat, pork lard, and wine stains. His hairy forearm is as thick as a ham, tattooed with a grinning sea-boar. He wields an iron ox-cleaver like a switch.",
                "mannerisms": "Bellows curses at terrified kitchen scullions; samples sauces with a greasy forefinger; wipes knife blades on his bloodstained leather apron; snorts contemptuously at aristocratic etiquette.",
                "quote": "His Grace wants peacock tongues in almond milk? Tell His Grace that peacocks don't sing in a famine, and if he complains again, I'll cook his pet mastiff in red wine.",
                "courtDCs": "Morale: 9 (Kitchen warlord); Initial Reaction: Gruff (0 on 2d6 Reaction Rolls). Charisma or Constitution check (eating his volcanic pepper-stew) to win his respect or secure covert passage down the dumbwaiters.",
                "publicStance": "Feigns uneducated rudeness and exhaustion, complaining endlessly about royal food budgets while secretly skimming thousands of gold pieces in luxury rations.",
                "secretAgenda": "To maintain his subterranean smuggling racket with Vesper the Key-Master in The Pit, exporting stolen palace silver, foreign truffles, and vintage wines in exchange for rare lotus extracts and underworld gold.",
                "rival": "Don Fernao de Silveira",
                "classLevel": "10th-Level Fighter (Scullery Despot)",
                "combatStats": "AC 3 (AAC 16) | HP 68 | THAC0 12 | Atk +11 (1d10+4) | Saves: 10/8/9/10/11"
            },
            "gmSecrets": "The great meat lifts and dumbwaiters behind the scullery hearths descend two hundred feet directly into the upper tunnels of <a href=\"#gazetteer/the-pit\" class=\"wiki-link\">The Pit</a>. Bartolomeo uses this secret elevator to smuggle fugitive duelists, stolen delicacies, and black-market gold. The PCs can use this shaft to bypass General Valenza's surface checkpoints entirely—if they pay Bartolomeo's price in rare spices or gold.",
            "relatedIds": ["palace-of-kordava", "the-pit", "vesper", "silveira", "escovedo", "court-matrix"],
            "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Palace Household &bull; Master Cook</span>
    <span class="badge rival-badge">Primary Rival: Don Fernao de Silveira</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A colossal, mountainously obese brute weighing 340 pounds, glistening with sweat, pork lard, and wine stains. His hairy forearm is as thick as a ham, tattooed with a grinning sea-boar. He wields an iron ox-cleaver like a switch.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Bellows curses at terrified kitchen scullions; samples sauces with a greasy forefinger; wipes knife blades on his bloodstained leather apron; snorts contemptuously at aristocratic etiquette.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;His Grace wants peacock tongues in almond milk? Tell His Grace that peacocks don't sing in a famine, and if he complains again, I'll cook his pet mastiff in red wine.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 9 (Kitchen warlord); Initial Reaction: Gruff (0 on 2d6 Reaction Rolls). Charisma or Constitution check (roll 1d20 under Con) to win his respect or secure covert passage down the dumbwaiters.</div>
  </div>
</div>

<h3>Public Persona &amp; Palace Duties</h3>
<p>Deep within the subterranean foundation of the High Alcázar lies the Great Scullery and Cavernous Kitchens—a sweltering, roaring inferno of iron cauldrons, charcoal smoke, and spitting tallow. Maestro Bartolomeo rules this subterranean empire as an absolute monarch. Eighty scullery boys, pastry apprentices, turnspits, and memory-retaining zombie scullions tremble before his thunderous voice and notched butcher's cleaver, <em>El Verdugo de las Reses</em>.</p>
<p>While the nobility feast on gilded pheasants and spun-sugar galleons on the crystal floors above, Bartolomeo controls what actually enters their bellies. He knows every grandee's culinary weaknesses, food allergies, and secret gluttonies.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>Bartolomeo is no simple cook: he is a key linchpin between the palace and <a href="#gazetteer/the-pit" class="wiki-link\">The Pit</a>. Behind the cavernous walk-in roasting chimneys are two massive, counter-weighted dumbwaiters originally designed to hoist coal from pre-Cataclysmic cellars. Bartolomeo uses these shafts to run a lucrative smuggling pipeline with <a href="#npcs/vesper" class="wiki-link">Vesper the Key-Master</a>. He can smuggle the PCs (or their covert agents) out of the palace past Valenza's perimeter guards in less than ten minutes—or dump an inconvenient assassin's corpse down the grease chute.</p>
</div>

<h3>Faction Ties &amp; Palace Relationships</h3>
<ul>
  <li><strong><a href="#npcs/silveira" class="wiki-link">Don Fernao de Silveira</a>:</strong> An epic, thirty-year blood feud. Bartolomeo considers Fernao a "rattling bag of dry twigs" who starves on punctilio; Fernao considers Bartolomeo a slovenly, treasonous swine who tracks lard across royal carpets. They carry daggers whenever they pass in the corridors.</li>
  <li><strong><a href="#npcs/vesper" class="wiki-link">Vesper the Key-Master</a>:</strong> Business partners. Bartolomeo supplies Vesper with vintage royal reserve brandies and palace gossip; Vesper pays in untraceable silver and subterranean truffles.</li>
  <li><strong><a href="#npcs/escovedo" class="wiki-link">Dr. Horatio Escovedo</a>:</strong> A nervous truce. Escovedo frequently inspects the kitchen larders for suspected poisons; Bartolomeo retaliates by feeding the doctor fiery curries that upset his delicate stomach.</li>
</ul>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Banquet of the Black River Sturgeon</h4>
  <p><strong>Premise:</strong> A crucial state gala for foreign grandees and the Argossean envoy is scheduled. Three hours before the feast, Maestro Bartolomeo storms into the Triumvirate's private solar, declaring that the royal treasury has failed to pay the butcher guild, and the scullions are staging a sit-down strike over their cold broth rations.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must either pay 500 gold pieces from their personal purse, use martial intimidation, or mediate between Bartolomeo and the scullions before the foreign ambassadors arrive to find cold bread and empty platters.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Charisma check (roll 1d20 under Cha) to negotiate with Bartolomeo; Strength check (roll 1d20 under Str) to win a drinking contest or physical arm-wrestle against the cook.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the PCs fail to resolve the strike, Bartolomeo serves salted hardtack and vinegar to <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a>, who interprets it as a deliberate diplomatic insult against Argos.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Corpse in the Dumbwaiter</h4>
  <p><strong>Premise:</strong> At midnight, Bartolomeo frantically signals the PCs via a secret kitchen bell. Stuck halfway down the subterranean meat shaft between the palace and The Pit is the body of a royal courier carrying an intercepted cipher signed by <a href="#npcs/sadoria" class="wiki-link">Marquis Sadoria</a>.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must descend into the greasy, vertical chimney flue to retrieve the body and the cipher before morning kitchen preparations begin, avoiding the mechanical counterweights and zombie thralls patrolling below.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Dexterity check (roll 1d20 under Dex) or Thief Climb Walls to rappel down the grease-slicked flue; Strength check (roll 1d20 under Str) to pry open the jammed bronze pulley gears.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the winch collapses, the crashing dumbwaiter alerts General Valenza's guards in the sub-cellar, who believe an underworld invasion is underway.</p>
</div>
"""
        },
        {
            "id": "silveira",
            "category": "npcs",
            "title": "Don Fernao de Silveira",
            "subtitle": "Lord of the Royal Bedchamber & Master of the Three Hundred Keys &bull; Palace Household / Loyalists",
            "tags": ["Royal Court", "NPC", "Palace Staff", "Period VIII", "Gormenghast", "Court Intrigue"],
            "aliases": ["Don Fernao", "Fernao de Silveira", "Lord Chamberlain", "Keeper of the Keys", "The Clicking Lord"],
            "summary": "The gaunt, severe Lord of the Bedchamber whose dry knee joints click rhythmically with every step. Unbribable and fanatically loyal to the Ancillus bloodline, he wanders the draughty corridors at 3:00 AM carrying a chatelaine of three hundred keys, hunting assassins and protecting the young Triumvirate.",
            "stats": {
                "classLevel": "10th-Level Thief / Royal Retainer",
                "combatStats": "AC 2 (AAC 17) | HP 44 | THAC0 14 | Atk +8 (1d6+2) | Backstab x4 | Saves: 13/10/9/11/12",
                "alignment": "Lawful (Austere, unbribable monarchist, fanatically loyal to the Ancillus bloodline)",
                "station": "Lord Chamberlain of the Bedchamber & Senior Gentleman of the Privy Stool",
                "ac": "AC 2 (AAC 17)",
                "acBreakdown": "Supple Silk-Lined Leather +2, Ring of Protection +1, DEX 15 (-1)",
                "hd": "9d4+4 (+9 CON bonus on first 9 HD)",
                "hp": 44,
                "move": "120' (40')",
                "thaco": "14 (Base Attack Bonus +5)",
                "attacks": "Zingaran Stiletto Rapier +2 (+8 to hit, 1d6+2 piercing); Concealed Spring-Loaded Wrist Crossbow (+8 to hit, 1d4 damage + sleep venom [save vs Poison or fall unconscious 1d6 turns], range 30')",
                "abilities": [
                    ("STR", 12, "Normal (0)"),
                    ("DEX", 15, "+1 missile to hit, -1 AC bonus"),
                    ("CON", 14, "+1 HP per Hit Die up to 9th level"),
                    ("INT", 15, "+1 language, encyclopedic knowledge of palace architecture"),
                    ("WIS", 16, "+2 saves vs magic, extraordinary alertness"),
                    ("CHA", 11, "Grim, unsmiling, severe demeanor")
                ],
                "saves": [
                    ("Breath Weapon (BW)", 13),
                    ("Poison or Death (P/D)", 10),
                    ("Petrify or Paralyze (PP)", 9),
                    ("Wands (W)", 11),
                    ("Spells (S)", 12)  # Base 14 - 2 for WIS 16
                ],
                "thiefSkills": [
                    ("Pick Pockets", "65%"),
                    ("Open Locks", "85%"),
                    ("Find/Remove Traps", "75%"),
                    ("Move Silently", "70%"),
                    ("Climb Walls", "90%"),
                    ("Hide in Shadows", "60%"),
                    ("Hear Noise", "1-4 on 1d6")
                ],
                "magicItems": [
                    "The Great Chatelaine of Kalenius (Iron ring of 300 ancient keys; opens every non-magical lock in the Alcázar and hums when within 10' of a secret door)",
                    "Stiletto of the Night Watch (+2 Zingaran parrying blade; tip turns bright purple if dipped into any poison)",
                    "Boots of the Shadow Walk (Muffles the clicking of his dry knee joint when moving silently in darkness)",
                    "Amulet of Non-Detection (Shields his location from magical scrying and divination spells)"
                ],
                "tactics": "<strong>Tapestry Ambush:</strong> Fernao never attacks from the open. He strikes from behind velvet arras (Backstab x4 for 4d6+8 damage), blinds foes with thrown pepper-dust, or fires his poisoned sleeve crossbow before retreating through concealed jib-doors.<br><strong>Master of the Locks:</strong> Can lock or bar any door in the Alcázar in 1 combat segment, dividing attacking forces.",
                "pcComparison": "While not a frontline tank like Valenza or Bartolomeo, Fernao's intimate mastery of palace secret doors, acoustic spy-tubes, and master keys makes him the PCs' most invaluable protector within the walls."
            },
            "atAGlance": {
                "appearance": "A tall, skeletal figure in threadbare, impeccably brushed black velvet. He has high, flint-like cheekbones, hollow eyes, and silver hair tied back with a black ribbon. His left knee joint pops with a dry, rhythmic click (*crack... crack...*) as he walks.",
                "mannerisms": "Never blinks while speaking; glides soundlessly until his knee pops; touches his heavy iron keyrings constantly; inspects door hinges and window latches compulsively.",
                "quote": "A monarch who trusts his Council is a corpse waiting for a shroud. Sleep with your boots on, Your Majesties. I have locked the west gallery, but the rats have teeth tonight.",
                "courtDCs": "Morale: 11 (Unyielding protector); Initial Reaction: Gruff Respect (+1 on 2d6 Reaction Rolls for true Ancillus descendants). Wisdom check to spot him shadowing the PCs through corridors.",
                "publicStance": "Treats all grandees, ministers, and foreign ambassadors with frigid, contemptuous formality, acknowledging only the direct blood of King Ancillus I.",
                "secretAgenda": "To purge the Restoration Council's spies from the royal bedchambers, preserve the Triumvirate from assassination, and maintain royal control over the Sealed Solares (the walled-off apartments of the ancient kings).",
                "rival": "Maestro Bartolomeo 'El Basto'",
                "classLevel": "10th-Level Thief / Royal Retainer",
                "combatStats": "AC 2 (AAC 17) | HP 44 | THAC0 14 | Atk +8 (1d6+2) | Backstab x4 | Saves: 13/10/9/11/12"
            },
            "gmSecrets": "Fernao possesses the only working master key to the *Sealed Solares*—the royal apartments walled off eighty years ago after the Black Solstice massacre. Inside lies the private treasury and genealogical vault of the old kings. Furthermore, Fernao knows a secret acoustic peephole behind a tapestry in the Queen's Gallery that looks directly down into Marquis Sadoria's private salon.",
            "relatedIds": ["palace-of-kordava", "basto", "obregon", "sadoria", "valenza", "court-matrix"],
            "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Palace Household &bull; Lord Chamberlain</span>
    <span class="badge rival-badge">Primary Rival: Maestro Bartolomeo 'El Basto'</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A tall, skeletal figure in threadbare, impeccably brushed black velvet. He has high, flint-like cheekbones, hollow eyes, and silver hair tied back with a black ribbon. His left knee joint pops with a dry, rhythmic click (<em>crack... crack...</em>) as he walks.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Never blinks while speaking; glides soundlessly until his knee pops; touches his heavy iron keyrings constantly; inspects door hinges and window latches compulsively.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;A monarch who trusts his Council is a corpse waiting for a shroud. Sleep with your boots on, Your Majesties. I have locked the west gallery, but the rats have teeth tonight.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 11 (Unyielding protector); Initial Reaction: Gruff Respect (+1 on 2d6 Reaction Rolls for true Ancillus descendants). Wisdom check (roll 1d20 under Wis) to spot him shadowing the PCs through corridors.</div>
  </div>
</div>

<h3>Public Persona &amp; Palace Duties</h3>
<p>Don Fernao de Silveira is the guardian of the sovereigns' sleep. While the military guards of <a href="#npcs/valenza" class="wiki-link">General Valenza</a> stand watch at outer portcullises and palace gates, Don Fernao controls the interior corridors, bedchambers, and private solares of the High Alcázar. Gaunt, severe, and incorruptible, he carries the Great Chatelaine of Kalenius—a cluster of three hundred iron, brass, and obsidian keys that unlock every private lock in the citadel.</p>
<p>He is legendary for his nocturnal vigils. Between the hours of midnight and dawn, Fernao patrols the draughty stone halls in felt slippers, accompanied only by the dry, rhythmic clicking of his damaged knee joint (<em>crack... crack...</em>), hunting unauthorized courtiers, listening at spyholes, and verifying that every deadbolt is thrown.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>Fernao owes no allegiance to <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a> or the Restoration Council. He views them as parasitic opportunists who stole the crown's authority. He has dedicated his remaining years to keeping the young Triumvirate alive. He knows that Sadoria has planted two dagger-wielding assassins among the palace footmen; he has not killed them yet because he is waiting for them to receive written orders from Sadoria to provide the PCs with unassailable proof of high treason.</p>
</div>

<h3>Faction Ties &amp; Palace Relationships</h3>
<ul>
  <li><strong><a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo</a>:</strong> A vicious feud. Fernao believes Bartolomeo's greasy kitchen empire is a cesspool of republican smuggling and gluttony; Bartolomeo once hurled a roasted turnip at Fernao's head during a state dinner.</li>
  <li><strong><a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a>:</strong> Cold, silent war. Sadoria has tried four times to replace Fernao with a pliable courtier; Fernao routinely locks Sadoria's clerks out of royal ante-rooms using forgotten municipal fire codes.</li>
  <li><strong><a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a>:</strong> Deep suspicion. Fernao recognizes that Ignacio climbs through palace flues and knows too many secrets, and is actively seeking an excuse to hang the young scrivener from the sea-ramparts.</li>
</ul>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Whispering Gallery of Sadoria</h4>
  <p><strong>Premise:</strong> At two in the morning, Don Fernao taps on the Triumvirate's bedchamber door. He leads the PCs through a narrow masonry crawlspace behind the tapestries to a hollow decorative frieze positioned directly above Marquis Sadoria's private salon, where Sadoria is currently meeting with a foreign conspirator.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs can listen to the conspiracy (discovering that Sadoria is embezzling crown naval timber for foreign merchant cartels), but an acoustic draft threatens to extinguish their candle or blow soot into the salon below.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Thief Move Silently or Dexterity check (roll 1d20 under Dex) to hold motionless inside the stone crawlspace; Wisdom check (roll 1d20 under Wis) to transcribe the ciphered dialect.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If discovered, Sadoria's guards rush the crawlspace; Fernao must lock the iron fire-door behind the PCs, holding off the attackers alone with his rapier.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Key to the Sealed Solares</h4>
  <p><strong>Premise:</strong> Facing imminent bankruptcy and unable to pay the city watch, Don Fernao offers the PCs his most dangerous secret: the heavy obsidian key to the *Sealed Solares*, a wing of the palace walled up eighty years ago after the Black Solstice massacre, where the private emergency bullion of King Daedalus is rumored to remain.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must breach the bricked-up entryway in secret, explore the dust-choked, trap-ridden apartments, and retrieve the royal bullion chests while contending with the restless spectral remnants of the slaughtered court.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Thief Find/Remove Traps or Dexterity check (roll 1d20 under Dex) to disarm pre-deluvial spring-scythe traps; Cleric Turn Undead (or Wisdom check) to banish the wailing phantoms of the Black Solstice.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> Breaching the sealed wing releases eighty years of accumulated necrotic gas into the ventilation flues, causing palace servants in the wing below to suffer violent hallucinations.</p>
</div>
"""
        },
        {
            "id": "escovedo",
            "category": "npcs",
            "title": "Dr. Horatio Escovedo",
            "subtitle": "Chief Royal Chirurgeon & Court Toxicologist &bull; Palace Household / Scholarly Guilds",
            "tags": ["Royal Court", "NPC", "Palace Staff", "Period VIII", "Gormenghast", "Alchemy"],
            "aliases": ["Dr. Escovedo", "Horatio Escovedo", "Royal Chirurgeon", "Court Toxicologist", "The Doctor"],
            "summary": "The hyper-kinetic, smoked-quartz-bespectacled chief court physician whose manic giggles and torrent of Latin circumlocutions conceal a terrifyingly sharp clinical intellect. He tests the Triumvirate's food for venom, analyzes necrotic tissue, and secretly brews life-saving antidotes for the PCs.",
            "stats": {
                "classLevel": "10th-Level Magic-User / Physician",
                "combatStats": "AC 4 (AAC 15) | HP 32 | THAC0 17 | Atk +6 (1d4 + Elixir) | Saves: 13/11/11/11/12",
                "alignment": "Neutral (Eccentric scholar, hypochondriac humanist, terrified conspirator)",
                "station": "Chief Physician to the Royal Household & Master of the Palace Scriptorium-Apothecary",
                "ac": "AC 4 (AAC 15)",
                "acBreakdown": "Concealed Quilted Silk Doublet +1, Ring of Shielding (+1 AC), DEX 16 (-2)",
                "hd": "9d4+2 (+9 CON bonus on first 9 HD)",
                "hp": 32,
                "move": "120' (40')",
                "thaco": "17 (Base Attack Bonus +4)",
                "attacks": "Silver Surgical Scalpel +1 (+6 to hit, 1d4 damage + paralytic essence [save vs Poison or paralyzed for 2d4 turns])",
                "abilities": [
                    ("STR", 9, "Normal (0)"),
                    ("DEX", 16, "+2 missile to hit, -2 AC bonus"),
                    ("CON", 14, "+1 HP per Hit Die up to 9th level"),
                    ("INT", 18, "+3 languages, master of anatomy, alchemy, and toxicology"),
                    ("WIS", 15, "+1 saves vs magic, diagnostic brilliance"),
                    ("CHA", 13, "+1 reaction, high-strung eccentric charm")
                ],
                "saves": [
                    ("Breath Weapon (BW)", 13),
                    ("Poison or Death (P/D)", 11),
                    ("Petrify or Paralyze (PP)", 11),
                    ("Wands (W)", 11),
                    ("Spells (S)", 12)
                ],
                "spellsPrepared": [
                    ("1st Circle", "Sleep, Detect Magic, Hold Portal, Read Languages"),
                    ("2nd Circle", "Invisibility, Locate Object, Mirror Image"),
                    ("3rd Circle", "Dispel Magic, Haste"),
                    ("4th Circle", "Confusion, Polymorph Self"),
                    ("5th Circle", "Feeblemind")
                ],
                "magicItems": [
                    "The Smoked-Quartz Spectacles of Truth (Enchanted lenses; reveals poisoned food, necrotic decay, invisible creatures, and concealed wounds upon glance)",
                    "Apothecary's Bandolier of Panaceas (Contains 4 universal antitoxins, 2 draughts of restoration [cures disease/paralysis], and 2 flash-globes of blinding powder)",
                    "Cane of the Two-Headed Viper (Hollow cane containing 6 doses of fast-acting belladonna antidote)",
                    "Ring of Shielding (+1 bonus to Armor Class, included in stats)"
                ],
                "tactics": "<strong>Flash-Globe & Vanish:</strong> If attacked, Escovedo smashes a phosphorus globe onto the stones (all within 10' must save vs Wands or be blinded 1d4 rounds), then immediately casts <em>Invisibility</em> or <em>Mirror Image</em>.<br><strong>Toxicological Defense:</strong> Wields an alchemically treated silver scalpel coated in paralyzing manticore secretion.",
                "pcComparison": "Frail in prolonged physical combat (32 HP), but possessor of 5th-circle arcane magic (matching Master Alchemist Vane) and genius-level intelligence (INT 18). He is the only person in Kordava capable of neutralizing Sadoria's subtle metabolic poisons."
            },
            "atAGlance": {
                "appearance": "Rail-thin, bird-like, clad in a faded plum velvet doublet with ink-stained lace ruffles. He wears thick, round smoked-quartz spectacles that give him the appearance of an enormous, inquisitive mantis. His long, spindly fingers flutter constantly.",
                "mannerisms": "Bursts into sudden, high-pitched musical laughs (*He-he-he! Exquisite!*); taps the ribs of courtiers with his brass stethoscope; speaks in breathless, torrential paragraphs filled with multi-syllabic medical Latin.",
                "quote": "A slight constriction of the radial pulse, Sire! Most delightful! Either Your Majesty has ingested three grains of dried wyvern gallbladder in your morning pheasant, or your aunt is visiting. Let us administer the black hellebore at once!",
                "courtDCs": "Morale: 7 (Nervous intellectual); Initial Reaction: Friendly (+2 on 2d6 Reaction Rolls for anyone discussing medicine or anatomy). Intelligence check to translate his rambling diagnostic advice into practical clues.",
                "publicStance": "Plays the part of an eccentric, harmless academic who is completely oblivious to power politics and interested only in bile, humors, and rare herbs.",
                "secretAgenda": "Tortured by guilt because Marquis Sadoria coerced him into brewing the slow-acting heart tincture that murdered the previous regent. Escovedo is fanatically determined to protect the Triumvirate, slipping antidotes into their wine disguised as 'restorative digestive elixirs.'",
                "rival": "Master Alchemist Vane",
                "classLevel": "10th-Level Magic-User / Physician",
                "combatStats": "AC 4 (AAC 15) | HP 32 | THAC0 17 | Atk +6 (1d4 + Elixir) | Saves: 13/11/11/11/12"
            },
            "gmSecrets": "Escovedo keeps a locked lead-lined journal beneath the flagstones of his dissecting theater. It contains detailed forensic records proving that the late King Daedalus's brother was poisoned with concentrated nightshade supplied by <a href=\"#npcs/sadoria\" class=\"wiki-link\">Marquis Sadoria</a>. Escovedo lives in perpetual terror that Sadoria's cutthroats will slit his throat, which is why he always carries three doses of universal antitoxin on his person.",
            "relatedIds": ["palace-of-kordava", "sadoria", "vane", "basto", "court-matrix"],
            "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Palace Household &bull; Chief Chirurgeon</span>
    <span class="badge rival-badge">Primary Rival: Master Alchemist Vane</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> Rail-thin, bird-like, clad in a faded plum velvet doublet with ink-stained lace ruffles. He wears thick, round smoked-quartz spectacles that give him the appearance of an enormous, inquisitive mantis. His long, spindly fingers flutter constantly.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Bursts into sudden, high-pitched musical laughs (<em>He-he-he! Exquisite!</em>); taps the ribs of courtiers with his brass stethoscope; speaks in breathless, torrential paragraphs filled with multi-syllabic medical Latin.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;A slight constriction of the radial pulse, Sire! Most delightful! Either Your Majesty has ingested three grains of dried wyvern gallbladder in your morning pheasant, or your aunt is visiting. Let us administer the black hellebore at once!&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 7 (Nervous intellectual); Initial Reaction: Friendly (+2 on 2d6 Reaction Rolls for anyone discussing medicine or anatomy). Intelligence check (roll 1d20 under Int) to translate his rambling diagnostic advice into practical clues.</div>
  </div>
</div>

<h3>Public Persona &amp; Palace Duties</h3>
<p>Dr. Horatio Escovedo is the court physician, chief toxicologist, and master of the royal apothecary. Perched in the breezy Dissecting Tower above the sea-ramparts, he treats the ailments of the royal household, tastes official sovereign medicines, and delivers grand, bewildering medical lectures at the drop of a hat. Courtiers treat him as an amusing eccentric, chuckling at his frantic gesticulations and shrill laughter.</p>
<p>Behind this comic veneer lies one of the sharpest analytical minds in ancient Zingara. Escovedo can diagnose a poison by the smell of a sweat-soaked handkerchief, detect concealed daggers with his lodestone rods, and deduce a courtier's secret vices from the color of their tongue.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>Escovedo is haunted by his past. Six months before the campaign began, <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a> threatened to have Escovedo's sister burned as a witch by the Church of Nemeth unless the doctor prepared a slow, undetectable metabolic poison for the Regent Don Carlos. Escovedo complied, and Carlos died in his sleep of "cardiac melancholy." Consumed by remorse, Escovedo now views the PC Triumvirate as his only chance for redemption. He secretly spikes their morning tea with preventative broad-spectrum antidotes and constantly monitors their vitals for signs of Council tampering.</p>
</div>

<h3>Faction Ties &amp; Palace Relationships</h3>
<ul>
  <li><strong><a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a>:</strong> A relationship of terrified subordination. Sadoria believes he owns the doctor; Escovedo smiles obsequiously while hoarding toxicological evidence against the Chancellor.</li>
  <li><strong><a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a>:</strong> Bitter academic rivalry. Escovedo despises Vane's crude, necrotic reanimation rites as "vulgar butcher's necromancy," whereas Vane considers Escovedo an effete herbalist who lacks the courage to master true death-magic.</li>
  <li><strong><a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo</a>:</strong> A combative working relationship. Escovedo inspects the royal kitchens three times a week with silver testing-spoons, driving Bartolomeo into apoplectic rages.</li>
</ul>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Venom in the Communion Chalice</h4>
  <p><strong>Premise:</strong> During morning Mass in the Palace Chapel, Dr. Escovedo franticly spills the sacramental wine across the altar flagstones, screaming that the wine has turned "an improper shade of lilac." Father Malachai's priests accuse the doctor of sacrilegious blasphemy and demand his arrest.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must protect their trembling physician from the Church of Nemeth while helping him perform a field chemical test on the spilled wine to prove it was laced with concentrated nightshade intended for the Triumvirate.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Charisma check (roll 1d20 under Cha) to restrain the angry temple guards; Intelligence check (roll 1d20 under Int) to assist Escovedo in identifying the alchemical signature of the poison.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the poison is proven, the trail leads directly to a trusted royal cupbearer bribed by a rival provincial grandee, sparking an immediate palace-wide witch hunt.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Necrotic Autopsy</h4>
  <p><strong>Premise:</strong> Escovedo secretly summons the PCs to his dissecting theater at midnight. On the slab is a deceased zombie thrall recovered from the palace foundations, whose marrow has begun crystallizing into glowing, explosive black glass—identical to the residue found in the ruins of the pre-deluvial academy.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Escovedo warns that the alchemical catalyst being used by <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a> in The Pit is unstable; within weeks, hundreds of working thralls beneath Kordava could spontaneously detonate, collapsing the city's foundations into the sea.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Wisdom check (roll 1d20 under Wis) to extract the fragile crystal gland without detonating it (inflicts 4d6 damage on failure); Charisma check to convince Vane or the Council to pause thrall production.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the Council ignores the warning, a micro-tremor shakes the Alcázar, shattering twenty feet of the Throne Room's crystal floor.</p>
</div>
"""
        },
        {
            "id": "ignacio",
            "category": "npcs",
            "title": "Ignacio Mora",
            "subtitle": "The Climbing Scrivener & Scribe of the Sump &bull; Low Palace Bureaucracy / Master Infiltrator",
            "tags": ["Royal Court", "NPC", "Palace Staff", "Period VIII", "Gormenghast", "Underworld"],
            "aliases": ["Ignacio Mora", "Ignacio", "The Climbing Scrivener", "Scribe of the Sump", "The Climber"],
            "summary": "A pale, wiry, deceptively deferential young clerk who climbs the dizzying exterior sea-cliffs and interior ventilation flues of the Alcázar. Knowing every crawlspace and secret in the citadel, he plays all factions against each other as he ruthlessly schemes to rise from gutter to Grand Chancellor.",
            "stats": {
                "classLevel": "9th-Level Thief / Palace Infiltrator",
                "combatStats": "AC 1 (AAC 18) | HP 40 | THAC0 15 | Atk +9 (1d4+3 + Venom) | Backstab x4 | Saves: 13/11/10/12/13",
                "alignment": "Chaotic (Ruthless ambition, cold calculation, brilliant opportunist)",
                "station": "Under-Clerk of the Bureau of Wax & Salt Receipts / Independent Palace Intriguer",
                "ac": "AC 1 (AAC 18)",
                "acBreakdown": "Soft-Tanned Cat-Skin Leather +1, Ring of Protection +1, DEX 18 (-3)",
                "hd": "9d4+4 (+9 CON bonus on first 9 HD)",
                "hp": 40,
                "move": "120' (40')",
                "thaco": "15 (Base Attack Bonus +5)",
                "attacks": "Concealed Ebony Bodkin +2 (+9 to hit, 1d4+3 piercing + black lotus venom [save vs Poison at -2 or take 3d6 damage and collapse unconscious]); Thrown Throwing Needles +8 (1d3 + venom, range 20')",
                "abilities": [
                    ("STR", 11, "Normal (0)"),
                    ("DEX", 18, "+3 missile to hit, -3 AC bonus, master climber"),
                    ("CON", 14, "+1 HP per Hit Die up to 9th level"),
                    ("INT", 17, "+2 languages, photographic architectural memory"),
                    ("WIS", 12, "Normal (0)"),
                    ("CHA", 15, "+1 reaction, honeyed deferential charm")
                ],
                "saves": [
                    ("Breath Weapon (BW)", 13),
                    ("Poison or Death (P/D)", 11),
                    ("Petrify or Paralyze (PP)", 10),
                    ("Wands (W)", 12),
                    ("Spells (S)", 13)
                ],
                "thiefSkills": [
                    ("Pick Pockets", "80%"),
                    ("Open Locks", "75%"),
                    ("Find/Remove Traps", "70%"),
                    ("Move Silently", "80%"),
                    ("Climb Walls", "96%"),
                    ("Hide in Shadows", "70%"),
                    ("Hear Noise", "1-4 on 1d6")
                ],
                "magicItems": [
                    "Spider-Silk Slippers (Allow silent walking upon slate rooftops, vertical masonry, and sheer marble cornices)",
                    "The Wax-Seal of Forgery (A pre-Cataclysmic bronze stylus that can reproduce any noble or royal wax seal in 1 round)",
                    "Chime of Opening (Ancient silver cylinder, 4 charges remaining; opens barred doors and heavy iron grates silently)",
                    "Grappling Line of Kalenius (Unbreakable 100' spider-silk cord, coils itself on command)"
                ],
                "tactics": "<strong>Vertical Ambush & Vanish:</strong> Ignacio never fights on open ground. He drops from ceiling rafters, chandeliers, or chimney cornices (Backstab x4 for 4d4+12 damage + lotus poison), then scurries up a sheer flue or out an arrow-slit into the ocean gale.<br><strong>Flue-Running:</strong> Can navigate the palace's network of masonry flues and acoustic shafts at full running speed (120' per round).",
                "pcComparison": "A lethally agile rogue (DEX 18, Climb Walls 96%). While he cannot withstand a pitched battle with the PC Warrior, his ability to enter any room in the Alcázar unannounced makes him an existential intelligence threat or an invaluable spy."
            },
            "atAGlance": {
                "appearance": "A pale, slender youth of twenty-two with soot-stained knuckles, dark intelligent eyes, and quiet, cat-like footfalls. Wears a slightly frayed ink-spotted scribe's robe over supple, oil-treated leather. Outwardly bows until his forehead brushes his knees.",
                "mannerisms": "Speaks in a timid, halting whisper; keeps his eyes cast submissively downward while taking in every detail of the room; compulsively cleans ink from under his fingernails with a bone stylus.",
                "quote": "A low-born clerk hears nothing, Your Majesty, sees nothing, and forgets everything... unless, of course, Your Majesty desires to know why the Marquis was burning ledgers at three in the morning.",
                "courtDCs": "Morale: 8 (Cold pragmatist); Initial Reaction: Fawning / Calculating (0 on 2d6 Reaction Rolls). Charisma or Intelligence check to detect that his humble stammering is an act.",
                "publicStance": "The humble, overworked junior assistant in the Bureau of Salt & Wax Receipts who quietly files requisitions and runs errands for high-ranking nobles.",
                "secretAgenda": "To climb ruthlessly to supreme power over the kingdom's bureaucracy by playing the Council, the Church, the Republicans, and the Triumvirate against each other until he alone holds the reins of the state.",
                "rival": "Don Fernao de Silveira",
                "classLevel": "9th-Level Thief / Palace Infiltrator",
                "combatStats": "AC 1 (AAC 18) | HP 40 | THAC0 15 | Atk +9 (1d4+3 + Venom) | Backstab x4 | Saves: 13/11/10/12/13"
            },
            "gmSecrets": "Ignacio has discovered a forgotten pre-Cataclysmic mechanical chamber in the sub-cellars beneath the palace that controls the bronze sluice gates beneath the Crystal Floor. With the turn of a corroded wheel, he can drain the defensive moat, flood the lower dungeons, or vent toxic subterranean vapors from The Pit directly into the Grand Ballroom.",
            "relatedIds": ["palace-of-kordava", "silveira", "sadoria", "lucia", "vesper", "court-matrix"],
            "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Palace Household &bull; Bureau of Receipts</span>
    <span class="badge rival-badge">Primary Rival: Don Fernao de Silveira</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A pale, slender youth of twenty-two with soot-stained knuckles, dark intelligent eyes, and quiet, cat-like footfalls. Wears a slightly frayed ink-spotted scribe's robe over supple, oil-treated leather. Outwardly bows until his forehead brushes his knees.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Speaks in a timid, halting whisper; keeps his eyes cast submissively downward while taking in every detail of the room; compulsively cleans ink from under his fingernails with a bone stylus.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;A low-born clerk hears nothing, Your Majesty, sees nothing, and forgets everything... unless, of course, Your Majesty desires to know why the Marquis was burning ledgers at three in the morning.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 8 (Cold pragmatist); Initial Reaction: Fawning / Calculating (0 on 2d6 Reaction Rolls). Charisma or Intelligence check (roll 1d20 under Int) to detect that his humble stammering is an act.</div>
  </div>
</div>

<h3>Public Persona &amp; Palace Duties</h3>
<p>Officially, Ignacio Mora is the least significant person in the High Alcázar. As the third junior scrivener in the Bureau of Wax &amp; Salt Receipts, his official duties consist of counting tallow candles, filing provincial grain vouchers, and carrying bundles of parchment between ministry offices. He bows frantically to every passing grandee, stammering apologies for breathing the same air as his betters.</p>
<p>In reality, Ignacio is the supreme climber of Kordava—a prodigy of acrobatics, infiltration, and psychological manipulation who knows every flue, duct, chimney, and secret crawlspace in the citadel. By night, he strips off his scribe's gown, dons cat-skin leather, and runs across the dizzying slate roofs and gargoyles high above the crashing ocean surf, slipping into locked state apartments to read private correspondence.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>Ignacio is the Steerpike of Zingara. Born in the gutters of The Pit, he is animated by a ferocious, icy hatred of the hereditary aristocracy. He sells Council eavesdrops to <a href="#npcs/lucia" class="wiki-link">Lucia's republicans</a>, passes forged invoices to <a href="#npcs/sadoria" class="wiki-link">Marquis Sadoria</a>, and reports guard rotations to <a href="#npcs/vesper" class="wiki-link">Vesper</a>. His ultimate objective is not wealth, but total, unassailable administrative control: he intends to manufacture a catastrophic court scandal that wipes out both Valenza and Sadoria, positioning himself as the indispensable Chief Minister to the Triumvirate.</p>
</div>

<h3>Faction Ties &amp; Palace Relationships</h3>
<ul>
  <li><strong><a href="#npcs/silveira" class="wiki-link">Don Fernao de Silveira</a>:</strong> Mortal enemies in the shadows. Fernao knows someone is climbing through the palace flues and has laid poisoned caltrops in several chimney shafts; Ignacio enjoys outmaneuvering the old Chamberlain by inches.</li>
  <li><strong><a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a>:</strong> Ignacio plays the role of Sadoria's eager, terrified informant, feeding the Chancellor just enough true information to win his trust while copying Sadoria's most incriminating ciphers.</li>
  <li><strong><a href="#npcs/lucia" class="wiki-link">Fencing Master Lucia</a>:</strong> Clandestine informant. Ignacio provides Lucia's rebel cells with maps of palace guard rotations, though Lucia distrusts his cold, amoral ambition.</li>
</ul>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Scrivener's Bargain</h4>
  <p><strong>Premise:</strong> While the Triumvirate is meeting in their private solar, a ceiling grate slides open and Ignacio drops soundlessly onto the carpet. Bowing low, he produces a wax-sealed packet containing the secret minutes of last night's Restoration Council meeting, in which Sadoria proposed mortgaging the royal palace to the Kingdom of Argos.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Ignacio offers to become the PCs' personal secret agent inside the bureaucracy—for a price: a royal patent appointing him Chief Clerk of the Treasury and diplomatic immunity from Don Fernao's watch.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Wisdom check (roll 1d20 under Wis) to discern if the documents are genuine or a double-agent trap; Charisma check (roll 1d20 under Cha) to extract additional secrets without signing over legal immunity.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the PCs reject him, Ignacio sells the documents to foreign ambassadors, precipitating an immediate international financial panic.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Sluice of the Pit</h4>
  <p><strong>Premise:</strong> Ignacio discovers that republican insurgents from The Pit are preparing to detonate black powder beneath the Palace Cauldron Courtyard. Rather than informing the guard, Ignacio offers to guide the PCs through the sheer sea-cliff flues to disarm the sappers personally.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must climb the exterior face of the sea-ramparts at midnight during an ocean gale, following Ignacio across narrow masonry ledges where one slip means death on the jagged reefs three hundred feet below.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Dexterity check (roll 1d20 under Dex) or Thief Climb Walls to traverse the gale-swept parapets; Strength check (roll 1d20 under Str) to dismantle the powder kegs before the fuses burn down.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> During the climb, Ignacio attempts to pickpocket a royal signet ring from one of the PCs to seal his own forged promotion decrees.</p>
</div>
"""
        },
        {
            "id": "elvira",
            "category": "npcs",
            "title": "Doña Elvira de Ancillus-Moreno",
            "subtitle": "The Dowager Infanta & Keeper of the White Falcons &bull; Royal Bloodline / Reclusive Aristocracy",
            "tags": ["Royal Court", "NPC", "Palace Staff", "Period VIII", "Gormenghast", "Court Intrigue"],
            "aliases": ["Doña Elvira", "Elvira de Ancillus", "The Dowager Infanta", "Mistress of Falcons", "The Infanta"],
            "summary": "Great-aunt to the Triumvirate and sole surviving elder of the Ancillus dynasty. She lives in self-imposed exile in the windswept topmost spires of the Hanging Aviary, surrounded by forty white sea-falcons and sixty temple cats, utterly contemptuous of human politics yet possessing a lethal airborne spy network.",
            "stats": {
                "classLevel": "9th-Level Magic-User / Beastmistress",
                "combatStats": "AC 5 (AAC 14) | HP 34 | THAC0 17 | Atk +5 (1d6) | Saves: 14/12/12/12/13",
                "alignment": "Neutral (Imperial disdain, eccentric hermit, fiercely protective of her kin when roused)",
                "station": "Dowager Infanta of Zingara & Chatelaine of the High Spires and Aviary",
                "ac": "AC 5 (AAC 14)",
                "acBreakdown": "Ermine-Lined Mantle of Protection +2, DEX 9",
                "hd": "9d4+2 (+9 CON bonus on first 9 HD)",
                "hp": 34,
                "move": "90' (30')",
                "thaco": "17 (Base Attack Bonus +4)",
                "attacks": "Gilded Hunting Rod (+1 club, 1d6 damage); Commands 4 Hunting Falcons (+8 to hit, 1d4+2 talon slash, aim for eyes [save vs Paralysis or blinded for 1 turn])",
                "abilities": [
                    ("STR", 10, "Normal (0)"),
                    ("DEX", 9, "Normal (0)"),
                    ("CON", 14, "+1 HP per Hit Die up to 9th level"),
                    ("INT", 17, "+2 languages, master of arcane ornithology and dynastic history"),
                    ("WIS", 16, "+2 saves vs magic, supreme haughty perception"),
                    ("CHA", 17, "+2 reaction, imposing imperial presence, Morale 10")
                ],
                "saves": [
                    ("Breath Weapon (BW)", 14),
                    ("Poison or Death (P/D)", 12),
                    ("Petrify or Paralyze (PP)", 12),
                    ("Wands (W)", 12),
                    ("Spells (S)", 13)  # Base 15 - 2 for WIS 16
                ],
                "spellsPrepared": [
                    ("1st Circle", "Animal Friendship, Charm Person, Ventriloquism, Read Languages"),
                    ("2nd Circle", "Web, ESP, Phantasmal Force"),
                    ("3rd Circle", "Hold Person, Clairvoyance"),
                    ("4th Circle", "Confusion, Charm Monster"),
                    ("5th Circle", "Hold Monster")
                ],
                "magicItems": [
                    "The Silver Whistle of the Sea-Falcons (Summons a swarm of 20 fierce hunting falcons from the ocean cliffs within 2 combat rounds)",
                    "The Falcon-Eye Ring (Allows her to see and hear clairvoyantly through the senses of any bird she has fed within 10 miles)",
                    "Mantle of the Ermine Sovereign (+2 to Armor Class, grants total immunity to normal cold and gale-force winds)",
                    "Signet of Queen Sancha (Ancient royal seal granting access to high palace vaults)"
                ],
                "tactics": "<strong>The Falcon Squall:</strong> Elvira never engages in melee. She sounds her whistle to unleash a screaming vortex of 20 white sea-falcons (swarms attack as 5 HD monster, dealing 3d6 slashing damage per round and blinding foes) while casting <em>Web</em>, <em>Hold Person</em>, or <em>Confusion</em> from high balconies.<br><strong>Palace Mastiffs:</strong> Accompanied in her spires by two massive Zingaran Mastiffs (HD 4, AC 6, 22 HP, 2d4 bite).",
                "pcComparison": "A formidable spellcaster with high Charisma (CHA 17) and untouchable social immunity. Because she is the elder sister of King Ancillus I, neither Valenza nor Sadoria dare arrest or execute her without triggering immediate civil war among the loyalist grandees."
            },
            "atAGlance": {
                "appearance": "A massive, imperious matriarch of sixty-five draped in frayed silver damask, moth-eaten ermine, and pearls the size of pigeon eggs. She smells of sea salt, cedarwood, and birdlime. Perched on her leather gauntlet is a pure-white sea-falcon named 'Don Alfonso.'",
                "mannerisms": "Ignores speakers for minutes while feeding raw liver to her birds; addresses high dukes as 'foolish boys'; tosses chicken bones over the battlements; speaks with devastating, aristocratic drawl.",
                "quote": "General Valenza? You mean the blacksmith's grandson who plays with tin soldiers? Tell him if he marches his noisy cavalry beneath my aviaries again, my falcons will pluck out his remaining eye.",
                "courtDCs": "Morale: 10 (Regal sovereign); Initial Reaction: Cold / Imperial (0 on 2d6 Reaction Rolls; +2 for PCs showing proper deference to her birds). Charisma check to win her affection or gain access to her intercepted letters.",
                "publicStance": "Openly disdains the entire court, the Restoration Council, and the Church of Nemeth, living in high seclusion and refusing to set foot on the lower floors.",
                "secretAgenda": "Her hunting falcons patrol the skies over Kordava harbor and the Baracha Strait, routinely intercepting carrier pigeons, message ravens, and courier gulls. She hoards hundreds of intercepted ciphers in gilded birdcages, casually using them for cage linings or tossing them to the PCs when amused.",
                "rival": "General Don Rodrigo de Valenza",
                "classLevel": "9th-Level Magic-User / Beastmistress",
                "combatStats": "AC 5 (AAC 14) | HP 34 | THAC0 17 | Atk +5 (1d6) | Saves: 14/12/12/12/13"
            },
            "gmSecrets": "Doña Elvira possesses an intercepted carrier raven dispatch sent by <a href=\"#npcs/tiberio\" class=\"wiki-link\">Ambassador Tiberio</a> to the naval admirals of Argos, confirming that Argos intends to finance an amphibious blockade of Kordava within the month. She also holds the ancestral signet ring of Queen Sancha, which unlocks the high treasury vault in the North Spire.",
            "relatedIds": ["palace-of-kordava", "valenza", "sadoria", "tiberio", "court-matrix"],
            "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Royal Bloodline &bull; Dowager Infanta</span>
    <span class="badge rival-badge">Primary Rival: General Don Rodrigo de Valenza</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A massive, imperious matriarch of sixty-five draped in frayed silver damask, moth-eaten ermine, and pearls the size of pigeon eggs. She smells of sea salt, cedarwood, and birdlime. Perched on her leather gauntlet is a pure-white sea-falcon named 'Don Alfonso.'</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Ignores speakers for minutes while feeding raw liver to her birds; addresses high dukes as 'foolish boys'; tosses chicken bones over the battlements; speaks with devastating, aristocratic drawl.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;General Valenza? You mean the blacksmith's grandson who plays with tin soldiers? Tell him if he marches his noisy cavalry beneath my aviaries again, my falcons will pluck out his remaining eye.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 10 (Regal sovereign); Initial Reaction: Cold / Imperial (0 on 2d6 Reaction Rolls; +2 for PCs showing proper deference to her birds). Charisma check (roll 1d20 under Cha) to win her affection or gain access to her intercepted letters.</div>
  </div>
</div>

<h3>Public Persona &amp; Palace Duties</h3>
<p>Doña Elvira is the Countess Gertrude of Kordava. The elder sister of the late King and great-aunt to the PC Triumvirate, she is the highest-ranking surviving matriarch of the Ancillus dynasty. Thirty years ago, sickened by court hypocrisy and dynastic assassinations, she withdrew entirely from human court life, moving into the topmost windswept spires of the Hanging Aviary and Solarium.</p>
<p>Here, perched between the clouds and the crashing sea, she lives surrounded by forty pure-white Zingaran sea-falcons, screech-owls, and sixty fat, pampered temple cats that sleep on antique tapestry cushions. She refuses to attend court galas, treats ministers like begging serfs, and addresses <a href="#npcs/valenza" class="wiki-link">General Valenza</a> and <a href="#npcs/sadoria" class="wiki-link">Marquis Sadoria</a> with magnificent, blistering insults.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>While she affects total indifference to the realm, Elvira is fiercely protective of the young Triumvirate, viewing them as the last innocent blood of her house. Her white falcons are not decorative pets: they are trained aerial raptors that hunt messenger birds over Kordava harbor, the Baracha Strait, and the inland roads. Her gilded birdcages are stuffed with intercepted foreign ciphers, pirate trade manifests, and Council conspiracy letters. If the PCs climb to her high eyrie and bring her fresh quail or treat her pets with genuine reverence, she casually hands them intelligence that can break Council plots wide open.</p>
</div>

<h3>Faction Ties &amp; Palace Relationships</h3>
<ul>
  <li><strong><a href="#npcs/valenza" class="wiki-link">General Don Rodrigo de Valenza</a>:</strong> Absolute contempt. She views Valenza as an arrogant plebeian who usurped military command, and routinely commands her falcons to defecate on his gilded ceremonial parade armor.</li>
  <li><strong><a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a>:</strong> Sadoria once attempted to audit the aviary's poultry expenses; Elvira set two mastiffs on his clerks and threatened to have Sadoria thrown into the ocean surf from the high terrace.</li>
  <li><strong>The PC Triumvirate:</strong> Gruff, eccentric affection. She mocks their youth and lack of iron, but will use every ounce of her dynastic prestige and falcon-network to keep them from being poisoned by their handlers.</li>
</ul>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Intercepted Naval Cipher</h4>
  <p><strong>Premise:</strong> A dead messenger raven falls onto the Triumvirate's balcony, its throat torn out by talons. Attached to its leg is a wax capsule containing an encoded message from <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a> to an Argossean war fleet. Shortly after, a palace servant arrives with an invitation to tea from Doña Elvira in the High Aviary.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must climb the three hundred steps to the windy spires, endure Elvira's sharp tongue and haughty tests, and convince her to decode the cipher using an ancient genealogical cipher-wheel in her possession.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Charisma check (roll 1d20 under Cha) to impress the Dowager Infanta; Wisdom check (roll 1d20 under Wis) or Animal Handling to soothe her aggressive lead falcon, 'Don Alfonso.'</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the PCs anger Elvira, she feeds the cipher to an owl, forcing the rulers to search the aviary's guano-covered rafters at midnight.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Sacking of the Spire</h4>
  <p><strong>Premise:</strong> Suspicious of Elvira's carrier-bird intercepts, Marquis Sadoria sends six armed bailiffs to 'requisition' the High Aviary under the pretext of fortifying the sea-ramparts against pirate raids.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs hear the alarm bells and must decide whether to personally intervene against Sadoria's bailiffs (risking an open political confrontation with the Restoration Council), or let the aviary be raided, losing their premier aerial intelligence source.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Charisma check (or 2d6 Reaction Roll) to command the bailiffs to stand down under royal authority; Fighter Attack roll vs. AC 4 if swordplay erupts on the narrow stone stairways.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If swordplay breaks out, Elvira unleashes her entire flock of twenty hunting birds, creating total chaos on the high roofs that threatens to topple courtiers into the sea.</p>
</div>
"""
        },
        {
            "id": "pascual",
            "category": "npcs",
            "title": "Hermano Pascual",
            "subtitle": "Master Custodian of the Crystal Pavement &bull; Palace Household / Monastic Laborers",
            "tags": ["Royal Court", "NPC", "Palace Staff", "Period VIII", "Gormenghast", "The Pit"],
            "aliases": ["Hermano Pascual", "Pascual", "Custodian of the Crystal Floor", "The Polisher", "Brother Pascual"],
            "summary": "The quiet, half-blind custodian who has spent fifty years on his knees buffing the three-inch transparent quartz floor of the Grand Throne Room. By pressing his ear to the glass, he can hear the movements of creatures and rebels in The Pit two hundred feet below, and holds the secret release lever to the crystal dais.",
            "stats": {
                "classLevel": "7th-Level Fighter / Custodian",
                "combatStats": "AC 6 (AAC 13) | HP 38 | THAC0 15 | Atk +6 (1d6+2) | Saves: 13/10/11/12/13",
                "alignment": "Lawful (Devout duty, hyper-observant, quiet reverence for pre-Cataclysmic stone)",
                "station": "Master Custodian of the Transparent Quartz Floor of the Grand Throne Room",
                "ac": "AC 6 (AAC 13)",
                "acBreakdown": "Heavy Stitched Canvas & Leather Knee-Pads, DEX 12",
                "hd": "7d8 (+7 CON bonus on first 7 HD)",
                "hp": 38,
                "move": "90' (30')",
                "thaco": "15 (Base Attack Bonus +4)",
                "attacks": "Heavy Iron-Cored Chamois Staff (+6 to hit, 1d6+2 bludgeoning; trip on natural 18-20)",
                "abilities": [
                    ("STR", 15, "+1 to hit, +1 damage, lifts heavy stone blocks"),
                    ("DEX", 12, "Normal (0)"),
                    ("CON", 15, "+1 HP per Hit Die up to 7th level"),
                    ("INT", 14, "+1 language, deep knowledge of pre-deluvial engineering"),
                    ("WIS", 16, "+2 saves vs magic, extraordinary acoustic perception"),
                    ("CHA", 10, "Quiet, unassuming, overlooked by courtiers")
                ],
                "saves": [
                    ("Breath Weapon (BW)", 13),
                    ("Poison or Death (P/D)", 10),
                    ("Petrify or Paralyze (PP)", 11),
                    ("Wands (W)", 12),
                    ("Spells (S)", 13)  # Base 15 - 2 for WIS 16
                ],
                "magicItems": [
                    "The Tuning Fork of the Abyss (Bronze resonant fork; vibrates and rings softly when subterranean monsters or thrall armies move within 200' below the palace)",
                    "Salve of True Friction (Can turn a 20'x20' section of polished crystal either completely frictionless [as Grease spell] or completely slip-proof for 1 hour)",
                    "The Lens of Flaw-Finding (Magnifying loupe revealing structural micro-fractures and stress points in stone and crystal)"
                ],
                "tactics": "<strong>The Friction Trap:</strong> If threatened in the Throne Room, Pascual coats the quartz beneath attackers' boots with friction-nullifying whale oil (save vs Petrify or slide 30' across the floor and fall prone), then strikes with his staff.<br><strong>Dais Runic Release:</strong> Can throw the hidden bronze floor-switch beneath the throne dais, causing the transparent quartz to turn mirror-opaque or flash with blinding ancient Thurian luminescence.",
                "pcComparison": "A humble, unassuming servant (38 HP) who is treated as part of the architecture by nobles, giving him complete immunity from court suspicion while granting him unmatched acoustic intelligence from the underworld."
            },
            "atAGlance": {
                "appearance": "A quiet, round-shouldered man of sixty with permanently scarred, calloused knees and watery, squinting eyes from decades of staring into refracted quartz. Clad in a stained grey linen tunic and heavy leather knee-pads, smelling of pumice stone, lavender, and whale oil.",
                "mannerisms": "Crawls backwards while buffing flagstones with lamb's wool; cringes whenever nobles walk with sharp steel spurs; presses his ear to the cold floor for minutes at a time in silence.",
                "quote": "Careful where you step, Your Grace. That seam was laid when Valusia was young. Walk lightly... the things below are awake today.",
                "courtDCs": "Morale: 8 (Quiet guardian); Initial Reaction: Shy / Helpful (+1 on 2d6 Reaction Rolls for anyone who avoids scuffing his floor). Wisdom check to notice his subtle hand signals warning of danger.",
                "publicStance": "An invisible, humble palace laborer who buffs stone and cleans wax spills, completely beneath the notice of grandees and generals.",
                "secretAgenda": "To protect the pre-Cataclysmic crystal pavement from cracking, and warn the sovereigns when subterranean horrors or rebel sappers in The Pit begin boring upward beneath the throne.",
                "rival": "Master Alchemist Vane",
                "classLevel": "7th-Level Fighter / Custodian",
                "combatStats": "AC 6 (AAC 13) | HP 38 | THAC0 15 | Atk +6 (1d6+2) | Saves: 13/10/11/12/13"
            },
            "gmSecrets": "Hidden beneath the third step of the Obsidian Dais is an ancient Thurian mechanical lever that Pascual has maintained in secret for thirty years. Pushing the lever activates pre-deluvial refraction prisms, causing the transparent quartz floor to flash with blinding white light (all in the room blinded 2d4 rounds, save vs Spells) or polarizing the glass completely black so no one can peer down into The Pit.",
            "relatedIds": ["palace-of-kordava", "the-pit", "mausoleum-kalenius", "court-matrix"],
            "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Palace Household &bull; Custodian</span>
    <span class="badge rival-badge">Primary Rival: Master Alchemist Vane</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A quiet, round-shouldered man of sixty with permanently scarred, calloused knees and watery, squinting eyes from decades of staring into refracted quartz. Clad in a stained grey linen tunic and heavy leather knee-pads, smelling of pumice stone, lavender, and whale oil.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Crawls backwards while buffing flagstones with lamb's wool; cringes whenever nobles walk with sharp steel spurs; presses his ear to the cold floor for minutes at a time in silence.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;Careful where you step, Your Grace. That seam was laid when Valusia was young. Walk lightly... the things below are awake today.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 8 (Quiet guardian); Initial Reaction: Shy / Helpful (+1 on 2d6 Reaction Rolls for anyone who avoids scuffing his floor). Wisdom check (roll 1d20 under Wis) to notice his subtle hand signals warning of danger.</div>
  </div>
</div>

<h3>Public Persona &amp; Palace Duties</h3>
<p>Hermano Pascual is the Rottcodd of the High Alcázar. For fifty years, he has spent twelve hours a day on his hands and knees in the Grand Audience Chamber, buffing the three-inch transparent quartz flagstones of the Crystal Floor with pumice powder, lavender water, and lamb's wool. To the grandees, ministers, and foreign ambassadors who strut across the hall in feathered hats and gilded spurs, Pascual is simply a piece of moving furniture.</p>
<p>Because he is treated as invisible, courtiers openly discuss treason, bribes, and assassination plots while standing directly over him. Pascual hears everything, says nothing, and continues buffing the glass with rhythmic circular strokes.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>Pascual's true value lies in his extraordinary acoustic sensitivity. The Crystal Floor acts as a colossal acoustic diaphragm. By laying his temple against specific crystalline fault-lines, Pascual can listen to everything occurring two hundred feet below in <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>: he can hear republican cell meetings, the dragging footsteps of <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane's</a> zombie work-gangs, and the gnawing of subterranean horrors beneath the harbor. He quietly passes warnings to the Triumvirate by writing chalk symbols on the underside of their footstools.</p>
</div>

<h3>Faction Ties &amp; Palace Relationships</h3>
<ul>
  <li><strong>The PC Triumvirate:</strong> Quiet reverence. He treats the young rulers with gentle, paternal care, horrified when arrogant grandees force the monarchs to sit upon a drafty throne.</li>
  <li><strong><a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a>:</strong> Deep apprehension. Vane's underground blasting and necromantic excavation in The Pit creates seismic vibrations that are producing hairline fractures in the ancient crystal floor.</li>
  <li><strong><a href="#npcs/obregon" class="wiki-link">Lord Belisario de Obregon</a>:</strong> Mutual respect. Belisario protects Pascual's custodial budget from Sadoria's treasury cuts, recognizing that a clean crystal floor is essential to the dignity of royal audiences.</li>
</ul>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Scratch on the Crystal Dais</h4>
  <p><strong>Premise:</strong> Following a stormy audience with the provincial grandees, Hermano Pascual frantically tugs at the sleeve of the PC Warrior. He shows the PCs a fresh three-foot hairline fissure radiating directly from the base of the throne dais, through which a thin ribbon of sulfurous black vapor is seeping upward from The Pit.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must investigate whether the crack was caused by natural seismic settling, or if someone in The Pit is deliberately boring an explosive mine beneath the throne room to assassinate the entire court during the upcoming festival.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Wisdom check (roll 1d20 under Wis) or Dwarf Stonecunning to inspect the fracture; Intelligence check (roll 1d20 under Int) to analyze the chemical residue of the vapor.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the fissure is ignored, the center quadrant of the crystal floor shatters during the next grand audience, plunging two grandees into the dark abyss of The Pit.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Acoustic Warning</h4>
  <p><strong>Premise:</strong> At midnight, Pascual slips a folded note under the door of the royal bedchamber. Written in charcoal are three words: <em>"They dig tonight."</em> Pascual's tuning fork has detected military sappers tunneling through the old Thurian foundations directly toward the palace armory.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must follow Pascual into the narrow maintenance sub-basements beneath the crystal floor to confront the subterranean sappers before they breach the armory, choosing whether to execute them or recruit them against Sadoria.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Fighter Attack roll vs. AC 5 in tight subterranean crawlspaces; Charisma check (or 2d6 Reaction Roll) to interrogate the surviving sappers.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> The sappers are carrying dwarven blasting pots; a stray blow or fire spell risks collapsing the sub-cellar ceiling, threatening the stability of the throne room above.</p>
</div>
"""
        }
    ]

    # Add the stat blocks to the NPC contents
    for npc in palace_npcs_data:
        sb_html = make_stat_block(npc['title'], npc['stats'])
        # Insert stat block after npc-header-card
        c = npc['content']
        end_hdr = c.find('</div>\n\n<h3>Public Persona')
        if end_hdr != -1:
            end_hdr += 6
            c = c[:end_hdr] + "\n" + sb_html + "\n" + c[end_hdr:]
        else:
            c = sb_html + "\n" + c
        npc['content'] = c

    # -------------------------------------------------------------
    # 3. DEFINE THE PALACE GAZETTEER ARTICLE: palace-of-kordava
    # -------------------------------------------------------------
    palace_gazetteer = {
        "id": "palace-of-kordava",
        "category": "gazetteer",
        "title": "The High Alcázar of Kordava",
        "subtitle": "The Palace of the Crystal Floor & Labyrinth of Ancient Precedent",
        "tags": ["Gazetteer", "Kordava", "The High Alcázar", "Palace", "Royal Court", "Gormenghast", "Period VIII"],
        "aliases": [
            "The High Alcázar",
            "Alcázar of Kordava",
            "High Alcázar of Kordava",
            "The Palace of the Crystal Floor",
            "The Royal Palace",
            "Palace of Kordava",
            "El Alcázar de las Agujas",
            "The Crystal Floor Palace"
        ],
        "summary": "A colossal, decaying pre-Cataclysmic citadel perched on Kordava's sea-cliffs. Within its labyrinthine, draught-ridden stone spires, cavernous kitchens, and transparent quartz throne room, an eccentric caste of ancient palace staff enacts centuries of suffocating ceremonial ritual while the kingdom crumbles outside.",
        "gmSecrets": "Beneath the crystal floor lies The Pit; secret flues and dumbwaiters bypass the Restoration Council's guards; the sealed royal wings contain unlooted treasures and dark revenants from King Daedalus's reign; pre-deluvial mechanical levers control the throne room's transparency and lighting.",
        "relatedIds": [
            "kordava",
            "the-pit",
            "court-matrix",
            "campaign-premise",
            "valenza",
            "sadoria",
            "obregon",
            "basto",
            "silveira",
            "escovedo",
            "ignacio",
            "elvira",
            "pascual"
        ],
        "content": """
<div class="info-card">
  <p><strong>Geographical Type:</strong> Colossal Sea-Cliff Citadel &amp; Royal Palace Monolith</p>
  <p><strong>Strategic &amp; Political Value:</strong> Sovereign seat of the Zingaran Monarchy, the Triumvirate, the Restoration Council, and the high ministries of state.</p>
  <p><strong>Atmospheric Tone:</strong> Gormenghastian gothic decadence, suffocating ancestral protocol, drafty corridors, labyrinthine verticality, and dark subterranean dread.</p>
  <p><strong>Primary Encounter Hazards:</strong> Council spies, assassin darts behind tapestries, vertigo over the Crystal Floor, ceremonial legal traps, and necrotic vapor leaks from The Pit.</p>
</div>

<h3>1. An Architecture of Decadence &amp; Accretion</h3>
<p>Perched upon the sheer granite sea-cliffs overlooking the storm-tossed Western Ocean and the estuary of the Black River, the <strong>High Alcázar of Kordava</strong> (known colloquially as <em>El Alcázar de las Agujas</em>—the Alcázar of the Spires) is not a single coherent fortress, but a sprawling, cyclopean mountain of stone accumulated across twelve hundred years of contradictory architectural epochs.</p>
<p>Its cyclopean foundations are composed of black basalt blocks quarried during the pre-Cataclysmic Thurian era—stones so colossal that no modern crane can lift them. Atop these ancient bones rise soaring Zingaran Gothic additions: needle-thin white marble spires, flying buttresses that groan in the Atlantic gales, vaulted galleries hung with frayed tapestries of forgotten conquerors, and cold, echoing flagstone corridors where footsteps reverberate like drumbeats. The palace is vast beyond human utility: entire wings have been walled off and forgotten for generations, inhabited only by bats, silverfish, and the ghosts of poisoned dynasties.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE GORMENGHAST OF ZINGARA</div>
  <p>To the young PC <a href="#overview/campaign-premise" class="wiki-link">Triumvirate</a>, the Alcázar is a gilded prison. While they hold the legal title of sovereigns, their handlers—<a href="#npcs/valenza" class="wiki-link">General Valenza</a> and <a href="#npcs/sadoria" class="wiki-link">Marquis Sadoria</a>—control the guard garrisons at every gate. Yet the true masters of the citadel's interior are not the ministers, but an ancient, eccentric caste of hereditary palace staff who have inhabited these draughty corridors longer than the current dynasty. By mastering the palace's eccentric staff, secret flues, and ancestral rituals, the PCs can outmaneuver their handlers from within.</p>
</div>

<h3>2. The Six Great Sectors of the Alcázar</h3>

<div class="info-card">
  <h4>Sector I: The Grand Throne Room of the Crystal Floor</h4>
  <p>The ceremonial heart of Zingaran monarchy. A colossal vaulted hall supported by twelve fluted basalt columns. What makes the chamber legendary across the Hyborian world is its pavement: three hundred square yards of solid, transparent pre-Cataclysmic quartz crystal, three inches thick and polished to a flawless mirror sheen by <a href="#npcs/pascual" class="wiki-link">Hermano Pascual</a>. Sitting upon the Obsidian Dais, the young monarchs look down directly between their spurred boots into the terrible, murky abyss of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> two hundred feet below. Phosphorescent lichens, crumbling sunken colonnades, and the shambling shadows of working zombie thralls can be seen drifting through the green gloom beneath the monarchs' feet, instilling a sickening sense of vertigo in foreign ambassadors.</p>
</div>

<div class="info-card">
  <h4>Sector II: The Upper Spires &amp; The Gilded Cage</h4>
  <p>Perched high in the western towers, where the sea spray lashes the leaded lancet windows, lie the private royal apartments of the Triumvirate. Sumptuous yet suffocating, these chambers are furnished with decaying velvet canopies, braziers burning scented pine oil to mask the salt damp, and portraits of stern ancestors who died violent deaths. The chambers are surrounded by <a href="#npcs/valenza" class="wiki-link">General Valenza's</a> royal army sentries. The only man with unconditional access to the sovereigns' bedchamber is the gaunt, clicking Lord Chamberlain, <a href="#npcs/silveira" class="wiki-link">Don Fernao de Silveira</a>.</p>
</div>

<div class="info-card">
  <h4>Sector III: The Cavernous Kitchens &amp; Roasting Pits</h4>
  <p>Deep within the subterranean foundations, directly above the damp cellars of old Kordava, lies an infernal empire of grease, charcoal smoke, and roaring hearths ruled despotically by <a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo 'El Basto'</a>. Eighty kitchen boys, pastry apprentices, turnspits, and memory-retaining zombie scullions toil in 110-degree heat, preparing sixteen-course banquets of roasted boars, peacock pastries, and almond cream. Behind the walk-in chimneys are massive, counter-weighted dumbwaiter shafts that drop two hundred feet straight down into the black market tunnels of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>.</p>
</div>

<div class="info-card">
  <h4>Sector IV: The Hall of Precedent, Ancient Archives &amp; Dust Galleries</h4>
  <p>An endless labyrinth of dry, whispering rooms stacked floor-to-ceiling with thousands of iron-bound calfskin ledgers, royal decrees, heraldic scrolls, and genealogical charts dating back to King Ancillus I. Controlled with iron pedantry by the ancient Grand Seneschal, <a href="#npcs/obregon" class="wiki-link">Lord Belisario de Obregon</a>, here twenty desiccated heralds spend entire decades debating whether an envoy from Argos is entitled to four or five trumpet fanfares upon crossing the threshold.</p>
</div>

<div class="info-card">
  <h4>Sector V: The Hanging Aviary &amp; Solarium of the Falcons</h4>
  <p>In the gale-swept topmost spires of the citadel, exposed to the open sky through grand Romanesque arches, resides the reclusive Dowager Infanta, <a href="#npcs/elvira" class="wiki-link">Doña Elvira de Ancillus-Moreno</a>. Draped in moth-eaten ermine and surrounded by forty pure-white Zingaran sea-falcons and dozens of fat temple cats, she looks down upon court politics with supreme imperial disdain. Her raptors patrol the coastal skies, hunting carrier pigeons and providing the only reliable aerial intelligence in the kingdom.</p>
</div>

<div class="info-card">
  <h4>Sector VI: The Sealed Solares &amp; Walled-Off Wings</h4>
  <p>Following the bloody dynastic massacre known as the Black Solstice eighty years ago, King Daedalus's regents bricked up an entire western quarter of the palace. Untouched for nearly a century, these dust-choked galleries contain forgotten royal libraries, sealed treasury vaults, pre-Cataclysmic mechanical traps, and the desiccated, unburied remains of murdered courtiers. Only <a href="#npcs/silveira" class="wiki-link">Don Fernao</a> holds the master key to the iron doors, though the climbing scrivener <a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a> has discovered secret chimney shafts leading inside.</p>
</div>

<h3>3. The Suffocating Court Protocol &amp; Daily Rituals</h3>
<p>Life in the High Alcázar is governed not by practical reason, but by the immovable, ossified precedent of four centuries. The daily schedule of the PC Triumvirate is dictated by the <em>Libro de las Horas Reales</em>:</p>
<ul>
  <li><strong>The Ritual of the Dawn Salutation (6:00 AM):</strong> The sovereigns must be awakened by twenty bronze hand-bells, followed by kissing the salted sea-stone of Ancillus I presented on a silver salver by <a href="#npcs/obregon" class="wiki-link">Lord Belisario</a>.</li>
  <li><strong>The Adornment of the Sovereign (7:00 AM – 9:00 AM):</strong> A two-hour ritual in which eleven different hereditary officials dress the rulers: one ties the right garter; another fastens the 40-pound lead-weighted mantle; a third inspects the lace ruff with silver calipers.</li>
  <li><strong>The Tasting of the Porridge (9:30 AM):</strong> <a href="#npcs/escovedo" class="wiki-link">Dr. Escovedo</a> drops silver needles into the royal broth to check for arsenic, while <a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo</a> glares from the doorway with his cleaver.</li>
  <li><strong>The Audience of the Void (11:00 AM – 2:00 PM):</strong> The monarchs sit on the Obsidian Dais above the Crystal Floor, receiving petitioners who must advance in rigid three-step waltzes, never turning their backs on the transparent floor lest they appear frightened by the abyss below.</li>
  <li><strong>The Night Lockdown (10:00 PM):</strong> <a href="#npcs/silveira" class="wiki-link">Don Fernao</a> locks the three hundred interior doors with his iron chatelaine, extinguishing all torchieres except the consecrated tapers of the ancestors.</li>
</ul>

<h3>4. The Master Directory of Palace Household Staff</h3>
<div style="overflow-x: auto; margin-top: 10px;">
<table class="wiki-table" style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="background: var(--bg-surface-elevated); border-bottom: 2px solid var(--border-gold);">
      <th style="padding: 8px 10px; text-align: left;">Official &bull; Dossier Link</th>
      <th style="padding: 8px 10px; text-align: left;">Household Office</th>
      <th style="padding: 8px 10px; text-align: left;">Labyrinth Lord Stats</th>
      <th style="padding: 8px 10px; text-align: left;">Palace Domain &amp; Secret Utility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="#npcs/obregon" class="wiki-link">Lord Belisario de Obregon</a></strong></td>
      <td>Grand Seneschal of Precedent</td>
      <td><span class="stat-class-level">Cleric 9 (Lawful)</span></td>
      <td>Hall of Precedent; controls court legitimacy &amp; holds the unredacted royal charter.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo 'El Basto'</a></strong></td>
      <td>Master Cook of the Kitchens</td>
      <td><span class="stat-class-level">Fighter 10 (Neutral)</span></td>
      <td>Subterranean Kitchens; controls food supply &amp; the dumbwaiters dropping into The Pit.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/silveira" class="wiki-link">Don Fernao de Silveira</a></strong></td>
      <td>Lord of the Bedchamber</td>
      <td><span class="stat-class-level">Thief 10 (Lawful)</span></td>
      <td>Royal Bedchambers; master keys, nocturnal bodyguard, knows the sealed wing entrance.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/escovedo" class="wiki-link">Dr. Horatio Escovedo</a></strong></td>
      <td>Chief Court Chirurgeon</td>
      <td><span class="stat-class-level">Magic-User 10 (Neutral)</span></td>
      <td>Dissecting Tower &amp; Apothecary; detects poisons, brews antidotes, shields the PCs.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a></strong></td>
      <td>The Climbing Scrivener</td>
      <td><span class="stat-class-level">Thief 9 (Chaotic)</span></td>
      <td>Bureau of Receipts &amp; Flues; master climber, sells secrets to all factions.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/elvira" class="wiki-link">Doña Elvira de Ancillus-Moreno</a></strong></td>
      <td>Dowager Infanta</td>
      <td><span class="stat-class-level">Magic-User 9 (Neutral)</span></td>
      <td>Hanging Aviaries; commands 40 white falcons that intercept courier ciphers.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/pascual" class="wiki-link">Hermano Pascual</a></strong></td>
      <td>Custodian of the Crystal Floor</td>
      <td><span class="stat-class-level">Fighter 7 (Lawful)</span></td>
      <td>Grand Throne Room; hears vibrations from The Pit &amp; controls the dais light-lever.</td>
    </tr>
  </tbody>
</table>
</div>

<h3>5. Mechanical Secrets &amp; Hidden Passages</h3>
<ul>
  <li><strong>The Kitchen Dumbwaiter to The Pit:</strong> Located behind the third roasting hearth in Maestro Bartolomeo's kitchen. Capable of carrying four human-sized creatures in a counter-weighted iron cage, dropping 200 feet directly into the smuggler alleys of The Pit in less than two minutes.</li>
  <li><strong>The Dais Light-Lever:</strong> Concealed beneath the third riser of the Obsidian Throne dais. Moving the bronze peg activates ancient Thurian refraction runes, polarizing the transparent crystal floor completely pitch-black or emitting a burst of blinding illumination.</li>
  <li><strong>The Acoustic Whispering Ducts:</strong> Pre-deluvial hollow bronze acoustic pipes run through the core masonry of the palace walls. The primary listening station terminates behind the grand tapestry of King Ancillus I in the Queen's Salon, allowing the listener to eavesdrop on Marquis Sadoria's private council chamber.</li>
  <li><strong>The Flue Highway:</strong> A network of narrow vertical chimney flues and masonry ledges, accessible from the Bureau of Salt &amp; Wax Receipts, that leads to the exterior parapets and sea-cliffs. Used exclusively by <a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a>.</li>
</ul>

<h3>6. Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Duel in the Hall of Mirrors</h4>
  <p><strong>Premise:</strong> During the three-hour Evening Recessional, a hot-headed young grandee from the Eastern League deliberately steps on the train of a PC ruler's ceremonial mantle, sneering that the Triumvirate are "puppets in borrowed finery." In accordance with the strict laws of <em>pundonor</em>, the insult cannot be ignored without losing 2 Crown Sovereignty points.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must immediately fight a formal rapier duel to first blood upon the slick, polished crystal floor, navigating both their opponent's blade and the vertigo of looking down into The Pit beneath their boots.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Fighter Attack roll vs. AC 2; Dexterity check (roll 1d20 under Dex) to maintain footing on the crystal without slipping; Charisma check to maintain regal composure.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If blood falls upon the crystal, <a href="#npcs/pascual" class="wiki-link">Hermano Pascual</a> weeps aloud, and the sulfurous vapors below bubble violently, attracting subterranean ghouls to press against the glass.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Midnight Heist of the Sealed Wing</h4>
  <p><strong>Premise:</strong> Facing a total financial embargo by <a href="#npcs/sadoria" class="wiki-link">Marquis Sadoria</a>, the PCs receive an offer from <a href="#npcs/silveira" class="wiki-link">Don Fernao</a>: he will unlock the iron portal to the Sealed Solares if the PCs accompany him inside to recover the lost coronation chalice of King Ancillus I before the Council can seize it.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must navigate the cobwebbed, trap-laden corridors of the abandoned wing, avoiding pre-deluvial spring-traps and spectral remnants, only to discover that <a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a> is already inside picking the lock of the royal strongbox.</p>
  <div class="dc-box"><strong>Basic D&D Challenge:</strong> Thief Find/Remove Traps or Dexterity check (roll 1d20 under Dex); Cleric Turn Undead vs. 4 HD Spectres; Charisma check to negotiate a split with Ignacio.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> An iron portcullis slams shut, trapping the PCs inside the sealed wing while toxic rot-gas begins venting from the floorboards.</p>
</div>
"""
    }

    # -------------------------------------------------------------
    # 4. INSERT INTO DATA.JS ARTICLES LIST
    # -------------------------------------------------------------
    # Check if palace-of-kordava already exists
    p_idx = next((i for i, a in enumerate(articles) if a['id'] == 'palace-of-kordava'), None)
    if p_idx is not None:
        articles[p_idx] = palace_gazetteer
        print("Updated existing palace-of-kordava article.")
    else:
        # Insert right after kordava
        k_idx = next((i for i, a in enumerate(articles) if a['id'] == 'kordava'), None)
        if k_idx is not None:
            articles.insert(k_idx + 1, palace_gazetteer)
        else:
            articles.append(palace_gazetteer)
        print("Inserted new palace-of-kordava article.")

    # Insert or update each of the 7 palace NPCs
    for npc in palace_npcs_data:
        existing_idx = next((i for i, a in enumerate(articles) if a['id'] == npc['id']), None)
        # Prepare article dictionary without 'stats' (stats are embedded in content and atAGlance)
        clean_article = {
            "id": npc["id"],
            "category": npc["category"],
            "title": npc["title"],
            "subtitle": npc["subtitle"],
            "tags": npc["tags"],
            "aliases": npc["aliases"],
            "summary": npc["summary"],
            "atAGlance": npc["atAGlance"],
            "gmSecrets": npc["gmSecrets"],
            "relatedIds": npc["relatedIds"],
            "content": npc["content"]
        }
        if existing_idx is not None:
            articles[existing_idx] = clean_article
            print(f"Updated NPC: {npc['id']}")
        else:
            # Find last NPC index to insert after
            last_npc_idx = max([i for i, a in enumerate(articles) if a.get('category') == 'npcs'] or [0])
            articles.insert(last_npc_idx + 1, clean_article)
            print(f"Inserted new NPC: {npc['id']}")

    # -------------------------------------------------------------
    # 5. UPDATE EXISTING ARTICLES (kordava, court-matrix, etc.)
    # -------------------------------------------------------------
    # Update kordava
    kordava_art = next((a for a in articles if a['id'] == 'kordava'), None)
    if kordava_art:
        if "palace-of-kordava" not in kordava_art.get("relatedIds", []):
            kordava_art["relatedIds"].append("palace-of-kordava")
        if "The High Alcázar of Kordava" not in kordava_art["content"]:
            palace_highlight = """
<h3>The High Alcázar of Kordava &amp; The Crystal Floor</h3>
<p>Dominating the city's skyline atop the sheer western sea-cliffs stands <strong><a href="#gazetteer/palace-of-kordava" class="wiki-link">The High Alcázar of Kordava</a></strong>—the sprawling, labyrinthine palace citadel of the Zingaran monarchy. Perched directly above the subterranean abyss of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>, the Alcázar is famous for its <em>Grand Throne Room of the Crystal Floor</em>, where sovereigns sit on an obsidian dais suspended upon three inches of transparent quartz over the dark underworld. Within its draught-ridden stone spires, an eccentric household of hereditary staff—including <a href="#npcs/obregon" class="wiki-link">Lord Belisario</a>, <a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo</a>, <a href="#npcs/silveira" class="wiki-link">Don Fernao</a>, <a href="#npcs/escovedo" class="wiki-link">Dr. Escovedo</a>, <a href="#npcs/elvira" class="wiki-link">Doña Elvira</a>, <a href="#npcs/pascual" class="wiki-link">Hermano Pascual</a>, and the climbing scrivener <a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a>—enact centuries of suffocating ancestral etiquette.</p>
"""
            # Insert before GM Callout
            gm_pos = kordava_art["content"].find('<div class="gm-callout">')
            if gm_pos != -1:
                kordava_art["content"] = kordava_art["content"][:gm_pos] + palace_highlight + "\n" + kordava_art["content"][gm_pos:]
            else:
                kordava_art["content"] += "\n" + palace_highlight
            print("Enhanced kordava article with High Alcázar cross-reference.")

    # Update court-matrix
    matrix_art = next((a for a in articles if a['id'] == 'court-matrix'), None)
    if matrix_art:
        for npc in palace_npcs_data:
            if npc["id"] not in matrix_art.get("relatedIds", []):
                matrix_art["relatedIds"].append(npc["id"])

        if "The Palace Household Staff: The Intramural Cold War" not in matrix_art["content"]:
            household_dynamics_html = """
<h3>The Palace Household Staff: The Intramural Cold War</h3>
<p>While the high ministers of the <a href="#factions/restoration-council" class="wiki-link">Restoration Council</a> and the generals of the <a href="#factions/military-elite" class="wiki-link">Military Elite</a> believe they control the kingdom from above, the day-to-day operation of the <a href="#gazetteer/palace-of-kordava" class="wiki-link">High Alcázar</a> is governed by an ancient, eccentric caste of household staff who pre-date the current regime. This produces a fierce, subterranean cold war within the palace walls:</p>

<div class="info-card">
  <h4>Intramural Household Dynamics</h4>
  <ul>
    <li><strong>The Bedchamber vs. The Kitchens:</strong> An ancient, vitriolic feud between <a href="#npcs/silveira" class="wiki-link">Don Fernao de Silveira</a> (the austere, clicking Lord Chamberlain) and <a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo</a> (the despotic kitchen butcher). Fernao considers the kitchens a nest of republican contraband; Bartolomeo routinely locks out the Chamberlain's footmen from hot water rations.</li>
    <li><strong>The Scriptorium's Shield:</strong> While <a href="#npcs/sadoria" class="wiki-link">Marquis Sadoria</a> relies on subtle poisons, the eccentric court physician <a href="#npcs/escovedo" class="wiki-link">Dr. Horatio Escovedo</a> secretly supplies the PC Triumvirate with daily panaceas and broad-spectrum antidotes disguised as digestive cordials.</li>
    <li><strong>The Spider of the Flues:</strong> The young scrivener <a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a> climbs the vertical chimney flues and masonry shafts at night, copying Sadoria's private letters and selling the leaks to <a href="#npcs/lucia" class="wiki-link">Lucia's republicans</a> and <a href="#npcs/vesper" class="wiki-link">Vesper</a>.</li>
    <li><strong>The Falcon Eyrie:</strong> High above the palace in the windswept spires, the reclusive Dowager Infanta <a href="#npcs/elvira" class="wiki-link">Doña Elvira</a> uses her forty white sea-falcons to intercept carrier pigeons sent by foreign ambassadors and treacherous grandees, hoarding the ciphers in gilded birdcages.</li>
    <li><strong>The Acoustic Watchdog:</strong> On his knees buffing the transparent quartz floor of the Throne Room, <a href="#npcs/pascual" class="wiki-link">Hermano Pascual</a> listens to vibrations from <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> two hundred feet below, quietly warning the sovereigns of underground incursions.</li>
  </ul>
</div>
"""
            # Also append rows to the Labyrinth Lord Hierarchy table if present
            palace_ll_rows = """
    <tr>
      <td><strong><a href="#npcs/obregon" class="wiki-link">Lord Belisario de Obregon</a></strong><br><small>Grand Seneschal of Precedent</small></td>
      <td><span class="stat-class-level">Cleric 9</span></td>
      <td>Lawful</td>
      <td><strong>5 (14)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">38</span></td>
      <td>15 (+4)</td>
      <td><em>Libro de las Horas Reales</em>, <em>Silver Calipers</em>, <em>Ring of Mind Shielding</em></td>
      <td>Frail physical combatant; commands 4 halberdiers; controls state legitimacy &amp; procedural vetoes.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/basto" class="wiki-link">Maestro Bartolomeo 'El Basto'</a></strong><br><small>Master Cook of the Kitchens</small></td>
      <td><span class="stat-class-level">Fighter 10</span></td>
      <td>Neutral</td>
      <td><strong>3 (16)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">68</span></td>
      <td>12 (+11)</td>
      <td><em>El Verdugo</em> (+2 Cleaver), Boiling Tallow, <em>Girdle of the Iron Girth</em></td>
      <td>STR 18 brute; hits as hard as Gonzalo; boiling fat cone; controls dumbwaiters to The Pit.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/silveira" class="wiki-link">Don Fernao de Silveira</a></strong><br><small>Lord of the Bedchamber</small></td>
      <td><span class="stat-class-level">Thief 10</span></td>
      <td>Lawful</td>
      <td><strong>2 (17)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">44</span></td>
      <td>14 (+8)</td>
      <td><em>Chatelaine of Kalenius</em> (300 Keys), Poison Wrist Crossbow, x4 Backstab</td>
      <td>Master of locks &amp; spyholes; unbribable sovereign bodyguard; knows the sealed wing entrance.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/escovedo" class="wiki-link">Dr. Horatio Escovedo</a></strong><br><small>Chief Royal Chirurgeon</small></td>
      <td><span class="stat-class-level">Magic-User 10</span></td>
      <td>Neutral</td>
      <td><strong>4 (15)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">32</span></td>
      <td>17 (+6)</td>
      <td><em>Smoked-Quartz Spectacles</em>, Flash-Globes, Bandolier of Panaceas, 5th-circle spells</td>
      <td>Neutralizes Sadoria's poisons; INT 18 physician; casts <em>Feeblemind</em> and <em>Haste</em>.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/ignacio" class="wiki-link">Ignacio Mora</a></strong><br><small>The Climbing Scrivener</small></td>
      <td><span class="stat-class-level">Thief 9</span></td>
      <td>Chaotic</td>
      <td><strong>1 (18)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">40</span></td>
      <td>15 (+9)</td>
      <td><em>Spider-Silk Slippers</em>, <em>Wax-Seal of Forgery</em>, Lotus Bodkin +2, x4 Backstab</td>
      <td>DEX 18; 96% Climb Walls; runs the palace flues; master infiltrator &amp; blackmailer.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/elvira" class="wiki-link">Doña Elvira de Ancillus-Moreno</a></strong><br><small>Dowager Infanta</small></td>
      <td><span class="stat-class-level">Magic-User 9</span></td>
      <td>Neutral</td>
      <td><strong>5 (14)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">34</span></td>
      <td>17 (+5)</td>
      <td><em>Silver Whistle of Falcons</em>, <em>Falcon-Eye Ring</em>, <em>Mantle of Protection +2</em></td>
      <td>Summons swarm of 20 white sea-falcons; untouchable royal status; intercepts courier birds.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/pascual" class="wiki-link">Hermano Pascual</a></strong><br><small>Custodian of the Crystal Floor</small></td>
      <td><span class="stat-class-level">Fighter 7</span></td>
      <td>Lawful</td>
      <td><strong>6 (13)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">38</span></td>
      <td>15 (+6)</td>
      <td><em>Tuning Fork of the Abyss</em>, <em>Salve of True Friction</em>, Dais Light-Lever</td>
      <td>Acoustic perception into The Pit; controls throne room friction &amp; pre-deluvial light wards.</td>
    </tr>
"""
            # Insert the household dynamics
            matrix_art["content"] += "\n" + household_dynamics_html

            # If the LL table exists in matrix_art, insert rows before </tbody>
            if "</tbody>" in matrix_art["content"]:
                matrix_art["content"] = matrix_art["content"].replace("</tbody>", palace_ll_rows + "\n  </tbody>", 1)
            print("Enhanced court-matrix with Palace Staff Intramural Dynamics & LL stats table rows.")

    # -------------------------------------------------------------
    # 6. FINALIZE META & WRITE BACK
    # -------------------------------------------------------------
    data["meta"]["totalArticles"] = len(articles)
    data["meta"]["lastUpdated"] = "2026-10-14T19:30:00.000Z"

    # Convert to JSON with pretty indentation
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    js_output = f"window.WIKI_DATA = {json_str};\n"

    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(js_output)

    print(f"Successfully updated js/data.js! Total articles now: {len(articles)}")

if __name__ == '__main__':
    main()
