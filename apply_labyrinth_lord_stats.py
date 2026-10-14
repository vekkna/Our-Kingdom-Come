"""
apply_labyrinth_lord_stats.py
Updates the Zingara Compendium with comprehensive Labyrinth Lord (B/X D&D retro-clone)
classes, levels, and statistics for all city NPCs, ensuring they are mechanically powerful
relative to the Level 8-9 PC Triumvirate (Warrior Lvl 9, Cleric Lvl 9, Mage Lvl 8 at 240,000 XP).
"""

import json
import re

# Comprehensive Labyrinth Lord Statistics for all 8 Kordava City NPCs
LL_NPCS = {
    "valenza": {
        "classLevel": "13th-Level Fighter (Warlord)",
        "combatStats": "AC -2 (AAC 21) | HP 78 | THAC0 10 | Atk +15 (1d8+6) | Saves: 7/6/7/8/8",
        "alignment": "Neutral (Cold martial pragmatism, ruthless state order)",
        "station": "Head of the Royal Army & Co-Architect of the Restoration",
        "ac": "AC -2 (AAC 21)",
        "acBreakdown": "Gilded Plate Mail +2, Large Steel Shield +1, DEX 14 (-1)",
        "hd": "9d8+8 (+18 CON bonus on first 9 HD)",
        "hp": 78,
        "move": "60' (20') in field plate / Mounted 120' (40')",
        "thaco": "10 (Base Attack Bonus +9)",
        "attacks": "Melee: +15 to hit (The Iron Edict +3 longsword, 1d8+6 slashing); 2 attacks/round vs creatures under 1 HD, 1 attack/round with devastating cleave against heroes",
        "abilities": [
            ("STR", 18, "+3 to hit, +3 damage, Open Doors 1-5 on 1d6"),
            ("DEX", 14, "+1 missile to hit, -1 AC bonus"),
            ("CON", 17, "+2 HP per Hit Die up to 9th level"),
            ("INT", 15, "+1 language, grand tactical strategy"),
            ("WIS", 13, "+1 on saving throws vs. magical spells"),
            ("CHA", 16, "+1 reaction, 6 retainers, morale 9")
        ],
        "saves": [
            ("Breath Weapon (BW)", 7),
            ("Poison or Death (P/D)", 6),
            ("Petrify or Paralyze (PP)", 7),
            ("Wands (W)", 8),
            ("Spells (S)", 8)  # Base 9 - 1 for WIS 13
        ],
        "magicItems": [
            "The Iron Edict (+3 Zingaran Longsword; sheds light in 30' radius on command; deals double damage [2d8+12] vs undead and republican insurgents)",
            "Gilded Plate Mail +2 (Mirror-polished steel plate)",
            "Large Steel Shield +1 (Emblazoned with the golden lion of Ancillus I)",
            "Ring of Free Action (Immune to Hold Person, paralysis, webs, and magical entanglement)",
            "Potions of Extra-Healing (x2 vials, each restores 3d6+3 HP)"
        ],
        "tactics": "<strong>Veteran Parry:</strong> Once per combat round, Rodrigo can sacrifice his attack to parry, imposing a -4 penalty on all incoming melee attacks against him until the next round.<br><strong>Command of the Host:</strong> All royal army guards within 60' receive a +2 bonus to Morale checks and +1 to hit as long as Don Rodrigo remains standing on the battlefield.",
        "pcComparison": "Compared to the Level 8–9 PC Triumvirate, Don Rodrigo substantially out-tanks and out-hits the PC Warrior (78 HP vs ~50 HP; AC -2 vs ~AC 2; attack +15 vs +6). A direct frontal martial assault against Rodrigo in Kordava is almost certain suicide without isolating him from his garrison, turning the army's loyalties, or finding an artifact like the <em>Black Blade of Kalenius</em>."
    },
    "sadoria": {
        "classLevel": "12th-Level Thief (Shadow Master & Master Assassin)",
        "combatStats": "AC 1 (AAC 18) | HP 48 | THAC0 14 | Atk +7 (1d4+2 + Venom) | Backstab x4 | Saves: 8/5/4/6/6",
        "alignment": "Chaotic (Cynical manipulator, embezzlement, ruthless survival)",
        "station": "High Chancellor of Zingara & Chief Monarchist Handler",
        "ac": "AC 1 (AAC 18)",
        "acBreakdown": "Concealed Elven Silk Doublet (Leather +2), Ring of Protection +2, DEX 17 (-2), Cloak of Displacement",
        "hd": "9d4+6 (+9 CON bonus on first 9 HD)",
        "hp": 48,
        "move": "120' (40')",
        "thaco": "14 (Base Attack Bonus +5)",
        "attacks": "Melee: +7 to hit (The Auditor's Quill +2 parrying dagger, 1d4+2 piercing + Black Lotus/Belladonna Venom); Off-Hand: +6 to hit (Concealed Stiletto +1, 1d4+1 piercing); Backstab: x4 Damage (4d4+8 + Venom from stealth)",
        "abilities": [
            ("STR", 11, "Normal (0)"),
            ("DEX", 17, "+2 missile to hit, -2 AC bonus"),
            ("CON", 13, "+1 HP per Hit Die up to 9th level"),
            ("INT", 18, "+3 languages, perfect bureaucratic recall"),
            ("WIS", 15, "+1 on saving throws vs. magical spells"),
            ("CHA", 18, "+2 reaction, 7 retainers, morale 10, peerless court diplomat")
        ],
        "saves": [
            ("Breath Weapon (BW)", 8),   # 12 - 4 (Ring +2, Cloak +2)
            ("Poison or Death (P/D)", 5), # 9 - 4
            ("Petrify or Paralyze (PP)", 4), # 8 - 4
            ("Wands (W)", 6),           # 10 - 4
            ("Spells (S)", 6)           # 11 - 4 - 1 (WIS 15)
        ],
        "thiefSkills": [
            ("Pick Pockets", "85%"),
            ("Open Locks", "72%"),
            ("Find/Remove Traps", "70%"),
            ("Move Silently", "78%"),
            ("Climb Sheer Surfaces", "94%"),
            ("Hide in Shadows", "65%"),
            ("Hear Noise", "1-4 on 1d6"),
            ("Read Languages", "80%"),
            ("Read Magic Scrolls", "90% (Can cast arcane & divine scrolls up to 7th level!)")
        ],
        "magicItems": [
            "The Auditor's Quill (+2 Parrying Dagger; -1 AC in off-hand; hollow reservoir holding 3 doses of contact venom)",
            "Cloak of Displacement (The first attack directed at him each round automatically misses; all subsequent attacks suffer -2 to hit; grants +2 on all saving throws)",
            "Ring of Protection +2",
            "Amulet of Proof against Detection and Location (Impervious to ESP, Detect Thoughts, and scrying magic)",
            "Dust of Disappearance (3 pinches remaining; renders user invisible even to See Invisibility)",
            "Scroll of Dimension Door & Teleport (Stashed inside the silk lining of his doublet for emergency extraction)"
        ],
        "tactics": "<strong>Poisoned Blade:</strong> The Auditor's Quill is coated in concentrated Black Lotus & Belladonna venom. Target struck must make a Save vs. Poison at -2 penalty or take 3d6 poison damage and lapse into an immediate coma for 1d4 hours (botch = instant death).<br><strong>Elusive Evasion:</strong> Sadoria never fights openly. If combat breaks out, he immediately throws a pinch of <em>Dust of Disappearance</em> or activates a scroll of <em>Dimension Door</em> to escape into the palace secret passages.",
        "pcComparison": "Compared to the Level 8–9 PC Triumvirate, Sadoria possesses peerless defense against magic (Amulet blocks all divinations by the PC Mage) and an opening evasion buffer (Cloak of Displacement negates the PC Warrior's first attack). His x4 Backstab can drop the PC Mage or Cleric in a single strike if he catches them unawares."
    },
    "lucia": {
        "classLevel": "12th-Level Fighter (Grandmaster Zingaran Duelist)",
        "combatStats": "AC -1 (AAC 20) | HP 68 | THAC0 12 | Atk +12/+10 (1d8+5 / 1d4+3) | Crit 18-20 | Saves: 8/6/7/8/9",
        "alignment": "Chaotic (Passionate anti-feudal rebel, champion of the oppressed)",
        "station": "Republican Cell Commander in The Pit & Sovereign Fencing Master",
        "ac": "AC -1 (AAC 20)",
        "acBreakdown": "Bracers of Defense AC 4 (AAC 15), DEX 18 (-3), Cloak of Protection +1 (-1), Dueling Main-Gauche (-1 in melee)",
        "hd": "9d8+6 (+9 CON bonus on first 9 HD)",
        "hp": 68,
        "move": "120' (40') / Sprint 240' (80') with Boots of Speed",
        "thaco": "12 (Base Attack Bonus +7)",
        "attacks": "Melee: +12 to hit (Butterfly's Sting +3 Zingaran Dueling Rapier, 1d8+5 piercing, Critical Hit on natural 18-20 dealing 2d8+10 damage); Off-Hand: +10 to hit (Dueling Main-Gauche, 1d4+3 piercing)",
        "abilities": [
            ("STR", 16, "+2 to hit, +2 damage, Open Doors 1-3 on 1d6"),
            ("DEX", 18, "+3 missile to hit, -3 AC bonus, +2 on Initiative"),
            ("CON", 15, "+1 HP per Hit Die up to 9th level"),
            ("INT", 15, "+1 language, dueling theory & geometry"),
            ("WIS", 12, "Normal (0)"),
            ("CHA", 17, "+2 reaction, 6 retainers, morale 9, revolutionary magnetism")
        ],
        "saves": [
            ("Breath Weapon (BW)", 8),   # 9 - 1 (Cloak)
            ("Poison or Death (P/D)", 6), # 7 - 1
            ("Petrify or Paralyze (PP)", 7), # 8 - 1
            ("Wands (W)", 8),           # 9 - 1
            ("Spells (S)", 9)           # 10 - 1
        ],
        "magicItems": [
            "Butterfly's Sting (+3 Zingaran Dueling Rapier; scores a critical hit on natural 18-20, dealing double damage; ignores non-magical shield AC bonuses)",
            "Bracers of Defense AC 4 (AAC 15)",
            "Boots of Speed (Can run at 240' for up to 30 minutes per day; grants +2 to AC while running)",
            "Cloak of Protection +1",
            "Ring of Invisibility (Used to slip through sewer grates into palace corridors unnoticed)"
        ],
        "tactics": "<strong>Flèche Riposte:</strong> In single combat or duels under pundonor, whenever an opponent attacks and misses Lucia, she gains an immediate free counter-attack at +2 to hit.<br><strong>Disarming Flourish:</strong> Can sacrifice her off-hand attack to disarm an opponent on a successful attack roll vs. AC; target's weapon flies 10' unless they make a Save vs. Paralyze.",
        "pcComparison": "In a 1-on-1 formal duel under pundonor, Lucia's AC -1, Riposte, and 18-20 Critical Threat make her significantly more dangerous than the PC Warrior (Level 9). The PCs cannot defeat her in a sporting duel without relying on tactical dishonor, terrain advantages, or magical assistance."
    },
    "malachai": {
        "classLevel": "13th-Level Cleric (Patriarch of the Gnostic Ebon Flame)",
        "combatStats": "AC 1 (AAC 18) | HP 58 | THAC0 11 | Atk +12 (1d6+4 + Withering) | Spells up to 6th | Saves: 8/3/5/6/4",
        "alignment": "Chaotic (Fanatical Gnostic zealot, occult ascetic, sworn enemy of thralls)",
        "station": "High Priest of the Underground Church of Nemeth & Blind Prophet",
        "ac": "AC 1 (AAC 18)",
        "acBreakdown": "Vestments of the Ebon Void (Chain Mail +2 equivalent, AC 3), Ring of Protection +2 (-2)",
        "hd": "9d6+4 (+9 CON bonus on first 9 HD)",
        "hp": 58,
        "move": "90' (30')",
        "thaco": "11 (Base Attack Bonus +8)",
        "attacks": "Melee: +12 to hit (The Rod of Nemeth +3 Staff of Striking & Withering, 1d6+4 blunt + charge expenditure: Striking deals +2d6 damage [3d6+4 total]; Withering forces Save vs. Death or age 10 years and permanently lose 1 point of CON)",
        "abilities": [
            ("STR", 13, "+1 to hit, +1 damage"),
            ("DEX", 10, "Normal (0)"),
            ("CON", 15, "+1 HP per Hit Die up to 9th level"),
            ("INT", 16, "+2 languages, forbidden pre-Cataclysmic theology"),
            ("WIS", 18, "+3 on saving throws vs. magical spells, maximum divine bonus"),
            ("CHA", 17, "+2 reaction, 6 retainers, morale 10, religious fervor")
        ],
        "saves": [
            ("Breath Weapon (BW)", 8),   # 10 - 2 (Ring +2)
            ("Poison or Death (P/D)", 3), # 5 - 2
            ("Petrify or Paralyze (PP)", 5), # 7 - 2
            ("Wands (W)", 6),           # 8 - 2
            ("Spells (S)", 4)           # 9 - 2 - 3 (WIS 18)
        ],
        "spellsPrepared": [
            ("1st Level (6 slots)", "Cause Light Wounds (x2), Cure Light Wounds (x2), Darkness, Command"),
            ("2nd Level (5 slots)", "Hold Person (x2), Silence 15' Radius, Snake Charm, Spiritual Weapon"),
            ("3rd Level (5 slots)", "Animate Dead (Gnostic variant), Continual Darkness, Cure Blindness, Dispel Magic, Prayer"),
            ("4th Level (4 slots)", "Cause Serious Wounds, Cure Serious Wounds, Poison (Save or die), Protection from Evil 10' Radius"),
            ("5th Level (4 slots)", "Flame Strike (6d8 divine fire damage), Insect Plague, Quest, True Seeing"),
            ("6th Level (1 slot)", "Finger of Death (Save vs. Death or die instantly; if saved, takes 3d8 damage) OR Word of Recall")
        ],
        "magicItems": [
            "The Rod of Nemeth (+3 Staff of Striking & Withering, 20 charges remaining)",
            "Vestments of the Ebon Void (Enchanted dark-woven ceremonial robe, acts as Chain Mail +2)",
            "Ring of Protection +2",
            "Phial of Gnostic Tears (Sacred curative draught; cures all poisons and diseases, and restores 4d6+4 HP)"
        ],
        "tactics": "<strong>Eyes of the Void:</strong> Completely blind physically, but immune to all visual illusions, blindness, and darkness; perceives the soul, alignment, and life-force of all living and undead creatures within 60'.<br><strong>Turn / Command Undead:</strong> Commands or dispels undead as a 13th-level Patriarch; can contest Master Vane's control of industrial zombies.",
        "pcComparison": "Father Malachai commands 6th-level divine miracles, out-tiering the PC Cleric (Level 9, max 5th-level spells). His Save vs. Poison and Death is an astonishing <strong>3</strong>, and his <em>Finger of Death</em> can kill any party member in a single heartbeat if they provoke his divine wrath."
    },
    "gonzalo-guarralid": {
        "classLevel": "11th-Level Fighter (Grandee Warlord & Baron of Jerida)",
        "combatStats": "AC -1 (AAC 20) | HP 72 | THAC0 12 | Atk +12 (1d8+5) / Lance (2d10+10) | Saves: 9/7/8/9/10",
        "alignment": "Neutral (Arrogant feudal lord, jealous of provincial wealth and grazing rights)",
        "station": "Grandee Representative of the Eastern League & Lord of the Southern Plains",
        "ac": "AC -1 (AAC 20)",
        "acBreakdown": "Ornate Fluted Plate Mail +1, Grandee Tower Shield +1, DEX 13 (-1)",
        "hd": "9d8+4 (+18 CON bonus on first 9 HD)",
        "hp": 72,
        "move": "60' (20') on foot / Mounted 120' (40') on armored charger",
        "thaco": "12 (Base Attack Bonus +7)",
        "attacks": "Melee: +12 to hit (The River Cleaver +2 flanged war-mace, 1d8+5 crushing; +2d6 damage vs structures and watercraft); Secondary: +11 to hit (Zingaran Broadsword +1, 2d4+4 slashing); Mounted Lance Charge: +12 to hit, 2d10+10 piercing (double damage on charge)",
        "abilities": [
            ("STR", 18, "+3 to hit, +3 damage, Open Doors 1-5 on 1d6"),
            ("DEX", 13, "+1 missile to hit, -1 AC bonus"),
            ("CON", 17, "+2 HP per Hit Die up to 9th level"),
            ("INT", 12, "Normal (0)"),
            ("WIS", 11, "Normal (0)"),
            ("CHA", 15, "+1 reaction, 6 retainers, morale 9, commanding noble presence")
        ],
        "saves": [
            ("Breath Weapon (BW)", 9),
            ("Poison or Death (P/D)", 7),
            ("Petrify or Paralyze (PP)", 8),
            ("Wands (W)", 9),
            ("Spells (S)", 10)
        ],
        "magicItems": [
            "The River Cleaver (+2 Flanged War-Mace; deals an extra 2d6 damage against boats, gates, and palisades)",
            "Ornate Fluted Plate Mail +1",
            "Grandee Tower Shield +1 (Gilded with the Guarralid bull emblem)",
            "Horn of Blasting (Kept in his fortified Kordava estate)",
            "Potion of Giant Strength (Grants STR 21: +4 to hit, +6 damage for 1 hour)"
        ],
        "tactics": "<strong>Grandee Cavalry Escort:</strong> Always accompanied in the city by 6 veteran mounted caballeros (Fighters Level 5, AC 2, 28 HP each) and his personal armorer.<br><strong>Cattle Baron's Defiance:</strong> Immune to mundane intimidation; gains +2 on all saving throws against fear and panic.",
        "pcComparison": "With 72 HP and a devastating mounted lance charge (2d10+10), Gonzalo hits harder than the PC Warrior. In the capital, his retinue of veteran caballeros gives him local numerical superiority over the PCs."
    },
    "vesper": {
        "classLevel": "12th-Level Thief (Shadow King of The Pit)",
        "combatStats": "AC 0 (AAC 19) | HP 47 | THAC0 14 | Atk +8 (1d4+3 + Venom) | Backstab x4 | Saves: 11/8/7/9/9",
        "alignment": "Neutral (Pragmatic criminal broker, black market fence, underworld survivor)",
        "station": "Guildmaster of the Subterranean Smugglers & Relic Fence of The Pit",
        "ac": "AC 0 (AAC 19)",
        "acBreakdown": "Gargoyle-Hide Leather Armor +2, Ring of Protection +1, DEX 18 (-3)",
        "hd": "9d4+6 (+9 CON bonus on first 9 HD)",
        "hp": 47,
        "move": "120' (40')",
        "thaco": "14 (Base Attack Bonus +5)",
        "attacks": "Melee: +8 to hit (The Serrated Key +2 dagger of venom, 1d4+3 piercing + Spider Venom); Ranged: +10 to hit (Hand Crossbow +2, 1d6+2 piercing, range 50'/100'/150'); Backstab: x4 Damage (4d4+12 + Venom from stealth)",
        "abilities": [
            ("STR", 13, "+1 to hit, +1 damage"),
            ("DEX", 18, "+3 missile to hit, -3 AC bonus, +2 on Initiative"),
            ("CON", 14, "+1 HP per Hit Die up to 9th level"),
            ("INT", 17, "+2 languages, master of ancient pre-Cataclysmic ruins"),
            ("WIS", 15, "+1 on saving throws vs. magical spells"),
            ("CHA", 15, "+1 reaction, 5 retainers, morale 9, subterranean street respect")
        ],
        "saves": [
            ("Breath Weapon (BW)", 11),  # 12 - 1 (Ring)
            ("Poison or Death (P/D)", 8), # 9 - 1
            ("Petrify or Paralyze (PP)", 7), # 8 - 1
            ("Wands (W)", 9),           # 10 - 1
            ("Spells (S)", 9)           # 11 - 1 - 1 (WIS 15)
        ],
        "thiefSkills": [
            ("Pick Pockets", "85%"),
            ("Open Locks", "95% (70% base + 25% from Skeleton Key of Kalenius!)"),
            ("Find/Remove Traps", "75%"),
            ("Move Silently", "85% (Boots of Elvenkind: completely inaudible)"),
            ("Climb Sheer Surfaces", "96%"),
            ("Hide in Shadows", "72%"),
            ("Hear Noise", "1-4 on 1d6"),
            ("Read Languages", "80%"),
            ("Read Magic Scrolls", "90%")
        ],
        "magicItems": [
            "The Serrated Key (+2 Dagger of Venom; hilt contains 4 doses of paralyzing spider venom: Save vs. Poison or take 2d8 damage and suffer -3 DEX for 24 hours)",
            "Skeleton Key of King Kalenius (Pre-Cataclysmic iron key; functions as a Chime of Opening 3/day and grants +25% on Open Locks checks)",
            "Boots of Elvenkind (Move Silently checks succeed automatically unless running through water or dry leaves)",
            "Ring of Protection +1",
            "Ring of Invisibility (2 charges per day)",
            "Rope of Climbing (50' enchanted silk cord)"
        ],
        "tactics": "<strong>Subterranean Master:</strong> Cannot be pinned down in The Pit. Knows every secret chute, crawlway, and sewer floodgate under Kordava. If confronted, he drops an alchemical smoke bomb, activates his Ring of Invisibility, and melts into the stonework.",
        "pcComparison": "With 95% Open Locks, 85% Move Silently, and ancient keys, Vesper can bypass every mechanical lock, gate, and dungeon ward in Kordava. He can infiltrate the royal bedrooms without waking the palace guard."
    },
    "vane": {
        "classLevel": "12th-Level Magic-User (Royal Necromancer & Fleshcrafter)",
        "combatStats": "AC 4 (AAC 15) | HP 36 | THAC0 16 | Atk +4 (1d4+1 + Paralysis) | Spells up to 6th | Saves: 11/9/8/9/9",
        "alignment": "Neutral (Coldly rational, completely devoid of moral sentiment regarding the dead)",
        "station": "Industrial Thrall Overseer & Master of the Royal Necromantic Laboratories",
        "ac": "AC 4 (AAC 15)",
        "acBreakdown": "Robes of the Alchemist's Hearth (Acts as Bracers AC 6), Ring of Protection +1 (-1), DEX 14 (-1)",
        "hd": "9d4+3 (+9 CON bonus on first 9 HD)",
        "hp": 36,
        "move": "120' (40')",
        "thaco": "16 (Base Attack Bonus +3)",
        "attacks": "Melee: +4 to hit (Needle-Scalpel +1, 1d4+1 piercing + Alchemical Paralytic: Save vs. Paralyze or become completely rigid for 2d4 turns)",
        "abilities": [
            ("STR", 9, "Normal (0)"),
            ("DEX", 14, "+1 missile to hit, -1 AC bonus"),
            ("CON", 14, "+1 HP per Hit Die up to 9th level"),
            ("INT", 18, "+3 languages, maximum spell comprehension, master of dark sciences"),
            ("WIS", 14, "+1 on saving throws vs. magical spells"),
            ("CHA", 8, "-1 reaction, pale cadaverous complexion and pungent chemical odor")
        ],
        "saves": [
            ("Breath Weapon (BW)", 11),  # 12 - 1 (Ring)
            ("Poison or Death (P/D)", 9), # 10 - 1
            ("Petrify or Paralyze (PP)", 8), # 9 - 1
            ("Wands (W)", 9),           # 10 - 1
            ("Spells (S)", 9)           # 11 - 1 - 1 (WIS 14)
        ],
        "spellsPrepared": [
            ("1st Level (4 slots)", "Magic Missile (5 missiles: 5d4+5 force damage), Shield (AC 2 vs. missiles), Sleep, Charm Person"),
            ("2nd Level (4 slots)", "Invisibility, Mirror Image (1d4 images), Web, Phantasmal Force"),
            ("3rd Level (4 slots)", "Fireball (12d6 fire damage!), Dispel Magic, Haste (can haste up to 12 zombies/retainers), Hold Person"),
            ("4th Level (4 slots)", "Dimension Door, Wall of Fire, Polymorph Other, Confusion"),
            ("5th Level (4 slots)", "Cloudkill (Instant death to creatures <=4 HD; 1d10 to higher), Conjure Elemental (Earth: 16 HD), Telekinesis, Hold Monster"),
            ("6th Level (1 slot)", "Death Spell (Destroys 4d8 HD of creatures of <=8 HD without a saving throw!) OR Disintegrate (Save vs. Death or disintegrate to dust!)")
        ],
        "magicItems": [
            "Canopic Urn of Kalenius (Ancient pre-Cataclysmic reliquary; allows mental coordination of up to 30 HD of memory-retaining zombies without verbal commands)",
            "Wand of Paralyzation (18 charges remaining; fires a 60' cone, Save vs. Wands or paralyzed for 6 turns)",
            "Ring of Regeneration (Restores 1 HP per combat round; can regrow severed fingers or flesh)",
            "Robes of the Alchemist's Hearth (Enchanted protective robes, provides AC 6 base)"
        ],
        "tactics": "<strong>Thrall Mind-Link:</strong> Vane never fights alone. In his laboratory, he is surrounded by 8 Heavy Zombie Enforcers (3 HD, 18 HP, AC 6, slam 1d8).<br><strong>Mass Haste:</strong> In battle, he casts <em>Haste</em> on his zombie guards (doubling their attacks and speed to 120'), while using <em>Wall of Fire</em> or <em>Cloudkill</em> to control the battlefield.",
        "pcComparison": "Vane casts 6th-level arcane spells, whereas the PC Mage (Level 8) is limited to 4th-level magic. His 12d6 <em>Fireball</em> can incinerate the PC Mage in a single volley, and his <em>Death Spell</em> can annihilate all royal household guards and retainers without allowing a saving throw."
    },
    "tiberio": {
        "classLevel": "11th-Level Fighter (Argossean Corsair Captain & Fleet Commander)",
        "combatStats": "AC 0 (AAC 19) | HP 65 | THAC0 12 | Atk +11 (1d8+5) | Saves: 9/7/8/9/9",
        "alignment": "Lawful (Strict adherence to maritime code, naval contracts, and commercial debt)",
        "station": "Plenipotentiary Envoy of the Merchant Kingdom of Argos",
        "ac": "AC 0 (AAC 19)",
        "acBreakdown": "Sea-Forged Scale Mail +2 (AC 4), Buckler of the Barachas +1 (-2), DEX 15 (-1)",
        "hd": "9d8+4 (+9 CON bonus on first 9 HD)",
        "hp": 65,
        "move": "90' (30') on land / 120' on ship deck",
        "thaco": "12 (Base Attack Bonus +7)",
        "attacks": "Melee: +11 to hit (The Foreclosure +2 heavy cutlass, 1d8+5 slashing, Critical Hit on natural 19-20 severs opponent's shield or armor strap); Ranged: +9 to hit (Heavy Crossbow +1, 1d8+1 piercing, range 80'/160'/240')",
        "abilities": [
            ("STR", 16, "+2 to hit, +2 damage, Open Doors 1-3 on 1d6"),
            ("DEX", 15, "+1 missile to hit, -1 AC bonus"),
            ("CON", 14, "+1 HP per Hit Die up to 9th level"),
            ("INT", 16, "+2 languages, international maritime law, trade diplomacy"),
            ("WIS", 14, "+1 on saving throws vs. magical spells"),
            ("CHA", 17, "+2 reaction, 6 retainers, morale 9, commanding sea-captain presence")
        ],
        "saves": [
            ("Breath Weapon (BW)", 9),
            ("Poison or Death (P/D)", 7),
            ("Petrify or Paralyze (PP)", 8),
            ("Wands (W)", 9),
            ("Spells (S)", 9)  # 10 - 1 (WIS 14)
        ],
        "magicItems": [
            "The Foreclosure (+2 Heavy Argossean Cutlass; critical hit on 19-20 destroys non-magical shields or armor straps, imposing -2 to opponent's AC)",
            "Sea-Forged Scale Mail +2 (Treated with alchemical sea-turtle oil; wearer floats automatically and swims at full movement without encumbrance penalties)",
            "Buckler of the Barachas +1 (Parrying naval buckler)",
            "Ring of Water Walking (Allows movement across harbor water at full running speed [120' per turn])",
            "Potions of Water Breathing (x2 vials)"
        ],
        "tactics": "<strong>Marine Phalanx:</strong> Accompanied in Kordava by 8 elite Messantian marines (Fighters Level 4, AC 3, 24 HP, armed with heavy cutlasses and crossbows).<br><strong>Naval Blockade Command:</strong> Can signal his offshore war-galleys in the bay (3 galleys, 180 marines, shipboard heavy ballistas) to cut off all food imports into Kordava.",
        "pcComparison": "Tiberio combines seasoned Level 11 martial combat with foreign superpower backing. The PCs cannot execute or imprison him without triggering an immediate naval blockade and declaration of war from the kingdom of Argos."
    }
}

