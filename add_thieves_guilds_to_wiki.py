"""
add_thieves_guilds_to_wiki.py
Adds the Kordovan Night Guild, the Velasco Syndicate, their key characters (Joachor Valiento,
Guildmaster Don Beltran, Capitan Don Cazmiro), the Velasco Gazetteer entry, and updates
existing files (js/data.js, data/sessions.json).
"""

import json
import re
import sys

def build_data():
    with open('js/data.js', 'r', encoding='utf-8') as f:
        text = f.read()

    prefix = 'window.WIKI_DATA = '
    idx = text.find(prefix)
    if idx == -1:
        print("ERROR: Could not find window.WIKI_DATA")
        sys.exit(1)

    raw_json = text[idx+len(prefix):].rstrip(';\n ')
    data = json.loads(raw_json)

    print(f"Loaded existing wiki data with {len(data['articles'])} articles.")

    # -------------------------------------------------------------
    # 1. NEW ARTICLE: joaquin (NPC: Joachor "El Grajo" Valiente)
    # -------------------------------------------------------------
    joaquin_article = {
        "id": "joaquin",
        "category": "npcs",
        "title": "Joachor 'The Jackdaw' Valiento",
        "subtitle": "Down-on-His-Luck Cutpurse & Outcast Scout • The Night Guild of Kordova",
        "tags": ["Royal Court", "NPC", "Thief", "Kordava", "The Pit", "Night Guild", "Session 1", "Underworld"],
        "aliases": [
            "Joachor Valiento",
            "El Grajo",
            "The Jackdaw",
            "Joachor",
            "The Down-on-His-Luck Thief",
            "The Jackdaw Valiento",
            "Down-on-His-Luck Thief"
        ],
        "summary": "A ragged, quick-fingered Zingaran cutpurse and rooftop scout who met the PC Triumvirate in The Drowned Rat tavern. Squeezed by Kordova's economic collapse, zombie labor displacement, and an unpaid 80-sovereign blood-tithe to his guildmaster, he brokered an introduction to the Kordovan Night Guild in exchange for coin and a cut of all royal schemes.",
        "atAGlance": {
            "appearance": "A lean, wiry youth of twenty-six with tangled black hair, hollow cheeks, and nervous, hyper-observant dark eyes. Wears a frayed, oil-stained leather jerkin patched with dried eel-skin, boots with cracked soles bound by hemp twine, and an empty stiletto sheath at his hip.",
            "mannerisms": "Perpetually rolls a dented copper bit across his knuckles; glances toward tavern doors every few heartbeats; flinches at the clatter of caballero plate armor; drops his voice into a breathless, urgent Zingaran gutter-whisper.",
            "quote": "A crown on the throne or a copper in the gutter—it's all iron and gold waiting for fingers that know how to coax it free. But in Kordova today, my lords, even the rats are pawning their whiskers to pay the garrison tax. Feed me, back me, cut me into your schemes—and I'll show you where the real kings of this city hold their court.",
            "courtDCs": "Morale: 7 (Desperate survivor); Initial Reaction: +2 on 2d6 Reaction Rolls when offered bread, wine, or silver (Hungry & Eager); Charisma check (or 50 gp advance) to secure his unquestioned loyalty under royal interrogation.",
            "publicStance": "Presents himself as a harmless, starving dock-scavenger and tavern errand-runner nursing dreg-ale in the lower sinks of Kordova.",
            "secretAgenda": "Joachor owes an 80-gold-sovereign 'blood tithe' to Guildmaster Don Beltrano de Soto after botching a jewel heist against an armored caballero coach. If he fails to pay by week's end, the guild enforcers will break his hands and sell him to Master Alchemist Vane's corpse-wagons. He hopes the PC Triumvirate's royal schemes will earn him enough bullion to clear his debt and elevate him into the guild's Inner Circle.",
            "rival": "'El Macho' Murzio Corvo (Guild Enforcer) & Inés 'La Loba' (Velascan Assassin)",
            "classLevel": "5th-Level Thief (Cutpurse & Roof-Runner)",
            "combatStats": "AC 5 (AAC 14) | HP 18 | THAC0 18 | Atk +4 (1d4+1) | Backstab x3 | Saves: 12/12/11/14/12"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Night Guild of Kordova &bull; The Pit Scouts</span>
    <span class="badge rival-badge">Primary Rivals: 'El Macho' Murzio Corvo &amp; Inés 'La Loba'</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A lean, wiry Zingaran youth of twenty-six with hollow cheeks, soot-smudged wrists, and hungry, hyper-alert dark eyes. His salt-stained leather doublet is patched with cured eel-hide, his boots have split soles tied with hemp twine, and his stiletto scabbard hangs conspicuously empty—pawned three nights ago for dry bread and sour wine.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Perpetually rolls a dented copper coin over his scarred knuckles; continuously scans doorways and ceiling rafters; flinches at the ringing clink of royal army mail; speaks in a hushed, conspiratorial Zingaran gutter-slang.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;A crown on the throne or a copper in the gutter—it's all iron and gold waiting for fingers that know how to coax it free. But in Kordova today, my lords, even the rats are pawning their whiskers to pay the garrison tax. Feed me, back me, cut me into your schemes—and I'll show you where the real kings of this city hold their court.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 7 (Desperate survivor); Initial Reaction: +2 on 2d6 Reaction Rolls when offered bread, wine, or silver (Hungry &amp; Eager). DC 14 Charisma or 50 gp advance to secure his absolute silence under interrogation.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Joachor 'The Jackdaw' Valiento</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Down-on-His-Luck Cutpurse, Cat Burglar &amp; Underground Guide &bull; Neutral (Desperate survival, opportunistic loyalty, street solidarity)</div>
    </div>
    <span class="stat-class-level">⚔️ 5th-Level Thief (Cutpurse &amp; Roof-Runner)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 5 (AAC 14) <small class="text-dim">(Supple Boar-Hide Jerkin, DEX 16 (-2))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 5d4 (+5 CON bonus) &bull; <span style="color: #2ecc71; font-weight: 700;">18 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40') / Rooftop Leap 20'</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 18 (Base Attack Bonus +2)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +4 to hit (<em>"El Picotazo"</em> +1 bone-handled stiletto, 1d4+1 piercing); Ranged: +4 to hit (Concealed Throwing Darts, 1d4, range 20'/40'/60'); Backstab: x3 Damage (3d4+3 piercing from stealth)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box">
      <div class="stat-ability-label">STR</div>
      <div class="stat-ability-score">11</div>
      <div class="stat-ability-mod">Normal (0)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">DEX</div>
      <div class="stat-ability-score">16</div>
      <div class="stat-ability-mod">+2 missile to hit, -2 AC bonus</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">12</div>
      <div class="stat-ability-mod">Normal (0)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">14</div>
      <div class="stat-ability-mod">+1 language, keen street geography</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">9</div>
      <div class="stat-ability-mod">-1 on saving throws vs. magical deception</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">+1 reaction, persuasive street patter</div>
    </div>
  </div>

  <div class="stat-section-title">Saving Throws (Labyrinth Lord 5-Column)</div>
  <div class="stat-saves-bar">
    <div class="stat-save-box" title="Breath Weapon (BW)">
      <div class="stat-save-label">BW</div>
      <div class="stat-save-val">15</div>
    </div>
    <div class="stat-save-box" title="Poison or Death (P/D)">
      <div class="stat-save-label">P/D</div>
      <div class="stat-save-val">12</div>
    </div>
    <div class="stat-save-box" title="Petrify or Paralyze (PP)">
      <div class="stat-save-label">PP</div>
      <div class="stat-save-val">11</div>
    </div>
    <div class="stat-save-box" title="Wands (W)">
      <div class="stat-save-label">W</div>
      <div class="stat-save-val">14</div>
    </div>
    <div class="stat-save-box" title="Spells (S)">
      <div class="stat-save-label">S</div>
      <div class="stat-save-val">12</div>
    </div>
  </div>

  <div class="stat-section-title">Thief Skills (Labyrinth Lord 5th Level)</div>
  <div class="stat-pill-list">
    <div class="stat-pill"><strong>Pick Pockets:</strong> 50%</div>
    <div class="stat-pill"><strong>Open Locks:</strong> 42%</div>
    <div class="stat-pill"><strong>Find/Remove Traps:</strong> 40%</div>
    <div class="stat-pill"><strong>Move Silently:</strong> 47%</div>
    <div class="stat-pill"><strong>Climb Sheer Surfaces:</strong> 89%</div>
    <div class="stat-pill"><strong>Hide in Shadows:</strong> 34%</div>
    <div class="stat-pill"><strong>Hear Noise:</strong> 1-3 on 1d6</div>
    <div class="stat-pill"><strong>Backstab:</strong> x3 Damage</div>
  </div>

  <div class="stat-section-title">Signature Equipment &amp; Street Relics</div>
  <div class="stat-pill-list">
    <div class="stat-pill">⚔️ <em>"El Picotazo"</em> (+1 Bone-Hilted Stiletto; carved from the bill of an estuary gar-fish; +1 on initiative rolls when drawn from his boot)</div>
    <div class="stat-pill">⚔️ Masterwork Lockpicks (Folded inside a greaseproof pig-bladder in his collar; +5% on Open Locks checks)</div>
    <div class="stat-pill">⚔️ Spider-Silk Climbing Cord (40-foot length, holds 400 lbs, muffled triple-fluked bronze grappling hook)</div>
    <div class="stat-pill">⚔️ Pawn Ticket from Broker Ignatus (Pawned his father's silver signet ring for 12 copper bits)</div>
  </div>

  <div class="stat-section-title">Special Combat Feats &amp; Street Arts</div>
  <p><strong>Gutter Slip:</strong> When Joachor is hit by a melee weapon, he can spend his reaction to collapse limp and roll backward 10 feet into shadows, reducing the damage by 1d6 (once per combat).<br>
  <strong>Rooftop Navigation:</strong> Joachor suffers no movement penalty when traversing sloped tile roofs, slippery sewer masonry, or narrow window ledges. In the alleys of Kordova, he detects ambushes and city watch patrols on 1-4 on 1d6.</p>

  <div class="stat-section-title">Power Scale vs. PC Triumvirate (Level 8–9 Rulers)</div>
  <p class="text-muted" style="margin-bottom: 0;">With only 18 HP and AC 5, Joachor is extraordinarily fragile compared to the Level 8–9 PC monarchs. A single blow from Don Rodorigo or a heavy caballero lance would cleave him in two. His value to the party is not martial brute force, but his encyclopedic knowledge of Kordova's subterranean drains, his cutpurse connections, and his willingness to risk his neck for silver.</p>
</div>

<h3>Origin: Hard Times in Kordova</h3>
<p>In the wake of <a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio de Sadoria</a> declaring national bankruptcy, economic paralysis has strangled Kordova. Grandees have locked their townhouses and doubled their private guard contingents; foreign trade caravans from Argos are stalled at the docks; and <a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a> has instituted draconian street curfews backed by public hangings. Worse still, <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a>'s industrial zombie laborers have replaced living dockworkers and quarry porters throughout the Lower Wards, destroying the casual wage economy upon which thousands of cutpurses, fences, and tavern keepers survived.</p>

<p>For Joachor Valiento, the son of a disgraced armorer who died during the Period VII civil war, the squeeze proved catastrophic. Last month, desperate for coin, Joachor attempted to pick the strongbox of an armored carriage belonging to <a href="#npcs/gonzalo-guarralid" class="wiki-link">Duke Gonzalgo de Guarralid</a>. The theft was botched when royal caballeros ambushed his crew. Joachor fled into the sewers, but his partners were captured and broken upon the wheel. Under the unwritten laws of <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild of Kordova</a> (<em>El Pundonor del Arroyo</em>), a thief who draws watch attention to a guild mark must pay a punitive "blood tithe." Guildmaster <a href="#npcs/beltran-desoto" class="wiki-link">Don Beltrano de Zoto</a> assessed Joachor an impossible fine of <strong>80 gold sovereigns</strong>.</p>

<h3>The Session 1 Encounter: The Bargain at The Drowned Rat</h3>
<p>Dressed in rags and nursing a single mug of sour vinegar-ale in the corner of <em>The Drowned Rat</em>—a sunken tavern clinging to the sewer flues where the Lower Ward drains into <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>—Joachor spotted the Player Characters. Despite their disguises or court cloaks, Joachor's practiced eye recognized high bearing, desperate ambition, and heavy purses.</p>

<p>Taking the gamble of his life, Joachor approached the Triumvirate and laid his cards on the table:</p>
<ul>
  <li><strong>The Introduction:</strong> He agreed to guide the PCs blindfolded through the labyrinthine sewer conduits to the <em>Cistern of the Blind Saint</em> and formally present them to the Inner Council of <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild of Kordova</a>.</li>
  <li><strong>The Demands:</strong> Immediate coin to pay his tavern debt, redeem his father's ring from the pawnshop, and buy boots; plus a sacred, unbreakable blood-oath that he will be included as an active partner in any future heists, smuggling operations, or schemes the PCs hatch.</li>
  <li><strong>The Warning:</strong> Joachor shared critical street intelligence: an alien, displaced thieves' guild from the southern port of <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>—violently kicked out of their home city by fanatical religious refugees from Kordova—has washed ashore in the capital and is aggressively muscling in on the Night Guild's turf, murdering local lookouts in broad daylight.</li>
</ul>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p><strong>The Alcázar Drainage Chimney:</strong> Joachor possesses one immense secret he has concealed from both the guild and the PCs: while fleeing a watch patrol six months ago, he discovered an ancient vertical chimney conduit that leads from the upper storm drains directly into the dry larder beneath <a href="#npcs/basto" class="wiki-link">Maestro Bartorzo</a>'s royal kitchens in <a href="#gazetteer/palace-of-kordava" class="wiki-link">The High Alcázar</a>. If pressed or rewarded, he can guide the PCs into their own palace unnoticed, bypassing Don Rodorigo's gatehouse guards entirely.</p>
  <p><strong>The Debt Deadline:</strong> Joachor has exactly 48 hours remaining before Guild Enforcer 'El Macho' Murzio Corvo tracks him down. If the PCs do not help him pay or renegotiate his 80-sovereign debt, the guild will seize him and sell him to Master Vane's corpse-carts.</p>
</div>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Midnight Descent to the Cistern</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Joachor is ready to lead the PCs to meet <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano</a>. However, the path winds through the contested border zones of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>, where lookouts from the <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a> are lying in ambush. The PCs must choose whether to take the flooded sewer skiffs (risking toxic water and drowners) or the dry upper catacombs (risking a violent knife-fight with Velascan scouts).</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 14 Stealth / Move Silently to slip past Velascan sentries; DC 15 Persuasion / Pundonor check to address Don Beltrano without insulting the guild's gutter pride.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If the PCs enter the Cistern armed with royal army insignia or fail to disarm before Beltrano's crossbowmen, the guild assumes Joachor has led a royal purge squad and attacks in force.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Pawnshop Stiletto Recovery</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Before Joachor will step into the deep cisterns, he begs the PCs to help him recover <em>"El Picotazo"</em>—his magical gar-fish stiletto pawned to Ignatus the Bone-Carver for 15 silver pieces. Unfortunately, a corrupt royal army watch sergeant named Corporal Vanezo has already claimed the blade and is currently drinking in a nearby guard post. The PCs can buy it back at extortionate markup, pickpocket the drunken sergeant, or provoke a street duel under Pundonor.</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 15 Sleight of Hand / Pick Pockets; DC 14 Intimidation; or an honor duel at rapier point.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If violence breaks out in the guard post, General Valenza's caballeros seal the district gates, trapping the PCs in the Lower Wards past curfew.</p>
</div>
""",
        "gmSecrets": "Joachor owes 80 gold sovereigns in blood tithe to Don Beltrano de Zoto. He knows an unmapped vertical flue leading into the High Alcázar's kitchens beneath Maestro Bartorzo's domain.",
        "relatedIds": ["kordovan-thieves-guild", "beltran-desoto", "velasco-thieves-guild", "casimiro-velasco", "the-pit", "kordava", "palace-of-kordava", "court-matrix"]
    }

    # -------------------------------------------------------------
    # 2. NEW ARTICLE: beltran-desoto (NPC: Guildmaster Don Beltrano)
    # -------------------------------------------------------------
    beltran_article = {
        "id": "beltran-desoto",
        "category": "npcs",
        "title": "Guildmaster Don Beltrano 'One-Eye' de Zoto",
        "subtitle": "Master of the Kordovan Night Guild & Patriarch of the Pit • The Shadow Exchange",
        "tags": ["Royal Court", "NPC", "Thief", "Crime Lord", "Night Guild", "The Pit", "Kordava", "Underworld"],
        "aliases": [
            "Don Beltrano",
            "El Tuerto",
            "Beltrano de Zoto",
            "The One-Eyed Crow",
            "Guildmaster Beltrano",
            "Master of the Night Guild",
            "Patriarch of the Pit"
        ],
        "summary": "The cynical, aristocratic patriarch of Kordova's indigenous thieves' guild. Ruling from the pre-Cataclysmic Cistern of the Blind Saint beneath The Pit, he governs the capital's criminal fraternity through fear, ancient gutter honor (El Pundonor del Arroyo), and an intricate network of fences, smugglers, and extortionists.",
        "atAGlance": {
            "appearance": "An austere, silver-bearded Zingaran of fifty-eight in faded grandee silks and a heavy sable cloak. His right eye is covered by a polished silver plate beaten into the likeness of a weeping eye; his left eye is pale, hawk-sharp, and unblinking. Wears three antique gold rings on ink-stained, scarred fingers.",
            "mannerisms": "Speaks with aristocratic precision that suddenly snaps into lethal street cant; sips spiced wine from a dented silver chalice while coldly calculating the net bullion value of everyone in the room.",
            "quote": "The Grandees above walk upon crystal and imagine they hold the heavens. But crystal is brittle, my young Lieges, and it rests upon our stone. In Kordova, kings rule the daylight; I govern everything that breathes in the dark.",
            "courtDCs": "Morale: 10; Initial Reaction: -1 on 2d6 Reaction Rolls (Suspicious & Calculating); DC 18 Charisma check (or a scheme promising at least 500 gp in net silver) to secure an operational alliance; DC 16 Wisdom check to detect his 4 hidden heavy crossbowmen.",
            "publicStance": "Officially dead in royal genealogies; formerly a minor noble of House Soto stripped of lands during the Period VII Restoration Civil War.",
            "secretAgenda": "Beltrano is terrified that the violent Velasco Syndicate will assassinate his lieutenants and seize the docks, but his pride forbids him from showing weakness. Furthermore, he possesses an ancient brass key that unlocks the Subterranean Water-Gate beneath the High Alcázar—a secret he has withheld even from Sadoria.",
            "rival": "Capitán Don Cazmiro de Velasco & General Don Rodorigo de Valenza",
            "classLevel": "11th-Level Thief (Master Criminal Patriarch)",
            "combatStats": "AC 0 (AAC 19) | HP 44 | THAC0 14 | Atk +8 (1d6+3 + venom) | Backstab x4 | Saves: 8/6/5/7/7"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Night Guild of Kordova &bull; Master of the Shadow Exchange</span>
    <span class="badge rival-badge">Primary Rivals: Capitán Don Cazmiro de Velasco &amp; General Don Rodorigo de Valenza</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> An austere, aristocratic Zingaran patriarch in his late fifties with a clipped silver beard and a tall, gaunt frame. Wears a faded, moth-eaten grandee doublet of midnight-blue velvet over dark silk mail, draped in a sable cloak. His right eye socket is covered by a polished silver plate embossed with a weeping eye; his left eye is pale grey, icy, and relentlessly calculating.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Alternates between courtly high-Zingaran rhetoric and raw cutpurse cant; idly turns an antique ivory chess piece between his thumb and forefinger; never turns his back to an unbarred passage.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;The Grandees above walk upon crystal and imagine they hold the heavens. But crystal is brittle, my young Lieges, and it rests upon our stone. In Kordova, kings rule the daylight; I govern everything that breathes in the dark.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 10; Initial Reaction: -1 on 2d6 Reaction Rolls (Suspicious &amp; Proud). DC 18 Charisma check or a tangible proposition worth 500+ gp to win his operational partnership.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Guildmaster Don Beltrano 'One-Eye' de Zoto</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Patriarch of the Pit &amp; Supreme Arbiter of the Gutter &bull; Neutral (Ruthless self-preservation, criminal order, punctilious underworld honor)</div>
    </div>
    <span class="stat-class-level">⚔️ 11th-Level Thief (Shadow Guildmaster)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 0 (AAC 19) <small class="text-dim">(Elven Shadow-Silk Gambeson +2, Ring of Protection +2, DEX 17 (-2))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 9d4+2 (+9 CON bonus) &bull; <span style="color: #2ecc71; font-weight: 700;">44 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 14 (Base Attack Bonus +5)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +8 to hit (<em>La Espina de Plata</em> +2 dueling rapier, 1d6+3 piercing + Lotus-Sap venom [Save vs Poison or collapse unconscious for 1d6 turns]); Off-Hand: +7 to hit (<em>The Crow's Beak</em> +1 main-gauche, 1d4+2, -1 AC bonus); Backstab: x4 Damage (4d6+12 + venom)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box">
      <div class="stat-ability-label">STR</div>
      <div class="stat-ability-score">12</div>
      <div class="stat-ability-mod">Normal (0)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">DEX</div>
      <div class="stat-ability-score">17</div>
      <div class="stat-ability-mod">+2 missile to hit, -2 AC bonus</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">+1 HP per Hit Die up to 9th level</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">16</div>
      <div class="stat-ability-mod">+2 languages, strategic underworld mastermind</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 on saving throws vs. magical spells</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 reaction, 6 retainers, morale 10</div>
    </div>
  </div>

  <div class="stat-section-title">Saving Throws (Labyrinth Lord 5-Column)</div>
  <div class="stat-saves-bar">
    <div class="stat-save-box" title="Breath Weapon (BW)">
      <div class="stat-save-label">BW</div>
      <div class="stat-save-val">10</div>
    </div>
    <div class="stat-save-box" title="Poison or Death (P/D)">
      <div class="stat-save-label">P/D</div>
      <div class="stat-save-val">7</div>
    </div>
    <div class="stat-save-box" title="Petrify or Paralyze (PP)">
      <div class="stat-save-label">PP</div>
      <div class="stat-save-val">6</div>
    </div>
    <div class="stat-save-box" title="Wands (W)">
      <div class="stat-save-label">W</div>
      <div class="stat-save-val">8</div>
    </div>
    <div class="stat-save-box" title="Spells (S)">
      <div class="stat-save-label">S</div>
      <div class="stat-save-val">8</div>
    </div>
  </div>

  <div class="stat-section-title">Thief Skills (Labyrinth Lord 11th Level)</div>
  <div class="stat-pill-list">
    <div class="stat-pill"><strong>Pick Pockets:</strong> 80%</div>
    <div class="stat-pill"><strong>Open Locks:</strong> 68%</div>
    <div class="stat-pill"><strong>Find/Remove Traps:</strong> 65%</div>
    <div class="stat-pill"><strong>Move Silently:</strong> 72%</div>
    <div class="stat-pill"><strong>Climb Sheer Surfaces:</strong> 93%</div>
    <div class="stat-pill"><strong>Hide in Shadows:</strong> 60%</div>
    <div class="stat-pill"><strong>Hear Noise:</strong> 1-4 on 1d6</div>
    <div class="stat-pill"><strong>Read Languages:</strong> 75%</div>
    <div class="stat-pill"><strong>Read Magic Scrolls:</strong> 80% (Arcane and divine scrolls up to 6th level)</div>
    <div class="stat-pill"><strong>Backstab:</strong> x4 Damage</div>
  </div>

  <div class="stat-section-title">Signature Magic Items &amp; Regalia</div>
  <div class="stat-pill-list">
    <div class="stat-pill">⚔️ <em>La Espina de Plata</em> (+2 Zingaran Dueling Rapier; grants free riposte attack whenever an opponent misses him by 5 or more in melee)</div>
    <div class="stat-pill">⚔️ <em>The Crow's Beak</em> (+1 Parrying Main-Gauche; -1 AC in off-hand)</div>
    <div class="stat-pill">⚔️ Ring of Protection +2</div>
    <div class="stat-pill">⚔️ Cloak of the Bat (Grants fly speed 150' in darkness; +20% to Hide in Shadows)</div>
    <div class="stat-pill">⚔️ Boots of Elvenkind (100% silent movement)</div>
    <div class="stat-pill">⚔️ Master Sluice Key of King Kalenius (Ancient pre-Cataclysmic bronze key that unlocks the submerged water-gates beneath the High Alcázar)</div>
  </div>

  <div class="stat-section-title">Special Combat Feats &amp; Gutter Pundonor</div>
  <p><strong>Riposte Duelist:</strong> Beltrano treats rapier duels with deadly punctilio. Once per round, when an enemy misses a melee attack against him, he can counterattack immediately without expending his normal action.<br>
  <strong>Gaze of the Silver Eye:</strong> Once per day, Beltrano can focus ambient light through his polished silver eyepatch, releasing a 30-foot cone of blinding brilliance (Save vs Spells or blinded for 1d4 rounds).<br>
  <strong>Cistern Guard:</strong> Beltrano is never alone. In his audience chamber, 4 Veteran Crossbowmen (3rd-level Thieves, AC 4, 15 HP each, heavy crossbows loaded with drowsing poison) are concealed behind stone corbels.</p>

  <div class="stat-section-title">Power Scale vs. PC Triumvirate (Level 8–9 Rulers)</div>
  <p class="text-muted" style="margin-bottom: 0;">Beltrano matches the PCs in experience, cunning, and Lethal backstab capability (x4 multiplier can inflict 40+ damage in a surprise round). However, he commands an underworld militia, not an army; a direct frontal clash with the royal garrisons or the PC monarchs would destroy his network. He operates through bargains, leverage, and proxy assassinations.</p>
</div>

<h3>Background &amp; Underworld Rule</h3>
<p>Thirty years ago, Don Beltrano de Zoto was a dashing second son of House Soto, celebrated for his rapier work in the courtly duels of the High Alcázar. During the catastrophic civil war of Period VII, his elder brother backed the losing claimant. The victorious Restoration Council executed his kin, stripped the family estates, and cast Beltrano into the dungeons. Gouging out his own right eye to blind a torturer with the bone shard, Beltrano slipped his manacles, killed his jailer, and vanished into <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>.</p>

<p>Over two decades of methodical violence and calculated bribery, Beltrano forged the warring cutpurse gangs, river smugglers, and sewer fences into a unified syndicate: <strong>The Night Guild of Kordova</strong>. He installed a strict chivalric parody of Zingaran honor—<em>El Pundonor del Arroyo</em>—where violations of territory, theft from registered guild fences, or cooperation with royal inquisitors are punished by the severing of fingers or slow drowning in the cess-canals.</p>

<p>Today, Beltrano sits upon a velvet armchair salvaged from a sunken palace in the <strong>Cistern of the Blind Saint</strong>. He collects a mandatory 15% tribute on all contraband moving through Kordova, commands a cadre of roof-runners, and maintains files of blackmail on half the Grandees in court.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; THE SLUICE KEY</div>
  <p><strong>The High Alcázar Water-Gate:</strong> Beltrano's greatest secret is the <em>Master Sluice Key of King Kalenius</em>. Recovered from a sunken tomb in Period VII, this key unlocks an iron grate thirty cubits beneath the royal palace's sea-cliffs, leading directly into the flooded vaults below the Crystal Floor. Beltrano has never used it because he lacks the manpower to bypass the palace guards, but he is willing to trade this knowledge to the PC Triumvirate in exchange for royal protection against the invading Velasco Syndicate and official non-interference in his smuggling conduits.</p>
</div>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Audience in the Cistern</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> When Joachor introduces the PCs, Beltrano tests their mettle. He demands proof that the young Triumvirate has the stomach to rule Kordova's shadows. He challenges them to resolve an escalating crisis: either assassinate an inquisitorial contact from the Church of Nemeth who is threatening a guild warehouse, or arrange the discreet release of three senior guild fences currently held in the palace dungeons.</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 16 Charisma (Persuasion or Deception); DC 15 Streetwise / Pundonor Lore check; or successful execution of the jailbreak.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If the PCs attempt to arrest Beltrano during the audience, his concealed crossbowmen fire drowsing bolts, and the guild floods the chamber with waist-deep cesspool water before vanishing through secret sluices.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Velasco Hit-List</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Beltrano reveals that Capitán Don Cazmiro's Velascan cutthroats have assassinated two of his quartermasters in the Fishermen's Ward. Beltrano offers the PCs 500 gold sovereigns and a copy of the palace vault blueprints if they eliminate Cazmiro's chief assassin, Inés 'La Loba', who is stalking the harbor taverns.</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 16 Investigation / Tracking in the docks; DC 17 Perception to detect La Loba's garrotte ambush.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If the PCs contact Cazmiro instead, Beltrano learns of the betrayal within 24 hours through his beggar informants and cuts off all underworld assistance, directing street gangs to sabotage crown tax wagons.</p>
</div>
""",
        "gmSecrets": "Beltrano possesses the Master Sluice Key of King Kalenius, which opens the water-gate into the flooded vaults beneath the High Alcázar's Crystal Floor. He is desperate to destroy the Velasco Syndicate before they execute a coup in The Pit.",
        "relatedIds": ["kordovan-thieves-guild", "joaquin", "velasco-thieves-guild", "casimiro-velasco", "the-pit", "palace-of-kordava", "sadoria", "court-matrix"]
    }

    # -------------------------------------------------------------
    # 3. NEW ARTICLE: casimiro-velasco (NPC: Capitán Don Cazmiro)
    # -------------------------------------------------------------
    casimiro_article = {
        "id": "casimiro-velasco",
        "category": "npcs",
        "title": "Capitán Don Cazmiro 'The Hawk' de Velasko",
        "subtitle": "War-Boss of the Velascan Exiles & Corsair Raider • The Gilded Dagger",
        "tags": ["Royal Court", "NPC", "Thief", "Fighter", "Velasco", "Exile", "The Pit", "Kordava", "Corsair"],
        "aliases": [
            "Don Cazmiro",
            "El Gavilán",
            "The Sparrowhawk",
            "Cazmiro de Velasko",
            "Capitán Cazmiro",
            "Master of the Velasco Syndicate",
            "The Corsair of Velasco"
        ],
        "summary": "The vengeful, battle-scarred leader of the displaced Velasco thieves' syndicate. Expelled from his native port by militant religious refugees from Kordova, Cazmiro has brought his battle-hardened band of maritime cutthroats to the capital to carve out a new empire through raw violence.",
        "atAGlance": {
            "appearance": "A broad-shouldered, sun-baked corsair of forty-two with a swept black mustache, wearing a sea-stained turquoise velvet coat over a breastplate of beaten sea-bronze engraved with krakens. Gold hoops dangle from both ears. His left cheek is disfigured by a jagged, branded holy sun burned into his flesh by Velascan religious zealots.",
            "mannerisms": "Laughs loudly before making lethal threats; constantly flips a brass-hilted navaja clasp-knife; spits upon the flagstones whenever priests, holy refugees, or the Church of Nemeth are mentioned.",
            "quote": "Those psalm-singing zealots from your holy capital drove us into the sea with torches and scripture. They burned our galleons, hung our women, and branded our faces. Now we are in Kordova—and we will slit this city's fat throat until our purses are full again.",
            "courtDCs": "Morale: 11 (Vengeful desperation); Initial Reaction: -3 on 2d6 Reaction Rolls if any PC wears religious emblems; DC 17 Charisma check (or offering intelligence on religious refugee camps) to strike a mercenary pact.",
            "publicStance": "Presents himself as an independent Argossean merchant captain seeking commercial anchorage in Kordova's harbor.",
            "secretAgenda": "Cazmiro desires far more than street turf: he wants bloody vengeance against the Church of Nemeth and the religious refugees who expelled him from Velasco. He is planning a nocturnal slaughter of the refugee camp outside Kordova's South Gate, intending to plunder their hidden church bullion.",
            "rival": "Guildmaster Don Beltrano de Soto & Father Malachai the Blind",
            "classLevel": "10th-Level Fighter / 8th-Level Thief (Corsair Warlord)",
            "combatStats": "AC -1 (AAC 20) | HP 62 | THAC0 11 | Atk +13 (1d8+6) & +11 (1d4+4) | Backstab x3 | Saves: 8/6/7/8/9"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Velasco Syndicate &bull; War-Boss of the Mudflats</span>
    <span class="badge rival-badge">Primary Rivals: Guildmaster Don Beltrano de Soto &amp; Father Malachai the Blind</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A barrel-chested, sun-darkened Zingaran corsair in his early forties with a swept black mustache and smoldering amber eyes. Wears a salt-crusted turquoise velvet frock coat trimmed with tarnished gold braid over a cuirass of green-patinated sea-bronze. His left cheek bears a hideous, raised brand of the holy sun—burned into his bone by the inquisitors of Velasco.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Flamboyant, boisterous swagger that instantly shifts into psychopathic focus; constantly clicks open and shut an enormous eight-inch bone-and-brass navaja; grinds his teeth at the sound of church bells.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;Those psalm-singing zealots from your holy capital drove us into the sea with torches and scripture. They burned our galleons, hung our women, and branded our faces. Now we are in Kordova—and we will slit this city's fat throat until our purses are full again.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 11 (Furious desperation); Initial Reaction: -3 on 2d6 Reaction Rolls if any party member displays holy symbols. DC 17 Charisma check or an offer of revenge against church zealots to negotiate.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Capitán Don Cazmiro 'The Hawk' de Velasko</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">War-Boss of the Velascan Exiles &amp; Master of the Gilded Dagger &bull; Chaotic (Vengeful fury, ruthless greed, fiercely protective of his surviving crew)</div>
    </div>
    <span class="stat-class-level">⚔️ 10th-Level Fighter / 8th-Level Thief (Corsair Warlord)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC -1 (AAC 20) <small class="text-dim">(Enchanted Sea-Bronze Breastplate +2, Large Corsair Buckler +1, DEX 16 (-2))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 9d8+2 (+18 CON bonus on first 9 HD) &bull; <span style="color: #2ecc71; font-weight: 700;">62 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40') / Swimming 90'</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 11 (Base Attack Bonus +8)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Primary: +13 to hit (<em>The Sea-Fang</em> +2 falchion, 1d8+6 slashing, cleave on kill); Off-Hand: +11 to hit (<em>The Salt-Bite</em> +2 navaja, 1d4+4 piercing + Sea-Wasp venom [Save vs Poison or suffer -4 to hit and AC for 1d6 rounds]); Backstab: x3 Damage (3d8+18 with falchion from stealth)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box">
      <div class="stat-ability-label">STR</div>
      <div class="stat-ability-score">18</div>
      <div class="stat-ability-mod">+3 to hit, +3 damage, Open Doors 1-5 on 1d6</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">DEX</div>
      <div class="stat-ability-score">16</div>
      <div class="stat-ability-mod">+2 missile to hit, -2 AC bonus</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">17</div>
      <div class="stat-ability-mod">+2 HP per Hit Die up to 9th level</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">+1 language, naval boarding tactics</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">11</div>
      <div class="stat-ability-mod">Normal (0)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">16</div>
      <div class="stat-ability-mod">+1 reaction, 6 retainers, morale 11</div>
    </div>
  </div>

  <div class="stat-section-title">Saving Throws (Labyrinth Lord 5-Column)</div>
  <div class="stat-saves-bar">
    <div class="stat-save-box" title="Breath Weapon (BW)">
      <div class="stat-save-label">BW</div>
      <div class="stat-save-val">9</div>
    </div>
    <div class="stat-save-box" title="Poison or Death (P/D)">
      <div class="stat-save-label">P/D</div>
      <div class="stat-save-val">8</div>
    </div>
    <div class="stat-save-box" title="Petrify or Paralyze (PP)">
      <div class="stat-save-label">PP</div>
      <div class="stat-save-val">9</div>
    </div>
    <div class="stat-save-box" title="Wands (W)">
      <div class="stat-save-label">W</div>
      <div class="stat-save-val">10</div>
    </div>
    <div class="stat-save-box" title="Spells (S)">
      <div class="stat-save-label">S</div>
      <div class="stat-save-val">11</div>
    </div>
  </div>

  <div class="stat-section-title">Thief Skills (Labyrinth Lord 8th Level)</div>
  <div class="stat-pill-list">
    <div class="stat-pill"><strong>Pick Pockets:</strong> 65%</div>
    <div class="stat-pill"><strong>Open Locks:</strong> 54%</div>
    <div class="stat-pill"><strong>Find/Remove Traps:</strong> 50%</div>
    <div class="stat-pill"><strong>Move Silently:</strong> 57%</div>
    <div class="stat-pill"><strong>Climb Sheer Surfaces:</strong> 91%</div>
    <div class="stat-pill"><strong>Hide in Shadows:</strong> 45%</div>
    <div class="stat-pill"><strong>Hear Noise:</strong> 1-3 on 1d6</div>
    <div class="stat-pill"><strong>Backstab:</strong> x3 Damage</div>
  </div>

  <div class="stat-section-title">Signature Magic Items &amp; Regalia</div>
  <div class="stat-pill-list">
    <div class="stat-pill">⚔️ <em>The Sea-Fang</em> (+2 Falchion; forged from meteorite iron by Barachan corsairs; ignores water drag; inflicts +1d6 bleeding on critical hits)</div>
    <div class="stat-pill">⚔️ <em>The Salt-Bite</em> (+2 Navaja Clasp-Knife; spring-loaded blade; 1d4+4 damage)</div>
    <div class="stat-pill">⚔️ Sea-Bronze Breastplate +2 (Impervious to rust; allows swimming at full land movement without encumbrance penalties)</div>
    <div class="stat-pill">⚔️ Ring of Fire Resistance (Allowed him to survive when religious mobs set fire to his Velasco guildhouse)</div>
    <div class="stat-pill">⚔️ <em>The Tears of Saint Moranna</em> (Stolen pre-Cataclysmic crying chalice; 1/week transforms 50 gallons of fresh water into corrosive acid)</div>
  </div>

  <div class="stat-section-title">Special Combat Feats &amp; Corsair Arts</div>
  <p><strong>Two-Weapon Boarding Tempest:</strong> Cazmiro fights with both falchion and navaja simultaneously without dual-wielding penalties. In close-quarters combat (such as tavern brawls or ship decks), he gains a +2 bonus on damage rolls.<br>
  <strong>Berserk Zealot-Hatred:</strong> When fighting clerics, paladins, or religious zealots (especially the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a>), Cazmiro gains +2 to hit, +4 damage, and immunity to fear and charm spells, but cannot retreat until all religious foes are dead.<br>
  <strong>Mudflat Retinue:</strong> In his hideout aboard the rotting hulks, Cazmiro is flanked by 8 Velascan Sea-Wolves (Fighters Level 3, AC 4, 18 HP each, armed with boarding axes and cutlasses).</p>

  <div class="stat-section-title">Power Scale vs. PC Triumvirate (Level 8–9 Rulers)</div>
  <p class="text-muted" style="margin-bottom: 0;">Cazmiro is an absolute martial powerhouse (62 HP, AC -1, two attacks dealing heavy damage). In open combat, he can trade blows with the PC Warrior on equal terms. His weakness is his psychopathic hatred for religion and his volatile temper, which can be exploited by clever diplomats or tacticians.</p>
</div>

<h3>The Fall of Velasco &amp; The Long March</h3>
<p>Until six months ago, Don Cazmiro reigned as the undisputed criminal master of <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>, running the privateer docks, luxury gambling galleons, and wine-smuggling fleets that made the southern port rich. But when the royal army cracked down on the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a> in Kordova, more than fifteen thousand religious refugees swarmed south into Velasco.</p>

<p>Organized into militant holy fraternities by fiery prophets, the refugees declared Velasco a 'City of Sacred Purification.' They overthrew the corrupt Grandees, seized the armories, and launched a merciless purge of the criminal underworld. Cazmiro's guildhouse was burned to the ground; ninety of his thieves were hung from the cathedral yard; and Cazmiro himself was captured, tied to a stone pillar, and branded with a red-hot iron in the likeness of the holy sun before his surviving corsairs staged a desperate midnight rescue.</p>

<p>Fleeing in three battered merchant cogs, Cazmiro and sixty battle-hardened survivors sailed north to Kordova. Impoverished, homeless, and burning with fury, they established a fortified camp among the abandoned, rotting hulks grounded in the tidal mudflats outside Kordova's harbor boom. From this redoubt, they have launched an aggressive campaign to carve out territory in Kordova by murdering lookouts from <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild</a>, seizing dockside smuggling slips, and hunting down religious refugees living in the capital's shantytowns.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE ACID CHALICE CONSPIRACY</div>
  <p><strong>The Tears of Saint Moranna:</strong> Before fleeing Velasco, Cazmiro's men looted a pre-Cataclysmic relic from the Convent of the Weeping Mother: <em>The Tears of Saint Moranna</em>. Cazmiro has concocted a horrific revenge scheme: he plans to sneak a squad into Kordova's South Ward and submerge the chalice inside the primary public cistern supplying the religious refugee camps, poisoning thousands of devotees with corrosive acid. The PCs can prevent this atrocity, weaponize it against church zealots, or force Cazmiro to surrender the chalice in exchange for a royal pardon.</p>
</div>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Mudflat Parley</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Word reaches the PCs that Cazmiro is looking for a powerful sponsor to legitimize his presence in Kordova. The PCs can row out across the treacherous tidal mudflats at low tide to negotiate with the corsair war-boss. Cazmiro offers to serve as the Triumvirate's personal shadow enforcers—hunting down republican rebels and sabotaging Council ledgers—if the crown grants him exclusive smuggling charters and orders General Valenza's garrisons to stand down.</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 15 Dexterity / Agility to navigate sinking mud and rope-bridges; DC 16 Charisma (Persuasion or Intimidation) to hold Cazmiro's respect.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If the tide rises while the PCs are aboard the rotting hulks, the retreat causeway floods with 12 feet of shark-infested sea water, leaving them trapped among 60 cutthroats.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Fishmarket Massacre</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Cazmiro's raiders stage a daylight assault on a Night Guild safehouse located beneath the Lower Fishmarket, turning the docks into a bloody battlefield. The PCs must choose whether to intervene with royal guards (risking exposure of their involvement in the underworld), hire mercenaries to wipe out the Velascans, or let the two guilds slaughter each other to weaken both.</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 16 Tactics / Command; DC 15 Reflex saving throw to avoid burning pitch hurled by corsairs.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If the battle spills into the open streets, General Valenza declares martial law across the Lower Wards and executes 20 commoners as examples.</p>
</div>
""",
        "gmSecrets": "Cazmiro possesses The Tears of Saint Moranna and intends to poison the refugee cisterns outside Kordova's South Gate. He is open to becoming a crown proxy if offered royal legitimacy.",
        "relatedIds": ["velasco-thieves-guild", "kordovan-thieves-guild", "beltran-desoto", "joaquin", "velasco", "the-pit", "church-of-nemeth", "court-matrix"]
    }

    # -------------------------------------------------------------
    # 4. NEW ARTICLE: kordovan-thieves-guild (Faction)
    # -------------------------------------------------------------
    kordovan_guild_article = {
        "id": "kordovan-thieves-guild",
        "category": "factions",
        "title": "The Night Guild of Kordova (La Cofradía de la Sombra)",
        "subtitle": "The Shadow Exchange • Indigenous Underworld Syndicate of the Capital & The Pit",
        "tags": ["Faction", "Thieves Guild", "Kordava", "The Pit", "Underworld", "Night Guild", "Period VIII"],
        "aliases": [
            "Night Guild of Kordova",
            "La Cofradía de la Sombra",
            "The Kordovan Thieves Guild",
            "Kordovan Guild",
            "The Shadow Exchange",
            "Cofradía de la Sombra",
            "The Local Guild",
            "Kordova Thieves Guild",
            "The Night Guild"
        ],
        "summary": "The ancient, entrenched underworld syndicate governing crime, smuggling, fencing, and extortion across Kordova and The Pit. Currently suffering under royal bankruptcy, zombie labor displacement, and an aggressive turf war launched by displaced cutthroats from Velasco.",
        "content": """
<div class="info-card">
  <p><strong>Faction Classification:</strong> Entrenched Urban Criminal Syndicate &bull; Shadow Fraternity</p>
  <p><strong>Supreme Leader:</strong> <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano 'One-Eye' de Zoto</a></p>
  <p><strong>Headquarters:</strong> The Cistern of the Blind Saint (Subterranean pre-Cataclysmic reservoir beneath <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>)</p>
  <p><strong>Faction Symbol:</strong> A silhouette of a black cat perched upon a cracked silver sovereign</p>
  <p><strong>Operational Strength:</strong> ~180 sworn cutpurses, fences, smugglers, and lock-breakers, plus hundreds of street urchins and tavern lookouts</p>
</div>

<h3>1. Overview &amp; Underworld Identity</h3>
<p><strong>The Shadow Twin of the High Alcázar.</strong> Established during Period IV (The Zombie Era) when municipal laborers and artisans were first displaced by enslaved undead, <strong>The Night Guild of Kordova</strong> (known in street cant as <em>La Cofradía de la Sombra</em> or <em>The Shadow Exchange</em>) is not a chaotic mob of bandits, but a deeply organized, ritualistic criminal brotherhood. Operating as the subterranean counterpart to the royal court, the guild regulates all illegal commerce across Kordova's Lower Wards, the harbor wharves, and the sunken ruins of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>.</p>

<p>The guild views itself as an essential pillar of Zingaran reality: while the Grandees play with silk, duels, and royal genealogies in the soaring spires of the <a href="#gazetteer/palace-of-kordava" class="wiki-link">High Alcázar</a>, the Night Guild manages the bread, silver, and vices of the half-million souls struggling in the city's mud.</p>

<h3>2. The Code: El Pundonor del Arroyo</h3>
<p>Unlike barbarian thieves, the Night Guild adheres to a strict, cynical parody of aristocratic Zingaran honor, known as <strong>El Pundonor del Arroyo</strong> ("The Honor of the Gutter"):</p>
<ul>
  <li><strong>The Ward Franchise:</strong> No member may pick a pocket, crack a lock, or cut a throat in another member's designated alley without paying a 20% territorial tithe to the local Ward Warden.</li>
  <li><strong>The Silence of the Iron Jaw:</strong> Any brother captured by <a href="#npcs/valenza" class="wiki-link">General Valenza</a>'s royal army who confesses under torture faces the 'Salt Bath'—his kin are stripped of guild protection, and he is executed upon his release.</li>
  <li><strong>Sanctuary of the Cistern:</strong> Drawing steel or spilling blood within the <em>Cistern of the Blind Saint</em> is punished by instant defenestration into the drowning sumps.</li>
  <li><strong>The Blood-Tithe on Botched Work:</strong> Any thief whose carelessness brings military garrisons into a guild quarter must pay a punitive fine (the blood-tithe) or be sold as unfree labor. This is the very trap currently crushing <a href="#npcs/joaquin" class="wiki-link">Joachor 'The Jackdaw' Valiento</a>.</li>
</ul>

<h3>3. Hard Times in Kordova: The Syndicate Under Siege</h3>
<p>The start of Period VIII has brought the Night Guild to the brink of financial starvation. The crisis is driven by three interlocking disasters:</p>
<ol>
  <li><strong>The Bankrupt Royal Treasury:</strong> With <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio de Sadoria</a> locking the mints and defaulting on foreign loans, high-denomination gold and silver have evaporated from Kordova's street economy. Wealthy Grandees have retreated into fortified compounds, leaving common cutpurses with nothing to steal but debased copper bits.</li>
  <li><strong>The Undead Labor Displacement:</strong> <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a>'s expansion of industrial necromancy has replaced living dockworkers and carters with mindless zombies. The guild previously earned massive revenue running protection rackets, gambling dens, and loan-sharking operations for living dock labor; zombies require neither food, dice, nor prostitutes.</li>
  <li><strong>Martial Curfews &amp; Public Hangings:</strong> General Don Rodorigo has deployed armored caballero patrols into the lower alleys, hanging suspected thieves from bridge arches without trial under martial decrees.</li>
</ol>

<h3>4. Active Schemes of the Night Guild</h3>
<ul>
  <li><strong>The Sump Siphon (Alcázar Infiltration):</strong> Guild sappers have been quietly picking through ancient Thurian drainage tunnels beneath <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>, seeking a route into the vaults beneath the <em>Crystal Floor</em> of the High Alcázar. Guildmaster Beltrano suspects an unlooted pre-Cataclysmic bullion cache lies sealed beneath the palace foundations.</li>
  <li><strong>The Embalming Salt Hijacking:</strong> To disrupt Master Vane's industrial monopoly, the guild has begun ambushing wagons carrying specialized mummification resins and soul-binding salts entering Kordova from the Zingg Valley, extorting the crown for their ransom.</li>
  <li><strong>Counterfeiting in the Sunken Ironworks:</strong> In a flooded smithy beneath The Pit, the guild operates a clandestine mint melting down lead sinkers and Argossean bronze to press counterfeit silver sovereigns.</li>
  <li><strong>Defensive Guerrilla Turf War:</strong> Setting deadfalls, sewer grease-traps, and crossbow ambushes to repel the brutal invasion of the <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a>.</li>
</ul>

<h3>5. Primary Hideouts &amp; Fronts</h3>
<ul>
  <li><strong>The Cistern of the Blind Saint:</strong> The master stronghold of the guild. A colossal subterranean vaulted reservoir built of Cyclopean granite during Period II. Accessible only via a counterweighted iron cage dropped down a dry well, or by swimming through a submerged sewer siphon. Holds the guild council chamber, the stolen goods vault, and Beltrano's private quarters.</li>
  <li><strong>The Drowned Rat Tavern:</strong> A squalid, waterlogged dive clinging to the sewer outfall in the Lower Ward. Managed by Old Mother Vespera, a retired fence. Serves as the primary public contact point where street runners like <a href="#npcs/joaquin" class="wiki-link">Joachor</a> meet foreign contacts and marks.</li>
  <li><strong>The Charnel Wharf:</strong> A hidden canal dock beneath Kordova's slaughterhouses where flat-bottomed skiffs unload untaxed wine, weapons, and smuggled silk in pitch darkness.</li>
</ul>

<h3>6. Cross-Faction Matrix &amp; Connections</h3>
<ul>
  <li><strong><a href="#factions/republican-insurgents" class="wiki-link">Republican Insurgents</a>:</strong> Uneasy coexistence in The Pit. <a href="#npcs/lucia" class="wiki-link">Luzaia de Vegara</a> despises the guild's criminal selfishness, but buys lockpicks, smuggled shortswords, and tunnel guides from Beltrano's fences.</li>
  <li><strong><a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio de Sadoria</a>:</strong> A corrupt, symbiotic relationship. Sadoria knows the guild exists and uses dead-drops to hire them for off-the-books assassinations and document theft, while staging periodic public raids to maintain appearances.</li>
  <li><strong><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a>:</strong> Uncompromising mortal hatred. Valenza views the guild as vermin and executes any member captured in the streets.</li>
  <li><strong><a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a>:</strong> The fanatical cult views the guild as demonic corrupters of the lower classes, frequently staging holy arson attacks against guild-affiliated brothels and dens.</li>
  <li><strong><a href="#factions/velasco-thieves-guild" class="wiki-link">The Velasco Syndicate</a>:</strong> Active, bloody gang war. Cazmiro's exiles are murdering Kordovan lookouts and seizing dock territory.</li>
</ul>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE GUILD'S STRATEGIC VALUE TO THE TRIUMVIRATE</div>
  <p>If the PC Triumvirate forms an alliance with the Night Guild through Joachor Valiento, they gain an operational asset their puppetmasters cannot control: an army of 180 cutpurses, cat burglars, and roof-runners who know every secret passage in Kordova. The guild can deliver blackmail on Grandees, smuggle the PCs out of the palace past Don Rodorigo's guards, and steal documents from Marquis Murzio's locked archives. But if the PCs double-cross Beltrano, the guild can turn the city's lower wards into an unmanageable riot zone.</p>
</div>
""",
        "gmSecrets": "The Night Guild controls pre-Cataclysmic tunnels leading directly beneath the High Alcázar. They are currently losing the dock war against the Velasco Syndicate and desperately need royal intervention or black-powder weapons.",
        "relatedIds": ["joaquin", "beltran-desoto", "velasco-thieves-guild", "casimiro-velasco", "the-pit", "kordava", "palace-of-kordava", "sadoria", "lucia", "court-matrix"]
    }

    # -------------------------------------------------------------
    # 5. NEW ARTICLE: velasco-thieves-guild (Faction)
    # -------------------------------------------------------------
    velasco_guild_article = {
        "id": "velasco-thieves-guild",
        "category": "factions",
        "title": "The Velasco Syndicate (The Gilded Dagger Exiles)",
        "subtitle": "Displaced Maritime Cutthroats & The League of the Red Tide • Velascan Invaders",
        "tags": ["Faction", "Thieves Guild", "Velasco", "Exiles", "Underworld", "Gang War", "The Pit", "Period VIII"],
        "aliases": [
            "Velasco Thieves Guild",
            "The Velasco Syndicate",
            "Velascan Exiles",
            "The Gilded Dagger",
            "La Garra Dorada",
            "Velasco Guild",
            "The Exiles of Velasco",
            "League of the Red Tide",
            "Velascan Cutthroats"
        ],
        "summary": "The displaced maritime thieves' guild of Velasco, violently expelled from their homeland by zealous religious refugees fleeing Kordova. Now encamped in Kordova's tidal mudflats and sea-caves, they are aggressively muscling in on the local guild's turf with cutthroat corsair brutality.",
        "content": """
<div class="info-card">
  <p><strong>Faction Classification:</strong> Invading Displaced Criminal Syndicate &bull; Corsair Warband</p>
  <p><strong>Supreme Leader:</strong> <a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro 'The Hawk' de Velasko</a></p>
  <p><strong>Headquarters:</strong> The Rotting Hulks of the Mudflats (Three grounded merchant cogs outside Kordova's harbor boom)</p>
  <p><strong>Faction Symbol:</strong> A golden talon clutching a snapped galley oar above three red waves</p>
  <p><strong>Operational Strength:</strong> ~60 hardened corsairs, cutthroats, and assassins; desperate, heavily armed, and battle-tested</p>
</div>

<h3>1. Genesis: The Religious Refugee Cataclysm in Velasco</h3>
<p>Until six months ago, <strong>The Velasco Syndicate</strong> (celebrated in the south as <em>La Garra Dorada</em> or <em>The Gilded Dagger</em>) was one of the wealthiest criminal syndicates in the Hyborian world. Headquartered in Zingara's sun-drenched southern port of <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>, they controlled luxury gambling galleons, the lucrative southern vintage smuggling trade, and deep-sea piracy along the Baracha Strait.</p>

<p>Their golden age ended in fire and blood. When <a href="#npcs/valenza" class="wiki-link">General Valenza</a> and the Restoration Council cracked down on the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a> in Kordova, more than fifteen thousand fanatical religious refugees fled south along the King's Highway to Velasco. There, joining with local ascetic sects, the refugees organized the <em>Inquisition of the Cleansing Tide</em>. Declaring all vice, luxury, and underworld operations to be blasphemous filth, the holy mobs stormed Velasco's palaces and warehouses with firebrands and war-mattocks.</p>

<p>The Velascan guild was caught completely unprepared. Their gaming galleons were torched in the harbor; their fences were broken on iron wheels; and their leaders were branded with the holy sun or burned at the stake. Stripped of their riches, homes, and dignity, the surviving sixty corsairs under <a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro</a> escaped aboard three battered cogs and sailed for Kordova—the very city whose religious turmoil had spawned their doom.</p>

<h3>2. The Velascan Threat in Kordova: Muscling in on Local Turf</h3>
<p>Arriving in Kordova destitute, bitter, and furious, Cazmiro's exiles have refused to beg for scraps. Viewing <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild of Kordova</a> as decadent, soft sewer-rats who have grown weak on pickpocketing and counterfeit coppers, the Velascans have launched a relentless, high-intensity turf war to seize control of the capital's underworld:</p>
<ul>
  <li><strong>The Dockside Purge:</strong> Velascan boarding parties have been ambushing Kordovan lookouts and river smugglers along the estuary. Over the past three weeks, seven Kordovan guild fences have been found in the harbor mud with their throats slashed from ear to ear.</li>
  <li><strong>Aggressive Undercutting:</strong> The Velascans are hijacking grain and wine barges on the open water before they reach the city docks, then fencing the stolen food directly to starving commoners at half the price charged by local merchants—winning immediate popular loyalty among the desperate poor.</li>
  <li><strong>Nocturnal Terror on Religious Refugees:</strong> Consumed by a pathological vendetta, Cazmiro's cutthroats stalk the outskirts of Kordova at night, hunting, beating, and murdering religious refugees and wandering Nemethian monks to avenge the purge of Velasco.</li>
</ul>

<h3>3. Key Figures of the Velasco Syndicate</h3>
<ul>
  <li><strong><a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro 'The Hawk' de Velasko</a>:</strong> Master of the syndicate. A ferocious 10th-Level Fighter / 8th-Level Thief who fights with dual blades and commands fanatical devotion from his survivors.</li>
  <li><strong>Inés 'La Loba' de Sotomayor:</strong> 8th-Level Assassin and Cazmiro's chief lieutenant. A cold, silent killer from the Velasco salt marshes who specializes in garrotte wire, throwing stilettos, and fatal doses of Argossean jellyfish venom.</li>
  <li><strong>Brother Tibalt the Apostate:</strong> A renegade former Nemethian monk who defected to the Velasco underworld during the purge; he provides inside intelligence on church liturgies, holy relic caches, and refugee safehouse networks in Kordova.</li>
</ul>

<h3>4. Fortified Hideouts</h3>
<ul>
  <li><strong>The Rotting Hulks of the Mudflats:</strong> Three partially grounded, decaying Argossean merchant cogs mired in the foul tidal mudflats outside the Kordova harbor boom. Connected by swaying rope-bridges, submerged rope causeways, and hidden swivel-guns, the hulks are virtually impregnable to ground assault: at high tide, the mudflats flood with 12 feet of churning sea water, cutting off all approach except by boat.</li>
  <li><strong>The Smuggler's Sea-Grotto (Cueva del Halcón):</strong> A natural tidal cavern carved into the limestone sea-cliffs beneath Kordova's western bastion. Accessible only at low tide via rowboat or through a treacherous 80-foot vertical chimney, it serves as Cazmiro's armory and council room.</li>
  <li><strong>The Salt-Fish Smokehouse:</strong> A reeking, abandoned fish-curing warehouse in the Fishermen's Ward utilized as an urban staging post and interrogation cellar.</li>
</ul>

<h3>5. Strategic Opportunities for the PC Triumvirate</h3>
<p>The arrival of the Velascan Syndicate introduces a volatile third power into Kordova's underworld:</p>
<ul>
  <li><strong>The Gang War Opportunity:</strong> The PCs can exploit the bitter feud between Don Beltrano's Night Guild and Cazmiro's Velascans, feeding intelligence to both sides to exhaust their strength and clear the city of criminal violence.</li>
  <li><strong>A Ruthless Sovereign Strike Force:</strong> Cazmiro cares nothing for Kordova's ancestral politics or Grandee etiquette. If the PCs offer the Velascans legal sanctuary, naval letters of marque, and permission to operate as the crown's private corsairs, Cazmiro will willingly assassinate corrupt Grandees, sabotage Marquis Murzio's tax barges, or raid Church of Nemeth strongholds on the crown's orders.</li>
  <li><strong>The Escalation Hazard:</strong> If left unchecked, the gang war will spill into the Merchant Quarter, triggering martial crackdowns by General Valenza that could lock down the capital entirely.</li>
</ul>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE ZEALOT MASSACRE CONSPIRACY</div>
  <p>Cazmiro is currently preparing an audacious strike: in three days, forty Velascan cutthroats armed with pitch-pots and crosscut axes will raid the sacred pilgrim hospices outside Kordova's South Gate, slaughtering the religious refugee elders and looting the silver they brought from Velasco. If this massacre occurs, <a href="#npcs/malachai" class="wiki-link">Father Malachai the Blind</a> will declare holy war against the crown, blaming the PC Triumvirate for failing to protect the faithful.</p>
</div>
""",
        "gmSecrets": "The Velasco Syndicate has stolen The Tears of Saint Moranna, an ancient relic capable of acidifying Kordova's water reservoirs. They plan a massive nocturnal raid on religious refugee camps in 3 days.",
        "relatedIds": ["casimiro-velasco", "kordovan-thieves-guild", "beltran-desoto", "joaquin", "velasco", "church-of-nemeth", "malachai", "the-pit", "court-matrix"]
    }

    # -------------------------------------------------------------
    # 6. NEW ARTICLE: velasco (Gazetteer)
    # -------------------------------------------------------------
    velasco_gazetteer_article = {
        "id": "velasco",
        "category": "gazetteer",
        "title": "Velasco (The Cleansed Port & The Sunken Pearl)",
        "subtitle": "Zingara's Southern Maritime Haven & Crucible of the Holy Refugee Revolution",
        "tags": ["Gazetteer", "Geography", "Coastal Port", "Velasco", "Church of Nemeth", "Refugees", "Period VIII"],
        "aliases": [
            "Velasco",
            "Port of Velasco",
            "The Cleansed Port",
            "The Sunken Pearl",
            "City of Velasco",
            "Velascan Coast"
        ],
        "summary": "Zingara's major southwestern maritime port, celebrated for rich vineyards, deepwater shipyards, and salt flats. Recently seized by thousands of militant religious refugees fleeing Kordova, who violently deposed the local nobility and purged the criminal underworld, transforming the port into a fortress of austere religious zealotry.",
        "content": """
<div class="info-card">
  <p><strong>Geographical Type:</strong> Coastal Deepwater Port &bull; Estuary Fortress City</p>
  <p><strong>Location:</strong> Southwestern Coast of Zingara, south of Kordova along the azure coast of the Western Sea</p>
  <p><strong>Strategic &amp; Economic Value:</strong> Deepwater shipyards, vintage wine exports, vast coastal salt evaporation pans, naval anchorage</p>
  <p><strong>Ruling Power:</strong> <em>The Council of the Pure</em> (Militant theocracy established by Kordovan religious refugees)</p>
  <p><strong>Primary Encounter Hazards:</strong> Inquisitorial zealots, public trials, martial religious patrols, displaced cutthroats</p>
</div>

<h3>1. Geographical Overview: The Sunken Pearl</h3>
<p>Situated upon a natural deepwater sound sheltered by jagged sea-stacks, <strong>Velasco</strong> was traditionally known as 'The Sunken Pearl' of Zingara. Blessed with a warmer, sunnier climate than Kordova, its surrounding hills are terraced with ancient vineyards producing the famed ruby-tinted Velascan vintage, while its shallow tidal lagoons host the kingdom's largest salt-works. Its massive stone quays were built in Period III by maritime architects, capable of berthing forty heavy Argossean trading caravels simultaneously.</p>

<p>Historically, Velasco was a decadent playground of corrupt Grandees, foreign privateers, and lavish gaming galleons. The local thieves' syndicate—<a href="#factions/velasco-thieves-guild" class="wiki-link">The Gilded Dagger</a>—operated openly, paying bribes to the governor and maintaining opulent mansions overlooking the azure bay.</p>

<h3>2. The Holy Refugee Revolution</h3>
<p>The peace of Velasco was obliterated at the close of Period VII. Following the defeat of the theocratic regime in Kordova and the subsequent Restoration Council crackdowns under <a href="#npcs/valenza" class="wiki-link">General Valenza</a>, tens of thousands of devout adherents, ascetic monks, and militant zealots of the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a> fled the capital. Carrying holy scriptures, relics, and burning grievances, this tidal wave of refugees marched south into Velasco.</p>

<p>Unlike the broken rural peasantry, the Kordovan refugees were organized into disciplined lay fraternities. Finding Velasco awash in secular vice, corrupt Grandee rule, and criminal syndicates, the refugee prophets declared the city an abomination. In a ferocious three-week uprising known as <em>The Cleansing Tide</em>, the religious refugees:</p>
<ul>
  <li>Stormed the governor's palace and executed Duke Alvaradro de Velasko on his own marble terrace.</li>
  <li>Burned the waterfront brothels, gambling galleons, and illicit distilleries to the waterline.</li>
  <li>Hunted down the indigenous criminal underworld, hanging over a hundred fences and forcing <a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro</a> and his surviving syndicate into exile.</li>
  <li>Instituted <strong>The Council of the Pure</strong>, an austere theocratic tribunal enforcing strict religious law, public penance, and mandatory tithes across the province.</li>
</ul>

<h3>3. Current State: The Fortress of Austerity</h3>
<p>Today, Velasco has ceased all luxury trade with the capital. The grand marble villas of its former nobility have been converted into ascetic monasteries, orphanages, and hospices for the pious. The city's famed shipyards are now constructing heavily armed holy galleasses, crewed by hymn-singing warrior-monks who patrol the southern coastline, seizing foreign merchant ships carrying "corrupting luxuries" and searching for fugitive criminals.</p>

<p>However, this revolution had an explosive ripple effect: the violent expulsion of Velasco's deeply entrenched thieves' guild drove sixty of the realm's deadliest cutthroats directly into Kordova, where they are currently waging a bloody turf war against <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild</a>.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; REVENUE AND EMBARGO THREAT</div>
  <p><strong>The Salt and Wine Embargo:</strong> The Council of the Pure in Velasco has officially cut off all tax remittances and salt shipments to the bankrupt crown in Kordova, declaring the PC Triumvirate to be 'impure puppets of godless warlords.' If the PCs do not either send an army to crush the theocracy or negotiate a concordat with the Council of the Pure, the capital will face a catastrophic winter salt famine, causing food stocks to rot across the lower wards.</p>
</div>

<h3>Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Salt Concordat Embassy</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> High Chancellor Marquis Murzio urges the PCs to dispatch an embassy to Velasco to demand the release of 10,000 sacks of preserved salt. However, the Council of the Pure demands a horrific concession in exchange: the Triumvirate must extradite all Velascan criminal exiles living in Kordova (including Capitán Cazmiro and his men) to be burned at the stake in Velasco's cathedral square.</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 17 Diplomacy / Theology to negotiate with the Council; DC 16 Insight to detect internal schisms among the zealot elders.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If the PCs refuse to surrender Cazmiro, the Council of the Pure launches privateer raids on Kordova's grain skiffs.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: Rescuing the Hostage Grandee</h4>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Donna Inez de Velasco, the surviving daughter of the executed governor, is being held in a secluded convent tower awaiting forced holy vows. Her loyal retainers in Kordova offer the PCs 1,000 gold pieces if they orchestrate a covert maritime extraction to smuggle her out of Velasco to the capital.</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 16 Infiltration / Lockpicking; DC 15 Stealth to navigate the torchlit patrols of warrior-monks.</div>
  <p class="escalation"><strong>Escalation Trigger:</strong> If the alarm sounds, the monastery bells ring across the sound, and four armed holy war-galleasses deploy to block the harbor mouth.</p>
</div>
""",
        "gmSecrets": "Velasco's Council of the Pure is withholding all salt and tax shipments to Kordova. They are secretly funding underground zealot cells in the capital under Father Malachai to prepare a holy coup against the Triumvirate.",
        "relatedIds": ["velasco-thieves-guild", "casimiro-velasco", "church-of-nemeth", "kordovan-thieves-guild", "malachai", "kordava", "gazetteer-matrix"]
    }

    # Add the 6 new articles to data['articles']
    new_articles = [
        joaquin_article,
        beltran_article,
        casimiro_article,
        kordovan_guild_article,
        velasco_guild_article,
        velasco_gazetteer_article
    ]

    for na in new_articles:
        # Check if already exists
        existing = next((a for a in data['articles'] if a['id'] == na['id']), None)
        if existing:
            data['articles'].remove(existing)
        data['articles'].append(na)
        print(f"Added/Updated article: {na['id']} ({na['title']})")

    # -------------------------------------------------------------
    # 7. UPDATE EXISTING ARTICLE: court-matrix
    # -------------------------------------------------------------
    court_matrix = next((a for a in data['articles'] if a['id'] == 'court-matrix'), None)
    if court_matrix:
        # Add table rows for Joachor, Beltran, Cazmiro before </tbody>
        new_matrix_rows = """
    <tr>
      <td><strong><a href="#npcs/joaquin" class="wiki-link">Joachor 'The Jackdaw' Valiento</a></strong><br><small>Down-on-His-Luck Cutpurse</small></td>
      <td><span class="badge">Night Guild / The Pit Outcasts</span></td>
      <td>Eager underworld guide; desperate for coin and protection under royal schemes.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Owes 80 gp blood tithe to Don Beltrano; knows unmapped drainage flue into High Alcázar kitchens.</span></td>
      <td><a href="#npcs/beltran-desoto" class="wiki-link">'El Macho' Corvo</a> &amp; <a href="#npcs/casimiro-velasco" class="wiki-link">Inés 'La Loba'</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano 'El Tuerto'</a></strong><br><small>Master of the Night Guild</small></td>
      <td><span class="badge">The Night Guild of Kordova</span></td>
      <td>Wary, cynical criminal patriarch; open to transaction if treated with gutter pundonor.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Possesses pre-Cataclysmic Sluice Key to palace water-gates; desperate to repel Velasco invaders.</span></td>
      <td><a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro</a> &amp; <a href="#npcs/valenza" class="wiki-link">General Valenza</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro 'The Hawk'</a></strong><br><small>War-Boss of the Velascan Exiles</small></td>
      <td><span class="badge">The Velasco Syndicate (Exiles)</span></td>
      <td>Violent, opportunistic intruder; willing to serve as crown shadow blades for legal amnesty.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Possesses acidifying chalice; plans massacre of religious refugees outside South Gate in 3 days.</span></td>
      <td><a href="#npcs/beltran-desoto" class="wiki-link">Don Beltrano de Zoto</a> &amp; <a href="#npcs/malachai" class="wiki-link">Father Malachai</a></td>
    </tr>
"""
        if '</tbody>' in court_matrix['content']:
            court_matrix['content'] = court_matrix['content'].replace('</tbody>', new_matrix_rows + '  </tbody>')
            print("Updated court-matrix with Joachor, Beltrano, and Cazmiro!")
        if 'relatedIds' in court_matrix:
            for nid in ['joaquin', 'beltran-desoto', 'casimiro-velasco']:
                if nid not in court_matrix['relatedIds']:
                    court_matrix['relatedIds'].append(nid)

    # -------------------------------------------------------------
    # 8. UPDATE EXISTING ARTICLE: state-of-the-realm
    # -------------------------------------------------------------
    state_realm = next((a for a in data['articles'] if a['id'] == 'state-of-the-realm'), None)
    if state_realm:
        # Add row to Master Crisis Quick-Reference Matrix table
        new_table_row = """    <tr>
      <td><strong>6. Underworld Gang War</strong></td>
      <td>Displaced Velasco Syndicate invading Kordova; street assassinations, refugee terror.</td>
      <td>Docks, Lower Ward &amp; The Pit</td>
      <td>Capitán Cazmiro vs. Don Beltrano / The Pit Cutpurses</td>
      <td>Choose an underworld faction to back, broker a gang truce, or purge both syndicates.</td>
    </tr>
"""
        if '</tbody>' in state_realm['content'] and '6. Underworld Gang War' not in state_realm['content']:
            state_realm['content'] = state_realm['content'].replace('</tbody>', new_table_row + '  </tbody>')

        # Add Sector 6 description before the end
        sector_6_html = """
<h4>Sector 6: Underworld Gang War &amp; The Velascan Incursion</h4>
<div class="hook-card info-card">
  <p><strong>The Strategic Crisis:</strong> The arrival of the displaced <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a>—violently expelled from the south by pious refugees from Kordova—has turned the capital's docks and <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> into a blood-soaked battleground. Displaced corsairs under <a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro</a> are assassinating lookouts of <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild</a>, hijacking river cargo, and conducting nocturnal raids against religious refugee camps outside the South Gate.</p>
  <p><strong>The Handlers' Manipulation:</strong> <a href="#npcs/valenza" class="wiki-link">General Valenza</a> is exploiting the underworld chaos to impose draconian martial law across the Lower Wards, stationing heavy caballeros at every gate and blaming the young Triumvirate for the disorder. Meanwhile, <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio</a> quietly encourages the Velascans to wipe out the Night Guild so he can seize control of the subterranean smuggling tunnels without paying kickbacks to <a href="#npcs/beltran-desoto" class="wiki-link">Don Beltrano</a>.</p>
  <p><strong>Direct Action Levers for PCs:</strong></p>
  <ul>
    <li><strong>Back the Indigenous Guild:</strong> Partner with Don Beltrano and <a href="#npcs/joaquin" class="wiki-link">Joachor Valiento</a> to crush the Velasco invaders, gaining access to the secret Sluice Key beneath the High Alcázar and securing an underground spy network.</li>
    <li><strong>Enlist the Velascan Corsairs:</strong> Legitimise Capitán Cazmiro's cutthroats with royal letters of marque, deploying them as expendable shadow assassins against corrupt Grandees and rebel agitators.</li>
    <li><strong>Purge Both Syndicates:</strong> Deploy the royal guards to conduct a coordinated raid on both the Cistern of the Blind Saint and the Mudflat Hulks, breaking the underworld's grip on Kordova once and for all.</li>
  </ul>
</div>
"""
        if 'Sector 6: Underworld Gang War' not in state_realm['content']:
            state_realm['content'] += sector_6_html
            print("Updated state-of-the-realm with Sector 6: Underworld Gang War!")
        if 'relatedIds' in state_realm:
            for fid in ['kordovan-thieves-guild', 'velasco-thieves-guild', 'joaquin', 'beltran-desoto', 'casimiro-velasco', 'velasco']:
                if fid not in state_realm['relatedIds']:
                    state_realm['relatedIds'].append(fid)

    # -------------------------------------------------------------
    # 9. UPDATE EXISTING ARTICLE: kordava & the-pit
    # -------------------------------------------------------------
    kordava_art = next((a for a in data['articles'] if a['id'] == 'kordava'), None)
    if kordava_art:
        kordava_expansion = """
<h3>The Lower Wards, Wharves &amp; The Underworld Turf War</h3>
<p>Downslope from the soaring sea-cliffs of the High Alcázar lie the sprawling, fog-drenched <strong>Lower Wards and Harbor Docks</strong> of Kordova. Here, between the fish-salting sheds, reeking tanneries, and timber wharves, the kingdom's economic paralysis is raw and suffocating. With state bankruptcy freezing official commerce, living workers displaced by <a href="#npcs/vane" class="wiki-link">Master Vane</a>'s industrial zombies, and food prices soaring, the waterfront has become a powder keg.</p>

<p>At the mouth of the great sewer outfall sits <em>The Drowned Rat</em>—a notorious subterranean dive where cutpurses, smugglers, and down-on-their-luck scoundrels like <a href="#npcs/joaquin" class="wiki-link">Joachor 'The Jackdaw' Valiento</a> congregate. The Lower Wards are currently gripped by a brutal gang war: the indigenous <a href="#factions/kordovan-thieves-guild" class="wiki-link">Night Guild of Kordova</a>, ruled by <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano de Soto</a> from deep within <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>, is fighting for its life against the ruthless <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a> under <a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro</a>—maritime cutthroats violently driven out of their southern home port by fanatical religious refugees.</p>
"""
        if 'The Lower Wards, Wharves &amp; The Underworld Turf War' not in kordava_art['content']:
            kordava_art['content'] += kordava_expansion
            print("Updated kordava article with Lower Wards and underworld details!")
        if 'relatedIds' in kordava_art:
            for xid in ['kordovan-thieves-guild', 'velasco-thieves-guild', 'joaquin', 'beltran-desoto', 'casimiro-velasco', 'velasco']:
                if xid not in kordava_art['relatedIds']:
                    kordava_art['relatedIds'].append(xid)

    the_pit_art = next((a for a in data['articles'] if a['id'] == 'the-pit'), None)
    if the_pit_art:
        pit_expansion = """
<h3>The Underworld Dens: The Cistern of the Blind Saint</h3>
<p>Deep beneath the ruined sunken palaces of The Pit, beyond the patrols of <a href="#factions/republican-insurgents" class="wiki-link">Republican Insurgents</a> and the zombie containment pits, lies the secret heart of Kordova's criminal empire: <strong>The Cistern of the Blind Saint</strong>. A colossal pre-Cataclysmic reservoir carved from black granite during Period II, this subterranean vault serves as the headquarters of <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild of Kordova</a>. From an elevated dais above the dark waters, <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano de Soto</a> administers <em>El Pundonor del Arroyo</em>, adjudicating criminal disputes, storing fenced silver, and coordinating defenses against <a href="#factions/velasco-thieves-guild" class="wiki-link">Velascan cutthroats</a> seeking to infiltrate the depths.</p>
"""
        if 'The Cistern of the Blind Saint' not in the_pit_art['content']:
            the_pit_art['content'] += pit_expansion
            print("Updated the-pit article with Cistern of the Blind Saint details!")
        if 'relatedIds' in the_pit_art:
            for xid in ['kordovan-thieves-guild', 'beltran-desoto', 'joaquin', 'velasco-thieves-guild', 'casimiro-velasco']:
                if xid not in the_pit_art['relatedIds']:
                    the_pit_art['relatedIds'].append(xid)

    # -------------------------------------------------------------
    # 10. UPDATE META
    # -------------------------------------------------------------
    data['meta']['totalArticles'] = len(data['articles'])
    data['meta']['lastUpdated'] = "2026-10-15T14:45:00.000Z"
    print(f"Total articles now: {data['meta']['totalArticles']}")

    # Write out updated js/data.js
    output_js = "window.WIKI_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(output_js)
    print("Successfully wrote updated js/data.js!")

    # -------------------------------------------------------------
    # 11. UPDATE data/sessions.json WITH SESSION 1
    # -------------------------------------------------------------
    with open('data/sessions.json', 'r', encoding='utf-8') as f:
        sessions = json.load(f)

    # Check if Session 1 already exists
    session_1_exists = any(s.get('sessionNumber') == 1 for s in sessions)
    if not session_1_exists:
        session_1 = {
            "sessionNumber": 1,
            "title": "The Thief's Bargain & The Shadows of Velasco",
            "realDate": "Session 1 Recap",
            "inGameDate": "Month of the Sun, Period VIII (Day 4 of the Triumvirate)",
            "summary": "Desperate for independent wealth to bypass High Chancellor Marquis Murzio's bankrupt treasury, the PC Triumvirate slipped in disguise into the Lower Wards of Kordova. In The Drowned Rat, a squalid dive clinging to the sewer outfall of The Pit, they met Joachor 'The Jackdaw' Valiento—a starving cutpurse crushed by the city's economic collapse and an 80-sovereign blood-tithe debt to his guildmaster. In exchange for coin and a blood-oath guarantee of being included in any future schemes, Joachor agreed to introduce the PCs to the elusive Night Guild of Kordova. Joachor revealed that an all-out underworld war is erupting: a displaced thieves' guild from the southern port of Velasco, violently expelled by the newly arrived religious refugees from Kordova, has invaded the capital to muscle in on local turf.",
            "sovereigntyPoints": 1,
            "pundonorStatus": "Unstained (Maintained incognito bearing in tavern)",
            "activeThreads": [
                "The Guild Audition: Joachor has arranged a midnight descent through the sewer sluices to the Cistern of the Blind Saint to meet Guildmaster Don Beltrano de Soto.",
                "The Velasco Incursion: Displaced maritime cutthroats under Capitán Don Cazmiro de Velasco are ambushing Kordovan lookouts and seizing dockside protection rackets.",
                "The Refugee Backlash: News arrives from the south that Kordovan religious refugees in Velasco have completely overthrown the city council, sparking panic among the Grandees.",
                "Joachor's Debt Clock: Joachor has 48 hours to pay his 80-sovereign fine to Don Beltrano before the guild breaks his fingers and sells him to Master Vane's corpse carts."
            ],
            "npcDispositions": {
                "Joachor 'The Jackdaw' Valiento": "Grateful / Bound by Oath (+1 Underworld Guide, High Debt Vulnerability)",
                "Guildmaster Don Beltrano de Soto": "Wary / Awaiting Tribute (Demands proof of royal competence)",
                "Capitán Don Cazmiro de Velasco": "Hostile / Opportunistic (Looking for weakness in Kordova)",
                "General Don Rodorigo de Valenza": "Unaware of PCs' nocturnal excursion (Stepped up curfew patrols)",
                "High Chancellor Marquis Murzio de Sadoria": "Suspicious of missing palace kitchen supplies"
            }
        }
        sessions.append(session_1)
        with open('data/sessions.json', 'w', encoding='utf-8') as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
        print("Successfully updated data/sessions.json with Session 1!")
    else:
        print("Session 1 already present in data/sessions.json.")

if __name__ == '__main__':
    build_data()
