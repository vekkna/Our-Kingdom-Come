"""
add_revella_to_wiki.py
Adds Don Tristán de Revella y Montalbán (the dissolute aristocratic fraternity brother),
his ancestral estate and tin mines in the Valley of Revella, the plot hook 'The Dissolute Baron:
The Tin Lode Gambit', and connects them across existing wiki articles, the court matrix,
the crisis registry, the gazetteer matrix, and data/sessions.json.
"""

import json
import sys

def main():
    print("Starting Revella & Don Tristán Wiki Expansion...")

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
    # 1. NEW NPC ARTICLE: tristan-revella
    # -------------------------------------------------------------
    tristan_article = {
        "id": "tristan-revella",
        "category": "npcs",
        "title": "Don Tristán de Revella y Montalbán",
        "subtitle": "The Dissolute Heir • Dispossessed Baron of Revella & Master of the Deep Lodes • Brother of the Golden Raven",
        "tags": ["Royal Court", "NPC", "Fighter", "Nobility", "Revella", "University", "Fraternity", "Period VIII", "Guarralid", "Tin Mines"],
        "aliases": [
            "Don Tristán de Revella",
            "Tristán de Revella",
            "Don Tristán",
            "The Dissolute Baron",
            "Tristán the Thirsty",
            "The Drunken Baron",
            "El Barón Ahogado",
            "The Last Lord of Revella",
            "Baron of Revella",
            "Lord Tristán",
            "Tristán de Montalbán",
            "The Raven Brother"
        ],
        "summary": "A dispossessed young Grandee and former classmate of the PC Necromancer at the Royal University of Kordava, where both were sworn brothers in the aristocratic fraternity La Cofradía del Cuervo Dorado (The Order of the Golden Raven). Sunk into severe alcoholism following the sack of his ancestral estate and slaughter of his kin during the civil war, Tristán has spent years drinking away his trauma in the squalid taverns of Kordova. Reinstated by the PC to reclaim his ancestral fief of Revella and its vital tin mines, he is a tragicomic liability: brilliant when sober, pathetic when drunk, touchy under pundonor, and entangled in disastrous debts and conflicting schemes.",
        "atAGlance": {
            "appearance": "A once-striking nobleman of twenty-eight with the high aristocratic cheekbones of old Zingara, pale sallow skin, bloodshot amber eyes, and a mop of unwashed, tangled dark curls. He wears a stained, moth-eaten doublet of plum-colored Genoa velvet with frayed gold piping, a lace ruff spotted with red wine and tobacco ash, a single rusted silver cavalry spur, and a battered felt hat sporting a wilted pheasant feather. He smells intensely of sweet fermented grapes, sour sweat, and stale clove pomade.",
            "mannerisms": "Alternates between theatrical fraternity handshakes ('In Sanguine et Calice!') and pathetic, hand-wringing melancholy; constantly fidgets for his leather hip flask or scans the room for unattended flagons; bursts into grandiose, flowery soliloquies about reviving his noble house before begging for silver; when sober, exhibits an astonishingly lethal, lightning-fast dueling reflex that shocks opponents.",
            "quote": "Brother! By the Black Chalice, my royal brother! Look at you in that crystal crown, while I am left to choke on the sour dregs of The Pit! Revella? You speak of Revella! The mountain wind through the chestnut groves! The ringing hammers of the tin smelters! Why, the veins run thick as bull's blood! Give me the royal charter, four good mules, and... perhaps a few barrels of Jerez sack to steady my nerves on the mountain passes, and I swear on our fraternity oath: the tin shall flow to Kordova like a silver river! What could possibly go awry?",
            "courtDCs": "Morale: 6 (Fragile alcoholic; crumbles under direct intimidation, but fights like a cornered cat if his aristocratic pundonor is impugned); Initial Reaction: Enthusiastic / Needy (+2 on 2d6 when meeting the PC Necromancer; views the PC as a miraculous meal-ticket and savior). DC 13 Persuasion or Insight to keep him sober for an audience; DC 15 Medicine / Arcana check to concoct an herbal or alchemical sobriety tonic; DC 16 Diplomacy to audit his fabricated ledgers before he commits the Crown to ruin.",
            "publicStance": "Presents himself as an unjustly ruined Grandee ready to gallantly ride forth and reclaim his ancestral birthright in service to the glorious Triumvirate.",
            "secretAgenda": "Wants to avoid physical labor, military violence, or personal accountability at all costs. Desperately schemes to turn Revella into a pleasure estate and vineyard, using royal zombie thralls to do the dangerous mine work so he can sit in the renovated castle courtyard sipping chilled vintage and hosting collegiate revels.",
            "rival": "High Duke Gonzalo de Guarralid (Ancestral land-grabber), Factor Demetrio Phokas & Marquis Mateo de Sadoria (Mortgage and debt-lien predators), and Foreman Toribio 'El Yunque' (Leader of the squatting mine commune).",
            "classLevel": "5th-Level Fighter (Swashbuckler / Dispossessed Noble)",
            "combatStats": "AC 4 (AAC 15) | HP 28 | THAC0 16 | Atk +6 (1d8+3 rapier 'El Brindis') | Saves: 10/11/12/13/14"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">House Revella &bull; Dispossessed Grandees of the Highlands</span>
    <span class="badge" style="background: rgba(184, 134, 11, 0.2); border-color: #b8860b; color: #d4af37;">Fraternity: La Cofradía del Cuervo Dorado</span>
    <span class="badge rival-badge">Rivals: Duke Gonzalo de Guarralid, Marquis Mateo de Sadoria &amp; Factor Demetrio Phokas</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A slender, once-handsome aristocrat of twenty-eight with fine Zingaran bone structure, hollow sallow cheeks, bloodshot amber eyes, and raven hair falling in tangled, unbrushed curls. He wears the rumpled ruins of courtly splendor: a plum velvet doublet stained with sweet fortified wine and pipe ash, shredded lace cuffs, scuffed cordwain boots missing their left buckle, and a single silver spur. He wears a tarnished gold signet ring whose coat-of-arms (a raven holding a pickaxe) is half-scratched away.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Greets the PC Necromancer with dramatic collegiate secret handshakes, quoting ancient Latin fraternity mottos (*"In Sanguine et Calice, Frater!"*); constantly pats his vest for his monogrammed silver flask; weeps with sentimental nostalgia over past student pranks before abruptly laughing with hysterical fatalism; flinches violently at sudden loud clangs that remind him of mine collapses.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;Brother! By the Black Chalice, my royal brother! Look at you in that crystal crown, while I am left to choke on the sour dregs of The Pit! Revella? You speak of Revella! The mountain wind through the chestnut groves! The ringing hammers of the tin smelters! Why, the veins run thick as bull's blood! Give me the royal charter, four good mules, and... perhaps a few barrels of Jerez sack to steady my nerves on the mountain passes, and I swear on our fraternity oath: the tin shall flow to Kordova like a silver river! What could possibly go awry?&rdquo;</div>
    <div class="glance-item dcs"><strong>Reaction &amp; Morale:</strong> Morale: 6 (Despondent addict; easily bullied when craving wine, but if challenged to a formal duel under <a href="#rules/pundonor" class="wiki-link">Pundonor</a>, his ancestral pride flares into reckless fury, boosting Morale to 10). Initial Reaction: +2 on 2d6 when addressing the PC Necromancer. DC 13 Wisdom/Insight to catch him concealing a bottle or forging a signature; DC 15 Charisma/Diplomacy to sober him up for strategic meetings; DC 14 Medicine check to purge delirium tremens.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Don Tristán de Revella y Montalbán</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Baron of Revella &bull; Master of the High Lodes &bull; Chaotic Neutral (Good-natured affection for fraternity kin, ruined by trauma, chronic alcoholism, and financial irresponsibility)</div>
    </div>
    <span class="stat-class-level">⚔️ 5th-Level Fighter (Swashbuckler / Dispossessed Noble)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 4 (AAC 15) <small class="text-dim">(Buff doublet AC 7, DEX 16 (-2 AC), Ancestral Dueling Ring -1 AC)</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 5d8-5 (-1 CON penalty from liver damage) &bull; <span style="color: #2ecc71; font-weight: 700;">28 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 16 (Base Attack Bonus +4)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +6 to hit (<em>"El Brindis"</em> +1 heirloom Toledo rapier, 1d8+3 piercing, 19-20 critical); Off-hand: +5 to hit (Silver-sheathed main-gauche, 1d4+1 piercing); Ranged: +6 to hit (Heavy silver-chased throwing flask or light wheellock dagger, 1d4+2)</div>
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
      <div class="stat-ability-score">16</div>
      <div class="stat-ability-mod">+2 Attack / -2 AC</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">8</div>
      <div class="stat-ability-mod">-1 HP per HD / Impaired Stamina</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">14</div>
      <div class="stat-ability-mod">+1 Language / High Academic Wit</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">7</div>
      <div class="stat-ability-mod">-1 Save vs. Spells / Terrible Judgment</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 Reaction / Disarming Aristocratic Charm</div>
    </div>
  </div>

  <div class="stat-section-title">Saving Throws (5th-Level Fighter)</div>
  <div class="stat-saves-bar">
    <div class="stat-save-item"><strong>Breath Attacks:</strong> 15</div>
    <div class="stat-save-item"><strong>Poison or Death:</strong> 12</div>
    <div class="stat-save-item"><strong>Petrify or Paralyze:</strong> 14</div>
    <div class="stat-save-item"><strong>Wands:</strong> 15</div>
    <div class="stat-save-item"><strong>Spells or Rods:</strong> 16</div>
  </div>

  <div class="stat-section-title">Combat Quirks &amp; Physical Conditions</div>
  <div style="font-size: 0.88rem; line-height: 1.5; color: var(--text-main); margin-top: 6px;">
    <strong>The Drunken Fencer Reflex:</strong> When moderately intoxicated (1-2 flagons of wine), Tristán gains immunity to fear, +1 on Morale, and an unexpected +2 to Armor Class from erratic, swaying footwork. However, he suffers -2 on all Intelligence and Wisdom checks.<br>
    <strong>Delirium Tremens &amp; The Morning Shake:</strong> If deprived of alcohol for more than 12 hours, Tristán suffers violent physical tremors, inflicting a -2 penalty on attack rolls, Dexterity checks, and armor class until he consumes at least 4 ounces of strong spirits or is cured by a DC 14 Medicine/Heal check.<br>
    <strong>"El Brindis" (The Toast):</strong> Tristán's heirloom +1 rapier. When drawn in high spirits, the hollow pommel chimes like a delicate crystal goblet. Scores a critical hit on natural 19 or 20.<br>
    <strong>Fraternity Blood Oath:</strong> Tristán will never willingly betray or draw steel against a sworn brother of <em>La Cofradía del Cuervo Dorado</em>, even when commanded under magical compulsion (grants +4 bonus on saves to resist betraying the PC).
  </div>
</div>

<h3>4. Narrative Role &amp; The Fraternity Connection</h3>
<p>During their reckless student days at <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>, Don Tristán and the PC Necromancer were initiates of <strong>La Cofradía del Cuervo Dorado (The Order of the Golden Raven)</strong>—an ancient, exclusive aristocratic fraternity whose members swore oaths of lifelong solidarity over flagons of spiced vintage and stolen anatomical treatises. While the PC pursued the deep arcana of thanatology under <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Don Baltasar de Argote</a>, Tristán was celebrated as the fraternity's most flamboyant swordsman, epicure, and poet, famed for scaling the Leaning Spire of Printius at midnight to drape student banners across the armillary sphere.</p>

<p>That gilded youth evaporated during <a href="#history/period-vii" class="wiki-link">Period VII: Restoration Civil War</a>. House Revella, staunch royalists, was ambushed in their highland estate. Tristán's father, Baron Gilberto, and his two elder brothers were slain; their ancestral fortress, <a href="#gazetteer/revella" class="wiki-link">Castillo de Revella</a>, was ransacked; and the lucrative <strong>San Gilberto Tin Mines</strong> were abandoned to rogue deserters and peasant squatters. Tristán fled to Kordova with nothing but his rapier and signet ring. Crushed by survivor's guilt, he took shelter in squalid dives like <em>The Drowned Rat</em> and <em>The Flayed Eel</em> near <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>, drinking himself into daily oblivion on cheap Jerida sack and dregs.</p>

<p>When the PC Necromancer—now co-ruler of Zingara upon the crystal throne—tracked down his old fraternity brother, the player saw an ideal strategic solution: reinstate Don Tristán to his ancestral barony of <a href="#gazetteer/revella" class="wiki-link">Revella</a> by royal decree. By restoring Tristán, the Triumvirate hopes to offload the messy, violent task of pacifying the rebellious highland miners, re-opening the tin mines, and funneling immense mineral revenues directly into the crown coffers without royal hands getting dirty.</p>

<h3>5. Tristán's Schemes, Delusions &amp; Entanglements</h3>
<p>While Tristán wept with gratitude at the PC's feet and swore eternal fealty, his actual plans for Revella bear little resemblance to the industrious mining venture the Triumvirate envisions:</p>
<ul>
  <li><strong>The Vineyard Delusion:</strong> Tristán privately loathes mining—he associates the sound of pickaxes with the siege that killed his family. He dreams of converting the terraced hills of Revella into sprawling vineyards to produce a vintage named <em>El Cuervo Real</em>. He intends to divert royal reconstruction funds into imported grapevine rootstocks from Argos and casks of aging brandy.</li>
  <li><strong>The Demand for Zombie Labor:</strong> Terrified of dealing with the heavily armed, sullen human miners currently occupying the valley, Tristán plans to beg the PC Necromancer for a permanent garrison of 200 obedient, uncomplaining zombie laborers. His logic is characteristically indolent: <em>&ldquo;Corpses do not unionize, brother, they do not ask for wages, and most importantly, they never drink my wine!&rdquo;</em></li>
  <li><strong>The Triple Mortgage Catastrophe:</strong> In a series of alcohol-fueled poker nights over the past two years, Tristán signed away overlapping legal claims to the Revella tin mines to no fewer than three predatory entities:
    <ol>
      <li><strong>To the Argossean Syndicates:</strong> For 50 silver pieces and six casks of Messantian Malmsey, he signed a deed pledging 40% of all future tin output to <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Demetrio Phokas</a> of the Grain Fleet.</li>
      <li><strong>To the Night Guild of Kordova:</strong> To settle a 120-sovereign dice debt to <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrán de Soto</a>, he pledged the toll-gates and river flumes of Revella as collateral.</li>
      <li><strong>To Chancellor Sadoria:</strong> A corrupt treasury notary purchased Tristán's defaulted tax debts for 300 silver pieces, giving <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a> a formal legal warrant to seize the entire estate the moment it becomes productive!</li>
    </ol>
  </li>
</ul>

<h3>6. Levers of Influence, Vulnerabilities &amp; Betrayal Triggers</h3>
<ul>
  <li><strong>The Sobriety Lever:</strong> When supplied with top-shelf spirits, Tristán is endlessly pliant, charming, and cooperative. If kept sober by strict minders or alchemical tonics, his sharp academic intellect re-emerges, allowing him to navigate complex highland boundary laws—but his withdrawal symptoms make him nervous, irritable, and prone to panic attacks.</li>
  <li><strong>Pundonor Baiting:</strong> Despite his beggarly state, Tristán is pathologically sensitive about his ancient lineage. If any Grandee or commoner insults House Revella or questions his martial honor, he will immediately demand satisfaction at rapier point, potentially dragging the Triumvirate into unwanted blood-feuds with powerful neighbors like <a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalo de Guarralid</a>.</li>
  <li><strong>The Black Shaft Phobia:</strong> Tristán harbors an unshakeable, screaming terror of the deep, flooded <em>Black Shaft</em> beneath the San Gilberto mines. Any order requiring him to physically enter the deep shafts requires a DC 16 Charisma check to overcome his hysterics.</li>
</ul>
""",
        "gmSecrets": "Tristán's alcoholism is not merely moral weakness—it is a desperate defense mechanism. On the night his family was massacred, fifteen-year-old Tristán hid in the flooded lowest gallery of the tin mines (The Black Shaft). In the pitch blackness, he pressed his ear to an unworked vein of strange, greasy 'Black Tin' and heard a rhythmic, telepathic pulse whispering ancient pre-Cataclysmic names. Whenever he is completely sober, the whispers return, vibrating inside his teeth. He drinks to drown out the voice of what slumbers beneath Revella.",
        "relatedIds": [
            "revella",
            "hook-the-dissolute-baron",
            "royal-university-of-kordava",
            "dean-baltasar-argote",
            "valeria-morata",
            "sadoria",
            "gonzalo-guarralid",
            "demetrio-phokas",
            "beltran-desoto",
            "joaquin",
            "pundonor",
            "command-friction"
        ]
    }

    # -------------------------------------------------------------
    # 2. NEW GAZETTEER ARTICLE: revella
    # -------------------------------------------------------------
    revella_article = {
        "id": "revella",
        "category": "gazetteer",
        "title": "The Valley & Tin Mines of Revella (El Señorío de Revella)",
        "subtitle": "Craggy Highland Fiefdom • The Deep Lodes of San Gilberto & The Raven's Roost",
        "tags": ["Gazetteer", "Geography", "Revella", "Tin Mines", "Guarralid", "Highlands", "Period VIII", "Economy"],
        "aliases": [
            "Revella",
            "Valley of Revella",
            "Tin Mines of Revella",
            "El Señorío de Revella",
            "Castillo de Revella",
            "San Gilberto Tin Mines",
            "The Deep Lodes of Revella",
            "Barony of Revella",
            "Revella Valley",
            "The Raven's Roost",
            "Mines of Revella",
            "San Gilberto",
            "The Deep Lodes"
        ],
        "summary": "A rugged, mist-shrouded mountain valley nestled in the jagged foothills between the Guarralid Highlands and the upper Thunder River defiles. Famed since Period II for the Deep Lodes of San Gilberto—the richest tin mines in Zingara—Revella was devastated during the Restoration Civil War when House Revella was purged. The ancestral fortress, Castillo de Revella (The Raven's Roost), stands semi-ruined, while the fortified tin mines are held by La Hermandad del Pico (The Brotherhood of the Pick), a hardened commune of deserters and rebel miners who violently resist noble reinstatement.",
        "content": """
<div class="info-card">
  <p><strong>Geographical Type:</strong> Craggy Highland Mountain Valley &bull; Fortified Mining Complex &bull; Alpine Torrent Gorge</p>
  <p><strong>Location:</strong> Western edge of the <a href="#gazetteer/guarralid" class="wiki-link">Guarralid Highlands</a>, overlooking the deep mountain defiles leading down to the lower Thunder River near <a href="#gazetteer/jerida" class="wiki-link">Jerida</a>.</p>
  <p><strong>Strategic &amp; Economic Value:</strong> Contains the <strong>Deep Lodes of San Gilberto</strong>, the preeminent tin deposit in Zingara. Tin is the critical bottleneck for bronze weaponry, artillery casting, bell-foundries, and the galvanic lead-tin solder essential for <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valeria's</a> and <a href="#npcs/vane" class="wiki-link">Master Vane's</a> memory-retaining thralls.</p>
  <p><strong>Current Political Status:</strong> Contested Border Fiefdom. Reinstated by royal decree to <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a>; de facto occupied by an armed miner collective; aggressively coveted by <a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalo de Guarralid</a>; legally encumbered by <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria's</a> debt warrants.</p>
  <p><strong>Primary Hazards:</strong> Mine-shaft collapses, toxic sulfur pockets, entrenched rebel miners armed with blasting powder, mountain ambushes by Duke Gonzalo's retainers, and eldritch whispers from the flooded Black Shaft.</p>
</div>

<h3>1. Geographical Overview &amp; Economic Vitality</h3>
<p>Carved by the churning turquoise waters of the Revella torrent through sheer granite bluffs, the <strong>Valley of Revella</strong> is a dramatic, cloud-capped highland gorge located sixty leagues north-west of <a href="#gazetteer/kordava" class="wiki-link">Kordava</a>. Shrouded in sweet-chestnut forests and wild highland heather, the valley is dominated by towering limestone cliffs riddled with dark mining adits and cascading timber water-flumes.</p>

<p>For four centuries, Revella was one of the wealthiest baronies in Zingara. Its fame rested entirely on the <strong>Deep Lodes of San Gilberto</strong>, an immense underground deposit of high-grade cassiterite (tin ore). In the pre-deluvial economy of Period VIII, tin is infinitely more valuable than ordinary iron:
<ul>
  <li><strong>Military Armament:</strong> Without tin to alloy with copper, neither bronze breastplates, ship-rams, nor cannon-bells can be cast for the royal forces.</li>
  <li><strong>Necromantic Galvanism:</strong> Both <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valeria de Morata</a> and <a href="#npcs/vane" class="wiki-link">Master Vane</a> require dozens of hundredweights of pure tin to forge non-corrosive galvanic spine-plates and nerve-solder for advanced, memory-retaining undead laborers.</li>
  <li><strong>Foreign Trade Leverage:</strong> Tin ingots from Revella are fiercely sought by merchant vessels from the <a href="#gazetteer/kingdom-of-argos" class="wiki-link">Kingdom of Argos</a>, Stygia, and Shem, commanding instantaneous payment in hard silver coin.</li>
</ul>
</p>

<h3>2. Key Valley Locations &amp; Strongholds</h3>
<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Site / Sector</th>
      <th>Physical Description</th>
      <th>Current Occupants &amp; Status</th>
      <th>Key Hazards / Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Castillo de Revella (The Raven's Roost / El Nido del Cuervo)</strong></td>
      <td>A perched granite keep anchored to a pinnacle cliff overlooking the valley entrance. Outer curtain wall intact; Great Hall roof caved in; cellars intact.</td>
      <td>Abandoned shell; roost for mountain condors; occasional bivouac for smuggler trains and bandit scouts.</td>
      <td>Crumbling timber floors (DC 12 DEX save or 2d6 fall); hidden ancestral wine vaults containing twelve sealed amphorae of vintage 80-year-old port.</td>
    </tr>
    <tr>
      <td><strong>The Upper Smelting Terraces &amp; Water Flumes</strong></td>
      <td>Tiered stone platforms with four large stone reverberatory blast furnaces powered by overshot waterwheels fed from the alpine torrent.</td>
      <td>Partially operational. Operated under armed guard by the miner commune to smelt small batches of contraband tin ingots.</td>
      <td>Boiling slag pits; toxic sulfur and arsenic fumes (DC 13 CON save or sickened for 1 hour); heavy wooden gears prone to snagging clothing.</td>
    </tr>
    <tr>
      <td><strong>The Deep Lodes of San Gilberto (Main Adits)</strong></td>
      <td>A sprawling, multi-tiered labyrinth of honeycombed granite tunnels extending over three miles into the mountain root.</td>
      <td>Heavily fortified base of <strong>La Hermandad del Pico</strong>. Barricaded with iron-clad timbers, murder-holes, and rolling rockfall traps.</td>
      <td>Winch-crossbow emplacements; unstable support timbers; pockets of choke-damp gas; rockfall triggers (1d10 bludgeoning damage).</td>
    </tr>
    <tr>
      <td><strong>The Black Shaft (El Pozo Oscuro)</strong></td>
      <td>A sheer, five-hundred-foot vertical drainage shaft plunging into flooded, pre-Cataclysmic lower galleries. Sealed with rusted iron grates since Period IV.</td>
      <td>Completely abandoned by miners, who shun the sector due to superstitious dread and unearthly auditory phenomena.</td>
      <td>Flooded black water; greasy veins of anomalous 'Black Tin'; telepathic madness resonance (DC 14 WIS save or temporary delirium).</td>
    </tr>
  </tbody>
</table>
</div>

<h3>3. The Occupying Power: La Hermandad del Pico</h3>
<p>When House Revella fell during the civil war, the surviving miners, smelter hands, and a contingent of deserted royal pikemen banded together to form <strong>La Hermandad del Pico (The Brotherhood of the Pick)</strong>. Led by a gruff, scarred veteran named <strong>Toribio &ldquo;El Yunque&rdquo; (The Anvil)</strong>, this sixty-man collective operates the upper workings as an egalitarian mountain redoubt.</p>

<p>The Brotherhood fiercely rejects any return to feudal servitude:
<ul>
  <li>They have repelled three separate attempts by <a href="#npcs/gonzalo-guarralid" class="wiki-link">Duke Gonzalo de Guarralid's</a> bailiffs to seize the mines, using mining explosive charges (pulverized sulfur-saltpeter blasts) and rolling granite boulders to crush cavalry in the gorge.</li>
  <li>They sell small consignments of contraband tin to river smugglers from <a href="#gazetteer/jerida" class="wiki-link">Jerida</a> to purchase grain, dried cod, salt, and crossbow bolts.</li>
  <li>If <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán</a> attempts to ride in and simply declare himself Lord of the Manor, Toribio's men will cheerfully hang him from his own castle gatehouse unless the Triumvirate negotiates an equitable profit-sharing charter or provides overwhelming military force.</li>
</ul>
</p>

<h3>4. Geopolitical Encroachment &amp; Strategic Levers</h3>
<p>Revella does not exist in a vacuum. Its re-emergence into royal politics threatens to trigger an explosive regional conflagration:</p>
<ul>
  <li><strong>Duke Gonzalo's Ambition:</strong> The ruler of the neighboring <a href="#gazetteer/guarralid" class="wiki-link">Guarralid Highlands</a> views Revella as his rightful geographic backyard. Gonzalo has already stationed twenty armored caballeros at the border outpost of <em>Paso del Hierro</em>, waiting for an excuse to march in, hang the miners as rebels, and annex the tin veins into his private ducal treasury.</li>
  <li><strong>Chancellor Sadoria's Debt Trap:</strong> <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria</a> holds 1,800 silver pieces in defaulted imperial tax bonds registered against House Revella. The moment royal sovereignty is formally re-established over the estate, Sadoria's tax bailiffs will arrive with crown writs demanding immediate repayment—or the transfer of the mines to Argossean merchant factors.</li>
  <li><strong>The Underworld Connection:</strong> River barges carrying Revella tin down the Thunder River must pass through customs checkpoints controlled by corrupt harbor masters aligned with <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild of Kordova</a> and the <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a>.</li>
</ul>
""",
        "gmSecrets": "Deep inside the flooded Black Shaft lies the submerged alchemical workshop of a Period IV court sorcerer who fled King Daedalus's purges. It contains the legendary 'Crying Crucible of Edmund'—an eldritch bronze refining furnace that can transmute raw cassiterite into 'Living Tin' (an alloy that automatically heals fractures and repels magical rust). However, the crucible is anchored atop an slumbering, tentacled void-spawn that feeds on metal and sanity.",
        "relatedIds": [
            "tristan-revella",
            "hook-the-dissolute-baron",
            "guarralid",
            "jerida",
            "sadoria",
            "gonzalo-guarralid",
            "valeria-morata",
            "vane",
            "industrial-pits"
        ]
    }

    # -------------------------------------------------------------
    # 3. NEW PLOT HOOK ARTICLE: hook-the-dissolute-baron
    # -------------------------------------------------------------
    hook_article = {
        "id": "hook-the-dissolute-baron",
        "category": "hooks",
        "title": "The Dissolute Baron: The Tin Lode Gambit",
        "subtitle": "Reinstating an Addled Fraternity Brother to Seize the Kingdom's Critical Tin Monopoly",
        "tags": ["Plot Hook", "Revella", "Tin Mines", "Economy", "Tristán", "Guarralid", "Pundonor", "Period VIII"],
        "aliases": [
            "The Dissolute Baron",
            "The Tin Lode Gambit",
            "Hook: The Dissolute Baron",
            "Revella Tin Gambit",
            "Reclaiming Revella",
            "The Tin Mines of Revella Hook",
            "The Dissolute Baron of Revella",
            "The Tin Lode Gambit Hook"
        ],
        "summary": "The PC Necromancer's plan to reinstate his dissolute college fraternity brother, Don Tristán de Revella, to his ancestral highland estate promises to secure the kingdom's richest tin mines without royal hands getting dirty. However, the mission is fraught with hilarious, lethal complications: an entrenched miners' commune, Tristán's overlapping debts to the Night Guild and Argossean syndicates, Duke Gonzalo's encroaching mercenaries, and an eldritch corruption awakening in the flooded lower shafts.",
        "content": """
<div class="info-card">
  <p><strong>Quest Sector:</strong> Economic Reconstruction &bull; Feudal Reinstatement &bull; Resource Sovereignty</p>
  <p><strong>Primary Instigator:</strong> The PC Necromancer &amp; <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella y Montalbán</a></p>
  <p><strong>Key Locations:</strong> <a href="#gazetteer/kordava" class="wiki-link">Kordava (The Lower Wards)</a> &rarr; The Thunder River Gorge &rarr; <a href="#gazetteer/revella" class="wiki-link">The Valley &amp; Tin Mines of Revella</a></p>
  <p><strong>Threat Level &amp; Urgency:</strong> MODERATE TO SEVERE. Duke Gonzalo's scouts are already surveying the valley passes, while Chancellor Sadoria's tax bailiffs are preparing foreclosure warrants within 7 days.</p>
  <p><strong>Potential Windfall:</strong> Control of the San Gilberto tin mines generates 80–120 gold sovereigns per month in raw ore revenue, provides essential galvanic alloy for royal thrall production, and breaks the Argossean trade monopoly.</p>
</div>

<h3>1. High-Concept Premise &amp; The Player's Calculation</h3>
<p>Faced with an empty royal treasury and <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo de Sadoria's</a> financial strangulation, the PC Necromancer has formulated an ingenious shortcut: revive the ruined noble house of an old college drinking companion from <em>La Cofradía del Cuervo Dorado</em>. By issuing a royal decree reinstating <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a> as Baron of Revella, the Crown avoids spending royal coin on an expensive military expedition, offloading the gritty burden of pacifying the highland estate and running the dangerous tin mines onto a devoted, indebted friend.</p>

<p>In theory, the plan is elegant statecraft. In reality, it drops the Triumvirate into a swashbuckling hornet's nest of drunken promises, armed peasant rebellions, predatory debt covenants, and ancient cosmic horror.</p>

<h3>2. The Four Cascading Complications</h3>
<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Complication</th>
      <th>The Underlying Problem</th>
      <th>Operational Crisis for the PCs</th>
      <th>Key Resolution Checks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. The Armed Commune</strong></td>
      <td>The tin mines are not sitting empty; they are held by 60 battle-hardened miners and deserters of <em>La Hermandad del Pico</em> under Toribio &ldquo;El Yunque.&rdquo;</td>
      <td>The miners refuse feudal lords. If Tristán struts in demanding oaths of serfdom, the miners will shower him with crossbow bolts and blasting powder.</td>
      <td>DC 15 Diplomacy to negotiate a cooperative crown charter with profit-sharing, or a DC 14 Warfare / Tactical Infiltration check to breach the adits.</td>
    </tr>
    <tr>
      <td><strong>2. The Multi-Creditor Ambush</strong></td>
      <td>While drunk in Kordova, Tristán signed away the mineral rights three times: to <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Demetrio Phokas</a> (Argos), <a href="#npcs/beltran-desoto" class="wiki-link">Don Beltrán de Soto</a> (Night Guild), and Sadoria's treasury clerks.</td>
      <td>The moment the mine is secured, armed debt-collectors from all three factions arrive at Revella demanding their legal share or threatening court foreclosures.</td>
      <td>DC 16 Intimidation / Legal Sleight of Hand check using royal prerogative to void drunken contracts, or paying off key debt tranches (80 silver each).</td>
    </tr>
    <tr>
      <td><strong>3. The Delirium Crisis &amp; The Black Shaft</strong></td>
      <td>Tristán suffers from severe alcoholism and auditory hallucinations. He refuses to go near the mines while sober, and when drunk, he makes catastrophic decisions.</td>
      <td>Tristán's fear is real: the flooded lower shafts house veins of 'Black Tin' resonating with a pre-Cataclysmic entity that triggers madness in sensitive minds.</td>
      <td>DC 14 Medicine / Alchemy to brew a stabilizing sobriety tincture; DC 15 Arcana to construct lead-lined psychic wards around the mine threshold.</td>
    </tr>
    <tr>
      <td><strong>4. The Highland Pundonor Trap</strong></td>
      <td><a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalo de Guarralid</a> sends an arrogant champion to challenge Tristán's noble title at a public mountain inn.</td>
      <td>Under the laws of <a href="#rules/pundonor" class="wiki-link">Pundonor</a>, refusing the duel forfeits the barony's legitimacy; accepting the duel means Tristán might be skewered unless the PCs cheat or bolster him.</td>
      <td>Formal rapier duel mechanics; DC 14 Sleight of Hand to slip a combat buff or poison into the rival's wine; or the PC stepping in as royal champion.</td>
    </tr>
  </tbody>
</table>
</div>

<h3>3. Operational Stages &amp; GM Adventure Flow</h3>

<h4>Stage 1: The Sobering of Don Tristán (Kordova)</h4>
<p>The PCs must track down Tristán in <em>The Drowned Rat</em> or the university gutters, pay off his immediate bar tabs (12 silver pieces), and clean him up for a formal private audience. If the PCs give him royal coin directly, he immediately vanishes for 24 hours on a celebratory bender, requiring a DC 13 Streetwise check to retrieve him from a brothel cellar. The PCs must equip him with a horse, a sober secretary, and a formal Royal Charter of Reinstatement.</p>

<h4>Stage 2: The Mountain Trek &amp; The Border Toll</h4>
<p>Traveling north toward Revella, the expedition must cross the rugged gorges of the upper Thunder River. At the border pass of <em>Paso del Hierro</em>, retainers of <a href="#npcs/gonzalo-guarralid" class="wiki-link">Duke Gonzalo</a> attempt to impose an exorbitant &ldquo;military transit tax&rdquo; of 50 silver pieces. The PCs can flash royal authority (DC 14 Intimidation), out-duel the checkpoint commander, or find a treacherous smugglers' trail guided by <a href="#npcs/joaquin" class="wiki-link">Joaquin 'El Grajo'</a>.</p>

<h4>Stage 3: Parley or Siege at the San Gilberto Mines</h4>
<p>Arriving in Revella, the PCs find <a href="#gazetteer/revella" class="wiki-link">Castillo de Revella</a> in ruins and the mine adits heavily barricaded by <em>La Hermandad del Pico</em>. Toribio &ldquo;El Yunque&rdquo; hoists a black banner and warns the party back:
<ul>
  <li><strong>The Diplomatic Route:</strong> The PCs can offer the miners a revolutionary deal: confirm their personal freedom, pardon their deserter records, and grant the commune a 30% dividend on all smelted tin in exchange for recognizing Don Tristán as nominal governor and sending 50% of production to Kordova. Toribio will accept if the PCs prove they can protect them from Duke Gonzalo (DC 15 Diplomacy check).</li>
  <li><strong>The Martial / Necromantic Route:</strong> The PCs assault the barricades or send a cohort of undead thralls through the flooded water flumes to outflank the defenders. If bloodshed occurs, the valley becomes hostile, and surviving miners sabotage the flumes before fleeing into the mountains.</li>
</ul>
</p>

<h4>Stage 4: Defeating the Debt Collectors</h4>
<p>Just as the smelters begin to churn out glowing ingots of tin, the three debt claimants arrive: an Argossean legal clerk backed by six marine crossbowmen, an enforcer from the Night Guild, and a royal bailiff sent by Marquis Sadoria. The PCs must weave a web of royal edicts, threats of treason, and strategic bribes to dismantle the predatory contracts without triggering an immediate naval trade embargo or underworld vendetta.</p>

<h4>Stage 5: The Horror of the Black Shaft</h4>
<p>With the upper mines secured, strange occurrences begin: miners sleepwalk into the flooded lower tunnels; tin ingots smelted on full moons develop uncanny geometric frost; and Tristán locks himself in the castle cellar, screaming that the &ldquo;Tin God&rdquo; is drinking his blood. The PCs must delve into the submerged <em>Black Shaft</em> to destroy or bind the slumbering eldritch entity before its psychic pulse drives the entire valley into homicidal delirium.</p>

<h3>4. Rewards &amp; Kingdom Sovereignty Outcomes</h3>
<ul>
  <li><strong>Sovereign Economic Windfall:</strong> A pacified, functioning Revella generates <strong>80–120 gold sovereigns per month</strong> for the Crown Treasury, directly funding independent royal guard regiments outside General Valenza's control.</li>
  <li><strong>Necromantic Dominance:</strong> High-grade Revella tin allows <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valeria</a> to outfit 100 royal undead thralls with non-corroding galvanic spine-braces, granting them immunity to damp rot and +2 HP per Hit Die.</li>
  <li><strong>Crown Sovereignty Boost:</strong> Successfully reclaiming an ancient ancestral fiefdom without Council permission grants the Triumvirate <strong>+2 Crown Sovereignty Points</strong> and earns high acclaim among traditional royalist Grandees.</li>
</ul>
""",
        "gmSecrets": "If the PCs completely fail to manage Tristán's drinking and debts, Chancellor Sadoria will use the defaulted Revella contracts to file a formal motion of sovereign financial incompetence before the Grandee Council, legally annexing the mines to the Kingdom of Argos as debt collateral and inflicting a permanent -2 penalty on Crown Sovereignty.",
        "relatedIds": [
            "tristan-revella",
            "revella",
            "royal-university-of-kordava",
            "dean-baltasar-argote",
            "sadoria",
            "gonzalo-guarralid",
            "demetrio-phokas",
            "beltran-desoto",
            "joaquin",
            "pundonor",
            "command-friction",
            "valeria-morata"
        ]
    }

    # Add the new articles
    data['articles'].append(tristan_article)
    data['articles'].append(revella_article)
    data['articles'].append(hook_article)
    print("Added tristan-revella, revella, and hook-the-dissolute-baron!")

    # -------------------------------------------------------------
    # 4. CROSS-LINKING & UPDATES TO EXISTING ARTICLES
    # -------------------------------------------------------------

    # A. Update royal-university-of-kordava
    uni_art = next((a for a in data['articles'] if a['id'] == 'royal-university-of-kordava'), None)
    if uni_art:
        fraternity_section = """
<h3>5. Student Life &amp; Aristocratic Fraternities</h3>
<p>Beneath the scholarly dignity of its lectures, the university has long been home to exclusive noble sodalities and student dining societies. Foremost among these was <strong>La Cofradía del Cuervo Dorado (The Order of the Golden Raven)</strong>—an ancient collegiate fraternity whose initiates included both the PC Necromancer and <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a>. Sworn over silver chalices of fortified wine and stolen arcane grimoires to uphold mutual honor and lifelong solidarity (*&ldquo;In Sanguine et Calice&rdquo;*), the Ravens were notorious for fencing escapades on the university battlements, defying city curfews, and midnight anatomical expeditions into the catacombs. While the civil wars scattered its membership, the fraternal bond remains a potent lever of loyalty across the kingdom.</p>
"""
        if 'La Cofradía del Cuervo Dorado' not in uni_art['content']:
            uni_art['content'] += fraternity_section
            print("Updated royal-university-of-kordava with fraternity lore!")
        for rid in ['tristan-revella', 'revella', 'hook-the-dissolute-baron']:
            if rid not in uni_art.get('relatedIds', []):
                uni_art.setdefault('relatedIds', []).append(rid)

    # B. Update dean-baltasar-argote
    dean_art = next((a for a in data['articles'] if a['id'] == 'dean-baltasar-argote'), None)
    if dean_art:
        tristan_ref = """
<p><strong>The Revella Connection:</strong> Dean Argote remembers <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a> with exasperated fondness as a young man of brilliant natural philosophical talent who squandered his intellect on wine flagons and student duels. However, the Dean is intensely eager for Tristán and the PC to regain the <a href="#gazetteer/revella" class="wiki-link">Tin Mines of Revella</a>: high-purity cassiterite tin is urgently required to construct non-corroding galvanic distillation retorts and alembics for the university's new thanatological laboratory.</p>
"""
        if 'The Revella Connection' not in dean_art['content']:
            dean_art['content'] += tristan_ref
            print("Updated dean-baltasar-argote with Revella connection!")
        for rid in ['tristan-revella', 'revella', 'hook-the-dissolute-baron']:
            if rid not in dean_art.get('relatedIds', []):
                dean_art.setdefault('relatedIds', []).append(rid)

    # C. Update valeria-morata
    valeria_art = next((a for a in data['articles'] if a['id'] == 'valeria-morata'), None)
    if valeria_art:
        tin_ref = """
<p><strong>Material Needs &amp; The Revella Tin Veins:</strong> Valeria's cutting-edge preservation suture-craft requires an unadulterated alloy of lead, silver, and high-grade highland tin to forge non-oxidizing spinal staples and nerve-plates. She has repeatedly petitioned the court to secure the <a href="#gazetteer/revella" class="wiki-link">Tin Mines of Revella</a>, warning that without pure tin, thralls deployed in damp mines or coastal forts will suffer catastrophic joint gangrene within three months.</p>
"""
        if 'Material Needs &amp; The Revella Tin Veins' not in valeria_art['content']:
            valeria_art['content'] += tin_ref
            print("Updated valeria-morata with tin requirements!")
        for rid in ['tristan-revella', 'revella']:
            if rid not in valeria_art.get('relatedIds', []):
                valeria_art.setdefault('relatedIds', []).append(rid)

    # D. Update sadoria
    sadoria_art = next((a for a in data['articles'] if a['id'] == 'sadoria'), None)
    if sadoria_art:
        sadoria_revella = """
<p><strong>The Revella Debt Lever:</strong> Sadoria has quietly acquired over 1,800 silver pieces in defaulted imperial tax bonds encumbering the ancestral barony of <a href="#gazetteer/revella" class="wiki-link">Revella</a>. Unbeknownst to the Triumvirate, Sadoria plans to use these bonds as leverage: if the PCs succeed in restarting the tin mines, Sadoria intends to immediately serve foreclosure writs to confiscate the output as debt servicing for the <a href="#gazetteer/kingdom-of-argos" class="wiki-link">Kingdom of Argos</a>.</p>
"""
        if 'The Revella Debt Lever' not in sadoria_art['content']:
            sadoria_art['content'] += sadoria_revella
            print("Updated sadoria with Revella debt scheme!")
        for rid in ['tristan-revella', 'revella', 'hook-the-dissolute-baron']:
            if rid not in sadoria_art.get('relatedIds', []):
                sadoria_art.setdefault('relatedIds', []).append(rid)

    # E. Update gonzalo-guarralid
    gonzalo_art = next((a for a in data['articles'] if a['id'] == 'gonzalo-guarralid'), None)
    if gonzalo_art:
        gonzalo_revella = """
<p><strong>Encroachment on Revella:</strong> Duke Gonzalo has long eyed the rich cassiterite deposits of the neighboring <a href="#gazetteer/revella" class="wiki-link">Valley of Revella</a>. He has stationed twenty armored retainers at <em>Paso del Hierro</em> to harass border trade, and regards the PC's attempt to reinstate the drunken <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a> as an insolent provocation against his regional hegemony.</p>
"""
        if 'Encroachment on Revella' not in gonzalo_art['content']:
            gonzalo_art['content'] += gonzalo_revella
            print("Updated gonzalo-guarralid with Revella encroachment!")
        for rid in ['tristan-revella', 'revella', 'hook-the-dissolute-baron']:
            if rid not in gonzalo_art.get('relatedIds', []):
                gonzalo_art.setdefault('relatedIds', []).append(rid)

    # F. Update joaquin
    joaquin_art = next((a for a in data['articles'] if a['id'] == 'joaquin'), None)
    if joaquin_art:
        joaquin_revella = """
<p><strong>The Drunken Baron's Tab:</strong> Joaquin is well-acquainted with <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a>, having frequently drunk with him at <em>The Drowned Rat</em>. Joaquin knows that Tristán pawned his family signet ring and signed promissory notes for over 120 gold sovereigns to the Night Guild to cover his gaming debts.</p>
"""
        if "The Drunken Baron's Tab" not in joaquin_art['content']:
            joaquin_art['content'] += joaquin_revella
            print("Updated joaquin with Tristán connection!")
        for rid in ['tristan-revella', 'revella']:
            if rid not in joaquin_art.get('relatedIds', []):
                joaquin_art.setdefault('relatedIds', []).append(rid)

    # G. Update court-matrix
    matrix_art = next((a for a in data['articles'] if a['id'] == 'court-matrix'), None)
    if matrix_art:
        tristan_row = """    <tr>
      <td><strong><a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a></strong><br><small>Dispossessed Baron of Revella</small></td>
      <td><span class="badge" style="background: rgba(184, 134, 11, 0.2); border-color: #b8860b; color: #d4af37;">House Revella / Golden Raven Fraternity</span></td>
      <td><strong>Enthusiastic / Needy Ally:</strong> Sworn fraternity brother to the PC Necromancer; eager to reclaim his ancestral tin mines, though severely impaired by chronic alcoholism and terrified of manual labor.</td>
      <td class="gm-only-cell"><span class="badge gm-badge">SECRETS</span> Signed away mine rights to Argos, the Night Guild, and Sadoria while drunk; drinks to silence the eldritch 'Black Tin' whispers in the deep shaft.</td>
      <td><a href="#npcs/gonzalo-guarralid" class="wiki-link">Duke Gonzalo</a>, <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo</a> &amp; <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Phokas</a></td>
    </tr>
"""
        if 'tristan-revella' not in matrix_art['content']:
            matrix_art['content'] = matrix_art['content'].replace('</tbody>', tristan_row + '  </tbody>')
            print("Updated court-matrix with Don Tristán!")
        for rid in ['tristan-revella', 'revella', 'hook-the-dissolute-baron']:
            if rid not in matrix_art.get('relatedIds', []):
                matrix_art.setdefault('relatedIds', []).append(rid)

    # H. Update gazetteer-matrix
    gaz_matrix = next((a for a in data['articles'] if a['id'] == 'gazetteer-matrix'), None)
    if gaz_matrix:
        revella_row = """    <tr>
      <td><strong><a href="#gazetteer/revella" class="wiki-link">Revella &amp; Tin Mines</a></strong></td>
      <td>Craggy Mountain Valley</td>
      <td>Zingara's richest tin deposits (San Gilberto), bronze armaments, galvanic thrall solder.</td>
      <td>Rebel miner commune, mountain ambushes, collapsing shafts, eldritch Black Tin corruption.</td>
    </tr>
"""
        if 'revella' not in gaz_matrix['content']:
            gaz_matrix['content'] = gaz_matrix['content'].replace('</tbody>', revella_row + '  </tbody>')
            print("Updated gazetteer-matrix with Revella!")
        if 'revella' not in gaz_matrix.get('relatedIds', []):
            gaz_matrix.setdefault('relatedIds', []).append('revella')

    # I. Update state-of-the-realm
    realm_art = next((a for a in data['articles'] if a['id'] == 'state-of-the-realm'), None)
    if realm_art:
        crisis_row = """    <tr>
      <td><strong>The Tin Crisis of Revella &amp; The Dissolute Heir</strong></td>
      <td><a href="#gazetteer/revella" class="wiki-link">Valley &amp; Tin Mines of Revella</a></td>
      <td><span class="badge" style="background: rgba(230, 126, 34, 0.2); border-color: #e67e22; color: #e67e22;">ECONOMIC / FEUDAL RESTITUTION</span></td>
      <td><a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a>, <a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalo</a>, <a href="#npcs/sadoria" class="wiki-link">Marquis Mateo</a></td>
      <td><a href="#hooks/hook-the-dissolute-baron" class="wiki-link">The Dissolute Baron: The Tin Lode Gambit</a></td>
      <td>The kingdom's richest tin mines are controlled by an armed miner commune, coveted by Duke Gonzalo, encumbered by Sadoria's debt liens, and nominally restored to a drunken fraternity brother.</td>
    </tr>
"""
        crisis_dossier = """
<h4>Crisis 9: The Tin Crisis of Revella &amp; The Dissolute Heir</h4>
<div class="crisis-card">
  <div class="crisis-meta">
    <span class="badge" style="background: rgba(230, 126, 34, 0.2); border-color: #e67e22; color: #e67e22;">SECTOR: RESOURCE SOVEREIGNTY &bull; FEUDAL RESTITUTION</span>
    <span class="threat-level severe">THREAT LEVEL: HIGH ECONOMIC OPPORTUNITY &bull; CRISIS CLOCK: 7 DAYS</span>
  </div>
  <p><strong>The Situation:</strong> Facing fiscal starvation, the PC Necromancer has hatched a plan to reinstate his old university fraternity brother, <a href="#npcs/tristan-revella" class="wiki-link">Don Tristán de Revella</a>, to his lost ancestral highland estate of <a href="#gazetteer/revella" class="wiki-link">Revella</a> to seize control of the valuable <strong>San Gilberto Tin Mines</strong>. However, Tristán is a broken alcoholic who signed away overlapping mine deeds to Argossean merchants, the Night Guild, and Chancellor Sadoria's clerks while intoxicated. Furthermore, the mines are held by an armed collective of 60 veteran miners (<em>La Hermandad del Pico</em>) who refuse feudal rule, and <a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalo</a> is massing troops at the pass to annex the valley.</p>
  <p><strong>Strategic Stakes:</strong> Securing the Revella mines generates 80–120 gold sovereigns per month, provides vital tin for bronze cannon casting and non-corroding necromantic thrall solder, and grants +2 Crown Sovereignty. Botching the mission hands the mines to Duke Gonzalo or Argos, discredits the Crown under Pundonor, and risks awakening the cosmic horror lurking in the flooded Black Shaft.</p>
  <p><strong>Associated Hook:</strong> <a href="#hooks/hook-the-dissolute-baron" class="wiki-link">The Dissolute Baron: The Tin Lode Gambit</a>.</p>
</div>
"""
        if 'Crisis 9: The Tin Crisis of Revella' not in realm_art['content']:
            if 'The Tin Crisis of Revella &amp; The Dissolute Heir' not in realm_art['content']:
                realm_art['content'] = realm_art['content'].replace('</tbody>', crisis_row + '  </tbody>', 1)
            realm_art['content'] += crisis_dossier
            print("Updated state-of-the-realm with Crisis 9!")
        for rid in ['tristan-revella', 'revella', 'hook-the-dissolute-baron']:
            if rid not in realm_art.get('relatedIds', []):
                realm_art.setdefault('relatedIds', []).append(rid)

    # J. Update hooks-index
    hooks_idx = next((a for a in data['articles'] if a['id'] == 'hooks-index'), None)
    if hooks_idx:
        hook_entry = """    <li><strong><a href="#hooks/hook-the-dissolute-baron" class="wiki-link">The Dissolute Baron: The Tin Lode Gambit</a>:</strong> Reclaim the kingdom's richest tin mines in the Valley of Revella by reinstating the PC's addled college fraternity brother Don Tristán, navigating rebel miners, predatory Argossean debt claims, and Duke Gonzalo's border mercenaries.</li>
"""
        if 'hook-the-dissolute-baron' not in hooks_idx['content']:
            target = '<h4>2. Economic Recovery &amp; Thrall Labor Crises</h4>\n  <ul>'
            if target in hooks_idx['content']:
                hooks_idx['content'] = hooks_idx['content'].replace(target, target + '\n' + hook_entry)
            else:
                hooks_idx['content'] += '\n' + hook_entry
            print("Updated hooks-index with The Dissolute Baron hook!")
        if 'hook-the-dissolute-baron' not in hooks_idx.get('relatedIds', []):
            hooks_idx.setdefault('relatedIds', []).append('hook-the-dissolute-baron')

    # -------------------------------------------------------------
    # 5. UPDATE META & WRITE js/data.js
    # -------------------------------------------------------------
    data['meta']['totalArticles'] = len(data['articles'])
    data['meta']['lastUpdated'] = "2026-10-15T23:05:00.000Z"
    print(f"Total articles now: {data['meta']['totalArticles']}")

    output_js = "window.WIKI_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(output_js)
    print("Successfully wrote updated js/data.js!")

    # -------------------------------------------------------------
    # 6. UPDATE data/sessions.json (Session 1)
    # -------------------------------------------------------------
    with open('data/sessions.json', 'r', encoding='utf-8') as f:
        sessions = json.load(f)

    s1 = next((s for s in sessions if s.get('sessionNumber') == 1), None)
    if s1:
        tristan_narrative = " In a tavern dive off the University Quadrangle, the player necromancer also made an unexpected, fateful discovery: Don Tristán de Revella y Montalbán, an aristocratic member of his old college fraternity (La Cofradía del Cuervo Dorado). Sunk into dissolute alcoholism and drowning in debts following the slaughter of his family during the civil war, Tristán is the sole surviving heir to the lost mountain estate of Revella. Seeing an audacious opportunity to solve the Crown's crushing resource crisis, the player hatched a plan to reinstate Tristán to his ancestral seat by royal decree, hoping to offload the headache of seizing and managing Revella's immensely valuable tin mines to his indebted fraternity brother. However, complications abound: Tristán's chronic inebriation makes him a volatile liability; the mines are currently fortified by an entrenched rebel miner commune (La Hermandad del Pico); Duke Gonzalo de Guarralid is massing troops at the highland pass to annex the veins; and while drunk, Tristán unwittingly signed away overlapping deeds to the mines to Argossean factors, the Night Guild, and Chancellor Sadoria's treasury clerks."

        if "don tristán de revella" not in s1['summary'].lower() and "don tristan" not in s1['summary'].lower():
            s1['summary'] += tristan_narrative
            print("Enriched Session 1 summary with Don Tristán & Revella discovery!")

        # Active threads
        revella_thread = "The Revella Tin Gambit: Reinstating the PC Necromancer's dissolute fraternity brother, Don Tristán de Revella, to his ancestral highland estate to seize control of the kingdom's richest tin mines before Chancellor Sadoria's Argossean creditors or High Duke Gonzalo annex the veins."
        if revella_thread not in s1['activeThreads']:
            s1['activeThreads'].append(revella_thread)
            print("Added Revella Tin Gambit active thread to Session 1!")

        # NPC Dispositions
        s1['npcDispositions']["Don Tristán de Revella y Montalbán"] = "Devoted Fraternity Brother / Alcoholic Liability (+2 Reaction to PC, Bound by Raven Fraternity Oath, Prone to Drunken Panic & Multi-Signed Debts)"

        with open('data/sessions.json', 'w', encoding='utf-8') as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
        print("Successfully updated data/sessions.json!")

    print("\n--- Revella & Don Tristán Wiki Expansion Complete! ---")

if __name__ == '__main__':
    main()