def generate_stat_block_html(nid, stats, npc_title):
    # Abilities bar
    ab_boxes = ""
    for ab_name, ab_val, ab_desc in stats["abilities"]:
        mod_str = f"+{ab_val-10}" if ab_val > 10 else f"{ab_val-10}"
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
        <div class="stat-section-title">Thief Skills (Labyrinth Lord 12th Level)</div>
        <div class="stat-pill-list">{thief_pills}</div>
        """

    # Optional Spells
    spells_html = ""
    if "spellsPrepared" in stats:
        spell_rows = ""
        for circle, slist in stats["spellsPrepared"]:
            spell_rows += f"<p style=\"margin-bottom: 4px;\"><strong>{circle}:</strong> {slist}</p>\n"
        spells_html = f"""
        <div class="stat-section-title">Spells Prepared (Labyrinth Lord Divine/Arcane Circles)</div>
        <div style="background: var(--bg-surface); padding: 10px 14px; border-radius: var(--radius-sm); margin: 6px 0;">
          {spell_rows}
        </div>
        """

    html = f"""
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

  <div class="stat-section-title">Special Combat Feats &amp; Pundonor Arts</div>
  <p>{stats['tactics']}</p>

  <div class="stat-section-title">Power Scale vs. PC Triumvirate (Level 8–9 Rulers)</div>
  <p class="text-muted" style="margin-bottom: 0;">{stats['pcComparison']}</p>
