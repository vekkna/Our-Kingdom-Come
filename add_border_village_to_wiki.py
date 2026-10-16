"""
add_border_village_to_wiki.py
Expands the Our Kingdom Come campaign wiki with:
1. Gazetteer Entry: San Severo del Vado (The Border Crossing of the Bitter Waters / The Salt-Gate)
2. Faction Entry: La Hermandad de las Espinas (The Border Uprising of San Severo / The Salt-Road Insurgents)
3. NPC Entry: Capitán Androvo 'The Broken' de Ojedo (The Broken Captain / Rebel Commander)
4. NPC Entry: Madre Soledor 'The Marked' (Gnostic Prophetess of the Border Refugees)
5. NPC Entry: Alcalde Barzolo Kadenzo (The Beleaguered Bailiff of San Severo)
6. Plot Hook 1: The Executioner's Crown: The Uprising at San Severo
7. Plot Hook 2: The Deserter's Confession: Rodorigo's Blood-Stained Ledger
8. Comprehensive updates & cross-links across:
   - General Don Rodorigo de Valenza (valenza): The Royal Expedition, Campaign March dynamics, Campfire Dilemmas, Testing the PCs
   - Velasco (velasco): Border Choke-Point, Refugee Conduit, Impending Holy Relief Warband
   - Church of Nemeth (church-of-nemeth): Border Sanctuaries & Gnostic Martyr Cells
   - Regional Gazetteer Matrix (gazetteer-matrix): San Severo row
   - Court Relationship Matrix (court-matrix): New rows for Androvo, Madre Soledor, Alcalde Kadenzo
   - State of the Realm Master Crisis Registry (state-of-the-realm): Crisis 10 Dossier
   - Master Plot Hooks Index (hooks-index): Military & Border Insurgency listings
   - Session Log (data/sessions.json): Session 2 logged and active threads updated
"""

import json
import sys

