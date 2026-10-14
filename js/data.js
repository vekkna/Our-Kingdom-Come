// Our Kingdom Come - Zingara Sandbox GM Compendium Data
// Auto-compiled from canonical source documents

const WIKI_DATA = {
  meta: {
    title: "Our Kingdom Come",
    subtitle: "Zingara Sandbox Campaign & GM Intrigue Compendium",
    epoch: "Period VIII: The Besieged Kingdom",
    totalArticles: 67
  },
  categories: [
    { id: "overview", name: "Campaign Overview", icon: "👑" },
    { id: "npcs", name: "Royal Court & NPCs", icon: "🎭" },
    { id: "factions", name: "Factions & Power Blocs", icon: "⚔️" },
    { id: "gazetteer", name: "Regional Gazetteer", icon: "🗺️" },
    { id: "history", name: "Chronology & Periods", icon: "📜" },
    { id: "rules", name: "Rules & Mechanics", icon: "⚖️" },
    { id: "relics", name: "Arcana & Relics", icon: "💀" },
    { id: "hooks", name: "Plot Hooks & Sandbox", icon: "🎯" },
    { id: "sessions", name: "Session Log", icon: "📖" }
  ],
  articles: [
  {
    "id": "campaign-premise",
    "category": "overview",
    "title": "Campaign Premise & World Parameters",
    "subtitle": "A Realm Shattered by Decadence, Puppetmasters, and Eldritch Hubris",
    "tags": [
      "Overview",
      "Period VIII",
      "The Triumvirate",
      "Core Themes"
    ],
    "aliases": [
      "Campaign Premise",
      "Premise",
      "World Parameters",
      "Our Kingdom Come"
    ],
    "summary": "Set within ancient pre-deluvial Zingara, the PCs are the newly installed Triumvirate: inexperienced descendants of King Ancillus I installed as puppet rulers over a bankrupt, besieged kingdom rotted by necromancy.",
    "content": "\n<h3>1.1 High-Concept Campaign Premise</h3>\n<p><strong>A Realm Shattered by Decadence and Eldritch Hubris.</strong> Set within the pre-deluvial, sword-and-sorcery epoch of ancient Zingara, <em>Our Kingdom Come</em> paints a dark portrait of a decadent, fallen nation rotting under the cumulative horrors of ancient sorcery, industrial necromantic exploitation, and cosmic ruin. Emerging from a complex ethnic synthesis\u2014where pastoral Zingg Valley agriculturalists merged with conquering Pictish tribes and invading Hyborian warriors\u2014Zingara stands as a land of sharp, irreconcilable contrasts. Flamboyant chivalric pageantry, touchy aristocratic honor, and soaring sea-facing bastions directly overlook rat-infested alleys, reeking industrial zombie pits, and subterranean abysses.</p>\n\n<p><strong>The Ascendancy Trap and Shadowed Puppetmasters.</strong> The primary narrative engine of the campaign centers on an operational crisis of political manipulation, bankruptcy, and decay: the Player Characters are the newly installed rulers\u2014a <strong>Triumvirate</strong> of blood-related descendants of <a href=\"#history/ancillus-i\" class=\"wiki-link\">King Ancillus I</a>\u2014who have inherited a bankrupt, besieged kingdom lingering on the edge of utter collapse. Installed following a bloody civil war by a shadowy cabal of monarchist elites (the <a href=\"#factions/restoration-council\" class=\"wiki-link\">Restoration Council</a> and the head of the royal army, <a href=\"#npcs/valenza\" class=\"wiki-link\">General Don Rodrigo de Valenza</a>), the PCs' ascension is not a victory, but a calculated trap. Their handlers view the untested rulers as weak, inexperienced stand-ins meant to bear public blame for the realm's desperate financial debts and social collapse while the Council rules from behind the throne.</p>\n\n<div class=\"gm-callout\">\n<div class=\"gm-badge\">GM CONFIDENTIAL &bull; ASCENDANCY TRAP</div>\n<p>The PCs were specifically chosen by <a href=\"#npcs/valenza\" class=\"wiki-link\">General Valenza</a> and <a href=\"#npcs/sadoria\" class=\"wiki-link\">Marquis Mateo de Sadoria</a> because their bloodline grants royal legitimacy, but their youth and lack of court experience make them seemingly easy to manipulate. The Treasury is empty; the provincial Grandees refuse to pay taxes; the Church of Nemeth demands a holy purge; and republican insurgents are plotting in The Pit. The handlers expect the Triumvirate to fail and take the blame, allowing the Council to seize direct authoritarian control.</p>\n</div>\n\n<h3>1.2 Canonical Worldbuilding Parameters</h3>\n<ul>\n  <li><strong>Epoch & Tone:</strong> Period VIII (The Besieged Kingdom). Gritty, lethal sword-and-sorcery with deep political intrigue, swashbuckling martial flair, and cosmic horror.</li>\n  <li><strong>Core Tension:</strong> Sovereign Monarchs vs. Shadowy Handlers. Can the young Triumvirate break their puppet strings before the kingdom tears itself apart?</li>\n  <li><strong>Pundonor (Aristocratic Honor):</strong> A rigid, hypersensitive code of conduct where any perceived insult must be answered by rapier duels at dawn.</li>\n  <li><strong>Industrial Necromancy:</strong> Memory-retaining undead used as forced labor in toxic mining pits, creating severe economic reliance and explosive moral crises.</li>\n  <li><strong>Cataclysmic Relics:</strong> Pre-Cataclysmic weapons of godlike power\u2014such as the <a href=\"#relics/black-blade\" class=\"wiki-link\">Black Blade of Azur</a> and the <a href=\"#relics/obsidian-blade\" class=\"wiki-link\">Obsidian Blade</a>\u2014buried beneath the city.</li>\n</ul>\n",
    "gmSecrets": "The handlers deliberately provoked the Treasury crisis to ensure the PCs cannot recruit an independent personal army without uncovering secret wealth or defying the Council.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "triumvirate-guide",
      "restoration-council",
      "period-viii"
    ]
  },
  {
    "id": "triumvirate-guide",
    "category": "overview",
    "title": "The Triumvirate & Sandbox Directives",
    "subtitle": "Game Master Execution Guide for Running Ruler PCs",
    "tags": [
      "Overview",
      "PCs",
      "GM Directives",
      "Mechanics"
    ],
    "aliases": [
      "Triumvirate",
      "The Triumvirate",
      "Sandbox Directives",
      "GM Directives"
    ],
    "summary": "Guidelines for running the campaign with the PCs as co-rulers: tracking Crown Sovereignty, handling Council pressure, managing the Pundonor economy, and balancing sandbox freedom.",
    "content": "\n<h3>1.3 Game Master Execution & Sandbox Directives</h3>\n<p>Running a kingdom-ruling sandbox campaign requires balancing macro-level kingdom decisions with intimate, lethal swashbuckling adventures. The PCs must not sit passively on their thrones\u2014their handlers ensure that resources are blocked unless the PCs venture into the shadows themselves.</p>\n\n<div class=\"info-card\">\n<h4>Three Pillars of Ruler Play</h4>\n<ol>\n  <li><strong>Covert Sovereign Operations:</strong> Because the <a href=\"#factions/restoration-council\" class=\"wiki-link\">Restoration Council</a> and <a href=\"#factions/military-elite\" class=\"wiki-link\">Military Elite</a> monitor official crown movements, the PCs must frequently slip out of the palace in disguise to conduct clandestine meetings, investigate conspirators, and explore the ancient subterranean ruins beneath <a href=\"#gazetteer/kordava\" class=\"wiki-link\">Kordava</a>.</li>\n  <li><strong>The Sovereign Sovereignty Clock:</strong> Track the Triumvirate's political independence. Every victory against their handlers, recovered relic, or independent revenue source grants <em>Crown Sovereignty</em>; every concession or public humiliation tightens the Council's leash.</li>\n  <li><strong>The Lethal Courtroom:</strong> Court is not a safe haven\u2014it is a dueling ground. Grandees will publicly test the PCs' courage using <a href=\"#rules/pundonor\" class=\"wiki-link\">Pundonor</a> honor-baiting. Refusing a duel damages the crown's legitimacy; accepting risks blade-point death.</li>\n</ol>\n</div>\n\n<div class=\"gm-callout\">\n<div class=\"gm-badge\">GM DIRECTIVE &bull; MULTI-FRONT PRESSURES</div>\n<p>At any given moment, the Triumvirate faces four simultaneous pressures:</p>\n<ul>\n  <li><strong>The Financial Stranglehold:</strong> <a href=\"#npcs/sadoria\" class=\"wiki-link\">Marquis Mateo</a> controls the treasury keys and withholds stipends.</li>\n  <li><strong>The Military Leash:</strong> <a href=\"#npcs/valenza\" class=\"wiki-link\">General Valenza</a> controls the city garrisons and gate guards.</li>\n  <li><strong>The Subterranean Threat:</strong> The <a href=\"#factions/republican-insurgents\" class=\"wiki-link\">Republican Insurgents</a> in <a href=\"#gazetteer/the-pit\" class=\"wiki-link\">The Pit</a> possess evidence of Council murder.</li>\n  <li><strong>The Fanatical Purge:</strong> <a href=\"#npcs/malachai\" class=\"wiki-link\">Father Malachai</a> and the <a href=\"#factions/church-of-nemeth\" class=\"wiki-link\">Church of Nemeth</a> demand the complete slaughter of all state necromancers and thralls.</li>\n</ul>\n</div>\n",
    "gmSecrets": "Encourage players to use their dual status: by day, issuing royal edicts and hosting envoys; by night, dueling in the alleys of Kordava or delving into the ruins of The Pit.",
    "relatedIds": [
      "campaign-premise",
      "valenza",
      "sadoria",
      "the-pit",
      "pundonor"
    ]
  },
  {
    "id": "valenza",
    "category": "npcs",
    "title": "General Don Rodrigo de Valenza",
    "subtitle": "Head of the Royal Army & Chief Military Handler",
    "tags": [
      "Puppetmaster",
      "Military Elite",
      "Restoration Council",
      "Caballeros"
    ],
    "aliases": [
      "Don Rodrigo",
      "General Valenza",
      "Rodrigo de Valenza",
      "Head of the Royal Army"
    ],
    "summary": "Head of the Royal Army & Chief Military Handler (Military Elite / Restoration Council). Outwardly presents himself as a stern, unyielding aristocratic protector of Zingara, a grandee of heavy cavalry (caballeros), and the primary defender...",
    "atAGlance": {
      "appearance": "A towering, battle-scarred veteran encased in gilded, mirror-polished steel plate armor, draped in a heavy crimson velvet cloak trimmed with black wolf fur. He keeps one hand permanently rested on the pommel of a broad-bladed Zingaran longsword.",
      "mannerisms": "Unnervingly unblinking gaze; rhythmically taps his armored gauntlet against his sword hilt whenever a young noble or PC speaks.",
      "quote": "Crowns are forged in dragon-fire and welded with blood, my young Lieges. Do not presume your silk robes grant you command over the iron that keeps your throats uncut.",
      "courtDCs": "DC 16 Insight to detect hidden political motives; DC 18 Persuasion to push past his dismissive military deflection.",
      "publicStance": "Outwardly presents himself as a stern, unyielding aristocratic protector of Zingara, a grandee of heavy cavalry (caballe...",
      "secretAgenda": "General Don Rodrigo's primary objective is to maintain absolute, unquestioned control over the Zingaran armed forces while keeping the Triumvirate completely dependent on his garrisons for physical survival. Furthermore, he harbors a deadly secret from Period VI: following the fall of the Church of Nemeth, he co-engineered the secret assassination of the primary republican leader during a victory conference and successfully framed the Church for the murder. If this conspiracy is exposed, it would reunite the republicans and shatter his authority.",
      "rival": "Fencing Master Lucia 'La Mariposa' de la Vega"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">Military Elite / Restoration Council</span>\n    <span class=\"badge rival-badge\">Primary Rival: Fencing Master Lucia 'La Mariposa' de la Vega</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> A towering, battle-scarred veteran encased in gilded, mirror-polished steel plate armor, draped in a heavy crimson velvet cloak trimmed with black wolf fur. He keeps one hand permanently rested on the pommel of a broad-bladed Zingaran longsword.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Unnervingly unblinking gaze; rhythmically taps his armored gauntlet against his sword hilt whenever a young noble or PC speaks.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;Crowns are forged in dragon-fire and welded with blood, my young Lieges. Do not presume your silk robes grant you command over the iron that keeps your throats uncut.&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 16 Insight to detect hidden political motives; DC 18 Persuasion to push past his dismissive military deflection.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>Outwardly presents himself as a stern, unyielding aristocratic protector of Zingara, a grandee of heavy cavalry (caballeros), and the primary defender of the young Triumvirate. He maintains a posture of selfless martial devotion, appearing at court in polished armor to reassure the realm that the crown is safe under his iron guard.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>General Don Rodrigo's primary objective is to maintain absolute, unquestioned control over the Zingaran armed forces while keeping the Triumvirate completely dependent on his garrisons for physical survival. Furthermore, he harbors a deadly secret from Period VI: following the fall of the Church of Nemeth, he co-engineered the secret assassination of the primary republican leader during a victory conference and successfully framed the Church for the murder. If this conspiracy is exposed, it would reunite the republicans and shatter his authority.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>The Concealed Execution Order</h4>\n  <p><strong>Premise:</strong> General Don Rodrigo requests the Triumvirate sign an official royal decree mobilizing troops to purge a 'rebel encampment' in the Zingg Valley. In reality, the camp houses surviving witnesses to the Period VI assassination of the republican founder.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must decide whether to rubber-stamp the order to maintain Don Rodrigo's favor, or delay the decree to dispatch covert agents (or personally travel to the Zingg Valley) to investigate who is actually in the camp.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 15 Investigation/Insight (uncover true identity of target camp); DC 16 Command/Persuasion (countermand military orders).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If the PCs delay signing the decree for more than 24 hours, Don Rodrigo executes the operation using his private household guard, citing 'emergency crown preservation,' and places the PCs' royal quarters under protective lockdown.</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>The Insurgent's Evidence</h4>\n  <p><strong>Premise:</strong> Republican agents in The Pit contact the PCs, claiming to possess written correspondence proving General Don Rodrigo ordered the Period VI political assassination.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must choose whether to buy the evidence using limited royal funds to gain blackmail leverage over their military handler, or alert Don Rodrigo to the cell's location to secure his immediate military loyalty against foreign raiders.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Stealth/Deception (slip past military watchers); DC 15 History (verify authenticity of Period VI seals).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If the PCs attempt to negotiate with the republicans without bringing personal guards, a royal army strike team ambushes the meeting location to destroy the documents and silence all parties.</p>\n</div>\n\n",
    "gmSecrets": "General Don Rodrigo's primary objective is to maintain absolute, unquestioned control over the Zingaran armed forces while keeping the Triumvirate completely dependent on his garrisons for physical survival. Furthermore, he harbors a deadly secret from Period VI: following the fall of the Church of Nemeth, he co-engineered the secret assassination of the primary republican leader during a victory conference and successfully framed the Church for the murder. If this conspiracy is exposed, it would reunite the republicans and shatter his authority.",
    "relatedIds": [
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "vane",
      "tiberio"
    ]
  },
  {
    "id": "sadoria",
    "category": "npcs",
    "title": "High Chancellor Marquis Mateo de Sadoria",
    "subtitle": "Chief Monarchist & Head of the Restoration Council",
    "tags": [
      "Puppetmaster",
      "Restoration Council",
      "Grandee",
      "Bureaucrat"
    ],
    "aliases": [
      "Marquis Mateo",
      "Mateo de Sadoria",
      "High Chancellor",
      "Chief Monarchist"
    ],
    "summary": "Chief Monarchist & Head of the Restoration Council (Restoration Council / Bureaucracy). The devoted elder statesman, administrative guide, and protective mentor of the inexperienced Triumvirate. He projects the aura of an exhausted patrio...",
    "atAGlance": {
      "appearance": "An aristocratic statesman in his late fifties, dressed in an impeccably tailored black velvet doublet embroidered with silver thread, crowned with an ermine-lined mantle. Slender, soft-handed, and wearing three signet rings bearing pre-Cataclysmic heraldry.",
      "mannerisms": "Speaks in smooth, measured cadences; steeples his fingers while listening, offering patronizing smiles that never reach his cold, calculating grey eyes.",
      "quote": "A kingdom is not ruled by steel, Your Majesties, but by ledgers, grain tallies, and patience. Leave the vulgarity of statecraft to those who bled to place that crown upon your brow.",
      "courtDCs": "DC 17 Insight to pierce his patronizing flattery; DC 16 Deception to conceal sovereign intentions from his interrogation.",
      "publicStance": "The devoted elder statesman, administrative guide, and protective mentor of the inexperienced Triumvirate. He projects t...",
      "secretAgenda": "Marquis Mateo intends to maintain complete financial paralysis over the Triumvirate. By strictly controlling the crown's purse strings, he hoards state revenues within private Council-controlled vaults and starves royal projects. He also seeks to eliminate the surviving provincial Grandees' autonomy by forcing them into debt through predatory crown loans.",
      "rival": "High Duke Gonzalo de Guarralid"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">Restoration Council / Bureaucracy</span>\n    <span class=\"badge rival-badge\">Primary Rival: High Duke Gonzalo de Guarralid</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> An aristocratic statesman in his late fifties, dressed in an impeccably tailored black velvet doublet embroidered with silver thread, crowned with an ermine-lined mantle. Slender, soft-handed, and wearing three signet rings bearing pre-Cataclysmic heraldry.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Speaks in smooth, measured cadences; steeples his fingers while listening, offering patronizing smiles that never reach his cold, calculating grey eyes.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;A kingdom is not ruled by steel, Your Majesties, but by ledgers, grain tallies, and patience. Leave the vulgarity of statecraft to those who bled to place that crown upon your brow.&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 17 Insight to pierce his patronizing flattery; DC 16 Deception to conceal sovereign intentions from his interrogation.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>The devoted elder statesman, administrative guide, and protective mentor of the inexperienced Triumvirate. He projects the aura of an exhausted patriot bearing the heavy burden of the realm's immense bankruptcy.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>Marquis Mateo intends to maintain complete financial paralysis over the Triumvirate. By strictly controlling the crown's purse strings, he hoards state revenues within private Council-controlled vaults and starves royal projects. He also seeks to eliminate the surviving provincial Grandees' autonomy by forcing them into debt through predatory crown loans.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>The Treasury Lockout</h4>\n  <p><strong>Premise:</strong> When the Triumvirate attempts to allocate funds for independent city watch recruitment, Marquis Mateo calmly informs them that crown coffers are completely dry, citing foreign debt payments owed to Argos.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must find a way to finance their rule without Council permission: raid an illicit black-market smuggling den in The Pit, audit Mateo's private provincial tax records, or negotiate a risky loan with foreign merchants.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Investigation (audit treasury scrolls to detect missing gold); DC 17 Persuasion/Intimidation (confront Mateo with proof of embezzled revenues).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If confronted directly without unassailable proof, Mateo retaliates by cutting the royal palace's servant and food budgets, claiming 'extreme wartime austerity.'</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>The Venomous Reminder</h4>\n  <p><strong>Premise:</strong> A loyal royal taster or servant collapses during a court banquet from a slow-acting, paralytic poison. A cryptic note left in the servant's pocket warns the PCs against meddling with provincial tax collectors.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must discreetly treat the victim and trace the poison's origin without letting Marquis Mateo's spies learn that they have identified the toxin as originating from his ancestral estate in Sadoria.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 14 Medicine/Arcana (identify the rare Sadorian belladonna derivative); DC 15 Stealth (intercept the courier who delivered the vial).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Failure to identify the poison within 6 hours leaves the loyal retainer permanently paralyzed, depriving the PCs of their only trustworthy informant in the palace kitchens.</p>\n</div>\n\n",
    "gmSecrets": "Marquis Mateo intends to maintain complete financial paralysis over the Triumvirate. By strictly controlling the crown's purse strings, he hoards state revenues within private Council-controlled vaults and starves royal projects. He also seeks to eliminate the surviving provincial Grandees' autonomy by forcing them into debt through predatory crown loans.",
    "relatedIds": [
      "valenza",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "vane",
      "tiberio"
    ]
  },
  {
    "id": "lucia",
    "category": "npcs",
    "title": "Fencing Master Lucia 'La Mariposa' de la Vega",
    "subtitle": "Commander of the Republican Insurgent Network",
    "tags": [
      "Rebel",
      "Republican Insurgents",
      "Fencer",
      "The Pit"
    ],
    "aliases": [
      "La Mariposa",
      "Lucia de la Vega",
      "Lucia",
      "Fencing Master Lucia"
    ],
    "summary": "Commander of the Republican Insurgent Network (Republican Insurgents (The Pit)). In elite court circles, Lucia poses as a sought-after private fencing tutor for high-born noble daughters, navigating elite salons with charming wit a...",
    "atAGlance": {
      "appearance": "A lithe, athletic woman in her late twenties, wearing dark cordwain dueling leathers, a hooded charcoal cloak, and a wide leather baldric supporting a masterwork Zingaran rapier and parrying dagger. A thin dueling scar crosses her left cheekbone.",
      "mannerisms": "Constantly shifts her balance lightly between the balls of her feet, as if anticipating a sudden lunge; speaks with sharp, irreverent wit.",
      "quote": "You wear the golden band of Ancillus, children, but in The Pit, gold does not stop cold steel. Prove you are sovereigns of the people, or bleed like the tyrants before you.",
      "courtDCs": "DC 15 Insight to gauge the sincerity of her truce offers; DC 16 Persuasion to convince her that the Triumvirate is not complicit in Council crimes.",
      "publicStance": "In elite court circles, Lucia poses as a sought-after private fencing tutor for high-born noble daughters, navigating el...",
      "secretAgenda": "As 'La Mariposa,' she commands the clandestine republican insurgent cells operating out of The Pit. Her life goal is the complete destruction of the feudal monarchy and the Restoration Council. She possesses fragment evidence that General Valenza murdered the republican founder during Period VI.",
      "rival": "General Don Rodrigo de Valenza"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">Republican Insurgents (The Pit)</span>\n    <span class=\"badge rival-badge\">Primary Rival: General Don Rodrigo de Valenza</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> A lithe, athletic woman in her late twenties, wearing dark cordwain dueling leathers, a hooded charcoal cloak, and a wide leather baldric supporting a masterwork Zingaran rapier and parrying dagger. A thin dueling scar crosses her left cheekbone.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Constantly shifts her balance lightly between the balls of her feet, as if anticipating a sudden lunge; speaks with sharp, irreverent wit.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;You wear the golden band of Ancillus, children, but in The Pit, gold does not stop cold steel. Prove you are sovereigns of the people, or bleed like the tyrants before you.&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 15 Insight to gauge the sincerity of her truce offers; DC 16 Persuasion to convince her that the Triumvirate is not complicit in Council crimes.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>In elite court circles, Lucia poses as a sought-after private fencing tutor for high-born noble daughters, navigating elite salons with charming wit and flawless etiquette.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>As 'La Mariposa,' she commands the clandestine republican insurgent cells operating out of The Pit. Her life goal is the complete destruction of the feudal monarchy and the Restoration Council. She possesses fragment evidence that General Valenza murdered the republican founder during Period VI.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>The Insurgent's Bargain</h4>\n  <p><strong>Premise:</strong> Lucia arranges a clandestine midnight rendezvous with the PCs in an abandoned crypt beneath Kordava, offering to supply critical intelligence on Council troop movements in exchange for royal pardons for her cell commanders.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must weigh allying with a known revolutionary against the danger of treason accusations if General Valenza's spies uncover the meeting.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Stealth (reach the crypt meeting without being followed by crown watchmen); DC 14 Insight (verify Lucia is not leading them into a kidnapping trap).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If royal guards patrol nearby during the exchange, Lucia assumes betrayal, engages the PCs in a non-lethal fencing duel, and vanishes into the labyrinth of The Pit.</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>Sabotage in the Iron Mines</h4>\n  <p><strong>Premise:</strong> Lucia's underground saboteurs plant alchemical explosives in a crown-controlled iron mine worked by industrial thralls near Jerida, threatening to collapse the facility unless the crown releases captured republican prisoners.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The Triumvirate must intervene personally to negotiate a hostage exchange or disarm the explosives before the collapse destroys a vital royal revenue stream.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 15 Athletics/Acrobatics (navigate the unstable mining shafts); DC 16 Arcana/Thievery (safely defuse the alchemical timing runes).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Detonation causes a cave-in that releases dozens of enraged, memory-retaining mining thralls into the lower valleys, devastating nearby villages.</p>\n</div>\n\n",
    "gmSecrets": "As 'La Mariposa,' she commands the clandestine republican insurgent cells operating out of The Pit. Her life goal is the complete destruction of the feudal monarchy and the Restoration Council. She possesses fragment evidence that General Valenza murdered the republican founder during Period VI.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "vane",
      "tiberio"
    ]
  },
  {
    "id": "malachai",
    "category": "npcs",
    "title": "Father Malachai the Blind",
    "subtitle": "High Priest of the Underground Church of Nemeth the Gnostic",
    "tags": [
      "Priest",
      "Zealot",
      "Church of Nemeth",
      "Theocrat"
    ],
    "aliases": [
      "Father Malachai",
      "Malachai",
      "High Priest of Nemeth"
    ],
    "summary": "High Priest of the Underground Church of Nemeth the Gnostic (Church of Nemeth the Gnostic). A harmless, reclusive mendicant holy man wandering the outskirts of Kordava, tending to destitute beggars and preaching temperance and repentance....",
    "atAGlance": {
      "appearance": "An emaciated, hollow-cheeked zealot cloaked in ragged, unbleached wool vestments cinched with a knotted hemp rope. A heavy white linen blindfold covers his scarred, sightless eye sockets. He carries a gnarled staff of petrified ash topped with an archaic bronze sun.",
      "mannerisms": "Tilts his head sharply when listening, as if hearing divine whispers; speaks in a raspy, hypnotic cadence that rises into furious scripture.",
      "quote": "The flesh of the dead rots the soul of the living! Cleanse this cursed kingdom in the fire of Nemeth, or drown in the reeking tide of your own abominations!",
      "courtDCs": "DC 14 Insight to distinguish between divine prophecy and manic fanaticism; DC 17 Religion to debate theological scripture and calm his zealotry.",
      "publicStance": "A harmless, reclusive mendicant holy man wandering the outskirts of Kordava, tending to destitute beggars and preaching ...",
      "secretAgenda": "Malachai leads the fanatical underground remnants of the Church of Nemeth the Gnostic. He seeks to completely eradicate necromancy, overthrow the secular monarchy, and restore the theocracy that ruled Zingara in Period VI. He is obsessed with finding the lost Fountain of Youth in the Rabirian Mountains.",
      "rival": "Master Alchemist Vane"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">Church of Nemeth the Gnostic</span>\n    <span class=\"badge rival-badge\">Primary Rival: Master Alchemist Vane</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> An emaciated, hollow-cheeked zealot cloaked in ragged, unbleached wool vestments cinched with a knotted hemp rope. A heavy white linen blindfold covers his scarred, sightless eye sockets. He carries a gnarled staff of petrified ash topped with an archaic bronze sun.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Tilts his head sharply when listening, as if hearing divine whispers; speaks in a raspy, hypnotic cadence that rises into furious scripture.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;The flesh of the dead rots the soul of the living! Cleanse this cursed kingdom in the fire of Nemeth, or drown in the reeking tide of your own abominations!&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 14 Insight to distinguish between divine prophecy and manic fanaticism; DC 17 Religion to debate theological scripture and calm his zealotry.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>A harmless, reclusive mendicant holy man wandering the outskirts of Kordava, tending to destitute beggars and preaching temperance and repentance.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>Malachai leads the fanatical underground remnants of the Church of Nemeth the Gnostic. He seeks to completely eradicate necromancy, overthrow the secular monarchy, and restore the theocracy that ruled Zingara in Period VI. He is obsessed with finding the lost Fountain of Youth in the Rabirian Mountains.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>Waters of the Fallen Shrine</h4>\n  <p><strong>Premise:</strong> Father Malachai sends an emissary to the PCs, offering a divine tincture capable of curing an eldritch illness afflicting one of their loyal courtiers, in exchange for royal protection for a hidden Gnostic shrine in the Rabirian Mountains.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The shrine is currently under siege by Argossean mercenaries hired by rival nobles. The PCs must decide whether to dispatch crown forces to protect the heretical shrine or seize the holy relic for themselves.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 15 Survival (guide a relief party through treacherous Rabirian mountain passes); DC 17 Religion (interpret the ancient scripture required to unlock the shrine's inner sanctuary).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If the shrine falls to the mercenaries, the holy spring is tainted with venom, unleashing an outbreak of virulent spiritual plague across the southeastern provinces.</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>The Purging of Edmund's Pits</h4>\n  <p><strong>Premise:</strong> Fanatical Gnostic cultists launch a suicidal raid on an industrial zombie pit overseen by Master Alchemist Vane, setting chemical storage vats ablaze and causing toxic vapors to flood residential districts.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must contain the toxic blaze, prevent Vane's guards from slaughtering peaceful pilgrims caught in the crossfire, and decide whether to prosecute Malachai's zealots or condemn Vane's necromancy.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 14 Constitution Save (resist toxic alchemical fumes); DC 16 Persuasion/Command (force both sides to disengage and extinguish the fire).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Failing to stop the fire within 4 rounds causes a catastrophic chemical explosion that permanently destroys the pit and irradiates the district with necromantic blight.</p>\n</div>\n\n",
    "gmSecrets": "Malachai leads the fanatical underground remnants of the Church of Nemeth the Gnostic. He seeks to completely eradicate necromancy, overthrow the secular monarchy, and restore the theocracy that ruled Zingara in Period VI. He is obsessed with finding the lost Fountain of Youth in the Rabirian Mountains.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "lucia",
      "gonzalo-guarralid",
      "vesper",
      "vane",
      "tiberio"
    ]
  },
  {
    "id": "gonzalo-guarralid",
    "category": "npcs",
    "title": "High Duke Gonzalo de Guarralid",
    "subtitle": "Spokesman of the Grandee Coalitions & Lord of the Highland Estates",
    "tags": [
      "Grandee",
      "Nobility",
      "Pundonor",
      "Highland"
    ],
    "aliases": [
      "Gonzalo de Guarralid",
      "Duke Gonzalo",
      "High Duke Gonzalo",
      "Guarralid"
    ],
    "summary": "Spokesman of the Grandee Coalitions & Lord of the Highland Estates (Grandee Coalitions (Eastern League)). The epitome of traditional Zingaran chivalry and martial pride. He portrays himself as the champion of provincial noble liberties against royal overre...",
    "atAGlance": {
      "appearance": "A broad-shouldered, barrel-chested aristocrat in his early forties, sporting a waxed handlebar mustache and wearing a lavish saffron-and-black slashed silk doublet over a damascened steel breastplate. Plumed felt hat perched arrogantly on his head.",
      "mannerisms": "Boisterous, booming laugh; places his hand on his rapier hilt at the slightest hint of disrespect, eager to demand satisfaction under pundonor.",
      "quote": "The blood of Guarralid flowed in these valleys before Ancillus learned to walk. Do not presume a circlet of gold makes you master of the mountain iron that forged it.",
      "courtDCs": "DC 15 Insight to identify when his swagger masks genuine political anxiety; DC 16 History to cite ancestral treaties that validate crown authority over his fief.",
      "publicStance": "The epitome of traditional Zingaran chivalry and martial pride. He portrays himself as the champion of provincial noble ...",
      "secretAgenda": "Gonzalo heads the Eastern Grandee League, a loose confederation of provincial lords committed to weakening central crown authority. He hoards iron and silver revenues from his mountain mines, refuses crown taxes, and seeks to force the Triumvirate into recognizing absolute provincial autonomy. He uses pundonor challenges to publicly humiliate crown officials.",
      "rival": "High Chancellor Marquis Mateo de Sadoria"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">Grandee Coalitions (Eastern League)</span>\n    <span class=\"badge rival-badge\">Primary Rival: High Chancellor Marquis Mateo de Sadoria</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> A broad-shouldered, barrel-chested aristocrat in his early forties, sporting a waxed handlebar mustache and wearing a lavish saffron-and-black slashed silk doublet over a damascened steel breastplate. Plumed felt hat perched arrogantly on his head.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Boisterous, booming laugh; places his hand on his rapier hilt at the slightest hint of disrespect, eager to demand satisfaction under pundonor.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;The blood of Guarralid flowed in these valleys before Ancillus learned to walk. Do not presume a circlet of gold makes you master of the mountain iron that forged it.&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 15 Insight to identify when his swagger masks genuine political anxiety; DC 16 History to cite ancestral treaties that validate crown authority over his fief.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>The epitome of traditional Zingaran chivalry and martial pride. He portrays himself as the champion of provincial noble liberties against royal overreach and foreign contamination.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>Gonzalo heads the Eastern Grandee League, a loose confederation of provincial lords committed to weakening central crown authority. He hoards iron and silver revenues from his mountain mines, refuses crown taxes, and seeks to force the Triumvirate into recognizing absolute provincial autonomy. He uses pundonor challenges to publicly humiliate crown officials.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>The Challenge of Pundonor</h4>\n  <p><strong>Premise:</strong> During a grand royal reception, Duke Gonzalo publicly mocks the Triumvirate's youth and tactical inexperience, challenging the most martial PC to a formal first-blood fencing duel at dawn.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> Refusing the duel inflicts a permanent -2 penalty to all future social and command checks with Zingaran nobility; accepting risks humiliating public defeat or death against a seasoned swordsman.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Fencing / Attack Roll Contest (fight Gonzalo to first blood); DC 17 Persuasion (reframe the insult into an honorable sporting trial with non-lethal conditions).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If a PC scores a critical success or disarms Gonzalo with spectacular flair, the Duke's wounded pride transforms into grudging respect, granting temporary Grandee political backing.</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>The Tax Revolt of Jerida</h4>\n  <p><strong>Premise:</strong> Duke Gonzalo orders his private garrison in Jerida to seize royal barges carrying timber and ore along the Thunder River, declaring an embargo until the crown cuts provincial customs tariffs.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must travel to Jerida to break the standoff through military intimidation, clever economic compromise, or covert sabotage of Gonzalo's supply lines.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 15 Intimidation (rally local merchants against Gonzalo's embargo); DC 14 Deception/Stealth (smuggle crown goods past the river blockade).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Failure to resolve the embargo within 3 days triggers an armed clash between royal army detachments and Gonzalo's retainers, threatening full civil war.</p>\n</div>\n\n",
    "gmSecrets": "Gonzalo heads the Eastern Grandee League, a loose confederation of provincial lords committed to weakening central crown authority. He hoards iron and silver revenues from his mountain mines, refuses crown taxes, and seeks to force the Triumvirate into recognizing absolute provincial autonomy. He uses pundonor challenges to publicly humiliate crown officials.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "vesper",
      "vane",
      "tiberio"
    ]
  },
  {
    "id": "vesper",
    "category": "npcs",
    "title": "Vesper the Key-Master",
    "subtitle": "Guildmaster of the Shadowed Key & Spymaster of The Pit",
    "tags": [
      "Spymaster",
      "Underworld",
      "The Pit",
      "Smuggler"
    ],
    "aliases": [
      "Vesper",
      "Key-Master",
      "The Key-Master"
    ],
    "summary": "Guildmaster of the Shadowed Key & Spymaster of The Pit (The Pit Underworld / Smugglers). Maintains no public presence at court whatsoever. In upper Kordava, he is whispered of as an urban myth\u2014a spectral broker of illicit antiquities and s...",
    "atAGlance": {
      "appearance": "A wiry, nondescript figure of ambiguous age, wrapped in a mottled grey cloak lined with dozens of hidden pockets, skeleton keys, and small vials. Wears soft leather gloves with reinforced fingertips and a half-mask of blackened silver concealing severe burn scars.",
      "mannerisms": "Speaks in a quiet, dry whisper; constantly manipulates a complex brass puzzle-lock between his fingers with uncanny dexterity.",
      "quote": "Every door in Zingara has a key, Your Majesties. Some are forged of iron, some of gold, and some of dark secrets whispered in the dark. My price is always the same: information.",
      "courtDCs": "DC 16 Insight to detect hidden motives behind his transactions; DC 15 Sleight of Hand to spot his pocketed eavesdropping devices.",
      "publicStance": "Maintains no public presence at court whatsoever. In upper Kordava, he is whispered of as an urban myth\u2014a spectral broke...",
      "secretAgenda": "Vesper controls the subterranean black markets and smuggling tunnels of The Pit. He hoards pre-Cataclysmic artifacts salvaged from the sunken ruins of old Kordava and sells intelligence to the highest bidder. He maintains a secret entrance into the submerged mausoleum of King Kalenius, seeking to plunder the ancient tomb.",
      "rival": "General Don Rodrigo de Valenza"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">The Pit Underworld / Smugglers</span>\n    <span class=\"badge rival-badge\">Primary Rival: General Don Rodrigo de Valenza</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> A wiry, nondescript figure of ambiguous age, wrapped in a mottled grey cloak lined with dozens of hidden pockets, skeleton keys, and small vials. Wears soft leather gloves with reinforced fingertips and a half-mask of blackened silver concealing severe burn scars.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Speaks in a quiet, dry whisper; constantly manipulates a complex brass puzzle-lock between his fingers with uncanny dexterity.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;Every door in Zingara has a key, Your Majesties. Some are forged of iron, some of gold, and some of dark secrets whispered in the dark. My price is always the same: information.&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 16 Insight to detect hidden motives behind his transactions; DC 15 Sleight of Hand to spot his pocketed eavesdropping devices.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>Maintains no public presence at court whatsoever. In upper Kordava, he is whispered of as an urban myth\u2014a spectral broker of illicit antiquities and stolen secrets.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>Vesper controls the subterranean black markets and smuggling tunnels of The Pit. He hoards pre-Cataclysmic artifacts salvaged from the sunken ruins of old Kordava and sells intelligence to the highest bidder. He maintains a secret entrance into the submerged mausoleum of King Kalenius, seeking to plunder the ancient tomb.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>The Tomb of King Kalenius</h4>\n  <p><strong>Premise:</strong> Vesper approaches the PCs through a secret passage in the palace wine cellar, offering a map to the forgotten crypt of King Kalenius beneath Kordava's harbor in exchange for royal immunity for his smuggling guild.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The crypt contains legendary pre-Cataclysmic weapons and the dormant Final Guard (one thousand animate stone warriors), but entering requires diving into flooded tunnels infested with aquatic ghoul constructs.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Athletics/Swimming (navigate flooded abyssal tunnels); DC 15 Arcana (decode the Thurian glyphs sealing the mausoleum gate).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Disturbing the crypt without the proper ritual key awakens six stone guardians who attack relentlessly until subdued or sealed back behind the stone gate.</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>Black-Market Espionage</h4>\n  <p><strong>Premise:</strong> Vesper offers to sell the PCs a stolen correspondence ledger revealing that Ambassador Tiberio of Messantia is bribing royal harbor officials to permit illegal Argossean arms shipments into Zingara.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must decide whether to pay Vesper's exorbitant fee, attempt to steal the ledger from his fortified safehouse in The Pit, or trade a sensitive royal secret in exchange.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Stealth/Thievery (infiltrate Vesper's trap-laden subterranean vault); DC 15 Persuasion/Barter (negotiate a reduced price using royal trade concessions).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Triggering a security ward inside Vesper's safehouse fills the vault with knockout gas and alerts a squad of mute assassin thralls who attempt to capture the intruders.</p>\n</div>\n\n",
    "gmSecrets": "Vesper controls the subterranean black markets and smuggling tunnels of The Pit. He hoards pre-Cataclysmic artifacts salvaged from the sunken ruins of old Kordava and sells intelligence to the highest bidder. He maintains a secret entrance into the submerged mausoleum of King Kalenius, seeking to plunder the ancient tomb.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vane",
      "tiberio"
    ]
  },
  {
    "id": "vane",
    "category": "npcs",
    "title": "Master Alchemist Vane",
    "subtitle": "Overseer of the Royal Labor Pits & Crown Necromancer",
    "tags": [
      "Necromancer",
      "Alchemist",
      "Zombie Pits",
      "Crown Official"
    ],
    "aliases": [
      "Master Vane",
      "Alchemist Vane",
      "Vane"
    ],
    "summary": "Overseer of the Royal Labor Pits & Crown Necromancer (Crown Necromantic Apparatus). Presents himself as a tireless, dispassionate royal civil servant whose alchemical innovations in preserved labor are the only thing preventing the ki...",
    "atAGlance": {
      "appearance": "A gaunt, sallow-skinned scholar in his late forties, smelling intensely of vinegar, sulfur, and embalming resins. Wears a lead-lined leather apron over dark scholarly robes, with heavy tinted glass goggles pushed up onto his bald pate. His fingers are permanently stained deep indigo from alchemical reagents.",
      "mannerisms": "Nervous, jerky movements; compulsively sniffs his fingers and wipes chemical residue onto a stained rag while rambling about labor efficiency metrics.",
      "quote": "The dead do not unionize, Your Grace. They do not demand bread, they do not conspire for republics, and they do not weep when the mine collapses. They are the only loyal subjects you have left.",
      "courtDCs": "DC 14 Insight to recognize when his scientific detachment conceals frantic panic over supply shortages; DC 16 Arcana to evaluate the stability of his preservation compounds.",
      "publicStance": "Presents himself as a tireless, dispassionate royal civil servant whose alchemical innovations in preserved labor are th...",
      "secretAgenda": "Vane is obsessed with unlocking the secrets of Period IV master necromancer Edmund and recovering the legendary Obsidian Blade. He conducts unsanctioned experiments on memory-retaining thralls to discover how to bind their wills permanently without decay, secretly using political dissidents supplied by General Valenza as test subjects.",
      "rival": "Father Malachai the Blind"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">Crown Necromantic Apparatus</span>\n    <span class=\"badge rival-badge\">Primary Rival: Father Malachai the Blind</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> A gaunt, sallow-skinned scholar in his late forties, smelling intensely of vinegar, sulfur, and embalming resins. Wears a lead-lined leather apron over dark scholarly robes, with heavy tinted glass goggles pushed up onto his bald pate. His fingers are permanently stained deep indigo from alchemical reagents.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Nervous, jerky movements; compulsively sniffs his fingers and wipes chemical residue onto a stained rag while rambling about labor efficiency metrics.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;The dead do not unionize, Your Grace. They do not demand bread, they do not conspire for republics, and they do not weep when the mine collapses. They are the only loyal subjects you have left.&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 14 Insight to recognize when his scientific detachment conceals frantic panic over supply shortages; DC 16 Arcana to evaluate the stability of his preservation compounds.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>Presents himself as a tireless, dispassionate royal civil servant whose alchemical innovations in preserved labor are the only thing preventing the kingdom's complete economic collapse.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>Vane is obsessed with unlocking the secrets of Period IV master necromancer Edmund and recovering the legendary Obsidian Blade. He conducts unsanctioned experiments on memory-retaining thralls to discover how to bind their wills permanently without decay, secretly using political dissidents supplied by General Valenza as test subjects.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>The Reeking Pits of Edmund</h4>\n  <p><strong>Premise:</strong> A containment vat fails at Pit #4 near Jerida, unleashing an alchemical sludge spill that threatens to dissolve the support timbers of the main iron shaft and turn dozens of thralls into feral horrors.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> Vane pleads with the Triumvirate to personally authorize the deployment of royal alchemical stockpiles to neutralize the sludge before word leaks to the Church of Nemeth.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 14 Arcana/Crafting (stabilize the chemical counter-agent); DC 15 Constitution Save (endure noxious fumes while securing the containment sluice).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Failure to contain the leak within 1 hour causes the slurry to seep into the local water table, turning downstream livestock and villagers into diseased ghoul-like abominations.</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>The Obsidian Awakening</h4>\n  <p><strong>Premise:</strong> Vane claims to have located an underground fissure beneath The Pit that leads to the tomb of Mad King Daedalus, where the Obsidian Blade is buried. He requests a detachment of crown guards to assist in an excavation expedition.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The PCs must decide whether to sanction the dangerous expedition to claim the ultimate necromantic weapon, knowing it could trigger another starfall anomaly or awaken Daedalus himself.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Arcana/History (identify Daedalus's ancient sealing wards); DC 15 Survival (navigate unstable subterranean ruins prone to tremors).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Breaching the outer seal unleashes an eldritch psychic shockwave that drives nearby mortal guards temporarily mad, forcing the PCs to subdue their own men while defending against emerging crypt horrors.</p>\n</div>\n\n",
    "gmSecrets": "Vane is obsessed with unlocking the secrets of Period IV master necromancer Edmund and recovering the legendary Obsidian Blade. He conducts unsanctioned experiments on memory-retaining thralls to discover how to bind their wills permanently without decay, secretly using political dissidents supplied by General Valenza as test subjects.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "tiberio",
    "category": "npcs",
    "title": "Ambassador Tiberio of Messantia",
    "subtitle": "Special Envoy of the Kingdom of Argos",
    "tags": [
      "Diplomat",
      "Argos",
      "Foreign Power",
      "Trader"
    ],
    "aliases": [
      "Ambassador Tiberio",
      "Tiberio",
      "Envoy Tiberio"
    ],
    "summary": "Special Envoy of the Kingdom of Argos (Kingdom of Argos / Foreign Envoy). The generous, cosmopolitan ambassador from Zingara's wealthy neighbor, offering low-interest merchant loans, grain shipments, and cultural exchange to...",
    "atAGlance": {
      "appearance": "A suave, handsome nobleman in his early thirties with olive skin, impeccably groomed dark curls, and a perfumed goatee. Wears a flowing Argossean silk tunic of sea-green and gold, draped with heavy gold chains set with sapphires and pearls.",
      "mannerisms": "Warm, disarming smile; gestures gracefully with rings on both hands; speaks Zingaran with a musical Argossean accent that flatters listeners.",
      "quote": "Zingara and Argos are like two sisters sharing the same stormy sea, my Lieges. Why quarrel over barren border rocks when our combined merchant galleys could command the wealth of the Western Ocean?",
      "courtDCs": "DC 17 Insight to pierce his warm diplomatic charm and detect calculating economic exploitation; DC 16 Deception to feign economic strength during trade negotiations.",
      "publicStance": "The generous, cosmopolitan ambassador from Zingara's wealthy neighbor, offering low-interest merchant loans, grain shipm...",
      "secretAgenda": "Tiberio's true mission is economic vassalage. He seeks to exploit Zingara's bankruptcy by locking the crown into predatory maritime trade concessions, seizing control of the Baracha Strait, and gathering tactical intelligence on Zingara's coastal defenses for the Argossean Admiralty.",
      "rival": "Vesper the Key-Master"
    },
    "content": "\n<div class=\"npc-header-card\">\n  <div class=\"npc-meta\">\n    <span class=\"badge faction-badge\">Kingdom of Argos / Foreign Envoy</span>\n    <span class=\"badge rival-badge\">Primary Rival: Vesper the Key-Master</span>\n  </div>\n  <div class=\"at-a-glance-grid\">\n    <div class=\"glance-item\"><strong>Appearance:</strong> A suave, handsome nobleman in his early thirties with olive skin, impeccably groomed dark curls, and a perfumed goatee. Wears a flowing Argossean silk tunic of sea-green and gold, draped with heavy gold chains set with sapphires and pearls.</div>\n    <div class=\"glance-item\"><strong>Mannerisms:</strong> Warm, disarming smile; gestures gracefully with rings on both hands; speaks Zingaran with a musical Argossean accent that flatters listeners.</div>\n    <div class=\"glance-item quote\"><strong>Iconic Quote:</strong> &ldquo;Zingara and Argos are like two sisters sharing the same stormy sea, my Lieges. Why quarrel over barren border rocks when our combined merchant galleys could command the wealth of the Western Ocean?&rdquo;</div>\n    <div class=\"glance-item dcs\"><strong>Court Social DCs:</strong> DC 17 Insight to pierce his warm diplomatic charm and detect calculating economic exploitation; DC 16 Deception to feign economic strength during trade negotiations.</div>\n  </div>\n</div>\n\n<h3>Public Persona</h3>\n<p>The generous, cosmopolitan ambassador from Zingara's wealthy neighbor, offering low-interest merchant loans, grain shipments, and cultural exchange to stabilize the fragile Triumvirate.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; SECRET AGENDA &amp; HIDDEN LEVER</div>\n  <p>Tiberio's true mission is economic vassalage. He seeks to exploit Zingara's bankruptcy by locking the crown into predatory maritime trade concessions, seizing control of the Baracha Strait, and gathering tactical intelligence on Zingara's coastal defenses for the Argossean Admiralty.</p>\n</div>\n\n<h3>Player-Led Plot Hooks</h3>\n\n<div class=\"hook-card\">\n  <h4>Blood in the Cauldron</h4>\n  <p><strong>Premise:</strong> Tiberio delivers an ultimatum from the Argossean senate: return the signet ring of an Argossean diplomat slaughtered during Period V, or face an immediate naval embargo of Kordava's harbor.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> The signet ring is currently held by an ancient, memory-retaining thrall trapped in an earthquake-exposed crypt beneath the palace. The PCs must infiltrate the crypt in secret to recover the ring before the deadline expires.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 15 History/Arcana (unravel crypt ward runes); DC 17 Persuasion (convince the memory-retaining thrall to relinquish the signet peacefully).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If the deadline passes, Argossean warships blockade the mouth of the Black River, cutting off all coastal food imports and sparking bread riots in Kordava.</p>\n</div>\n\n<div class=\"hook-card\">\n  <h4>The Barachan Maritime Deal</h4>\n  <p><strong>Premise:</strong> Tiberio secretly approaches the PCs with an offer to finance a new royal naval squadron, provided the Triumvirate grants Argossean privateers free hunting rights against Barachan pirate vessels in Zingaran waters.</p>\n  <p><strong>Core Conflict & Player Choice:</strong> Accepting the deal grants immediate naval strength, but severely antagonizes the Barachan pirate cartels, who threaten to retaliate by raiding Zingara's defenseless coastal fishing towns.</p>\n  <div class=\"dc-box\">\n    <strong>Suggested Skill Checks:</strong> DC 16 Persuasion/Barter (negotiate restrictive clauses that protect Zingaran merchant shipping); DC 15 Insight (spot hidden loopholes in the maritime treaty).\n  </div>\n  <p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Signing the treaty without modifying its terms provokes a coordinated pirate raid on the coastal town of Shar, burning the harbor and taking dozens of hostages.</p>\n</div>\n\n",
    "gmSecrets": "Tiberio's true mission is economic vassalage. He seeks to exploit Zingara's bankruptcy by locking the crown into predatory maritime trade concessions, seizing control of the Baracha Strait, and gathering tactical intelligence on Zingara's coastal defenses for the Argossean Admiralty.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "vane"
    ]
  },
  {
    "id": "court-matrix",
    "category": "npcs",
    "title": "Court Relationship Matrix & Cross-Faction Web",
    "subtitle": "Master Cross-Reference of Loyalties, Stances, Secret Levers, and Rivals",
    "tags": [
      "Court",
      "Matrix",
      "Factions",
      "Rivalries",
      "Quick Reference"
    ],
    "aliases": [
      "Court Matrix",
      "Relationship Matrix",
      "Court Web",
      "NPC Matrix"
    ],
    "summary": "Master matrix of all 8 key court NPCs detailing faction alignment, stated stance toward the PC Triumvirate, secret agenda, and primary court rival.",
    "content": "\n<h3>Court Relationship Matrix & Cross-Faction Web</h3>\n<p>This master matrix maps the lethal political architecture surrounding the PC Triumvirate. Every NPC possesses a public stance, a hidden lever, and a primary rival they seek to destroy.</p>\n\n<div class=\"table-container\">\n<table class=\"wiki-table\">\n  <thead>\n    <tr>\n      <th>NPC Name &amp; Title</th>\n      <th>Primary Faction</th>\n      <th>Stated Stance Toward PCs</th>\n      <th>Secret Agenda / Hidden Lever</th>\n      <th>Primary Court Rival</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td><strong><a href=\"#npcs/valenza\" class=\"wiki-link\">General Don Rodrigo de Valenza</a></strong><br><small>Head of Royal Army</small></td>\n      <td><span class=\"badge\">Military Elite / Restoration Council</span></td>\n      <td>Protective martial defender; loyal guardian of the crown.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Keep PCs dependent on army; conceal Period VI assassination of republican founder.</span></td>\n      <td><a href=\"#npcs/lucia\" class=\"wiki-link\">Lucia de la Vega</a></td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#npcs/sadoria\" class=\"wiki-link\">High Chancellor Marquis Mateo de Sadoria</a></strong><br><small>Chief Monarchist</small></td>\n      <td><span class=\"badge\">Restoration Council / Bureaucracy</span></td>\n      <td>Devoted mentor, elder statesman, and administrative guide.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Restrict royal stipend to keep PCs financially paralyzed; hoard state wealth in Council vaults.</span></td>\n      <td><a href=\"#npcs/gonzalo-guarralid\" class=\"wiki-link\">Duke Gonzalo de Guarralid</a></td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#npcs/lucia\" class=\"wiki-link\">Fencing Master Lucia 'La Mariposa' de la Vega</a></strong><br><small>Republican Commander</small></td>\n      <td><span class=\"badge\">Republican Insurgents (The Pit)</span></td>\n      <td>Openly hostile to monarchy; offers conditional secret pacts.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Expose Council's Period VI assassination plot; dismantle feudal monarchy for a republic.</span></td>\n      <td><a href=\"#npcs/valenza\" class=\"wiki-link\">General Don Rodrigo</a></td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#npcs/malachai\" class=\"wiki-link\">Father Malachai the Blind</a></strong><br><small>High Priest of Nemeth</small></td>\n      <td><span class=\"badge\">Church of Nemeth the Gnostic</span></td>\n      <td>Conditional ally against sorcery; demands religious conversion.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Eradicate all necromancy; clear church's name; find Fountain of Youth to impose divine theocracy.</span></td>\n      <td><a href=\"#npcs/vane\" class=\"wiki-link\">Master Alchemist Vane</a></td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#npcs/gonzalo-guarralid\" class=\"wiki-link\">High Duke Gonzalo de Guarralid</a></strong><br><small>Grandee Representative</small></td>\n      <td><span class=\"badge\">Grandee Coalitions (Eastern League)</span></td>\n      <td>Dismissive of young rulers; demands absolute provincial autonomy.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Weaken central crown tariffs; hoard mountain mineral wealth; test crown strength via duels.</span></td>\n      <td><a href=\"#npcs/sadoria\" class=\"wiki-link\">Marquis Mateo de Sadoria</a></td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#npcs/vesper\" class=\"wiki-link\">Vesper the Key-Master</a></strong><br><small>Spymaster of The Pit</small></td>\n      <td><span class=\"badge\">Underworld Syndicates / Smugglers</span></td>\n      <td>Opportunistic business partner; seller of secrets and relics.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Maintain control of subterranean Pit; profit from pre-Cataclysmic relics and extortion.</span></td>\n      <td><a href=\"#npcs/valenza\" class=\"wiki-link\">General Don Rodrigo</a></td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#npcs/vane\" class=\"wiki-link\">Master Alchemist Vane</a></strong><br><small>Industrial Thrall Overseer</small></td>\n      <td><span class=\"badge\">Crown Necromantic Apparatus</span></td>\n      <td>Obedient technical advisor and supervisor of state thralls.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Expand industrial zombie production for profit; locate Black Blade of Azur or Obsidian Blade.</span></td>\n      <td><a href=\"#npcs/malachai\" class=\"wiki-link\">Father Malachai</a></td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#npcs/tiberio\" class=\"wiki-link\">Ambassador Tiberio of Messantia</a></strong><br><small>Foreign Envoy of Argos</small></td>\n      <td><span class=\"badge\">Kingdom of Argos / Hyborian Powers</span></td>\n      <td>Suave diplomatic ally offering financial loans and trade ties.</td>\n      <td class=\"gm-only-cell\"><span class=\"gm-mask-text\">Exploit political instability; secure intelligence; force naval concessions in Baracha Strait.</span></td>\n      <td><a href=\"#npcs/vesper\" class=\"wiki-link\">Vesper the Key-Master</a></td>\n    </tr>\n  </tbody>\n</table>\n</div>\n",
    "gmSecrets": "The two primary puppetmasters (Valenza and Sadoria) are also secretly in conflict: Valenza wants a military dictatorship, while Sadoria wants an aristocratic oligarchy.",
    "relatedIds": [
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "guarralid",
      "vesper",
      "vane",
      "tiberio"
    ]
  },
  {
    "id": "ancillus-i",
    "category": "history",
    "title": "King Ancillus I",
    "subtitle": "Progenitor Monarch of the Golden Age & Undead Warlord &bull; Period II & Period VII",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period II & Period VII"
    ],
    "aliases": [
      "Ancillus",
      "King Ancillus",
      "Ancillus I"
    ],
    "summary": "Progenitor monarch who welcomed elven scholars and founded Kordava's magical academy. In Period VII, he was reanimated as an undead warlord.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Progenitor Monarch of the Golden Age & Undead Warlord</p>\n  <p><strong>Era of Prominence:</strong> Period II & Period VII</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Welcomed ocean-faring elven scholars to Zingara; founded the realm's premier elven-run magical academy in Kordava; established centuries of cultural prosperity. Centuries after his death, his tomb was desecrated by early necromancers in Period III. During Period VII, he was reanimated as a deathless warlord leading a massive zombie horde to reclaim his crown before being defeated by the mortal alliance.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>His bloodline forms the sole legal basis for royal legitimacy. The PCs derive their right to rule directly from their descent from Ancillus I.</p>\n",
    "gmSecrets": "Relics associated with King Ancillus I can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "printius",
    "category": "history",
    "title": "Printius",
    "subtitle": "Head of the Magical Academy & Co-Founder of Commercial Necromancy &bull; Period III",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period III"
    ],
    "aliases": [
      "Printius"
    ],
    "summary": "Academic leader who abandoned ethical restraints after an earthquake destroyed the academy, partnering with Lord Silkeneth to commercialize undead labor.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Head of the Magical Academy & Co-Founder of Commercial Necromancy</p>\n  <p><strong>Era of Prominence:</strong> Period III</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Led the magical academy during its expansion into commercial discovery. Following the cataclysmic earthquake that destroyed the academy and killed the governing council, Printius abandoned all ethical restraints, partnering with Lord Silkeneth to mass-produce zombie thralls for personal wealth.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>Co-founder of commercialized necromancy; established the techniques used to raise and bind memory-retaining undead.</p>\n",
    "gmSecrets": "Relics associated with Printius can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "silkeneth",
    "category": "history",
    "title": "Lord Silkeneth",
    "subtitle": "Mercenary Nobleman & Architect of Industrial Thrall Mercantilism &bull; Period III",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period III"
    ],
    "aliases": [
      "Silkeneth",
      "Lord Silkeneth"
    ],
    "summary": "Zingaran nobleman who partnered with Printius to transform necromancy from an arcane anomaly into a lucrative, profit-driven enterprise.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Mercenary Nobleman & Architect of Industrial Thrall Mercantilism</p>\n  <p><strong>Era of Prominence:</strong> Period III</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Capitalized on the collapse of the academy council to partner with Printius, transforming necromancy from an arcane anomaly into a lucrative, profit-driven enterprise.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>Established the economic blueprint for industrial undead labor and elevated the Silkeneth family line into dominant historical power brokers.</p>\n",
    "gmSecrets": "Relics associated with Lord Silkeneth can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "edmund",
    "category": "history",
    "title": "Edmund the Necromancer",
    "subtitle": "Master Necromancer & Engineer of the Industrial Zombie Pits &bull; Period IV",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period IV"
    ],
    "aliases": [
      "Edmund",
      "Master Edmund"
    ],
    "summary": "Grandson of Silkeneth who engineered large-scale industrial zombie pits for mining and hazardous labor across Zingara.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Master Necromancer & Engineer of the Industrial Zombie Pits</p>\n  <p><strong>Era of Prominence:</strong> Period IV</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Educated at the ruined magical academy, Edmund expanded his grandfather's commercial operations by engineering large-scale 'zombie pits' across Kordava's periphery and subterranean reaches, systematically institutionalizing mass undead labor.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>Responsible for the physical infrastructure of reeking zombie vats and hazardous mining shafts that dot modern Zingara.</p>\n",
    "gmSecrets": "Relics associated with Edmund the Necromancer can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "daedalus",
    "category": "history",
    "title": "Mad King Daedalus",
    "subtitle": "Tyrannical Monarch of the Starfall & Bearer of the Obsidian Blade &bull; Period V",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period V"
    ],
    "aliases": [
      "Daedalus",
      "Mad King Daedalus",
      "King Daedalus"
    ],
    "summary": "Tyrant who sacrificed Kordava in a ritual for personal godhood using the Obsidian Blade; trapped eternally in rubble after the Starfall meteor strike.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Tyrannical Monarch of the Starfall & Bearer of the Obsidian Blade</p>\n  <p><strong>Era of Prominence:</strong> Period V</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Recovered the Obsidian Blade and promised to restore Zingara as the magical capital of the world. Instead, he unleashed a zombie army upon Kordava, sacrificing his entire capital to fuel a ritual for personal godhood. When the Starfall meteor disrupted his ritual, his cosmic lover, Tanatos, trapped him in eternal, conscious imprisonment beneath the city rubble for boring her.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>Lies buried alive in the rubble beneath The Pit, still holding the Obsidian Blade and bound to his cosmic punishment.</p>\n",
    "gmSecrets": "Relics associated with Mad King Daedalus can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "fergus",
    "category": "history",
    "title": "Fergus the Holy Warrior",
    "subtitle": "Last Human King's Guard & Founder of the Church of Nemeth &bull; Period V & VI",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period V & VI"
    ],
    "aliases": [
      "Fergus",
      "Holy Fergus"
    ],
    "summary": "Guard who rebelled against Daedalus, launched a holy crusade in the name of Nemeth the Gnostic to purge zombies, and established theocratic rule.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Last Human King's Guard & Founder of the Church of Nemeth</p>\n  <p><strong>Era of Prominence:</strong> Period V & VI</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Disillusioned by Daedalus's atrocities, he disobeyed royal orders to slaughter foreign envoys, aided the escape of an incognito religious leader, and eloped with his companion. Drawing upon the martyrological myth of the fanatical cult leader who died in ritual fires and hijacked the horde, Fergus launched a post-Starfall holy crusade in the name of Nemeth the Gnostic to drive back the zombie hordes.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>Revered as the ultimate holy warrior by the underground Church of Nemeth; architect of the theocratic regime that ruled in Period VI.</p>\n",
    "gmSecrets": "Relics associated with Fergus the Holy Warrior can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "tanatos",
    "category": "history",
    "title": "Death (Tanatos)",
    "subtitle": "Cosmic Incarnation of Death & Cosmic Tormentor of Daedalus &bull; Period V",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period V"
    ],
    "aliases": [
      "Tanatos",
      "Death"
    ],
    "summary": "Cosmic incarnation of death and lover of King Daedalus who condemned him to eternal conscious imprisonment beneath Kordava because he bored her.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Cosmic Incarnation of Death & Cosmic Tormentor of Daedalus</p>\n  <p><strong>Era of Prominence:</strong> Period V</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Present at the dawn of the city sacrifice in Kordava, completely checked out and indifferent to mortal bloodletting. Following the Starfall meteor strike, she personally condemned Daedalus to eternal conscious imprisonment beneath the earth because his megalomania proved tedious and boring.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>A lingering, terrifying cosmic presence in Zingaran lore, symbolizing the absolute, inescapable end of all things.</p>\n",
    "gmSecrets": "Relics associated with Death (Tanatos) can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "falmouth",
    "category": "history",
    "title": "Priest Falmouth",
    "subtitle": "High Priest of Nemeth & Discoverer of the Fountain of Youth &bull; Period VI",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period VI"
    ],
    "aliases": [
      "Falmouth",
      "High Priest Falmouth"
    ],
    "summary": "Gnostic priest who discovered the legendary Fountain of Youth in the Rabirian Mountains, securing longevity for the ruling theocracy.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> High Priest of Nemeth & Discoverer of the Fountain of Youth</p>\n  <p><strong>Era of Prominence:</strong> Period VI</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Discovered the legendary Fountain of Youth in the Rabirian Mountains, securing miraculous physical longevity and divine prestige for the church's ruling priesthood. His era ended when the church was overthrown following a child crucifixion scandal.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>Left behind hidden, fanatical theocratic cells and the unresolved legend of the lost Fountain of Youth.</p>\n",
    "gmSecrets": "Relics associated with Priest Falmouth can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "nemeth",
    "category": "history",
    "title": "Nemeth the Gnostic",
    "subtitle": "Divine Entity of Holy Magic & Patron of the Underground Faith &bull; Period VI & Modern",
    "tags": [
      "Historical Figure",
      "Lore",
      "Period VI & Modern"
    ],
    "aliases": [
      "Nemeth",
      "Nemeth the Gnostic"
    ],
    "summary": "Divine figurehead whose teachings inspired the crusade against necromancy; venerated by the outlawed underground Church.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Historical Role:</strong> Divine Entity of Holy Magic & Patron of the Underground Faith</p>\n  <p><strong>Era of Prominence:</strong> Period VI & Modern</p>\n</div>\n<h3>Canonical Actions</h3>\n<p>Inspired Fergus's post-Starfall crusade against the zombie hordes, becoming the central deity of the theocratic regime that governed Zingara in Period VI.</p>\n<h3>Lasting Legacy on Modern Zingara</h3>\n<p>Object of fanatical veneration for the outlawed Church of Nemeth, who seek to restore his divine rule over the kingdom.</p>\n",
    "gmSecrets": "Relics associated with Nemeth the Gnostic can be found in the ruins of The Pit or Rabirian Mountains.",
    "relatedIds": [
      "history-matrix",
      "campaign-premise",
      "court-matrix"
    ]
  },
  {
    "id": "restoration-council",
    "category": "factions",
    "title": "Restoration Council",
    "subtitle": "Shadowy Monarchist Cabal & Aristocratic Bureaucracy",
    "tags": [
      "Faction",
      "Monarchist",
      "Puppetmasters",
      "Council"
    ],
    "aliases": [
      "Restoration Council",
      "Council",
      "Chief Monarchist",
      "Monarchist Cabal"
    ],
    "summary": "The cabal of monarchist elites who elevated the Triumvirate. They control the treasury, bureaucracy, and public policy from behind the throne.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Leadership:</strong> High Chancellor Marquis Mateo de Sadoria & Grandee Bureaucrats</p>\n  <p><strong>Primary Base:</strong> The Crystal Floor Court & Royal Citadel of Kordava</p>\n</div>\n\n<h3>Strategic Agenda</h3>\n<p>Rule from shadows via the PC Triumvirate, hoard state revenues, crush republican and religious dissent, and keep the crown financially dependent.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>\n  <p><strong>Operational Vulnerabilities:</strong> Overconfidence in their ability to manipulate the young PCs; secret guilt and blackmail exposure over the Period VI assassination.</p>\n  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>\n</div>\n",
    "gmSecrets": "Overconfidence in their ability to manipulate the young PCs; secret guilt and blackmail exposure over the Period VI assassination.",
    "relatedIds": [
      "court-matrix",
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "military-elite",
    "category": "factions",
    "title": "The Military Elite & Royal Army Command",
    "subtitle": "Chivalric Caballeros & Professional Garrisons",
    "tags": [
      "Faction",
      "Military",
      "Army",
      "Caballeros"
    ],
    "aliases": [
      "Military Elite",
      "Royal Army",
      "Zingaran Army",
      "Crown Army"
    ],
    "summary": "Commanded by General Valenza. Elite heavy cavalry and disciplined pike blocks that keep the realm safe, but view the PCs as inexperienced figureheads.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Leadership:</strong> General Don Rodrigo de Valenza</p>\n  <p><strong>Primary Base:</strong> The Citadel Fortress of Kordava & Provincial Garrisons</p>\n</div>\n\n<h3>Strategic Agenda</h3>\n<p>Maintain supreme control over the kingdom's armed forces, crush rebel insurrections, defend borders from Argos, and shelter the Triumvirate under an iron guard.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>\n  <p><strong>Operational Vulnerabilities:</strong> Command friction caused by arrogant noble officers; secret guilt over Period VI assassination; overstretched garrisons.</p>\n  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>\n</div>\n",
    "gmSecrets": "Command friction caused by arrogant noble officers; secret guilt over Period VI assassination; overstretched garrisons.",
    "relatedIds": [
      "court-matrix",
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "republican-insurgents",
    "category": "factions",
    "title": "Republican Insurgents",
    "subtitle": "Underground Radical Cells & Fencing Agitators",
    "tags": [
      "Faction",
      "Rebels",
      "Republicans",
      "The Pit"
    ],
    "aliases": [
      "Republican Insurgents",
      "Republicans",
      "The Pit Rebels",
      "La Mariposa Cells"
    ],
    "summary": "Decentralized revolutionary network operating from The Pit. Determined to dismantle the monarchy, they hold dangerous proof of Council assassinations.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Leadership:</strong> Fencing Master Lucia 'La Mariposa' de la Vega</p>\n  <p><strong>Primary Base:</strong> The Pit (Subterranean Kordava) & Secret Rural Safehouses</p>\n</div>\n\n<h3>Strategic Agenda</h3>\n<p>Overthrow the feudal monarchy, expose Council war crimes and political assassinations, dismantle thrall labor, and establish a democratic republic.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>\n  <p><strong>Operational Vulnerabilities:</strong> Fractured command structure post-assassination; lack heavy armor, cavalry, and open battlefield units; reliant on urban ambush tactics.</p>\n  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>\n</div>\n",
    "gmSecrets": "Fractured command structure post-assassination; lack heavy armor, cavalry, and open battlefield units; reliant on urban ambush tactics.",
    "relatedIds": [
      "court-matrix",
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "church-of-nemeth",
    "category": "factions",
    "title": "Church of Nemeth the Gnostic",
    "subtitle": "Underground Fanatical Theocracy & Holy Purifiers",
    "tags": [
      "Faction",
      "Religious",
      "Theocracy",
      "Zealots"
    ],
    "aliases": [
      "Church of Nemeth",
      "Nemeth the Gnostic",
      "Gnostic Church",
      "Nemeth Cult"
    ],
    "summary": "Outlawed holy zealots who view necromancy as an abomination. They seek to recover the Fountain of Youth and cleanse the realm in holy fire.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Leadership:</strong> Father Malachai the Blind</p>\n  <p><strong>Primary Base:</strong> Hidden Catacombs beneath Kordava & Abandoned Rabirian Shrines</p>\n</div>\n\n<h3>Strategic Agenda</h3>\n<p>Eradicate all industrial necromancy, overthrow secular rule, purify the kingdom with holy fire, and restore divine theocratic governance.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>\n  <p><strong>Operational Vulnerabilities:</strong> Deep public distrust stemming from the historical child crucifixion scandal in Period VI; outlawed status makes them hunted pariahs.</p>\n  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>\n</div>\n",
    "gmSecrets": "Deep public distrust stemming from the historical child crucifixion scandal in Period VI; outlawed status makes them hunted pariahs.",
    "relatedIds": [
      "court-matrix",
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "grandees",
    "category": "factions",
    "title": "Grandee Coalitions",
    "subtitle": "Hereditary High Nobility (Eastern & Western Leagues)",
    "tags": [
      "Faction",
      "Nobility",
      "Grandees",
      "Lords"
    ],
    "aliases": [
      "Grandee Coalitions",
      "Grandees",
      "Eastern League",
      "Western League",
      "High Nobility"
    ],
    "summary": "Proud, touchy high nobles who govern private fiefs. They maintain independent armies and challenge royal authority with duels and tax boycotts.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Leadership:</strong> High Duke Gonzalo de Guarralid & Provincial Lords</p>\n  <p><strong>Primary Base:</strong> Autonomous Mountain Fiefdoms, Fortified Castles, & Manorial Estates</p>\n</div>\n\n<h3>Strategic Agenda</h3>\n<p>Maintain near-total provincial autonomy, hoard private mine wealth, evade royal tariffs, and expand private mercenary armies.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>\n  <p><strong>Operational Vulnerabilities:</strong> Internal disunity caused by petty hereditary feuds, commercial rivalries, and hypersensitive pride (pundonor).</p>\n  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>\n</div>\n",
    "gmSecrets": "Internal disunity caused by petty hereditary feuds, commercial rivalries, and hypersensitive pride (pundonor).",
    "relatedIds": [
      "court-matrix",
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "barachan-pirates",
    "category": "factions",
    "title": "Barachan Pirates & Corsairs",
    "subtitle": "Ruthless Maritime Raiders & Freebooters",
    "tags": [
      "Faction",
      "Pirates",
      "Baracha",
      "Corsairs",
      "Naval"
    ],
    "aliases": [
      "Barachan Pirates",
      "Barachan Corsairs",
      "Corsairs",
      "Freebooters"
    ],
    "summary": "Freebooters infesting the southwestern archipelago. They raid merchant galleys, battle Argossean ships, and smuggle relics into Kordava's underworld.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Leadership:</strong> Independent Corsair Captains & Smuggler Barons</p>\n  <p><strong>Primary Base:</strong> Barachan Isles (Shark Island, Darksome Island) & Coastal Coves</p>\n</div>\n\n<h3>Strategic Agenda</h3>\n<p>Plunder merchant shipping in the Baracha Strait, extort coastal settlements, smuggle contraband into The Pit, and sell mercenary naval services.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>\n  <p><strong>Operational Vulnerabilities:</strong> Complete lack of central discipline; easily bought off or swayed by greed, plunder, or internal mutiny.</p>\n  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>\n</div>\n",
    "gmSecrets": "Complete lack of central discipline; easily bought off or swayed by greed, plunder, or internal mutiny.",
    "relatedIds": [
      "court-matrix",
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "foreign-powers",
    "category": "factions",
    "title": "Foreign Powers & Regional Neighbors",
    "subtitle": "Kingdom of Argos, Poitain (Aquilonia), & Pictish Clans",
    "tags": [
      "Faction",
      "Foreign",
      "Argos",
      "Picts",
      "Poitain"
    ],
    "aliases": [
      "Foreign Powers",
      "Kingdom of Argos",
      "Argos",
      "Messantia",
      "Picts",
      "Poitain"
    ],
    "summary": "The predatory neighbors encircling Zingara, ready to carve up the bankrupt realm the moment the Triumvirate falters.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Leadership:</strong> Ambassador Tiberio (Argos), Count of Poitain, Pictish Chiefs</p>\n  <p><strong>Primary Base:</strong> Messantia (Argos), Poitain Frontier, Northern Wilds</p>\n</div>\n\n<h3>Strategic Agenda</h3>\n<p>Argos seeks commercial subjugation and naval control; Poitain guards against raiders; Pictish tribes launch bloodthirsty raids across the northern border.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; FACTION VULNERABILITIES &amp; EXPLOITATION</div>\n  <p><strong>Operational Vulnerabilities:</strong> Argos is vulnerable to pirate disruption; Poitain is preoccupied with Aquilonian civil affairs; Picts are divided into warring clans.</p>\n  <p><strong>Role at the Table:</strong> Can be manipulated, allied with, or targeted by the PC Triumvirate to alter the kingdom's balance of power.</p>\n</div>\n",
    "gmSecrets": "Argos is vulnerable to pirate disruption; Poitain is preoccupied with Aquilonian civil affairs; Picts are divided into warring clans.",
    "relatedIds": [
      "court-matrix",
      "valenza",
      "sadoria",
      "lucia",
      "malachai",
      "gonzalo-guarralid",
      "vesper",
      "tiberio"
    ]
  },
  {
    "id": "kordava",
    "category": "gazetteer",
    "title": "Kordava",
    "subtitle": "Coastal Port, Royal Capital, & Seat of the Crystal Floor Court",
    "tags": [
      "Gazetteer",
      "Capital",
      "Court",
      "Coast"
    ],
    "aliases": [
      "Kordava",
      "The Capital",
      "Royal Citadel",
      "Crystal Floor Court"
    ],
    "summary": "The political and economic heart of Zingara at the mouth of the Black River. Famous for whitewashed arcades, fencing academies, and the Crystal Floor Court.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Capital City / Coastal Fortress</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Seat of the royal court, foreign diplomacy, naval shipyards, and merchant harbor.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Court conspiracies, royal army patrols, dueling hotheads in plazas, hidden assassins.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>Situated dramatically at the mouth of the Black River where its dark waters spill into the Western Ocean, modern Kordava is the political and economic center of Zingara. Renowned for its royal court with its famous floor of polished crystal, the surface city features prestigious fencing academies (esgrimas), grand whitewashed arcades, and massive sea-facing bastions. However, this chivalric splendor sits directly atop a hollow, ruined foundation\u2014the subterranean labyrinth of The Pit.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Court conspiracies, royal army patrols, dueling hotheads in plazas, hidden assassins.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Court conspiracies, royal army patrols, dueling hotheads in plazas, hidden assassins.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "the-pit",
    "category": "gazetteer",
    "title": "The Pit",
    "subtitle": "Subterranean Sunken Ruins beneath Kordava",
    "tags": [
      "Gazetteer",
      "Subterranean",
      "The Pit",
      "Ruins",
      "Underworld"
    ],
    "aliases": [
      "The Pit",
      "Subterranean Depths",
      "Sunken Ruins",
      "Old Kordava"
    ],
    "summary": "Sunless subterranean labyrinth formed when Old Kordava was swallowed by earthquake and starfall. Ruled by smugglers, outlaws, and republican rebels.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Subterranean Labyrinth / Criminal Haven</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Black markets, criminal syndicates, pre-Cataclysmic relic caches, underground insurgent hideouts.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Rogue zombie thralls, toxic cave-ins, criminal ambushes, eldritch radiation, ancient stone guardians.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>Sprawling beneath the streets of modern Kordava lies The Pit\u2014a sunless, lawless subterranean labyrinth formed when old Kordava was swallowed by earthquake and starfall. Excavated over generations by outlaws, deserters, and runaway thralls, it is ruled by criminal syndicates, renegade duelists, and republican insurgent cells. Deep beneath the rubble lie two legendary relics: the Black Blade of Azur and the Obsidian Blade.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Rogue zombie thralls, toxic cave-ins, criminal ambushes, eldritch radiation, ancient stone guardians.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Rogue zombie thralls, toxic cave-ins, criminal ambushes, eldritch radiation, ancient stone guardians.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "mausoleum-kalenius",
    "category": "gazetteer",
    "title": "Submerged Mausoleum of King Kalenius",
    "subtitle": "Abyssal Pre-Cataclysmic Crypt & The Final Guard",
    "tags": [
      "Gazetteer",
      "Tomb",
      "Ancient",
      "Relic",
      "The Pit"
    ],
    "aliases": [
      "Mausoleum of King Kalenius",
      "Tomb of Kalenius",
      "King Kalenius Crypt",
      "The Final Guard"
    ],
    "summary": "Deepest abyssal reach beneath Kordava's harbor. Contains the ancient tomb of Thurian King Kalenius, guarded by 1,000 elite warriors turned to animate stone.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Underwater Ancient Tomb</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Holds pre-Cataclysmic Thurian weaponry, ancient armor, and the dormant Final Guard.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Flooded vertical shafts, aquatic ghoul constructs, 1,000 animate stone guardians.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>Located in the deepest abyssal reaches of The Pit beneath Kordava's harbor lies the ancient pre-Cataclysmic tomb of King Kalenius\u2014a legendary monarch of the ancient Thurian Age. Kalenius's mausoleum is permanently guarded by the Final Guard\u2014one thousand elite ancient Thurian warriors transformed into deathless, animate stone.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Flooded vertical shafts, aquatic ghoul constructs, 1,000 animate stone guardians.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Flooded vertical shafts, aquatic ghoul constructs, 1,000 animate stone guardians.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "zingg-valley",
    "category": "gazetteer",
    "title": "Zingg Valley",
    "subtitle": "Fertile River Basin & Agricultural Heartland",
    "tags": [
      "Gazetteer",
      "Heartland",
      "Valley",
      "Agriculture"
    ],
    "aliases": [
      "Zingg Valley",
      "Zingg",
      "Valley of Zingg"
    ],
    "summary": "Fertile agricultural spine of Zingara. Dotted with fortified manorial estates, sprawling vineyards, olive groves, and ancient buried relics.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Agricultural River Basin</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Breadbasket of the kingdom; extensive vineyards, olive groves, and ancestral manors.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Republican guerrilla raiding, hidden Gnostic shrines, noble border skirmishes.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>Bounded by rolling pastoral hills and fed by river tributaries, the Zingg Valley is the food-producing heartland of the nation. Sprawling vineyards, ancient olive groves, and fortified manorial estates dominate the landscape. Historically settled by Shemitish agriculturalists before Pictish and Hyborian conquests, it remains a battleground for local noble feuds and hidden Church shrines.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Republican guerrilla raiding, hidden Gnostic shrines, noble border skirmishes.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Republican guerrilla raiding, hidden Gnostic shrines, noble border skirmishes.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "jerida",
    "category": "gazetteer",
    "title": "Jerida",
    "subtitle": "Fortified Inland River Port on the Lower Thunder River",
    "tags": [
      "Gazetteer",
      "Port",
      "Trade",
      "Thunder River"
    ],
    "aliases": [
      "Jerida",
      "Port Jerida"
    ],
    "summary": "Heavily fortified river port acting as the critical trade gateway between the interior and the coast, controlling timber and iron distribution.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> River Port / Trade Bastion</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Controls trade of northern timber floated downriver and iron ore hauled from mountain mines.</p>\n  <p><strong>Primary Encounter Hazards:</strong> River pirates, corrupt customs inspectors, mercenary blockades, thrall labor riots.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>A heavily fortified river port acting as the critical trade gateway between the interior and the coast. Jerida controls the distribution of northern timber floated down river and iron ore hauled out of interior mountain mines. It is garrisoned by paranoid river customs officials and mercenary companies.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> River pirates, corrupt customs inspectors, mercenary blockades, thrall labor riots.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "River pirates, corrupt customs inspectors, mercenary blockades, thrall labor riots.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "guarralid",
    "category": "gazetteer",
    "title": "Guarralid Highlands",
    "subtitle": "Autonomous Mountain Duchy & Mining Fiefdom",
    "tags": [
      "Gazetteer",
      "Mountains",
      "Highlands",
      "Mines"
    ],
    "aliases": [
      "Guarralid",
      "Duchy of Guarralid",
      "Guarralid Highlands"
    ],
    "summary": "Fiercely independent highland duchy governed by proud Grandees. Controls mountain iron mines and maintains an independent private army.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Mountain Highlands / Autonomous Duchy</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Vast mineral wealth (iron, silver), defensive highland passes, private standing army.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Grandee private armies, hereditary feud ambushes, treacherous mountain terrain.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>A powerful, fiercely independent interior duchy located in the highlands. Governed by proud Grandees who hoard private mineral wealth, Guarralid maintains an independent standing army and is plagued by bloody, hereditary border feuds with neighboring provinces.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Grandee private armies, hereditary feud ambushes, treacherous mountain terrain.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Grandee private armies, hereditary feud ambushes, treacherous mountain terrain.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "sadoria-kova",
    "category": "gazetteer",
    "title": "Sadoria & Kova",
    "subtitle": "Central Agricultural Plains & Warhorse Hubs",
    "tags": [
      "Gazetteer",
      "Plains",
      "Agriculture",
      "Horses"
    ],
    "aliases": [
      "Sadoria",
      "Kova",
      "Sadoria & Kova",
      "Central Provinces"
    ],
    "summary": "Prime agricultural hubs in central/western Zingara, famous across the Hyborian world for breeding warhorses and operating massive manorial estates.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Rolling Agricultural Plains</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Breeding of high-mettled Hyborian warhorses, citrus production, grain estates.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Thrall labor revolts, noble press-gangs, highwaymen, alchemical pit runoff.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>Prime agricultural hubs dominating central and western Zingara. Renowned across the Hyborian world for breeding high-mettled warhorses, cultivating extensive citrus groves, and operating vast manorial estates worked by bonded peasants and industrial thrall labor.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Thrall labor revolts, noble press-gangs, highwaymen, alchemical pit runoff.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Thrall labor revolts, noble press-gangs, highwaymen, alchemical pit runoff.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "baracha-strait",
    "category": "gazetteer",
    "title": "Baracha Strait & Isles",
    "subtitle": "Reef-Choked Pirate Archipelago",
    "tags": [
      "Gazetteer",
      "Maritime",
      "Islands",
      "Pirates"
    ],
    "aliases": [
      "Baracha Strait",
      "Barachan Isles",
      "Shark Island",
      "Darksome Island"
    ],
    "summary": "Treacherous, reef-choked waters off the southwestern coast. Haunt of ruthless Barachan corsairs, privateers, and smugglers.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Maritime Island Chain / Coral Reefs</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Dominates coastal trade lanes to Argos; pirate havens (Shark Island, Darksome Island).</p>\n  <p><strong>Primary Encounter Hazards:</strong> Barachan corsairs, naval privateer skirmishes, sudden oceanic squalls, razor reefs.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>The treacherous, reef-choked maritime corridor off the southwestern coast. The strait separates the mainland from the pirate-infested Barachan Isles\u2014including infamous havens like Shark Island and Darksome Island. These waters host relentless skirmishes between Zingaran merchantmen, royal privateers, and ruthless corsairs.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Barachan corsairs, naval privateer skirmishes, sudden oceanic squalls, razor reefs.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Barachan corsairs, naval privateer skirmishes, sudden oceanic squalls, razor reefs.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "forest-of-ghouls",
    "category": "gazetteer",
    "title": "Forest of Ghouls & City of the Ghouls",
    "subtitle": "Primeval Gloom-Draped Cursed Wilderness",
    "tags": [
      "Gazetteer",
      "Wilderness",
      "Horror",
      "Ruins"
    ],
    "aliases": [
      "Forest of Ghouls",
      "City of the Ghouls"
    ],
    "summary": "Gloom-draped wilderness in southeastern Zingara. Hides the ancient City of the Ghouls, where feral undead and forgotten cults wander marble ruins.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Cursed Wilderness / Ancient Ruins</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Pre-Cataclysmic ruin salvage, rare alchemical reagents, ancient forbidden texts.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Feral ghouls, wandering necromantic constructs, lost cultists, toxic miasma.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>A primeval, gloom-draped wilderness in southeastern Zingara near the Rabirian border. Avoided by commoners and knights alike, this superstitious forest conceals the ancient, cursed City of the Ghouls, where feral necromantic constructs, rogue ghouls, and forgotten cults wander through overgrown marble ruins.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Feral ghouls, wandering necromantic constructs, lost cultists, toxic miasma.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Feral ghouls, wandering necromantic constructs, lost cultists, toxic miasma.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "pictish-wilderness",
    "category": "gazetteer",
    "title": "Pictish Wilderness",
    "subtitle": "Untamed Northern Frontier & Savage Jungle",
    "tags": [
      "Gazetteer",
      "Borderlands",
      "Picts",
      "Wilderness"
    ],
    "aliases": [
      "Pictish Wilderness",
      "Pictish Frontier",
      "Northern Border"
    ],
    "summary": "Savage northern frontier beyond Zingara's border. Dense forests give way to hostile barbarian tribes who frequently launch bloodthirsty raids.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Frontier Wilderness / Jungle</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Timber reserves, pelts, natural buffer against northern barbarians.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Pictish raiding warbands, wild beasts, uncharted treacherous swamps.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>The savage, untamed northern frontier lying beyond Zingara's northern border. Dense, dark forests give way to hostile barbarian tribes who frequently launch bloodthirsty raiding parties against border settlements.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Pictish raiding warbands, wild beasts, uncharted treacherous swamps.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Pictish raiding warbands, wild beasts, uncharted treacherous swamps.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "poitain-alimane",
    "category": "gazetteer",
    "title": "Poitain Mountains & River Alimane",
    "subtitle": "Northeastern Alpine Frontier with Aquilonia",
    "tags": [
      "Gazetteer",
      "Mountains",
      "Borderlands",
      "Poitain"
    ],
    "aliases": [
      "Poitain Mountains",
      "River Alimane",
      "Alimane"
    ],
    "summary": "Rugged northeastern mountain range and border river separating Zingara from Poitain, the prosperous southern province of Aquilonia.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Alpine Mountain Border / Frontier River</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Natural barrier protecting against northern invasion; alpine trade routes.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Mountain avalanches, Aquilonian border patrols, smuggler ambushes.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>Marking the northeastern frontier, this rugged mountain range and its cascading border river, the Alimane, separate Zingara from Poitain, the prosperous southern province of Aquilonia.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Mountain avalanches, Aquilonian border patrols, smuggler ambushes.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Mountain avalanches, Aquilonian border patrols, smuggler ambushes.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "rabirian-mountains",
    "category": "gazetteer",
    "title": "Rabirian Mountains",
    "subtitle": "Southeastern Barrier Range & Caches of the Fountain",
    "tags": [
      "Gazetteer",
      "Mountains",
      "Borderlands",
      "Fountain of Youth"
    ],
    "aliases": [
      "Rabirian Mountains",
      "Rabirian Range"
    ],
    "summary": "Jagged southeastern range forming the border with Argos. Its high passes conceal abandoned theocratic shrines and the legendary Fountain of Youth.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Jagged Barrier Mountain Range</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Border defense against Argos; conceals abandoned Gnostic shrines and the Fountain of Youth.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Mountain bandits, Gnostic religious fanatics, sheer cliff passes.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>A jagged, barrier-like southeastern range forming the natural border between Zingara and the Kingdom of Argos. Its high passes are haunted by mountain bandits and conceal abandoned theocratic shrines. Sealed deep within one of these mountain shrines lies the legendary Fountain of Youth.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Mountain bandits, Gnostic religious fanatics, sheer cliff passes.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Mountain bandits, Gnostic religious fanatics, sheer cliff passes.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "kingdom-of-argos",
    "category": "gazetteer",
    "title": "Kingdom of Argos & Port Messantia",
    "subtitle": "Ancient Maritime Rival & Wealthy Merchant Empire",
    "tags": [
      "Gazetteer",
      "Foreign",
      "Argos",
      "Messantia"
    ],
    "aliases": [
      "Kingdom of Argos",
      "Argos",
      "Messantia"
    ],
    "summary": "Zingara's ancient maritime rival to the southeast. Relations are perpetually tense over naval blockades, privateer skirmishes, and predatory loans.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Geographical Classification:</strong> Foreign Maritime Empire</p>\n  <p><strong>Strategic &amp; Economic Value:</strong> Vast naval commerce, banking conglomerates, maritime trade concessions.</p>\n  <p><strong>Primary Encounter Hazards:</strong> Argossean naval squadrons, foreign spies, predatory merchant lenders.</p>\n</div>\n\n<h3>Geographical Overview</h3>\n<p>Zingara's ancient maritime rival to the southeast. Sharing a bitter history of commercial warfare, privateer skirmishes, and naval blockades, tension between Kordava and Messantia remains at a perpetual boiling point.</p>\n\n<div class=\"gm-callout\">\n  <div class=\"gm-badge\">GM CONFIDENTIAL &bull; TABLE ENCOUNTERS &amp; PLOT LEADS</div>\n  <p><strong>Encounter Complications:</strong> Argossean naval squadrons, foreign spies, predatory merchant lenders.</p>\n  <p>When running sessions here, emphasize the local environmental flavor and social tension.</p>\n</div>\n",
    "gmSecrets": "Argossean naval squadrons, foreign spies, predatory merchant lenders.",
    "relatedIds": [
      "kordava",
      "the-pit",
      "zingg-valley",
      "jerida",
      "guarralid",
      "baracha-strait"
    ]
  },
  {
    "id": "period-i",
    "category": "history",
    "title": "Period I: The Gift",
    "subtitle": "Founding of the Realm & The Buried Blade",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period I: The Gift",
      "period i"
    ],
    "summary": "Kingdom founded in Zingg Valley; Black Blade of Azur forged by sorcerer; sorcerer executed; blade buried underground.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> Kingdom founded in Zingg Valley; Black Blade of Azur forged by sorcerer; sorcerer executed; blade buried underground.</p>\n  <p><strong>Key Historical Figures:</strong> Founding Monarch, Youngest Son, Executed Sorcerer</p>\n  <p><strong>Lasting Legacy:</strong> Established core national territory and buried the primary anti-sorcery relic beneath the valley.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>In the earliest era, pastoral agriculturalists settled the fertile Zingg Valley. A sorcerer forged the Black Blade of Azur\u2014a blade of pure anti-magic. Fearing its terrifying power, the founding king executed the sorcerer and buried the blade deep beneath the earth, laying the foundation of the kingdom.</p>\n",
    "gmSecrets": "Events from Period I: The Gift directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "period-ii",
    "category": "history",
    "title": "Period II: Time of the Elves",
    "subtitle": "The Golden Age of Ancillus I & Elven Academies",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period II: Time of the Elves",
      "period ii"
    ],
    "summary": "Arrival of ocean-faring elven longships; era of cross-cultural peace and enrichment; founding of the elven-run magical academy in Kordava.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> Arrival of ocean-faring elven longships; era of cross-cultural peace and enrichment; founding of the elven-run magical academy in Kordava.</p>\n  <p><strong>Key Historical Figures:</strong> King Ancillus I, Elven Scholars</p>\n  <p><strong>Lasting Legacy:</strong> Codified advanced arcane traditions and established elven architectural and academic influence.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>Ocean-faring elven longships arrived along the Zingaran coast. King Ancillus I welcomed the scholars with open arms, forging an alliance that established centuries of golden peace. The elven scholars built a renowned magical academy in Kordava, elevating Zingara to the pinnacle of civilization.</p>\n",
    "gmSecrets": "Events from Period II: Time of the Elves directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "period-iii",
    "category": "history",
    "title": "Period III: The Magical Capital",
    "subtitle": "The Desecration, The Earthquake, & The First Undead",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period III: The Magical Capital",
      "period iii"
    ],
    "summary": "First zombie created; tomb of Ancillus I desecrated; earthquake subsumes academy; Black Blade lost; necromancy commercialized.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> First zombie created; tomb of Ancillus I desecrated; earthquake subsumes academy; Black Blade lost; necromancy commercialized.</p>\n  <p><strong>Key Historical Figures:</strong> Printius, Lord Silkeneth, King Ancillus I (deceased)</p>\n  <p><strong>Lasting Legacy:</strong> Created the subterranean sunken ruins beneath Kordava and introduced profit-driven necromancy.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>Hubris overtook the academy. Scholars desecrated the tomb of Ancillus I to experiment with soul-binding, creating the first conscious undead thrall. A catastrophic earthquake shattered the city, swallowing the academy into the abyss. In the chaos, Printius and Lord Silkeneth partnered to turn necromancy into a commercial goldmine.</p>\n",
    "gmSecrets": "Events from Period III: The Magical Capital directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "period-iv",
    "category": "history",
    "title": "Period IV: The Zombie Era",
    "subtitle": "Edmund's Industrial Necromancy & Thrall Mines",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period IV: The Zombie Era",
      "period iv"
    ],
    "summary": "Industrialization of undead labor; construction of vast 'zombie pits' for mining and hazardous labor across the realm.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> Industrialization of undead labor; construction of vast 'zombie pits' for mining and hazardous labor across the realm.</p>\n  <p><strong>Key Historical Figures:</strong> Edmund (grandson of Silkeneth)</p>\n  <p><strong>Lasting Legacy:</strong> Shifted the kingdom's economy to rely permanently on thrall labor; left reeking necromantic vats across the land.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>Edmund, grandson of Silkeneth, institutionalized mass undead labor on an industrial scale. Massive pits were dug across the kingdom to mine iron and toxic minerals using memory-retaining thralls. The Zingaran economy became permanently addicted to unpaid undead labor, creating deep social rot.</p>\n",
    "gmSecrets": "Events from Period IV: The Zombie Era directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "period-v",
    "category": "history",
    "title": "Period V: Mad King Daedalus & The Starfall",
    "subtitle": "The City Sacrifice, Cosmic Ruin, & The Obsidian Blade",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period V: Mad King Daedalus & The Starfall",
      "period v"
    ],
    "summary": "Obsidian Blade unearthed; city sacrifice of Kordava; Starfall meteor strike; Daedalus trapped; cult leader hijacks horde.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> Obsidian Blade unearthed; city sacrifice of Kordava; Starfall meteor strike; Daedalus trapped; cult leader hijacks horde.</p>\n  <p><strong>Key Historical Figures:</strong> King Daedalus, Fergus, Tanatos (Death), Cult Leader</p>\n  <p><strong>Lasting Legacy:</strong> Shattered old Kordava into rubble; created memory-retaining zombie hordes; birthed Church of Nemeth via cult leader's martyrdom.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>Mad King Daedalus unearthed the Obsidian Blade, sacrificing his own capital to fuel an eldritch ritual for godhood alongside his cosmic lover, Tanatos. Mid-ritual, a cosmic Starfall meteor pulverized Old Kordava. Tanatos imprisoned Daedalus alive beneath the rubble for boring her, while a martyred cult leader hijacked the undead horde.</p>\n",
    "gmSecrets": "Events from Period V: Mad King Daedalus & The Starfall directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "period-vi",
    "category": "history",
    "title": "Period VI: Religious Rulership & Fall",
    "subtitle": "The Gnostic Holy Crusade, The Fountain, & Child Crucifixion",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period VI: Religious Rulership & Fall",
      "period vi"
    ],
    "summary": "Holy crusade against zombies; Fountain of Youth found; child crucifixion scandal; monarchist-republican coup; covert murder.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> Holy crusade against zombies; Fountain of Youth found; child crucifixion scandal; monarchist-republican coup; covert murder.</p>\n  <p><strong>Key Historical Figures:</strong> Fergus, Falmouth, Nemeth the Gnostic, Head of Army (Don Rodrigo)</p>\n  <p><strong>Lasting Legacy:</strong> Left hidden theocratic cults; created deep monarchist-republican rift; lost the Fountain of Youth.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>Fergus led a holy crusade in the name of Nemeth the Gnostic, driving back the zombies and establishing a theocracy. Priest Falmouth discovered the Fountain of Youth. But the church collapsed after a horrific child crucifixion scandal. Monarchists and republicans united to overthrow the priests, only for General Valenza to covertly murder the republican leader.</p>\n",
    "gmSecrets": "Events from Period VI: Religious Rulership & Fall directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "period-vii",
    "category": "history",
    "title": "Period VII: Restoration Civil War",
    "subtitle": "The Return of Undead King Ancillus & The Puppetmaster Coup",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period VII: Restoration Civil War",
      "period vii"
    ],
    "summary": "Discovery of Ancillus's lineage; republican revolt; return of undead King Ancillus I; mortal alliance and monarchist betrayal.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> Discovery of Ancillus's lineage; republican revolt; return of undead King Ancillus I; mortal alliance and monarchist betrayal.</p>\n  <p><strong>Key Historical Figures:</strong> Undead King Ancillus I, Restoration Council, General Valenza, Marquis Mateo</p>\n  <p><strong>Lasting Legacy:</strong> Decimated population; crippled republican leadership through assassination; cemented monarchist control.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>A catastrophic civil war erupted. Necromancers resurrected King Ancillus I as an undead warlord leading a zombie legion to reclaim his throne. Monarchists and republicans forged a temporary truce to destroy the undead king. Once victorious, the Restoration Council seized power and purged the weakened republicans.</p>\n",
    "gmSecrets": "Events from Period VII: Restoration Civil War directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "period-viii",
    "category": "history",
    "title": "Period VIII: The Besieged Kingdom",
    "subtitle": "Current Campaign Era: The Triumvirate's Ascendancy Trap",
    "tags": [
      "History",
      "Chronology",
      "Lore"
    ],
    "aliases": [
      "Period VIII: The Besieged Kingdom",
      "period viii"
    ],
    "summary": "Installation of PC Triumvirate by puppetmasters; growth of 'The Pit'; multi-front insurgent and foreign threats.",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Defining Events:</strong> Installation of PC Triumvirate by puppetmasters; growth of 'The Pit'; multi-front insurgent and foreign threats.</p>\n  <p><strong>Key Historical Figures:</strong> The Triumvirate (Player Characters), General Valenza, Marquis Mateo, Faction Leaders</p>\n  <p><strong>Lasting Legacy:</strong> Modern campaign era: an unstable, bankrupt state ruled by inexperienced monarchs surrounded by enemies.</p>\n</div>\n\n<h3>Historical Narrative</h3>\n<p>The current campaign epoch. The Player Characters are installed as the Triumvirate on the crystal throne of Kordava. Surrounding them are greedy handlers, rebellious grandees, underground zealots, and lurking relics in the depths.</p>\n",
    "gmSecrets": "Events from Period VIII: The Besieged Kingdom directly inform modern conspiracy hooks and ancient subterranean relics in The Pit.",
    "relatedIds": [
      "history-matrix",
      "ancillus-i",
      "daedalus",
      "valenza",
      "sadoria"
    ]
  },
  {
    "id": "history-matrix",
    "category": "history",
    "title": "Historical Chronology Master Matrix",
    "subtitle": "Eight-Period Timeline of Zingaran Cataclysm and Rebirth",
    "tags": [
      "History",
      "Timeline",
      "Matrix",
      "Quick Reference"
    ],
    "aliases": [
      "Historical Matrix",
      "Timeline",
      "Eight Periods",
      "Chronology Matrix"
    ],
    "summary": "Master reference matrix outlining all eight historical epochs from the founding gift to the modern Besieged Kingdom.",
    "content": "\n<h3>Historical Chronology Master Matrix</h3>\n<div class=\"table-container\">\n<table class=\"wiki-table\">\n  <thead>\n    <tr>\n      <th>Period &amp; Name</th>\n      <th>Defining Canonical Events</th>\n      <th>Key Historical Figures</th>\n      <th>Lasting Legacy on Modern Zingara</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td><strong><a href=\"#history/period-i\" class=\"wiki-link\">I: The Gift</a></strong></td>\n      <td>Kingdom founded in Zingg Valley; Black Blade forged by sorcerer; sorcerer executed; blade buried underground.</td>\n      <td>Founding Monarch, Executed Sorcerer</td>\n      <td>Established core territory and buried primary anti-sorcery relic beneath valley.</td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#history/period-ii\" class=\"wiki-link\">II: Time of the Elves</a></strong></td>\n      <td>Arrival of elven longships; cross-cultural peace; founding of magical academy in Kordava.</td>\n      <td><a href=\"#history/ancillus-i\" class=\"wiki-link\">King Ancillus I</a>, Elven Scholars</td>\n      <td>Codified advanced arcane traditions and elven architectural influence.</td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#history/period-iii\" class=\"wiki-link\">III: Magical Capital</a></strong></td>\n      <td>First zombie created; tomb of Ancillus desecrated; earthquake subsumes academy; Black Blade lost; necromancy commercialized.</td>\n      <td><a href=\"#history/printius\" class=\"wiki-link\">Printius</a>, <a href=\"#history/silkeneth\" class=\"wiki-link\">Lord Silkeneth</a></td>\n      <td>Created subterranean sunken ruins beneath Kordava; introduced commercial undead labor.</td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#history/period-iv\" class=\"wiki-link\">IV: Zombie Era</a></strong></td>\n      <td>Industrialization of undead labor; vast zombie pits engineered across the realm for mining.</td>\n      <td><a href=\"#history/edmund\" class=\"wiki-link\">Edmund the Necromancer</a></td>\n      <td>Permanently shifted economy to rely on thrall labor; left toxic vats across the realm.</td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#history/period-v\" class=\"wiki-link\">V: Mad King Daedalus</a></strong></td>\n      <td>Obsidian Blade unearthed; city sacrifice of Kordava; Starfall meteor strike; Daedalus imprisoned by Tanatos.</td>\n      <td><a href=\"#history/daedalus\" class=\"wiki-link\">King Daedalus</a>, <a href=\"#history/tanatos\" class=\"wiki-link\">Tanatos</a>, <a href=\"#history/fergus\" class=\"wiki-link\">Fergus</a></td>\n      <td>Shattered old Kordava into rubble; created memory-retaining zombie hordes; birthed Church of Nemeth.</td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#history/period-vi\" class=\"wiki-link\">VI: Religious Rulership</a></strong></td>\n      <td>Holy crusade against zombies; Fountain of Youth found; child crucifixion scandal; coup; covert murder.</td>\n      <td><a href=\"#history/fergus\" class=\"wiki-link\">Fergus</a>, <a href=\"#history/falmouth\" class=\"wiki-link\">Falmouth</a>, <a href=\"#history/nemeth\" class=\"wiki-link\">Nemeth</a>, <a href=\"#npcs/valenza\" class=\"wiki-link\">General Valenza</a></td>\n      <td>Left hidden theocratic cults; created monarchist-republican rift; lost the Fountain of Youth.</td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#history/period-vii\" class=\"wiki-link\">VII: Restoration Civil War</a></strong></td>\n      <td>Discovery of Ancillus lineage; republican revolt; undead King Ancillus I returns; alliance and betrayal.</td>\n      <td>Undead Ancillus I, <a href=\"#factions/restoration-council\" class=\"wiki-link\">Restoration Council</a></td>\n      <td>Decimated population; crippled republican leaders via assassination; cemented Council control.</td>\n    </tr>\n    <tr>\n      <td><strong><a href=\"#history/period-viii\" class=\"wiki-link\">VIII: Besieged Kingdom</a></strong></td>\n      <td>Installation of PC Triumvirate by puppetmasters; growth of The Pit; multi-front threats.</td>\n      <td>The Triumvirate (PCs), <a href=\"#npcs/valenza\" class=\"wiki-link\">Valenza</a>, <a href=\"#npcs/sadoria\" class=\"wiki-link\">Mateo</a></td>\n      <td>Modern campaign setting: bankrupt, besieged realm ruled by young rulers surrounded by wolves.</td>\n    </tr>\n  </tbody>\n</table>\n</div>\n",
    "gmSecrets": "Notice how every period ended in betrayal or cataclysm\u2014the cycle the Triumvirate must break.",
    "relatedIds": [
      "period-i",
      "period-viii",
      "campaign-premise"
    ]
  },
  {
    "id": "pundonor",
    "category": "rules",
    "title": "Dueling Culture & Pundonor Rules",
    "subtitle": "Aristocratic Honor System, Duels, Penalties, & Swashbuckling Flair",
    "tags": [
      "Rules",
      "Pundonor",
      "Combat",
      "Social",
      "Dueling"
    ],
    "aliases": [
      "Pundonor",
      "Dueling Rules",
      "Honor Rules",
      "Pundonor System"
    ],
    "summary": "The touchy Zingaran code of honor. Yielding or refusing a duel inflicts a persistent -2 social penalty until cleansed by victory in formal combat.",
    "content": "\n<h3>6.2 Dueling Culture & Pundonor Rules</h3>\n<p>Swordsmanship is Zingara's preeminent art form. Zingarans reject brute-force hacking weapons in favor of slender cut-and-thrust rapiers and main-gauche parrying daggers. Master swordsmen operate prestigious fencing academies (esgrimas) throughout Kordava. Social slights, territorial squabbles, or romantic rivalries are settled through formal duels at dawn or fatal back-alley encounters.</p>\n\n<div class=\"rule-box\">\n  <div class=\"rule-header\">MECHANICAL RULE: PUNDONOR (HONOR)</div>\n  <p><strong>Trigger:</strong> A character yields, flees, or refuses a legitimate duel of honor when challenged by a social peer or noble in public.</p>\n  <p><strong>Mechanical Effect:</strong> The character suffers a persistent <strong>-2 penalty</strong> to all Social, Persuasion, and Command checks when interacting with Zingaran nobility, military officers, or high-class merchants.</p>\n  <p><strong>Cleansing the Stain:</strong> The penalty remains active until the character's honor is cleansed by defeating a social peer in a formal duel or completing an extraordinary feat of public bravery.</p>\n</div>\n\n<h3>NPC Honor-Baiting Tactics (GM Roleplay Guidance)</h3>\n<p>Rival Grandees and fencing masters exploit pundonor as a political weapon against the PC Triumvirate. An NPC will deliberately issue mild public insults\u2014questioning a PC's martial skill, royal legitimacy, or courage\u2014in front of assembled court nobles. This forces the PC into a dilemma:</p>\n<ul>\n  <li>Accept an illegal or potentially fatal duel on the NPC's home turf.</li>\n  <li>Refuse and suffer the persistent -2 Pundonor penalty to all subsequent royal governance and persuasion attempts.</li>\n</ul>\n\n<div class=\"info-card\">\n  <h4>GM Advice for Swashbuckling Combat Flair</h4>\n  <p>Reward players who incorporate the environment into martial encounters. Grant a <strong>+2 situational bonus</strong> to attack rolls or Armor Class whenever a player executes swashbuckling maneuvers, such as:</p>\n  <ul>\n    <li>Swinging from wrought-iron chandeliers or balconies.</li>\n    <li>Wrapping a velvet cloak around an off-hand arm to parry a blade.</li>\n    <li>Vaulting over wine casks or tavern tables during fencing duels.</li>\n    <li>Kicking sand or wine into an opponent's eyes before a lunge.</li>\n  </ul>\n</div>\n",
    "gmSecrets": "Use Duke Gonzalo de Guarralid as the primary NPC to test players with honor-baiting early in the campaign.",
    "relatedIds": [
      "gonzalo-guarralid",
      "command-friction",
      "social-hierarchy"
    ]
  },
  {
    "id": "command-friction",
    "category": "rules",
    "title": "Military Doctrines & Command Friction",
    "subtitle": "Tactical Arms, Aristocratic Insubordination, & Royal Edicts",
    "tags": [
      "Rules",
      "Warfare",
      "Tactics",
      "Command",
      "Military"
    ],
    "aliases": [
      "Command Friction",
      "Military Doctrines",
      "Warfare Rules"
    ],
    "summary": "Four tactical arms of Zingara and the Command Friction mechanic: noble commanders routinely refuse orders from rivals without a DC 14 check.",
    "content": "\n<h3>5.2 Military Doctrines & Tactical Arms</h3>\n<p>Zingaran military strategy relies on four distinct tactical arms:</p>\n<ul>\n  <li><strong>Heavy Cavalry (Caballeros):</strong> Armored noble lancers mounted on barded warhorses. Recruited from the noble caste, they form the elite striking arm of Grandee armies, devastating in open-field shock charges.</li>\n  <li><strong>Pike Blocks &amp; Arbalesters:</strong> Disciplined municipal defensive squares composed of peasant levies and city guards armed with long pikes, supported by heavy crossbowmen (arbalesters) capable of punching through knightly armor.</li>\n  <li><strong>Fencing Skirmishers:</strong> Light infantry specialized in urban skirmishing, boarding actions, and rough terrain. Armed with rapiers, bucklers, and throwing blades, they excel at maneuverability and harassment.</li>\n  <li><strong>The Royal Fleet &amp; Privateers:</strong> War galleys and swift caravels equipped for close-quarters naval action, featuring ramming prows, archer platforms, and boarding raiders.</li>\n</ul>\n\n<div class=\"rule-box\">\n  <div class=\"rule-header\">COMMAND FRICTION MECHANICS</div>\n  <p><strong>The Core Military Flaw:</strong> The fundamental vulnerability of any Zingaran military force is command friction caused by aristocratic hubris, feudal bloodlines, and sensitive personal honor (pundonor).</p>\n  <p><strong>Operational Execution:</strong> Because military appointments are tied to social rank rather than competence, high-born Grandees routinely refuse to take orders from social rivals or low-born officers.</p>\n  <p><strong>Check Mechanics:</strong> In mass tactical engagements, when an order is issued to a subordinate noble unit, the commander must make a <strong>DC 14 Command Check</strong> utilizing Warfare, Leadership, or Persuasion. On a failure, the subordinate noble considers the order an insult to their personal honor, resulting in an uncoordinated charge, refusal of reinforcement, or complete battlefield withdrawal.</p>\n  <p><strong>Player Mitigation Options:</strong> Player Characters acting as the Triumvirate can bypass or reduce this Command Friction through direct royal intervention:</p>\n  <ul>\n    <li><em>Expend a Royal Edict:</em> Expending a formal Crown Decree automatically succeeds on the check, though it increases Council suspicion.</li>\n    <li><em>Issue a Direct Duel Challenge:</em> A PC can publicly challenge an insubordinate Grandee to an immediate duel of honor; if accepted or conceded, the DC is reduced to <strong>DC 8</strong> for the remainder of the battle.</li>\n  </ul>\n</div>\n",
    "gmSecrets": "When players lead army units, use command friction to make large-scale battles tense and character-driven.",
    "relatedIds": [
      "pundonor",
      "military-elite",
      "guarralid"
    ]
  },
  {
    "id": "social-hierarchy",
    "category": "rules",
    "title": "Ethnic Genesis & Social Hierarchy",
    "subtitle": "The Four Strata: Grandees, Caballeros, Chulos, and Thralls",
    "tags": [
      "Culture",
      "Society",
      "Classes",
      "Lore"
    ],
    "aliases": [
      "Social Hierarchy",
      "Ethnic Genesis",
      "Social Strata",
      "Zingaran Society"
    ],
    "summary": "Synthesis of Shemite, Pictish, and Hyborian bloodlines forming four rigid classes: Grandees, Caballeros, Chulos & Commoners, and Undead Thralls.",
    "content": "\n<h3>6.1 Ethnic Genesis & Social Hierarchy</h3>\n<p>Zingaran society arose from three distinct historical waves: peaceful Shemitish agriculturalists of the Zingg Valley merged first with primitive conquering Pictish tribes, and later with invading Hyborian warriors. This fusion created a proud, dark-complexioned, slender people who combined Hyborian martial traditions, Shemitish agricultural roots, and tempestuous Pictish blood.</p>\n\n<div class=\"info-card\">\n<h4>The Four Rigid Social Strata</h4>\n<ol>\n  <li><strong>Grandees (Grandes):</strong> The hereditary high nobility (dukes, counts, high barons). They govern vast fiefdoms as near-sovereign lords, maintain private armies, mint provincial coin, and obey the crown only when compelled by military force.</li>\n  <li><strong>Caballeros &amp; Hidalgos:</strong> The lesser nobility, knights, and landed gentry. Serving primarily as heavy cavalry, retainers to Grandees, or fencing masters, they are obsessed with military reputation and genealogical purity.</li>\n  <li><strong>Chulos &amp; Commoners:</strong> Urban artisans, shopkeepers, maritime laborers, and manorial peasants. While peasants are bound to rural soil under manorial burdens, urban commoners possess a fiery, rebellious spirit and vibrant pub culture.</li>\n  <li><strong>Undead Thralls:</strong> The lowest underclass. Memory-retaining zombies used for brutal, toxic labor in the mining pits. Stripped of all mortal rights, yet horrifyingly conscious of their former lives.</li>\n</ol>\n</div>\n",
    "gmSecrets": "The tension between Caballeros (who aspire to be Grandees) and Commoners (who lean republican) is ripe for player recruitment.",
    "relatedIds": [
      "pundonor",
      "necromancy-mechanics",
      "campaign-premise"
    ]
  },
  {
    "id": "necromancy-mechanics",
    "category": "relics",
    "title": "Memory-Retaining Undead Mechanics",
    "subtitle": "The Horrific Psychology and Exploitation of Zingaran Thralls",
    "tags": [
      "Arcana",
      "Undead",
      "Necromancy",
      "Mechanics",
      "Horror"
    ],
    "aliases": [
      "Memory-Retaining Undead",
      "Thrall Mechanics",
      "Necromancy Mechanics",
      "Undead Rules"
    ],
    "summary": "Zingaran zombies retain their living memories and personalities while trapped in complete physical servitude to their masters.",
    "content": "\n<h3>7.1 Necromantic Mechanics & Industrial Exploitation</h3>\n<p>Unlike mindless skeletons found in other fantasy settings, zombies created through Zingaran necromancy retain their pre-death human memories, intellect, and personalities, while remaining totally enthralled to their master's magical commands or controlling artifacts. This creates three core operational dilemmas at the table:</p>\n\n<div class=\"rule-box\">\n  <div class=\"rule-header\">THREE OPERATIONAL THRALL DILEMMAS</div>\n  <ol>\n    <li><strong>The Reanimated Acquaintance:</strong> PCs encounter fallen allies, family members, or historical figures who recognize them, speaking with tragic clarity and experiencing conscious horror at their own servitude while forced to attack.</li>\n    <li><strong>Tactical Intelligence Exploitation:</strong> Capturing and interrogating an enthralled thrall allows characters to extract vital historical memories, secret passage locations, or security passwords known by the individual in life (<strong>DC 14 Interrogation/Persuasion Check</strong>).</li>\n    <li><strong>Moral Sabotage:</strong> PCs can manipulate a thrall's deep personal memories or unfulfilled life vows to create momentary cognitive dissonance. A successful <strong>DC 16 Persuasion Check</strong> temporarily paralyzes a thrall for <strong>1d4 rounds</strong> as its living mind fights the binding magic.</li>\n  </ol>\n</div>\n",
    "gmSecrets": "Have an NPC the players cared about in their backstory appear as a reanimated thrall in Master Vane's laboratory.",
    "relatedIds": [
      "industrial-pits",
      "vane",
      "edmund",
      "obsidian-blade"
    ]
  },
  {
    "id": "industrial-pits",
    "category": "relics",
    "title": "Industrial Zombie Pits & Blueprint Layout",
    "subtitle": "Mass Thrall Labor Infrastructure, Toxic Vats, & Hazard Rules",
    "tags": [
      "Arcana",
      "Dungeon",
      "Zombie Pits",
      "Hazards"
    ],
    "aliases": [
      "Industrial Zombie Pits",
      "Zombie Pits",
      "The Pits",
      "Edmund's Pits"
    ],
    "summary": "Modular blueprints and environmental hazards for the reeking chemical extraction pits engineered by Edmund across Zingara.",
    "content": "\n<h3>Industrial Zombie Pits Architecture &amp; Mechanics</h3>\n<p>Engineered during Period IV by Edmund the Necromancer, these industrial complexes are dug into subterranean caverns and open quarries to extract valuable ores and toxic minerals using disposable, tireless undead labor.</p>\n\n<div class=\"info-card\">\n<h4>Modular Pit Blueprint Layout</h4>\n<ul>\n  <li><strong>1. Excavation Pit &amp; Mine Shafts:</strong> Deep, unventilated subterranean shafts where thralls chisel raw ore in total darkness. Prone to cave-ins and gas pockets.</li>\n  <li><strong>2. Chemical Preservation Vats:</strong> Massive stone cisterns filled with acidic embalming slurry and sulfurous resins used to pickle thrall flesh and prevent rot.</li>\n  <li><strong>3. The Processing Floor:</strong> Sorting belts and crushing mills where thralls crush rock with bare hands and iron hammers. High risk of mechanical accidents.</li>\n  <li><strong>4. The Overseer's Iron Cage:</strong> A fortified, suspended metal redoubt overlooking the pit where mortal alchemists and guards issue commands using control amulets.</li>\n</ul>\n</div>\n\n<div class=\"rule-box\">\n  <div class=\"rule-header\">PIT ENVIRONMENTAL HAZARDS</div>\n  <ul>\n    <li><strong>Toxic Alchemical Slurry:</strong> Falling into a preservation pool deals <strong>2d6 acid damage</strong> per round and forces a <strong>DC 13 Fortitude/Constitution Save</strong> against toxic fumes.</li>\n    <li><strong>Fume Inhalation:</strong> Characters in the pit must save every 10 minutes or suffer cumulative -1 penalties to physical checks.</li>\n    <li><strong>Thrall Frenzy / Meltdown:</strong> If the alchemical Overseer Amulet is destroyed, all thralls in the chamber fly into an uncoordinated frenzy, attacking the nearest living creatures.</li>\n  </ul>\n</div>\n",
    "gmSecrets": "The pit near Jerida contains an unmapped secret tunnel connecting directly to the crypt of the Black Blade of Azur.",
    "relatedIds": [
      "necromancy-mechanics",
      "vane",
      "edmund",
      "black-blade"
    ]
  },
  {
    "id": "black-blade",
    "category": "relics",
    "title": "The Black Blade of Azur",
    "subtitle": "Pre-Deluvial Anti-Sorcery Relic",
    "origin": "Forged in Period I by an ancient sorcerer in the Zingg Valley; buried underground after the sorcerer's execution.",
    "powers": "Pure negation of all arcane and necromantic energies; severs magical bindings on contact; instantly unbinds undead thralls.",
    "status": "Lost in the subterranean abyss beneath the ruins of the old magical academy, far below The Pit in Kordava.",
    "tags": [
      "Relic",
      "Artifact",
      "Anti-Magic",
      "Weapon"
    ],
    "aliases": [
      "Black Blade of Azur",
      "Black Blade",
      "Blade of Azur"
    ],
    "summary": "Legendary anti-sorcery weapon forged in Period I. Capable of instantly severing necromantic control and nullifying magical wards.",
    "content": "\n<h3>The Black Blade of Azur</h3>\n<div class=\"info-card\">\n  <p><strong>Historical Origin:</strong> Forged in Period I by an ancient sorcerer in the Zingg Valley; buried underground following the sorcerer's execution to prevent catastrophic misuse.</p>\n  <p><strong>Current Status:</strong> Lost in the subterranean abyss beneath the ruins of the old magical academy, far below The Pit in Kordava.</p>\n</div>\n\n<h3>Eldritch Properties &amp; Powers</h3>\n<p>The Black Blade is forged from an unreflective, light-devouring matte black alloy. It possesses absolute anti-magic properties:</p>\n<ul>\n  <li><strong>Arcane Nullification:</strong> Radiates a constant 10-foot aura of magical suppression, dispelling spells and magical wards on contact.</li>\n  <li><strong>Thrall Severance:</strong> Striking a necromantic thrall with the blade immediately severs its binding runes, granting the soul permanent release into death without reanimation.</li>\n  <li><strong>Sovereign Defense:</strong> In the hands of the Triumvirate, the blade would completely neutralize the Restoration Council's secret sorcerous countermeasures.</li>\n</ul>\n",
    "gmSecrets": "Master Alchemist Vane is desperately trying to locate this blade to destroy it before it can be used against his thralls.",
    "relatedIds": [
      "obsidian-blade",
      "the-pit",
      "vane",
      "period-i"
    ]
  },
  {
    "id": "obsidian-blade",
    "category": "relics",
    "title": "The Obsidian Blade",
    "subtitle": "Eldritch Mass-Binding Conduit of Mad King Daedalus",
    "origin": "Uncovered by Mad King Daedalus in Period V to channel the blood of foreign envoys into his ritual cauldron.",
    "powers": "Massive necromantic conduit; allows the wielder to instantly bind, command, or exhume vast armies of undead thralls.",
    "status": "Buried deep within the smoldering rubble of old Kordava beneath The Pit, where Daedalus lies eternally trapped.",
    "tags": [
      "Relic",
      "Artifact",
      "Necromancy",
      "Weapon",
      "Horror"
    ],
    "aliases": [
      "The Obsidian Blade",
      "Obsidian Blade"
    ],
    "summary": "Terrifying necromantic conduit uncovered by Mad King Daedalus. Grants supreme command over undead hordes, buried with Daedalus beneath The Pit.",
    "content": "\n<h3>The Obsidian Blade</h3>\n<div class=\"info-card\">\n  <p><strong>Historical Origin:</strong> Uncovered by Mad King Daedalus in Period V to channel the sacrificial blood of citizens and envoys into his cauldron for godhood.</p>\n  <p><strong>Current Status:</strong> Buried deep within the smoldering rubble of old Kordava beneath The Pit, where King Daedalus lies eternally trapped by Tanatos.</p>\n</div>\n\n<h3>Eldritch Properties &amp; Powers</h3>\n<ul>\n  <li><strong>Horde Command:</strong> The wielder can mentally command hundreds of memory-retaining thralls simultaneously over miles without verbal orders.</li>\n  <li><strong>Mass Exhumation:</strong> Plunging the blade into unhallowed ground automatically animates fallen corpses within a 300-foot radius.</li>\n  <li><strong>The Cosmic Curse:</strong> The blade constantly whispers with the voices of Daedalus and the victims of the Starfall. Wielding it requires a DC 16 Wisdom/Sanity check every dawn or suffer paranoid megalomania.</li>\n</ul>\n",
    "gmSecrets": "If the blade is removed from Daedalus's grasp, it will break Tanatos's imprisonment spell, awakening the Mad King.",
    "relatedIds": [
      "daedalus",
      "black-blade",
      "the-pit",
      "tanatos"
    ]
  },
  {
    "id": "fountain-of-youth",
    "category": "relics",
    "title": "The Fountain of Youth",
    "subtitle": "Sacred Waters of Miraculous Longevity & Purification",
    "origin": "Discovered by Priest Falmouth in Period VI during the early Church of Nemeth era.",
    "powers": "Grants physical longevity, cures any mortal disease or poison, and completely reverses necromantic corruption.",
    "status": "Hidden within an abandoned, sealed mountain shrine in the Rabirian borderlands following the church's downfall.",
    "tags": [
      "Relic",
      "Healing",
      "Church of Nemeth",
      "Rabirian"
    ],
    "aliases": [
      "The Fountain of Youth",
      "Fountain of Youth",
      "Waters of the Shrine"
    ],
    "summary": "Miraculous sacred spring discovered in Period VI in the Rabirian Mountains. Cures all poisons, reverses decay, and grants centuries of life.",
    "content": "\n<h3>The Fountain of Youth</h3>\n<div class=\"info-card\">\n  <p><strong>Historical Origin:</strong> Discovered by High Priest Falmouth in Period VI in the Rabirian Mountains, securing divine prestige for the Church of Nemeth.</p>\n  <p><strong>Current Status:</strong> Concealed inside a sealed, trapped mountain shrine in the Rabirian borderlands, disputed by Argossean mercenaries and Gnostic cultists.</p>\n</div>\n\n<h3>Miraculous Powers</h3>\n<ul>\n  <li><strong>Absolute Healing:</strong> Drinking the waters immediately cures any mortal poison, disease, or magical wasting sickness.</li>\n  <li><strong>Necromantic Reversal:</strong> Reverses physical decay in living creatures touched by necromancy, and can purify blighted land.</li>\n  <li><strong>Longevity:</strong> Grants centuries of unaging vigor, making it the ultimate prize for aging Grandees and foreign kings.</li>\n</ul>\n",
    "gmSecrets": "Marquis Mateo used a slow wasting poison on a PC relative specifically to force the PCs to seek out this fountain.",
    "relatedIds": [
      "malachai",
      "falmouth",
      "rabirian-mountains",
      "church-of-nemeth"
    ]
  },
  {
    "id": "final-guard",
    "category": "relics",
    "title": "The Final Guard of King Kalenius",
    "subtitle": "One Thousand Pre-Cataclysmic Thurian Stone Warriors",
    "origin": "Ancient Thurian epoch; interred with King Kalenius beneath Kordava's harbor.",
    "powers": "Deathless animate stone guardians immune to pain, poison, mental influence, and normal weapon damage.",
    "status": "Asleep in the submerged mausoleum beneath The Pit, awaiting the true heir or the proper ritual invocation.",
    "tags": [
      "Relic",
      "Guardians",
      "Ancient",
      "Thurian",
      "Military"
    ],
    "aliases": [
      "The Final Guard",
      "Final Guard",
      "Stone Guardians",
      "Kalenius Guard"
    ],
    "summary": "One thousand deathless stone warriors guarding King Kalenius's tomb. If commanded, they would provide an unstoppable royal army.",
    "content": "\n<h3>The Final Guard of King Kalenius</h3>\n<p>Dating back to the pre-Cataclysmic Thurian epoch (recorded in the chronicles of Karl Edward Wagner), the Final Guard was King Kalenius's elite royal bodyguard. Through ancient rites, one thousand warriors were petrified into living, animate stone to guard their king's rest for eternity.</p>\n\n<div class=\"info-card\">\n<h4>Combat &amp; Mechanical Attributes</h4>\n<ul>\n  <li><strong>Animate Stone Physiology:</strong> Immune to poison, bleed, mental influence, and necromantic corruption. Resistant to slashing and piercing damage.</li>\n  <li><strong>Thurian Masterwork Armament:</strong> Equipped with star-metal broadswords and tower shields that ignore standard magical armor.</li>\n  <li><strong>The True Command:</strong> If the PC Triumvirate can secure the Royal Signet of Kalenius from his sarcophagus, they could awaken the Final Guard to serve as their personal, incorruptible household army.</li>\n</ul>\n</div>\n",
    "gmSecrets": "Vesper knows the entrance to this tomb and will trade it for a royal pardon for his entire criminal syndicate.",
    "relatedIds": [
      "mausoleum-kalenius",
      "vesper",
      "the-pit"
    ]
  },
  {
    "id": "hook-blood-in-cauldron",
    "category": "hooks",
    "title": "Blood in the Cauldron",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: The Triumvirate, Restoration Council, Kingdom of Argos, The Pit Underworld",
    "tags": [
      "Hook",
      "Diplomacy",
      "Argos",
      "The Pit",
      "Obsidian Blade"
    ],
    "aliases": [
      "Blood in the Cauldron"
    ],
    "summary": "Argos threatens naval blockade unless the signet ring of an ambassador murdered in Period V is returned from an earthquake-exposed crypt beneath Korda...",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> The Triumvirate, Restoration Council, Kingdom of Argos, The Pit Underworld</p>\n  <p><strong>Strategic Reward:</strong> Prevents naval blockade of Kordava; secures diplomatic reprieve with Argos; potential access to the Obsidian Blade.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>Argos threatens naval blockade unless the signet ring of an ambassador murdered in Period V is returned from an earthquake-exposed crypt beneath Kordava. The Council forbids intervention, hoping to humiliate the crown.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>In the crypt, the PCs discover the ambassador is now a conscious, memory-retaining thrall guarding the Obsidian Blade. The rulers must choose whether to destroy him and return the ring, free him via ritual, or claim the blade.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 15 History/Arcana (identify unbinding runes); DC 17 Persuasion (appeal to living memories to secure ring peacefully).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> If PCs take more than 3 rounds, a Council strike team enters to seize relics and eliminate witnesses.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-insurgents-bargain",
    "category": "hooks",
    "title": "The Insurgent's Bargain",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: The Triumvirate, Republican Insurgents, Restoration Council, Church of Nemeth",
    "tags": [
      "Hook",
      "Intrigue",
      "Puppetmasters",
      "Republicans",
      "Blackmail"
    ],
    "aliases": [
      "The Insurgent's Bargain"
    ],
    "summary": "Republican insurgents contact the PCs during a royal gala with written proof that General Valenza and Marquis Mateo assassinated the republican founde...",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> The Triumvirate, Republican Insurgents, Restoration Council, Church of Nemeth</p>\n  <p><strong>Strategic Reward:</strong> Absolute blackmail evidence against General Valenza and Marquis Mateo, enabling a crown purge of the puppetmasters.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>Republican insurgents contact the PCs during a royal gala with written proof that General Valenza and Marquis Mateo assassinated the republican founder in Period VI and framed the Church.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>Republicans want pardons; Church zealots intercept demanding the evidence to clear their name; Council assassins lurk. Who do the PCs align with or betray?</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 16 Stealth/Deception (slip away from royal handlers at gala); DC 14 Insight (detect double-dealing zealots).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Hesitation causes royal army assassins to strike, attempting to burn documents and silence all informants.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-pits-of-edmund",
    "category": "hooks",
    "title": "The Reeking Pits of Edmund",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: The Triumvirate, Restoration Council, Grandee Coalitions, Master Alchemist Vane",
    "tags": [
      "Hook",
      "Necromancy",
      "Jerida",
      "Zombie Pits",
      "Black Blade"
    ],
    "aliases": [
      "The Reeking Pits of Edmund"
    ],
    "summary": "Pit #4 near Jerida collapses, releasing hundreds of memory-retaining thralls who seize a vital iron mine. The Council cuts royal household stipends in...",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> The Triumvirate, Restoration Council, Grandee Coalitions, Master Alchemist Vane</p>\n  <p><strong>Strategic Reward:</strong> Restores royal iron production and yields a secret map to the Black Blade of Azur crypt.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>Pit #4 near Jerida collapses, releasing hundreds of memory-retaining thralls who seize a vital iron mine. The Council cuts royal household stipends in retaliation.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>Inside the mine, a reanimated Period IV scholar offers a secret passage into the crypt of the Black Blade of Azur if the PCs help the thralls escape to the Pictish Wilderness.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 14 Athletics/Survival (navigate toxic pit slurry); DC 16 Warfare/Tactics (organize stealth escape route through Grandee lines).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Toxic alchemical fumes force DC 13 Fortitude Save every 10 min; failure deals cumulative -1 penalties.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-fallen-shrine",
    "category": "hooks",
    "title": "Waters of the Fallen Shrine",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: The Triumvirate, Restoration Council, Church of Nemeth, Kingdom of Argos",
    "tags": [
      "Hook",
      "Rabirian",
      "Fountain of Youth",
      "Church of Nemeth",
      "Healing"
    ],
    "aliases": [
      "Waters of the Fallen Shrine"
    ],
    "summary": "A loyal royal relative is struck by a slow wasting poison secretly administered by Marquis Mateo. To find the cure, the PCs must locate the lost Fount...",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> The Triumvirate, Restoration Council, Church of Nemeth, Kingdom of Argos</p>\n  <p><strong>Strategic Reward:</strong> Waters of the Fountain of Youth, providing an absolute cure for poisons and necromantic decay.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>A loyal royal relative is struck by a slow wasting poison secretly administered by Marquis Mateo. To find the cure, the PCs must locate the lost Fountain of Youth in the Rabirian Mountains.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>At the shrine, Gnostic zealots guard the waters while Argossean mercenaries assault the gates. PCs must negotiate, fight, or steal the waters.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 15 Perception (spot Argossean mountain scouts); DC 17 Religion (quote scripture to secure Gnostic sanctuary).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> On round 4 of combat inside the shrine, the cavern ceiling collapses, destroying the primary pool forever.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-concealed-order",
    "category": "hooks",
    "title": "The Concealed Execution Order",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: Military Elite, Republican Insurgents, The Triumvirate",
    "tags": [
      "Hook",
      "Valenza",
      "Military",
      "Zingg Valley",
      "Investigation"
    ],
    "aliases": [
      "The Concealed Execution Order"
    ],
    "summary": "General Valenza asks the PCs to rubber-stamp an execution order against a 'rebel camp' in the Zingg Valley\u2014actually surviving witnesses to his Period ...",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> Military Elite, Republican Insurgents, The Triumvirate</p>\n  <p><strong>Strategic Reward:</strong> Saves key witnesses to Period VI state crimes, earning the secret allegiance of urban republican cells.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>General Valenza asks the PCs to rubber-stamp an execution order against a 'rebel camp' in the Zingg Valley\u2014actually surviving witnesses to his Period VI assassination.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>Sign the order to keep Valenza's favor, or delay and investigate to save witnesses and gain republican allies.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 15 Investigation/Insight (uncover identity of target camp); DC 16 Command/Persuasion (countermand military orders).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Delaying more than 24 hours causes Valenza to execute the order with his private guard and place the PCs on lockdown.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-treasury-lockout",
    "category": "hooks",
    "title": "The Treasury Lockout",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: Restoration Council, The Triumvirate, Marquis Mateo",
    "tags": [
      "Hook",
      "Sadoria",
      "Treasury",
      "Intrigue",
      "Economy"
    ],
    "aliases": [
      "The Treasury Lockout"
    ],
    "summary": "Marquis Mateo refuses to fund the PCs' personal guard, claiming the treasury is dry due to foreign debts....",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> Restoration Council, The Triumvirate, Marquis Mateo</p>\n  <p><strong>Strategic Reward:</strong> Exposes Council embezzlement and forces release of crown funds for an independent royal guard.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>Marquis Mateo refuses to fund the PCs' personal guard, claiming the treasury is dry due to foreign debts.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>Audit Mateo's ledgers to prove embezzlement, raid an underworld den in The Pit, or borrow from foreign merchants.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 16 Investigation (audit treasury scrolls to detect missing gold); DC 17 Persuasion/Intimidation (confront Mateo).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Confronting without unassailable proof causes Mateo to slash palace servant and food budgets.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-tax-revolt-jerida",
    "category": "hooks",
    "title": "The Tax Revolt of Jerida",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: Grandee Coalitions, Restoration Council, Barachan Pirates",
    "tags": [
      "Hook",
      "Jerida",
      "Guarralid",
      "Grandees",
      "Economy"
    ],
    "aliases": [
      "The Tax Revolt of Jerida"
    ],
    "summary": "Duke Gonzalo's garrison in Jerida seizes royal barges on the Thunder River, declaring an embargo until tariffs are cut....",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> Grandee Coalitions, Restoration Council, Barachan Pirates</p>\n  <p><strong>Strategic Reward:</strong> Re-establishes crown trade tariffs on the Thunder River, generating independent royal revenue.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>Duke Gonzalo's garrison in Jerida seizes royal barges on the Thunder River, declaring an embargo until tariffs are cut.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>Break the standoff through military intimidation, clever trade compromise, or covert sabotage of supply lines.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 15 Intimidation/Persuasion (force river inspectors to yield); DC 14 Navigation/Sailing (outmaneuver river blockade).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Failure to resolve within 3 days triggers an armed clash between royal troops and Grandee retainers.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-tomb-kalenius",
    "category": "hooks",
    "title": "The Tomb of King Kalenius",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: Vesper the Key-Master, Grandee Coalitions, The Triumvirate",
    "tags": [
      "Hook",
      "The Pit",
      "Dungeon",
      "Relic",
      "Final Guard"
    ],
    "aliases": [
      "The Tomb of King Kalenius"
    ],
    "summary": "Vesper offers a map through flooded tunnels into the pre-Cataclysmic crypt of King Kalenius beneath Kordava harbor....",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> Vesper the Key-Master, Grandee Coalitions, The Triumvirate</p>\n  <p><strong>Strategic Reward:</strong> Secures Thurian masterwork armor and weapons; potential activation of the 1,000 stone warriors.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>Vesper offers a map through flooded tunnels into the pre-Cataclysmic crypt of King Kalenius beneath Kordava harbor.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>Navigate flooded abyssal tunnels and aquatic ghouls to claim star-metal weapons and the dormant Final Guard.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 16 Athletics/Endurance (underwater tunnel navigation); DC 17 Warfare/Tactics (survive stone guardian encounter).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Disturbing the tomb without proper ritual keys awakens six stone guardians in a violent fury.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  },
  {
    "id": "hook-treasury-heist",
    "category": "hooks",
    "title": "The Treasury Heist",
    "subtitle": "Sandbox Ruler Hook &bull; Factions: Restoration Council, Vesper the Key-Master, The Triumvirate",
    "tags": [
      "Hook",
      "Heist",
      "Vesper",
      "The Pit",
      "Gold"
    ],
    "aliases": [
      "The Treasury Heist"
    ],
    "summary": "The PCs partner with Vesper to break into the Restoration Council's secret subterranean vaults beneath Kordava....",
    "content": "\n<div class=\"info-card\">\n  <p><strong>Involved Factions:</strong> Restoration Council, Vesper the Key-Master, The Triumvirate</p>\n  <p><strong>Strategic Reward:</strong> Reclaims millions in hoarded state gold, allowing direct payment of the Kordava city watch for absolute loyalty.</p>\n</div>\n\n<h3>Narrative Premise</h3>\n<p>The PCs partner with Vesper to break into the Restoration Council's secret subterranean vaults beneath Kordava.</p>\n\n<h3>Core Conflict &amp; Player Choice</h3>\n<p>Bypass pre-Cataclysmic mechanical wards, avoid Council patrols, and extract hoarded bullion.</p>\n\n<div class=\"dc-box\">\n  <strong>Suggested Skill Checks:</strong> DC 16 Thievery/Stealth (bypass vault traps); DC 15 Arcana (disarm pre-Cataclysmic mechanical wards).\n</div>\n\n<p class=\"escalation\"><strong>Dynamic Escalation Trigger:</strong> Triggering alarms floods the vault with toxic alchemical mist and locks all egress gates.</p>\n",
    "gmSecrets": "Resolution of this hook permanently shifts the Crown Sovereignty clock by +1 or -1.",
    "relatedIds": [
      "court-matrix",
      "campaign-premise",
      "valenza",
      "sadoria",
      "lucia",
      "vesper"
    ]
  }
]
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = WIKI_DATA;
}