</div>
"""
    return html

def update_data_file():
    import os
    with open('temp_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update each NPC
    for nid, stats in LL_NPCS.items():
        art = next((a for a in data['articles'] if a['id'] == nid), None)
        if not art:
            print(f"Warning: Article {nid} not found!")
            continue

        # Update atAGlance
        if 'atAGlance' not in art:
            art['atAGlance'] = {}
        art['atAGlance']['classLevel'] = stats['classLevel']
        art['atAGlance']['combatStats'] = stats['combatStats']

        # Generate stat block
        stat_block = generate_stat_block_html(nid, stats, art['title'])

        # Inject into content right below the npc-header-card (or at the top if no header card)
        c = art['content']
        # Remove old stat block if present
        c = re.sub(r'<div class="stat-block">.*?</div>\s*(?=<h3>|$)', '', c, flags=re.DOTALL)

        header_card_end = c.find('</div>\n\n<h3>Public Persona')
        if header_card_end != -1:
            # Find the closing </div> of npc-header-card
            header_card_end = c.find('</div>\n\n<h3>Public Persona') + 6
            c = c[:header_card_end] + "\n" + stat_block + "\n" + c[header_card_end:]
        else:
            # Prepend before Public Persona
            pub_idx = c.find('<h3>Public Persona')
            if pub_idx != -1:
                c = c[:pub_idx] + stat_block + "\n" + c[pub_idx:]
            else:
                c = stat_block + "\n" + c

        art['content'] = c
        print(f"Updated NPC {nid} ({stats['classLevel']})")

    # 2. Update court-matrix with Master Labyrinth Lord Hierarchy Table
    matrix_art = next((a for a in data['articles'] if a['id'] == 'court-matrix'), None)
    if matrix_art:
        ll_table_html = """
