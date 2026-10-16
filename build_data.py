"""
build_data.py - Compiles the full lore and rules from Campaign Setting.docx and Royal Court NPCs.docx into js/data.js
"""

import json

def main():
    articles = []

    # ==========================================
    # 1. CAMPAIGN OVERVIEW ARTICLES
    # ==========================================
    articles.append({
        "id": "campaign-premise",
        "category": "overview",
        "title": "Campaign Premise & World Parameters",
        "subtitle": "A Realm Shattered by Decadence, Puppetmasters, and Eldritch Hubris",
        "tags": ["Overview", "Period VIII", "The Triumvirate", "Core Themes"],
        "aliases": ["Campaign Premise", "Premise", "World Parameters", "Our Kingdom Come"],
        "summary": "Set within ancient pre-deluvial Zingara, the PCs are the newly installed Triumvirate: inexperienced descendants of King Ancillus I installed as puppet rulers over a bankrupt, besieged kingdom rotted by necromancy.",
        "content": """
<h3>1.1 High-Concept Campaign Premise</h3>
<p><strong>A Realm Shattered by Decadence and Eldritch Hubris.</strong> Set within the pre-deluvial, sword-and-sorcery epoch of ancient Zingara, <em>Our Kingdom Come</em> paints a dark portrait of a decadent, fallen nation rotting under the cumulative horrors of ancient sorcery, industrial necromantic exploitation, and cosmic ruin. Emerging from a complex ethnic synthesis—where pastoral Zingg Valley agriculturalists merged with conquering Pictish tribes and invading Hyborian warriors—Zingara stands as a land of sharp, irreconcilable contrasts. Flamboyant chivalric pageantry, touchy aristocratic honor, and soaring sea-facing bastions directly overlook rat-infested alleys, reeking industrial zombie pits, and subterranean abysses.</p>

<p><strong>The Ascendancy Trap and Shadowed Puppetmasters.</strong> The primary narrative engine of the campaign centers on an operational crisis of political manipulation, bankruptcy, and decay: the Player Characters are the newly installed rulers—a <strong>Triumvirate</strong> of blood-related descendants of <a href="#history/ancillus-i" class="wiki-link">King Ancillus I</a>—who have inherited a bankrupt, besieged kingdom lingering on the edge of utter collapse. Installed following a bloody civil war by a shadowy cabal of monarchist elites (the <a href="#factions/restoration-council" class="wiki-link">Restoration Council</a> and the head of the royal army, <a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a>), the PCs' ascension is not a victory, but a calculated trap. Their handlers view the untested rulers as weak, inexperienced stand-ins meant to bear public blame for the realm's desperate financial debts and social collapse while the Council rules from behind the throne.</p>

<div class="gm-callout">
<div class="gm-badge">GM CONFIDENTIAL &bull; ASCENDANCY TRAP</div>
<p>The PCs were specifically chosen by <a href="#npcs/valenza" class="wiki-link">General Valenza</a> and <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio de Sadoria</a> because their bloodline grants royal legitimacy, but their youth and lack of court experience make them seemingly easy to manipulate. The Treasury is empty; the provincial Grandees refuse to pay taxes; the Church of Nemeth demands a holy purge; and republican insurgents are plotting in The Pit. The handlers expect the Triumvirate to fail and take the blame, allowing the Council to seize direct authoritarian control.</p>
</div>

<h3>1.2 Canonical Worldbuilding Parameters</h3>
<ul>
  <li><strong>Epoch & Tone:</strong> Period VIII (The Besieged Kingdom). Gritty, lethal sword-and-sorcery with deep political intrigue, swashbuckling martial flair, and cosmic horror.</li>
  <li><strong>Core Tension:</strong> Sovereign Monarchs vs. Shadowy Handlers. Can the young Triumvirate break their puppet strings before the kingdom tears itself apart?</li>
  <li><strong>Pundonor (Aristocratic Honor):</strong> A rigid, hypersensitive code of conduct where any perceived insult must be answered by rapier duels at dawn.</li>
  <li><strong>Industrial Necromancy:</strong> Memory-retaining undead used as forced labor in toxic mining pits, creating severe economic reliance and explosive moral crises.</li>
  <li><strong>Cataclysmic Relics:</strong> Pre-Cataclysmic weapons of godlike power—such as the <a href="#relics/black-blade" class="wiki-link">Black Blade of Azur</a> and the <a href="#relics/obsidian-blade" class="wiki-link">Obsidian Blade</a>—buried beneath the city.</li>
</ul>
""",
        "gmSecrets": "The handlers deliberately provoked the Treasury crisis to ensure the PCs cannot recruit an independent personal army without uncovering secret wealth or defying the Council.",
        "relatedIds": ["valenza", "sadoria", "triumvirate-guide", "restoration-council", "period-viii"]
    })

    articles.append({
        "id": "triumvirate-guide",
        "category": "overview",
        "title": "The Triumvirate & Sandbox Directives",
        "subtitle": "Game Master Execution Guide for Running Ruler PCs",
        "tags": ["Overview", "PCs", "GM Directives", "Mechanics"],
        "aliases": ["Triumvirate", "The Triumvirate", "Sandbox Directives", "GM Directives"],
        "summary": "Guidelines for running the campaign with the PCs as co-rulers: tracking Crown Sovereignty, handling Council pressure, managing the Pundonor economy, and balancing sandbox freedom.",
        "content": """
<h3>1.3 Game Master Execution & Sandbox Directives</h3>
<p>Running a kingdom-ruling sandbox campaign requires balancing macro-level kingdom decisions with intimate, lethal swashbuckling adventures. The PCs must not sit passively on their thrones—their handlers ensure that resources are blocked unless the PCs venture into the shadows themselves.</p>

<div class="info-card">
<h4>Three Pillars of Ruler Play</h4>
<ol>
  <li><strong>Covert Sovereign Operations:</strong> Because the <a href="#factions/restoration-council" class="wiki-link">Restoration Council</a> and <a href="#factions/military-elite" class="wiki-link">Military Elite</a> monitor official crown movements, the PCs must frequently slip out of the palace in disguise to conduct clandestine meetings, investigate conspirators, and explore the ancient subterranean ruins beneath <a href="#gazetteer/kordava" class="wiki-link">Kordava</a>.</li>
  <li><strong>The Sovereign Sovereignty Clock:</strong> Track the Triumvirate's political independence. Every victory against their handlers, recovered relic, or independent revenue source grants <em>Crown Sovereignty</em>; every concession or public humiliation tightens the Council's leash.</li>
  <li><strong>The Lethal Courtroom:</strong> Court is not a safe haven—it is a dueling ground. Grandees will publicly test the PCs' courage using <a href="#rules/pundonor" class="wiki-link">Pundonor</a> honor-baiting. Refusing a duel damages the crown's legitimacy; accepting risks blade-point death.</li>
</ol>
</div>

<div class="gm-callout">
<div class="gm-badge">GM DIRECTIVE &bull; MULTI-FRONT PRESSURES</div>
<p>At any given moment, the Triumvirate faces four simultaneous pressures:</p>
<ul>
  <li><strong>The Financial Stranglehold:</strong> <a href="#npcs/sadoria" class="wiki-link">Marquis Murzio</a> controls the treasury keys and withholds stipends.</li>
  <li><strong>The Military Leash:</strong> <a href="#npcs/valenza" class="wiki-link">General Valenza</a> controls the city garrisons and gate guards.</li>
  <li><strong>The Subterranean Threat:</strong> The <a href="#factions/republican-insurgents" class="wiki-link">Republican Insurgents</a> in <a href="#gazetteer/the-pit" class="wiki-link">The Pit</a> possess evidence of Council murder.</li>
  <li><strong>The Fanatical Purge:</strong> <a href="#npcs/malachai" class="wiki-link">Father Malachai</a> and the <a href="#factions/church-of-nemeth" class="wiki-link">Church of Nemeth</a> demand the complete slaughter of all state necromancers and thralls.</li>
</ul>
</div>
""",
        "gmSecrets": "Encourage players to use their dual status: by day, issuing royal edicts and hosting envoys; by night, dueling in the alleys of Kordava or delving into the ruins of The Pit.",
        "relatedIds": ["campaign-premise", "valenza", "sadoria", "the-pit", "pundonor"]
    })

    # ==========================================
    # 2. ACTIVE ROYAL COURT NPCS (8 DOSSIERS)
    # ==========================================
    npcs_data = [
        {
            "id": "valenza",
            "name": "General Don Rodorigo de Valenza",
            "title": "Head of the Royal Army & Chief Military Handler",
            "faction": "Military Elite / Restoration Council",
            "tags": ["Puppetmaster", "Military Elite", "Restoration Council", "Caballeros"],
            "aliases": ["Don Rodorigo", "General Valenza", "Rodorigo de Valenza", "Head of the Royal Army"],
            "appearance": "A towering, battle-scarred veteran encased in gilded, mirror-polished steel plate armor, draped in a heavy crimson velvet cloak trimmed with black wolf fur. He keeps one hand permanently rested on the pommel of a broad-bladed Zingaran longsword.",
            "mannerisms": "Unnervingly unblinking gaze; rhythmically taps his armored gauntlet against his sword hilt whenever a young noble or PC speaks.",
            "quote": "Crowns are forged in dragon-fire and welded with blood, my young Lieges. Do not presume your silk robes grant you command over the iron that keeps your throats uncut.",
            "courtDCs": "DC 16 Insight to detect hidden political motives; DC 18 Persuasion to push past his dismissive military deflection.",
            "publicPersona": "Outwardly presents himself as a stern, unyielding aristocratic protector of Zingara, a grandee of heavy cavalry (caballeros), and the primary defender of the young Triumvirate. He maintains a posture of selfless martial devotion, appearing at court in polished armor to reassure the realm that the crown is safe under his iron guard.",
            "secretAgenda": "General Don Rodorigo's primary objective is to maintain absolute, unquestioned control over the Zingaran armed forces while keeping the Triumvirate completely dependent on his garrisons for physical survival. Furthermore, he harbors a deadly secret from Period VI: following the fall of the Church of Nemeth, he co-engineered the secret assassination of the primary republican leader during a victory conference and successfully framed the Church for the murder. If this conspiracy is exposed, it would reunite the republicans and shatter his authority.",
            "rival": "Fencing Master Luzaia 'The Mariposa' de Vegara",
            "hooks": [
                {
                    "title": "The Concealed Execution Order",
                    "premise": "General Don Rodorigo requests the Triumvirate sign an official royal decree mobilizing troops to purge a 'rebel encampment' in the Zingg Valley. In reality, the camp houses surviving witnesses to the Period VI assassination of the republican founder.",
                    "conflict": "The PCs must decide whether to rubber-stamp the order to maintain Don Rodorigo's favor, or delay the decree to dispatch covert agents (or personally travel to the Zingg Valley) to investigate who is actually in the camp.",
                    "dcs": "DC 15 Investigation/Insight (uncover true identity of target camp); DC 16 Command/Persuasion (countermand military orders).",
                    "escalation": "If the PCs delay signing the decree for more than 24 hours, Don Rodorigo executes the operation using his private household guard, citing 'emergency crown preservation,' and places the PCs' royal quarters under protective lockdown."
                },
                {
                    "title": "The Insurgent's Evidence",
                    "premise": "Republican agents in The Pit contact the PCs, claiming to possess written correspondence proving General Don Rodorigo ordered the Period VI political assassination.",
                    "conflict": "The PCs must choose whether to buy the evidence using limited royal funds to gain blackmail leverage over their military handler, or alert Don Rodorigo to the cell's location to secure his immediate military loyalty against foreign raiders.",
                    "dcs": "DC 16 Stealth/Deception (slip past military watchers); DC 15 History (verify authenticity of Period VI seals).",
                    "escalation": "If the PCs attempt to negotiate with the republicans without bringing personal guards, a royal army strike team ambushes the meeting location to destroy the documents and silence all parties."
                }
            ]
        },
        {
            "id": "sadoria",
            "name": "High Chancellor Marquis Murzio de Sadoria",
            "title": "Chief Monarchist & Head of the Restoration Council",
            "faction": "Restoration Council / Bureaucracy",
            "tags": ["Puppetmaster", "Restoration Council", "Grandee", "Bureaucrat"],
            "aliases": ["Marquis Murzio", "Murzio de Sadoria", "High Chancellor", "Chief Monarchist"],
            "appearance": "An aristocratic statesman in his late fifties, dressed in an impeccably tailored black velvet doublet embroidered with silver thread, crowned with an ermine-lined mantle. Slender, soft-handed, and wearing three signet rings bearing pre-Cataclysmic heraldry.",
            "mannerisms": "Speaks in smooth, measured cadences; steeples his fingers while listening, offering patronizing smiles that never reach his cold, calculating grey eyes.",
            "quote": "A kingdom is not ruled by steel, Your Majesties, but by ledgers, grain tallies, and patience. Leave the vulgarity of statecraft to those who bled to place that crown upon your brow.",
            "courtDCs": "DC 17 Insight to pierce his patronizing flattery; DC 16 Deception to conceal sovereign intentions from his interrogation.",
            "publicPersona": "The devoted elder statesman, administrative guide, and protective mentor of the inexperienced Triumvirate. He projects the aura of an exhausted patriot bearing the heavy burden of the realm's immense bankruptcy.",
            "secretAgenda": "Marquis Murzio intends to maintain complete financial paralysis over the Triumvirate. By strictly controlling the crown's purse strings, he hoards state revenues within private Council-controlled vaults and starves royal projects. He also seeks to eliminate the surviving provincial Grandees' autonomy by forcing them into debt through predatory crown loans.",
            "rival": "High Duke Gonzalgo de Guarralid",
            "hooks": [
                {
                    "title": "The Treasury Lockout",
                    "premise": "When the Triumvirate attempts to allocate funds for independent city watch recruitment, Marquis Murzio calmly informs them that crown coffers are completely dry, citing foreign debt payments owed to Argos.",
                    "conflict": "The PCs must find a way to finance their rule without Council permission: raid an illicit black-market smuggling den in The Pit, audit Murzio's private provincial tax records, or negotiate a risky loan with foreign merchants.",
                    "dcs": "DC 16 Investigation (audit treasury scrolls to detect missing gold); DC 17 Persuasion/Intimidation (confront Murzio with proof of embezzled revenues).",
                    "escalation": "If confronted directly without unassailable proof, Murzio retaliates by cutting the royal palace's servant and food budgets, claiming 'extreme wartime austerity.'"
                },
                {
                    "title": "The Venomous Reminder",
                    "premise": "A loyal royal taster or servant collapses during a court banquet from a slow-acting, paralytic poison. A cryptic note left in the servant's pocket warns the PCs against meddling with provincial tax collectors.",
                    "conflict": "The PCs must discreetly treat the victim and trace the poison's origin without letting Marquis Murzio's spies learn that they have identified the toxin as originating from his ancestral estate in Sadoria.",
                    "dcs": "DC 14 Medicine/Arcana (identify the rare Sadorian belladonna derivative); DC 15 Stealth (intercept the courier who delivered the vial).",
                    "escalation": "Failure to identify the poison within 6 hours leaves the loyal retainer permanently paralyzed, depriving the PCs of their only trustworthy informant in the palace kitchens."
                }
            ]
        },
        {
            "id": "lucia",
            "name": "Fencing Master Luzaia 'The Mariposa' de Vegara",
            "title": "Commander of the Republican Insurgent Network",
            "faction": "Republican Insurgents (The Pit)",
            "tags": ["Rebel", "Republican Insurgents", "Fencer", "The Pit"],
            "aliases": ["La Mariposa", "Luzaia de Vegara", "Luzaia", "Fencing Master Luzaia"],
            "appearance": "A lithe, athletic woman in her late twenties, wearing dark cordwain dueling leathers, a hooded charcoal cloak, and a wide leather baldric supporting a masterwork Zingaran rapier and parrying dagger. A thin dueling scar crosses her left cheekbone.",
            "mannerisms": "Constantly shifts her balance lightly between the balls of her feet, as if anticipating a sudden lunge; speaks with sharp, irreverent wit.",
            "quote": "You wear the golden band of Ancillus, children, but in The Pit, gold does not stop cold steel. Prove you are sovereigns of the people, or bleed like the tyrants before you.",
            "courtDCs": "DC 15 Insight to gauge the sincerity of her truce offers; DC 16 Persuasion to convince her that the Triumvirate is not complicit in Council crimes.",
            "publicPersona": "In elite court circles, Luzaia poses as a sought-after private fencing tutor for high-born noble daughters, navigating elite salons with charming wit and flawless etiquette.",
            "secretAgenda": "As 'La Mariposa,' she commands the clandestine republican insurgent cells operating out of The Pit. Her life goal is the complete destruction of the feudal monarchy and the Restoration Council. She possesses fragment evidence that General Valenza murdered the republican founder during Period VI.",
            "rival": "General Don Rodorigo de Valenza",
            "hooks": [
                {
                    "title": "The Insurgent's Bargain",
                    "premise": "Luzaia arranges a clandestine midnight rendezvous with the PCs in an abandoned crypt beneath Kordava, offering to supply critical intelligence on Council troop movements in exchange for royal pardons for her cell commanders.",
                    "conflict": "The PCs must weigh allying with a known revolutionary against the danger of treason accusations if General Valenza's spies uncover the meeting.",
                    "dcs": "DC 16 Stealth (reach the crypt meeting without being followed by crown watchmen); DC 14 Insight (verify Luzaia is not leading them into a kidnapping trap).",
                    "escalation": "If royal guards patrol nearby during the exchange, Luzaia assumes betrayal, engages the PCs in a non-lethal fencing duel, and vanishes into the labyrinth of The Pit."
                },
                {
                    "title": "Sabotage in the Iron Mines",
                    "premise": "Luzaia's underground saboteurs plant alchemical explosives in a crown-controlled iron mine worked by industrial thralls near Jerida, threatening to collapse the facility unless the crown releases captured republican prisoners.",
                    "conflict": "The Triumvirate must intervene personally to negotiate a hostage exchange or disarm the explosives before the collapse destroys a vital royal revenue stream.",
                    "dcs": "DC 15 Athletics/Acrobatics (navigate the unstable mining shafts); DC 16 Arcana/Thievery (safely defuse the alchemical timing runes).",
                    "escalation": "Detonation causes a cave-in that releases dozens of enraged, memory-retaining mining thralls into the lower valleys, devastating nearby villages."
                }
            ]
        },
        {
            "id": "malachai",
            "name": "Father Malachai the Blind",
            "title": "High Priest of the Underground Church of Nemeth the Gnostic",
            "faction": "Church of Nemeth the Gnostic",
            "tags": ["Priest", "Zealot", "Church of Nemeth", "Theocrat"],
            "aliases": ["Father Malachai", "Malachai", "High Priest of Nemeth"],
            "appearance": "An emaciated, hollow-cheeked zealot cloaked in ragged, unbleached wool vestments cinched with a knotted hemp rope. A heavy white linen blindfold covers his scarred, sightless eye sockets. He carries a gnarled staff of petrified ash topped with an archaic bronze sun.",
            "mannerisms": "Tilts his head sharply when listening, as if hearing divine whispers; speaks in a raspy, hypnotic cadence that rises into furious scripture.",
            "quote": "The flesh of the dead rots the soul of the living! Cleanse this cursed kingdom in the fire of Nemeth, or drown in the reeking tide of your own abominations!",
            "courtDCs": "DC 14 Insight to distinguish between divine prophecy and manic fanaticism; DC 17 Religion to debate theological scripture and calm his zealotry.",
            "publicPersona": "A harmless, reclusive mendicant holy man wandering the outskirts of Kordava, tending to destitute beggars and preaching temperance and repentance.",
            "secretAgenda": "Malachai leads the fanatical underground remnants of the Church of Nemeth the Gnostic. He seeks to completely eradicate necromancy, overthrow the secular monarchy, and restore the theocracy that ruled Zingara in Period VI. He is obsessed with finding the lost Fountain of Youth in the Rabirian Mountains.",
            "rival": "Master Alchemist Vane",
            "hooks": [
                {
                    "title": "Waters of the Fallen Shrine",
                    "premise": "Father Malachai sends an emissary to the PCs, offering a divine tincture capable of curing an eldritch illness afflicting one of their loyal courtiers, in exchange for royal protection for a hidden Gnostic shrine in the Rabirian Mountains.",
                    "conflict": "The shrine is currently under siege by Argossean mercenaries hired by rival nobles. The PCs must decide whether to dispatch crown forces to protect the heretical shrine or seize the holy relic for themselves.",
                    "dcs": "DC 15 Survival (guide a relief party through treacherous Rabirian mountain passes); DC 17 Religion (interpret the ancient scripture required to unlock the shrine's inner sanctuary).",
                    "escalation": "If the shrine falls to the mercenaries, the holy spring is tainted with venom, unleashing an outbreak of virulent spiritual plague across the southeastern provinces."
                },
                {
                    "title": "The Purging of Edmund's Pits",
                    "premise": "Fanatical Gnostic cultists launch a suicidal raid on an industrial zombie pit overseen by Master Alchemist Vane, setting chemical storage vats ablaze and causing toxic vapors to flood residential districts.",
                    "conflict": "The PCs must contain the toxic blaze, prevent Vane's guards from slaughtering peaceful pilgrims caught in the crossfire, and decide whether to prosecute Malachai's zealots or condemn Vane's necromancy.",
                    "dcs": "DC 14 Constitution Save (resist toxic alchemical fumes); DC 16 Persuasion/Command (force both sides to disengage and extinguish the fire).",
                    "escalation": "Failing to stop the fire within 4 rounds causes a catastrophic chemical explosion that permanently destroys the pit and irradiates the district with necromantic blight."
                }
            ]
        },
        {
            "id": "gonzalo-guarralid",
            "name": "High Duke Gonzalgo de Guarralid",
            "title": "Spokesman of the Grandee Coalitions & Lord of the Highland Estates",
            "faction": "Grandee Coalitions (Eastern League)",
            "tags": ["Grandee", "Nobility", "Pundonor", "Highland"],
            "aliases": ["Gonzalgo de Guarralid", "Duke Gonzalgo", "High Duke Gonzalgo", "Guarralid"],
            "appearance": "A broad-shouldered, barrel-chested aristocrat in his early forties, sporting a waxed handlebar mustache and wearing a lavish saffron-and-black slashed silk doublet over a damascened steel breastplate. Plumed felt hat perched arrogantly on his head.",
            "mannerisms": "Boisterous, booming laugh; places his hand on his rapier hilt at the slightest hint of disrespect, eager to demand satisfaction under pundonor.",
            "quote": "The blood of Guarralid flowed in these valleys before Ancillus learned to walk. Do not presume a circlet of gold makes you master of the mountain iron that forged it.",
            "courtDCs": "DC 15 Insight to identify when his swagger masks genuine political anxiety; DC 16 History to cite ancestral treaties that validate crown authority over his fief.",
            "publicPersona": "The epitome of traditional Zingaran chivalry and martial pride. He portrays himself as the champion of provincial noble liberties against royal overreach and foreign contamination.",
            "secretAgenda": "Gonzalgo heads the Eastern Grandee League, a loose confederation of provincial lords committed to weakening central crown authority. He hoards iron and silver revenues from his mountain mines, refuses crown taxes, and seeks to force the Triumvirate into recognizing absolute provincial autonomy. He uses pundonor challenges to publicly humiliate crown officials.",
            "rival": "High Chancellor Marquis Murzio de Sadoria",
            "hooks": [
                {
                    "title": "The Challenge of Pundonor",
                    "premise": "During a grand royal reception, Duke Gonzalgo publicly mocks the Triumvirate's youth and tactical inexperience, challenging the most martial PC to a formal first-blood fencing duel at dawn.",
                    "conflict": "Refusing the duel inflicts a permanent -2 penalty to all future social and command checks with Zingaran nobility; accepting risks humiliating public defeat or death against a seasoned swordsman.",
                    "dcs": "DC 16 Fencing / Attack Roll Contest (fight Gonzalgo to first blood); DC 17 Persuasion (reframe the insult into an honorable sporting trial with non-lethal conditions).",
                    "escalation": "If a PC scores a critical success or disarms Gonzalgo with spectacular flair, the Duke's wounded pride transforms into grudging respect, granting temporary Grandee political backing."
                },
                {
                    "title": "The Tax Revolt of Jerida",
                    "premise": "Duke Gonzalgo orders his private garrison in Jerida to seize royal barges carrying timber and ore along the Thunder River, declaring an embargo until the crown cuts provincial customs tariffs.",
                    "conflict": "The PCs must travel to Jerida to break the standoff through military intimidation, clever economic compromise, or covert sabotage of Gonzalgo's supply lines.",
                    "dcs": "DC 15 Intimidation (rally local merchants against Gonzalgo's embargo); DC 14 Deception/Stealth (smuggle crown goods past the river blockade).",
                    "escalation": "Failure to resolve the embargo within 3 days triggers an armed clash between royal army detachments and Gonzalgo's retainers, threatening full civil war."
                }
            ]
        },
        {
            "id": "vesper",
            "name": "Vesper the Key-Master",
            "title": "Guildmaster of the Shadowed Key & Spymaster of The Pit",
            "faction": "The Pit Underworld / Smugglers",
            "tags": ["Spymaster", "Underworld", "The Pit", "Smuggler"],
            "aliases": ["Vesper", "Key-Master", "The Key-Master"],
            "appearance": "A wiry, nondescript figure of ambiguous age, wrapped in a mottled grey cloak lined with dozens of hidden pockets, skeleton keys, and small vials. Wears soft leather gloves with reinforced fingertips and a half-mask of blackened silver concealing severe burn scars.",
            "mannerisms": "Speaks in a quiet, dry whisper; constantly manipulates a complex brass puzzle-lock between his fingers with uncanny dexterity.",
            "quote": "Every door in Zingara has a key, Your Majesties. Some are forged of iron, some of gold, and some of dark secrets whispered in the dark. My price is always the same: information.",
            "courtDCs": "DC 16 Insight to detect hidden motives behind his transactions; DC 15 Sleight of Hand to spot his pocketed eavesdropping devices.",
            "publicPersona": "Maintains no public presence at court whatsoever. In upper Kordava, he is whispered of as an urban myth—a spectral broker of illicit antiquities and stolen secrets.",
            "secretAgenda": "Vesper controls the subterranean black markets and smuggling tunnels of The Pit. He hoards pre-Cataclysmic artifacts salvaged from the sunken ruins of old Kordava and sells intelligence to the highest bidder. He maintains a secret entrance into the submerged mausoleum of King Kalenius, seeking to plunder the ancient tomb.",
            "rival": "General Don Rodorigo de Valenza",
            "hooks": [
                {
                    "title": "The Tomb of King Kalenius",
                    "premise": "Vesper approaches the PCs through a secret passage in the palace wine cellar, offering a map to the forgotten crypt of King Kalenius beneath Kordava's harbor in exchange for royal immunity for his smuggling guild.",
                    "conflict": "The crypt contains legendary pre-Cataclysmic weapons and the dormant Final Guard (one thousand animate stone warriors), but entering requires diving into flooded tunnels infested with aquatic ghoul constructs.",
                    "dcs": "DC 16 Athletics/Swimming (navigate flooded abyssal tunnels); DC 15 Arcana (decode the Thurian glyphs sealing the mausoleum gate).",
                    "escalation": "Disturbing the crypt without the proper ritual key awakens six stone guardians who attack relentlessly until subdued or sealed back behind the stone gate."
                },
                {
                    "title": "Black-Market Espionage",
                    "premise": "Vesper offers to sell the PCs a stolen correspondence ledger revealing that Ambassador Tiberio of Messantia is bribing royal harbor officials to permit illegal Argossean arms shipments into Zingara.",
                    "conflict": "The PCs must decide whether to pay Vesper's exorbitant fee, attempt to steal the ledger from his fortified safehouse in The Pit, or trade a sensitive royal secret in exchange.",
                    "dcs": "DC 16 Stealth/Thievery (infiltrate Vesper's trap-laden subterranean vault); DC 15 Persuasion/Barter (negotiate a reduced price using royal trade concessions).",
                    "escalation": "Triggering a security ward inside Vesper's safehouse fills the vault with knockout gas and alerts a squad of mute assassin thralls who attempt to capture the intruders."
                }
            ]
        },
        {
            "id": "vane",
            "name": "Master Alchemist Vane",
            "title": "Overseer of the Royal Labor Pits & Crown Necromancer",
            "faction": "Crown Necromantic Apparatus",
            "tags": ["Necromancer", "Alchemist", "Zombie Pits", "Crown Official"],
            "aliases": ["Master Vane", "Alchemist Vane", "Vane"],
            "appearance": "A gaunt, sallow-skinned scholar in his late forties, smelling intensely of vinegar, sulfur, and embalming resins. Wears a lead-lined leather apron over dark scholarly robes, with heavy tinted glass goggles pushed up onto his bald pate. His fingers are permanently stained deep indigo from alchemical reagents.",
            "mannerisms": "Nervous, jerky movements; compulsively sniffs his fingers and wipes chemical residue onto a stained rag while rambling about labor efficiency metrics.",
            "quote": "The dead do not unionize, Your Grace. They do not demand bread, they do not conspire for republics, and they do not weep when the mine collapses. They are the only loyal subjects you have left.",
            "courtDCs": "DC 14 Insight to recognize when his scientific detachment conceals frantic panic over supply shortages; DC 16 Arcana to evaluate the stability of his preservation compounds.",
            "publicPersona": "Presents himself as a tireless, dispassionate royal civil servant whose alchemical innovations in preserved labor are the only thing preventing the kingdom's complete economic collapse.",
            "secretAgenda": "Vane is obsessed with unlocking the secrets of Period IV master necromancer Edmund and recovering the legendary Obsidian Blade. He conducts unsanctioned experiments on memory-retaining thralls to discover how to bind their wills permanently without decay, secretly using political dissidents supplied by General Valenza as test subjects.",
            "rival": "Father Malachai the Blind",
            "hooks": [
                {
                    "title": "The Reeking Pits of Edmund",
                    "premise": "A containment vat fails at Pit #4 near Jerida, unleashing an alchemical sludge spill that threatens to dissolve the support timbers of the main iron shaft and turn dozens of thralls into feral horrors.",
                    "conflict": "Vane pleads with the Triumvirate to personally authorize the deployment of royal alchemical stockpiles to neutralize the sludge before word leaks to the Church of Nemeth.",
                    "dcs": "DC 14 Arcana/Crafting (stabilize the chemical counter-agent); DC 15 Constitution Save (endure noxious fumes while securing the containment sluice).",
                    "escalation": "Failure to contain the leak within 1 hour causes the slurry to seep into the local water table, turning downstream livestock and villagers into diseased ghoul-like abominations."
                },
                {
                    "title": "The Obsidian Awakening",
                    "premise": "Vane claims to have located an underground fissure beneath The Pit that leads to the tomb of Mad King Daedalus, where the Obsidian Blade is buried. He requests a detachment of crown guards to assist in an excavation expedition.",
                    "conflict": "The PCs must decide whether to sanction the dangerous expedition to claim the ultimate necromantic weapon, knowing it could trigger another starfall anomaly or awaken Daedalus himself.",
                    "dcs": "DC 16 Arcana/History (identify Daedalus's ancient sealing wards); DC 15 Survival (navigate unstable subterranean ruins prone to tremors).",
                    "escalation": "Breaching the outer seal unleashes an eldritch psychic shockwave that drives nearby mortal guards temporarily mad, forcing the PCs to subdue their own men while defending against emerging crypt horrors."
                }
            ]
        },
        {
            "id": "tiberio",
            "name": "Ambassador Tiberio of Messantia",
            "title": "Special Envoy of the Kingdom of Argos",
            "faction": "Kingdom of Argos / Foreign Envoy",
            "tags": ["Diplomat", "Argos", "Foreign Power", "Trader"],
            "aliases": ["Ambassador Tiberio", "Tiberio", "Envoy Tiberio"],
            "appearance": "A suave, handsome nobleman in his early thirties with olive skin, impeccably groomed dark curls, and a perfumed goatee. Wears a flowing Argossean silk tunic of sea-green and gold, draped with heavy gold chains set with sapphires and pearls.",
            "mannerisms": "Warm, disarming smile; gestures gracefully with rings on both hands; speaks Zingaran with a musical Argossean accent that flatters listeners.",
            "quote": "Zingara and Argos are like two sisters sharing the same stormy sea, my Lieges. Why quarrel over barren border rocks when our combined merchant galleys could command the wealth of the Western Ocean?",
            "courtDCs": "DC 17 Insight to pierce his warm diplomatic charm and detect calculating economic exploitation; DC 16 Deception to feign economic strength during trade negotiations.",
            "publicPersona": "The generous, cosmopolitan ambassador from Zingara's wealthy neighbor, offering low-interest merchant loans, grain shipments, and cultural exchange to stabilize the fragile Triumvirate.",
            "secretAgenda": "Tiberio's true mission is economic vassalage. He seeks to exploit Zingara's bankruptcy by locking the crown into predatory maritime trade concessions, seizing control of the Baracha Strait, and gathering tactical intelligence on Zingara's coastal defenses for the Argossean Admiralty.",
            "rival": "Vesper the Key-Master",
            "hooks": [
                {
                    "title": "Blood in the Cauldron",
                    "premise": "Tiberio delivers an ultimatum from the Argossean senate: return the signet ring of an Argossean diplomat slaughtered during Period V, or face an immediate naval embargo of Kordava's harbor.",
                    "conflict": "The signet ring is currently held by an ancient, memory-retaining thrall trapped in an earthquake-exposed crypt beneath the palace. The PCs must infiltrate the crypt in secret to recover the ring before the deadline expires.",
                    "dcs": "DC 15 History/Arcana (unravel crypt ward runes); DC 17 Persuasion (convince the memory-retaining thrall to relinquish the signet peacefully).",
                    "escalation": "If the deadline passes, Argossean warships blockade the mouth of the Black River, cutting off all coastal food imports and sparking bread riots in Kordava."
                },
                {
                    "title": "The Barachan Maritime Deal",
                    "premise": "Tiberio secretly approaches the PCs with an offer to finance a new royal naval squadron, provided the Triumvirate grants Argossean privateers free hunting rights against Barachan pirate vessels in Zingaran waters.",
                    "conflict": "Accepting the deal grants immediate naval strength, but severely antagonizes the Barachan pirate cartels, who threaten to retaliate by raiding Zingara's defenseless coastal fishing towns.",
                    "dcs": "DC 16 Persuasion/Barter (negotiate restrictive clauses that protect Zingaran merchant shipping); DC 15 Insight (spot hidden loopholes in the maritime treaty).",
                    "escalation": "Signing the treaty without modifying its terms provokes a coordinated pirate raid on the coastal town of Shar, burning the harbor and taking dozens of hostages."
                }
            ]
        }
    ]

    for n in npcs_data:
        # Build HTML content for NPC
        hooks_html = ""
        for h in n["hooks"]:
            hooks_html += f"""
<div class="hook-card">
  <h4>{h['title']}</h4>
  <p><strong>Premise:</strong> {h['premise']}</p>
  <p><strong>Core Conflict & Player Choice:</strong> {h['conflict']}</p>
  <div class="dc-box">
    <strong>Suggested Skill Checks:</strong> {h['dcs']}
  </div>
  <p class="escalation"><strong>Dynamic Escalation Trigger:</strong> {h['escalation']}</p>
</div>
"""
        content_html = f"""
<div class="npc-header-card">
  <div class="npc-meta">
    <span class="badge faction-badge">{n['faction']}</span>
    <span class="badge rival-badge">Primary Rival: {n['rival']}</span>
  </div>
  <div class="at-a-glance-grid">
    <div class="glance-item"><strong>Appearance:</strong> {n['appearance']}</div>
    <div class="glance-item"><strong>Mannerisms:</strong> {n['mannerisms']}</div>
    <div class="glance-item quote"><strong>Iconic Quote:</strong> &ldquo;{n['quote']}&rdquo;</div>
    <div class="glance-item dcs"><strong>Court Social DCs:</strong> {n['courtDCs']}</div>
  </div>
</div>

<h3>Public Persona</h3>
<p>{n['publicPersona']}</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>
  <p>{n['secretAgenda']}</p>
</div>

<h3>Player-Led Plot Hooks</h3>
{hooks_html}
"""
        articles.append({
            "id": n["id"],
            "category": "npcs",
            "title": n["name"],
            "subtitle": n["title"],
            "tags": n["tags"],
            "aliases": n["aliases"],
            "summary": f"{n['title']} ({n['faction']}). {n['publicPersona'][:150]}...",
            "atAGlance": {
                "appearance": n["appearance"],
                "mannerisms": n["mannerisms"],
                "quote": n["quote"],
                "courtDCs": n["courtDCs"],
                "publicStance": n["publicPersona"][:120] + "...",
                "secretAgenda": n["secretAgenda"],
                "rival": n["rival"]
            },
            "content": content_html,
            "gmSecrets": n["secretAgenda"],
            "relatedIds": [r for r in ["valenza", "sadoria", "lucia", "malachai", "gonzalo-guarralid", "vesper", "vane", "tiberio"] if r != n["id"]]
        })

    # ==========================================
    # 3. COURT RELATIONSHIP MATRIX ARTICLE
    # ==========================================
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
      <th>Secret Agenda / Hidden Lever</th>
      <th>Primary Court Rival</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo de Valenza</a></strong><br><small>Head of Royal Army</small></td>
      <td><span class="badge">Military Elite / Restoration Council</span></td>
      <td>Protective martial defender; loyal guardian of the crown.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Keep PCs dependent on army; conceal Period VI assassination of republican founder.</span></td>
      <td><a href="#npcs/lucia" class="wiki-link">Luzaia de Vegara</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Murzio de Sadoria</a></strong><br><small>Chief Monarchist</small></td>
      <td><span class="badge">Restoration Council / Bureaucracy</span></td>
      <td>Devoted mentor, elder statesman, and administrative guide.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Restrict royal stipend to keep PCs financially paralyzed; hoard state wealth in Council vaults.</span></td>
      <td><a href="#npcs/gonzalo-guarralid" class="wiki-link">Duke Gonzalgo de Guarralid</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/lucia" class="wiki-link">Fencing Master Luzaia 'The Mariposa' de Vegara</a></strong><br><small>Republican Commander</small></td>
      <td><span class="badge">Republican Insurgents (The Pit)</span></td>
      <td>Openly hostile to monarchy; offers conditional secret pacts.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Expose Council's Period VI assassination plot; dismantle feudal monarchy for a republic.</span></td>
      <td><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/malachai" class="wiki-link">Father Malachai the Blind</a></strong><br><small>High Priest of Nemeth</small></td>
      <td><span class="badge">Church of Nemeth the Gnostic</span></td>
      <td>Conditional ally against sorcery; demands religious conversion.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Eradicate all necromancy; clear church's name; find Fountain of Youth to impose divine theocracy.</span></td>
      <td><a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalgo de Guarralid</a></strong><br><small>Grandee Representative</small></td>
      <td><span class="badge">Grandee Coalitions (Eastern League)</span></td>
      <td>Dismissive of young rulers; demands absolute provincial autonomy.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Weaken central crown tariffs; hoard mountain mineral wealth; test crown strength via duels.</span></td>
      <td><a href="#npcs/sadoria" class="wiki-link">Marquis Murzio de Sadoria</a></td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/vesper" class="wiki-link">Vesper the Key-Master</a></strong><br><small>Spymaster of The Pit</small></td>
      <td><span class="badge">Underworld Syndicates / Smugglers</span></td>
      <td>Opportunistic business partner; seller of secrets and relics.</td>
      <td class="gm-only-cell"><span class="gm-mask-text">Maintain control of subterranean Pit; profit from pre-Cataclysmic relics and extortion.</span></td>
      <td><a href="#npcs/valenza" class="wiki-link">General Don Rodorigo</a></td>
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
        "gmSecrets": "The two primary puppetmasters (Valenza and Sadoria) are also secretly in conflict: Valenza wants a military dictatorship, while Sadoria wants an aristocratic oligarchy.",
        "relatedIds": ["valenza", "sadoria", "lucia", "malachai", "guarralid", "vesper", "vane", "tiberio"]
    })

    # ==========================================
    # 4. HISTORICAL FIGURES (DRAMATIS PERSONAE)
    # ==========================================
    historical_figures = [
        {
            "id": "ancillus-i",
            "name": "King Ancillus I",
            "subtitle": "Progenitor Monarch of the Golden Age & Undead Warlord",
            "period": "Period II & Period VII",
            "aliases": ["Ancillus", "King Ancillus", "Ancillus I"],
            "summary": "Progenitor monarch who welcomed elven scholars and founded Kordava's magical academy. In Period VII, he was reanimated as an undead warlord.",
            "desc": "Welcomed ocean-faring elven scholars to Zingara; founded the realm's premier elven-run magical academy in Kordava; established centuries of cultural prosperity. Centuries after his death, his tomb was desecrated by early necromancers in Period III. During Period VII, he was reanimated as a deathless warlord leading a massive zombie horde to reclaim his crown before being defeated by the mortal alliance.",
            "legacy": "His bloodline forms the sole legal basis for royal legitimacy. The PCs derive their right to rule directly from their descent from Ancillus I."
        },
        {
            "id": "printius",
            "name": "Printius",
            "subtitle": "Head of the Magical Academy & Co-Founder of Commercial Necromancy",
            "period": "Period III",
            "aliases": ["Printius"],
            "summary": "Academic leader who abandoned ethical restraints after an earthquake destroyed the academy, partnering with Lord Silkeneth to commercialize undead labor.",
            "desc": "Led the magical academy during its expansion into commercial discovery. Following the cataclysmic earthquake that destroyed the academy and killed the governing council, Printius abandoned all ethical restraints, partnering with Lord Silkeneth to mass-produce zombie thralls for personal wealth.",
            "legacy": "Co-founder of commercialized necromancy; established the techniques used to raise and bind memory-retaining undead."
        },
        {
            "id": "silkeneth",
            "name": "Lord Silkeneth",
            "subtitle": "Mercenary Nobleman & Architect of Industrial Thrall Mercantilism",
            "period": "Period III",
            "aliases": ["Silkeneth", "Lord Silkeneth"],
            "summary": "Zingaran nobleman who partnered with Printius to transform necromancy from an arcane anomaly into a lucrative, profit-driven enterprise.",
            "desc": "Capitalized on the collapse of the academy council to partner with Printius, transforming necromancy from an arcane anomaly into a lucrative, profit-driven enterprise.",
            "legacy": "Established the economic blueprint for industrial undead labor and elevated the Silkeneth family line into dominant historical power brokers."
        },
        {
            "id": "edmund",
            "name": "Edmund the Necromancer",
            "subtitle": "Master Necromancer & Engineer of the Industrial Zombie Pits",
            "period": "Period IV",
            "aliases": ["Edmund", "Master Edmund"],
            "summary": "Grandson of Silkeneth who engineered large-scale industrial zombie pits for mining and hazardous labor across Zingara.",
            "desc": "Educated at the ruined magical academy, Edmund expanded his grandfather's commercial operations by engineering large-scale 'zombie pits' across Kordava's periphery and subterranean reaches, systematically institutionalizing mass undead labor.",
            "legacy": "Responsible for the physical infrastructure of reeking zombie vats and hazardous mining shafts that dot modern Zingara."
        },
        {
            "id": "daedalus",
            "name": "Mad King Daedalus",
            "subtitle": "Tyrannical Monarch of the Starfall & Bearer of the Obsidian Blade",
            "period": "Period V",
            "aliases": ["Daedalus", "Mad King Daedalus", "King Daedalus"],
            "summary": "Tyrant who sacrificed Kordava in a ritual for personal godhood using the Obsidian Blade; trapped eternally in rubble after the Starfall meteor strike.",
            "desc": "Recovered the Obsidian Blade and promised to restore Zingara as the magical capital of the world. Instead, he unleashed a zombie army upon Kordava, sacrificing his entire capital to fuel a ritual for personal godhood. When the Starfall meteor disrupted his ritual, his cosmic lover, Tanatos, trapped him in eternal, conscious imprisonment beneath the city rubble for boring her.",
            "legacy": "Lies buried alive in the rubble beneath The Pit, still holding the Obsidian Blade and bound to his cosmic punishment."
        },
        {
            "id": "fergus",
            "name": "Fergus the Holy Warrior",
            "subtitle": "Last Human King's Guard & Founder of the Church of Nemeth",
            "period": "Period V & VI",
            "aliases": ["Fergus", "Holy Fergus"],
            "summary": "Guard who rebelled against Daedalus, launched a holy crusade in the name of Nemeth the Gnostic to purge zombies, and established theocratic rule.",
            "desc": "Disillusioned by Daedalus's atrocities, he disobeyed royal orders to slaughter foreign envoys, aided the escape of an incognito religious leader, and eloped with his companion. Drawing upon the martyrological myth of the fanatical cult leader who died in ritual fires and hijacked the horde, Fergus launched a post-Starfall holy crusade in the name of Nemeth the Gnostic to drive back the zombie hordes.",
            "legacy": "Revered as the ultimate holy warrior by the underground Church of Nemeth; architect of the theocratic regime that ruled in Period VI."
        },
        {
            "id": "tanatos",
            "name": "Death (Tanatos)",
            "subtitle": "Cosmic Incarnation of Death & Cosmic Tormentor of Daedalus",
            "period": "Period V",
            "aliases": ["Tanatos", "Death"],
            "summary": "Cosmic incarnation of death and lover of King Daedalus who condemned him to eternal conscious imprisonment beneath Kordava because he bored her.",
            "desc": "Present at the dawn of the city sacrifice in Kordava, completely checked out and indifferent to mortal bloodletting. Following the Starfall meteor strike, she personally condemned Daedalus to eternal conscious imprisonment beneath the earth because his megalomania proved tedious and boring.",
            "legacy": "A lingering, terrifying cosmic presence in Zingaran lore, symbolizing the absolute, inescapable end of all things."
        },
        {
            "id": "falmouth",
            "name": "Priest Falmouth",
            "subtitle": "High Priest of Nemeth & Discoverer of the Fountain of Youth",
            "period": "Period VI",
            "aliases": ["Falmouth", "High Priest Falmouth"],
            "summary": "Gnostic priest who discovered the legendary Fountain of Youth in the Rabirian Mountains, securing longevity for the ruling theocracy.",
            "desc": "Discovered the legendary Fountain of Youth in the Rabirian Mountains, securing miraculous physical longevity and divine prestige for the church's ruling priesthood. His era ended when the church was overthrown following a child crucifixion scandal.",
            "legacy": "Left behind hidden, fanatical theocratic cells and the unresolved legend of the lost Fountain of Youth."
        },
        {
            "id": "nemeth",
            "name": "Nemeth the Gnostic",
            "subtitle": "Divine Entity of Holy Magic & Patron of the Underground Faith",
            "period": "Period VI & Modern",
            "aliases": ["Nemeth", "Nemeth the Gnostic"],
            "summary": "Divine figurehead whose teachings inspired the crusade against necromancy; venerated by the outlawed underground Church.",
            "desc": "Inspired Fergus's post-Starfall crusade against the zombie hordes, becoming the central deity of the theocratic regime that governed Zingara in Period VI.",
            "legacy": "Object of fanatical veneration for the outlawed Church of Nemeth, who seek to restore his divine rule over the kingdom."
        }
    ]

    for hf in historical_figures:
        articles.append({
            "id": hf["id"],
            "category": "history",
            "title": hf["name"],
            "subtitle": f"{hf['subtitle']} &bull; {hf['period']}",
            "tags": ["Historical Figure", "Lore", hf["period"]],
            "aliases": hf["aliases"],
            "summary": hf["summary"],
            "content": f"""
<div class="info-card">
  <p><strong>Historical Role:</strong> {hf['subtitle']}</p>
  <p><strong>Era of Prominence:</strong> {hf['period']}</p>
</div>
<h3>Canonical Actions</h3>
<p>{hf['desc']}</p>
<h3>Lasting Legacy on Modern Zingara</h3>
<p>{hf['legacy']}</p>
""",
            "gmSecrets": f"Relics associated with {hf['name']} can be found in the ruins of The Pit or Rabirian Mountains.",
            "relatedIds": ["history-matrix", "campaign-premise", "court-matrix"]
        })

    # ==========================================
    # 5. FACTIONS & POWER BLOCS
    # ==========================================
    factions_data = [
        {
            "id": "restoration-council",
            "name": "Restoration Council",
            "subtitle": "Shadowy Monarchist Cabal & Aristocratic Bureaucracy",
            "leadership": "High Chancellor Marquis Murzio de Sadoria & Grandee Bureaucrats",
            "headquarters": "The Crystal Floor Court & Royal Citadel of Kordava",
            "agenda": "Rule from shadows via the PC Triumvirate, hoard state revenues, crush republican and religious dissent, and keep the crown financially dependent.",
            "vulnerabilities": "Overconfidence in their ability to manipulate the young PCs; secret guilt and blackmail exposure over the Period VI assassination.",
            "tags": ["Faction", "Monarchist", "Puppetmasters", "Council"],
            "aliases": ["Restoration Council", "Council", "Chief Monarchist", "Monarchist Cabal"],
            "summary": "The cabal of monarchist elites who elevated the Triumvirate. They control the treasury, bureaucracy, and public policy from behind the throne."
        },
        {
            "id": "military-elite",
            "name": "The Military Elite & Royal Army Command",
            "subtitle": "Chivalric Caballeros & Professional Garrisons",
            "leadership": "General Don Rodorigo de Valenza",
            "headquarters": "The Citadel Fortress of Kordava & Provincial Garrisons",
            "agenda": "Maintain supreme control over the kingdom's armed forces, crush rebel insurrections, defend borders from Argos, and shelter the Triumvirate under an iron guard.",
            "vulnerabilities": "Command friction caused by arrogant noble officers; secret guilt over Period VI assassination; overstretched garrisons.",
            "tags": ["Faction", "Military", "Army", "Caballeros"],
            "aliases": ["Military Elite", "Royal Army", "Zingaran Army", "Crown Army"],
            "summary": "Commanded by General Valenza. Elite heavy cavalry and disciplined pike blocks that keep the realm safe, but view the PCs as inexperienced figureheads."
        },
        {
            "id": "republican-insurgents",
            "name": "Republican Insurgents",
            "subtitle": "Underground Radical Cells & Fencing Agitators",
            "leadership": "Fencing Master Luzaia 'The Mariposa' de Vegara",
            "headquarters": "The Pit (Subterranean Kordava) & Secret Rural Safehouses",
            "agenda": "Overthrow the feudal monarchy, expose Council war crimes and political assassinations, dismantle thrall labor, and establish a democratic republic.",
            "vulnerabilities": "Fractured command structure post-assassination; lack heavy armor, cavalry, and open battlefield units; reliant on urban ambush tactics.",
            "tags": ["Faction", "Rebels", "Republicans", "The Pit"],
            "aliases": ["Republican Insurgents", "Republicans", "The Pit Rebels", "La Mariposa Cells"],
            "summary": "Decentralized revolutionary network operating from The Pit. Determined to dismantle the monarchy, they hold dangerous proof of Council assassinations."
        },
        {
            "id": "church-of-nemeth",
            "name": "Church of Nemeth the Gnostic",
            "subtitle": "Underground Fanatical Theocracy & Holy Purifiers",
            "leadership": "Father Malachai the Blind",
            "headquarters": "Hidden Catacombs beneath Kordava & Abandoned Rabirian Shrines",
            "agenda": "Eradicate all industrial necromancy, overthrow secular rule, purify the kingdom with holy fire, and restore divine theocratic governance.",
            "vulnerabilities": "Deep public distrust stemming from the historical child crucifixion scandal in Period VI; outlawed status makes them hunted pariahs.",
            "tags": ["Faction", "Religious", "Theocracy", "Zealots"],
            "aliases": ["Church of Nemeth", "Nemeth the Gnostic", "Gnostic Church", "Nemeth Cult"],
            "summary": "Outlawed holy zealots who view necromancy as an abomination. They seek to recover the Fountain of Youth and cleanse the realm in holy fire."
        },
        {
            "id": "grandees",
            "name": "Grandee Coalitions",
            "subtitle": "Hereditary High Nobility (Eastern & Western Leagues)",
            "leadership": "High Duke Gonzalgo de Guarralid & Provincial Lords",
            "headquarters": "Autonomous Mountain Fiefdoms, Fortified Castles, & Manorial Estates",
            "agenda": "Maintain near-total provincial autonomy, hoard private mine wealth, evade royal tariffs, and expand private mercenary armies.",
            "vulnerabilities": "Internal disunity caused by petty hereditary feuds, commercial rivalries, and hypersensitive pride (pundonor).",
            "tags": ["Faction", "Nobility", "Grandees", "Lords"],
            "aliases": ["Grandee Coalitions", "Grandees", "Eastern League", "Western League", "High Nobility"],
            "summary": "Proud, touchy high nobles who govern private fiefs. They maintain independent armies and challenge royal authority with duels and tax boycotts."
        },
        {
            "id": "barachan-pirates",
            "name": "Barachan Pirates & Corsairs",
            "subtitle": "Ruthless Maritime Raiders & Freebooters",
            "leadership": "Independent Corsair Captains & Smuggler Barons",
            "headquarters": "Barachan Isles (Shark Island, Darksome Island) & Coastal Coves",
            "agenda": "Plunder merchant shipping in the Baracha Strait, extort coastal settlements, smuggle contraband into The Pit, and sell mercenary naval services.",
            "vulnerabilities": "Complete lack of central discipline; easily bought off or swayed by greed, plunder, or internal mutiny.",
            "tags": ["Faction", "Pirates", "Baracha", "Corsairs", "Naval"],
            "aliases": ["Barachan Pirates", "Barachan Corsairs", "Corsairs", "Freebooters"],
            "summary": "Freebooters infesting the southwestern archipelago. They raid merchant galleys, battle Argossean ships, and smuggle relics into Kordava's underworld."
        },
        {
            "id": "foreign-powers",
            "name": "Foreign Powers & Regional Neighbors",
            "subtitle": "Kingdom of Argos, Poitain (Aquilonia), & Pictish Clans",
            "leadership": "Ambassador Tiberio (Argos), Count of Poitain, Pictish Chiefs",
            "headquarters": "Messantia (Argos), Poitain Frontier, Northern Wilds",
            "agenda": "Argos seeks commercial subjugation and naval control; Poitain guards against raiders; Pictish tribes launch bloodthirsty raids across the northern border.",
            "vulnerabilities": "Argos is vulnerable to pirate disruption; Poitain is preoccupied with Aquilonian civil affairs; Picts are divided into warring clans.",
            "tags": ["Faction", "Foreign", "Argos", "Picts", "Poitain"],
            "aliases": ["Foreign Powers", "Kingdom of Argos", "Argos", "Messantia", "Picts", "Poitain"],
            "summary": "The predatory neighbors encircling Zingara, ready to carve up the bankrupt realm the moment the Triumvirate falters."
        }
    ]

    for f in factions_data:
        articles.append({
            "id": f["id"],
            "category": "factions",
            "title": f["name"],
            "subtitle": f["subtitle"],
            "tags": f["tags"],
            "aliases": f["aliases"],
            "summary": f["summary"],
            "content": f"""
<div class="info-card">
  <p><strong>Leadership:</strong> {f['leadership']}</p>
  <p><strong>Primary Base:</strong> {f['headquarters']}</p>
</div>

<h3>Strategic Agenda</h3>
<p>{f['agenda']}</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>
  <p><strong>Operational Vulnerabilities:</strong> {f['vulnerabilities']}</p>
  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>
</div>
""",
            "gmSecrets": f["vulnerabilities"],
            "relatedIds": ["court-matrix", "valenza", "sadoria", "lucia", "malachai", "gonzalo-guarralid", "vesper", "tiberio"]
        })

    # ==========================================
    # 6. REGIONAL GAZETTEER
    # ==========================================
    gazetteer_data = [
        {
            "id": "kordava",
            "name": "Kordava",
            "subtitle": "Coastal Port, Royal Capital, & Seat of the Crystal Floor Court",
            "type": "Capital City / Coastal Fortress",
            "strategic": "Seat of the royal court, foreign diplomacy, naval shipyards, and merchant harbor.",
            "hazards": "Court conspiracies, royal army patrols, dueling hotheads in plazas, hidden assassins.",
            "tags": ["Gazetteer", "Capital", "Court", "Coast"],
            "aliases": ["Kordava", "The Capital", "Royal Citadel", "Crystal Floor Court"],
            "summary": "The political and economic heart of Zingara at the mouth of the Black River. Famous for whitewashed arcades, fencing academies, and the Crystal Floor Court.",
            "desc": "Situated dramatically at the mouth of the Black River where its dark waters spill into the Western Ocean, modern Kordava is the political and economic center of Zingara. Renowned for its royal court with its famous floor of polished crystal, the surface city features prestigious fencing academies (esgrimas), grand whitewashed arcades, and massive sea-facing bastions. However, this chivalric splendor sits directly atop a hollow, ruined foundation—the subterranean labyrinth of The Pit."
        },
        {
            "id": "the-pit",
            "name": "The Pit",
            "subtitle": "Subterranean Sunken Ruins beneath Kordava",
            "type": "Subterranean Labyrinth / Criminal Haven",
            "strategic": "Black markets, criminal syndicates, pre-Cataclysmic relic caches, underground insurgent hideouts.",
            "hazards": "Rogue zombie thralls, toxic cave-ins, criminal ambushes, eldritch radiation, ancient stone guardians.",
            "tags": ["Gazetteer", "Subterranean", "The Pit", "Ruins", "Underworld"],
            "aliases": ["The Pit", "Subterranean Depths", "Sunken Ruins", "Old Kordava"],
            "summary": "Sunless subterranean labyrinth formed when Old Kordava was swallowed by earthquake and starfall. Ruled by smugglers, outlaws, and republican rebels.",
            "desc": "Sprawling beneath the streets of modern Kordava lies The Pit—a sunless, lawless subterranean labyrinth formed when old Kordava was swallowed by earthquake and starfall. Excavated over generations by outlaws, deserters, and runaway thralls, it is ruled by criminal syndicates, renegade duelists, and republican insurgent cells. Deep beneath the rubble lie two legendary relics: the Black Blade of Azur and the Obsidian Blade."
        },
        {
            "id": "mausoleum-kalenius",
            "name": "Submerged Mausoleum of King Kalenius",
            "subtitle": "Abyssal Pre-Cataclysmic Crypt & The Final Guard",
            "type": "Underwater Ancient Tomb",
            "strategic": "Holds pre-Cataclysmic Thurian weaponry, ancient armor, and the dormant Final Guard.",
            "hazards": "Flooded vertical shafts, aquatic ghoul constructs, 1,000 animate stone guardians.",
            "tags": ["Gazetteer", "Tomb", "Ancient", "Relic", "The Pit"],
            "aliases": ["Mausoleum of King Kalenius", "Tomb of Kalenius", "King Kalenius Crypt", "The Final Guard"],
            "summary": "Deepest abyssal reach beneath Kordava's harbor. Contains the ancient tomb of Thurian King Kalenius, guarded by 1,000 elite warriors turned to animate stone.",
            "desc": "Located in the deepest abyssal reaches of The Pit beneath Kordava's harbor lies the ancient pre-Cataclysmic tomb of King Kalenius—a legendary monarch of the ancient Thurian Age. Kalenius's mausoleum is permanently guarded by the Final Guard—one thousand elite ancient Thurian warriors transformed into deathless, animate stone."
        },
        {
            "id": "zingg-valley",
            "name": "Zingg Valley",
            "subtitle": "Fertile River Basin & Agricultural Heartland",
            "type": "Agricultural River Basin",
            "strategic": "Breadbasket of the kingdom; extensive vineyards, olive groves, and ancestral manors.",
            "hazards": "Republican guerrilla raiding, hidden Gnostic shrines, noble border skirmishes.",
            "tags": ["Gazetteer", "Heartland", "Valley", "Agriculture"],
            "aliases": ["Zingg Valley", "Zingg", "Valley of Zingg"],
            "summary": "Fertile agricultural spine of Zingara. Dotted with fortified manorial estates, sprawling vineyards, olive groves, and ancient buried relics.",
            "desc": "Bounded by rolling pastoral hills and fed by river tributaries, the Zingg Valley is the food-producing heartland of the nation. Sprawling vineyards, ancient olive groves, and fortified manorial estates dominate the landscape. Historically settled by Shemitish agriculturalists before Pictish and Hyborian conquests, it remains a battleground for local noble feuds and hidden Church shrines."
        },
        {
            "id": "jerida",
            "name": "Jerida",
            "subtitle": "Fortified Inland River Port on the Lower Thunder River",
            "type": "River Port / Trade Bastion",
            "strategic": "Controls trade of northern timber floated downriver and iron ore hauled from mountain mines.",
            "hazards": "River pirates, corrupt customs inspectors, mercenary blockades, thrall labor riots.",
            "tags": ["Gazetteer", "Port", "Trade", "Thunder River"],
            "aliases": ["Jerida", "Port Jerida"],
            "summary": "Heavily fortified river port acting as the critical trade gateway between the interior and the coast, controlling timber and iron distribution.",
            "desc": "A heavily fortified river port acting as the critical trade gateway between the interior and the coast. Jerida controls the distribution of northern timber floated down river and iron ore hauled out of interior mountain mines. It is garrisoned by paranoid river customs officials and mercenary companies."
        },
        {
            "id": "guarralid",
            "name": "Guarralid Highlands",
            "subtitle": "Autonomous Mountain Duchy & Mining Fiefdom",
            "type": "Mountain Highlands / Autonomous Duchy",
            "strategic": "Vast mineral wealth (iron, silver), defensive highland passes, private standing army.",
            "hazards": "Grandee private armies, hereditary feud ambushes, treacherous mountain terrain.",
            "tags": ["Gazetteer", "Mountains", "Highlands", "Mines"],
            "aliases": ["Guarralid", "Duchy of Guarralid", "Guarralid Highlands"],
            "summary": "Fiercely independent highland duchy governed by proud Grandees. Controls mountain iron mines and maintains an independent private army.",
            "desc": "A powerful, fiercely independent interior duchy located in the highlands. Governed by proud Grandees who hoard private mineral wealth, Guarralid maintains an independent standing army and is plagued by bloody, hereditary border feuds with neighboring provinces."
        },
        {
            "id": "sadoria-kova",
            "name": "Sadoria & Kova",
            "subtitle": "Central Agricultural Plains & Warhorse Hubs",
            "type": "Rolling Agricultural Plains",
            "strategic": "Breeding of high-mettled Hyborian warhorses, citrus production, grain estates.",
            "hazards": "Thrall labor revolts, noble press-gangs, highwaymen, alchemical pit runoff.",
            "tags": ["Gazetteer", "Plains", "Agriculture", "Horses"],
            "aliases": ["Sadoria", "Kova", "Sadoria & Kova", "Central Provinces"],
            "summary": "Prime agricultural hubs in central/western Zingara, famous across the Hyborian world for breeding warhorses and operating massive manorial estates.",
            "desc": "Prime agricultural hubs dominating central and western Zingara. Renowned across the Hyborian world for breeding high-mettled warhorses, cultivating extensive citrus groves, and operating vast manorial estates worked by bonded peasants and industrial thrall labor."
        },
        {
            "id": "baracha-strait",
            "name": "Baracha Strait & Isles",
            "subtitle": "Reef-Choked Pirate Archipelago",
            "type": "Maritime Island Chain / Coral Reefs",
            "strategic": "Dominates coastal trade lanes to Argos; pirate havens (Shark Island, Darksome Island).",
            "hazards": "Barachan corsairs, naval privateer skirmishes, sudden oceanic squalls, razor reefs.",
            "tags": ["Gazetteer", "Maritime", "Islands", "Pirates"],
            "aliases": ["Baracha Strait", "Barachan Isles", "Shark Island", "Darksome Island"],
            "summary": "Treacherous, reef-choked waters off the southwestern coast. Haunt of ruthless Barachan corsairs, privateers, and smugglers.",
            "desc": "The treacherous, reef-choked maritime corridor off the southwestern coast. The strait separates the mainland from the pirate-infested Barachan Isles—including infamous havens like Shark Island and Darksome Island. These waters host relentless skirmishes between Zingaran merchantmen, royal privateers, and ruthless corsairs."
        },
        {
            "id": "forest-of-ghouls",
            "name": "Forest of Ghouls & City of the Ghouls",
            "subtitle": "Primeval Gloom-Draped Cursed Wilderness",
            "type": "Cursed Wilderness / Ancient Ruins",
            "strategic": "Pre-Cataclysmic ruin salvage, rare alchemical reagents, ancient forbidden texts.",
            "hazards": "Feral ghouls, wandering necromantic constructs, lost cultists, toxic miasma.",
            "tags": ["Gazetteer", "Wilderness", "Horror", "Ruins"],
            "aliases": ["Forest of Ghouls", "City of the Ghouls"],
            "summary": "Gloom-draped wilderness in southeastern Zingara. Hides the ancient City of the Ghouls, where feral undead and forgotten cults wander marble ruins.",
            "desc": "A primeval, gloom-draped wilderness in southeastern Zingara near the Rabirian border. Avoided by commoners and knights alike, this superstitious forest conceals the ancient, cursed City of the Ghouls, where feral necromantic constructs, rogue ghouls, and forgotten cults wander through overgrown marble ruins."
        },
        {
            "id": "pictish-wilderness",
            "name": "Pictish Wilderness",
            "subtitle": "Untamed Northern Frontier & Savage Jungle",
            "type": "Frontier Wilderness / Jungle",
            "strategic": "Timber reserves, pelts, natural buffer against northern barbarians.",
            "hazards": "Pictish raiding warbands, wild beasts, uncharted treacherous swamps.",
            "tags": ["Gazetteer", "Borderlands", "Picts", "Wilderness"],
            "aliases": ["Pictish Wilderness", "Pictish Frontier", "Northern Border"],
            "summary": "Savage northern frontier beyond Zingara's border. Dense forests give way to hostile barbarian tribes who frequently launch bloodthirsty raids.",
            "desc": "The savage, untamed northern frontier lying beyond Zingara's northern border. Dense, dark forests give way to hostile barbarian tribes who frequently launch bloodthirsty raiding parties against border settlements."
        },
        {
            "id": "poitain-alimane",
            "name": "Poitain Mountains & River Alimane",
            "subtitle": "Northeastern Alpine Frontier with Aquilonia",
            "type": "Alpine Mountain Border / Frontier River",
            "strategic": "Natural barrier protecting against northern invasion; alpine trade routes.",
            "hazards": "Mountain avalanches, Aquilonian border patrols, smuggler ambushes.",
            "tags": ["Gazetteer", "Mountains", "Borderlands", "Poitain"],
            "aliases": ["Poitain Mountains", "River Alimane", "Alimane"],
            "summary": "Rugged northeastern mountain range and border river separating Zingara from Poitain, the prosperous southern province of Aquilonia.",
            "desc": "Marking the northeastern frontier, this rugged mountain range and its cascading border river, the Alimane, separate Zingara from Poitain, the prosperous southern province of Aquilonia."
        },
        {
            "id": "rabirian-mountains",
            "name": "Rabirian Mountains",
            "subtitle": "Southeastern Barrier Range & Caches of the Fountain",
            "type": "Jagged Barrier Mountain Range",
            "strategic": "Border defense against Argos; conceals abandoned Gnostic shrines and the Fountain of Youth.",
            "hazards": "Mountain bandits, Gnostic religious fanatics, sheer cliff passes.",
            "tags": ["Gazetteer", "Mountains", "Borderlands", "Fountain of Youth"],
            "aliases": ["Rabirian Mountains", "Rabirian Range"],
            "summary": "Jagged southeastern range forming the border with Argos. Its high passes conceal abandoned theocratic shrines and the legendary Fountain of Youth.",
            "desc": "A jagged, barrier-like southeastern range forming the natural border between Zingara and the Kingdom of Argos. Its high passes are haunted by mountain bandits and conceal abandoned theocratic shrines. Sealed deep within one of these mountain shrines lies the legendary Fountain of Youth."
        },
        {
            "id": "kingdom-of-argos",
            "name": "Kingdom of Argos & Port Messantia",
            "subtitle": "Ancient Maritime Rival & Wealthy Merchant Empire",
            "type": "Foreign Maritime Empire",
            "strategic": "Vast naval commerce, banking conglomerates, maritime trade concessions.",
            "hazards": "Argossean naval squadrons, foreign spies, predatory merchant lenders.",
            "tags": ["Gazetteer", "Foreign", "Argos", "Messantia"],
            "aliases": ["Kingdom of Argos", "Argos", "Messantia"],
            "summary": "Zingara's ancient maritime rival to the southeast. Relations are perpetually tense over naval blockades, privateer skirmishes, and predatory loans.",
            "desc": "Zingara's ancient maritime rival to the southeast. Sharing a bitter history of commercial warfare, privateer skirmishes, and naval blockades, tension between Kordava and Messantia remains at a perpetual boiling point."
        }
    ]

    for g in gazetteer_data:
        articles.append({
            "id": g["id"],
            "category": "gazetteer",
            "title": g["name"],
            "subtitle": g["subtitle"],
            "tags": g["tags"],
            "aliases": g["aliases"],
            "summary": g["summary"],
            "content": f"""
<div class="info-card">
  <p><strong>Geographical Classification:</strong> {g['type']}</p>
  <p><strong>Strategic &amp; Economic Value:</strong> {g['strategic']}</p>
  <p><strong>Primary Encounter Hazards:</strong> {g['hazards']}</p>
</div>

<h3>Geographical Overview</h3>
<p>{g['desc']}</p>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>
  <p><strong>Encounter Complications:</strong> {g['hazards']}</p>
  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>
</div>
""",
            "gmSecrets": g["hazards"],
            "relatedIds": ["kordava", "the-pit", "zingg-valley", "jerida", "guarralid", "baracha-strait"]
        })

    # ==========================================
    # 7. HISTORICAL CHRONOLOGY (PERIODS I - VIII)
    # ==========================================
    history_periods = [
        {
            "id": "period-i",
            "title": "Period I: The Gift",
            "subtitle": "Founding of the Realm & The Buried Blade",
            "defining": "Kingdom founded in Zingg Valley; Black Blade of Azur forged by sorcerer; sorcerer executed; blade buried underground.",
            "figures": "Founding Monarch, Youngest Son, Executed Sorcerer",
            "legacy": "Established core national territory and buried the primary anti-sorcery relic beneath the valley.",
            "desc": "In the earliest era, pastoral agriculturalists settled the fertile Zingg Valley. A sorcerer forged the Black Blade of Azur—a blade of pure anti-magic. Fearing its terrifying power, the founding king executed the sorcerer and buried the blade deep beneath the earth, laying the foundation of the kingdom."
        },
        {
            "id": "period-ii",
            "title": "Period II: Time of the Elves",
            "subtitle": "The Golden Age of Ancillus I & Elven Academies",
            "defining": "Arrival of ocean-faring elven longships; era of cross-cultural peace and enrichment; founding of the elven-run magical academy in Kordava.",
            "figures": "King Ancillus I, Elven Scholars",
            "legacy": "Codified advanced arcane traditions and established elven architectural and academic influence.",
            "desc": "Ocean-faring elven longships arrived along the Zingaran coast. King Ancillus I welcomed the scholars with open arms, forging an alliance that established centuries of golden peace. The elven scholars built a renowned magical academy in Kordava, elevating Zingara to the pinnacle of civilization."
        },
        {
            "id": "period-iii",
            "title": "Period III: The Magical Capital",
            "subtitle": "The Desecration, The Earthquake, & The First Undead",
            "defining": "First zombie created; tomb of Ancillus I desecrated; earthquake subsumes academy; Black Blade lost; necromancy commercialized.",
            "figures": "Printius, Lord Silkeneth, King Ancillus I (deceased)",
            "legacy": "Created the subterranean sunken ruins beneath Kordava and introduced profit-driven necromancy.",
            "desc": "Hubris overtook the academy. Scholars desecrated the tomb of Ancillus I to experiment with soul-binding, creating the first conscious undead thrall. A catastrophic earthquake shattered the city, swallowing the academy into the abyss. In the chaos, Printius and Lord Silkeneth partnered to turn necromancy into a commercial goldmine."
        },
        {
            "id": "period-iv",
            "title": "Period IV: The Zombie Era",
            "subtitle": "Edmund's Industrial Necromancy & Thrall Mines",
            "defining": "Industrialization of undead labor; construction of vast 'zombie pits' for mining and hazardous labor across the realm.",
            "figures": "Edmund (grandson of Silkeneth)",
            "legacy": "Shifted the kingdom's economy to rely permanently on thrall labor; left reeking necromantic vats across the land.",
            "desc": "Edmund, grandson of Silkeneth, institutionalized mass undead labor on an industrial scale. Massive pits were dug across the kingdom to mine iron and toxic minerals using memory-retaining thralls. The Zingaran economy became permanently addicted to unpaid undead labor, creating deep social rot."
        },
        {
            "id": "period-v",
            "title": "Period V: Mad King Daedalus & The Starfall",
            "subtitle": "The City Sacrifice, Cosmic Ruin, & The Obsidian Blade",
            "defining": "Obsidian Blade unearthed; city sacrifice of Kordava; Starfall meteor strike; Daedalus trapped; cult leader hijacks horde.",
            "figures": "King Daedalus, Fergus, Tanatos (Death), Cult Leader",
            "legacy": "Shattered old Kordava into rubble; created memory-retaining zombie hordes; birthed Church of Nemeth via cult leader's martyrdom.",
            "desc": "Mad King Daedalus unearthed the Obsidian Blade, sacrificing his own capital to fuel an eldritch ritual for godhood alongside his cosmic lover, Tanatos. Mid-ritual, a cosmic Starfall meteor pulverized Old Kordava. Tanatos imprisoned Daedalus alive beneath the rubble for boring her, while a martyred cult leader hijacked the undead horde."
        },
        {
            "id": "period-vi",
            "title": "Period VI: Religious Rulership & Fall",
            "subtitle": "The Gnostic Holy Crusade, The Fountain, & Child Crucifixion",
            "defining": "Holy crusade against zombies; Fountain of Youth found; child crucifixion scandal; monarchist-republican coup; covert murder.",
            "figures": "Fergus, Falmouth, Nemeth the Gnostic, Head of Army (Don Rodorigo)",
            "legacy": "Left hidden theocratic cults; created deep monarchist-republican rift; lost the Fountain of Youth.",
            "desc": "Fergus led a holy crusade in the name of Nemeth the Gnostic, driving back the zombies and establishing a theocracy. Priest Falmouth discovered the Fountain of Youth. But the church collapsed after a horrific child crucifixion scandal. Monarchists and republicans united to overthrow the priests, only for General Valenza to covertly murder the republican leader."
        },
        {
            "id": "period-vii",
            "title": "Period VII: Restoration Civil War",
            "subtitle": "The Return of Undead King Ancillus & The Puppetmaster Coup",
            "defining": "Discovery of Ancillus's lineage; republican revolt; return of undead King Ancillus I; mortal alliance and monarchist betrayal.",
            "figures": "Undead King Ancillus I, Restoration Council, General Valenza, Marquis Murzio",
            "legacy": "Decimated population; crippled republican leadership through assassination; cemented monarchist control.",
            "desc": "A catastrophic civil war erupted. Necromancers resurrected King Ancillus I as an undead warlord leading a zombie legion to reclaim his throne. Monarchists and republicans forged a temporary truce to destroy the undead king. Once victorious, the Restoration Council seized power and purged the weakened republicans."
        },
        {
            "id": "period-viii",
            "title": "Period VIII: The Besieged Kingdom",
            "subtitle": "Current Campaign Era: The Triumvirate's Ascendancy Trap",
            "defining": "Installation of PC Triumvirate by puppetmasters; growth of 'The Pit'; multi-front insurgent and foreign threats.",
            "figures": "The Triumvirate (Player Characters), General Valenza, Marquis Murzio, Faction Leaders",
            "legacy": "Modern campaign era: an unstable, bankrupt state ruled by inexperienced monarchs surrounded by enemies.",
            "desc": "The current campaign epoch. The Player Characters are installed as the Triumvirate on the crystal throne of Kordava. Surrounding them are greedy handlers, rebellious grandees, underground zealots, and lurking relics in the depths."
        }
    ]

    for hp in history_periods:
        articles.append({
            "id": hp["id"],
            "category": "history",
            "title": hp["title"],
            "subtitle": hp["subtitle"],
            "tags": ["History", "Chronology", "Lore"],
            "aliases": [hp["title"], hp["id"].replace("-", " ")],
            "summary": hp["summary"] if "summary" in hp else hp["defining"],
            "content": f"""
<div class="info-card">
  <p><strong>Defining Events:</strong> {hp['defining']}</p>
  <p><strong>Key Historical Figures:</strong> {hp['figures']}</p>
  <p><strong>Lasting Legacy:</strong> {hp['legacy']}</p>
</div>

<h3>Historical Narrative</h3>
<p>{hp['desc']}</p>
""",
            "gmSecrets": f"Events from {hp['title']} directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
            "relatedIds": ["history-matrix", "ancillus-i", "daedalus", "valenza", "sadoria"]
        })

    # Historical Master Matrix Article
    articles.append({
        "id": "history-matrix",
        "category": "history",
        "title": "Historical Chronology Master Matrix",
        "subtitle": "Eight-Period Timeline of Zingaran Cataclysm and Rebirth",
        "tags": ["History", "Timeline", "Matrix", "Quick Reference"],
        "aliases": ["Historical Matrix", "Timeline", "Eight Periods", "Chronology Matrix"],
        "summary": "Master reference matrix outlining all eight historical epochs from the founding gift to the modern Besieged Kingdom.",
        "content": """
<h3>Historical Chronology Master Matrix</h3>
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
      <td>The Triumvirate (PCs), <a href="#npcs/valenza" class="wiki-link">Valenza</a>, <a href="#npcs/sadoria" class="wiki-link">Murzio</a></td>
      <td>Modern campaign setting: bankrupt, besieged realm ruled by young rulers surrounded by wolves.</td>
    </tr>
  </tbody>
</table>
</div>
""",
        "gmSecrets": "Notice how every period ended in betrayal or cataclysm—the cycle the Triumvirate must break.",
        "relatedIds": ["period-i", "period-viii", "campaign-premise"]
    })

    # ==========================================
    # 8. RULES, SYSTEMS & CULTURE
    # ==========================================
    articles.append({
        "id": "pundonor",
        "category": "rules",
        "title": "Dueling Culture & Pundonor Rules",
        "subtitle": "Aristocratic Honor System, Duels, Penalties, & Swashbuckling Flair",
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
        "gmSecrets": "Use Duke Gonzalgo de Guarralid as the primary NPC to test players with honor-baiting early in the campaign.",
        "relatedIds": ["gonzalo-guarralid", "command-friction", "social-hierarchy"]
    })

    articles.append({
        "id": "command-friction",
        "category": "rules",
        "title": "Military Doctrines & Command Friction",
        "subtitle": "Tactical Arms, Aristocratic Insubordination, & Royal Edicts",
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
        "gmSecrets": "When players lead army units, use command friction to make large-scale battles tense and character-driven.",
        "relatedIds": ["pundonor", "military-elite", "guarralid"]
    })

    articles.append({
        "id": "social-hierarchy",
        "category": "rules",
        "title": "Ethnic Genesis & Social Hierarchy",
        "subtitle": "The Four Strata: Grandees, Caballeros, Chulos, and Thralls",
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
        "gmSecrets": "The tension between Caballeros (who aspire to be Grandees) and Commoners (who lean republican) is ripe for player recruitment.",
        "relatedIds": ["pundonor", "necromancy-mechanics", "campaign-premise"]
    })

    # ==========================================
    # 9. ARCANA, RELICS & UNDEAD
    # ==========================================
    articles.append({
        "id": "necromancy-mechanics",
        "category": "relics",
        "title": "Memory-Retaining Undead Mechanics",
        "subtitle": "The Horrific Psychology and Exploitation of Zingaran Thralls",
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
        "gmSecrets": "Have an NPC the players cared about in their backstory appear as a reanimated thrall in Master Vane's laboratory.",
        "relatedIds": ["industrial-pits", "vane", "edmund", "obsidian-blade"]
    })

    articles.append({
        "id": "industrial-pits",
        "category": "relics",
        "title": "Industrial Zombie Pits & Blueprint Layout",
        "subtitle": "Mass Thrall Labor Infrastructure, Toxic Vats, & Hazard Rules",
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
        "gmSecrets": "The pit near Jerida contains an unmapped secret tunnel connecting directly to the crypt of the Black Blade of Azur.",
        "relatedIds": ["necromancy-mechanics", "vane", "edmund", "black-blade"]
    })

    articles.append({
        "id": "black-blade",
        "category": "relics",
        "title": "The Black Blade of Azur",
        "subtitle": "Pre-Deluvial Anti-Sorcery Relic",
        "origin": "Forged in Period I by an ancient sorcerer in the Zingg Valley; buried underground after the sorcerer's execution.",
        "powers": "Pure negation of all arcane and necromantic energies; severs magical bindings on contact; instantly unbinds undead thralls.",
        "status": "Lost in the subterranean abyss beneath the ruins of the old magical academy, far below The Pit in Kordava.",
        "tags": ["Relic", "Artifact", "Anti-Magic", "Weapon"],
        "aliases": ["Black Blade of Azur", "Black Blade", "Blade of Azur"],
        "summary": "Legendary anti-sorcery weapon forged in Period I. Capable of instantly severing necromantic control and nullifying magical wards.",
        "content": """
<h3>The Black Blade of Azur</h3>
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
        "gmSecrets": "Master Alchemist Vane is desperately trying to locate this blade to destroy it before it can be used against his thralls.",
        "relatedIds": ["obsidian-blade", "the-pit", "vane", "period-i"]
    })

    articles.append({
        "id": "obsidian-blade",
        "category": "relics",
        "title": "The Obsidian Blade",
        "subtitle": "Eldritch Mass-Binding Conduit of Mad King Daedalus",
        "origin": "Uncovered by Mad King Daedalus in Period V to channel the blood of foreign envoys into his ritual cauldron.",
        "powers": "Massive necromantic conduit; allows the wielder to instantly bind, command, or exhume vast armies of undead thralls.",
        "status": "Buried deep within the smoldering rubble of old Kordava beneath The Pit, where Daedalus lies eternally trapped.",
        "tags": ["Relic", "Artifact", "Necromancy", "Weapon", "Horror"],
        "aliases": ["The Obsidian Blade", "Obsidian Blade"],
        "summary": "Terrifying necromantic conduit uncovered by Mad King Daedalus. Grants supreme command over undead hordes, buried with Daedalus beneath The Pit.",
        "content": """
<h3>The Obsidian Blade</h3>
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
        "gmSecrets": "If the blade is removed from Daedalus's grasp, it will break Tanatos's imprisonment spell, awakening the Mad King.",
        "relatedIds": ["daedalus", "black-blade", "the-pit", "tanatos"]
    })

    articles.append({
        "id": "fountain-of-youth",
        "category": "relics",
        "title": "The Fountain of Youth",
        "subtitle": "Sacred Waters of Miraculous Longevity & Purification",
        "origin": "Discovered by Priest Falmouth in Period VI during the early Church of Nemeth era.",
        "powers": "Grants physical longevity, cures any mortal disease or poison, and completely reverses necromantic corruption.",
        "status": "Hidden within an abandoned, sealed mountain shrine in the Rabirian borderlands following the church's downfall.",
        "tags": ["Relic", "Healing", "Church of Nemeth", "Rabirian"],
        "aliases": ["The Fountain of Youth", "Fountain of Youth", "Waters of the Shrine"],
        "summary": "Miraculous sacred spring discovered in Period VI in the Rabirian Mountains. Cures all poisons, reverses decay, and grants centuries of life.",
        "content": """
<h3>The Fountain of Youth</h3>
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
        "gmSecrets": "Marquis Murzio used a slow wasting poison on a PC relative specifically to force the PCs to seek out this fountain.",
        "relatedIds": ["malachai", "falmouth", "rabirian-mountains", "church-of-nemeth"]
    })

    articles.append({
        "id": "final-guard",
        "category": "relics",
        "title": "The Final Guard of King Kalenius",
        "subtitle": "One Thousand Pre-Cataclysmic Thurian Stone Warriors",
        "origin": "Ancient Thurian epoch; interred with King Kalenius beneath Kordava's harbor.",
        "powers": "Deathless animate stone guardians immune to pain, poison, mental influence, and normal weapon damage.",
        "status": "Asleep in the submerged mausoleum beneath The Pit, awaiting the true heir or the proper ritual invocation.",
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
        "gmSecrets": "Vesper knows the entrance to this tomb and will trade it for a royal pardon for his entire criminal syndicate.",
        "relatedIds": ["mausoleum-kalenius", "vesper", "the-pit"]
    })

    # ==========================================
    # 10. PLOT HOOKS & SANDBOX QUESTS
    # ==========================================
    hooks_data = [
        {
            "id": "hook-blood-in-cauldron",
            "name": "Blood in the Cauldron",
            "category": "hooks",
            "factions": ["The Triumvirate", "Restoration Council", "Kingdom of Argos", "The Pit Underworld"],
            "premise": "Argos threatens naval blockade unless the signet ring of an ambassador murdered in Period V is returned from an earthquake-exposed crypt beneath Kordava. The Council forbids intervention, hoping to humiliate the crown.",
            "conflict": "In the crypt, the PCs discover the ambassador is now a conscious, memory-retaining thrall guarding the Obsidian Blade. The rulers must choose whether to destroy him and return the ring, free him via ritual, or claim the blade.",
            "checks": "DC 15 History/Arcana (identify unbinding runes); DC 17 Persuasion (appeal to living memories to secure ring peacefully).",
            "escalation": "If PCs take more than 3 rounds, a Council strike team enters to seize relics and eliminate witnesses.",
            "reward": "Prevents naval blockade of Kordava; secures diplomatic reprieve with Argos; potential access to the Obsidian Blade.",
            "tags": ["Hook", "Diplomacy", "Argos", "The Pit", "Obsidian Blade"]
        },
        {
            "id": "hook-insurgents-bargain",
            "name": "The Insurgent's Bargain",
            "category": "hooks",
            "factions": ["The Triumvirate", "Republican Insurgents", "Restoration Council", "Church of Nemeth"],
            "premise": "Republican insurgents contact the PCs during a royal gala with written proof that General Valenza and Marquis Murzio assassinated the republican founder in Period VI and framed the Church.",
            "conflict": "Republicans want pardons; Church zealots intercept demanding the evidence to clear their name; Council assassins lurk. Who do the PCs align with or betray?",
            "checks": "DC 16 Stealth/Deception (slip away from royal handlers at gala); DC 14 Insight (detect double-dealing zealots).",
            "escalation": "Hesitation causes royal army assassins to strike, attempting to burn documents and silence all informants.",
            "reward": "Absolute blackmail evidence against General Valenza and Marquis Murzio, enabling a crown purge of the puppetmasters.",
            "tags": ["Hook", "Intrigue", "Puppetmasters", "Republicans", "Blackmail"]
        },
        {
            "id": "hook-pits-of-edmund",
            "name": "The Reeking Pits of Edmund",
            "category": "hooks",
            "factions": ["The Triumvirate", "Restoration Council", "Grandee Coalitions", "Master Alchemist Vane"],
            "premise": "Pit #4 near Jerida collapses, releasing hundreds of memory-retaining thralls who seize a vital iron mine. The Council cuts royal household stipends in retaliation.",
            "conflict": "Inside the mine, a reanimated Period IV scholar offers a secret passage into the crypt of the Black Blade of Azur if the PCs help the thralls escape to the Pictish Wilderness.",
            "checks": "DC 14 Athletics/Survival (navigate toxic pit slurry); DC 16 Warfare/Tactics (organize stealth escape route through Grandee lines).",
            "escalation": "Toxic alchemical fumes force DC 13 Fortitude Save every 10 min; failure deals cumulative -1 penalties.",
            "reward": "Restores royal iron production and yields a secret map to the Black Blade of Azur crypt.",
            "tags": ["Hook", "Necromancy", "Jerida", "Zombie Pits", "Black Blade"]
        },
        {
            "id": "hook-fallen-shrine",
            "name": "Waters of the Fallen Shrine",
            "category": "hooks",
            "factions": ["The Triumvirate", "Restoration Council", "Church of Nemeth", "Kingdom of Argos"],
            "premise": "A loyal royal relative is struck by a slow wasting poison secretly administered by Marquis Murzio. To find the cure, the PCs must locate the lost Fountain of Youth in the Rabirian Mountains.",
            "conflict": "At the shrine, Gnostic zealots guard the waters while Argossean mercenaries assault the gates. PCs must negotiate, fight, or steal the waters.",
            "checks": "DC 15 Perception (spot Argossean mountain scouts); DC 17 Religion (quote scripture to secure Gnostic sanctuary).",
            "escalation": "On round 4 of combat inside the shrine, the cavern ceiling collapses, destroying the primary pool forever.",
            "reward": "Waters of the Fountain of Youth, providing an absolute cure for poisons and necromantic decay.",
            "tags": ["Hook", "Rabirian", "Fountain of Youth", "Church of Nemeth", "Healing"]
        },
        {
            "id": "hook-concealed-order",
            "name": "The Concealed Execution Order",
            "category": "hooks",
            "factions": ["Military Elite", "Republican Insurgents", "The Triumvirate"],
            "premise": "General Valenza asks the PCs to rubber-stamp an execution order against a 'rebel camp' in the Zingg Valley—actually surviving witnesses to his Period VI assassination.",
            "conflict": "Sign the order to keep Valenza's favor, or delay and investigate to save witnesses and gain republican allies.",
            "checks": "DC 15 Investigation/Insight (uncover identity of target camp); DC 16 Command/Persuasion (countermand military orders).",
            "escalation": "Delaying more than 24 hours causes Valenza to execute the order with his private guard and place the PCs on lockdown.",
            "reward": "Saves key witnesses to Period VI state crimes, earning the secret allegiance of urban republican cells.",
            "tags": ["Hook", "Valenza", "Military", "Zingg Valley", "Investigation"]
        },
        {
            "id": "hook-treasury-lockout",
            "name": "The Treasury Lockout",
            "category": "hooks",
            "factions": ["Restoration Council", "The Triumvirate", "Marquis Murzio"],
            "premise": "Marquis Murzio refuses to fund the PCs' personal guard, claiming the treasury is dry due to foreign debts.",
            "conflict": "Audit Murzio's ledgers to prove embezzlement, raid an underworld den in The Pit, or borrow from foreign merchants.",
            "checks": "DC 16 Investigation (audit treasury scrolls to detect missing gold); DC 17 Persuasion/Intimidation (confront Murzio).",
            "escalation": "Confronting without unassailable proof causes Murzio to slash palace servant and food budgets.",
            "reward": "Exposes Council embezzlement and forces release of crown funds for an independent royal guard.",
            "tags": ["Hook", "Sadoria", "Treasury", "Intrigue", "Economy"]
        },
        {
            "id": "hook-tax-revolt-jerida",
            "name": "The Tax Revolt of Jerida",
            "category": "hooks",
            "factions": ["Grandee Coalitions", "Restoration Council", "Barachan Pirates"],
            "premise": "Duke Gonzalgo's garrison in Jerida seizes royal barges on the Thunder River, declaring an embargo until tariffs are cut.",
            "conflict": "Break the standoff through military intimidation, clever trade compromise, or covert sabotage of supply lines.",
            "checks": "DC 15 Intimidation/Persuasion (force river inspectors to yield); DC 14 Navigation/Sailing (outmaneuver river blockade).",
            "escalation": "Failure to resolve within 3 days triggers an armed clash between royal troops and Grandee retainers.",
            "reward": "Re-establishes crown trade tariffs on the Thunder River, generating independent royal revenue.",
            "tags": ["Hook", "Jerida", "Guarralid", "Grandees", "Economy"]
        },
        {
            "id": "hook-tomb-kalenius",
            "name": "The Tomb of King Kalenius",
            "category": "hooks",
            "factions": ["Vesper the Key-Master", "Grandee Coalitions", "The Triumvirate"],
            "premise": "Vesper offers a map through flooded tunnels into the pre-Cataclysmic crypt of King Kalenius beneath Kordava harbor.",
            "conflict": "Navigate flooded abyssal tunnels and aquatic ghouls to claim star-metal weapons and the dormant Final Guard.",
            "checks": "DC 16 Athletics/Endurance (underwater tunnel navigation); DC 17 Warfare/Tactics (survive stone guardian encounter).",
            "escalation": "Disturbing the tomb without proper ritual keys awakens six stone guardians in a violent fury.",
            "reward": "Secures Thurian masterwork armor and weapons; potential activation of the 1,000 stone warriors.",
            "tags": ["Hook", "The Pit", "Dungeon", "Relic", "Final Guard"]
        },
        {
            "id": "hook-treasury-heist",
            "name": "The Treasury Heist",
            "category": "hooks",
            "factions": ["Restoration Council", "Vesper the Key-Master", "The Triumvirate"],
            "premise": "The PCs partner with Vesper to break into the Restoration Council's secret subterranean vaults beneath Kordava.",
            "conflict": "Bypass pre-Cataclysmic mechanical wards, avoid Council patrols, and extract hoarded bullion.",
            "checks": "DC 16 Thievery/Stealth (bypass vault traps); DC 15 Arcana (disarm pre-Cataclysmic mechanical wards).",
            "escalation": "Triggering alarms floods the vault with toxic alchemical mist and locks all egress gates.",
            "reward": "Reclaims millions in hoarded state gold, allowing direct payment of the Kordava city watch for absolute loyalty.",
            "tags": ["Hook", "Heist", "Vesper", "The Pit", "Gold"]
        }
    ]

    for hk in hooks_data:
        articles.append({
            "id": hk["id"],
            "category": "hooks",
            "title": hk["name"],
            "subtitle": f"Sandbox Ruler Hook &bull; Factions: {', '.join(hk['factions'])}",
            "tags": hk["tags"],
            "aliases": [hk["name"]],
            "summary": hk["premise"][:150] + "...",
            "content": f"""
<div class="info-card">
  <p><strong>Involved Factions:</strong> {', '.join(hk['factions'])}</p>
  <p><strong>Strategic Reward:</strong> {hk['reward']}</p>
</div>

<h3>Narrative Premise</h3>
<p>{hk['premise']}</p>

<h3>Core Conflict &amp; Player Choice</h3>
<p>{hk['conflict']}</p>

<div class="dc-box">
  <strong>Suggested Skill Checks:</strong> {hk['checks']}
</div>

<p class="escalation"><strong>Dynamic Escalation Trigger:</strong> {hk['escalation']}</p>
""",
            "gmSecrets": f"Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
            "relatedIds": ["court-matrix", "campaign-premise", "valenza", "sadoria", "lucia", "vesper"]
        })

    # Save to data.js
    data_js = f"""// Our Kingdom Come - Zingara Sandbox GM Compendium Data
// Auto-compiled from canonical source documents

const WIKI_DATA = {{
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

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = WIKI_DATA;
}}
"""

    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(data_js)
    print(f"Generated js/data.js with {len(articles)} articles!")

if __name__ == '__main__':
    main()
