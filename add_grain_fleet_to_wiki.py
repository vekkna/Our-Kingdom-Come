"""
add_grain_fleet_to_wiki.py
Adds the Argossean Grain Fleet, Capitán-Commodore Nikolos Voros, Factor Demetrio Phokas,
the Great Grain Heist plot hook, and links them across existing wiki articles,
the State of the Realm crisis registry, and data/sessions.json.
"""

import json
import sys

def main():
    print("Starting Grain Fleet Wiki Expansion...")

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
    # 1. NEW NPC ARTICLE: nikolos-voros
    # -------------------------------------------------------------
    voros_article = {
        "id": "nikolos-voros",
        "category": "npcs",
        "title": "Capitán-Commodore Nikolos Voros",
        "subtitle": "Fleet Commander of the Argossean Grain Armada • Captain of The Gilded Sheaf",
        "tags": ["Royal Court", "NPC", "Fighter", "Argos", "Messantia", "Grain Fleet", "Maritime", "Session 1"],
        "aliases": [
            "Nikolos Voros",
            "Commodore Voros",
            "The Bronze Bull",
            "Capitán Voros",
            "Captain of the Grain Fleet",
            "Voros",
            "Capitán-Commodore Voros",
            "Argossean Fleet Captain",
            "The Bronze Bull of Messantia"
        ],
        "summary": "Veteran Argossean naval commodore anchored 800 yards off Kordova aboard the great carrack The Gilded Sheaf. Invited to the High Alcázar to negotiate grain prices, he balances strict adherence to the Rhodian Sea Law against secret instructions from Ambassador Tiberio to bleed Zingara dry.",
        "atAGlance": {
            "appearance": "A broad-shouldered, barrel-chested mariner of forty-eight with weathered bronze complexion, salt-and-pepper beard, and a crooked broken nose from a boarding pike. Wears a high-collared sea-green officer's coat with heavy gold bullion epaulets over a cuirass of polished sea-bronze, calfskin sea-boots, and an embroidered sash holding a heavy naval backsword and an ivory-stocked wheellock pistol.",
            "mannerisms": "Speaks with a gravelly, resonant mariner's baritone; taps his heavy signet ring against mahogany tables; consults a gold pocket sun-chronometer; refuses to drink unwatered wine while negotiating; maintains a sharp, tactical eye on palace exits.",
            "quote": "A starving belly knows no politics, Your Majesties, but a merchant's ledger knows no pity. My cogs hold fifty thousand bushels of golden Argossean wheat. Pay our price in good silver, or watch your people eat the cobblestones of Kordova. We sail under the flag of Argos; touch a single sack without payment, and you invite the wrath of our war fleet.",
            "courtDCs": "Morale: 10 (Hardened naval veteran); Initial Reaction: Hostile / Wary (-1 on 2d6 Reaction Rolls due to Zingara's notorious bankruptcy). DC 16 Diplomacy to lower asking price; DC 17 Insight to realize he is under secret orders from Ambassador Tiberio; DC 15 Intimidation to shake his nerve (requires credible threat of naval or arcane violence).",
            "publicStance": "Presents himself as a legitimate commercial naval officer upholding international maritime contracts and demanding fair market bullion for his cargo.",
            "secretAgenda": "Voros invested his personal life savings (a 20% equity stake) into this grain shipment. If the cargo rots or is confiscated, he faces debtor's prison in Messantia. Furthermore, Ambassador Tiberio secretly instructed him to stall negotiations until bread riots force the Triumvirate to cede naval rights in the Baracha Strait. However, Voros despises being Tiberio's political pawn and fears his ships being trapped by winter storms or Barachan corsairs.",
            "rival": "Ambassador Tiberio (Manipulative Handler) & Capitán Don Cazmiro (Velascan Corsair Rival)",
            "classLevel": "9th-Level Fighter (Argossean Corsair Commander & Fleet Commodore)",
            "combatStats": "AC 1 (AAC 18) | HP 58 | THAC0 13 | Atk +10 (1d8+4) | Saves: 8/9/10/10/12"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Argossean Grain Fleet &bull; Fleet Command</span>
    <span class="badge rival-badge">Rivals: Ambassador Tiberio &amp; Capitán Don Cazmiro</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A broad-shouldered, barrel-chested mariner of forty-eight with weathered bronze skin, a close-cropped grizzled beard, and a crooked broken nose earned on the boarding deck of a Barachan pirate caravel. He wears an Argossean naval officer's dark sea-green coat with bullion epaulets over a cuirass of polished sea-bronze, calfskin sea-boots, and an embroidered silk sash holding an ivory-stocked wheellock pistol and a massive naval backsword.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Speaks with a deep, resonant mariner's cadence that carries over wind and surf; rhythmically taps a heavy gold seal-ring on tables; frequently pulls a gold sun-chronometer from his waistcoat; refuses to touch unwatered wine during negotiations; continually scans doorways, guards, and balcony lines for tactical archer angles.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;A starving belly knows no politics, Your Majesties, but a merchant's ledger knows no pity. My cogs hold fifty thousand bushels of golden Argossean wheat. Pay our price in good silver, or watch your people eat the cobblestones of Kordova. We sail under the flag of Argos; touch a single sack without payment, and you invite the wrath of our war fleet.&rdquo;</div>
    <div class="glance-item dcs"><strong>Court Reaction &amp; Morale:</strong> Morale: 10 (Iron-nerved sea captain); Initial Reaction: -1 on 2d6 Reaction Rolls (Wary of Zingaran sovereign default). DC 16 Diplomacy to lower his asking price; DC 17 Insight to discern he is being secretly manipulated by <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a>; DC 15 Intimidation to pierce his haughty facade.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Capitán-Commodore Nikolos Voros</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Commodore of the Corn Armada &bull; Captain of The Gilded Sheaf &bull; Lawful Neutral (Naval discipline, commercial contract, mariner's honor)</div>
    </div>
    <span class="stat-class-level">⚔️ 9th-Level Fighter (Argossean Corsair Commander)</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 1 (AAC 18) <small class="text-dim">(Sea-Bronze Cuirass +1 (AC 5), Buckler +1 (-2), DEX 14 (-1))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 9d8+9 (+9 CON bonus) &bull; <span style="color: #2ecc71; font-weight: 700;">58 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 90' (30') on land / 120' on ship deck</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 13 (Base Attack Bonus +6)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +10 to hit (<em>"The Wave-Cleaver"</em> +2 Argossean naval backsword, 1d8+4 slashing; on nat 19-20, shatters non-magical shield or knocks medium target prone); Ranged: +8 to hit (Wheellock horse pistol, 1d8 piercing, range 50', 1 shot then 2 rounds to reload); Off-hand: +7 to hit (Spiked Naval Buckler +1, 1d4+2 bludgeoning)</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box">
      <div class="stat-ability-label">STR</div>
      <div class="stat-ability-score">16</div>
      <div class="stat-ability-mod">+2 to hit, +2 damage</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">DEX</div>
      <div class="stat-ability-score">14</div>
      <div class="stat-ability-mod">+1 missile, -1 AC bonus</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CON</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 HP per Hit Die</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">INT</div>
      <div class="stat-ability-score">13</div>
      <div class="stat-ability-mod">+1 language (Argossean, Zingaran, Barachan Cant)</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">WIS</div>
      <div class="stat-ability-score">14</div>
      <div class="stat-ability-mod">+1 on Mental Saves</div>
    </div>
    <div class="stat-ability-box">
      <div class="stat-ability-label">CHA</div>
      <div class="stat-ability-score">15</div>
      <div class="stat-ability-mod">+1 reaction, Morale 10</div>
    </div>
  </div>

  <div class="stat-section-title">Saving Throws (Fighter 9)</div>
  <div class="stat-save-grid">
    <div class="stat-save-box" title="Breath Attacks (B)"><div class="stat-save-label">B</div><div class="stat-save-val">10</div></div>
    <div class="stat-save-box" title="Poison or Death (P/D)"><div class="stat-save-label">P/D</div><div class="stat-save-val">8</div></div>
    <div class="stat-save-box" title="Petrify or Paralyze (PP)"><div class="stat-save-label">PP</div><div class="stat-save-val">9</div></div>
    <div class="stat-save-box" title="Wands (W)"><div class="stat-save-label">W</div><div class="stat-save-val">10</div></div>
    <div class="stat-save-box" title="Spells (S)"><div class="stat-save-label">S</div><div class="stat-save-val">12</div></div>
  </div>

  <div class="stat-section-title">Signature Equipment &amp; Magic Regalia</div>
  <div class="stat-pill-list">
    <div class="stat-pill">🗡️ <em>The Wave-Cleaver</em> (+2 Naval Backsword; deals double damage vs. aquatic/marine beasts; floats if dropped in water)</div>
    <div class="stat-pill">🛡️ Spiked Naval Buckler +1 (-2 AC bonus, off-hand 1d4+2 strike)</div>
    <div class="stat-pill">📿 <em>Amulet of the Sea-Father</em> (Grants constant <em>Water Breathing</em> and +2 to saves vs. drowning, fog, and lightning)</div>
    <div class="stat-pill">🎺 <em>Signal Whistle of Triton</em> (Silver boatswain's pipe: 1/day produces a deafening high-frequency screech audible 2 miles across open water, signaling his offshore fleet to initiate emergency battle orders)</div>
    <div class="stat-pill">⏱️ Gold Sun-Chronometer of Messantia (120 gp; navigates longitude and solar noon)</div>
    <div class="stat-pill">📜 Boot-Lining Secret Orders (Wax-sealed dispatch from Ambassador Tiberio)</div>
  </div>

  <div class="stat-section-title">Combat Tactics, Retainers &amp; Palace Escort</div>
  <p><strong>Palace Audience Escort:</strong> When attending royal negotiations in the <a href="#gazetteer/palace-of-kordava" class="wiki-link">High Alcázar</a>, Voros never walks alone. He is flanked by <strong>Factor Demetrio Phokas</strong> and <strong>4 Veteran Argossean Sea-Marines</strong> (Level 4 Fighters, AC 3 in hardened scale and pavise shields, 26 HP each, armed with heavy naval cutlasses and repeating crossbows [2 shots/round, 1d6 damage]).</p>
  <p><strong>Defensive Square &amp; Whistle Protocol:</strong> If royal guards draw steel or attempt an arrest, Voros blows his <em>Signal Whistle of Triton</em>. His marines instantly lock shields into a bristling boar's snout formation, firing poisoned quarrel volleys while fighting their way down the Grand Marble Staircase toward the Sea Gate. His whistle alerts the harbor skiffs, causing the war-galleass <em>The Talon of Bel</em> to clear for action.</p>

  <div class="stat-section-title">Power Scale vs. PC Triumvirate (Level 8-9 Rulers)</div>
  <p class="text-muted" style="margin-bottom: 0;">In single combat, an 8th-level PC Fighter or duelist can match Voros blade-for-blade. However, Voros's real lethal armor is geopolitical: he sails under the sovereign charter of the Kingdom of Argos. If killed or arrested without an ironclad, unimpeachable legal justification, the Triumvirate will trigger an immediate Argossean naval embargo and a full-scale war.</p>
</div>

<h3>1. Public Persona &amp; Court Presentation</h3>
<p>To the court of Kordova, Commodore Nikolos Voros presents himself as the archetype of the incorruptible, hard-bitten Hyborian sea captain. He stands with ramrod posture, bowing with formal punctilio to the PC Triumvirate while making it abundantly clear that he answers not to Zingaran crowns, but to the High Admiralty of Messantia and the written clauses of the Rhodian Sea Code.</p>
<p>He displays supreme indifference to Zingaran chivalric pageantry and <a href="#rules/pundonor" class="wiki-link">Pundonor</a>. When grandees boast of ancient lineages, Voros calmly replies with cargo tallies and draft depths. He insists that his fleet came to Kordova in good faith to save the realm from starvation—and that if the capital starves, the blood is solely upon the hands of <a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio</a>, who refuses to unlock the royal treasury.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDAS &amp; HIDDEN LEVERS</div>
  <p><strong>The Personal Bankruptcy Terror:</strong> Despite his haughty demeanor, Voros is privately on the brink of panic. To secure command of this prestigious armada, he pooled his life savings and pledged his family estate in Messantia to purchase a 20% equity stake in the 50,000 bushels of grain. If the fleet is seized, or if the grain rots from bilge-damp in the roadstead, Voros will be completely ruined and thrown into an Argossean debtor's hulk.</p>
  <p><strong>Ambassador Tiberio's Puppet Strings:</strong> Concealed inside the lining of his left boot is an encoded letter bearing the seal of <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a>. The letter explicitly orders Voros to reject all royal promissory notes, reject any price below 45,000 gold sovereigns, and drag out negotiations until bread riots force the Triumvirate to cede full naval jurisdiction over the <a href="#gazetteer/baracha-strait" class="wiki-link">Baracha Strait</a> to Argos. Voros hates Tiberio's political games—he knows that every day anchored off Kordova exposes his wooden ships to Barachan pirate raids and hull-fouling—but Tiberio holds the power to revoke his naval charter.</p>
  <p><strong>The Secret Failsafe Order:</strong> Voros's second-in-command aboard <em>The Gilded Sheaf</em>, Marine Centurion Korinna, holds standing orders: if Voros is imprisoned or does not return by the third night bell, she is to cut the anchor cables of the grain cogs, fire incendiary catapult pots into Kordova's lower timber wharves, and sail for open sea.</p>
</div>

<h3>2. Faction Ties &amp; Underworld Entanglements</h3>
<p>While Voros ostensibly scorns Zingaran criminals, his presence has galvanized the entire maritime underworld of Kordova:</p>
<ul>
  <li><strong><a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a>:</strong> His political master. Tiberio communicates with Voros via nocturnal courier skiffs carrying blue lantern signals. However, Voros secretly suspects Tiberio would happily sacrifice Voros's ships if it gave Argos a pretext to annex Zingara's ports.</li>
  <li><strong><a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro</a> &amp; The Velasco Syndicate:</strong> Cazmiro recognizes Voros's flagship from their old privateering days in the southern sea lanes. Cazmiro considers Voros an arrogant Hyborian interloper and has already approached the PCs through dockside contacts, offering his exiled cutthroats to board and seize the grain fleet.</li>
  <li><strong><a href="#npcs/joaquin" class="wiki-link">Joachor 'The Jackdaw' Valiento</a>:</strong> Joachor has been scouting the landing jetty where Voros's longboat docks. Joachor knows the exact patrol routes of Voros's shore marines and has spotted the locked iron case carried by Factor Demetrio.</li>
  <li><strong><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a>:</strong> Rodorigo views Voros's presence as an intolerable foreign provocation. He has urged the Triumvirate to allow the Royal Army to storm the ships and hang Voros from his own yardarm, but fears an open war with Argos.</li>
</ul>

<h3>3. Player-Led Plot Hooks &amp; Table Encounters</h3>

<div class="hook-card info-card">
  <h4>Hook 1: The Throne Room Showdown &amp; The Boot-Lining Secret</h4>
  <p><strong>Premise:</strong> During the formal price negotiations in the High Alcázar, Commodore Voros demands an exorbitant 45,000 gold sovereigns upfront, sneering at Marquis Murzio's empty vaults. The PCs must break his haughty posture before the court.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs can use raw social leverage, psychological pressure, or physical subterfuge. If they orchestrate a distraction (e.g., spilling wine, a faked duel, or <a href="#npcs/joaquin" class="wiki-link">Joachor</a> picking his pocket) to discover or expose the secret dispatch from <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a>, Voros's legal immunity collapses. The PCs can confront him with the conspiracy: prove he is an agent provocateur rather than an honest merchant, justifying his arrest under Zingaran high treason laws without violating <a href="#rules/pundonor" class="wiki-link">Pundonor</a>!</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 15 Sleight of Hand to extract or read the dispatch; DC 16 Insight to detect his anxiety over his 20% equity stake; DC 16 Diplomacy/Intimidation to force him into a secret royal side-deal.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If threatened with crude violence without legal pretexts, Voros blows his <em>Signal Whistle of Triton</em>, ordering his marines to shoot and his fleet to clear for battle.</p>
</div>

<div class="hook-card info-card">
  <h4>Hook 2: The Gilded Sheaf Heist (Cutting the Cables)</h4>
  <p><strong>Premise:</strong> While Voros is detained in the High Alcázar under protracted 'treaty negotiations', the PCs launch a daring night raid into the Outer Roadstead to board and commandeer the grain armada.</p>
  <p><strong>Core Conflict &amp; Player Choice:</strong> The PCs must decide which underworld ally to trust to pilot the ships: <a href="#npcs/joaquin" class="wiki-link">Joachor</a> and the <a href="#factions/kordovan-thieves-guild" class="wiki-link">Night Guild</a> (who demand grain for the lower wards and silver to pay debts), or <a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Cazmiro</a> (who demands royal letters of marque and 10% of the fleet's cargo).</p>
  <div class="dc-box"><strong>Key Checks:</strong> DC 14 Stealth to row past the war-galleass <em>The Talon of Bel</em>; DC 15 Open Locks/Climb Walls to scale the carrack's tallow-greased hull; DC 16 Sailing to pilot the heavy cogs over the harbor bar at midnight high tide.</div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> If an alarm rocket explodes over the water, Centurion Korinna fires incendiary catapult pots into the nearest grain cog, forcing the PCs to extinguish burning wheat while fighting elite marines.</p>
</div>
""",
        "gmSecrets": "Voros carries a sealed parchment from Ambassador Tiberio in his boot lining ordering him to reject any royal offer under 40,000 sovereigns to force the Baracha Strait cession. If shown proof of Tiberio's deceit or offered a secret royal letter of credit backed by provincial land, Voros's personal financial panic makes him vulnerable to manipulation.",
        "relatedIds": ["argossean-grain-fleet", "demetrio-phokas", "tiberio", "sadoria", "valenza", "joaquin", "casimiro-velasco", "hook-grain-fleet-heist", "kordava", "baracha-strait"]
    }

    # -------------------------------------------------------------
    # 2. NEW NPC ARTICLE: demetrio-phokas
    # -------------------------------------------------------------
    demetrio_article = {
        "id": "demetrio-phokas",
        "category": "npcs",
        "title": "Factor Demetrio 'The Abacus' Phokas",
        "subtitle": "Chief Supercargo & Syndicate Factor • The Golden Pelican Cartel of Messantia",
        "tags": ["NPC", "Merchant", "Argos", "Messantia", "Grain Fleet", "Bureaucracy", "Session 1"],
        "aliases": [
            "Demetrio Phokas",
            "Factor Demetrio",
            "The Abacus",
            "Demetrio",
            "The Supercargo",
            "Phokas",
            "Factor Phokas",
            "Demetrio the Abacus"
        ],
        "summary": "The fastidious, terrified chief accountant and supercargo of the Argossean Grain Fleet. He holds the cargo manifests, weight tallies, and secret price-gouging agreements with Ambassador Tiberio. A coward in physical danger, he is the key lever for any legal sequester or forged manifest scheme.",
        "atAGlance": {
            "appearance": "A slender, nervous man of forty-two with sunken eyes, twitching brows, ink-blackened fingers, and an amber velvet robe lined with marten fur. Carries an ivory-and-brass calculating abacus and a locked iron-bound ledger case.",
            "mannerisms": "Flicks abacus beads nervously when addressed; gulps audibly; dabs perspiration from his balding forehead with an embroidered silk handkerchief; cowers behind Commodore Voros's armored bulk whenever weapons are drawn.",
            "quote": "The mathematics of hunger are immutable, Your Radiance. Kordova consumes twelve hundred bushels of grain each sunrise. You have four days before the bread riots breach the gates of the High Alcázar. Sign the debt covenant, or we weigh anchor.",
            "courtDCs": "Morale: 4 (Unarmed coward); Initial Reaction: Neutral (0 on 2d6). DC 13 Intimidation to cause him to babble confidential cargo numbers; DC 15 Insight to spot him glancing nervously at Ambassador Tiberio; DC 14 Sleight of Hand to pickpocket the ledger key from his sash.",
            "publicStance": "Presents himself as a detached, professional mercantile agent who cares only for contract law, certified weight seals, and prompt coin settlement.",
            "secretAgenda": "Embezzled 2,000 bushels of grain back in Messantia by falsifying moisture loss on the bills of lading. Terrified of an official crown audit or physical torture; if threatened with imprisonment in The Pit or being handed over to Master Vane, he will readily forge or sign whatever documents the PCs place before him.",
            "rival": "High Chancellor Marquis Murzio (Fiscal Competitor)",
            "classLevel": "3rd-Level Specialist / Merchant (Civilian Factor)",
            "combatStats": "AC 9 (AAC 10) | HP 9 | THAC0 20 | Atk +0 (1d4-1 concealed stiletto) | Saves: 14/15/16/17/17"
        },
        "content": """
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">The Golden Pelican Syndicate of Messantia</span>
    <span class="badge rival-badge">Primary Rival: High Chancellor Marquis Murzio</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Visual Appearance:</strong> A gaunt, nervous Argossean burgher of forty-two with a sallow complexion, twitching cheek muscles, and fingertips perpetually stained with iron-gall ink. He wears an expensive amber velvet robe trimmed with marten fur that hangs loosely on his frame, round spectacles with polished quartz lenses, and clutches a heavy, brass-bound iron ledger box as if it were a talisman against violence.</div>
    <div class="glance-item"><strong>Mannerisms:</strong> Rapidly clicks the beads of his ivory abacus whenever someone speaks numbers; dabs his sweating forehead with a perfumed kerchief; habitually hides his hands in his voluminous sleeves; cowers instinctively whenever a knight's scabbard clatters.</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;The mathematics of hunger are immutable, Your Radiance. Kordova consumes twelve hundred bushels of grain each sunrise. You have four days before the bread riots breach the gates of the High Alcázar. Sign the debt covenant, or we weigh anchor.&rdquo;</div>
    <div class="glance-item dcs"><strong>Court Reaction &amp; Morale:</strong> Morale: 4 (Utter coward); Initial Reaction: 0 on 2d6. DC 13 Intimidation causes him to break into a stammering panic; DC 14 Sleight of Hand to pickpocket the small bronze key around his neck that opens his manifest box.</div>
  </div>
</div>

<div class="stat-block">
  <div class="stat-block-header">
    <div>
      <span class="stat-npc-name">Factor Demetrio 'The Abacus' Phokas</span>
      <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 2px;">Chief Supercargo &bull; The Golden Pelican Syndicate &bull; Neutral (Greed, bureaucratic self-preservation, commercial compliance)</div>
    </div>
    <span class="stat-class-level">📜 3rd-Level Specialist / Merchant</span>
  </div>

  <div class="stat-grid-primary">
    <div class="stat-row-item"><strong>Armor Class:</strong> AC 9 (AAC 10) <small class="text-dim">(Unarmored, DEX 9 (0))</small></div>
    <div class="stat-row-item"><strong>Hit Dice / HP:</strong> 3d6 &bull; <span style="color: #e74c3c; font-weight: 700;">9 HP</span></div>
    <div class="stat-row-item"><strong>Movement:</strong> 120' (40')</div>
    <div class="stat-row-item"><strong>THAC0 (Base Atk):</strong> 20 (Base Attack Bonus +0)</div>
    <div class="stat-row-item" style="grid-column: 1 / -1;"><strong>Attacks &amp; Damage:</strong> Melee: +0 to hit (Concealed silver letter-opener / stiletto, 1d4-1 piercing); will immediately surrender or faint if struck.</div>
  </div>

  <div class="stat-section-title">Ability Scores (Labyrinth Lord Modifiers)</div>
  <div class="stat-abilities-bar">
    <div class="stat-ability-box"><div class="stat-ability-label">STR</div><div class="stat-ability-score">8</div><div class="stat-ability-mod">-1 to hit/damage</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">DEX</div><div class="stat-ability-score">9</div><div class="stat-ability-mod">Normal (0)</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">CON</div><div class="stat-ability-score">10</div><div class="stat-ability-mod">Normal (0)</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">INT</div><div class="stat-ability-score">17</div><div class="stat-ability-mod">+3 languages, master accounting</div>
    </div>
    <div class="stat-ability-box"><div class="stat-ability-label">WIS</div><div class="stat-ability-score">11</div><div class="stat-ability-mod">Normal (0)</div></div>
    <div class="stat-ability-box"><div class="stat-ability-label">CHA</div><div class="stat-ability-score">10</div><div class="stat-ability-mod">Normal (0)</div></div>
  </div>

  <div class="stat-section-title">Signature Possessions &amp; Critical Game Relics</div>
  <div class="stat-pill-list">
    <div class="stat-pill">💼 <em>The Grand Cargo Ledger of Messantia</em> (Iron-bound parchment volume detailing exact cargo bushels, bilgewater inspection stamps, and true ownership shares)</div>
    <div class="stat-pill">🗝️ Bronze Seal-Key (Worn on an oiled silk cord around his neck; unlocks the master ledger and the strongbox on <em>The Gilded Sheaf</em>)</div>
    <div class="stat-pill">🧮 Ivory and Brass Calculating Abacus (Pre-Cataclysmic workmanship; +2 on commercial evaluation checks)</div>
    <div class="stat-pill">📜 The Secret Syndicate Codicil (Parchment proving that Ambassador Tiberio guaranteed the merchants a 30% bonus if they withheld grain until the PC Triumvirate signed the Baracha Strait treaty)</div>
  </div>
</div>

<h3>1. Public Persona &amp; Court Role</h3>
<p>Demetrio sits at Commodore Voros's left hand during royal audiences, dipping a swan-feather quill into black ink and rattling his abacus with infuriating rhythm. Whenever <a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio</a> argues that Zingara cannot pay in bullion, Demetrio smoothly recites international banking statutes, interest accruals, and demurrage penalties.</p>
<p>He views the PC Triumvirate as desperate children playing at sovereignty. Yet unlike Voros, who is shielded by martial courage, Demetrio is profoundly terrified of Zingaran savagery. The rumors of <a href="#npcs/vane" class="wiki-link">Master Vane</a>'s flesh-pits and the guillotine in <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> give him sleepless nightmares.</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; THE WEAKEST LINK IN THE FLEET</div>
  <p><strong>The Embezzlement Secret:</strong> Demetrio has his own dirty secret. Before the fleet departed Messantia, he skimmed 2,000 bushels of grain on paper, selling the fictitious surplus to a rival merchant cartel and pocketing 800 gold coins. If his cargo ledger is subjected to an official crown customs audit, the discrepancy will be exposed, bringing down the lethal wrath of the Argossean merchant masters upon his head.</p>
  <p><strong>The Turncoat Factor:</strong> Demetrio is the ideal target for players who want to steal the fleet legally. If separated from Commodore Voros and subjected to credible royal intimidation (e.g., being shown a dungeon cell in the High Alcázar or being threatened with Master Vane's corpse carts), Demetrio will crumble completely. For a guarantee of royal sanctuary, a bag of 500 gold sovereigns, and safe passage out of Zingara, he will:</p>
  <ul>
    <li>Provide certified falsified manifests declaring the grain infected, contraband, or forfeited to the Zingaran crown under ancient maritime admiralty laws.</li>
    <li>Surrender the secret night-watch passwords and recognition lanterns used by the fleet.</li>
    <li>Sign an affidavit swearing that <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a> conspired to wage illegal economic warfare against Zingara.</li>
  </ul>
</div>
""",
        "gmSecrets": "Demetrio embezzled 2,000 bushels in Messantia and is terrified of an audit. If isolated from Voros and threatened with The Pit or offered a royal payoff, he will happily sign forged manifests, hand over cargo ledgers, and give the PCs the night-watch passwords to the fleet.",
        "relatedIds": ["nikolos-voros", "argossean-grain-fleet", "tiberio", "sadoria", "hook-grain-fleet-heist", "kordava"]
    }

    # -------------------------------------------------------------
    # 3. NEW FACTION ARTICLE: argossean-grain-fleet
    # -------------------------------------------------------------
    fleet_article = {
        "id": "argossean-grain-fleet",
        "category": "factions",
        "title": "The Argossean Grain Fleet (The Corn Armada of Messantia)",
        "subtitle": "Foreign Mercantile Armada & Offshore Blockade Risk • The Golden Pelican Syndicate under Royal Charter",
        "tags": ["Faction", "Argos", "Messantia", "Maritime", "Grain Fleet", "Kordava", "Commerce", "Session 1"],
        "aliases": [
            "Argossean Grain Fleet",
            "The Grain Fleet",
            "The Corn Armada",
            "Golden Pelican Syndicate",
            "The Fleet",
            "The Argosy",
            "Grain Fleet",
            "La Flota del Trigo",
            "Messantian Grain Fleet",
            "The Corn Armada of Messantia"
        ],
        "summary": "A flotilla of five heavily laden Argossean merchant cogs and an escort war-galleass anchored in Kordova's outer roadstead, holding 50,000 bushels of grain. While ostensibly waiting for debt guarantees, the fleet is being used by Ambassador Tiberio to strangle the capital into diplomatic submission.",
        "content": """
<div class="info-card">
  <p><strong>Faction Classification:</strong> Foreign Mercantile Armada &bull; Offshore Commercial Leverage</p>
  <p><strong>Supreme Commander:</strong> <a href="#npcs/nikolos-voros" class="wiki-link">Capitán-Commodore Nikolos Voros</a></p>
  <p><strong>Commercial Factor:</strong> <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Demetrio 'The Abacus' Phokas</a> (The Golden Pelican Syndicate of Messantia)</p>
  <p><strong>Anchorage:</strong> The Outer Roadstead of Kordova (800 yards offshore, between King Kalenius's sunken reef and the deep-water harbor mouth)</p>
  <p><strong>Vessel Strength:</strong> 1 Great Carrack (Flagship), 3 Heavy Grain Cogs, 1 Cargo Fluyt, 1 War-Galleass Escort</p>
  <p><strong>Armed Personnel:</strong> 140 seasoned Argossean heavy sea-marines, 60 rowers, ~220 sailors</p>
  <p><strong>Cargo Manifest:</strong> 50,000 bushels of golden wheat, barley, and rye; 400 amphorae of Messantian olive oil; 200 barrels of salt-pork</p>
</div>

<h3>1. Fleet Composition &amp; Vessel Anatomy</h3>
<p>The armada riding the swells of Kordova's bay is not a ragtag merchant flotilla, but a formidable corporate-military enterprise dispatched under royal charter from the maritime superpower of <strong>Argos</strong>. Its vessels comprise:</p>
<ul>
  <li><strong><em>The Gilded Sheaf (Nea Messantia):</em></strong> The flagship. A towering four-masted great carrack (150 Hull Points, AC 4). Features a reinforced iron beakhead, high forecastle and sterncastle towers equipped with 3 heavy pivot-ballistas firing barbed chain-bolts, and anti-boarding rope nettings greased with mutton tallow. Holds 20,000 bushels of grain, the commodore's stateroom, and the fleet strongbox.</li>
  <li><strong><em>The Bull of Messantia:</em></strong> A broad, deep-bellied roundship (120 Hull Points, AC 5). Holds 15,000 bushels of hardened winter wheat. Heavily laden, drawing 18 feet of water.</li>
  <li><strong><em>The Horn of Ceres:</em></strong> A stout Argossean cog (90 Hull Points, AC 6). Holds 12,000 bushels of barley and rye.</li>
  <li><strong><em>The Sea-Nymph's Bounty:</em></strong> A cargo fluyt (70 Hull Points, AC 6). Holds 3,000 bushels of grain, plus luxury provisions: 400 amphorae of Messantian olive oil and 200 casks of salt-pork.</li>
  <li><strong><em>The Talon of Bel:</em></strong> A swift 50-oar war-galleass (80 Hull Points, AC 4). Armed with a bronze ramming prow, 2 light catapults throwing Greek-fire pots, 60 rowers, and 40 veteran marine crossbowmen under Marine Centurion Korinna. Patrolling the perimeter day and night to keep Zingaran fishing boats and Barachan corsairs at bay.</li>
</ul>

<h3>2. The Strategic Deadlock: Why Are They Waiting?</h3>
<p>The fleet arrived off Kordova eight days ago. To the starving commoners gazing from the sea-bastions of the Lower Wards, the ships appear as floating mountains of salvation. Yet not a single sack of flour has crossed the harbor boom. Why?</p>
<ul>
  <li><strong>The Bankruptcy Barrier:</strong> High Chancellor <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio de Sadoria</a> has formally refused to pay the consortium's asking price of 45,000 gold sovereigns, claiming the state vaults hold only worthless promissory scrip.</li>
  <li><strong>Ambassador Tiberio's Economic Strangulation:</strong> In truth, the delay is artificially manufactured. <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a> has privately instructed <a href="#npcs/nikolos-voros" class="wiki-link">Commodore Voros</a> to reject all Zingaran compromises. Tiberio is weaponizing the city's hunger. He calculates that within four days, bread riots will explode in <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>, forcing the desperate PC Triumvirate to sign the <strong>Baracha Strait Navigation Concordat</strong>—surrendering Zingara's maritime sovereignty and handing Argos control over coastal trade routes.</li>
</ul>

<h3>3. Operational Strengths &amp; Tactical Vulnerabilities</h3>

<div class="stat-pill-list">
  <div class="stat-pill">⚔️ <strong>Strengths:</strong> Overwhelming naval firepower; high ship sides make boarding without grapples nearly impossible; protected by international maritime law and Argossean superpower backing.</div>
  <div class="stat-pill">⚠️ <strong>The Sea-Damp Clock:</strong> Bilgewater moisture and grain-weevils begin spoiling wheat after 12–14 days at anchor. Factor Demetrio knows they have less than 6 days before the bottom holds start rotting.</div>
  <div class="stat-pill">⚠️ <strong>Tidal Traps:</strong> The deep cogs draw 18 feet of water. They cannot enter Kordova's inner harbor basin without native Zingaran harbor pilots or high tide over the harbor bar.</div>
  <div class="stat-pill">⚠️ <strong>Night Exhaustion:</strong> Double night watches against Barachan pirates have left the skeleton crews fatigued, making them vulnerable to silent boarding operations.</div>
</div>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; STRATEGIC FACTION IMPACT</div>
  <p><strong>The Famine Clock:</strong> Kordova consumes approximately 1,200 bushels of grain per day. The municipal granaries have barely 4 days of reserves remaining. If the PCs fail to secure the fleet's cargo within 96 hours:</p>
  <ul>
    <li>Bread riots will erupt in the Lower Wards, incited by <a href="#factions/republican-insurgents" class="wiki-link">Republican Insurgents</a>.</li>
    <li>The PC Triumvirate will lose 1 Crown Sovereignty Point per day of unrest.</li>
    <li><a href="#npcs/vane" class="wiki-link">Master Vane</a> will offer to 'solve the bread crisis' by replacing living municipal workers with 500 new industrial zombies—further terrifying the populace.</li>
  </ul>
  <p>Conversely, if the PCs successfully seize or purchase the grain and flood the markets, bread prices drop by 80% overnight, the bread riots vanish, and the PCs gain <strong>+2 Crown Sovereignty Points</strong> and unshakeable public adoration from the common folk!</p>
</div>
""",
        "gmSecrets": "The fleet's grain holds are already beginning to warm from moisture fermentation in the lowest decks. Factor Demetrio is terrified the syndicate will discover the spoilage. If the PCs delay the fleet or blockade them in the roadstead, the merchants will be forced to dump the grain or sell at fire-sale prices.",
        "relatedIds": ["nikolos-voros", "demetrio-phokas", "tiberio", "sadoria", "valenza", "joaquin", "kordovan-thieves-guild", "velasco-thieves-guild", "casimiro-velasco", "hook-grain-fleet-heist", "kordava", "baracha-strait"]
    }

    # -------------------------------------------------------------
    # 4. NEW PLOT HOOK ARTICLE: hook-grain-fleet-heist
    # -------------------------------------------------------------
    hook_article = {
        "id": "hook-grain-fleet-heist",
        "category": "hooks",
        "title": "The Gilded Sheaf: The Great Grain Heist",
        "subtitle": "Master Sandbox Heist & Political Extortion Blueprint • Legal Sequester vs. Black-Flag Piracy",
        "tags": ["Plot Hook", "Sandbox", "Heist", "Grain Fleet", "Kordava", "Pundonor", "The Pit", "Session 1"],
        "aliases": [
            "Grain Fleet Heist",
            "The Great Grain Heist",
            "Stealing the Grain Fleet",
            "Grain Heist",
            "The Gilded Sheaf Heist",
            "Hook: Grain Fleet",
            "The Grain Heist"
        ],
        "summary": "The complete tactical and political blueprint for the PC Triumvirate's plan to seize the 50,000 bushels of grain from the Argossean fleet waiting offshore, detailing both the court-based legal trap (trumped-up charges) and the midnight maritime piracy operation.",
        "content": """
<div class="info-card">
  <p><strong>Involved Factions:</strong> The PC Triumvirate, The Argossean Grain Fleet, <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a>, <a href="#factions/kordovan-thieves-guild" class="wiki-link">The Night Guild</a>, <a href="#factions/velasco-thieves-guild" class="wiki-link">The Velasco Syndicate</a>, <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio</a>, <a href="#npcs/valenza" class="wiki-link">General Don Rodorigo</a></p>
  <p><strong>Strategic Stakes:</strong> 50,000 bushels of grain; immediate relief of Kordova's starvation; +2 Sovereignty Points; potential war with the Kingdom of Argos if botched.</p>
</div>

<h3>1. Narrative Premise &amp; The Players' Dilemma</h3>
<p>Faced with an empty treasury, looming bread riots, and an offshore armada holding the city's food supply hostage, the Player Character Triumvirate has invited <a href="#npcs/nikolos-voros" class="wiki-link">Capitán-Commodore Nikolos Voros</a> to the <a href="#gazetteer/palace-of-kordava" class="wiki-link">High Alcázar</a> under the pretext of price negotiations. In truth, the players intend to steal the grain—either by springing <strong>trumped-up criminal charges</strong> during the court audience, or by launching a covert <strong>maritime heist / act of piracy</strong> under cover of darkness.</p>

<p>Below is the complete GM sandbox blueprint for resolving both approaches at the table.</p>

---

<h3>2. Approach A: The Legal Ambush &amp; Trumped-Up Criminal Charges</h3>
<p><strong>Concept:</strong> The PCs use their royal authority within the High Alcázar to entrap, arrest, or legally sequester Commodore Voros and his fleet, manufacturing lawful pretexts to bypass foreign diplomatic immunity and preserve their royal <a href="#rules/pundonor" class="wiki-link">Pundonor</a>.</p>

<h4>Step 1: Setting the Stage in the High Alcázar</h4>
<p>Commodore Voros arrives in the Throne Room flanked by 4 veteran Argossean marines and <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Demetrio Phokas</a> clutching his cargo ledgers. General Don Rodorigo's caballeros line the walls. High Chancellor Marquis Murzio looks visibly distressed, while Ambassador Tiberio watches smugly from the grand balcony.</p>

<h4>Step 2: Deploying the Trumped-Up Pretexts (The Levers)</h4>
<p>The PCs can employ one or more of the following manufactured charges:</p>
<ul>
  <li><strong>Pretext 1: Contraband &amp; High Treason (Planting Evidence):</strong>
    <br>Prior to or during the audience, the PCs or an allied cutpurse (<a href="#npcs/joaquin" class="wiki-link">Joachor Valiento</a>) secretly plant contraband into Voros's landing longboat or the grain sample sacks brought to court. Examples: prohibited alchemical fire-pitch, forged letters linking Voros to the <a href="#factions/republican-insurgents" class="wiki-link">Republican Insurgents</a> in The Pit, or outlawed Gnostic devotional texts of the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a>.
    <br><em>Skill Checks:</em> DC 15 Sleight of Hand / Stealth to plant the evidence without alerting Voros's marines; DC 16 Court Law / Charisma to dramatically reveal the contraband and declare the fleet guilty of conspiracy against the Crown.</li>
  <li><strong>Pretext 2: The Ancient Roadstead Tithe of King Ancillus I:</strong>
    <br>Resurrecting an obscure royal maritime edict from Period I: any foreign vessel carrying weapons of war that anchors within three leagues of the Black River mouth without paying the ancient "Pearl Anchor-Tax" forfeits all cargo to the royal granaries under sovereign maritime right.
    <br><em>Skill Checks:</em> DC 15 History / Heraldry to cite the statute; DC 17 Intimidation / Pundonor to shout down Marquis Murzio's objections and silence Ambassador Tiberio's treaty protests.</li>
  <li><strong>Pretext 3: The Black Grain Rot Quarantine:</strong>
    <br>With the assistance of royal physician <a href="#npcs/escovedo" class="wiki-link">Dr. Horasto Escovador</a> or <a href="#npcs/vane" class="wiki-link">Master Vane</a>, the PCs produce an official medical finding claiming the grain samples show symptoms of toxic ergot or foreign sea-plague. By royal sanitary decree, the entire fleet must be impounded immediately, the crew restricted to quarters, and the grain transferred to royal silos for "alchemical cleansing."
    <br><em>Skill Checks:</em> DC 14 Medicine / Deception to convincingly stage the diagnosis; DC 13 Insight to notice that Factor Demetrio is already terrified of grain moisture spoilage.</li>
</ul>

<h4>Step 3: Breaking the Supercargo</h4>
<p>Once the charges are levied, the PCs can turn the screws on <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Demetrio</a> (Morale 4). If isolated from Voros and threatened with the dungeon, Demetrio will eagerly sign an official surrender of the cargo in exchange for royal protection, handing over the recognition passwords and anchor maps!</p>

<h4>Step 4: Managing Pundonor &amp; Diplomatic Fallout</h4>
<div class="dc-box">
  <strong>Pundonor Check:</strong> Arresting an invited guest violates chivalric hospitality unless the PCs publicly prove the foreigner acted dishonorably first. If the PCs succeed on their Deception/Law checks, their Pundonor remains <strong>Unstained (+1 Sovereignty)</strong>. If they botch the charges and simply butcher or lock up Voros without proof, they suffer <strong>-1 Pundonor</strong> and face accusations of tyranny from Duke Gonzalgo.
</div>

---

<h3>3. Approach B: The Black-Flag Piracy &amp; Midnight Boarding</h3>
<p><strong>Concept:</strong> While Voros is detained at the palace (or during the confusion of negotiations), the PCs coordinate a covert night operation to board, commandeer, and slip the grain cogs into Kordova's inner harbor basin.</p>

<h4>Phase 1: Assembling the Strike Force</h4>
<p>The PCs must choose their underworld cutthroats:</p>
<ul>
  <li><strong>The Night Guild Option (<a href="#npcs/joaquin" class="wiki-link">Joachor</a> &amp; <a href="#npcs/beltran-desoto" class="wiki-link">Don Beltrano</a>):</strong> Joachor procures 4 muffled rowing skiffs, grappling hooks, and guides the strike team through the subterranean sea-caves of <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> directly into the Outer Roadstead. Cost: 80 gold sovereigns to cancel Joachor's blood-tithe.</li>
  <li><strong>The Velasco Syndicate Option (<a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Don Cazmiro</a>):</strong> Cazmiro provides 20 hardened corsair veterans who specialize in cutting anchor cables and steering heavy cogs in pitch darkness. Cost: Cazmiro demands 10% of the grain and royal letters of marque.</li>
  <li><strong>Master Vane's Undead Divers:</strong> <a href="#npcs/vane" class="wiki-link">Master Vane</a> offers 12 memory-retaining zombie sailors who walk across the ocean floor, climb the anchor cables from below the waterline, and quietly strangle the deck watches without making a sound! Cost: Vane demands the corpses of any marines killed during the raid.</li>
</ul>

<h4>Phase 2: Infiltration &amp; The Sentry Perimeter</h4>
<p>The fleet is anchored 800 yards out. <em>The Talon of Bel</em> (war-galleass) rows patrol circles every 30 minutes.</p>
<div class="dc-box">
  <strong>Key Infiltration Checks:</strong>
  <ul>
    <li>DC 14 Stealth / Sailing to time the rowing skiffs between the galleass's lantern sweeps.</li>
    <li>DC 15 Thief Skills (Climb Sheer Surfaces) or DC 14 Strength (Athletics) to scale the tallow-greased hull of <em>The Bull of Messantia</em> using rope grapnels.</li>
    <li>DC 15 Melee Stealth to neutralize the 4 sleeping night-watch marines on deck without raising the alarm.</li>
  </ul>
</div>

<h4>Phase 3: Slipping the Cables &amp; The Midnight Tide</h4>
<p>Once on deck, the boarding team must chop the massive 6-inch hemp anchor cables with boarding axes and raise the storm jibs.</p>
<p class="escalation"><strong>The Nautical Hazard:</strong> The heavy roundships draw 18 feet. A DC 16 Sailing / Navigation check is required to navigate through the shoals and avoid the jagged granite pillars of the Submerged Mausoleum of King Kalenius. If failed, the ship scrapes a reef, taking 20 hull damage and alerting harbor lookouts!</p>

<h4>Phase 4: Beached on the Wharves</h4>
<p>At high tide (approx. 3:00 AM), the commandeered cogs glide past the harbor boom and beach directly upon the stone wharves of the Lower Wards. Hundreds of starving dockers, alerted by Night Guild runners, immediately begin offloading sacks of grain into the municipal storehouses before dawn!</p>

---

<h3>4. Dynamic Escalation Triggers</h3>
<ul>
  <li><strong>The Lantern Alarm:</strong> If an alarm rocket is fired from <em>The Gilded Sheaf</em>, Marine Centurion Korinna orders the galleass to ram the nearest hijacked cog and begins firing incendiary pots at the harbor wharves.</li>
  <li><strong>Ambassador Tiberio's Retaliation:</strong> If Tiberio realizes the PCs are seizing the fleet, he activates his 8 elite Messantian marines stationed at the foreign embassy to attempt to assassinate Factor Demetrio (to silence him) or set fire to the royal granaries.</li>
  <li><strong>The Grandee Backlash:</strong> If the grain is secured, High Chancellor Marquis Murzio attempts to claim custody of the grain to sell it at market prices to pay foreign debts. The PCs must publicly override him, distributing it directly to the poor to cement their Crown Sovereignty!</li>
</ul>
""",
        "gmSecrets": "If the players use Master Vane's underwater zombies to hijack the ships, some commoners will see undead hands hauling grain sacks onto the wharves at dawn. Republican agitators in The Pit will seize on this to spread rumors that the grain has been cursed by necromancy, forcing the PCs to publicly eat bread baked from the flour to dispel panic.",
        "relatedIds": ["nikolos-voros", "demetrio-phokas", "argossean-grain-fleet", "tiberio", "sadoria", "valenza", "joaquin", "kordovan-thieves-guild", "velasco-thieves-guild", "casimiro-velasco", "kordava", "pundonor"]
    }

    # Add new articles
    data['articles'].extend([voros_article, demetrio_article, fleet_article, hook_article])
    print("Added 4 new articles: nikolos-voros, demetrio-phokas, argossean-grain-fleet, hook-grain-fleet-heist.")

    # -------------------------------------------------------------
    # 5. UPDATE EXISTING ARTICLE: tiberio
    # -------------------------------------------------------------
    tiberio_art = next((a for a in data['articles'] if a['id'] == 'tiberio'), None)
    if tiberio_art:
        tiberio_expansion = """
<h3>The Offshore Grain Leverage &amp; Secret Directives to Commodore Voros</h3>
<p>Behind his perfumed handkerchief and silk tunics, Ambassador Tiberio is the hidden architect of Kordova's current food crisis. While publicly offering his 'deepest sympathies' to the PC Triumvirate, Tiberio is secretly commanding <a href="#npcs/nikolos-voros" class="wiki-link">Capitán-Commodore Nikolos Voros</a> of the offshore <a href="#factions/argossean-grain-fleet" class="wiki-link">Argossean Grain Fleet</a> via nocturnal courier skiffs.</p>

<p>Tiberio's secret orders to Voros are explicit: reject all royal paper credit, demand 45,000 gold sovereigns upfront, and stall off the coast until bread riots in <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> bring the Triumvirate to its knees. Tiberio plans to step in at the final hour, offering to 'personally purchase' the grain for the crown—in exchange for the PCs signing the <em>Baracha Strait Navigation Concordat</em>, granting Argossean warships unrestricted patrol and hunting rights in Zingaran waters.</p>

<p>If the PC Triumvirate dares to arrest Voros, trump up charges, or seize the grain fleet through <a href="#hooks/hook-grain-fleet-heist" class="wiki-link">maritime piracy</a>, Tiberio's polished mask slips. He will storm the High Alcázar, invoke the sacred treaties of Messantia, threaten an immediate naval war, and dispatch embassy assassins to eliminate <a href="#npcs/demetrio-phokas" class="wiki-link">Factor Demetrio</a> before the supercargo can reveal Tiberio's written conspiracy.</p>
"""
        if 'The Offshore Grain Leverage' not in tiberio_art['content']:
            tiberio_art['content'] += tiberio_expansion
            print("Updated tiberio article with Grain Fleet conspiracy details!")
        for rid in ['nikolos-voros', 'demetrio-phokas', 'argossean-grain-fleet', 'hook-grain-fleet-heist']:
            if rid not in tiberio_art.get('relatedIds', []):
                tiberio_art.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 6. UPDATE EXISTING ARTICLE: sadoria (Marquis Murzio)
    # -------------------------------------------------------------
    sadoria_art = next((a for a in data['articles'] if a['id'] == 'sadoria'), None)
    if sadoria_art:
        sadoria_expansion = """
<h3>The Grain Fleet Panic &amp; The Empty Treasury</h3>
<p>The arrival of the <a href="#factions/argossean-grain-fleet" class="wiki-link">Argossean Grain Fleet</a> has thrown High Chancellor Marquis Murzio into a cold panic. With the royal vaults empty and provincial tax revenues halted, Murzio is terrified that the haughty <a href="#npcs/nikolos-voros" class="wiki-link">Commodore Voros</a> will sail away, leaving Kordova to starve. Yet he is equally terrified of the PCs' reckless schemes to 'steal' or legally sequester the grain. Murzio warns the Triumvirate that seizing foreign cargo will trigger an immediate trade embargo from all Hyborian nations, ruin his personal banking partners in Messantia, and permanently destroy Zingara's international credit.</p>
"""
        if 'The Grain Fleet Panic &amp; The Empty Treasury' not in sadoria_art['content']:
            sadoria_art['content'] += sadoria_expansion
            print("Updated sadoria article with Grain Fleet panic!")
        for rid in ['nikolos-voros', 'demetrio-phokas', 'argossean-grain-fleet', 'hook-grain-fleet-heist']:
            if rid not in sadoria_art.get('relatedIds', []):
                sadoria_art.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 7. UPDATE EXISTING ARTICLE: valenza (General Don Rodorigo)
    # -------------------------------------------------------------
    valenza_art = next((a for a in data['articles'] if a['id'] == 'valenza'), None)
    if valenza_art:
        valenza_expansion = """
<h3>Military Assessment of the Offshore Grain Fleet</h3>
<p>General Don Rodorigo views the presence of the <a href="#factions/argossean-grain-fleet" class="wiki-link">Argossean Grain Fleet</a> as an insulting foreign provocation. While he despises the idea of 'vulgar dockside piracy'—which he claims tarnishes royal <a href="#rules/pundonor" class="wiki-link">Pundonor</a>—he is desperate to feed his royal caballeros and city garrison. Rodorigo has privately informed the PCs that if they can establish an ironclad legal pretext or royal edict of sequester, he will personally order 30 elite Royal Armored Marines to board and secure the grain ships under royal military law.</p>
"""
        if 'Military Assessment of the Offshore Grain Fleet' not in valenza_art['content']:
            valenza_art['content'] += valenza_expansion
            print("Updated valenza article with Grain Fleet military stance!")
        for rid in ['nikolos-voros', 'argossean-grain-fleet', 'hook-grain-fleet-heist']:
            if rid not in valenza_art.get('relatedIds', []):
                valenza_art.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 8. UPDATE EXISTING ARTICLE: joaquin
    # -------------------------------------------------------------
    joaquin_art = next((a for a in data['articles'] if a['id'] == 'joaquin'), None)
    if joaquin_art:
        joaquin_expansion = """
<h3>The Grain Heist Opportunity: Wiping the Blood-Tithe</h3>
<p>When Joachor learned that the PC Triumvirate invited <a href="#npcs/nikolos-voros" class="wiki-link">Commodore Voros</a> to court and planned to seize the <a href="#factions/argossean-grain-fleet" class="wiki-link">Argossean Grain Fleet</a>, his eyes lit with desperate ambition. Joachor sees this operation as his golden ticket to survival. In exchange for the PCs paying off his 80-sovereign debt to <a href="#npcs/beltran-desoto" class="wiki-link">Guildmaster Don Beltrano</a>, Joachor offers to:</p>
<ul>
  <li>Procure muffled rowing skiffs from the old smuggler caves beneath <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>.</li>
  <li>Slip aboard Voros's landing skiff to plant incriminating contraband (forged insurgent treaties or outlawed Gnostic texts) to support trumped-up criminal charges.</li>
  <li>Guide the PCs' boarding party through the misty roadstead at midnight to cut the anchor cables of the heavy grain cogs.</li>
</ul>
"""
        if 'The Grain Heist Opportunity' not in joaquin_art['content']:
            joaquin_art['content'] += joaquin_expansion
            print("Updated joaquin article with Grain Heist opportunities!")
        for rid in ['nikolos-voros', 'demetrio-phokas', 'argossean-grain-fleet', 'hook-grain-fleet-heist']:
            if rid not in joaquin_art.get('relatedIds', []):
                joaquin_art.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 9. UPDATE EXISTING ARTICLE: casimiro-velasco
    # -------------------------------------------------------------
    casimiro_art = next((a for a in data['articles'] if a['id'] == 'casimiro-velasco'), None)
    if casimiro_art:
        casimiro_expansion = """
<h3>The Corsair's Ambition: Seizing the Argossean Carrack</h3>
<p>Capitán Don Cazmiro has fought Argossean merchantmen in the Baracha Strait for twenty years. Hearing of the <a href="#factions/argossean-grain-fleet" class="wiki-link">Argossean Grain Fleet</a> anchored in the roadstead, Cazmiro has sent word to the palace offering the veteran privateers of the <a href="#factions/velasco-thieves-guild" class="wiki-link">Velasco Syndicate</a> to board, butcher the marine skeleton crews, and pilot the grain cogs onto the docks. In return, Cazmiro demands 10% of the grain, royal letters of marque recognizing him as a Crown Privateer, and full pardons for his exiled men.</p>
"""
        if 'The Corsair\'s Ambition' not in casimiro_art['content']:
            casimiro_art['content'] += casimiro_expansion
            print("Updated casimiro-velasco article with Grain Fleet corsair offer!")
        for rid in ['nikolos-voros', 'argossean-grain-fleet', 'hook-grain-fleet-heist']:
            if rid not in casimiro_art.get('relatedIds', []):
                casimiro_art.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 10. UPDATE EXISTING ARTICLE: beltran-desoto
    # -------------------------------------------------------------
    beltran_art = next((a for a in data['articles'] if a['id'] == 'beltran-desoto'), None)
    if beltran_art:
        beltran_expansion = """
<h3>Underworld Grain Distribution &amp; Black-Market Leverage</h3>
<p>Don Beltrano de Zoto understands the power of bread better than any grandee in the High Alcázar. If the PCs succeed in seizing the <a href="#factions/argossean-grain-fleet" class="wiki-link">Argossean Grain Fleet</a>, Beltrano's <a href="#factions/kordovan-thieves-guild" class="wiki-link">Night Guild</a> is the only organization in Kordova with the covert warehousing and street-level bakery networks capable of distributing 50,000 bushels without triggering rioting or theft. In exchange for managing the distribution, Beltrano demands an exclusive 5% distribution rake and the cancellation of all City Watch arrest warrants against his senior fences.</p>
"""
        if 'Underworld Grain Distribution' not in beltran_art['content']:
            beltran_art['content'] += beltran_expansion
            print("Updated beltran-desoto article with Underworld Grain Distribution!")
        for rid in ['argossean-grain-fleet', 'hook-grain-fleet-heist', 'nikolos-voros']:
            if rid not in beltran_art.get('relatedIds', []):
                beltran_art.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 11. UPDATE EXISTING ARTICLE: state-of-the-realm
    # -------------------------------------------------------------
    state_realm = next((a for a in data['articles'] if a['id'] == 'state-of-the-realm'), None)
    if state_realm:
        crisis_7_html = """
<div class="crisis-card info-card" style="border-left: 4px solid #f39c12; margin-top: 20px;">
  <div class="crisis-header" style="display: flex; justify-content: space-between; align-items: center;">
    <h4 style="margin: 0; color: #f39c12;">Crisis 7: The Starvation Clock &amp; The Offshore Grain Armada</h4>
    <span class="badge" style="background: #e67e22; color: #fff;">CRITICAL &bull; 96-HOUR COUNTDOWN</span>
  </div>
  <p><strong>Threat Classification:</strong> Impending Mass Famine, Civil Insurrection &amp; Foreign Naval Extortion</p>
  <p><strong>Core Dilemma:</strong> Kordova's municipal granaries hold barely 4 days of flour before catastrophic bread riots erupt across the Lower Wards and <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a>. Anchored 800 yards offshore in the Outer Roadstead lies <a href="#factions/argossean-grain-fleet" class="wiki-link">The Argossean Grain Fleet</a> under <a href="#npcs/nikolos-voros" class="wiki-link">Capitán-Commodore Nikolos Voros</a>, laden with 50,000 bushels of wheat. However, the armada is being used as a diplomatic cudgel by <a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio</a>, who refuses to release the grain until the bankrupt crown surrenders naval sovereignty over the <a href="#gazetteer/baracha-strait" class="wiki-link">Baracha Strait</a>.</p>
  <p><strong>Active Player Action:</strong> At the conclusion of Session 1, the PC Triumvirate dispatched a royal summons inviting Commodore Voros to the High Alcázar under the guise of price negotiations, while secretly preparing to seize the cargo via <a href="#hooks/hook-grain-fleet-heist" class="wiki-link">trumped-up criminal charges or black-flag maritime piracy</a>.</p>
  <div class="dc-box">
    <strong>Resolution Paths:</strong>
    <ul>
      <li><strong>Path 1 (Diplomatic Submission):</strong> Pay 45,000 sovereigns or sign the Baracha Strait treaty (Averts famine; costs sovereignty and -1 Pundonor).</li>
      <li><strong>Path 2 (The Legal Ambush):</strong> Plant contraband or cite ancient maritime statutes to arrest Voros and sequester the fleet (+1 Sovereignty, risks Argossean trade sanctions).</li>
      <li><strong>Path 3 (Black-Flag Piracy):</strong> Partner with <a href="#npcs/joaquin" class="wiki-link">Joachor</a> or <a href="#npcs/casimiro-velasco" class="wiki-link">Capitán Cazmiro</a> to board and hijack the cogs at midnight (+2 Sovereignty, immediate bread riot relief, risks direct naval clash with <em>The Talon of Bel</em>).</li>
    </ul>
  </div>
</div>
"""
        if 'Crisis 7: The Starvation Clock' not in state_realm['content']:
            state_realm['content'] += crisis_7_html
            print("Updated state-of-the-realm with Crisis 7: The Starvation Clock!")
        for rid in ['argossean-grain-fleet', 'nikolos-voros', 'demetrio-phokas', 'hook-grain-fleet-heist']:
            if rid not in state_realm.get('relatedIds', []):
                state_realm.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 12. UPDATE EXISTING ARTICLE: kordava
    # -------------------------------------------------------------
    kordava_art = next((a for a in data['articles'] if a['id'] == 'kordava'), None)
    if kordava_art:
        kordava_harbor_expansion = """
<h3>The Outer Roadstead &amp; The Anchorage of the Corn Armada</h3>
<p>Beyond the granite breakwaters and iron chain-boom of Kordova's inner harbor lies <strong>The Outer Roadstead</strong>—a deep-water anchorage sheltered from the fiercest Atlantic gales by the submerged granite spine of King Kalenius's ancient causeway. Currently, this roadstead is dominated by the looming silhouettes of <a href="#factions/argossean-grain-fleet" class="wiki-link">The Argossean Grain Fleet</a>. The great carrack <em>The Gilded Sheaf</em> and three massive grain cogs ride at heavy hemp anchors 800 yards from the city's sea-walls, guarded by the patrol galleass <em>The Talon of Bel</em>. The anchorage has become the focal point of the city's desperate hopes and the PC Triumvirate's high-stakes gamble to break the famine.</p>
"""
        if 'The Outer Roadstead &amp; The Anchorage of the Corn Armada' not in kordava_art['content']:
            kordava_art['content'] += kordava_harbor_expansion
            print("Updated kordava article with Outer Roadstead details!")
        for rid in ['argossean-grain-fleet', 'nikolos-voros', 'hook-grain-fleet-heist']:
            if rid not in kordava_art.get('relatedIds', []):
                kordava_art.setdefault('relatedIds', []).append(rid)

    # -------------------------------------------------------------
    # 13. UPDATE META
    # -------------------------------------------------------------
    data['meta']['totalArticles'] = len(data['articles'])
    data['meta']['lastUpdated'] = "2026-10-15T15:10:00.000Z"
    print(f"Total articles now: {data['meta']['totalArticles']}")

    # Write out updated js/data.js
    output_js = "window.WIKI_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(output_js)
    print("Successfully wrote updated js/data.js!")

    # -------------------------------------------------------------
    # 14. UPDATE data/sessions.json (Session 1)
    # -------------------------------------------------------------
    with open('data/sessions.json', 'r', encoding='utf-8') as f:
        sessions = json.load(f)

    # Find Session 1 and enrich it with the grain fleet decision
    s1 = next((s for s in sessions if s.get('sessionNumber') == 1), None)
    if s1:
        s1['title'] = "The Thief's Bargain & The Shadows of the Corn Armada"
        if "grain fleet" not in s1['summary'].lower():
            s1['summary'] += " With Kordova's municipal granaries down to four days of food, the Triumvirate took a bold gamble: they dispatched a formal royal herald to invite Capitán-Commodore Nikolos Voros of the offshore Argossean Grain Fleet to the High Alcázar to 'negotiate grain prices.' In secret, the young monarchs are laying plans to steal the entire 50,000-bushel cargo—either by trapping the Commodore on trumped-up criminal charges in court or by orchestrating a midnight boarding operation with cutthroats from the Night Guild or the Velasco Syndicate."
        
        # Add active threads if not present
        fleet_thread_1 = "The Grain Fleet Summons: Commodore Nikolos Voros and Factor Demetrio Phokas have accepted the royal invitation to negotiate grain prices at the High Alcázar; the PCs must prepare their legal ambush or finalize night-boarding plans."
        fleet_thread_2 = "The Famine Clock: Kordova has less than 96 hours of grain remaining before devastating bread riots erupt across the Lower Wards and The Pit."
        
        if fleet_thread_1 not in s1['activeThreads']:
            s1['activeThreads'].append(fleet_thread_1)
        if fleet_thread_2 not in s1['activeThreads']:
            s1['activeThreads'].append(fleet_thread_2)

        # Update NPC dispositions
        s1['npcDispositions']["Capitán-Commodore Nikolos Voros"] = "Arrogant / Commercial Stance (Awaiting formal audience with 4 armed marines & Factor Demetrio Phokas)"
        s1['npcDispositions']["Factor Demetrio 'The Abacus' Phokas"] = "Nervous / Calculating (Clutching master grain manifests and debt covenants)"
        s1['npcDispositions']["Ambassador Tiberio of Messantia"] = "Smug / Orchestrating (Instructed Voros to reject all royal credit to force the Baracha Strait treaty)"

        with open('data/sessions.json', 'w', encoding='utf-8') as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
        print("Successfully updated data/sessions.json with Grain Fleet developments!")

if __name__ == '__main__':
    main()