<h3>Labyrinth Lord Rules: City Power &amp; Combat Hierarchy Matrix</h3>
<p>In accordance with <em>Labyrinth Lord</em> (B/X D&amp;D retro-clone) rules, the Player Characters constitute an untested sovereign Triumvirate (Level 8–9; 240,000 XP baseline: Fighter 9, Cleric 9, Magic-User 8). The entrenched military handlers, ministers, cult patriarchs, and subterranean kingpins of Kordava are <strong>veterans of 11th to 13th level</strong> who hold overwhelming direct martial, arcane, and financial superiority.</p>

<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>NPC Leader</th>
      <th>Labyrinth Lord Class &amp; Level</th>
      <th>Alignment</th>
      <th>AC (AAC)</th>
      <th>HP</th>
      <th>THAC0 (Atk)</th>
      <th>Signature Relic / Magic</th>
      <th>Tactical Scale vs. PC Triumvirate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong><a href="#npcs/valenza" class="wiki-link">General Don Rodrigo de Valenza</a></strong><br><small>Head of Royal Army</small></td>
      <td><span class="stat-class-level">Fighter 13</span></td>
      <td>Neutral</td>
      <td><strong>-2 (21)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">78</span></td>
      <td>10 (+15)</td>
      <td><em>The Iron Edict</em> (+3 Longsword), <em>Plate +2</em>, <em>Ring of Free Action</em></td>
      <td>Out-tanks and out-hits PC Fighter (Lvl 9). Direct martial duel is near-suicide without dividing his garrisons.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/sadoria" class="wiki-link">High Chancellor Marquis Mateo de Sadoria</a></strong><br><small>Chief Monarchist</small></td>
      <td><span class="stat-class-level">Thief 12</span></td>
      <td>Chaotic</td>
      <td><strong>1 (18)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">48</span></td>
      <td>14 (+7)</td>
      <td><em>Auditor's Quill</em> (+2 Venom Dagger), <em>Cloak of Displacement</em></td>
      <td>1st attack auto-misses; mind shielded from Mage divinations; x4 Backstab drops unarmored royals.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/lucia" class="wiki-link">Fencing Master Lucia 'La Mariposa'</a></strong><br><small>Republican Commander</small></td>
      <td><span class="stat-class-level">Fighter 12</span></td>
      <td>Chaotic</td>
      <td><strong>-1 (20)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">68</span></td>
      <td>12 (+12)</td>
      <td><em>Butterfly's Sting</em> (+3 Rapier, Crit 18-20), <em>Boots of Speed</em></td>
      <td>Counters every missed attack with free Riposte. Decisively defeats PC Warrior in sporting pundonor duel.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/malachai" class="wiki-link">Father Malachai the Blind</a></strong><br><small>High Priest of Nemeth</small></td>
      <td><span class="stat-class-level">Cleric 13</span></td>
      <td>Chaotic</td>
      <td><strong>1 (18)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">58</span></td>
      <td>11 (+12)</td>
      <td><em>Rod of Nemeth</em> (Withering), <em>Finger of Death</em> (6th-circle)</td>
      <td>Casts 6th-level miracles (PC Cleric has 5th). Save vs Death is 3; can destroy or command party's thralls.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/gonzalo-guarralid" class="wiki-link">High Duke Gonzalo de Guarralid</a></strong><br><small>Grandee Representative</small></td>
      <td><span class="stat-class-level">Fighter 11</span></td>
      <td>Neutral</td>
      <td><strong>-1 (20)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">72</span></td>
      <td>12 (+12)</td>
      <td><em>River Cleaver</em> (+2 Mace), Lance Charge (2d10+10), <em>Plate +1</em></td>
      <td>Brutal martial HP; charge deals 2d10+10; backed by 6 veteran mounted caballero retainers in Kordava.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/vesper" class="wiki-link">Vesper the Key-Master</a></strong><br><small>Spymaster of The Pit</small></td>
      <td><span class="stat-class-level">Thief 12</span></td>
      <td>Neutral</td>
      <td><strong>0 (19)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">47</span></td>
      <td>14 (+8)</td>
      <td><em>Serrated Key</em> (+2 Venom), <em>Skeleton Key of Kalenius</em></td>
      <td>Open Locks 95%; inaudible stealth; can penetrate any royal treasury, chamber, or dungeon unobserved.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/vane" class="wiki-link">Master Alchemist Vane</a></strong><br><small>Royal Necromancer</small></td>
      <td><span class="stat-class-level">Magic-User 12</span></td>
      <td>Neutral</td>
      <td><strong>4 (15)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">36</span></td>
      <td>16 (+4)</td>
      <td><em>Death Spell</em> (6th), 12d6 <em>Fireball</em>, <em>Canopic Urn</em></td>
      <td>Casts 6th-circle arcane magic (PC Mage has 4th). <em>Death Spell</em> wipes out retainers without saving throw.</td>
    </tr>
    <tr>
      <td><strong><a href="#npcs/tiberio" class="wiki-link">Ambassador Tiberio of Messantia</a></strong><br><small>Foreign Envoy of Argos</small></td>
      <td><span class="stat-class-level">Fighter 11</span></td>
      <td>Lawful</td>
      <td><strong>0 (19)</strong></td>
      <td><span style="color: #2ecc71; font-weight:700;">65</span></td>
      <td>12 (+11)</td>
      <td><em>The Foreclosure</em> (+2 Cutlass), <em>Sea-Forged Scale +2</em></td>
      <td>Veteran naval captain backed by 8 elite Messantian marines and 3 offshore war-galleys blockading port.</td>
    </tr>
  </tbody>
