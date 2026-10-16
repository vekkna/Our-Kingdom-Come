"""
add_university_to_wiki.py
Adds the Royal University of Kordava (campus), Dean Don Balthaso de Argoto,
university faculty & student NPCs (Maestra Valessa de Morato, Maestro Eusevios Falcon,
Doña Kostanza de Silvero), the plot hook 'The Necromancer's Endowment',
and links them across existing wiki articles, the court matrix, the crisis registry,
and data/sessions.json.
"""

import json
import sys

def main():
    print("Starting University of Kordava Wiki Expansion...")

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
    # 1. NEW GAZETTEER ARTICLE: royal-university-of-kordava
    # -------------------------------------------------------------
    university_campus = {
        "id": "royal-university-of-kordava",
        "category": "gazetteer",
        "title": "The Royal University of Kordava (La Real Academia de San Ancillus)",
        "subtitle": "The Battered Cradle of Zingaran Arcana • Ruined Halls of Philosophy, Fleshcraft & Forgotten Lore",
        "tags": ["Gazetteer", "Geography", "Kordava", "University", "Academy", "Necromancy", "Period VIII", "Arcana"],
        "aliases": [
            "The Royal University of Kordava",
            "Royal University of Kordava",
            "University of Kordava",
            "La Real Academia de San Ancillus",
            "The Ruined University",
            "The Old Academy",
            "San Ancillus Academy",
            "The University",
            "University Campus",
            "Campus of Kordava",
            "The Sunken Scriptorium",
            "Academia de San Ancillus",
            "The University of Kordava"
        ],
        "summary": "Perched precariously along Kordova's western escarpment overlooking the chasm of The Pit, the ancient university is a crumbling, battle-scarred gothic compound founded in Period II by King Ancillus I and elven scholars. Ravaged by the Restoration Civil War, stripped of crown stipends by Marquis Murzio de Sadoria, and teetering on bankruptcy, its dean and remaining faculty are eagerly preparing a radical pivot toward practical, state-sponsored necromancy if the PC Necromancer can secure funding.",
        "content": """
<div class="info-card">
  <p><strong>Geographical Type:</strong> Ancient Academic Campus &bull; Fortified Scholastic Compound &bull; Subterranean Vault System</p>
  <p><strong>Location:</strong> Upper Western Escarpment of <a href="#gazetteer/kordava" class="wiki-link">Kordava</a>, perched directly between the Old Elven Quarter and the sheer crumbling precipice overlooking <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>.</p>
  <p><strong>Strategic &amp; Arcane Value:</strong> The sole surviving center of higher scholarship in Zingara; repository of pre-Cataclysmic texts; contains subterranean amphitheaters and direct, sealed conduits descending into the buried Period III academy ruins where the <a href="#relics/black-blade" class="wiki-link">Black Blade of Azur</a> was lost.</p>
  <p><strong>Current Condition:</strong> Near-total ruin. Slate roofs shattered by civil war trebuchets, classical marble colonnades blackened by fire, libraries half-plundered or sold for firewood, laboratories lacking reagents, and faculty unpaid for eight months.</p>
  <p><strong>Rector Magnificus:</strong> <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a> (Former academic mentor to the PC Necromancer).</p>
</div>

<h3>1. Geographical &amp; Architectural Overview</h3>
<p>Rising like a weathered granite fortress above the smog, sewage fumes, and shrieks of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>, <strong>The Royal University of Kordava</strong>—known historically as <em>La Real Academia de San Ancillus</em>—is one of the oldest contiguous structures in the Hyborian world. Founded during <a href="#history/period-ii" class="wiki-link">Period II: The Time of the Elves</a> by <a href="#history/ancillus-i" class="wiki-link">King Ancillus I</a> and seafaring elven philosophers, the campus was designed to synthesize high elven mathematics and arcane disciplines with Zingaran natural philosophy.</p>

<p>Today, the university presents a haunting spectacle of tragic neglect and gothic decadence. Its soaring elven arches, fluted white marble porticos, and traceried cloisters are choked with moss, ivy, and soot. During <a href="#history/period-vii" class="wiki-link">Period VII: Restoration Civil War</a>, the campus was seized as a fortified artillery redoubt by monarchist forces, subjecting its lecture halls and dormitories to brutal catapult barrages, street fighting, and sorcerous fires. When the unquiet dead of King Ancillus I rampaged through Kordova, the western courtyards became a slaughterhouse.</p>

<p>Following the wars, <a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio de Sadoria</a> classified higher education as an &ldquo;unproductive luxury,&rdquo; canceling all royal endowments to service foreign debt covenants with the <a href="#gazetteer/kingdom-of-argos" class="wiki-link">Kingdom of Argos</a>. Windows are shuttered with rotted cedar planks, rain drips rhythmically into pewter buckets in drafty lecture halls, and impoverished professors boil scrap leather and wild thistles for dinner. Yet beneath this destitute facade, an electrifying intellectual renaissance is stirring: the Dean and surviving faculty have embraced the PC Necromancer's visit as a divine opportunity to reinvent the university as the preeminent <strong>College of Applied Thanatology &amp; Deathless Industry</strong>.</p>

<h3>2. Key Campus Facilities &amp; Sub-Locations</h3>
<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Facility / Sector</th>
      <th>Architectural State</th>
      <th>Current Purpose &amp; Activities</th>
      <th>Key Hazards / Secrets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>The Great Quadrangle of Ancillus (El Patio de los Sabios)</strong></td>
      <td>Crumbling fluted marble colonnade; cracked flagstones overgrown with wolfsbane, nightshade, and wild poppies; headless statues of elven sages.</td>
      <td>Central assembly yard where surviving students (barely fourteen remain) debate philosophy, practice blade forms, and trade scavenged food.</td>
      <td>Loose stonework (DC 13 DEX check or 1d6 falling masonry); undercover spies from <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a> watch the gates.</td>
    </tr>
    <tr>
      <td><strong>The Spire of Printius (The Leaning Observatory)</strong></td>
      <td>An octagonal, five-story granite tower with an alarming 4-degree lean toward the precipice of The Pit.</td>
      <td>Houses the private study, bedchamber, and alchemical alembics of <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a>. Upper dome holds a cracked brass armillary sphere and telescope.</td>
      <td>Shaky structural integrity; secret trapdoor behind the Dean's bookcase opens onto a dizzying vertical shaft descending into the foundations.</td>
    </tr>
    <tr>
      <td><strong>The Great Amphitheatre of Anatomia &amp; Fleshcraft</strong></td>
      <td>Steep, tiered auditorium of dark polished Spanish cedar with tiered brass candle-sconces and a circular zinc dissecting table equipped with blood-sluices.</td>
      <td>Presided over by <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valessa de Morato</a>. Lectures in reanimation physics, tendon-suturing, and galvanic fluid injection take place by tallow candle.</td>
      <td>Pungent vapors of vitriol, formaldehyde, and brimstone (DC 12 CON save to avoid coughing spasms); zinc table is enchanted with permanent preservation runes.</td>
    </tr>
    <tr>
      <td><strong>The Sunken Scriptorium &amp; Chained Vaults</strong></td>
      <td>Four subterranean levels descending beneath the water table; vaulted stone ribs dripping with condensation and black cellar-mold.</td>
      <td>Guarded by <a href="#npcs/eusebio-falcon" class="wiki-link">Maestro Eusevios Falkor</a> and three animated skeletal copyists. Preserves waterlogged folios of <a href="#history/printius" class="wiki-link">Printius</a> and <a href="#history/edmund" class="wiki-link">Edmund</a>.</td>
      <td>Flooded knee-deep corridors; rotted floor grates over bottomless abysses; secret submerged passage leading to <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild's</a> cisterns.</td>
    </tr>
    <tr>
      <td><strong>The Zombie Paddock &amp; Proving Crypts</strong></td>
      <td>Former botanical glasshouses and winter orangeries, their shattered panes replaced with heavy wrought-iron salvage bars and oak braces.</td>
      <td>Currently holds six experimental labor thralls, a stitched quadruped flesh-hound, and several articulated skeletal porters undergoing stability testing.</td>
      <td>Rogue reanimation shockwaves; thralls retain fragmented living memories and occasionally whisper mournful warnings to visitors through the bars.</td>
    </tr>
  </tbody>
</table>
</div>

<h3>3. The New Necromantic Direction</h3>
<p>Rather than lamenting the demise of esoteric elven poetry and astronomical theology, Dean Argoto and the faculty view necromancy as the supreme synthesis of Zingaran engineering, biology, and economic salvation. Their vision for the university includes:</p>
<ul>
  <li><strong>The Department of Labor Fleshcraft:</strong> Training state engineers to construct stable, memory-retaining labor thralls capable of deep-vein mining, quarrying, and sewer clearing without suffering necrotic collapse.</li>
  <li><strong>The Chair of Military Thanatology:</strong> Developing specialized shock-troops—shield-bearing skeletal phalanges, unyielding rampart guards, and immune siege laborers—to defend the crown against <a href="#factions/barachan-pirates" class="wiki-link">Barachan corsairs</a> and <a href="#gazetteer/pictish-wilderness" class="wiki-link">Pictish raiders</a>.</li>
  <li><strong>The Sunken Excavation Project:</strong> Clearing the subterranean rubble beneath the Sunken Scriptorium to breach the lost Period III academy ruins, unearthing ancient elven spell-matrices and hunting for the lost <a href="#relics/black-blade" class="wiki-link">Black Blade of Azur</a>.</li>
  <li><strong>State Necromantic Certification:</strong> Establishing the university as the crown's official licensing authority for necromancers, directly challenging <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane's</a> monopoly over the state zombie pits.</li>
</ul>

<div class="gm-callout">
<div class="gm-badge">GM CONFIDENTIAL &bull; THE UNDERGROUND ROAD</div>
<p>Beneath the lowest vault of the Sunken Scriptorium lies <strong>The Iron Sluice of Edmund</strong>—a heavy bronze floodgate sealed since <a href="#history/period-iv" class="wiki-link">Period IV</a>. Beyond this gate lies an ancient aqueduct leading directly into the sunken ruins of the Period III academy far below <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>. If the university receives funding and excavation begins, the workers will inevitably breach forgotten crypts containing pristine pre-Cataclysmic elven relics, guardian stone golems, and ancient slumbering undead from the original earthquake.</p>
</div>
""",
        "gmSecrets": "Chancellor Sadoria has already drawn up secret contracts with merchant syndicates from Messantia to demolish the university's southern cloisters and convert them into private bonded warehouses unless the back taxes (1,200 silver pieces) are paid by the turn of the moon. Master Vane has placed a paid informant among the student body (Apprentice Tiago) to report on any dangerous reanimation breakthroughs.",
        "relatedIds": [
            "kordava",
            "the-pit",
            "dean-baltasar-argote",
            "valeria-morata",
            "eusebio-falcon",
            "constanza-silva",
            "hook-the-necromancers-endowment",
            "vane",
            "escovedo",
            "sadoria",
            "necromancy-mechanics",
            "black-blade"
        ]
    }

    # -------------------------------------------------------------
    # 2. NEW NPC ARTICLE: dean-baltasar-argote
    # -------------------------------------------------------------
    dean_article = {
        "id": "dean-baltasar-argote",
        "category": "npcs",
        "title": "Dean Don Balthaso de Argoto",
        "subtitle": "Rector Magnificus of the Royal University of Kordava • Chair of Thanatological Philosophy",
        "tags": ["Royal Court", "NPC", "Magic-User", "Scholar", "University", "Necromancy", "Period VIII", "Academic", "Kordava"],
        "aliases": [
            "Dean Balthaso de Argoto",
            "Dean Argoto",
            "Don Balthaso de Argoto",
            "Dean Balthaso",
            "Rector Magnificus",
            "The Dean",
            "Balthaso de Argoto",
            "The Necromantic Dean",
            "Argote",
            "Dean of the University",
            "The Rector"
        ],
        "summary": "The flamboyant, silver-haired Rector Magnificus of the Royal University of Kordava and former academic mentor to the PC Necromancer. An unapologetic visionary who considers necromancy the ultimate triumph of natural philosophy, he is eager to transform his bankrupt, war-battered institution into a world-class necromantic academy—if his royal former student can secure 500 gold sovereigns in funding.",
        "atAGlance": {
            "appearance": "A tall, gaunt scholar of sixty-two with an untamed shock of silver hair, ink-stained fingers, and pale green eyes magnified behind thick circular brass-framed lenses. Wears a frayed, moth-eaten academic robe of indigo velvet trimmed with tarnished silver bullion and black bone lace, over which he drapes a stole fashioned from cured vellum inscribed with necromantic axioms.",
            "mannerisms": "Gestures sweeping flourishes with an ivory-and-brass pointing wand; absentmindedly taps human skulls on his desk as if adjusting notes on a lute; lapses into theatrical philosophical lectures with booming dramatic cadence; brews black bitter tea in an alchemical crucible over an open spirit burner.",
            "quote": "Morality, my brilliant young Sovereign, is the meager invention of priests who fear the dark because they lack the wit to kindle a candle! What is a corpse but an unstrung lute, waiting for the master's touch to sing once more? Master Vane boils dead peasants in iron grease to dig trenches; we, my friend, shall teach the dead to think, to build, to conquer! Give me five hundred gold sovereigns to mend our roofs and refill our retorts, and I shall forge you an empire that laughs in the face of the grave!",
            "courtDCs": "Morale: 8 (Fiercely obstinate scholar); Initial Reaction: Enthusiastic (+3 on 2d6 Reaction Rolls when meeting the PC Necromancer). DC 14 Diplomacy to negotiate royal terms or student tithes; DC 16 Arcana check to debate cutting-edge memory-retention theory; DC 12 Insight to perceive that behind his grandiose rhetoric lies terror of having his life's work auctioned off by Chancellor Sadoria.",
            "publicStance": "Presents himself as a traditional humanist academician defending ancient intellectual liberties against the philistinism of the Restoration Council.",
            "secretAgenda": "Desperately seeks to dig beneath the Sunken Scriptorium to uncover Printius's lost *Original Grimoire of the Reanimated Flesh*, which he believes contains the forgotten formula for granting undead true self-repair and spellcasting memory. Despises Master Vane as an illiterate mechanical butcher and dreams of displacing him as Chief Royal Sorcerer.",
            "rival": "Master Alchemist Vane (Ideological & Arcane Rival) & High Chancellor Marquis Murzio de Sadoria (Fiscal Executioner)",
            "classLevel": "11th-Level Magic-User (Academic Savant & Master Thanatologist)",
            "combatStats": "AC 6 (AAC 13) | HP 34 | THAC0 16 | Atk +5 (1d6+2 + Chill) | Spells up to 6th | Saves: 11/9/8/9/9"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Royal University of Kordava &bull; Rector Magnificus</span>
    <span class="badge rival-badge">Rivals: Master Alchemist Vane &amp; Marquis Murzio de Sadoria</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A tall, eccentric academic of sixty-two with gaunt, theatrical cheekbones, a mane of untamed silver hair, and piercing pale eyes behind circular green-tinted reading spectacles. He wears a frayed doctoral gown of faded indigo velvet with patched sleeves, hemmed in tarnished silver thread and black bone beads. He smells richly of cedar sawdust, dried lavender, pipe tobacco, and alchemical embalming fluid.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Speaks in torrents of resonant, oratorical eloquence punctuated by Latin maxims and sweeping gestures with a jointed ivory pointer; habitually polishes human skulls on his mahogany desk with his velvet sleeve; pours steaming tea from an alchemical retort into cracked porcelain teacups; treats the PC Necromancer with paternal affection and awed royal respect.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;Morality, my brilliant young Sovereign, is the meager invention of priests who fear the dark because they lack the wit to kindle a candle! What is a corpse but an unstrung lute, waiting for the master's touch to sing once more? Master Vane boils dead peasants in iron grease to dig trenches; we, my friend, shall teach the dead to think, to build, to conquer! Give me five hundred gold sovereigns to mend our roofs and refill our retorts, and I shall forge you an empire that laughs in the face of the grave!&rdquo;</div>
    <div class="glance-item dcs"><strong>Court Reaction &amp; Morale:</strong> Morale: 8 (Unshakeable intellectual conviction); Initial Reaction: +3 on 2d6 Reaction Rolls when addressing the PC Necromancer (Devoted Academic Mentor). DC 14 Diplomacy to secure honorary university appointments or specialized research thralls; DC 16 Arcana check to co-develop advanced reanimation rites; DC 12 Insight to sense his panic over looming eviction.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Dean Don Balthaso de Argoto</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Rector Magnificus &bull; Chair of Thanatological Philosophy &bull; Chaotic Neutral (Devotion to knowledge, ethical indifference to taboos, passionate mentor)</div>
    </div>
    <span class="stat-class-level">⚔️ 11th-Level Magic-User (Master Thanatologist)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 6 (AAC 13) <small class="text-dim">(Mantle of Bone-Weave +2, Ring of Protection +1, DEX 11)</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 11d4+11 (+11 CON bonus) &bull; <span style="color: #2ecc71; font-weight: 700;">34 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 16 (Base Attack Bonus +4)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +5 to hit (<em>"The Rod of Ancillus"</em> +2 ivory-and-brass scepter, 1d6+2 bludgeoning plus necrotic chill; on hit, target must succeed on DC 14 Save vs. Spells or suffer -2 STR for 1 turn); Ranged: +4 to hit (Dagger of Silvered Bone +1, 1d4+1 piercing)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box">
      <div class="stat-ability-label">STR</div>
      <div class="stat-ability-score">10</div>
      <div class="stat-ability-mod">Normal (0)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">DEX</div>
      <div class="stat-ability-score">12</div>
      <div class="stat-ability-mod">Normal (0)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">+1 HP per Hit Die</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">18</div>
      <div class="stat-ability-mod">+3 Spells / Savant (+3 on Arcana / Research)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">11</div>
      <div class="stat-ability-mod">Normal (0)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 Reaction Modifier</div>
    </div>
  </div>

  <div class="stat-section-title">Saving Throws (11th-Level Magic-User)</div>
  <div class="stat-saves-bar">
    <div class="stat-save-item"><strong>Breath Attacks:</strong> 11</div>
    <div class="stat-save-item"><strong>Poison or Death:</strong> 9</div>
    <div class="stat-save-item"><strong>Petrify or Paralyze:</strong> 8</div>
    <div class="stat-save-item"><strong>Wands:</strong> 9</div>
    <div class="stat-save-item"><strong>Spells or Rods:</strong> 9</div>
  </div>

  <div class="stat-section-title">Prepared Spells (4 / 4 / 4 / 3 / 3 / 1)</div>
  <div style="font-size: 0.88rem; line-height: 1.5; color: var(--text-main); margin-top: 6px;">
    <strong>1st Level:</strong> <em>Shield, Read Magic, Hold Portal, Detect Magic</em><br>
    <strong>2nd Level:</strong> <em>Invisibility, Mirror Image, Web, Locate Object</em><br>
    <strong>3rd Level:</strong> <em>Animate Dead (Mastery variant: raises 2 HD per caster level), Dispel Magic, Hold Person, Clairvoyance</em><br>
    <strong>4th Level:</strong> <em>Dimension Door, Wall of Ice, Arcane Eye</em><br>
    <strong>5th Level:</strong> <em>Cloudkill, Feeblemind, Telekinesis</em><br>
    <strong>6th Level:</strong> <em>Death Spell (or Disintegrate)</em>
  </div>
</div>

<h3>4. Narrative Role &amp; The Academic Relationship</h3>
<p>Dean Balthaso taught the PC Necromancer during the tumultuous years preceding the <a href="#history/period-vii" class="wiki-link">Restoration Civil War</a>. While the rest of the faculty cowered before conservative church inquiries or fled the country, Dean Argoto secretly provided the young PC with forbidden grimoires, access to the Chained Vaults, and fresh cadavers from the city morgue. He regarded the PC as the sharpest arcane prodigy to walk the cloistered halls of Ancillus in four generations.</p>

<p>When the PC entered the Dean's study in the Leaning Spire, Argote did not kneel as a frightened subject—he embraced the PC like a long-lost son and fellow philosopher. Over lukewarm lapsang souchong tea, he laid bare the university's harrowing plight: <a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio de Sadoria</a> has seized the university's rent rolls, issued a final eviction notice for 1,200 silver pieces in back taxes, and threatened to demolish the western cloisters to make way for military grain warehouses.</p>

<p>Rather than pleading for charity, the Dean proposes a partnership of epochal proportions: grant the university <strong>500 gold sovereigns</strong> in immediate reconstruction funding, issue a <strong>Royal Sovereign Charter of Thanatological Sciences</strong>, and designate the academy as the crown's premier research engine. In return, Dean Argoto will grant the PC the title of <strong>Grand Chancellor of the Arcane Faculty</strong>, give the Triumvirate exclusive access to all newly raised specialized thrall variants, and begin the subterranean excavation of the buried Period III academy ruins.</p>

<h3>5. Levers of Influence, Secrets &amp; Betrayal Triggers</h3>
<ul>
  <li><strong>The Bitter Feud with Master Vane:</strong> Dean Argoto despises <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a> with venomous passion. He views Vane as a commercial mercenary who ruined the reputation of Zingaran necromancy by churning out rotting, dumb laborers in open cesspools. Argote will readily provide the PCs with alchemical counter-agents to disrupt Vane's industrial pits or expose Vane's embezzlement of state corpse budgets.</li>
  <li><strong>The Printius Grimoire:</strong> Argote knows that buried eighty feet beneath the campus lies the intact sanctum of Printius, untouched since the earthquake of <a href="#history/period-iii" class="wiki-link">Period III</a>. He believes the sanctum holds the legendary <em>Black Blade of Azur</em>—or the exact maps leading to it.</li>
  <li><strong>Financial Desperation:</strong> If the PCs refuse funding or mock his offer, the Dean will be forced to entertain desperate overtures from <a href="#factions/kordovan-thieves-guild" class="wiki-link">Don Beltrano de Zoto</a> of the Night Guild (who wants to use the campus as a fortress and smuggling warehouse) or even the <a href="#factions/foreign-powers" class="wiki-link">Kingdom of Argos</a>, who offered to buy the university's antique library for shipment to Messantia.</li>
</ul>
""",
        "gmSecrets": "Dean Argoto has secretly kept the reanimated corpse of his former predecessor, Dean Don Ramonzo de Corderor, locked in a lead-lined trunk in his bedchamber. The old rector retains full memories of the Period VI church persecutions and knows the secret password to unseal the iron floodgates beneath the Sunken Scriptorium.",
        "relatedIds": [
            "royal-university-of-kordava",
            "valeria-morata",
            "eusebio-falcon",
            "constanza-silva",
            "hook-the-necromancers-endowment",
            "vane",
            "sadoria",
            "escovedo",
            "kordava",
            "the-pit",
            "necromancy-mechanics"
        ]
    }

    # -------------------------------------------------------------
    # 3. NEW NPC ARTICLE: valeria-morata
    # -------------------------------------------------------------
    valeria_article = {
        "id": "valeria-morata",
        "category": "npcs",
        "title": "Maestra Valessa de Morato",
        "subtitle": "Chief Anatomist & Mistress of Suturecraft • Royal University of Kordava",
        "tags": ["NPC", "Anatomist", "Fleshcrafter", "University", "Period VIII", "Scholar", "Medicine"],
        "aliases": [
            "Maestra Valessa de Morato",
            "Valessa de Morato",
            "Maestra Valessa",
            "The Fleshcrafter",
            "Valessa Morato",
            "The Needle of Kordava",
            "The Anatomist",
            "Mistress Valessa"
        ],
        "summary": "A sharp-witted, thirty-four-year-old former battlefield surgeon turned academic reanimation artisan. Presiding over the Great Amphitheatre of Anatomia, she is a pragmatic genius of muscle-grafting, organ stabilization, and galvanic preservation who considers the living body a flawed draft and the reanimated thrall a polished final edition.",
        "atAGlance": {
            "appearance": "A slender, hawk-eyed woman of thirty-four with sharp features, dark hair coiled tightly in a brass net, and sleeves rolled past her elbows. Wears a stiffened cuirass-apron of boiled bull-hide stained with iodine, copper acetate, and dried arterial rust. Custom brass rings shaped like curved suture-needles adorn her right fingers.",
            "mannerisms": "Continuously flexes her long, dexterous surgeon's fingers; cleans fingernails with an ivory-handled lancet during conversations; speaks in brisk, clipped, surgical sentences without academic fluff; inspects physical wounds or posture of guests with unsettling clinical interest.",
            "quote": "The living are fragile, sentimental, and constantly leaking fluids. A muscle severed in battle rots in three days; an embalmed tendon spliced to seasoned sinew endures for three hundred years. Give me clean zinc, twenty carboys of lead-sugar brine, and fresh cadavers from the lower wards, and I will craft thralls that do not decay in your royal mines.",
            "courtDCs": "Morale: 8 (Hardened battlefield surgeon); Initial Reaction: Neutral (0 on 2d6; deeply cynical about politicians). DC 14 Medicine / Arcana to earn her professional respect; DC 15 Charisma to convince her the Triumvirate has the stomach for real fleshcraft; DC 16 Sleight of Hand to spot her secret anatomical notebook tucked into her corset.",
            "publicStance": "Presents herself as a detached natural anatomist providing instruction in emergency surgical trauma and embalming to surviving medical apprentices.",
            "secretAgenda": "Operates a clandestine cadaver supply ring with the Night Guild of Kordova, paying cutpurses two silver reals for unclaimed bodies washed up from the harbor. She longs for royal authorization so she no longer has to hide her dissecting vats from the city watch.",
            "rival": "Dr. Horasto Escovador (Professional Rivalry over toxicology & humors) & Master Alchemist Vane (Contempt for his crude pit slurry)",
            "classLevel": "7th-Level Specialist / Anatomist (Fleshcraft Artisan)",
            "combatStats": "AC 4 (AAC 15) | HP 26 | THAC0 17 | Atk +6 (1d4+2 + Nerve Paralysis) | Saves: 12/12/11/14/12"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Royal University of Kordava &bull; Faculty of Anatomia</span>
    <span class="badge rival-badge">Rivals: Dr. Horasto Escovador &amp; Master Alchemist Vane</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A sharp-featured, thirty-four-year-old woman with pale olive skin, severe dark eyes, and raven hair bound tightly in a woven brass hairnet. She wears an oil-rubbed leather work apron over dark woolen skirts, with high-cuffed calfskin gloves. Her fingers are adorned with specialized silver thimbles and curved surgical needle-rings.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Speaks with brisk, razor-sharp precision; perpetually turns a polished silver scalpel between her fingers; assesses the physical posture and muscle tone of interlocutors as if calculating carcass yield; never blinks during uncomfortable silences.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;The living are fragile, sentimental, and constantly leaking fluids. A muscle severed in battle rots in three days; an embalmed tendon spliced to seasoned sinew endures for three hundred years. Give me clean zinc, twenty carboys of lead-sugar brine, and fresh cadavers from the lower wards, and I will craft thralls that do not decay in your royal mines.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 8 (Ice-nerved war surgeon); Initial Reaction: Neutral (0 on 2d6; distrusts politicians and nobility). DC 14 Medicine or Arcana check to impress her with technical anatomical knowledge; DC 16 Insight to detect her secret trade with underworld grave-robbers.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Maestra Valessa de Morato</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Chief Anatomist &bull; Mistress of Suturecraft &bull; True Neutral (Pragmatic science, anatomical perfection, anti-sentimental efficiency)</div>
    </div>
    <span class="stat-class-level">⚔️ 7th-Level Specialist (Anatomist / Fleshcrafter)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 4 (AAC 15) <small class="text-dim">(Hardened Leather Apron AC 7, DEX 17 (-3))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 7d6 (+7 CON bonus) &bull; <span style="color: #2ecc71; font-weight: 700;">26 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 17 (Base Attack Bonus +3)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +6 to hit (Dual silver surgical scalpels, 1d4+2 slashing; on hit, target must succeed on DC 13 Save vs. Poison or suffer localized muscle paralysis inflicting -2 on attack rolls and DEX checks for 3 rounds); Ranged: +6 to hit (Weighted surgical needles, 1d3+1, range 20')</div>
  </div>

  <div class="stat-section-title">Anatomical Mastery &amp; Fleshcraft Special Abilities</div>
  <div style="font-size: 0.88rem; line-height: 1.5; color: var(--text-main); margin-top: 6px;">
    <strong>Preservative Embalming:</strong> Undead raised or treated under Valessa's supervision do not rot, produce no odor, and gain +2 HP per Hit Die.<br>
    <strong>Suture-Grafting:</strong> Can repair damaged thralls during a short rest, restoring 2d8 hit points per corpse using needlecraft and alchemical pitch.<br>
    <strong>Surgical Precision:</strong> Scores a critical strike on natural 19-20 when using light piercing or slashing weapons against humanoids.
  </div>
</div>

<h3>4. Background &amp; Court Web Connections</h3>
<p>Valessa served three brutal campaigns as senior field surgeon with General Valenza's artillery trains during the civil war. She witnessed hundreds of young recruits bleed out in muddy trenches while incompetent court physicians like <a href="#npcs/escovedo" class="wiki-link">Dr. Horasto Escovador</a> recommended bloodletting and herbal teas. Disgusted by the limitations of mortal flesh, she accepted Dean Argoto's invitation to head the university's anatomical theater, determined to master the mechanics of eternal physical restoration.</p>

<p>Her relationship with <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a> is pure contempt. She views his industrial zombie pits as bio-hazardous butcheries that waste valuable corpses through rapid bacterial gangrene. If backed by the PCs, Valessa can establish an elite <em>Royal Fleshcraft Atelier</em> capable of producing clean, articulate, and non-decomposing servant thralls suitable for royal palaces and military engineering.</p>
""",
        "gmSecrets": "Valessa's younger brother, Tiago de Morata, is currently an unbonded clerk in Chancellor Sadoria's treasury offices. She uses him to leak confidential state budget memos to Dean Argoto. If Tiago is ever caught or threatened with The Pit, Valessa will do anything—including assassinating a court official with untraceable nerve venom—to protect him.",
        "relatedIds": [
            "royal-university-of-kordava",
            "dean-baltasar-argote",
            "eusebio-falcon",
            "constanza-silva",
            "escovedo",
            "vane",
            "kordovan-thieves-guild",
            "hook-the-necromancers-endowment"
        ]
    }

    # -------------------------------------------------------------
    # 4. NEW NPC ARTICLE: eusebio-falcon
    # -------------------------------------------------------------
    eusebio_article = {
        "id": "eusebio-falcon",
        "category": "npcs",
        "title": "Maestro Eusevios 'The Scribe' Falkor",
        "subtitle": "Grand Archivist & Paleographer • The Sunken Scriptorium of Ancillus",
        "tags": ["NPC", "Scholar", "Archivist", "Librarian", "University", "Period VIII", "Arcana"],
        "aliases": [
            "Maestro Eusevios Falkor",
            "Eusevios Falkor",
            "Maestro Eusevios",
            "The Scribe",
            "Archivist Falkor",
            "Eusevios the Scribe",
            "Old Eusevios",
            "The Blind Scribe"
        ],
        "summary": "A frail, seventy-year-old paleographer who has spent forty-five years living in the damp, subterranean vaults of the Sunken Scriptorium. Aided by three obedient skeletal scribes, he dedicates his remaining days to copying and preserving rotting pre-Cataclysmic grimoires from water damage and church inquisitors.",
        "atAGlance": {
            "appearance": "A stooped, frail old man with squinting watery gray eyes, a wispy beard yellowed by tallow smoke, and ink-stained knuckles calloused from sixty years of quillwork. He wears a heavy woolen cowl patched with sailcloth to fend off cellar damp, a pair of cracked horn spectacles tied with leather cords, and fingerless wool gloves.",
            "mannerisms": "Speaks in a fragile, dry whisper resembling rustling leaves; constantly sniffs dried ink cakes; absentmindedly corrects the grammar of courtiers; lovingly pats his three skeletal assistants on their skulls while they transcribe manuscripts.",
            "quote": "Ink outlasts empires, young monarchs, but damp conquers even ink. When the soldiers of the Church smashed our stained glass, they left our books to drown in cellar water. Three hundred scrolls of Period II elven calculus have already turned to black moss. Give me dry parchment, lamp oil, and two carboys of gall-nut ink, and I will restore to you the lost wisdom of your ancestors.",
            "courtDCs": "Morale: 5 (Frail scholar); Initial Reaction: Warm (+1 on 2d6; treats anyone holding a book with reverence). DC 14 History / Arcana to decipher ancient scripts; DC 16 Perception to locate hidden grimoires behind false cellar flagstones; DC 12 Charisma to win his unreserved cooperation.",
            "publicStance": "Presents himself as a harmless, half-blind relic of the old regime who merely catalogs damp law codes and theological tracts.",
            "secretAgenda": "Has secretly transcribed and hidden surviving fragments of Printius's forbidden work *De Animarum Catenis* ('On the Chaining of Souls'). He seeks someone worthy to finish translating its chapter on breaking the bonds of the Obsidian Blade.",
            "rival": "Father Malachai the Blind (Theological Book-Burner) & Vesper the Key-Master (Who denied him palace library access)",
            "classLevel": "6th-Level Magic-User / Paleographer",
            "combatStats": "AC 9 (AAC 10) | HP 16 | THAC0 19 | Atk +1 (1d4 cane dagger) | Saves: 13/11/11/11/12"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Royal University of Kordava &bull; The Sunken Scriptorium</span>
    <span class="badge rival-badge">Primary Rivals: Father Malachai the Blind &amp; Vesper the Key-Master</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A stooped, seventy-year-old scholar clad in a salt-stained, hooded monastic habit lined with mangy rabbit fur against the cellar cold. He peers through round horn spectacles perched on a red, perpetually dripping nose. His long, spidery fingers are permanently blackened with gall-nut ink and lampblack.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Speaks in an intimate, parchment-dry whisper; constantly polishes a magnifying crystal with his hem; gently chides his three skeletal scribes (*&ldquo;Hush, Murzio, do not smudge the margin with your phalange&rdquo;*); shuffles along damp vaults without a lantern, navigating purely by touch and smell.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;Ink outlasts empires, young monarchs, but damp conquers even ink. When the soldiers of the Church smashed our stained glass, they left our books to drown in cellar water. Three hundred scrolls of Period II elven calculus have already turned to black moss. Give me dry parchment, lamp oil, and two carboys of gall-nut ink, and I will restore to you the lost wisdom of your ancestors.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 5 (Physically helpless, morally iron-willed); Initial Reaction: +1 on 2d6 (+3 if gifted dry parchment or ancient manuscripts). DC 14 History or Arcana check to identify rare eldritch codices; DC 16 Investigation to uncover his hidden waterproof scroll-chests.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Maestro Eusevios 'The Scribe' Falkor</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Grand Archivist &bull; Paleographer of the Scriptorium &bull; Neutral Good (Preservation of truth, historical loyalty to the House of Ancillus)</div>
    </div>
    <span class="stat-class-level">⚔️ 6th-Level Magic-User (Paleographer &amp; Cryptographer)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 9 (AAC 10) <small class="text-dim">(Heavy Woolen Cowl, DEX 8 (-1 AC))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 6d4 (+0 CON) &bull; <span style="color: #2ecc71; font-weight: 700;">16 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 90' (30')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 19 (Base Attack Bonus +2)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +1 to hit (Iron-shod oak cane with concealed 1d4 silver needle-blade)</div>
  </div>

  <div class="stat-section-title">Paleographical Special Abilities &amp; Retinue</div>
  <div style="font-size: 0.88rem; line-height: 1.5; color: var(--text-main); margin-top: 6px;">
    <strong>The Scriptorium Triumvirate (Skeletal Scribes):</strong> Accompanied everywhere by three ancient human skeletons named <em>Lucas, Murzio, and Juan</em>. Each wears an ink-stained scholar's scapular and possesses flawless calligraphic skill. They copy manuscripts 24 hours a day, produce no noise, and defend Eusevios with heavy oak book-press clamps (1d6 bludgeoning) if he is physically attacked.<br>
    <strong>Polyglot Decipherment:</strong> Automatically reads any pre-Cataclysmic script, elven rune-matrix, or ciphered text on a successful DC 12 Intelligence check.<br>
    <strong>Spells Prepared (3 / 2 / 2):</strong> <em>Comprehend Languages, Erase, Read Magic; Continual Light, Locate Object; Dispel Magic, Secret Page</em>.
  </div>
</div>

<h3>4. Role in the Kingdom &amp; The Black Blade Legend</h3>
<p>Old Eusevios is the living institutional memory of the university. During the dark reign of the Church of Nemeth, Eusevios walled himself into the sub-basement with two wheelbarrows of salted fish and six hundred irreplaceable books, emerging only when the inquisitors were overthrown. He possesses an authentic map drawn in Period IV by Edmund himself, marking the fault line where the original Period III academy collapsed into the subterranean abyss.</p>

<p>According to Eusevios's research, the mythical <a href="#relics/black-blade" class="wiki-link">Black Blade of Azur</a> did not dissolve in the earth—it remains lodged within the crystallized heart of the ancient elven lecture vault directly beneath the Sunken Scriptorium. If the PC Necromancer finances the pumping of the flooded cellar levels, Eusevios can guide them directly to the threshold of the lost vaults.</p>
""",
        "gmSecrets": "Eusevios suffers from advancing pulmonary consumption from decades of breathing damp cellar mold. He knows he has less than six months to live unless treated by the waters of the Fountain of Youth or receiving specialized necromantic life-extension. He will trade his most dangerous secret—the location of the Black Blade map—in exchange for an oath from the PC Necromancer that the Scriptorium will be permanently endowed.",
        "relatedIds": [
            "royal-university-of-kordava",
            "dean-baltasar-argote",
            "valeria-morata",
            "constanza-silva",
            "black-blade",
            "printius",
            "edmund",
            "hook-the-necromancers-endowment"
        ]
    }

    # -------------------------------------------------------------
    # 5. NEW NPC ARTICLE: constanza-silva
    # -------------------------------------------------------------
    constanza_article = {
        "id": "constanza-silva",
        "category": "npcs",
        "title": "Doña Kostanza de Silvero",
        "subtitle": "Student Bursar & Pyrotechnic Alchemist • The Dispossessed Gentry",
        "tags": ["NPC", "Student", "Alchemist", "University", "Period VIII", "Revolutionary", "Magic-User"],
        "aliases": [
            "Doña Kostanza de Silvero",
            "Kostanza de Silvero",
            "Kostanza",
            "Student Bursar Kostanza",
            "The Lady Alchemist",
            "Kostanza the Bursar"
        ],
        "summary": "A fierce, brilliant nineteen-year-old noblewoman whose family estates in the Zingg Valley were unlawfully confiscated by Duke Gonzalgo de Guarralid after her father fell in the civil war. Disguised as a common scholar, she manages the university's bankrupt ledgers while synthesizing volatile corpse-fuel and rallying the remaining students behind the Triumvirate.",
        "atAGlance": {
            "appearance": "A fiery-eyed young woman of nineteen with sun-bronzed skin, high aristocratic cheekbones smudged with charcoal and sulfur, and soot-singed honey-brown hair pinned back with iron laboratory needles. She wears a stained coarse-linen student smock over worn leather breeches and riding boots, with a bandolier of glass vials and brass measuring calipers across her chest.",
            "mannerisms": "Rolls an unstoppered glass vial of volatile phosphorus between her palms when thinking; calculates fiscal sums aloud in rapid Zingaran arithmetics; bites her lower lip when furious; maintains a proud, defiant posture that betrays her noble bloodline despite her beggar's clothing.",
            "quote": "High Duke Gonzalgo stole my father's wheat fields with a forged royal seal while my father was still dying on the battlefield of Jerida. Chancellor Sadoria taxes the salt on our crusts and calls it fiscal prudence. If the Crown wants a compliant court, look to the Grandees. But if you want a generation of scholars who will brew fire from corpse fat and burn your handlers' leashes to ash, fund this university!",
            "courtDCs": "Morale: 9 (Fierce vengeance & high ideals); Initial Reaction: Skeptical (+0 on 2d6; wary of royal promises). DC 14 Diplomacy to win her passionate loyalty; DC 16 History check to recognize her family crest carved into her mother's signet ring; DC 14 Arcana to appreciate her corpse-fueled incendiary recipes.",
            "publicStance": "Presents herself as an aggressive, overworked student bursar trying to stop the roof from collapsing on the remaining fourteen scholars.",
            "secretAgenda": "Seeks to perfect an alchemical compound derived from necromantic tallow that creates self-propagating green wildfire. She plans to use it to storm and burn Duke Gonzalgo's manor house in Guarralid to reclaim her ancestral land.",
            "rival": "High Duke Gonzalgo de Guarralid (Family Nemesis) & Marquis Murzio de Sadoria (Bureaucratic Thief)",
            "classLevel": "4th-Level Magic-User / Alchemist (Pyrotechnic Savant)",
            "combatStats": "AC 7 (AAC 12) | HP 14 | THAC0 19 | Atk +3 (1d4+1 dagger or 1d6 alchemical vial) | Saves: 14/13/11/15/12"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Royal University of Kordava &bull; Student Body &amp; Bursary</span>
    <span class="badge rival-badge">Primary Rivals: High Duke Gonzalgo de Guarralid &amp; Marquis Murzio de Sadoria</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A proud, slender young woman of nineteen with sharp aristocratic features, sun-freckled skin, and honey-brown hair singed at the fringes from laboratory flash-fires. She wears an ink-splattered homespun scholar's smock belted over heavy buckskin riding trousers and scuffed riding boots. An alchemist's bandolier of stoppered glass phials, copper funnels, and brass measuring spoons sits across her chest.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Rapidly tallies numbers on her fingers while listening; perpetually taps the brass neck of an alchemical flask; speaks with crisp, high-born Zingaran diction that she hastily suppresses into gruff collegiate slang; glares with naked hatred at visiting courtiers wearing silk.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;High Duke Gonzalgo stole my father's wheat fields with a forged royal seal while my father was still dying on the battlefield of Jerida. Chancellor Sadoria taxes the salt on our crusts and calls it fiscal prudence. If the Crown wants a compliant court, look to the Grandees. But if you want a generation of scholars who will brew fire from corpse fat and burn your handlers' leashes to ash, fund this university!&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 9 (Fiercely courageous noble exile); Initial Reaction: Neutral (0 on 2d6; hates the royal court for abandoning her family). DC 14 Diplomacy or a credible pledge of justice against Duke Gonzalgo turns her into a fanatical royal partisan.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Doña Kostanza de Silvero</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Student Bursar &bull; Alchemical Savant &bull; Chaotic Good (Revolutionary zeal, familial justice, fierce loyalty to fellow students)</div>
    </div>
    <span class="stat-class-level">⚔️ 4th-Level Magic-User (Alchemist &amp; Pyrotechnician)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 7 (AAC 12) <small class="text-dim">(Stiffened Canvas Smock, DEX 15 (-1 AC))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 4d4 (+4 CON bonus) &bull; <span style="color: #2ecc71; font-weight: 700;">14 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 19 (Base Attack Bonus +1)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +3 to hit (Tempered copper-alloy bodkin, 1d4+1 piercing); Ranged: +4 to hit (Thrown Alchemical Phial, 1d6 fire/acid, range 30', 5-foot blast radius; DC 14 DEX save or ignited for 1d4 damage/round for 2 rounds)</div>
  </div>

  <div class="stat-section-title">Alchemical Formulas &amp; Special Equipment</div>
  <div style="font-size: 0.88rem; line-height: 1.5; color: var(--text-main); margin-top: 6px;">
    <strong>Corpse-Tallow Wildfire (3 flasks):</strong> Explodes in a spray of emerald flame that clings to armor and water alike, dealing 1d6 damage per round and requiring a full action with sand or vinegar to extinguish.<br>
    <strong>Phosphor Blinding Dust (2 pellets):</strong> Explodes in a dazzling flash (10' radius; all sighted creatures must save vs. Spells or be blinded for 1d4 rounds).<br>
    <strong>Spells Prepared (2 / 2):</strong> <em>Burning Hands, Magic Missile; Pyrotechnics, Web</em>.
  </div>
</div>

<h3>4. The Student Vanguard &amp; The Bursar's Ledgers</h3>
<p>Kostanza is the undisputed leader of the university's fourteen surviving students. When the civil war ended and the professors contemplated disbanding, it was Kostanza who organized night foraging into the ruined warehouses of the harbor, pawned her mother's emerald ear-drops to buy coal, and browbeat the faculty into continuing classes by candlelight.</p>

<p>As bursar, she knows the exact penny-by-penny financial catastrophe facing the university: 1,200 silver pieces owed to the crown, 400 silver pieces in arrears to harbor coal-factors, and 180 silver pieces for grain flour. If the PC Triumvirate provides the 500 gold sovereigns (equal to 5,000 silver pieces), Kostanza will not merely clear the debts—she will organize a disciplined, armed student militia capable of serving as the Triumvirate's loyal intelligence network and laboratory cadre.</p>
""",
        "gmSecrets": "Kostanza possesses the original land title to the Silva Valley wheat estates bearing the authentic wax seal of King Ancillus I. If presented before the Grandee Assembly, it would legally invalidate Duke Gonzalgo de Guarralid's territorial claim, triggering an immediate duel of honor under pundonor rules.",
        "relatedIds": [
            "royal-university-of-kordava",
            "dean-baltasar-argote",
            "valeria-morata",
            "eusebio-falcon",
            "gonzalo-guarralid",
            "sadoria",
            "hook-the-necromancers-endowment"
        ]
    }

    # -------------------------------------------------------------
    # 6. NEW PLOT HOOK ARTICLE: hook-the-necromancers-endowment
    # -------------------------------------------------------------
    hook_article = {
        "id": "hook-the-necromancers-endowment",
        "category": "hooks",
        "title": "The Necromancer's Endowment: Reclaiming the Sunken Spire",
        "subtitle": "Funding the Royal University of Kordava & The Great Thanatological Pivot",
        "tags": ["Plot Hook", "Kingdom Building", "University", "Necromancy", "Triumvirate", "Funding", "Period VIII"],
        "aliases": [
            "The Necromancer's Endowment",
            "Reclaiming the Sunken Spire",
            "The University Endowment",
            "University Funding Hook",
            "The Thanatological Pivot",
            "The Royal University Hook"
        ],
        "summary": "The PC Necromancer's visit to his bankrupt alma mater opens an unprecedented opportunity: finance the university with 500 gold sovereigns to break Master Vane's monopoly, establish an independent royal corps of advanced labor and combat thralls, and uncover the sunken Period III academy ruins beneath the campus.",
        "content": """
<div class="info-card">
  <h4>Executive Hook Summary</h4>
  <p><strong>The Proposition:</strong> <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a>, former mentor to the PC Necromancer, proposes a radical institutional revolution: transform the war-shattered, bankrupt <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">Royal University of Kordava</a> into a state-chartered <strong>College of Applied Thanatology &amp; Deathless Industry</strong> under the direct sovereign patronage of the Triumvirate.</p>
  <p><strong>The Capital Requirement:</strong> 500 Gold Sovereigns (or 5,000 Silver Reals in bullion, grain credit from the <a href="#factions/argossean-grain-fleet" class="wiki-link">Argossean Fleet</a>, or underworld plunder from the <a href="#factions/kordovan-thieves-guild" class="wiki-link">Night Guild</a>) to clear back taxes, repair the leaking roofs, refill the laboratory retorts, and pay the faculty.</p>
  <p><strong>Primary Opposition:</strong> <a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio de Sadoria</a> (threatening immediate eviction), <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a> (fearing the loss of his crown monopoly), and <a href="#npcs/malachai" class="wiki-link">Father Malachai the Blind</a> (rallying pious mobs to burn the campus).</p>
</div>

<h3>1. Narrative Premise &amp; The Rulers' Dilemma</h3>
<p>While exploring the desperate streets of Kordova in disguise, the PC Necromancer returned to their old alma mater, <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>. What they discovered was an institution on the brink of extinction: classrooms open to the rain, libraries rotting from water damage, and the surviving faculty boiling thistles to survive. Yet in the Leaning Spire of Printius, their old professor, <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a>, welcomed them not with despair, but with fiery, messianic ambition.</p>

<p>The Dean wants to discard the useless remnants of scholastic metaphysics and pivot the entire university toward <strong>practical necromancy and deathless industry</strong>. If the PC Triumvirate can deliver 500 gold sovereigns in funding, the Dean promises to create a loyal, crown-controlled academic engine capable of supplying the young monarchs with:</p>
<ul>
  <li><strong>Uncorrupted Sovereign Thralls:</strong> Specialized memory-retaining undead who swear fealty directly to the PC Triumvirate rather than the Restoration Council.</li>
  <li><strong>Subterranean Excavation of the Black Blade:</strong> Pumping out the flooded basements of the Sunken Scriptorium to breach the lost Period III academy ruins where the <a href="#relics/black-blade" class="wiki-link">Black Blade of Azur</a> was swallowed by the earth.</li>
  <li><strong>Alchemical &amp; Pyrotechnic Ordnance:</strong> Mass production of corpse-tallow wildfire and nerve-paralysis agents engineered by <a href="#npcs/constanza-silva" class="wiki-link">Doña Kostanza</a> and <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valessa</a>.</li>
</ul>

<h3>2. The Three Pathways to Funding</h3>
<p>Because Marquis Murzio has padlocked the Royal Treasury, the PCs cannot simply sign a crown check. They must secure the 500 sovereigns through one of three high-stakes sandbox vectors:</p>

<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Funding Pathway</th>
      <th>Method of Acquisition</th>
      <th>Required Checks &amp; Actions</th>
      <th>Political Fallout &amp; Consequences</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>The Grain Fleet Diversion</strong></td>
      <td>Seize, tax, or negotiate a share of the 50,000 bushels aboard <a href="#npcs/nikolos-voros" class="wiki-link">Commodore Voros's</a> fleet, transferring grain credit to harbor merchants in exchange for gold bullion.</td>
      <td>DC 16 Diplomacy or DC 15 Intimidation against Factor Demetrio Phokas; legal confiscation charter signed by Triumvirate.</td>
      <td>Infuriates <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a> and Argos; immediately solves both the city famine and the university crisis.</td>
    </tr>
    <tr>
      <td><strong>The Underworld Syndication</strong></td>
      <td>Broker an investment pact with <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano</a> of the Night Guild. The thieves provide 500 sovereigns of stolen gold in exchange for laboratory fencing and subterranean smuggle-ways.</td>
      <td>DC 15 Charisma check; negotiated treaty with Don Beltrano using <a href="#npcs/joaquin" class="wiki-link">Joachor</a> as intermediary; granting immunity to guild couriers.</td>
      <td>Ties the university intimately to Kordova's underworld; enrages General Valenza's city watch if discovered.</td>
    </tr>
    <tr>
      <td><strong>The Treasury Heist</strong></td>
      <td>Execute the covert infiltration of Chancellor Sadoria's sealed vaults beneath the High Alcázar (<a href="#hooks/hook-treasury-heist" class="wiki-link">The Treasury Heist</a>), liberating the crown's emergency bullion reserves.</td>
      <td>DC 16 Stealth, DC 15 Thievery, and bypassing Vesper the Key-Master's mechanical clockwork wards.</td>
      <td>High Chancellor Sadoria discovers the theft and immediately suspects a palace conspiracy; provides pure sovereign gold with no debt strings.</td>
    </tr>
  </tbody>
</table>
</div>

<h3>3. Escalations &amp; Handler Counter-Moves</h3>
<ol>
  <li><strong>The Chancellor's Eviction Notice:</strong> If the PCs take longer than five days, Marquis Murzio dispatches thirty royal bailiffs and two companies of municipal guards to padlock the university gates and auction the library to Messantian merchants. The PCs must openly countermand the order or pay the arrears.</li>
  <li><strong>Vane's Poisoned Crucible:</strong> <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a> sends an assassin to dump flesh-dissolving vitriol into Maestra Valessa's embalming vats, attempting to frame the university for releasing necrotic contagion into the city gutters.</li>
  <li><strong>The Zealots' Torchlight March:</strong> Pious agitators incited by the underground <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a> gather outside the university gates, demanding the burning of all &ldquo;corpse-witchcraft halls.&rdquo; The PCs must choose between deploying lethal force or debating the mob with pundonor rhetoric.</li>
</ol>

<h3>4. Sovereign Rewards &amp; Kingdom Benefits</h3>
<ul>
  <li><strong>+2 Crown Sovereignty Points:</strong> Demonstrates that the young Triumvirate can establish independent national institutions without the permission of the Restoration Council.</li>
  <li><strong>The Royal Academy Thanatological Engine:</strong> The PCs unlock the ability to commission custom-engineered undead units at half market cost:
    <ul>
      <li><em>Scribe Thralls:</em> Flawless clerical copyists who manage royal ministries without bribery or leaks.</li>
      <li><em>Surgical Embalmed Guards:</em> Non-decomposing shock-troops with +2 HP/HD and natural armor.</li>
      <li><em>Alchemical Munitions:</em> Regular supplies of Corpse-Tallow Wildfire and Paralysis Vials for royal retainers.</li>
    </ul>
  </li>
  <li><strong>Subterranean Infiltration Route:</strong> Direct access to the Sunken Scriptorium's secret tunnels, bypassing city gates and descending into the deepest vaults of <a href="#relics/black-blade" class="wiki-link">The Black Blade of Azur</a>.</li>
</ul>
""",
        "gmSecrets": "If the PC Necromancer performs the foundation reanimation ritual in the Great Amphitheatre personally, the resonance awakens an ancient elven spirit trapped in the marble friezes. The spirit recognizes the PC as a true scion of Ancillus and whispers the command phrase that deactivates the stone golems guarding the deepest Period III catacombs.",
        "relatedIds": [
            "royal-university-of-kordava",
            "dean-baltasar-argote",
            "valeria-morata",
            "eusebio-falcon",
            "constanza-silva",
            "sadoria",
            "vane",
            "nikolos-voros",
            "kordovan-thieves-guild",
            "black-blade",
            "state-of-the-realm"
        ]
    }

    # Add new articles to data['articles']
    new_articles = [
        university_campus,
        dean_article,
        valeria_article,
        eusebio_article,
        constanza_article,
        hook_article
    ]

    # Check for existing IDs to avoid duplicates if re-run
    existing_ids = {a['id'] for a in data['articles']}
    added_count = 0
    for art in new_articles:
        if art['id'] in existing_ids:
            # Update existing
            idx_art = next(i for i, a in enumerate(data['articles']) if a['id'] == art['id'])
            data['articles'][idx_art] = art
            print(f"Updated article: {art['id']}")
        else:
            data['articles'].append(art)
            existing_ids.add(art['id'])
            added_count += 1
            print(f"Added new article: {art['id']}")

    # -------------------------------------------------------------
    # 7. UPDATE EXISTING ARTICLES WITH EXPANDED LORE & HYPERLINKS
    # -------------------------------------------------------------

    # A. Update kordava (Gazetteer)
    kordava_art = next((a for a in data['articles'] if a['id'] == 'kordava'), None)
    if kordava_art:
        uni_section = """
<h4>The University Quarter &amp; The Cloisters of San Ancillus</h4>
<p>Clinging to the western granite escarpment overlooking the chasm of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> sits the <strong>University Quarter</strong>, dominated by the walled, battle-scarred compound of <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>. Once celebrated as the philosophical capital of the Hyborian world, the quarter was ravaged during the <a href="#history/period-vii" class="wiki-link">Restoration Civil War</a>. Today, narrow cobblestone alleys wind between soot-stained marble arcades, shuttered apothecary shops, and cheap taverns where hungry scholars and dispossessed students rub shoulders with underworld cutpurses. Under the visionary leadership of <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a>, the district is on the verge of a dark rebirth as the kingdom's new center for practical thanatological research and deathless engineering.</p>
"""
        if 'The University Quarter &amp; The Cloisters of San Ancillus' not in kordava_art['content']:
            kordava_art['content'] += uni_section
            print("Updated kordava article with University Quarter!")
        for rid in ['royal-university-of-kordava', 'dean-baltasar-argote', 'hook-the-necromancers-endowment']:
            if rid not in kordava_art.get('relatedIds', []):
                kordava_art.setdefault('relatedIds', []).append(rid)

    # B. Update vane (Master Alchemist Vane)
    vane_art = next((a for a in data['articles'] if a['id'] == 'vane'), None)
    if vane_art:
        vane_rivalry = """
<p><strong>The Academic Feud with Dean Argoto:</strong> Vane nurses a cold, contemptuous hatred for <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a> and the faculty of <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>, where Vane once studied before abandoning the academy for lucrative crown monopolies. Vane views Argote as an impractical philosophical dinosaur who squanders resources on preserving the memories and souls of corpses, whereas Vane believes in breaking thralls into dumb, efficient beasts of burden. Vane has planted an informant among the students and has urged Chancellor Sadoria to bulldoze the campus to prevent the university from breaking the crown's industrial monopoly.</p>
"""
        if 'The Academic Feud with Dean Argoto' not in vane_art['content']:
            vane_art['content'] += vane_rivalry
            print("Updated vane article with Dean Argoto rivalry!")
        if 'Dean Don Balthaso de Argoto' not in vane_art['atAGlance']['rival']:
            vane_art['atAGlance']['rival'] += " & Dean Don Balthaso de Argoto (Academic Ideological Rival)"
        for rid in ['dean-baltasar-argote', 'royal-university-of-kordava', 'valeria-morata']:
            if rid not in vane_art.get('relatedIds', []):
                vane_art.setdefault('relatedIds', []).append(rid)

    # C. Update escovedo (Dr. Horasto Escovador)
    escovedo_art = next((a for a in data['articles'] if a['id'] == 'escovedo'), None)
    if escovedo_art:
        escovedo_connection = """
<p><strong>Ties to the Royal University:</strong> Dr. Escovador maintains a lively, clandestine correspondence with <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Balthaso de Argoto</a> and <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valessa de Morato</a> at <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>. Although Escovador publicly dismisses reanimation as &ldquo;anatomical vulgarity,&rdquo; he frequently trades rare imported medicinal roots and court cadaver samples with Maestra Valessa in exchange for purified embalming salts and nerve-stabilizing compounds.</p>
"""
        if 'Ties to the Royal University' not in escovedo_art['content']:
            escovedo_art['content'] += escovedo_connection
            print("Updated escovedo article with university connection!")
        for rid in ['royal-university-of-kordava', 'valeria-morata', 'dean-baltasar-argote']:
            if rid not in escovedo_art.get('relatedIds', []):
                escovedo_art.setdefault('relatedIds', []).append(rid)

    # D. Update sadoria (High Chancellor Marquis Murzio de Sadoria)
    sadoria_art = next((a for a in data['articles'] if a['id'] == 'sadoria'), None)
    if sadoria_art:
        sadoria_uni = """
<p><strong>The University Foreclosure:</strong> Sadoria has deliberately stripped <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a> of all state subsidies, labeling higher education a frivolous luxury during national bankruptcy. He has issued a formal foreclosure warrant against <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Argoto</a> for 1,200 silver pieces in back taxes, planning to demolish the historic cloisters to construct bonded warehouses for Argossean mercantile syndicates.</p>
"""
        if 'The University Foreclosure' not in sadoria_art['content']:
            sadoria_art['content'] += sadoria_uni
            print("Updated sadoria article with university foreclosure!")
        for rid in ['royal-university-of-kordava', 'dean-baltasar-argote', 'hook-the-necromancers-endowment']:
            if rid not in sadoria_art.get('relatedIds', []):
                sadoria_art.setdefault('relatedIds', []).append(rid)

    # E. Update the-pit (The Pit)
    pit_art = next((a for a in data['articles'] if a['id'] == 'the-pit'), None)
    if pit_art:
        pit_uni = """
<p><strong>The University Scriptorium Outfall:</strong> Directly above the northern rim of The Pit loom the crumbling foundations of <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>. Flooded drainage conduits and ancient elven cisterns beneath the Sunken Scriptorium descend straight into the upper levels of The Pit, providing a covert smuggling conduit utilized by <a href="#npcs/eusebio-falcon" class="wiki-link">Maestro Eusevios</a> and underworld scavengers from the <a href="#factions/kordovan-thieves-guild" class="wiki-link">Night Guild</a>.</p>
"""
        if 'The University Scriptorium Outfall' not in pit_art['content']:
            pit_art['content'] += pit_uni
            print("Updated the-pit article with university conduit!")
        for rid in ['royal-university-of-kordava', 'dean-baltasar-argote']:
            if rid not in pit_art.get('relatedIds', []):
                pit_art.setdefault('relatedIds', []).append(rid)

    # F. Update kordovan-thieves-guild
    thieves_art = next((a for a in data['articles'] if a['id'] == 'kordovan-thieves-guild'), None)
    if thieves_art:
        thieves_uni = """
<p><strong>The Academic Black Market:</strong> The Night Guild maintains a thriving contraband conduit with the faculty and student body of <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>. In exchange for copper coin and illicit alchemical reagents from <a href="#npcs/constanza-silva" class="wiki-link">Doña Kostanza</a>, guild cutpurses smuggle fresh unclaimed cadavers from the harbor slums to <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valessa</a> and fence rare manuscripts stolen from noble estates through <a href="#npcs/eusebio-falcon" class="wiki-link">Maestro Eusevios</a>.</p>
"""
        if 'The Academic Black Market' not in thieves_art['content']:
            thieves_art['content'] += thieves_uni
            print("Updated kordovan-thieves-guild with academic black market connection!")
        for rid in ['royal-university-of-kordava', 'valeria-morata', 'eusebio-falcon']:
            if rid not in thieves_art.get('relatedIds', []):
                thieves_art.setdefault('relatedIds', []).append(rid)

    # G. Update necromancy-mechanics
    necro_art = next((a for a in data['articles'] if a['id'] == 'necromancy-mechanics'), None)
    if necro_art:
        necro_uni = """
<p><strong>The Academic School of Thanatology:</strong> While commercial operators like <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a> ignore the psychological torment of memory-retaining thralls to maximize manual output, <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a> and the faculty of <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a> study memory-retention as a noble arcane science. Their research focuses on stabilizing living memories to produce specialized clerical, surgical, and defensive thralls who serve with conscious loyalty rather than brute compulsion.</p>
"""
        if 'The Academic School of Thanatology' not in necro_art['content']:
            necro_art['content'] += necro_uni
            print("Updated necromancy-mechanics with university academic lineage!")
        for rid in ['royal-university-of-kordava', 'dean-baltasar-argote', 'valeria-morata']:
            if rid not in necro_art.get('relatedIds', []):
                necro_art.setdefault('relatedIds', []).append(rid)

    # H. Update court-matrix
    matrix_art = next((a for a in data['articles'] if a['id'] == 'court-matrix'), None)
    if matrix_art:
        dean_row = """    <tr>
      <td><strong><a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a></strong><br><small>Rector Magnificus of Royal University</small></td>
      <td><span class="badge">The Royal University of Kordava / Arcane Academia</span></td>
      <td><strong>Delighted / Academic Mentor &amp; Ally:</strong> Enthusiastically offers to pivot the university into a state necromantic powerhouse if the PC Necromancer can secure funding.</td>
      <td class="gm-only-cell"><span class="badge gm-badge">SECRETS</span> Desperate to excavate buried Period III academy ruins to find Printius's grimoire; keeps reanimated predecessor in a locked trunk; terrified of Sadoria's eviction bailiffs.</td>
      <td><a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a> &amp; <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio de Sadoria</a></td>
    </tr>
"""
        if 'dean-baltasar-argote' not in matrix_art['content']:
            # Insert before </tbody>
            matrix_art['content'] = matrix_art['content'].replace('</tbody>', dean_row + '  </tbody>')
            print("Updated court-matrix with Dean Argoto!")
        if 'dean-baltasar-argote' not in matrix_art.get('relatedIds', []):
            matrix_art.setdefault('relatedIds', []).append('dean-baltasar-argote')

    # I. Update state-of-the-realm
    realm_art = next((a for a in data['articles'] if a['id'] == 'state-of-the-realm'), None)
    if realm_art:
        crisis_row = """    <tr>
      <td><strong>The Intellectual Collapse &amp; The Necromantic Pivot</strong></td>
      <td><a href="#gazetteer/royal-university-of-kordava" class="wiki-link">Royal University of Kordava</a></td>
      <td><span class="badge" style="background: rgba(155, 89, 182, 0.2); border-color: #9b59b6; color: #9b59b6;">ARCANE / RECONSTRUCTION</span></td>
      <td><a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a>, <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio</a>, <a href="#npcs/vane" class="wiki-link">Master Vane</a></td>
      <td><a href="#hooks/hook-the-necromancers-endowment" class="wiki-link">The Necromancer's Endowment</a></td>
      <td>The kingdom's sole university is bankrupt and faces eviction by Sadoria. The Dean seeks 500 gold sovereigns from the PC Necromancer to rebuild the campus as a state necromantic powerhouse, challenging Master Vane's monopoly.</td>
    </tr>
"""
        crisis_dossier = """
<h4>Crisis 8: The Ruined Alma Mater &amp; The Thanatological Charter</h4>
<div class="crisis-card">
  <div class="crisis-meta">
    <span class="badge" style="background: rgba(155, 89, 182, 0.2); border-color: #9b59b6; color: #9b59b6;">SECTOR: ARCANE RECONSTRUCTION &bull; INSTITUTIONAL POWER</span>
    <span class="threat-level severe">THREAT LEVEL: HIGH INSTITUTIONAL OPPORTUNITY &bull; CRISIS CLOCK: 5 DAYS</span>
  </div>
  <p><strong>The Situation:</strong> The historic <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">Royal University of Kordava</a>, where the PC Necromancer was educated, stands in ruins following the civil war. Chancellor Sadoria has served an eviction warrant for 1,200 silver pieces in back taxes to auction the grounds to Argossean merchant syndicates. <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Balthaso de Argoto</a> has offered to pivot the university into an independent royal college of necromancy if the PC can secure 500 gold sovereigns in funding.</p>
  <p><strong>Strategic Stakes:</strong> Funding the university breaks <a href="#npcs/vane" class="wiki-link">Master Vane's</a> corrupt monopoly over undead labor, provides the Triumvirate with loyal necromantic researchers and non-decomposing shock-troops, and opens an excavation route into the subterranean ruins of the Period III academy where the <a href="#relics/black-blade" class="wiki-link">Black Blade of Azur</a> was lost.</p>
  <p><strong>Associated Hook:</strong> <a href="#hooks/hook-the-necromancers-endowment" class="wiki-link">The Necromancer's Endowment: Reclaiming the Sunken Spire</a>.</p>
</div>
"""
        if 'Crisis 8: The Ruined Alma Mater' not in realm_art['content']:
            # Insert into table before </tbody>
            if 'The Intellectual Collapse &amp; The Necromantic Pivot' not in realm_art['content']:
                realm_art['content'] = realm_art['content'].replace('</tbody>', crisis_row + '  </tbody>', 1)
            realm_art['content'] += crisis_dossier
            print("Updated state-of-the-realm with Crisis 8!")
        for rid in ['royal-university-of-kordava', 'dean-baltasar-argote', 'hook-the-necromancers-endowment']:
            if rid not in realm_art.get('relatedIds', []):
                realm_art.setdefault('relatedIds', []).append(rid)

    # J. Update hooks-index
    hooks_idx = next((a for a in data['articles'] if a['id'] == 'hooks-index'), None)
    if hooks_idx:
        hook_entry = """    <li><strong><a href="#hooks/hook-the-necromancers-endowment" class="wiki-link">The Necromancer's Endowment</a>:</strong> Secure 500 gold sovereigns to fund Dean Argoto's radical necromantic pivot at the ruined Royal University of Kordava, defying Chancellor Sadoria and breaking Master Vane's monopoly.</li>
"""
        if 'hook-the-necromancers-endowment' not in hooks_idx['content']:
            # Add under Economic Recovery & Thrall Labor Crises or Arcana
            target = '<h4>4. Arcana, Relics &amp; Eldritch Threats</h4>\n  <ul>'
            if target in hooks_idx['content']:
                hooks_idx['content'] = hooks_idx['content'].replace(target, target + '\n' + hook_entry)
            else:
                hooks_idx['content'] += '\n' + hook_entry
            print("Updated hooks-index with The Necromancer's Endowment!")
        if 'hook-the-necromancers-endowment' not in hooks_idx.get('relatedIds', []):
            hooks_idx.setdefault('relatedIds', []).append('hook-the-necromancers-endowment')

    # -------------------------------------------------------------
    # 8. UPDATE META & WRITE js/data.js
    # -------------------------------------------------------------
    data['meta']['totalArticles'] = len(data['articles'])
    data['meta']['lastUpdated'] = "2026-10-15T17:15:00.000Z"
    print(f"Total articles now: {data['meta']['totalArticles']}")

    output_js = "window.WIKI_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(output_js)
    print("Successfully wrote updated js/data.js!")

    # -------------------------------------------------------------
    # 9. UPDATE data/sessions.json (Session 1)
    # -------------------------------------------------------------
    with open('data/sessions.json', 'r', encoding='utf-8') as f:
        sessions = json.load(f)

    s1 = next((s for s in sessions if s.get('sessionNumber') == 1), None)
    if s1:
        uni_narrative = " Meanwhile, taking advantage of their incognito journey into the city, the player necromancer broke off to visit his old alma mater, the Royal University of Kordava. Found clinging to the western cliffs above The Pit in near-total ruin after the civil wars, the campus is on the verge of eviction by High Chancellor Marquis Murzio. In the Leaning Spire of Printius, the player met his former mentor, Dean Don Balthaso de Argoto. Rather than despairing, Dean Argoto enthusiastically shared the player's passion for necromancy and expressed unbridled delight at the prospect of taking the university in a new, zombie-focused direction—transforming the battered institution into a state-sponsored College of Applied Thanatology and Deathless Industry, provided the player can secure 500 gold sovereigns in funding."
        
        if "royal university of kordava" not in s1['summary'].lower():
            s1['summary'] += uni_narrative
            print("Enriched Session 1 summary with university visit!")

        # Active threads
        uni_thread = "The Dean's Endowment: Dean Don Balthaso de Argoto is eager to transform the ruined Royal University of Kordava into a premier necromantic college if the PC Necromancer can secure 500 gold sovereigns in funding before Chancellor Sadoria's eviction bailiffs arrive."
        if uni_thread not in s1['activeThreads']:
            s1['activeThreads'].append(uni_thread)
            print("Added Dean's Endowment active thread to Session 1!")

        # NPC Dispositions
        s1['npcDispositions']["Dean Don Balthaso de Argoto"] = "Delighted / Enthusiastic Mentor (+3 Reaction, Awaiting 500-sovereign royal funding to launch the necromantic curriculum)"
        s1['npcDispositions']["Maestra Valessa de Morato"] = "Wary / Professionally Curious (Demands clean zinc tables, embalming brine, and fresh cadavers)"
        s1['npcDispositions']["Doña Kostanza de Silvero"] = "Skeptical / Calculating (Managing the university's bankrupt ledgers and watching the Triumvirate's promises)"

        with open('data/sessions.json', 'w', encoding='utf-8') as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
        print("Successfully updated data/sessions.json!")

    print("\n--- University of Kordava Wiki Expansion Complete! ---")

if __name__ == '__main__':
    main()
