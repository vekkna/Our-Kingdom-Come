"""
add_drowned_rat_to_wiki.py
Expands the Our Kingdom Come campaign wiki with:
1. Gazetteer Entry: The Drowned Rat Tavern (the-drowned-rat)
2. NPC Entry: Old Mother Vespera (madre-vespera)
3. NPC Entry: Pale Beatriza (beatriz-la-palida) - The Zombie Barmaid
4. Updates cross-links and relatedIds across:
   - Joachor 'The Jackdaw' Valiento (joaquin)
   - Don Tristao de Revello (tristan-revella)
   - The Night Guild of Kordova (kordovan-thieves-guild)
   - The Pit (the-pit)
   - Kordava (kordava)
   - The Velasco Syndicate (velasco-thieves-guild)
   - Maestra Valessa de Morato (valeria-morata)
   - Royal University of Kordava (royal-university-of-kordava)
"""

import json
import sys

def main():
    print("Starting The Drowned Rat Tavern Wiki Expansion...")

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
    # 1. NEW GAZETTEER ARTICLE: the-drowned-rat
    # -------------------------------------------------------------
    drowned_rat_article = {
        "id": "the-drowned-rat",
        "category": "gazetteer",
        "title": "The Drowned Rat Tavern (El Mesón de la Rata Ahogada)",
        "subtitle": "Sinking Relic of the Canal District • Underworld Haven & Sewer Sluice Nexus",
        "tags": ["Gazetteer", "Geography", "Kordava", "The Pit", "Tavern", "The Drowned Rat", "Night Guild", "Session 1", "Period VIII", "Underworld"],
        "aliases": [
            "The Drowned Rat",
            "The Drowned Rat Tavern",
            "La Rata Ahogada",
            "El Mesón de la Rata Ahogada",
            "The Alabaster Swan",
            "El Cisne de Alabastro",
            "Drowned Rat",
            "Drowned Rat Dive"
        ],
        "summary": "A squalid, semi-submerged dive clinging to the ancient stone sewer outfall where Kordova's Lower Ward empties into The Pit. Once an opulent Period V cabaret known as The Alabaster Swan, it is now a waterlogged underworld haven for cutpurses, fences, and smugglers—famed for its one-eyed mistress Old Mother Vespera, its gentle reanimated zombie barmaid Beatriza, and a secret sewer siphon connecting directly to the Night Guild's subterranean cisterns.",
        "content": """
<div class="info-card">
  <p><strong>Establishment Type:</strong> Semi-Submerged Waterfront Tavern, Underworld Neutral Ground &amp; Smugglers' Clearinghouse</p>
  <p><strong>Location:</strong> Lower Ward of <a href="#gazetteer/kordava" class="wiki-link">Kordova</a>, perched over the great sluice outfall where the municipal storm conduits cascade into the sunken ruins of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a></p>
  <p><strong>Proprietress:</strong> <a href="#npcs/madre-vespera" class="wiki-link">Old Mother Vespera ("La Balanza")</a>, veteran fence and retired cabaret dancer</p>
  <p><strong>Notable Staff:</strong> <a href="#npcs/beatriz-la-palida" class="wiki-link">Pale Beatriza</a> (Reanimated Zombie Barmaid), "Gordo" Basilio (Cook, Tapster &amp; Bilge-Pumper)</p>
  <p><strong>Affiliated Factions:</strong> <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild of Kordova</a> (primary street front), <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a> (hostile extortion target), <a href="#factions/republican-insurgents" class="wiki-link">Republican Insurgents</a> (occasional patrons)</p>
</div>

<h3>1. Architecture: From Gilded Salon to Drowned Dive</h3>
<p>In the triumphant reign of King Ancillus I during <a href="#history/period-v" class="wiki-link">Period V</a>, this establishment was celebrated across the Western Ocean as <strong>El Cisne de Alabastro</strong> (<em>The Alabaster Swan</em>)—an opulent two-story waterfront salon where grandees, corsair admirals, and merchant-princes from Argos drank vintage Zingg Malmsey beneath barrel-vaulted ceilings of white marble, crystal teardrop chandeliers, and gilded moldings celebrating naval triumphs. Poets recited sonnets from an elevated cedar gallery, while oyster barges unloaded directly into the tavern's private salt-water basins.</p>

<p>Three centuries of geotechnical subsidence, coastal erosion, and the catastrophic civil wars of <a href="#history/period-vii" class="wiki-link">Period VII</a> dragged the entire canal quarter thirty feet downward. The construction of the city's municipal drainage flues redirected millions of gallons of black sewer runoff directly beneath the foundations. Today, the tavern is a rotting, waterlogged shadow of its former glory:</p>

<ul>
  <li><strong>The Submerged Floor &amp; Plankways:</strong> The white marble flagstones are now permanently slick with black sewer silt and green sea-lichen. At low tide, three to six inches of brackish, foul-smelling canal water sloshes across the floor; at high spring tide, the water rises to mid-calf. Patrons navigate the taproom along a maze of warped, slippery catwalks made of salvaged driftwood, ship's planking, and overturned salt-beef firkins. Anyone falling off the planks must make a <strong>DC 11 Dexterity check</strong> or land face-first in slimy, foul bilge.</li>
  <li><strong>The Desecrated Swan:</strong> Mounted above the salt-caked oak bar is the tavern's namesake relic: the colossal carved figurehead of an alabaster swan, salvaged from an ancient Period IV caravel. Its neck is cracked and reinforced with rusted iron straps; its left eye has been gouged out; and nailed directly through its immaculate breast is the taxidermied, bloated carcass of a giant sewer wharf-rat—the tavern's grim, underworld moniker given physical form.</li>
  <li><strong>The Whaler's Ribs:</strong> The sagging, rotten plaster ceiling has collapsed in multiple places, exposing black rafters reinforced with the bleached rib-bones of a stranded right whale, lashed together with tarred rigging cordage.</li>
  <li><strong>The Atmospheric Scent:</strong> A dense, unmistakable miasma hangs in the humid air: sour vinegar-ale, boiling fish-heads, wet dog, tallow smoke, brackish swamp mud, and drifting over it all, the sweet, eerie fragrance of dried lavender and embalming spices emanating from the tavern's deathless barmaid.</li>
</ul>

<h3>2. Layout &amp; Secret Chambers</h3>
<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Chamber</th>
      <th>Physical Description</th>
      <th>Operational Role &amp; Atmosphere</th>
      <th>Mechanical / Hazard Checks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>The Slanted Taproom</strong></td>
      <td>Twenty-foot-wide hall tilted five degrees toward the water. Heavy trestle tables propped on granite ballast stones.</td>
      <td>Common drinking floor. Cutpurses, off-duty smugglers, dock scavengers, and down-at-heel mercenaries huddle around iron fire-baskets burning peat and dried eel-bones.</td>
      <td>Difficult terrain; running requires DC 12 DEX check or slipping into knee-deep bilge.</td>
    </tr>
    <tr>
      <td><strong>The Sump Booths</strong></td>
      <td>Four recessed alcoves carved from ancient sewer stone, draped with dripping, moldering canvas sails.</td>
      <td>Private negotiation dens. Where <a href="#npcs/joaquin" class="wiki-link">Joachor 'El Grajo'</a> met the PC Triumvirate. Whispered conversations cannot be overheard over the deafening roar of the adjacent sewer sluice.</td>
      <td>Grants +2 on Stealth / Hide in Shadows checks; immune to mundane eavesdropping.</td>
    </tr>
    <tr>
      <td><strong>The Bar &amp; Balanza</strong></td>
      <td>Massive counter carved from a salvaged galleon mast, pitted with knife gouges and coin tests.</td>
      <td>The command post of <a href="#npcs/madre-vespera" class="wiki-link">Old Mother Vespera</a>. Houses her brass scales, three loaded flintlock pistols beneath the rail, and a lead-weighted cudgel. Served by <a href="#npcs/beatriz-la-palida" class="wiki-link">Pale Beatriza</a>.</td>
      <td>Heavy oak bar provides hard cover (+4 AC against missile fire).</td>
    </tr>
    <tr>
      <td><strong>The Galley &amp; Pump Station</strong></td>
      <td>Soot-stained alcove with an iron wood-stove and a massive cast-iron suction pump with a six-foot lever.</td>
      <td>Domain of "Gordo" Basilio. He stirs the perpetual cauldron of "Sump Broth" and pumps bilge water back into the sewer outfall every two hours to keep the tavern from drowning.</td>
      <td>If the pump is disabled, the tavern floor floods by 1 foot every 30 minutes.</td>
    </tr>
    <tr>
      <td><strong>Mother Vespera's Snug</strong></td>
      <td>A dry, cramped wooden cabin suspended eight feet above the taproom, accessible via a retractable rope ladder.</td>
      <td>Vespera's private quarters and counting room. Smells of dried chamomile, pipe weed, and candle wax. Houses her locked iron-bound ledger chest and secret pawned valuables.</td>
      <td>Locked door (DC 16 Open Locks); ladder can be pulled up instantly in a fight.</td>
    </tr>
    <tr>
      <td><strong>The Sluice Siphon (The Night Trap)</strong></td>
      <td>Hidden trapdoor beneath a stack of sour beer hogsheads behind the bar, leading to a submerged granite chute.</td>
      <td>The secret subterranean portal to <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild of Kordova</a>. Drops into a stagnant sewer canal where a muffled flatboat is moored, leading to the <em>Cistern of the Blind Saint</em>.</td>
      <td>Requires guild recognition token or DC 15 Streetwise check to open without triggering an iron deadfall trap (2d6 crushing damage).</td>
    </tr>
    <tr>
      <td><strong>The Flooded Vault of the Swan</strong></td>
      <td>Submerged cellar twenty feet beneath the floorboards, drowned under six feet of black tidal sewage.</td>
      <td>The sealed strongroom from the tavern's Period V golden age. Said to contain the locked sea-chest of Captain Estevar de Morillo, holding pre-Cataclysmic reef charts.</td>
      <td>Completely submerged; requires underwater swimming checks and illumination; inhabited by giant sewer lampreys.</td>
    </tr>
  </tbody>
</table>
</div>

<h3>3. House Offerings &amp; Gutter Customs</h3>
<ul>
  <li><strong>The Bilge Broth (El Caldo del Fondo):</strong> Two copper bits per wooden bowl. A thick, gelatinous, bubbling stew prepared by Gordo Basilio from salt-dogfish heads, split yellow peas, wild canal celery, turnip skins, and generous splashes of vinegar to mask the rancidity. Surprisingly nourishing, but requires a <strong>DC 10 Constitution check</strong> for high-born stomachs to avoid mild nausea.</li>
  <li><strong>The Drowned Pint:</strong> One copper bit. Sour, cloudy ale brewed from grain sweepings discarded at the harbor wharves, cut with brackish water. Leaves a bitter copper tang on the tongue.</li>
  <li><strong>Zingg Aguardiente:</strong> Three silver pieces per horn. Raw, fiery cane rum smuggled from the southern estates, hot enough to strip paint off a galleon's hull. The favored drink of <a href="#npcs/tristan-revella" class="wiki-link">Don Tristao de Revello</a> during his binges.</li>
  <li><strong>The Copper for the Drowned:</strong> Gutter superstition dictates that every patron must flick their first copper bit into the stagnant water pooling around their boots before taking their first drink. The coin sinks into the floor silt "to pay the blind ferryman so he doesn't drag our heels down." At closing time, Pale Beatriza wades through the water with an iron dredge to harvest the coins.</li>
</ul>

<h3>4. Notable Staff</h3>
<ul>
  <li><strong><a href="#npcs/madre-vespera" class="wiki-link">Old Mother Vespera ("La Balanza")</a> — Proprietress &amp; Master Fence:</strong> A sixty-seven-year-old one-eyed underworld veteran who has survived four kings, three sieges, and two plague years. She treats monarchs and cutpurses with equal, biting cynicism and keeps the tavern neutral ground under <em>El Pundonor del Arroyo</em>.</li>
  <li><strong><a href="#npcs/beatriz-la-palida" class="wiki-link">Pale Beatriza</a> — The Undead Barmaid:</strong> The legendary singing barmaid of the tavern who died of canal typhus during the civil war. Reanimated by a renegade university necromancer at Vespera's expense, she glides silently through the flooded taproom in an antique lace apron, powdered with dried lavender, carrying tankards with terrifying undead balance and breaking the bones of rowdy brawlers with 18 Strength rigor mortis.</li>
  <li><strong>"Gordo" Basilio — Cook, Tapster &amp; Bilge-Pumper:</strong> A half-deaf, four-hundred-pound former whaling harpooner missing his left ear and three fingers. Basilio tends the fire, chops fish with a rusted flensing cleaver, and works the bilge pump like a tireless iron engine. If a fight turns lethal, Basilio hurls scalding chowder or swings a heavy oak pump handle (1d8+3 damage).</li>
</ul>

<h3>5. Habitual Patrons &amp; Street Fixtures</h3>
<ul>
  <li><strong><a href="#npcs/joaquin" class="wiki-link">Joachor 'The Jackdaw' Valiento</a>:</strong> The desperate cutpurse who practically lives in the rearmost Sump Booth, nursing a single pint of sour ale for six hours while watching the door for Night Guild enforcers or Velascan assassins.</li>
  <li><strong><a href="#npcs/tristan-revella" class="wiki-link">Don Tristao de Revello y Montalvo</a>:</strong> The PC Necromancer's aristocratic college fraternity brother, frequently found passed out face-down on a corner trestle table, clutching an empty bottle of plum brandy and singing student songs while creditors circle like gulls.</li>
  <li><strong>Tía Moros ("The Harbor Hag"):</strong> An eighty-year-old former smuggler with a narwhal-horn peg leg who sits on a dry salt barrel by the peat stove. She sells waterproof tallow candles, dried marsh tobacco, and flawless tide schedules of the subterranean sea-caves for a few copper bits.</li>
  <li><strong>Cristóbal "El Aguja" (The Needle):</strong> A twitching, ink-stained former copyist dismissed from <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio's</a> treasury for selling tax duplicates. From a dim booth, Cristóbal uses forged seals to draft counterfeit grain manifests, travel passes, and pawn receipts for two silver pieces each.</li>
  <li><strong>"Gato Salado" (Murzio de Velasco):</strong> A silent, scar-faced scout for the <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a>. Clad in salt-stained oilskins, he sips rum near the entrance, covertly recording the faces of Night Guild runners using the sewer trapdoor.</li>
</ul>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE PALACE CHIMNEY &amp; THE SUBMERGED VAULT</div>
  <p><strong>The Alcázar Kitchen Conduit:</strong> The Drowned Rat's cellar connects to an ancient Thurian drainage siphon that ascends 300 vertical feet directly into the dry larder beneath Maestro Bartorzo's royal kitchens in the <a href="#gazetteer/palace-of-kordava" class="wiki-link">High Alcázar</a>. Joachor Valiento discovered it while fleeing watchmen; Mother Vespera also knows of it, but keeps it secret as her ultimate emergency escape route.</p>
  <p><strong>The Sealed Chest of Captain Estevar:</strong> Deep inside the flooded sub-cellar lies the water-locked iron chest of Captain Estevar de Morillo, lost during Period V. If recovered, the chest contains 450 ancient minted gold sovereigns, a gold-plated sextant, and a vellum chart revealing the underwater sea-gate into the <a href="#gazetteer/mausoleum-kalenius" class="wiki-link">Submerged Mausoleum of King Kalenius</a>.</p>
</div>

<h3>6. Player-Led Plot Hooks</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Preservation Crisis (The Barmaid's Mortuary Run)</h4>
  <p><strong>Premise:</strong> Pale Beatriza's preservation is breaking down. Cheap Zingg embalming salts used during her reanimation have decayed in the tavern's humid dampness; her wrist tendons are turning brittle and grey necrosis is spreading across her neck. Mother Vespera has only 48 hours before Beatriza collapses into mindless zombie rot. She begs the PCs—specifically the PC Necromancer—for help.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Stabilizing Beatriza requires half a gallon of refined <em>Galvanic Mercurial Brine</em>. This controlled alchemical agent is held in only two places in Kordova: the secured dissecting vats of <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valessa</a> at the <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">Royal University</a>, or the heavily guarded state corpse-distilleries of <a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a>. The PCs must decide whether to call in a favor from their university mentor <a href="#npcs/dean-baltasar-argote" class="wiki-link">Dean Argoto</a>, stage a covert heist of Master Vane's warehouse, or synthesize an unstable herbal alternative using toxic marsh reeds from the Zingg mudflats.</p>
  <div class="dc-box"><strong>Key Checks:</strong> Intelligence / Alchemy or Medicine check (or Necromancer class ability) to properly administer the brine and re-stitch the neck tendons; Charisma / Reaction roll to persuade Maestra Valessa to release the restricted reagents.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If the brine is not procured in time, Beatriza suffers necrotic spasm: her Strength surges to 19, she enters a homicidal feral frenzy, and she begins strangling patrons in the taproom until put down or bound.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Velascan Arson Ultimatum</h4>
  <p><strong>Premise:</strong> Capitán <a href="#npcs/casimiro-velasco" class="wiki-link">Cazmiro de Velasko</a> has delivered an ultimatum to Mother Vespera: pay a weekly "maritime protection tax" of 25 silver sovereigns and hand over the sewer trapdoor keys, or his syndicates will burn The Drowned Rat to the water's edge with Greek fire. Vespera refused, spitting on their messenger's boots.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Tonight at midnight, three Velascan firebugs armed with pitch-pots and incendiary flasks are slipping through the canal flues to firebomb the whale-rib rafters. Vespera and Joachor alert the PCs. The PCs can set an ambush in the flooded taproom, out-duel the arson squad silently before they ignite their pots, or track the arsonists back to the Velasco Syndicate's dock warehouse to burn <em>their</em> contraband instead.</p>
  <div class="dc-box"><strong>Key Checks:</strong> Dexterity / Move Silently to ambush the saboteurs in pitch darkness; Strength / Athletics check to wrestle live Greek fire pots into the flooded bilge before they detonate.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If a single pitch pot is smashed, the whale-rib rafters ignite into an alchemical firestorm. The PCs have 3 combat rounds to evacuate the patrons, carry the heavy iron ledger chest, and lead Beatriza to safety through the rising smoke.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 3: Don Tristao's Pawned Heritage</h4>
  <p><strong>Premise:</strong> In the throes of a three-day aguardiente bender, <a href="#npcs/tristan-revella" class="wiki-link">Don Tristao de Revello</a> ran up an astronomical 14-silver-piece bar tab. Lacking coin, he pawned his ancestral signet ring and a hand-drawn map of the secret ventilation tunnels of the <a href="#gazetteer/revella" class="wiki-link">Revella Tin Mines</a> to Mother Vespera. Now, <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Demetrio Phokas</a> (the Argossean grain factor) has caught wind of the map and offered Vespera 60 gold sovereigns to buy it so Argos can legally foreclose on the mines.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> Vespera is an underworld woman of honor: she gives the PCs 12 hours to settle Tristao's debt and claim the map before she sells it to Argos. The PCs must scrounge or steal the 14 silver, intimidate Phokas's debt agents out of the tavern, or convince Vespera that crown favor is worth far more than foreign gold.</p>
  <div class="dc-box"><strong>Key Checks:</strong> Charisma / Pundonor check (or 14 silver cash) to settle the tab; DC 14 Intimidation check to send Phokas's clerks fleeing back to the docks empty-handed.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> Phokas sends four armed Argossean marine crossbowmen to seize the map by force if Vespera hesitates, sparking a close-quarters shootout in the narrow, flooded booths.</p>
</div>
""",
        "gmSecrets": "The Drowned Rat's flooded sub-cellar contains the sealed chest of Captain Estevar de Morillo, holding pre-Cataclysmic gold and reef maps to King Kalenius's sunken tomb. A secret flue leads directly from behind the bar into the High Alcázar's kitchens.",
        "relatedIds": [
            "joaquin",
            "madre-vespera",
            "beatriz-la-palida",
            "kordovan-thieves-guild",
            "beltran-desoto",
            "velasco-thieves-guild",
            "casimiro-velasco",
            "the-pit",
            "kordava",
            "tristan-revella",
            "valeria-morata",
            "dean-baltasar-argote",
            "vane",
            "demetrio-phokas",
            "palace-of-kordava",
            "mausoleum-kalenius"
        ]
    }

    # -------------------------------------------------------------
    # 2. NEW NPC ARTICLE: madre-vespera
    # -------------------------------------------------------------
    vespera_article = {
        "id": "madre-vespera",
        "category": "npcs",
        "title": "Old Mother Vespera (Vespera 'The Scales')",
        "subtitle": "Mistress of The Drowned Rat • Master Fence & Underworld Matriarch",
        "tags": ["Royal Court", "NPC", "Fence", "The Drowned Rat", "Kordava", "The Pit", "Night Guild", "Underworld", "Period VIII"],
        "aliases": [
            "Old Mother Vespera",
            "Mother Vespera",
            "Madre Vespera",
            "Vespera The Scales",
            "Vespera the One-Eyed",
            "Vespera la Tuerta",
            "Vespera Valiente",
            "The One-Eyed Fence"
        ],
        "summary": "The shrewd, one-eyed matriarch of The Drowned Rat tavern. A retired jewel-fence and cabaret dancer from the tavern's golden age, she commands respect from cutpurses and Grandees alike, wielding a weighted brass balance scale and keeping the tavern stubbornly afloat amid the sewer tides of Kordova.",
        "atAGlance": {
            "appearance": "A sixty-seven-year-old Zingaran woman with a proud, hawkish profile, severe silver hair pinned with carved bone bodkins, and an eye patch of faded purple velvet concealing a cataract-ruined eye. She wears a moth-eaten brocade gown with frayed silver threading—a relic of the tavern's royal era—under a heavy boiled-leather apron with deep, velvet-lined pockets for appraising contraband.",
            "mannerisms": "Perpetually rolls a calibrated brass balance weight across her knuckles; taps her scales with an iron nail when appraising stolen goods; addresses all visitors—from gutter-cutpurses to disguised monarchs—as 'mi corazón' with razor-sharp irony.",
            "quote": "Kings lose their crowns and grandees lose their heads, but a thirst for bad wine and a need to unload hot silver? That outlasts every dynasty in Zingara. Welcome to the Rat, heart of mine. Keep your steel in its scabbard, your silver on the wood, and your boots out of the deep end.",
            "courtDCs": "Morale: 9 (Stubborn survivor); Initial Reaction: Neutral (wary of guards and new faces; +2 if shown high-grade stolen jewelry or offered unclipped silver); Charisma check (or paying off a regular's tab) to unlock her confidential street intelligence.",
            "publicStance": "Presents herself as a cantankerous, exhausted old dive-keeper constantly complaining about rising salt taxes, leaky roofs, and deadbeat cutpurses.",
            "secretAgenda": "Quietly hoarding pre-Cataclysmic bullion in a lead-lined chest beneath the bilge pump, hoping to buy a peaceful olive orchard in the upper Zingg Valley before Kordova sinks into the sea; fiercely protective of Pale Beatriza, whom she views as her surrogate daughter.",
            "rival": "Capitán Cazmiro de Velasco (demanding extortion) & Tax Bailiff Escovador (threatening closure for unpaid wharf duties)",
            "classLevel": "6th-Level Thief (Master Fence & Smuggler)",
            "combatStats": "AC 7 (AAC 12, Padded Silk & Ring of Protection) | HP 22 | THAC0 17 | Atk +3 (1d4+1, Concealed Silver Stiletto / Lead-Weighted Balance) | Saves: 12/12/11/14/12"
        },
        "content": """
<div class="npc-at-a-glance">
  <div class="glance-item"><strong>Class &amp; Level:</strong> 6th-Level Thief (Master Fence &amp; Smuggler)</div>
  <div class="glance-item"><strong>Armor Class:</strong> AC 7 (AAC 12, Padded Silk Vest &amp; Ring of Protection +1)</div>
  <div class="glance-item"><strong>Hit Points:</strong> 22 (6d4+6 HD)</div>
  <div class="glance-item"><strong>Movement:</strong> 90' (30')</div>
  <div class="glance-item"><strong>Attacks:</strong> Concealed Silver Stiletto +3 (1d4+1 + paralytic spider venom) or Leaded Brass Scale Pan +3 (1d4+1 blunt)</div>
  <div class="glance-item"><strong>Saving Throws:</strong> Breath 15 | Poison/Death 12 | Petrify 11 | Wands 12 | Spells 13</div>
  <div class="glance-item"><strong>Morale:</strong> 9 (Unshakable tavern veteran)</div>
  <div class="glance-item"><strong>Alignment:</strong> Neutral (Pragmatic, family-loyal survivalist)</div>
  <div class="glance-item"><strong>Ability Scores:</strong> STR 10, DEX 15 (+1), CON 13 (+1), INT 16 (+2), WIS 15 (+1), CHA 14 (+1)</div>
  <div class="glance-item"><strong>Thief Skills:</strong> Pick Pockets 55%, Open Locks 52%, Find/Remove Traps 50%, Move Silently 50%, Climb Walls 90%, Hide in Shadows 40%, Hear Noise 1-3 on 1d6, Appraise Contraband 95%</div>
</div>

<h3>1. Character Origin &amp; The Gilded Memories</h3>
<p>Born during the twilight of <a href="#history/period-vi" class="wiki-link">Period VI</a>, Vespera was once celebrated as the most captivating flamenco dancer and jewel-smuggler in the lower canal district. She performed at <em>The Alabaster Swan</em> when it still served chilled Argossean white wine to grandees and corsair nobility. Her sharp mathematical mind and photographic memory for gemstone cuts soon made her the city's foremost fence: grandees paid her to liquidate family heirlooms to settle gambling debts, while corsairs from the Barachan Isles brought her sackcloth bags of unpolished pearls.</p>

<p>When the canal district subsided and the civil war of <a href="#history/period-vii" class="wiki-link">Period VII</a> turned the waterfront into a reeking marsh of blood and sewage, the salon's wealthy patrons abandoned the quarter. Vespera bought the sinking property for twelve ounces of melted silver, renamed it <em>The Drowned Rat</em>, and fortified it into an unassailable underworld sanctuary. She has outlived three husbands, five criminal guilds, and two kings—and she has no intention of surrendering her tavern to rising water or rival gangs.</p>

<h3>2. Personality &amp; Operational Code</h3>
<p>Vespera possesses the icy composure of a veteran who has seen every human vice, triumph, and atrocity. She sits behind her counter like an enthroned queen of the gutter, resting one calloused hand near her brass balance scales and the other inches from a loaded, primed flintlock pistol hidden beneath the bar rail.</p>

<p>She enforces <strong>El Pundonor del Arroyo</strong> with absolute firmness:
<ul>
  <li><strong>No Blood on the Planks:</strong> Anyone who draws steel or attacks another patron within the tavern is immediately clubbed unconscious by Gordo Basilio or grappled by Pale Beatriza, stripped of their purse, and dumped into the sewer flues.</li>
  <li><strong>The Sacred Ledger:</strong> Vespera never reveals who pawned an item or who purchased fenced goods—unless the Crown or the Guild meets her price or threatens her tavern.</li>
  <li><strong>Sanctuary for the Starving:</strong> Down-on-their-luck cutpurses like <a href="#npcs/joaquin" class="wiki-link">Joachor</a> are allowed to nurse a single pint of sour ale for hours without harassment, provided they cause no trouble and share street rumors.</li>
</ul>
</p>

<h3>3. Levers of Influence &amp; GM Intrigue</h3>
<ul>
  <li><strong>The Pawned Noble Heirlooms:</strong> Vespera's locked iron chest in her private snug contains proof of devastating aristocratic indiscretions: pawned signet rings belonging to <a href="#npcs/gonzalo-guarralid" class="wiki-link">Duke Gonzalgo's</a> household officers, forged debt notes signed by <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio's</a> clerks, and Don Tristao's original Revella mining maps.</li>
  <li><strong>The Secret Sluice:</strong> Vespera holds the only key to the iron gate in the sub-cellar leading to the <em>Cistern of the Blind Saint</em>. If the PCs win her trust, she can grant them covert ingress to <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano's</a> council chamber without having to navigate the monster-infested public sewers.</li>
  <li><strong>Protective Love for Beatriza:</strong> Vespera's sole emotional vulnerability is <a href="#npcs/beatriz-la-palida" class="wiki-link">Pale Beatriza</a>. If anyone threatens, insults, or attempts to damage the undead barmaid, Vespera's cynical detachment evaporates into cold, murderous fury. Anyone who assists in preserving Beatriza's physical form earns Vespera's eternal, unshakeable loyalty.</li>
</ul>
""",
        "gmSecrets": "Vespera knows the exact location of the underwater chimney leading into the royal kitchens of the High Alcázar. She keeps 300 pre-Cataclysmic gold sovereigns hidden inside the hollowed-out wooden piston of the tavern's bilge pump.",
        "relatedIds": [
            "the-drowned-rat",
            "beatriz-la-palida",
            "joaquin",
            "kordovan-thieves-guild",
            "beltran-desoto",
            "velasco-thieves-guild",
            "casimiro-velasco",
            "the-pit",
            "kordava",
            "tristan-revella",
            "valeria-morata",
            "vane"
        ]
    }

    # -------------------------------------------------------------
    # 3. NEW NPC ARTICLE: beatriz-la-palida
    # -------------------------------------------------------------
    beatriz_article = {
        "id": "beatriz-la-palida",
        "category": "npcs",
        "title": "Pale Beatrizaa (Beatriza the Pale)",
        "subtitle": "The Undead Barmaid of The Drowned Rat • Gentle Thrall of the Canal District",
        "tags": ["Royal Court", "NPC", "Undead", "Zombie", "The Drowned Rat", "Kordava", "The Pit", "Necromancy", "Underworld", "Period VIII"],
        "aliases": [
            "Pale Beatriza",
            "Beatriza the Pale",
            "Beatriza",
            "The Zombie Barmaid",
            "La Bella Beatriza",
            "The Pale Barmaid",
            "Beatriza the Silent",
            "The Undead Barmaid"
        ],
        "summary": "Once the singing darling of the canal district who died of the canal plague during the civil war, Beatriza was lovingly preserved and reanimated by Mother Vespera through illicit university necromancy. Powdered with dried lavender and moving with eerie, silent grace, she serves sour ale to cutpurses, crushes the bones of rowdy brawlers with unyielding rigor mortis, and remains a poignant symbol of Kordova's tragic decay.",
        "atAGlance": {
            "appearance": "A slender, ethereal young Zingaran woman in her early twenties with porcelain-pale, waxy skin dusted with white rice powder and crushed lavender to mask the faint, sharp tang of embalming salts. Her throat bears a delicate, neat row of black silk mortuary stitches. She wears a faded scarlet flamenco dress frayed at the hem, a clean lace apron patched with eel-leather, and her dark hair is woven with dried purple marsh blossoms.",
            "mannerisms": "Utterly silent; moves with uncanny, floating balance across flooded, slippery floorboards without splashing; tilts her head with sorrowful curiosity when listening to conversations; wipes the same wet table ring repeatedly until gently touched; offers a slow, tragic curtsy when tipped a copper.",
            "quote": "[Silently glides through knee-deep bilge water without a splash, sets down an iron mug of foaming sour ale, and wipes the wet tabletop with methodical, mechanical gentleness. As she straightens, a faint scent of dried lavender and mortuary brine drifts across the table.]",
            "courtDCs": "Morale: 12 (Fearless Undead); Initial Reaction: Indifferent (executes tavern duties with clockwork precision); Reaction rolls do not alter her behavior; can be commanded only by Mother Vespera or a recognized necromancer with superior arcane authority.",
            "publicStance": "Presents herself as a quiet, bizarrely obedient barmaid who never talks, never tires, and never makes a mistake with drink orders.",
            "secretAgenda": "Possesses poignant cognitive fragments of her former living existence: she hoards copper coins tipped to her inside a hollow knot in the oak bar counter, and on foggy nights she stands by the sewer grating staring out toward the sea where her sailor lover perished.",
            "rival": "Master Alchemist Vane (who considers her unlicensed, taxable undead property to be seized for the state bone-pits) & Rowdy drunkards",
            "classLevel": "2nd-Level Special Undead Thrall (Preserved Labor Servant)",
            "combatStats": "AC 7 (AAC 12, Unyielding Cadaveric Flesh) | HP 16 (2d8+8 HD) | THAC0 18 | Atk +3 (1d6+3, Unyielding Rigor Mortis Crush) | Immune to Sleep, Charm, Hold, Poison, Cold, Fear, Morale checks | Morale: 12 | Saves: 12/13/14/15/16"
        },
        "content": """
<div class="npc-at-a-glance">
  <div class="glance-item"><strong>Creature Type:</strong> 2nd-Level Special Undead Thrall (Preserved Servant)</div>
  <div class="glance-item"><strong>Armor Class:</strong> AC 7 (AAC 12, Cadaveric Toughness &amp; Thick Velvet Garments)</div>
  <div class="glance-item"><strong>Hit Points:</strong> 16 (2d8+8 HD; exceptionally resilient fleshcraft)</div>
  <div class="glance-item"><strong>Movement:</strong> 90' (30') — Ignores shallow water and mud penalties</div>
  <div class="glance-item"><strong>Attacks:</strong> 1 Unyielding Grip / Slam +3 (1d6+3 blunt / crushing)</div>
  <div class="glance-item"><strong>Special Traits:</strong> Unyielding Rigor Grip (target grappled on natural 18-20, taking 1d6+3 damage per round until escaping with a DC 16 STR check); Silent Gliding; Immune to Sleep, Charm, Hold, Poison, Disease, Fear, Cold, and Morale checks</div>
  <div class="glance-item"><strong>Saving Throws:</strong> Breath 16 | Poison/Death 12 | Petrify 13 | Wands 14 | Spells 15</div>
  <div class="glance-item"><strong>Morale:</strong> 12 (Fearless, unyielding)</div>
  <div class="glance-item"><strong>Alignment:</strong> Neutral (Tragic, harmless unless provoked)</div>
  <div class="glance-item"><strong>Ability Scores:</strong> STR 18 (+3, Supernatural Cadaveric Rigor), DEX 12 (0), CON — (Undead), INT 6 (-1, Residual Muscle Memory), WIS 10 (0), CHA 11 (0, Eerily Beautiful)</div>
</div>

<h3>1. Origin &amp; The Tragic Reanimation</h3>
<p>In life, Beatriza was the radiant daughter of a drowned fisherman, endowed with an enchanting contralto voice and a radiant spirit that brought laughter to the darkest corners of Kordova's canal slums. When Mother Vespera opened <em>The Drowned Rat</em>, Beatriza became its heart—singing mournful Zingaran ballads and defusing violent knife fights with a sharp jest and a bright smile.</p>

<p>During the brutal winter siege of <a href="#history/period-vii" class="wiki-link">Period VII</a>, the deadly "Grey Shivers" (canal typhus) swept through the Lower Ward. When Beatriza succumbed, municipal bailiffs arrived with carts to fling her into Master Vane's mass lime pits. Heartbroken and fiercely defiant, Mother Vespera hid the girl's corpse in the cold beer cellar. She liquidated thirty silver sovereigns—her emergency savings—to hire a renegade student from <a href="#gazetteer/royal-university-of-kordava" class="wiki-link">The Royal University of Kordava</a>, who had studied advanced flesh-preservation under <a href="#npcs/valeria-morata" class="wiki-link">Maestra Valessa de Morato</a>.</p>

<p>Unlike the mindless, decomposing brutes produced in Master Vane's industrial pits, Beatriza underwent an intricate anatomical preservation: her blood was replaced with sweet almond oil, zinc chloride, and lead-sugar brine; her lungs and vocal cords were sealed; and her spinal marrow was charged with galvanic mercury. When she opened her amber eyes, she was dead—yet serene, graceful, and endowed with the muscle memory of her living duties.</p>

<h3>2. Presence in the Taproom</h3>
<p>To the patrons of <em>The Drowned Rat</em>, Beatriza is not a monster; she is a cherished, permanent fixture of their world. She glides through the knee-deep brackish water without splashing, balancing iron trays laden with heavy ceramic mugs of sour ale. When a patron places a coin on the table, she collects it with delicate, cool fingers, wipes the wood with clean rag-cotton, and offers a slow, dignified curtsy.</p>

<p>Her undead physiology makes her the tavern's most terrifyingly effective bouncer:
<ul>
  <li><strong>The Iron Grip of Rigor Mortis:</strong> Because her muscular tissues are locked in perpetual rigor, Beatriza possesses the unyielding physical strength of a siege laborer (STR 18). If a patron draws a weapon, strikes a woman, or attempts to touch her improperly, Beatriza calmly reaches out and takes the offender by the wrist. She does not scream or scowl; she simply squeezes with inexorable, cold hydraulic pressure (1d6+3 damage), bringing the largest dockworker to his knees screaming in agony until he drops his weapon.</li>
  <li><strong>Water Immunity:</strong> While living patrons stumble on the slick floorboards, Beatriza walks across submerged flagstones and slippery catwalks with flawless, unnatural equilibrium.</li>
</ul>
</p>

<h3>3. The Residual Soul &amp; The Preservation Clock</h3>
<p>Unlike standard mindless zombies created by low-tier necromancy, Beatriza retains fragmented shards of her living soul—a phenomenon known among academic thanatologists as <em>Post-Mortem Resonance</em>:</p>
<ul>
  <li><strong>The Secret Coin Stash:</strong> When patrons tip her copper bits, Beatriza slips them into a secret knot-hole beneath the center of the bar counter. She does not spend them; she is hoarding them, driven by the subconscious memory of saving coin to buy her fisherman father a new boat.</li>
  <li><strong>The Sea Grating Vigil:</strong> Between 3:00 AM and dawn, when the taproom empties, Beatriza stands motionless by the rear sewer grating, staring through the iron bars toward the open waters of Kordova's harbor where her betrothed perished at sea.</li>
  <li><strong>The Preservative Decay:</strong> The humid, salty air of the sewer outfall is gradually breaking down her embalming matrix. Her joints require periodic injections of refined mercurial brine to prevent stiffness and necrotic collapse, providing the PCs with an urgent, emotional quest to secure arcane supplies from the Royal University or Master Vane.</li>
</ul>
""",
        "gmSecrets": "If a necromancer of 5th level or higher casts Speak with Dead on Beatriza or attunes to her galvanic spinal charge, she can whisper three sentences of crucial intelligence: she overheard Marquis Murzio's debt-bailiff whispering the combination to the royal tax-barge strongbox to a Velasco Syndicate captain.",
        "relatedIds": [
            "the-drowned-rat",
            "madre-vespera",
            "joaquin",
            "kordovan-thieves-guild",
            "valeria-morata",
            "dean-baltasar-argote",
            "vane",
            "the-pit",
            "kordava",
            "royal-university-of-kordava"
        ]
    }

    # Add the three articles to data['articles']
    # Check if they exist first, replace or append
    art_dict = {a['id']: a for a in data['articles']}
    
    art_dict['the-drowned-rat'] = drowned_rat_article
    art_dict['madre-vespera'] = vespera_article
    art_dict['beatriz-la-palida'] = beatriz_article

    # -------------------------------------------------------------
    # 4. CROSS-LINKING & UPDATING EXISTING ARTICLES
    # -------------------------------------------------------------

    # Update Joachor
    if 'joaquin' in art_dict:
        joaquin_art = art_dict['joaquin']
        for nid in ['the-drowned-rat', 'madre-vespera', 'beatriz-la-palida']:
            if nid not in joaquin_art['relatedIds']:
                joaquin_art['relatedIds'].append(nid)
        print("Updated Joachor with Drowned Rat links.")

    # Update Tristan de Revella
    if 'tristan-revella' in art_dict:
        tristan_art = art_dict['tristan-revella']
        for nid in ['the-drowned-rat', 'madre-vespera', 'beatriz-la-palida']:
            if nid not in tristan_art['relatedIds']:
                tristan_art['relatedIds'].append(nid)
        print("Updated Tristan with Drowned Rat links.")

    # Update Night Guild
    if 'kordovan-thieves-guild' in art_dict:
        guild_art = art_dict['kordovan-thieves-guild']
        for nid in ['the-drowned-rat', 'madre-vespera', 'beatriz-la-palida']:
            if nid not in guild_art['relatedIds']:
                guild_art['relatedIds'].append(nid)
        print("Updated Night Guild with Drowned Rat links.")

    # Update The Pit
    if 'the-pit' in art_dict:
        pit_art = art_dict['the-pit']
        for nid in ['the-drowned-rat', 'madre-vespera']:
            if nid not in pit_art['relatedIds']:
                pit_art['relatedIds'].append(nid)
        print("Updated The Pit with Drowned Rat links.")

    # Update Kordava
    if 'kordava' in art_dict:
        kordava_art = art_dict['kordava']
        for nid in ['the-drowned-rat', 'madre-vespera']:
            if nid not in kordava_art['relatedIds']:
                kordava_art['relatedIds'].append(nid)
        print("Updated Kordava with Drowned Rat links.")

    # Update Velasco Thieves Guild
    if 'velasco-thieves-guild' in art_dict:
        velasco_art = art_dict['velasco-thieves-guild']
        for nid in ['the-drowned-rat', 'madre-vespera']:
            if nid not in velasco_art['relatedIds']:
                velasco_art['relatedIds'].append(nid)
        print("Updated Velasco Thieves Guild with Drowned Rat links.")

    # Update Valessa Morato & University
    if 'valeria-morata' in art_dict:
        valeria_art = art_dict['valeria-morata']
        for nid in ['the-drowned-rat', 'beatriz-la-palida', 'madre-vespera']:
            if nid not in valeria_art['relatedIds']:
                valeria_art['relatedIds'].append(nid)
        print("Updated Valessa Morato with Drowned Rat links.")

    # Reconstruct article list
    data['articles'] = list(art_dict.values())
    print(f"Total articles after expansion: {len(data['articles'])}")

    # Write back to js/data.js
    new_text = prefix + json.dumps(data, indent=2, ensure_ascii=False) + ';\n'
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(new_text)

    print("SUCCESS: Successfully wrote updated data to js/data.js!")

if __name__ == '__main__':
    main()