</table>
</div>
"""
        if "Labyrinth Lord Rules: City Power &amp; Combat Hierarchy Matrix" not in matrix_art['content']:
            matrix_art['content'] += "\n" + ll_table_html
            print("Updated court-matrix with Labyrinth Lord Hierarchy table")

    # 3. Add or update rules article: rules/labyrinth-lord-mechanics
    ll_rules_id = "labyrinth-lord-mechanics"
    ll_rules_art = next((a for a in data['articles'] if a['id'] == ll_rules_id), None)
    
    ll_rules_content = """
<h3>1. The Labyrinth Lord Rules Framework in Our Kingdom Come</h3>
<p><em>Our Kingdom Come</em> is structured upon the classic <strong>Labyrinth Lord</strong> ruleset—an authentic retro-clone of the classic 1981 B/X Fantasy Adventure rules. It employs the six foundational ability scores (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma), classic descending Armor Class (with ascending AAC in parentheses), the five canonical saving throw categories, and the 3-point alignment continuum (Law, Neutrality, Chaos).</p>

<div class="rule-box">
  <div class="rule-header">CORE LABYRINTH LORD CONVERSIONS</div>
  <p><strong>Descending Armor Class (AC):</strong> Unarmored is AC 9 (AAC 10). Leather is AC 7 (AAC 12). Chain Mail is AC 5 (AAC 14). Plate Mail is AC 3 (AAC 16). Shields improve AC by -1 (AAC +1). Magical bonuses further decrease AC down into the negative numbers (e.g. AC -2 is AAC 21).</p>
  <p><strong>Saving Throws (5-Column Matrix):</strong> Saving throws are rolled on 1d20 against a target number determined by character class and level: <strong>Breath Weapon (BW)</strong>, <strong>Poison or Death (P/D)</strong>, <strong>Petrify or Paralyze (PP)</strong>, <strong>Wands (W)</strong>, and <strong>Spells or Spell-like Devices (S)</strong>.</p>
  <p><strong>THAC0 (To Hit Armor Class 0):</strong> Represents the combat roll needed on 1d20 to hit an AC 0 opponent. Roll 1d20 + Attack Bonuses &ge; (THAC0 - Target's AC).</p>
</div>

<h3>2. The PC Triumvirate Baseline (240,000 Experience Points)</h3>
<p>The three Player Characters—descendants of King Ancillus I installed as the ruling Triumvirate—have earned experience points equivalent to a <strong>9th-Level Fighter (240,000 XP)</strong>. Under Labyrinth Lord rules, different classes advance at different XP scales, establishing the following party tier:</p>

<div class="table-container">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Player Character Class</th>
      <th>XP Threshold</th>
      <th>Level Attained</th>
      <th>Title / Station</th>
      <th>Hit Dice &amp; Combat Profile</th>
      <th>Spell Slots / Abilities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>The Warrior (Fighter)</strong></td>
      <td>240,000 XP</td>
      <td><strong>Level 9</strong></td>
      <td>Lord / Superhero</td>
      <td>9d8 HD (~50 HP), THAC0 14 (+5 Atk), Saves: 8/9/10/13/10</td>
      <td>Can establish a stronghold, attract a mercenary company of 1d4&times;10 fighters, and wield any weapon/armor.</td>
    </tr>
    <tr>
      <td><strong>The Cleric</strong></td>
      <td>200,000 XP (at 240k)</td>
      <td><strong>Level 9</strong></td>
      <td>High Priest / Prelate</td>
      <td>9d6 HD (~40 HP), THAC0 14 (+5 Atk), Saves: 12/6/9/10/11</td>
      <td>Spells: 3 / 3 / 3 / 2 / 1 (Up to 5th-level spells like <em>Flame Strike</em>, <em>Raise Dead</em>, and <em>Quest</em>). Turn Undead as High Priest.</td>
    </tr>
    <tr>
      <td><strong>The Mage (Magic-User)</strong></td>
      <td>150,000 XP (at 240k)</td>
      <td><strong>Level 8</strong></td>
      <td>Sorcerer / Magus</td>
      <td>8d4 HD (~24 HP), THAC0 17 (+2 Atk), Saves: 14/12/11/12/13</td>
      <td>Spells: 3 / 3 / 2 / 2 (Up to 4th-level spells like <em>Fireball</em>, <em>Lightning Bolt</em>, <em>Dimension Door</em>, and <em>Wall of Fire</em>). Requires 300,000 XP for 9th level!</td>
    </tr>
  </tbody>
</table>
</div>

<h3>3. The City Power Hierarchy: Why the Handlers Out-Tier the PCs</h3>
<p>The Game Master must enforce the central operational premise: <strong>the PCs are untested monarchs whose city handlers are veterans of Level 11 to 13</strong>.</p>
<ul>
  <li><strong>Military Elite (General Don Rodrigo de Valenza — Fighter 13, AC -2, 78 HP):</strong> Boasts nearly double the PC Fighter's health, an attack bonus of +15 with <em>The Iron Edict</em>, and command over hundreds of garrison troops. A frontal assault against him leads to swift military capture or death.</li>
  <li><strong>Monarchist Bureaucracy (Marquis Mateo de Sadoria — Thief 12, AC 1, 48 HP):</strong> His <em>Cloak of Displacement</em> automatically negates the PCs' first attack, while his <em>Amulet</em> prevents the PC Mage from reading his mind. His x4 Backstab with lethal venom can assassinate an isolated PC.</li>
  <li><strong>Underground Nemeth (Father Malachai the Blind — Cleric 13, AC 1, 58 HP):</strong> Wields 6th-circle divine miracles (including <em>Finger of Death</em> and <em>Word of Recall</em>) and a Save vs. Poison/Death of <strong>3</strong>. He outclasses the PC Cleric by two entire spell levels.</li>
  <li><strong>Industrial Necromancy (Master Alchemist Vane — Magic-User 12, AC 4, 36 HP):</strong> Casts 6th-circle arcane magic (including <em>Death Spell</em> and <em>Disintegrate</em>) and can hurl 12d6 <em>Fireballs</em>. His <em>Death Spell</em> slays creatures of 8 HD or less without a saving throw, meaning PC retainers and guards are wiped out instantly.</li>
</ul>

<div class="gm-callout">
  <div class="gm-badge">GM CONFIDENTIAL &bull; SANDBOX RESOLUTION DIRECTIVE</div>
  <p>Because the city handlers out-tier the PCs in direct combat, the Triumvirate must overcome their handlers through <strong>asymmetric sandbox play</strong>:</p>
  <ul>
    <li>Exploit rivalries: Set General Don Rodrigo against Marquis Mateo, or pit Father Malachai's zealots against Master Vane's thrall pits.</li>
    <li>Recover pre-Cataclysmic relics: The <em>Black Blade of Kalenius</em> and <em>Obsidian Blade of Azur</em> level the playing field against high-level warlords.</li>
    <li>Utilize Pundonor duel exemptions: Under Zingaran code, even a Level 13 General must face formal duel conditions if insulted under sacred forms.</li>
    <li>Secure independent revenue: Bypass Sadoria's treasury lockout by tapping smuggling channels with Vesper or uncovering King Kalenius's flooded tombs.</li>
  </ul>
</div>
"""

    if not ll_rules_art:
        data['articles'].append({
            "id": ll_rules_id,
            "category": "rules",
            "title": "Labyrinth Lord Rules & PC/NPC Tier System",
            "subtitle": "Retro-Clone D&D Core System, Level 8-9 PC Baseline, & Level 11-13 City Power Hierarchy",
            "tags": ["Rules", "Labyrinth Lord", "Mechanics", "PC Tiers", "NPC Levels", "D&D Retro-Clone"],
            "aliases": ["Labyrinth Lord Rules", "Labyrinth Lord", "PC Levels", "NPC Levels", "D&D Rules", "Labyrinth Lord Mechanics"],
            "summary": "Complete Labyrinth Lord (B/X retro-clone) mechanical parameters: Level 9 Warrior (240k XP), Level 9 Cleric, Level 8 Mage, versus Level 11–13 city handlers, saves, THAC0, and combat dynamics.",
            "content": ll_rules_content,
            "gmSecrets": "Ensure players realize that attacking Rodrigo, Sadoria, or Vane directly is a TPK without alliances or relics.",
            "relatedIds": ["court-matrix", "valenza", "sadoria", "lucia", "malachai", "pundonor", "command-friction"]
        })
        print("Created rules/labyrinth-lord-mechanics article")
    else:
        ll_rules_art['content'] = ll_rules_content
        print("Updated rules/labyrinth-lord-mechanics article")

    # Update meta count
    data['meta']['totalArticles'] = len(data['articles'])

    # Write back to js/data.js
    new_data_str = f"// Our Kingdom Come - Zingara Sandbox GM Compendium Data\n// Auto-compiled from canonical source documents and Labyrinth Lord game statistics\n\nwindow.WIKI_DATA = {json.dumps(data, indent=2)};\n\nvar WIKI_DATA = window.WIKI_DATA;\n\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = WIKI_DATA;\n}}\n"

    with open('js/data.js', 'w', encoding='utf-8') as f:
        f.write(new_data_str)

    if os.path.exists('temp_data.json'):
        os.remove('temp_data.json')

    print(f"\nSuccessfully updated js/data.js! Total articles: {len(data['articles'])}")

if __name__ == '__main__':
    update_data_file()