def main():
    print("Starting San Severo Border Village & Don Rodorigo Expedition Wiki Expansion...")

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
    # 1. NEW GAZETTEER ARTICLE: san-severo
    # -------------------------------------------------------------
    san_severo_article = {
        "id": "san-severo",
        "category": "gazetteer",
        "title": "San Severo del Vado (The Bitter Ford & The Salt Gate)",
        "subtitle": "Border Waypoint Between Kordova & Velasco • Crucible of the Refugee Uprising",
        "tags": ["Gazetteer", "Geography", "Border", "San Severo", "Velasco", "Church of Nemeth", "Refugees", "Period VIII", "Rebellion"],
        "aliases": [
            "San Severo",
            "San Severo del Vado",
            "El Vado Amargo",
            "The Bitter Ford",
            "Village of San Severo",
            "The Salt Gate",
            "Vado de San Severo",
            "Puente de los Desamparados",
            "San Severo Crossing"
        ],
        "summary": "A fortified river-crossing and frontier settlement situated on the old royal highway midway between Kordova and the rebellious port of Velasco. Built around the pre-Cataclysmic stone bridge of El Puente de los Desamparados, San Severo has become an explosive flashpoint: overwhelmed by hundreds of destitute religious refugees who collapsed during the southern exodus, the starving village rose in armed revolt against the crown's ruinous grain requisitions and salt monopolies. Now barricaded by La Hermandad de las Espinas, the village faces imminent annihilation by General Don Rodorigo de Valenza's punitive expedition.",
        "content": """
<div class="info-card">
  <p><strong>Geographical Type:</strong> Fortified River Crossing &bull; Agricultural &amp; Salt-Caravan Waypoint</p>
  <p><strong>Location:</strong> The borderlands between the central Kordovan scrub-plains and the southwestern coastal hills of <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>, spanning the Rio Salado (River of Bitter Salt)</p>
  <p><strong>Strategic &amp; Economic Value:</strong> Sole heavy wagon crossing on <em>El Camino del Sur</em> (The Salt Highway); customs toll-house; royal granary outpost; caravan staging post</p>
  <p><strong>Ruling Power (De Facto):</strong> <em>La Hermandad de las Espinas</em> (Armed insurgent commune of local peasants, army deserters, and Gnostic refugees)</p>
  <p><strong>Nominal Crown Bailiff:</strong> <a href="#npcs/alcalde-cadenas" class="wiki-link">Alcalde Barzolo Kadenzo</a> (Detained / Coerced Magistrate)</p>
  <p><strong>Primary Encounter Hazards:</strong> Spiked bridge barricades, boiling pitch caldrons, concealed caltrop fields, desperate refugee archers, approaching theocratic relief warbands</p>
</div>

<h3>1. Geographical Overview: The Bitter Ford</h3>
<p>Nestled in a limestone depression where the arid scrub of central Zingara descends into the fertile, brackish salt marshes of the southern coast, <strong>San Severo del Vado</strong> commands the only reliable heavy wagon ford across the <strong>Rio Salado</strong>. The river here runs shallow but treacherous over jagged white salt-crusted shoals, flanked by steep gypsum bluffs. For centuries, all land commerce between the capital of <a href="#gazetteer/kordava" class="wiki-link">Kordova</a> and the maritime hub of <a href="#gazetteer/velasco" class="wiki-link">Velasco</a> had to funnel across the village's centerpiece: <strong>El Puente de los Desamparados (The Bridge of the Forsaken)</strong>—a massive, three-arched pre-Cataclysmic bridge of weathered green basalt that has stood since Period II.</p>

<p>The settlement itself consists of roughly eighty whitewashed stone-and-timber cottages with low clay-tile roofs, clustered around a cobblestone plaza, a fortified stone granary, and <strong>La Capilla de los Afligidos (The Chapel of the Afflicted)</strong>. The surrounding landscape is a patchwork of parched barley terraces, scrub olive groves, and ancient shallow evaporation basins where villagers scrape coarse grey rock salt from the river mud.</p>

<h3>2. The War Exodus &amp; The Refugee Influx</h3>
<p>The tragedy of San Severo began during the brutal close of Period VII and the early days of Period VIII. When the Restoration Council under <a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a> initiated widespread purges of suspected heretics in Kordova, tens of thousands of devout adherents of the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a> embarked on their desperate, panic-stricken migration south toward Velasco. <em>El Camino del Sur</em> became an open artery of misery: hundreds of sick, elderly, wounded, and orphaned refugees collapsed on the sun-baked road before reaching the coast.</p>

<p>Moved by basic human pity—and long alienated by the greedy exactions of Kordova's tax-farmers—the people of San Severo opened their doors. Led by the charismatic refugee prophetess <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor 'The Marked'</a>, more than three hundred refugees found shelter in the village chapel, abandoned barns, and dry river caves. The refugees brought with them their austere Gnostic faith, their communal bread-sharing rituals, and horrific eyewitness accounts of the royal army's atrocities in the capital. Within months, the local peasantry had adopted the refugees' symbols, intertwining local agrarian despair with fervent religious solidarity.</p>

<h3>3. The Spark of Uprising: The Salt Embargo &amp; The Press-Gangs</h3>
<p>The uneasy peace shattered when the holy revolution triumphed in Velasco. The newly instituted <em>Council of the Pure</em> expelled the nobility and clamped a total trade embargo on Kordova, cutting off shipments of preserved fish and fine salt. In Kordova, High Chancellor <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio de Sadoria</a> faced financial ruin, while General Valenza needed food and men to maintain his border garrisons.</p>

<p>Three weeks ago, Royal Army bailiffs and press-gangs descended upon San Severo. They demanded:</p>
<ul>
  <li>Immediate surrender of seventy percent of the village's winter seed grain to feed Valenza's cavalry mounts.</li>
  <li>Forced seizure of all stockpiled rock salt for crown meat-packing depots.</li>
  <li>Conscription of every able-bodied youth between fourteen and forty into the royal penal cohorts.</li>
  <li>The arrest and extradition of all Kordovan religious refugees as "proscribed seditionists."</li>
</ul>

<p>When two village elders knelt in the dust to beg for mercy, the army bailiff ordered them flogged to death on the village fountain. The settlement erupted. Led by <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo 'The Broken' de Ojedo</a>—a former royal army cavalry lieutenant living in hiding—the villagers and refugees seized billhooks, scythes, and hunting bows, drove the bailiffs into the river, detained <a href="#npcs/alcalde-cadenas" class="wiki-link">Alcalde Barzolo Kadenzo</a>, and declared the <strong>Commune of the Bitter Ford</strong>. They hoisted the ragged black banner of <strong><a href="#factions/hermandad-de-las-espinas" class="wiki-link">La Hermandad de las Espinas</a></strong> and swore an oath over the chapel altar to die before surrendering a single grain of wheat or a single refugee orphan to the crown.</p>

<h3>4. The Defensive Redoubt &amp; The Barricaded Bridge</h3>
<p>Under the veteran military eye of Capitán Androvo, San Severo was transformed in under a fortnight into a formidable defensive redoubt:</p>
<ul>
  <li><strong>The Bridgehead Bastion:</strong> Both ends of <em>El Puente de los Desamparados</em> have been choked with overturned freight wains, timber stakes, and rubble. Spiked iron chains are stretched across the basalt parapets to trip charging heavy warhorses.</li>
  <li><strong>The Pitch Caldrons:</strong> Large copper vats of boiling river pitch and sulfurous tallow, gathered from local sheep-dip pits, are positioned above the bridge piers, ready to be dumped on any infantry attempting to scale the spans.</li>
  <li><strong>The Salt Marshes:</strong> The river shallows above and below the bridge have been seeded with iron caltrops and deep, muddy stakes, making outflanking cavalry maneuvers nearly suicidal.</li>
</ul>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE GENERAL'S SECRET MOTIVE</div>
  <p><strong>Rodorigo's Personal Vendetta:</strong> General Don Rodorigo de Valenza's stated objective to the PC Triumvirate is that San Severo represents a 'cancerous treason' that must be cauterized to show the realm that the new monarchs possess an iron will. However, Rodorigo's true panic stems from the fact that <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo de Ojedo</a> is alive and leading the rebels. Androvo was Rodorigo's personal vanguard officer during Period VII and holds a physical, wax-sealed military order written in Rodorigo's own hand commanding the deliberate slaughter and church-burning of an unresisting refugee column. If that document reaches the young monarchs or the public, Rodorigo's martial reputation under <a href="#rules/pundonor" class="wiki-link">Pundonor</a> will be irreparably shattered.</p>
</div>

<h3>5. Strategic Stakes for the PC Triumvirate</h3>
<p>Riding with General Valenza's punitive expedition, the young monarchs face their first real crucible of kingship beyond the palace walls:</p>
<ul>
  <li><strong>Public Royal Image:</strong> Riding at the head of two hundred steel-clad caballeros allows the PCs to present themselves to the provincial populace as active, warrior sovereigns rather than decadent palace captives. However, if they stand by and permit a bloody slaughter of starving peasants and weeping nuns, they will be forever branded as butchering tyrants across southern Zingara.</li>
  <li><strong>Evaluating the General:</strong> Observing Don Rodorigo on the march provides unprecedented insight into his tactical command doctrines, his ruthless efficiency, and the private fissures within his officer corps.</li>
  <li><strong>The Ticking Clock of Velasco:</strong> Unknown to Don Rodorigo, <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor</a> has dispatched carrier pigeons to <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>. An armed relief column of eighty fanatical warrior-monks (<em>Los Flagelantes del Mar</em>) is currently marching up the river road. If blood is spilled at San Severo before a resolution is reached, all-out war between Kordova and Velasco will ignite.</li>
</ul>
""",
        "gmSecrets": "San Severo's stone chapel conceals a subterranean crypt connected to an ancient pre-Cataclysmic aqueduct that runs underneath the Rio Salado, offering a secret infiltration route directly behind the rebel barricades. Furthermore, Alcalde Kadenzo has buried 450 silver pieces and 35 gold sovereigns of embezzled crown transit taxes beneath the flagstones of the customs house.",
        "relatedIds": [
            "valenza",
            "velasco",
            "hermandad-de-las-espinas",
            "andres-hojeda",
            "madre-soledad",
            "alcalde-cadenas",
            "church-of-nemeth",
            "hook-uprising-san-severo",
            "hook-the-deserters-testimony",
            "gazetteer-matrix",
            "state-of-the-realm"
        ]
    }

    # -------------------------------------------------------------
    # 2. NEW FACTION ARTICLE: hermandad-de-las-espinas
    # -------------------------------------------------------------
    hermandad_article = {
        "id": "hermandad-de-las-espinas",
        "category": "factions",
        "title": "La Hermandad de las Espinas (The Border Uprising of San Severo)",
        "subtitle": "The Insurgent Commune of the Salt-Gate & Border Refugee Covenant",
        "tags": ["Faction", "Rebellion", "Insurgents", "San Severo", "Peasantry", "Church of Nemeth", "Refugees", "Period VIII"],
        "aliases": [
            "The Brotherhood of Thorns",
            "La Hermandad de las Espinas",
            "San Severo Rebels",
            "The Salt-Gate Insurgents",
            "The Rebels of San Severo",
            "The Bitter Ford Covenant",
            "Comuneros del Vado",
            "Hermandad del Vado",
            "The Thorn Brotherhood"
        ],
        "summary": "An armed populist coalition formed between the starving agrarian peasantry of San Severo, royal army deserters, and militant Gnostic religious refugees fleeing Kordova. Fortified behind the basalt bridge of El Puente de los Desamparados, the Brotherhood has renounced royal taxation, seized crown granaries, and sworn to defend their border sanctuary to the death against General Valenza's army.",
        "content": """
<div class="info-card">
  <p><strong>Faction Classification:</strong> Armed Border Commune &bull; Popular Insurgent Coalition</p>
  <p><strong>Military Commander:</strong> <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo 'The Broken' de Ojedo</a> (Former Royal Cavalry Officer)</p>
  <p><strong>Spiritual Leader:</strong> <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor 'The Marked'</a> (Gnostic Prophetess)</p>
  <p><strong>Headquarters:</strong> The Barricaded Basalt Bridge (<em>El Puente de los Desamparados</em>) &amp; La Capilla de los Afligidos, <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a></p>
  <p><strong>Faction Symbol:</strong> A crown of wild river briars encircling a broken silver cavalry sword</p>
  <p><strong>Combat Strength:</strong> ~120 active combatants (20 veteran deserters, 40 refugee zealots, 60 armed peasants) backed by 200 non-combatant refugees and villagers</p>
  <p><strong>Primary Allies:</strong> Sympathetic underground cells of the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a>, peasant communes of the southern salt roads, and potential relief forces from <a href="#gazetteer/velasco" class="wiki-link">Velasco</a></p>
  <p><strong>Primary Enemies:</strong> <a href="#factions/military-elite" class="wiki-link">The Military Elite</a> (<a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a>), <a href="#factions/restoration-council" class="wiki-link">The Restoration Council</a>, and royal tax bailiffs</p>
</div>

<h3>1. Origins &amp; Composition: The Covenant of Thorns</h3>
<p><strong>La Hermandad de las Espinas (The Brotherhood of Thorns)</strong> was born of sheer desperation in the dusty borderlands of southern Zingara. When the Restoration Council in Kordova sought to finance its bankrupt treasury through draconian grain seizures and forced military conscription, the border settlement of <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a> became the breaking point. The Brotherhood unites three distinct social groups who would ordinarily never stand together:</p>
<ol>
  <li><strong>The Disillusioned Army Deserters (The Iron Core):</strong> Twenty battle-hardened veterans of Period VII led by <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo de Ojedo</a>. Equipped with battered breastplates, broadswords, and heavy military crossbows, they provide tactical discipline, engineer barricades, and know the royal army's assault doctrines intimately.</li>
  <li><strong>The Religious Refugee Zealots (The Spiritual Spine):</strong> Forty ascetic men and women who survived the religious purges in Kordova and revere <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor</a>. Clad in grey homespun habits and armed with hunting spears and morningstars, they are driven by a burning conviction that the Triumvirate's court is an unholy den of necromancy and oppression. They fight without fear of death, singing somber Gnostic hymns under arrow fire.</li>
  <li><strong>The Local Agrarian Peasantry (The Mass Levies):</strong> Sixty local salt-workers, farmers, and olive-growers. Armed with re-forged scythes, pitchforks, billhooks, and sling-stones, they fight to preserve the remaining sacks of flour that will keep their children alive through the winter.</li>
</ol>

<h3>2. The Political &amp; Ideological Divide</h3>
<p>While united behind the barricades, the Brotherhood suffers from an intense internal ideological friction that the PC Triumvirate can exploit through diplomacy:</p>
<ul>
  <li><strong>The Moderate Peasant Faction (Androvo's Wing):</strong> Realistic and war-weary. They do not seek to overthrow the monarchy; they want survival. Their demands are practical: a full royal pardon, suspension of the winter grain requisition, confirmation of their salt-gathering rights, and the removal of abusive crown bailiffs. If the PCs demonstrate genuine royal mercy and sovereign authority independent of Rodorigo, Androvo will surrender his sword.</li>
  <li><strong>The Fanatical Zealot Faction (Soledor's Wing):</strong> Radical and unyielding. They view the uprising as an apocalyptic holy war. They demand that Kordova dismantle its industrial zombie pits, outlaw necromancy, and hand over General Valenza for a public trial before the elders of <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>. They would rather see the village burn to ash than bend the knee to an 'impure puppet of warlords.'</li>
</ul>

<h3>3. Military Arsenal &amp; Defenses</h3>
<p>Despite being outnumbered by General Valenza's professional army, the Brotherhood holds massive terrain advantages:</p>
<ul>
  <li><strong>Choke-Point Bridgehead:</strong> <em>El Puente de los Desamparados</em> forces attackers into a narrow, twenty-foot-wide kill-zone where cavalry charges are broken by heavy oak timber chevaux-de-frise and spiked chains.</li>
  <li><strong>Sulfurous Fire Pots:</strong> The rebels have prepared fifty ceramic vessels filled with distilled marsh pitch, brimstone, and quicklime, designed to shatter and engulf armored caballeros in inextinguishable flame.</li>
  <li><strong>The Ford Caltrops:</strong> Hundreds of four-spiked forged iron caltrops litter the river bed, preventing horsemen from wading the Rio Salado to flank the village.</li>
</ul>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE VELASCO WAR-BARGE FACTOR</div>
  <p><strong>The Impending Crusade:</strong> Unknown to Don Rodorigo, Madre Soledor sent a courier pigeon to the Council of the Pure in Velasco three days ago. An armed river-cog carrying eighty holy warrior-monks (<em>Los Flagelantes del Mar</em>) under Father Barzolo the Unforgiving is currently forty miles downriver, navigating upstream toward San Severo. If Rodorigo launches a frontal assault, the battle will draw Velasco's forces directly into the fray, expanding a local pacification into a full-scale religious war.</p>
</div>
""",
        "gmSecrets": "If the Brotherhood is massacred, surviving sleeper cells in the salt marsh will swear a blood-vendetta against the PC Triumvirate, sending fanatical suicide assassins armed with poisoned pitch daggers to infiltrate the High Alcázar in Kordova.",
        "relatedIds": [
            "san-severo",
            "andres-hojeda",
            "madre-soledad",
            "alcalde-cadenas",
            "valenza",
            "velasco",
            "church-of-nemeth",
            "military-elite",
            "hook-uprising-san-severo"
        ]
    }

    # -------------------------------------------------------------
    # 3. NEW NPC ARTICLE: andres-hojeda
    # -------------------------------------------------------------
    andres_article = {
        "id": "andres-hojeda",
        "category": "npcs",
        "title": "Capitán Androvo 'The Broken' de Ojedo",
        "subtitle": "The Broken Captain • Rebel Commander of San Severo & Disillusioned Veteran of the Royal Army",
        "tags": ["Royal Court", "NPC", "Fighter", "Rebel", "Military", "San Severo", "Period VII", "Period VIII", "Labyrinth Lord"],
        "aliases": [
            "Capitán Androvo",
            "Androvo de Ojedo",
            "The Broken",
            "The Broken Captain",
            "Captain Ojedo",
            "Androvo el Quebrantado",
            "Commander Ojedo",
            "The Rebel Captain",
            "Androvo of the Ford"
        ],
        "summary": "Former trusted cavalry lieutenant in General Don Rodorigo de Valenza's elite vanguard during the Restoration Civil War. Disillusioned and haunted by atrocities committed against defenseless refugee columns, Androvo broke his sword, deserted his post, and sought anonymous peace as a blacksmith in San Severo. When the crown pushed the village past endurance, he reluctantly took command of the peasant uprising. He possesses devastating, first-hand knowledge of Don Rodorigo's military methods—and holds the sealed execution order that could ruin the General's career.",
        "atAGlance": {
            "appearance": "A tall, broad-shouldered man in his late thirties with a weathered, sun-bronzed countenance, close-cropped steel-grey hair, and a deep, jagged scar running across his left jawline. He wears a dented, unpolished steel cuirass over a coarse wool tunic, salt-stained leather breeches, and heavy riding boots. Around his neck hangs a tarnished silver cord bearing the snapped hilt of his former officer's sword.",
            "mannerisms": "Speaks with quiet, gravelly authority; constantly scans high ground and timberlines with an instinctive cavalryman's eye; refuses to wear gloves, displaying severe burn scars on his palms from saving refugee children from a burning church; treats the PCs with formal military courtesy ('Your Majesties') even while standing behind barricades.",
            "quote": "General Valenza brought you here not to instruct you in the arts of kingship, my young Lieges. He brought you to bathe your white royal hands in the blood of starving dirt-farmers, so that when he commits his next atrocity in Kordova, you will never dare to look upon his iron armor and call him a butcher. I know him. I rode beside him. And I know the price he charges for your survival.",
            "courtDCs": "Morale: 9 (Disciplined military veteran; fights tactically and avoids suicidal posturing; if his men's lives and a royal pardon are guaranteed, Morale drops to 5 for surrender). Initial Reaction: +1 to 2d6 Reaction Rolls when addressing the PCs (Respectful of the crown, but deeply suspicious of Valenza). DC 14 Persuasion / Diplomacy to convince him to parley; DC 16 Warfare / Command Friction to negotiate a tactical compromise; DC 15 Insight to deduce his personal history with Don Rodorigo.",
            "publicStance": "Presents himself as the reluctant defender of a starving border community driven to arms by corrupt bailiffs and brutal army quartermasters.",
            "secretAgenda": "Wants to secure royal pardons and food for the village, then quietly disappear across the border into Velasco. Above all, he wants to ensure that the sealed parchment proving Rodorigo's Period VII war crimes is placed safely in the hands of someone who can hold the warlord accountable.",
            "rival": "General Don Rodorigo de Valenza (Former commanding officer and blood-enemy) & High Chancellor Marquis Murzio de Sadoria",
            "classLevel": "6th-Level Fighter (Veteran Vanguard Captain)",
            "combatStats": "AC 3 (AAC 16) | HP 36 | THAC0 15 | Atk +7 (1d8+3 bastard sword 'La Penitencia') or +6 (1d6+2 heavy military crossbow) | Saves: 10/11/12/13/14"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">La Hermandad de las Espinas &bull; Military Commander</span>
    <span class="badge" style="background: rgba(192, 57, 43, 0.2); border-color: #c0392b; color: #e74c3c;">Ex-Royal Vanguard Officer (Period VII)</span>
    <span class="badge rival-badge">Primary Rival: General Don Rodorigo de Valenza</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A rugged, battle-hardened veteran of thirty-eight with a square jaw, hawkish grey eyes, and a prominent sabre scar tracing from his left ear to his chin. His hair is cropped short in the imperial cavalry fashion, silvered at the temples. He wears an old blackened steel breastplate stripped of all royal regalia, heavy leather brigandine sleeves, and a wool cloak dyed the color of river clay. A broken silver hilt dangles from a leather thong at his throat.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Maintains rigid military posture; speaks in a low, measured baritone without raising his voice; habitually rests his thumb in the notch of his sword belt; flinches when church bells toll, recalling the burning of the southern sanctuaries during the civil war; displays unfailing, formal deference to the PC monarchs while addressing Don Rodorigo with icy contempt.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;General Valenza brought you here not to instruct you in the arts of kingship, my young Lieges. He brought you to bathe your white royal hands in the blood of starving dirt-farmers, so that when he commits his next atrocity in Kordova, you will never dare to look upon his iron armor and call him a butcher. I know him. I rode beside him. And I know the price he charges for your survival.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 9 (Hardened soldier; will not break under terror tactics, but is deeply invested in the survival of his people. If the PCs offer a binding royal decree guaranteeing bread, pardon, and protection for the refugee orphans, he will willingly surrender his own neck to spare the village). Initial Reaction: +1 on 2d6. DC 14 Persuasion to open parley; DC 16 Warfare check to counter his bridge defenses; DC 15 Insight to uncover his hidden connection to Rodorigo.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Capitán Androvo 'The Broken' de Ojedo</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Commander of the Salt-Gate &bull; Ex-Lieutenant of the Royal Caballeros &bull; Lawful Neutral (Disciplined soldier bound by personal honor, scarred by moral revulsion at war crimes)</div>
    </div>
    <span class="stat-class-level">⚔️ 6th-Level Fighter (Veteran Vanguard Captain)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 3 (AAC 16) <small class="text-dim">(Blackened Breastplate AC 5, Large Steel Buckler -1 AC, DEX 14 (-1 AC))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 6d8+6 (+1 CON bonus) &bull; <span style="color: #2ecc71; font-weight: 700;">36 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 90' (30') in field armor / Mounted 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 15 (Base Attack Bonus +5)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +7 to hit (<em>"La Penitencia"</em> +1 Toledo bastard sword, 1d8+3 one-handed or 2d4+4 two-handed); Ranged: +6 to hit (Heavy Arbalest / Military Crossbow, 1d8+2 piercing, range 80/160/240); Off-hand: +6 to hit (Forged salt-spike dagger, 1d4+2 piercing)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box">
      <div class="stat-ability-label">STR</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 to hit &amp; damage</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">DEX</div>
      <div class="stat-ability-score">14</div>
      <div class="stat-ability-mod">+1 missile to hit, -1 AC</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">+1 HP per Hit Die</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">14</div>
      <div class="stat-ability-mod">+1 language / tactical lore</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">12</div>
      <div class="stat-ability-mod">Normal</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 loyalty / reaction (+1 to recruit/command)</div>
    </div>
  </div>

  <div class="stat-section-title">Saving Throws (Labyrinth Lord 5-Column)</div>
  <div class="stat-saves-bar">
    <div class="stat-save-box" title="Breath Weapon (BW)">
      <div class="stat-save-label">BW</div>
      <div class="stat-save-val">12</div>
    </div>
    <div class="stat-save-box" title="Poison or Death (P/D)">
      <div class="stat-save-label">P/D</div>
      <div class="stat-save-val">10</div>
    </div>
    <div class="stat-save-box" title="Petrify or Paralyze (PP)">
      <div class="stat-save-label">PP</div>
      <div class="stat-save-val">11</div>
    </div>
    <div class="stat-save-box" title="Wands (W)">
      <div class="stat-save-label">W</div>
      <div class="stat-save-val">12</div>
    </div>
    <div class="stat-save-box" title="Spells (S)">
      <div class="stat-save-label">S</div>
      <div class="stat-save-val">13</div>
    </div>
  </div>

  <div class="stat-section-title">Combat Tactics &amp; Command Traits</div>
  <p><strong>Master of Defense:</strong> All rebel defenders within 30' of Androvo receive a +1 bonus to Morale and +1 to saving throws against fear and panic.<br>
  <strong>Anticipate Rodorigo's Playbook:</strong> Having served five years under Don Rodorigo, Androvo automatically recognizes every signal trumpet call and cavalry flanking tactic employed by the royal army, granting his defenders +2 to AC against the initial cavalry charge.</p>
</div>

<h3>Public Persona</h3>
<p>To the villagers and refugees of San Severo, Androvo is their protector—a stern, sorrowful guardian who stood between them and the lash of the crown's tax bailiffs. He lives in a small room behind the village forge, never touches strong drink, and spends his evenings whittling wooden toys for the refugee orphans sheltered at the chapel.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE BLOOD-STAINED LEDGER</div>
  <p><strong>The Proof of Rodorigo's Crime:</strong> Buried beneath the altar stone of <em>La Capilla de los Afligidos</em>, inside a sealed wax-and-lead cylinder, Androvo holds the original written dispatch from the final month of the Restoration Civil War. Signed with General Don Rodorigo's personal signet ring (a crowned lion biting an iron spear), the decree explicitly orders Androvo's vanguard to <em>'intercept the convoy of Church negotiators at the Rio Salado ford, execute all thirty priests and envoys without quarter, burn their documents, and publicly blame the atrocity upon republican marauders from The Pit.'</em> If the PCs obtain this scroll, they possess the ultimate leverage over Don Rodorigo.</p>
</div>

<h3>Player Interactions &amp; Roleplay Leads</h3>
<ul>
  <li><strong>Parley at the Bridgehead:</strong> If the PCs accompany Don Rodorigo to parley before the barricades, Androvo will refuse to speak with the General, addressing only the young monarchs: <em>&ldquo;Sire! Liege! You wear the crown of Zingara, yet you follow behind a wolf in gilded steel. Look upon this bridge. These are not foreign spies or rebellious grandees. These are your people, starved of salt and bread. Will your reign begin with the slaughter of children?&rdquo;</em></li>
  <li><strong>Secret Night Meeting:</strong> Under cover of darkness, Androvo can send a courier to slip into the royal camp, inviting the PCs to slip past Rodorigo's sentries for a clandestine meeting in the river crypt, offering them the sealed document in exchange for a signed royal charter of protection for the village.</li>
</ul>
""",
        "gmSecrets": "If Don Rodorigo realizes that the PCs have spoken with Androvo in private, he will immediately assume they have learned of his war crimes. He will orchestrate a 'friendly fire' incident or nighttime assassin attack against Androvo's cell before a trial can occur.",
        "relatedIds": [
            "san-severo",
            "valenza",
            "madre-soledad",
            "alcalde-cadenas",
            "hermandad-de-las-espinas",
            "velasco",
            "hook-uprising-san-severo",
            "hook-the-deserters-testimony"
        ]
    }

    # -------------------------------------------------------------
    # 4. NEW NPC ARTICLE: madre-soledad
    # -------------------------------------------------------------
    soledad_article = {
        "id": "madre-soledad",
        "category": "npcs",
        "title": "Madre Soledor 'The Marked'",
        "subtitle": "Gnostic Prophetess of the Border Refugees • Voice of the Afflicted & Emissary to Velasco",
        "tags": ["Royal Court", "NPC", "Cleric", "Church of Nemeth", "Refugees", "San Severo", "Velasco", "Period VIII", "Labyrinth Lord"],
        "aliases": [
            "Madre Soledor",
            "Soledor the Marked",
            "The Marked Mother",
            "Prophetess Soledor",
            "Madre Soledor of the Ford",
            "Hermana Soledor",
            "The Gnostic Prophetess",
            "The Marked Nun"
        ],
        "summary": "An ascetic holy woman and charismatic lay-preacher of the Church of Nemeth who survived imperial inquisitorial branding in Kordova before shepherding three hundred destitute refugees south toward Velasco. Stranded at San Severo, she established a hospital and sanctuary in the village chapel. Believing the Triumvirate's court is hopelessly corrupted by sorcery and state necromancy, she provides the unyielding spiritual fervor behind the uprising and maintains secret communication with the Council of the Pure in Velasco.",
        "atAGlance": {
            "appearance": "A frail, severe woman of forty-five dressed in patched, coarse homespun robes of bleached wool, cinched with a knotted hempen rope. Her face is drawn and pale from relentless fasting, framed by iron-grey hair tucked beneath an austere linen veil. Her hands and wrists bear horrific, raised red scars from imperial branding irons shaped like crowned skulls.",
            "mannerisms": "Never blinks when staring into the eyes of nobility; continually fingers a string of smoothed river-pebbles that serve as a Gnostic prayer rosary; speaks with an eerie, quiet serenity that commands instant silence even in the midst of shouting crowds.",
            "quote": "You come with banners of silk and cavalry of iron, child-kings of Kordova. You think the crown makes you masters of life and breath. But the mud remembers. The blood of thirty thousand slaughtered innocents cries from the ditches between here and the capital. Kill us if you must; our bones will choke your horses, and Velasco will send an ocean of holy fire to wash your throne away.",
            "courtDCs": "Morale: 12 (Fanatical martyr; utterly fearless of physical death, pain, or intimidation; cannot be coerced by violence). Initial Reaction: -3 to 2d6 Reaction Rolls when addressing the PCs (Condemns the court as necromantic blasphemers). DC 17 Diplomacy / Theology to convince her that the PC monarchs genuinely seek justice; DC 15 Insight to realize her uncompromising stance is driven by ferocious maternal love for the refugee orphans.",
            "publicStance": "Presents herself as the humble servant of God and the poor, demanding that the crown cease all persecution, dismantle its zombie pits, and feed the hungry.",
            "secretAgenda": "Wants to secure safe transit for the three hundred refugees to Velasco. She has already summoned an armed river warband from Velasco's Council of the Pure and intends to hold the bridge until the holy warriors arrive.",
            "rival": "General Don Rodorigo de Valenza & High Chancellor Marquis Murzio de Sadoria",
            "classLevel": "7th-Level Cleric (Gnostic Contemplative)",
            "combatStats": "AC 6 (AAC 13) | HP 32 | THAC0 15 | Atk +4 (1d6 wooden staff of the saint) | Spells: 1st: Cure Light Wounds (x2), Detect Evil; 2nd: Hold Person (x2), Silence 15' Radius; 3rd: Cure Serious Wounds, Prayer | Saves: 8/9/10/12/11"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Church of Nemeth the Gnostic &bull; Border Refuge Emissary</span>
    <span class="badge" style="background: rgba(142, 68, 173, 0.2); border-color: #8e44ad; color: #9b59b6;">Velasco Refugee Covenant</span>
    <span class="badge rival-badge">Rivals: General Valenza &amp; Master Alchemist Vane</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A gaunt, hollow-cheeked woman of forty-five whose dark, luminous eyes burn with prophetic intensity. She wears an unadorned robe of rough grey frieze tied with a coarse cord of braided horsehair. Her wrists and forearms bear the deep, puckered purple brands of the Kordovan High Inquisition. Across her shoulders hangs a battered leather satchel containing handwritten copies of the Gospel of the Pure.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Keeps her scarred palms held outward in an attitude of continuous prayer; recites scripture in low, hypnotic whispers; places herself physically in front of children or wounded peasants whenever armed soldiers draw near; exhibits complete, terrifying indifference to drawn blades.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;You come with banners of silk and cavalry of iron, child-kings of Kordova. You think the crown makes you masters of life and breath. But the mud remembers. The blood of thirty thousand slaughtered innocents cries from the ditches between here and the capital. Kill us if you must; our bones will choke your horses, and Velasco will send an ocean of holy fire to wash your throne away.&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 12 (Immune to fear; actively embraces the prospect of holy martyrdom). Initial Reaction: -3 on 2d6. Threats of torture or execution instantly fail; DC 17 Charisma (Theology or Persuasion) to find common ground; DC 15 Medicine check to treat an outbreak of swamp ague among the children, which softens her heart and grants +3 to subsequent negotiations.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Madre Soledor 'The Marked'</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Prophetess of the Afflicted &bull; Spiritual Mother of the Border Exodus &bull; Lawful Good (Compassionate toward the wretched, fiercely uncompromising against tyrannical oppression)</div>
    </div>
    <span class="stat-class-level">✨ 7th-Level Cleric of Nemeth the Gnostic</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 6 (AAC 13) <small class="text-dim">(Blessed Woolen Habit AC 8, Holy Icon Reliquary -1 AC, DEX 13 (-1 AC))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 7d6+7 &bull; <span style="color: #2ecc71; font-weight: 700;">32 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 15 (Base Attack Bonus +4)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +4 to hit (<em>"El Báculo de Espinas"</em> ashwood pilgrim's staff, 1d6 bludgeoning) or Holy Touch (1d4 subdual / paralysis vs undead on successful touch attack)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box">
      <div class="stat-ability-label">STR</div>
      <div class="stat-ability-score">10</div>
      <div class="stat-ability-mod">Normal</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">DEX</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">-1 AC bonus</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">14</div>
      <div class="stat-ability-mod">+1 HP per Hit Die</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">Literate (Ancient Gnostic Script)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">17</div>
      <div class="stat-ability-mod">+2 on saves vs. mind-affecting magic</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">16</div>
      <div class="stat-ability-mod">+1 reaction, Morale 12 inspiration</div>
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

  <div class="stat-section-title">Clerical Spells Prepared (Labyrinth Lord Cleric Level 7)</div>
  <p><strong>1st Level (3 slots):</strong> <em>Cure Light Wounds</em> (x2), <em>Detect Evil</em><br>
  <strong>2nd Level (3 slots):</strong> <em>Hold Person</em> (x2), <em>Silence 15' Radius</em><br>
  <strong>3rd Level (1 slot):</strong> <em>Cure Serious Wounds</em> (or <em>Prayer</em>)</p>
</div>

<h3>Public Stance &amp; Spiritual Power</h3>
<p>To the people of San Severo, Madre Soledor is a living saint. Her prayers have reportedly purified brackish salt wells and halted fever epidemics. When she speaks, even battle-hardened deserters drop to their knees. However, her deep hatred of the royal court's necromancy makes her deeply suspicious of the PC Necromancer: she can immediately sense the aura of grave-dirt and soul-binding on anyone who practices the deathless arts.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE VELASCO PIGEON NETWORK</div>
  <p><strong>The Secret Link to Velasco:</strong> Soledor maintains the only active, direct messenger pigeon link between the central borderlands and <em>The Council of the Pure</em> in <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>. If the PCs win her trust, she can serve as their diplomatic conduit to the theocratic government, opening the door to lifting the ruinous salt and wine embargo without bloodshed.</p>
</div>
""",
        "gmSecrets": "Madre Soledor carries in her leather satchel a small silver reliquary containing the mummified finger of Saint Ancillus the Martyr. If touched by a reigning crowned monarch of Zingara who speaks a sincere oath of mercy, the relic radiates a warm golden light that cures all diseases within a 30-foot radius.",
        "relatedIds": [
            "san-severo",
            "velasco",
            "church-of-nemeth",
            "andres-hojeda",
            "alcalde-cadenas",
            "valenza",
            "hook-uprising-san-severo"
        ]
    }

    # -------------------------------------------------------------
    # 5. NEW NPC ARTICLE: alcalde-cadenas
    # -------------------------------------------------------------
    cadenas_article = {
        "id": "alcalde-cadenas",
        "category": "npcs",
        "title": "Alcalde Barzolo Kadenzo",
        "subtitle": "The Beleaguered Bailiff of San Severo • Crown Magistrate Caught in the Vice",
        "tags": ["Royal Court", "NPC", "Noble", "Magistrate", "San Severo", "Restoration Council", "Period VIII", "Labyrinth Lord"],
        "aliases": [
            "Alcalde Kadenzo",
            "Barzolo Kadenzo",
            "Bailiff Kadenzo",
            "Mayor Kadenzo",
            "Don Barzolo",
            "The Mayor of San Severo",
            "The Sweat-Drenched Magistrate"
        ],
        "summary": "The corrupt, thoroughly terrified royal magistrate and customs master of San Severo del Vado. Appointed by High Chancellor Marquis Murzio de Sadoria to squeeze transit taxes from the southern road, Kadenzo was trapped when the village revolted. Held hostage by the rebels, he now wanders the barricades in trembling panic, terrified that Don Rodorigo will hang him for treason and that the peasants will pitch him into the river if he flees.",
        "atAGlance": {
            "appearance": "A plump, soft-handed gentleman of fifty-two with thinning oiled brown hair, watery hazel eyes, and a perpetually sweat-drenched, ruddy forehead. He wears the rumpled remnants of courtly dignity: an ochre velvet doublet with tarnished silver frogs, wine-stained breeches, and a heavy brass chain of municipal office that he constantly clutches to steady his shaking hands.",
            "mannerisms": "Dabs his streaming forehead with a grease-spotted silk handkerchief every ten seconds; flinches violently at the sound of horses whinnying or metal clanking; addresses anyone armed as 'My noble Lord' or 'Most gracious General'; drops to his knees in instant supplication at the first hint of anger.",
            "quote": "Your Majesties! Royal saviors! Merciful crowned monarchs! Tell the General I am a loyal servant of the Restoration! I had nothing to do with this madness! The peasants seized the keys to the granary at scythe-point! They forced me to sign their treasonous petitions! If General Valenza hangs me, who will decipher the toll-ledgers? Who will show your treasury where the hidden customs silver is buried?!",
            "courtDCs": "Morale: 4 (Cowardly bureaucrat; collapses into hysterics under physical threats or harsh shouting); Initial Reaction: Fawning / Desperate (+3 on 2d6 when meeting the PC monarchs; sees them as his only salvation from Rodorigo's gallows). DC 12 Intimidation to extract his hidden ledgers; DC 14 Insight to discover that he personally embezzled forty percent of the border transit taxes.",
            "publicStance": "Presents himself as a blameless, loyal crown servant held hostage by wild religious fanatics and rebellious dirt-farmers.",
            "secretAgenda": "Wants to save his own skin, avoid Don Rodorigo's noose, retrieve his hidden stash of stolen gold and silver from the customs cellar, and flee on a fast mule to Messantia or Argos.",
            "rival": "Capitán Androvo de Ojedo & High Chancellor Marquis Murzio de Sadoria (Fears Sadoria's accounting audits)",
            "classLevel": "2nd-Level Normal Human (Corrupt Bureaucrat)",
            "combatStats": "AC 9 (AAC 10) | HP 7 | THAC0 20 | Atk +0 (1d4 ivory-handled dagger) | Saves: 14/15/16/17/18"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">Restoration Council &bull; Municipal Administration</span>
    <span class="badge" style="background: rgba(243, 156, 18, 0.2); border-color: #f39c12; color: #f39c12;">Customs &amp; Toll Magistrate</span>
    <span class="badge rival-badge">Fears: General Don Rodorigo de Valenza &amp; Chancellor Sadoria</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A portly, nervous man of fifty-two whose bulging belly strains against the seams of an outmoded ochre velvet doublet. His round, pasty face glistens with nervous perspiration, and his thinning grey hair is plastered to his forehead. He wears scuffed kidskin slippers unsuited for muddy barricades and nervously fumbles with a tarnished chain of municipal office around his neck.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Constantly mops his brow and jowls with a soiled lace kerchief; stammers profusely when speaking to military officers; bows so low his belly nearly grazes his knees; nervously glances toward the timber gallows erected by the army sentries on the opposite riverbank.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;Your Majesties! Royal saviors! Merciful crowned monarchs! Tell the General I am a loyal servant of the Restoration! I had nothing to do with this madness! The peasants seized the keys to the granary at scythe-point! They forced me to sign their treasonous petitions! If General Valenza hangs me, who will decipher the toll-ledgers? Who will show your treasury where the hidden customs silver is buried?!&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 4 (Total coward; will confess to anything if a blade is drawn). Initial Reaction: +3 on 2d6 when addressing the PC Triumvirate. DC 12 Intimidation to force him to disclose his hidden emergency treasury; DC 14 Investigation to audit his books and discover evidence of systemic tax-skimming.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Alcalde Barzolo Kadenzo</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Crown Bailiff of San Severo &bull; Neutral Evil (Self-serving, greedy, and cowardly bureaucrat)</div>
    </div>
    <span class="stat-class-level">📜 2nd-Level Normal Human (Municipal Bailiff)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 9 (AAC 10) <small class="text-dim">(Unarmored velvet doublet, DEX 9 (0))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 2d4 &bull; <span style="color: #2ecc71; font-weight: 700;">7 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 90' (30')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 20 (Base Attack Bonus +0)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +0 to hit (Ornamental ivory-handled eating dagger, 1d4-1 piercing)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box"><div class="stat-ability-label">STR</div><div class="stat-ability-score">9</div><div class="stat-ability-mod">Normal</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">DEX</div><div class="stat-ability-score">9</div><div class="stat-ability-mod">Normal</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">CON</div><div class="stat-ability-score">10</div><div class="stat-ability-mod">Normal</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">INT</div><div class="stat-ability-score">13</div><div class="stat-ability-mod">Skilled bookkeeper / corrupt accountant</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">WIS</div><div class="stat-ability-score">8</div><div class="stat-ability-mod">-1 on saving throws vs. magic</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">CHA</div><div class="stat-ability-score">10</div><div class="stat-ability-mod">Normal</div></div>
  </div>

  <div class="stat-section-title">Saving Throws (Labyrinth Lord 5-Column)</div>
  <div class="stat-saves-bar">
    <div class="stat-save-box" title="Breath Weapon (BW)"><div class="stat-save-label">BW</div><div class="stat-save-val">16</div></div>
    <div class="stat-save-box" title="Poison or Death (P/D)"><div class="stat-save-label">P/D</div><div class="stat-save-val">14</div></div>
    <div class="stat-save-box" title="Petrify or Paralyze (PP)"><div class="stat-save-label">PP</div><div class="stat-save-val">15</div></div>
    <div class="stat-save-box" title="Wands (W)"><div class="stat-save-label">W</div><div class="stat-save-val">16</div></div>
    <div class="stat-save-box" title="Spells (S)"><div class="stat-save-label">S</div><div class="stat-save-val">17</div></div>
  </div>
</div>

<h3>The Embezzler's Secret Ledger</h3>
<p>While publicly lamenting the crown's poverty, Barzolo has been systematically falsifying transit tolls along the southern highway for five years. He possesses two sets of parchment ledgers:</p>
<ol>
  <li><strong>The Official Ledger:</strong> Shows miserable returns, claiming trade with Velasco died years ago.</li>
  <li><strong>The Cipher Ledger (Hidden in his mattress):</strong> Proves that over 2,000 gold sovereigns worth of illicit contraband—fine Velascan wine, foreign silks, and unrefined salt—passed through the ford with the active collusion of Chancellor Sadoria's treasury clerks.</li>
</ol>
""",
        "gmSecrets": "Barzolo has buried an iron strongbox beneath the third flagstone to the left of the fireplace in the village customs house. It contains 450 silver pieces, 35 gold sovereigns, and six flawless Velascan pearls worth 50 gold pieces each. He will surrender the location in exchange for the PCs sparing him from Rodorigo's gallows.",
        "relatedIds": [
            "san-severo",
            "valenza",
            "sadoria",
            "andres-hojeda",
            "madre-soledad",
            "hook-uprising-san-severo"
        ]
    }

    # -------------------------------------------------------------
    # 6. NEW PLOT HOOK ARTICLE: hook-uprising-san-severo
    # -------------------------------------------------------------
    hook_uprising_article = {
        "id": "hook-uprising-san-severo",
        "category": "hooks",
        "title": "The Executioner's Crown: The Uprising at San Severo",
        "subtitle": "Border Insurgency, Royal Justice, and the Iron Crucible of Don Rodorigo",
        "tags": ["Plot Hook", "Military", "San Severo", "Rebellion", "Valenza", "Velasco", "Refugees", "Period VIII"],
        "aliases": [
            "The Executioner's Crown",
            "The Uprising at San Severo",
            "San Severo Uprising",
            "The Salt Gate Rebellion",
            "The Trial of San Severo"
        ],
        "summary": "General Don Rodorigo de Valenza brings the PC Triumvirate to the besieged border village of San Severo del Vado, demanding they personally preside over the storming of the barricaded bridge and the summary execution of the rebel leaders. The PCs must navigate military ruthlessness, the desperate plight of religious refugees, the approaching warbands of Velasco, and their own sovereign destiny.",
        "content": """
<div class="info-card">
  <p><strong>Involved Factions:</strong> <a href="#factions/military-elite" class="wiki-link">The Military Elite</a>, <a href="#factions/hermandad-de-las-espinas" class="wiki-link">La Hermandad de las Espinas</a>, <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a>, <a href="#gazetteer/velasco" class="wiki-link">Velasco (The Council of the Pure)</a>, The PC Triumvirate</p>
  <p><strong>Key Locations:</strong> <em>El Puente de los Desamparados</em>, <em>La Capilla de los Afligidos</em>, The Royal Command Pavillion, <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a></p>
  <p><strong>Strategic Rewards:</strong> Secures vital border crossing; averts an all-out holy war with Velasco; recruits an independent veteran border guard; gains royal acclaim (+2 Crown Sovereignty); or gains supreme leverage over General Valenza.</p>
</div>

<h3>1. Narrative Premise &amp; Royal Dilemma</h3>
<p>General Don Rodorigo de Valenza has marched a punitive strike force of two hundred heavy cavalry, armored pikemen, and crossbowmen to the border crossing of <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a>. The village has barricaded the basalt bridge of <em>El Puente de los Desamparados</em>, driven out crown bailiffs, and refused to surrender winter grain or religious refugees.</p>

<p>Having invited the young PC Triumvirate to accompany him to 'display royal resolution to the kingdom,' Rodorigo now places the burden directly upon their shoulders. Erecting three heavy wooden gallows on the riverbank facing the village, Rodorigo presents the young monarchs with three pre-written death warrants bearing the names of <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo de Ojedo</a>, <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor</a>, and <a href="#npcs/alcalde-cadenas" class="wiki-link">Alcalde Barzolo Kadenzo</a>.</p>

<blockquote>
  &ldquo;A king who will not spill blood to defend his law is not a sovereign, Liege—he is merely a corpse awaiting a ditch. The army watches. The Grandees watch. Sign the warrants, order the bridge stormed, and let the realm see that the crown has teeth.&rdquo;
  <br>&mdash; <em>General Don Rodorigo de Valenza</em>
</blockquote>

<h3>2. The Three Strategic Paths &amp; Player Agency</h3>

<div class="hook-card info-card">
  <h4>Path A: The Iron Hand (The Executioner's Crown)</h4>
  <p><strong>Action:</strong> The PCs sign the decrees, sanction the military assault, and order the summary hanging of Androvo, Soledor, and Kadenzo on the bridge parapets.</p>
  <p><strong>Outcome:</strong></p>
  <ul>
    <li><strong>Military Acclaim:</strong> General Valenza is deeply impressed by their cold resolve (+2 Reaction Roll bonus, eliminates Command Friction in the army for 30 days). The royal army secures the border road.</li>
    <li><strong>Catastrophic Political Fallback:</strong> The common folk and peasants of southern Zingara brand the Triumvirate as bloodthirsty butcher-puppets (-2 Crown Sovereignty).</li>
    <li><strong>Holy Retaliation:</strong> The Council of the Pure in <a href="#gazetteer/velasco" class="wiki-link">Velasco</a> permanently declares the Triumvirate an 'anathema to God,' intensifying the salt and wine embargo and dispatching holy assassins to Kordova.</li>
  </ul>
</div>

<div class="hook-card info-card">
  <h4>Path B: The Sovereign's Prerogative (The Royal Pardon &amp; The Salt Accord)</h4>
  <p><strong>Action:</strong> The PCs ride between the parley lines, countermand Rodorigo's assault orders under their supreme constitutional authority, and enter San Severo under royal safe-conduct to negotiate directly with the rebels.</p>
  <p><strong>Outcome:</strong></p>
  <ul>
    <li><strong>The Compromise:</strong> The PCs commute the death sentences, grant a royal pardon to the deserters, convert the village into a demilitarized royal sanctuary, and grant the peasants a permanent 20% dividend on border salt gathering in exchange for reopening the road and acknowledging crown sovereignty.</li>
    <li><strong>Recruiting the Border Guard:</strong> Capitán Androvo swears fealty directly to the Triumvirate, transforming the Brotherhood into an elite, independent frontier ranger company (<em>Los Guardas del Vado</em>) that answers solely to the monarchs, completely bypassing Valenza!</li>
    <li><strong>Velasco Diplomatic Breakthrough:</strong> Impressed by their mercy toward the refugee orphans, Madre Soledor uses her pigeon network to open official peace talks with Velasco, offering a path to end the salt famine in Kordova.</li>
    <li><strong>Friction with Rodorigo:</strong> Valenza is enraged by the slight to his military authority (DC 16 <a href="#rules/pundonor" class="wiki-link">Pundonor</a> check to soothe his aristocratic pride without provoking a duel or mutiny).</li>
  </ul>
</div>

<div class="hook-card info-card">
  <h4>Path C: The Shadow Gambit (The Faked Executions &amp; The Blackmail Extraction)</h4>
  <p><strong>Action:</strong> The PCs use stealth, necromancy, or alchemical trickery to appear to comply with Don Rodorigo while secretly spiriting Androvo and the secret documents away.</p>
  <p><strong>Outcome:</strong></p>
  <ul>
    <li>Using an alchemical feign-death draught (provided by <a href="#npcs/escovedo" class="wiki-link">Dr. Horasto Escovador</a>) or substituting freshly reanimated corpses disguised as the condemned, the PCs stage the hangings to satisfy Rodorigo's troops, while secretly escorting Androvo and Soledor to safety.</li>
    <li>The PCs secure Androvo's sealed evidence proving Rodorigo's Period VII war crimes, establishing an ironclad blackmail lever over their general.</li>
  </ul>
</div>

<h3>3. Key Challenge Checks &amp; Mechanics</h3>
<ul>
  <li><strong>DC 15 Insight:</strong> Uncover that Don Rodorigo's urgency is driven by personal panic over Androvo's identity, not military strategy.</li>
  <li><strong>DC 16 Warfare / Command Friction:</strong> Identify fatal flaws in Rodorigo's frontal bridge-assault plan (the hidden sulfur-pitch pots) and propose a flanking maneuver that saves soldiers' lives.</li>
  <li><strong>DC 17 Persuasion / Pundonor:</strong> Force Rodorigo to stand down his cavalry without impugning his martial honor before his officers.</li>
  <li><strong>DC 15 Stealth / Infiltration:</strong> Navigate the river reeds and pre-Cataclysmic drainage conduits beneath the bridge to enter San Severo undetected.</li>
</ul>

<h3>4. Dynamic Escalation Trigger</h3>
<p class="escalation"><strong>The Horns of Velasco (The 12-Hour Clock):</strong> Madre Soledor's messenger pigeon reached Velasco. An armed river war-cog carrying eighty holy warrior-monks (<em>Los Flagelantes del Mar</em>) under Father Barzolo the Unforgiving will arrive at the river ford in exactly 12 hours. If the bridge is still besieged or blood has been spilled when the war-cog arrives, an uncontrollable three-way battle will erupt, plunging Zingara into total civil war.</p>
""",
        "gmSecrets": "If the PCs resolve the crisis peacefully and recruit Androvo, he reveals that Rodorigo's chief cavalry captain, Capitán Ferrugo, is a secret member of the underground republican movement who was waiting for the right moment to defect.",
        "relatedIds": [
            "san-severo",
            "valenza",
            "andres-hojeda",
            "madre-soledad",
            "alcalde-cadenas",
            "hermandad-de-las-espinas",
            "velasco",
            "church-of-nemeth",
            "hook-the-deserters-testimony",
            "state-of-the-realm"
        ]
    }

    # -------------------------------------------------------------
    # 7. NEW PLOT HOOK ARTICLE: hook-the-deserters-testimony
    # -------------------------------------------------------------
    hook_deserter_article = {
        "id": "hook-the-deserters-testimony",
        "category": "hooks",
        "title": "The Deserter's Confession: Rodorigo's Blood-Stained Ledger",
        "subtitle": "A Civil War Atrocity Exposed & The Warlord's Secret Vulnerability",
        "tags": ["Plot Hook", "Intrigue", "San Severo", "Valenza", "Pundonor", "Period VII", "Blackmail"],
        "aliases": [
            "The Deserter's Confession",
            "Rodorigo's Blood-Stained Ledger",
            "The Sealed Dispatch of the Ford",
            "Androvo's Secret",
            "The War Crime of Rio Salado"
        ],
        "summary": "Capitán Androvo de Ojedo secretly possesses the original, wax-sealed military order written by General Don Rodorigo de Valenza during the Restoration Civil War commanding the massacre of a neutral church peace delegation. If the PCs can recover this document before Rodorigo's strike teams destroy it, they gain absolute blackmail leverage to neutralize the General's coup threats.",
        "content": """
<div class="info-card">
  <p><strong>Involved Factions:</strong> The PC Triumvirate, <a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a>, <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo de Ojedo</a>, <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a></p>
  <p><strong>Key Locations:</strong> The Subterranean Crypt of <em>La Capilla de los Afligidos</em>, <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a></p>
  <p><strong>Strategic Reward:</strong> Absolute political blackmail leverage over General Don Rodorigo de Valenza, permanently preventing him from staging a military coup or threatening the Triumvirate under Pundonor.</p>
</div>

<h3>1. Narrative Premise</h3>
<p>During the parley at the bridgehead of San Severo, <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo de Ojedo</a> secretly passes a coded message or gestures toward the village chapel. If the PCs arrange a covert audience with him in the crypts of <em>La Capilla de los Afligidos</em>, Androvo reveals why Don Rodorigo is so frantic to hang him without a public trial.</p>

<p>Androvo was the officer who received General Rodorigo's infamous <strong>Dispatch of the Black River</strong> during Period VII. In that sealed document, Rodorigo ordered his vanguard to ambush and butcher thirty unresisting Church emissaries carrying peace terms, burn their corpses in a lime pit, and plant forged republican pamphlets on the bodies to justify continuing the war. Androvo refused the order, broke his sword, and fled with the original parchment.</p>

<h3>2. The Extraction Mission</h3>
<p>The document is hidden in a lead scroll-case inside the hollowed altar-stone of Saint Severo. However, retrieving it presents multiple hazards:</p>
<ul>
  <li><strong>Rodorigo's Inquisitors:</strong> Don Rodorigo has ordered four trusted hound-masters and ten elite dismounted caballeros to encircle the chapel the moment the bridge is breached, under strict orders to <em>'burn the chapel to the ground and let no one leave alive.'</em></li>
  <li><strong>The Crypt Wards:</strong> The crypt is protected by ancient pre-Cataclysmic guardian traps: a swinging scythe pendulum (DC 14 Reflex / Dexterity check to avoid 2d8 damage) and a glyph of blinding flash (DC 13 Save vs. Spells).</li>
  <li><strong>The Clock:</strong> Rodorigo intends to launch his assault at dawn. The PCs have four hours of darkness to slip into the village, retrieve the parchment, and decide Androvo's fate.</li>
</ul>

<h3>3. How the PCs Can Use the Evidence</h3>
<div class="hook-card info-card">
  <h4>Option 1: The Sovereign's Leash (Blackmail)</h4>
  <p>The PCs confront Don Rodorigo in his private command tent with the sealed dispatch. Facing absolute public dishonor and trial under royal <a href="#rules/pundonor" class="wiki-link">Pundonor</a>, Rodorigo's arrogant defiance collapses. He agrees to recognize the PCs' absolute command over the royal garrisons, accept a permanent royal veto over troop movements, and spare the village.</p>
</div>

<div class="hook-card info-card">
  <h4>Option 2: The Righteous Purge</h4>
  <p>The PCs present the document before the assembled Grandees and the Restoration Council in Kordova, stripping Rodorigo of his rank and arresting him for high treason. However, this risks triggering a violent mutiny among his fiercely loyal heavy cavalry unless the PCs have secured their own independent troops.</p>
</div>
""",
        "gmSecrets": "If Chancellor Marquis Murzio de Sadoria discovers the PCs possess this document, he will attempt to steal or buy it from them, seeking to use it to puppet Don Rodorigo himself.",
        "relatedIds": [
            "san-severo",
            "valenza",
            "andres-hojeda",
            "madre-soledad",
            "sadoria",
            "pundonor",
            "hook-uprising-san-severo"
        ]
    }

    # Add the 7 new articles
    data['articles'].append(san_severo_article)
    data['articles'].append(hermandad_article)
    data['articles'].append(andres_article)
    data['articles'].append(soledad_article)
    data['articles'].append(cadenas_article)
    data['articles'].append(hook_uprising_article)
    data['articles'].append(hook_deserter_article)

    print("Added 7 new articles: san-severo, hermandad-de-las-espinas, andres-hojeda, madre-soledad, alcalde-cadenas, hook-uprising-san-severo, hook-the-deserters-testimony!")

    # -------------------------------------------------------------
    # 8. CROSS-LINKING & ENRICHING EXISTING ARTICLES
    # -------------------------------------------------------------

    # A. Update General Don Rodorigo de Valenza (valenza)
    valenza_art = next((a for a in data['articles'] if a['id'] == 'valenza'), None)
    if valenza_art:
        expedition_section = """
<h3>The San Severo Expedition &amp; The Royal Campaign March</h3>
<p>In response to the armed uprising at <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a>, General Don Rodorigo has mobilized a two-hundred-strong punitive strike force composed of his elite <em>Caballeros de Sangre</em> (heavy cavalry in mirror-polished steel plate), armored pikemen, and heavy crossbowmen. To test the mettle of the young PC Triumvirate, Rodorigo has brought the monarchs along on campaign—ostensibly to display royal majesty and instruct them in 'the iron arithmetic of state survival.'</p>

<h4>1. Life on Campaign with Don Rodorigo</h4>
<p>Observing Don Rodorigo on the march reveals a military commander of terrifying discipline and unyielding stamina:</p>
<ul>
  <li><strong>The Iron Routine:</strong> Rodorigo rises two hours before dawn, personally inspects the horse lines, and executes camp looters without trial to enforce absolute order. He sleeps in his field cuirass on a folding canvas cot, draped in black wolf-fur.</li>
  <li><strong>Campfire Dilemmas:</strong> Each evening, Rodorigo invites the PC Triumvirate to his command pavilion to share roasted mutton and austere red wine. He relentlessly probes their political philosophy, posing tactical and moral conundrums:
    <blockquote>
      &ldquo;A king must balance three daggers on his fingertips: the army, the nobility, and the bread-mob. Which blade do you drop first when your horse stumbles, Liege?&rdquo;
    </blockquote>
  </li>
  <li><strong>Testing the Triumvirate:</strong> Rodorigo subtly evaluates each monarch. He challenges martial PCs to sunrise sparring bouts with blunted broadswords; he coldly quizzes magic-using PCs on how many fallen cavalry mounts they could reanimate to pull baggage wagons; and he watches constantly to see if they flinch at the sight of iron and blood.</li>
</ul>

<h4>2. Secret Terror: Capitán Androvo de Ojedo</h4>
<p>Beneath his unyielding composure, Rodorigo harbors a hidden panic: the rebel commander at San Severo is his former cavalry lieutenant, <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo 'The Broken' de Ojedo</a>. Androvo possesses the original sealed order proving Rodorigo ordered the massacre of a church peace delegation in Period VII. Rodorigo is desperate to ensure Androvo is killed during the assault before he can speak with the young monarchs.</p>
"""
        if 'The San Severo Expedition &amp; The Royal Campaign March' not in valenza_art['content']:
            valenza_art['content'] += expedition_section
            print("Updated valenza with San Severo Expedition and Campfire Lore!")
        for rid in ['san-severo', 'hermandad-de-las-espinas', 'andres-hojeda', 'madre-soledad', 'alcalde-cadenas', 'hook-uprising-san-severo', 'hook-the-deserters-testimony']:
            if rid not in valenza_art.get('relatedIds', []):
                valenza_art.setdefault('relatedIds', []).append(rid)

    # B. Update Velasco (velasco)
    velasco_art = next((a for a in data['articles'] if a['id'] == 'velasco'), None)
    if velasco_art:
        velasco_border_section = """
<h3>The Northern Border Choke-Point: San Severo del Vado</h3>
<p>Between Velasco and Kordova lies the strategic border settlement of <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a>, spanning the Rio Salado along the ancient salt highway. When tens of thousands of religious refugees fled the capital during Period VII, hundreds of wounded and elderly collapsed at San Severo and were sheltered by the villagers. Today, the village has risen in armed revolt under <a href="#factions/hermandad-de-las-espinas" class="wiki-link">La Hermandad de las Espinas</a>, resisting royal grain requisitions.</p>

<p><em>The Council of the Pure</em> in Velasco regards the defense of San Severo as a holy obligation. Informed by <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor</a>, the Council has dispatched an armed war-cog and eighty fanatical warrior-monks (<em>Los Flagelantes del Mar</em>) up the river. If <a href="#npcs/valenza" class="wiki-link">General Valenza</a> assaults the village, it will spark an all-out, catastrophic war between the Velascan Theocracy and the Crown of Kordova.</p>
"""
        if 'The Northern Border Choke-Point: San Severo del Vado' not in velasco_art['content']:
            velasco_art['content'] += velasco_border_section
            print("Updated velasco with San Severo border connection!")
        for rid in ['san-severo', 'hermandad-de-las-espinas', 'andres-hojeda', 'madre-soledad', 'hook-uprising-san-severo']:
            if rid not in velasco_art.get('relatedIds', []):
                velasco_art.setdefault('relatedIds', []).append(rid)

    # C. Update Church of Nemeth (church-of-nemeth)
    church_art = next((a for a in data['articles'] if a['id'] == 'church-of-nemeth'), None)
    if church_art:
        church_border_section = """
<h3>The Border Sanctuaries &amp; The Covenant of San Severo</h3>
<p>While the Church operates in deep secrecy within Kordova under <a href="#npcs/malachai" class="wiki-link">Father Malachai</a>, and rules openly in <a href="#gazetteer/velasco" class="wiki-link">Velasco</a>, its most vulnerable frontier outpost is <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a>. Here, <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor 'The Marked'</a> has turned the village chapel into a sanctuary for three hundred refugee orphans. The armed uprising of <a href="#factions/hermandad-de-las-espinas" class="wiki-link">La Hermandad de las Espinas</a> represents the living intersection of peasant desperation and Gnostic martyrdom, serving as the frontline buffer between the holy revolution in the south and the warlords of the capital.</p>
"""
        if 'The Border Sanctuaries &amp; The Covenant of San Severo' not in church_art['content']:
            church_art['content'] += church_border_section
            print("Updated church-of-nemeth with San Severo border sanctuary!")
        for rid in ['san-severo', 'madre-soledad', 'hermandad-de-las-espinas', 'velasco', 'hook-uprising-san-severo']:
            if rid not in church_art.get('relatedIds', []):
                church_art.setdefault('relatedIds', []).append(rid)

    # D. Update court-matrix
    matrix_art = next((a for a in data['articles'] if a['id'] == 'court-matrix'), None)
    if matrix_art:
        new_rows = """    <tr>
      <td><strong><a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo de Ojedo</a></strong><br><small>Rebel Commander of San Severo</small></td>
      <td><span class="badge" style="background: rgba(192, 57, 43, 0.2); border-color: #c0392b; color: #e74c3c;">La Hermandad de las Espinas / Ex-Royal Army</span></td>
      <td><strong>Cautious / Honorable Adversary:</strong> Respects the monarchy; despises General Valenza; willing to yield if his people are spared and granted royal pardon.</td>
      <td class="gm-only-cell"><span class="badge gm-badge">SECRETS</span> Holds the sealed Period VII dispatch proving Rodorigo ordered the massacre of a church peace delegation.</td>
      <td><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor 'The Marked'</a></strong><br><small>Gnostic Prophetess of the Refugees</small></td>
      <td><span class="badge" style="background: rgba(142, 68, 173, 0.2); border-color: #8e44ad; color: #9b59b6;">Church of Nemeth / Velasco Refugee Covenant</span></td>
      <td><strong>Fanatical / Hostile Stance:</strong> Condemns the court as corrupt necromancers; willing to embrace martyrdom to protect her 300 refugee orphans.</td>
      <td class="gm-only-cell"><span class="badge gm-badge">SECRETS</span> Secret pigeon link to Velasco's Council of the Pure; summoned an armed relief war-cog arriving in 12 hours.</td>
      <td><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a> &amp; <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/alcalde-cadenas" class="wiki-link">Alcalde Barzolo Kadenzo</a></strong><br><small>Crown Bailiff of San Severo</small></td>
      <td><span class="badge" style="background: rgba(243, 156, 18, 0.2); border-color: #f39c12; color: #f39c12;">Restoration Council / Municipal Bailiff</span></td>
      <td><strong>Desperate / Fawning Supplicant:</strong> Terrified of Rodorigo's gallows and peasant pitchforks; begs the PC monarchs for intervention.</td>
      <td class="gm-only-cell"><span class="badge gm-badge">SECRETS</span> Embezzled 40% of southern transit tolls; has 450 silver pieces and 35 gold sovereigns buried in customs house.</td>
      <td><a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo</a> &amp; <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio de Sadoria</a></td>
    </tr>
"""
        if 'andres-hojeda' not in matrix_art['content']:
            matrix_art['content'] = matrix_art['content'].replace('</tbody>', new_rows + '  </tbody>')
            print("Updated court-matrix with Androvo, Soledor, and Kadenzo!")
        for rid in ['andres-hojeda', 'madre-soledad', 'alcalde-cadenas', 'san-severo', 'hook-uprising-san-severo']:
            if rid not in matrix_art.get('relatedIds', []):
                matrix_art.setdefault('relatedIds', []).append(rid)

    # E. Update gazetteer-matrix
    gaz_matrix = next((a for a in data['articles'] if a['id'] == 'gazetteer-matrix'), None)
    if gaz_matrix:
        severo_row = """    <tr>
      <td><strong><a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a></strong></td>
      <td>Fortified River Crossing / Border Waypoint</td>
      <td>Sole heavy bridge (El Puente de los Desamparados) on Camino del Sur to Velasco, rock salt extraction.</td>
      <td>Barricaded bridgeheads, sulfur pitch pots, angry refugee zealots, approaching Velasco crusaders.</td>
    </tr>
"""
        if 'san-severo' not in gaz_matrix['content']:
            gaz_matrix['content'] = gaz_matrix['content'].replace('</tbody>', severo_row + '  </tbody>')
            print("Updated gazetteer-matrix with San Severo del Vado!")
        if 'san-severo' not in gaz_matrix.get('relatedIds', []):
            gaz_matrix.setdefault('relatedIds', []).append('san-severo')

    # F. Update state-of-the-realm
    realm_art = next((a for a in data['articles'] if a['id'] == 'state-of-the-realm'), None)
    if realm_art:
        crisis_row = """    <tr>
      <td><strong>The Border Uprising of San Severo &amp; The General's March</strong></td>
      <td><a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a></td>
      <td><span class="badge" style="background: rgba(192, 57, 43, 0.2); border-color: #c0392b; color: #e74c3c;">MILITARY / BORDER PACIFICATION</span></td>
      <td><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo</a>, <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo</a>, <a href="#npcs/madre-soledad" class="wiki-link">Madre Soledor</a></td>
      <td><a href="#hooks/hook-uprising-san-severo" class="wiki-link">The Executioner's Crown: The Uprising at San Severo</a></td>
      <td>The fortified border crossing between Kordova and Velasco is held by an armed commune of refugees and deserters; General Rodorigo has mobilized the royal army to execute the leaders, bringing the PC Triumvirate along to test their ruthlessness.</td>
    </tr>
"""
        crisis_dossier = """
<h4>Crisis 10: The Border Uprising of San Severo &amp; The General's March</h4>
<div class="crisis-card">
  <div class="crisis-meta">
    <span class="badge" style="background: rgba(192, 57, 43, 0.2); border-color: #c0392b; color: #e74c3c;">SECTOR: MILITARY PACIFICATION &bull; BORDER SOVEREIGNTY</span>
    <span class="threat-level severe">THREAT LEVEL: CRITICAL CIVIL WAR RISK &bull; CRISIS CLOCK: 12 HOURS</span>
  </div>
  <p><strong>The Situation:</strong> Driven past endurance by Kordova's grain seizures and salt monopolies, the border settlement of <a href="#gazetteer/san-severo" class="wiki-link">San Severo del Vado</a> has risen in armed revolt under <a href="#factions/hermandad-de-las-espinas" class="wiki-link">La Hermandad de las Espinas</a>. The rebels—comprising starving peasants, Gnostic religious refugees, and army deserters led by <a href="#npcs/andres-hojeda" class="wiki-link">Capitán Androvo de Ojedo</a>—have fortified the ancient stone bridge of <em>El Puente de los Desamparados</em>. <a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a> has mobilized a punitive strike force of 200 heavy cavalry and infantry to crush the revolt and execute the ringleaders, demanding the PC Triumvirate accompany him and sign the death warrants. Meanwhile, an armed relief war-cog from the theocracy in <a href="#gazetteer/velasco" class="wiki-link">Velasco</a> is navigating upriver, threatening an all-out holy war.</p>
  <p><strong>Strategic Stakes:</strong> Pacifying the crossing peacefully secures the southern trade road, averts a ruinous war with Velasco, recruits an independent frontier guard company, and earns +2 Crown Sovereignty. Botching the expedition triggers an immediate border war with Velasco, brands the monarchs as bloody tyrants, and risks exposing or losing the war crime evidence that could break Rodorigo's political grip.</p>
  <p><strong>Associated Hooks:</strong> <a href="#hooks/hook-uprising-san-severo" class="wiki-link">The Executioner's Crown: The Uprising at San Severo</a> &bull; <a href="#hooks/hook-the-deserters-testimony" class="wiki-link">The Deserter's Confession: Rodorigo's Blood-Stained Ledger</a>.</p>
</div>
"""
        if 'Crisis 10: The Border Uprising of San Severo' not in realm_art['content']:
            if 'The Border Uprising of San Severo &amp; The General\'s March' not in realm_art['content']:
                realm_art['content'] = realm_art['content'].replace('</tbody>', crisis_row + '  </tbody>', 1)
            realm_art['content'] += crisis_dossier
            print("Updated state-of-the-realm with Crisis 10!")
        for rid in ['san-severo', 'andres-hojeda', 'madre-soledad', 'hook-uprising-san-severo']:
            if rid not in realm_art.get('relatedIds', []):
                realm_art.setdefault('relatedIds', []).append(rid)

    # G. Update hooks-index
    hooks_idx = next((a for a in data['articles'] if a['id'] == 'hooks-index'), None)
    if hooks_idx:
        hook_entries = """    <li><strong><a href="#hooks/hook-uprising-san-severo" class="wiki-link">The Executioner's Crown: The Uprising at San Severo</a>:</strong> Ride with General Don Rodorigo de Valenza to suppress an armed uprising of starving peasants, army deserters, and religious refugees at the border ford to Velasco, navigating the general's tests of royal ruthlessness and the ticking clock of approaching holy crusaders.</li>
    <li><strong><a href="#hooks/hook-the-deserters-testimony" class="wiki-link">The Deserter's Confession: Rodorigo's Blood-Stained Ledger</a>:</strong> Extract the sealed war-crime order held by rebel commander Capitán Androvo in the river crypts of San Severo, securing absolute political leverage over General Don Rodorigo de Valenza.</li>
"""
        if 'hook-uprising-san-severo' not in hooks_idx['content']:
            target = '<h4>1. Political Intrigue &amp; Handler Confrontations</h4>\n  <ul>'
            if target in hooks_idx['content']:
                hooks_idx['content'] = hooks_idx['content'].replace(target, target + '\n' + hook_entries)
            else:
                hooks_idx['content'] += '\n' + hook_entries
            print("Updated hooks-index with San Severo plot hooks!")
        for rid in ['hook-uprising-san-severo', 'hook-the-deserters-testimony']:
            if rid not in hooks_idx.get('relatedIds', []):
                hooks_idx.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 9. UPDATE META & WRITE js/data.js
    # -------------------------------------------------------------
    data['meta']['totalArticles'] = len(data['articles'])
    data['meta']['lastUpdated'] = "2026-10-16T10:00:00.000Z"
    print(f"Total articles now: {data['meta']['totalArticles']}")

    output_js = "window.WIKI_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(output_js)
    print("Successfully wrote updated js/data.js!")

    # -------------------------------------------------------------
    # 10. UPDATE data/sessions.json (Add Session 2 & Update Dispositions)
    # -------------------------------------------------------------
    with open('data/sessions.json', 'r', encoding='utf-8') as f:
        sessions = json.load(f)

    # Check if Session 2 already exists
    s2 = next((s for s in sessions if s.get('sessionNumber') == 2), None)
    if not s2:
        session_2 = {
            "sessionNumber": 2,
            "title": "The General's Muster & The Road to the Salt-Gate",
            "realDate": "Session 2 - Current Frontier Expedition",
            "inGameDate": "Month of the Sun, Period VIII (Day 6 of the Triumvirate)",
            "summary": "Stung by ongoing unrest and desperate to enforce martial discipline over the restless borderlands, General Don Rodorigo de Valenza entered the Royal Presence in full battle plate. He delivered grave intelligence: the border settlement of San Severo del Vado—commanding the sole heavy wagon bridge on the southern highway midway between Kordova and the hostile theocratic port of Velasco—has risen in open armed rebellion under La Hermandad de las Espinas. Starving peasants, royal army deserters, and desperate Gnostic religious refugees have barricaded El Puente de los Desamparados, driven out crown bailiffs, and seized the royal granaries. Don Rodorigo announced an immediate punitive expedition of 200 heavy cavalry and infantry to storm the crossing and execute the rebel ringleaders. Refusing to remain cloistered palace puppets under the thumb of High Chancellor Marquis Murzio, the PC Triumvirate made a daring sovereign choice: they ordered their warhorses saddled to personally accompany General Valenza's column. Their goals: present themselves to the kingdom as active, warrior monarchs, learn the realities of the frontier provinces, and scrutinize General Don Rodorigo's tactics, officer corps, and secret motivations up close. As the column marched south across parched scrubland, Rodorigo began testing the young monarchs with ruthless tactical conundrums by the evening campfire, while intelligence hints that the rebel commander is an old ghost from Rodorigo's own blood-soaked past.",
            "sovereigntyPoints": 2,
            "pundonorStatus": "Maintained (Mounted royal progress; martial bearing recognized by caballeros)",
            "activeThreads": [
                "The Executioner's Crown: Rodorigo demands the PCs sign death warrants for Capitán Androvo, Madre Soledor, and Alcalde Kadenzo upon reaching San Severo; the PCs must decide whether to execute, pardon, or engineer a covert compromise.",
                "The Deserter's Ledger: Intelligence suggests rebel leader Capitán Androvo de Ojedo possesses sealed proof of Rodorigo's war crimes from Period VII hidden in the village crypts.",
                "The Velasco Relief Clock: A war-cog carrying 80 fanatical holy warrior-monks from Velasco is sailing up the Rio Salado; the PCs have less than 12 hours upon arrival to prevent an all-out holy war.",
                "The Salt & Grain Accord: San Severo controls the gateway to Velascan salt; negotiating a settlement could alleviate Kordova's salt famine without bloodshed.",
                "The Grain Fleet Summons: Commodore Nikolos Voros and Factor Demetrio Phokas remain in Kordova awaiting the delayed royal grain conference.",
                "The Dean's Necromantic Endowment: Dean Argoto awaits the 500-sovereign endowment to transform the university into a College of Applied Thanatology.",
                "The Revella Tin Gambit: Don Tristao de Revello awaits royal marching orders to reclaim his ancestral tin mines."
            ],
            "npcDispositions": {
                "General Don Rodorigo de Valenza": "Stern Mentor / Secretly Wary (+1 Reaction for mounting the expedition; testing PCs' stomach for blood; terrified Androvo will expose his war crimes)",
                "Capitán Androvo 'The Broken'": "Defiant Commander / Awaiting Parley (Respects the crown; ready to negotiate if his people are spared, but ready to die fighting Valenza)",
                "Madre Soledor 'The Marked'": "Fiery Prophetess (Views court as necromantic heretics; desperately protecting 300 refugee orphans; summoned Velascan relief force)",
                "Alcalde Barzolo Kadenzo": "Terrified Bureaucrat (Trapped hostage; begging PCs for mercy; desperate to save his embezzled silver)",
                "High Chancellor Marquis Murzio de Sadoria": "Uneasy at Palace (Annoyed the PCs left Kordova with the army, outside his financial surveillance)",
                "Capitán-Commodore Nikolos Voros": "Biding Time in Port (Impressed by the PCs' martial display; awaiting grain negotiations)",
                "Don Tristao de Revello y Montalvo": "Sleeping off Hangover (Awaiting the Triumvirate's return from the southern border to march on Revella)"
            }
        }
        sessions.append(session_2)
        print("Logged Session 2: The General's Muster & The Road to the Salt-Gate in data/sessions.json!")

        with open('data/sessions.json', 'w', encoding='utf-8') as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
        print("Successfully updated data/sessions.json!")

    print("\n--- San Severo Border Village & Don Rodorigo Expedition Wiki Expansion Complete! ---")

if __name__ == '__main__':
    main()
