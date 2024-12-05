from config import ROOT_REPO as ROOT


def img(i: str, w: int = 16, h: int = 16):
    return f'<img src="{i}" width="{w}" height="{h}"/>'

def link(name: str, url: str, i: str, w: int = 16, h: int = 16):
    return f'{img(i, w, h)} [{name}]({url})' if url else name

RECIPE_SOURCES = {
    'Tier 1 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/constructor/icon1.png) [[ Alta Constructor ]]': [
        'alta_constructor1',
    ],
    'Tier 2 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/constructor/icon2.png) [[ Alta Constructor ]]': [
        'alta_constructor2',
    ],
    'Tier 3 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/constructor/icon3.png) [[ Alta Constructor ]]': [
        'alta_constructor3',
    ],
    'Tier 4 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/constructor/icon4.png) [[ Alta Constructor ]]': [
        'alta_constructor4',
    ],
    'Tier 5 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/constructor/icon5.png) [[ Alta Constructor ]]': [
        'alta_constructor5',
    ],
    'Tier 1 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon1.png) [[ Alta Crafting Station ]]': [
        "alta_t1", "alta_t1+",
    ],
    'Tier 2 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon2.png) [[ Alta Crafting Station ]]': [
        "alta_t2", "alta_t2+", "alta_t2m",
    ],
    'Tier 3 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon3.png) [[ Alta Crafting Station ]]': [
        "alta_t3", "alta_t3+", "alta_t3m", "alta_t3mm",
    ],
    'Tier 4 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon4.png) [[ Alta Crafting Station ]]': [
        "alta_t4", "alta_t4+", "alta_t4m", "alta_t4mm", "alta_t4mmm",
    ],
    '![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/datacenter/icon.png) [[ Alta Datacenter|Alta-Datacenter ]]': [
        'alta_codex',
    ],
    'Tier 1 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/upgrade_station/icon1.png) [[ Alta Upgrade Station|Alta-Upgrade-Station ]]': [
        'ct_alta_upg1',
    ],
    'Tier 2 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/upgrade_station/icon2.png) [[ Alta Upgrade Station|Alta-Upgrade-Station ]]': [
        'ct_alta_upg2',
    ],
    f'{link("Cooking Stations", "https://starbounder.org/Cooking#Meal_Prep_Stations", "https://starbounder.org/mediawiki/images/b/b2/Chic_Cooking_Table.png", 12, 8)}': [
        'craftingfood',
    ],
    f'{link("Inventor`s Table", "https://starbounder.org/Inventor%27s_Table", "https://starbounder.org/mediawiki/images/3/3f/Inventor%27s_Table.png", 12, 14)}': [
        'inventorstable',
    ],
    f'{link("Refinery", "https://starbounder.org/Refinery", "https://starbounder.org/mediawiki/images/2/2a/Refinery.gif", 12, 12)}': [
        'refinery',
    ],
    f'{link("Treasured Trophies", "https://starbounder.org/Treasured_Trophies", "https://starbounder.org/mediawiki/images/2/2b/Treasured_Trophies.gif", 17, 9)}': [
        'treasuredtrophies',
    ],
}

RECIPE_SOURCES_ADMIN = {
    '![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/constructor/icon5.png) [[ Ultimate Constructor|Alta-Constructor ]]': [
        'alta_constructor1',
        'alta_constructor2',
        'alta_constructor3',
        'alta_constructor4',
        'alta_constructor5',
        'alta_constructor6',
    ],
    '![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon5.png) [[ Ultimate Crafting Station|Alta-Crafting-Station ]]': [
        "alta_t1", "alta_t1+",
        "alta_t2", "alta_t2+", "alta_t2m",
        "alta_t3", "alta_t3+", "alta_t3m", "alta_t3mm",
        "alta_t4", "alta_t4+", "alta_t4m", "alta_t4mm", "alta_t4mmm",
        'alta_max',
    ],
    link("Tabula Rasa", "https://community.playstarbound.com/resources/the-tabula-rasa.3222/", "https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/", 8, 12): [
        'mod',
    ],
}

RECIPE_SIP = link('Spawnable Item Pack', 'https://steamcommunity.com/sharedfiles/filedetails/?id=733665104', 'https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png', 18, 14)

RARITIES = {
    'Common': 'a common',
    'Uncommon': 'an uncommon',
    'Rare': 'a rare',
    'Legendary': 'a legendary',
    'Essential': 'a unique',
}

ELEMENTS = {
    'physical': '[physical](https://starbounder.org/Damage)',
    'electric': f'{link("electric", "https://starbounder.org/Weapons#Elemental_Damage", "https://starbounder.org/mediawiki/images/1/15/Electric_%28Attack%29.png", 16, 16)}',
    'fire': f'{link("fire", "https://starbounder.org/Weapons#Elemental_Damage", "https://starbounder.org/mediawiki/images/8/82/Fire_%28Attack%29.png", 16, 16)}',
    'ice': f'{link("ice", "https://starbounder.org/Weapons#Elemental_Damage", "https://starbounder.org/mediawiki/images/3/35/Frost_%28Attack%29.png", 16, 16)}',
    'poison': f'{link("poison", "https://starbounder.org/Weapons#Elemental_Damage", "https://starbounder.org/mediawiki/images/d/dd/Poison_%28Attack%29.png", 16, 16)}',
    'water': '[water](https://starbounder.org/Weapons#Elemental_Damage)',
    'impulse': '![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/damage/ct_impulse.png) [impulse](Ceternia#damage)',
    'plasma': '![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/damage/ct_plasma.png) [plasma](Alternia#damage)',
    'ionic': '![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/damage/ct_ionic.png) [ionic](Enternia#damage)',
}

RACES = {
    'alta': 'Alta',
    'apex': 'https://starbounder.org/Apex',
    'avian': 'https://starbounder.org/Avian',
    'floran': 'https://starbounder.org/Floran',
    'glitch': 'https://starbounder.org/Glitch',
    'human': 'https://starbounder.org/Human',
    'hylotl': 'https://starbounder.org/Hylotl',
    'novakid': 'https://starbounder.org/Novakid',
    'generic': 'https://starbounder.org/Perfectly_Generic_Item',
    'ancient': 'https://starbounder.org/Ancient',
    'agaran': 'https://starbounder.org/Agaran',
    'alpaca': 'https://starbounder.org/Alpaca',
    'deadbeat': 'https://starbounder.org/Deadbeat',
    'fenerox': 'https://starbounder.org/Fenerox',
    'frogg': 'https://starbounder.org/Frogg',
    'penguin': 'https://starbounder.org/Penguin',
    'shadow': 'https://starbounder.org/Shadow',
}

# \{ 'name': '-', 'category': '-', 'title': ('Alterash'), 'icon': (ROOT \+ '.*') \},
# $1: $2,

PAGES = {
    'Alterash': ROOT + '/interface/bookmarks/icons/ct_alterash_planet.png',
    'Alterash Prime': ROOT + '/interface/bookmarks/icons/ct_alterash_prime_planet.png',
    'Enterash': ROOT + '/interface/bookmarks/icons/ct_enterash_planet.png',
    'Enterash Prime': ROOT + '/interface/bookmarks/icons/ct_enterash_prime_planet.png',
    'EDS': ROOT + '/items/active/unsorted/alta/loot/ct_eds_loot.png',
    'Faradea': ROOT + '/items/active/unsorted/alta/loot/ct_faradea_loot.png',

    'Ceternia': ROOT + '/damage/ct_impulse.png',
    'Alternia': ROOT + '/damage/ct_plasma.png',
    'Enternia': ROOT + '/damage/ct_ionic.png',

    # 'Aric': ROOT + '/items/active/unsorted/alta/loot/ct_shroomic_loot.png',
    'Ayaka': ROOT + '/objects/biome/alterash/ayaka/ct_aya_pile/icon.png',
    'Isoslime': ROOT + '/items/throwables/ct_isoslime_ball.png',
    'Koywa': ROOT + '/objects/biome/alterash/koywa/grass/bushy/icon.png',
    'Nivera': ROOT + '/objects/biome/alterash/warped/ct_nivera_thorns/icon.png',
    'Tonnova': ROOT + '/items/throwables/ct_tonna.png',
    'Warped': ROOT + '/items/throwables/ct_warped_hive.png',
    'Yaara': ROOT + '/items/generic/produce/ct_yaara_root.png',

    'Bionid': ROOT + '/items/generic/crafting/ct_bionid.png',
    'Phospholion': ROOT + '/items/generic/crafting/ct_phospholion.png',

    'Bishyn': ROOT + '/objects/biome/alterash_prime/bishyn/ct_poison_crystal1/icon.png',
    'Calin': ROOT + '/objects/biome/alterash_prime/calin/decorative/ct_calin_sample/icon.png',
    # 'Crystalline Prime': ROOT + '/items/active/unsorted/alta/loot/ct_crystalline_prime_loot.png',
    'Gheatsyn': ROOT + '/items/throwables/ct_gheatsyn_shard.png',
    'Hevika': ROOT + '/items/generic/crafting/ct_alternia_shard.png',
}

ALIASES = {
    'faction': 'Factions',
    'planet': 'Planets',
    'tree': 'Plants#saplings',
    'weapon': 'Weapons',
    'energy': 'World#energy',
    'crystallic': 'World#crystallic',
    'crystallic environment': 'World#crystallic',

    'Combo Attacks': 'Weapons#Combo-Attacks',
    'Charged Hits': 'Weapons#Charged-Hits',
    'Downstab': 'Weapons#Downstab',
    'Blade Charge': 'Weapons#Blade-Charge',
    'Rising Slash': 'Weapons#Rising-Slash',
    'Kunai Blast': 'Weapons#Kunai-Blast',
    'Trail Dash': 'Weapons#Trail-Dash',
    'Spin Slash': 'Weapons#Spin-Slash',
    'Super Spin Slash': 'Weapons#Super-Spin-Slash',

    'antorash': 'Alterash#antorash',
    'underworld': 'Alterash#antorash',
    'alterash planet': 'Alterash',
    'alterash prime planet': 'Alterash-Prime',
    'alterash underworld': 'Alterash#antorash',
    'evarus': 'Alterash#evarus',
    'esetera': 'Alterash-Prime#esetera',
    'esetera caves': 'Alterash-Prime#esetera-caves',
    'esetera depths': 'Alterash-Prime#esetera-depths',
    'evarus prime': 'Alterash-Prime#evarus-prime',
    'ion core': 'Alterash-Prime#ion-core',
    'verriskoywa': 'Koywa',
    'io ceterai': 'io',

    'impulse status immunity': 'Ceternia#immunity',
    'plasma status immunity': 'Alternia#immunity',
    'ionic status immunity': 'Enternia#immunity',
    'impulse immunity': 'Ceternia#immunity',
    'plasma immunity': 'Alternia#immunity',
    'ionic immunity': 'Enternia#immunity',

    'tsyntex process': 'Gheatsyn#crystals',
    'yonnur': 'Warped#yonnur',

    'alta technology': 'Alta#technology',
    'alta equipment': 'Alta#equipment',
    'alta robotic': 'Alta#robotics',
    'alta object': 'Alta#objects',
    'alta culture': 'Alta#culture',
    'alta faction': 'Alta#factions',
    'alta decoration': 'Alta#objects',
    'alta city decoration': 'Alta#objects',
    'alta lab decoration': 'Alta#objects',
    'alta ship decoration': 'Alta#objects',
    'alta capital decoration': 'Alta#objects',
    'alta citadel decoration': 'Alta#objects',
    'alta food': 'Alta#food',
    'alta cuisine': 'Alta#food',
    'runeva cuisine': 'Alta#runeva',
    'calin cuisine': 'Alta#calin',
    'nia cuisine': 'Alta#nia',
    'yava cuisine': 'Alta#yava',
    'runeva alta cuisine': 'Alta#runeva',
    'calin alta cuisine': 'Alta#calin',
    'nia alta cuisine': 'Alta#nia',
    'yava alta cuisine': 'Alta#yava',
    'calin decor': 'Calin#decorative',
    'bishyn decor': 'Bishyn#decorative',
    'hevika decor': 'Hevika#decorative',
    'gheatsyn decor': 'Gheatsyn#decorative',
    'EDS Objects': 'EDS#objects',

    'C.T.': 'Project-Ceterai',
    'Ghearun': 'Gheatsyn#ghearun',
    'Hevika Ordis': 'Hevika#hevika-ordis',
    'Arco': 'A.R.C.O. Research',
    'A.R.C.O.': 'A.R.C.O. Research',
    'Unika': 'Alta#unika',
    'Perizhad': 'Alta#perizhad',
    'Tserera': 'Alta#tserera',
    'Elin': 'Elin-Gardens',

    'Arcolar': 'Alta#culture',
    'Ectolar': 'EDS#visual-style',
    'Seturna': 'Bishyn#visual-style',

    'Hevikai Incident': 'Hevika#hevikai-incident',
    'Gheatsyn Guardians': 'Gheatsyn#guardians',
    'energy tool': 'Weapons',
    'Faradea legend': 'Faradea#legends',
}

ICONS = {
    'antorash': ROOT + '/interface/bookmarks/icons/ct_alterash_planet.png',
    'evarus': ROOT + '/interface/bookmarks/icons/ct_alterash_planet.png',
    'esetera': ROOT + '/interface/bookmarks/icons/ct_alterash_prime_planet.png',
    'evarus prime': ROOT + '/interface/bookmarks/icons/ct_alterash_prime_planet.png',
    'ion core': ROOT + '/items/active/unsorted/alta/loot/ct_ion_core_loot.png',
    'verriskoywa': ROOT + '/objects/biome/alterash/koywa/grass/bushy/icon.png',
    'alterash planet': ROOT + '/interface/bookmarks/icons/ct_alterash_planet.png',
    'alterash prime planet': ROOT + '/interface/bookmarks/icons/ct_alterash_prime_planet.png',

    'alta decoration': ROOT + '/objects/alta/basic/flag/icon.png',
    'alta lab decoration': ROOT + '/objects/alta/lab/bed/icon.png',
    'alta city decoration': ROOT + '/objects/alta/city/pyramid/icon.png',
    'alta ship decoration': ROOT + '/objects/alta/ship/pod/icon.png',
    'calin decor': ROOT + '/objects/biome/alterash_prime/calin/decorative/ct_calin_terminal/icon.png',
    'bishyn decor': ROOT + '/objects/biome/alterash_prime/bishyn/decorative/ct_bishyn_terminal/icon.png',
    'hevika decor': ROOT + '/objects/biome/alterash_prime/hevika/decorative/ct_hevika_terminal/icon.png',
    'gheatsyn decor': ROOT + '/objects/biome/alterash_prime/gheatsyn/decorative/ct_gheatsyn_terminal/icon.png',
    'EDS Objects': ROOT + '/objects/alta/eds/decorative/terminal/icon.png',

    'Ghearun': ROOT + '/items/active/unsorted/alta/loot/sets/ct_ghearun_set.png',
    'Hevika Ordis': ROOT + '/items/active/unsorted/alta/loot/ct_hevika_loot.png',
    'Arco': ROOT + '/items/active/unsorted/alta/loot/sets/ct_arco_set.png',
    'A.R.C.O.': ROOT + '/items/active/unsorted/alta/loot/sets/ct_arco_set.png',

    'Hevikai Incident': ROOT + '/codex/alta/datamass/hevika.png',
    'Gheatsyn Guardians': ROOT + '/items/active/unsorted/ct_alta_spawner/ct_gheatsyn_droid.png',

    'impulse status immunity': ROOT + '/stats/effects/ct_impulse_block.png',
    'plasma status immunity': ROOT + '/stats/effects/ct_plasma_block.png',
    'ionic status immunity': ROOT + '/stats/effects/ct_ionicblockade.png',
    'impulse immunity': ROOT + '/stats/effects/ct_impulse_block.png',
    'plasma immunity': ROOT + '/stats/effects/ct_plasma_block.png',
    'ionic immunity': ROOT + '/stats/effects/ct_ionicblockade.png',
}

WIKI_LINKS = {
    # Custom
    'prism shard': ("Prism Shard", "https://starbounder.org/Prism_Shard", "https://starbounder.org/mediawiki/images/c/c0/Prism_Shard.png", 10, 10),
    'prism crystal': ("Prism Crystal", "https://starbounder.org/Prism_Shard", "https://starbounder.org/mediawiki/images/c/c0/Prism_Shard.png", 10, 10),
    'prism': ("Prism", "https://starbounder.org/Prism_Shard", "https://starbounder.org/mediawiki/images/c/c0/Prism_Shard.png", 10, 10),
    'Calotorn': ("Calotorn", "https://starbounder.org/Geode", "https://starbounder.org/mediawiki/images/4/43/Geode.png", 12, 11),
    'Crystalline': ("Crystalline", "https://starbounder.org/Crystalline", "https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/unsorted/alta/loot/ct_crystalline_prime_loot.png", 16, 16),
    'cloud': ("Cloud", "https://starbounder.org/Cloud", "https://starbounder.org/mediawiki/images/d/d2/Cloud.png", 16, 16),
    'electric resistance': ('Electric Resistance', 'https://starbounder.org/Electric_Resistance', 'https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png', 16, 16),
    'electricStatusImmunity': ('Electric Status Immunity', 'https://starbounder.org/Electric_Resistance', 'https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png', 16, 16),
    'electric immunity': ('Electric Immunity', 'https://starbounder.org/Electric_Resistance', 'https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png', 16, 16),
    'electrified': ('Electrified', 'https://starbounder.org/Electrified', 'https://starbounder.org/mediawiki/images/3/34/Status_Electrified.png', 16, 16),
    'ct_impulse': ('Impulse', 'Ceternia#damage', ROOT + '/damage/ct_impulse.png', 16, 16),
    'ct_plasma': ('Plasma', 'Alternia#damage', ROOT + '/damage/ct_plasma.png', 16, 16),
    'ct_ionic': ('Ionic', 'Enternia#damage', ROOT + '/damage/ct_ionic.png', 16, 16),
    'cal': ('Ionic', 'Calin', "https://starbounder.org/mediawiki/images/3/31/Crystal.png", 12, 16),
    'icecrystal': ("Ice Crystal", "https://starbounder.org/Ice_Crystal", "https://starbounder.org/mediawiki/images/c/ca/Ice_Crystal.png", 10, 16),
    'slime': ("Slime Blob", "https://starbounder.org/Slime_Blob", "https://starbounder.org/mediawiki/images/d/dc/Slime_Blob.png", 10, 14),

    # Items
    'prisiliteore': ("Prism Shard", "https://starbounder.org/Prism_Shard", "https://starbounder.org/mediawiki/images/c/c0/Prism_Shard.png", 10, 10),
    'crystal': ("Crystal", "https://starbounder.org/Crystal", "https://starbounder.org/mediawiki/images/3/31/Crystal.png", 12, 16),
    'diamond': ("Diamond", "https://starbounder.org/Diamond", "https://starbounder.org/mediawiki/images/e/ea/Diamond.png", 16, 16),
    'tungstenore': ('Tungsten Ore', 'https://starbounder.org/Tungsten_Ore', 'https://starbounder.org/mediawiki/images/6/6f/Tungsten_Ore.png', 10, 9),
    'titaniumore': ("Titanium", "https://starbounder.org/Titanium_Ore", "https://starbounder.org/mediawiki/images/3/34/Titanium_Ore.png", 16, 16),
    'durasteelore': ("Durasteel", "https://starbounder.org/Durasteel_Ore", "https://starbounder.org/mediawiki/images/d/d5/Durasteel_Ore.png", 16, 16),
    'aegisaltore': ("Aegisalt", "https://starbounder.org/Aegisalt_Ore", "https://starbounder.org/mediawiki/images/7/78/Aegisalt_Ore.png", 16, 16),
    'feroziumore': ("Ferozium", "https://starbounder.org/Ferozium_Ore", "https://starbounder.org/mediawiki/images/b/b8/Ferozium_Ore.png", 16, 16),
    'violiumore': ("Violium", "https://starbounder.org/Violium_Ore", "https://starbounder.org/mediawiki/images/3/3a/Violium_Ore.png", 16, 16),

    'titanium': ("Titanium Bar", "https://starbounder.org/Titanium_Bar", "https://starbounder.org/mediawiki/images/9/94/Titanium_Bar.png", 14, 13),
    'durasteel': ("Durasteel Bar", "https://starbounder.org/Durasteel_Bar", "https://starbounder.org/mediawiki/images/0/09/Durasteel_Bar.png", 14, 13),
    'titaniumbar': ("Titanium Bar", "https://starbounder.org/Titanium_Bar", "https://starbounder.org/mediawiki/images/9/94/Titanium_Bar.png", 14, 13),
    'durasteelbar': ("Durasteel Bar", "https://starbounder.org/Durasteel_Bar", "https://starbounder.org/mediawiki/images/0/09/Durasteel_Bar.png", 14, 13),
    'logblock': ('Wooden Log', 'https://starbounder.org/Wooden_Log', 'https://starbounder.org/mediawiki/images/d/d8/Wooden_Log.png', 16, 9),
    'plantfibre': ('Plant Fibre', 'https://starbounder.org/Plant_Fibre', 'https://starbounder.org/mediawiki/images/4/4f/Plant_Fibre.png', 14, 15),
    'greenslime': ('Slime Blob', 'https://starbounder.org/Slime_Blob', 'https://starbounder.org/mediawiki/images/d/dc/Slime_Blob.png', 10, 14),
    'volatilepowder': ('Volatile Powder', 'https://starbounder.org/Volatile_Powder', 'https://starbounder.org/mediawiki/images/b/b4/Volatile_Powder.png', 15, 12),
    'refinedaegisalt': ("Refined Aegisalt", "https://starbounder.org/Refined_Aegisalt", "https://starbounder.org/mediawiki/images/a/a0/Refined_Aegisalt.png", 13, 13),
    'refinedferozium': ("Refined Ferozium", "https://starbounder.org/Refined_Ferozium", "https://starbounder.org/mediawiki/images/8/82/Refined_Ferozium.png", 14, 14),
    'refinedviolium': ("Refined Violium", "https://starbounder.org/Refined_Violium", "https://starbounder.org/mediawiki/images/7/7d/Refined_Violium.png", 11, 11),

    'liquidwater': ("Water", "https://starbounder.org/Water", "https://starbounder.org/mediawiki/images/9/9d/Water.png", 16, 16),
    'liquidpoison': ("Poison", "https://starbounder.org/Poison", "https://starbounder.org/mediawiki/images/0/05/Poison.png", 16, 16),
    'liquidfuel': ("Liquid Erchius Fuel", "https://starbounder.org/Liquid_Erchius_Fuel", "https://starbounder.org/mediawiki/images/5/55/Liquid_Erchius_Fuel.png", 10, 14),
    
    'crystalplant': ("Crystal Plant", "https://starbounder.org/Crystal_Plant", "https://starbounder.org/mediawiki/images/f/f2/Crystal_Plant.png", 13, 12),
    'geode': ("Geode", "https://starbounder.org/Geode", "https://starbounder.org/mediawiki/images/4/43/Geode.png", 12, 11),

    'bluedye': ('Blue Dye', 'https://starbounder.org/Blue_Dye', 'https://starbounder.org/mediawiki/images/c/c9/Blue_Dye.png', 8, 12),
    'greendye': ('Green Dye', 'https://starbounder.org/Green_Dye', 'https://starbounder.org/mediawiki/images/b/be/Green_Dye.png', 8, 12),
    'purpledye': ('Purple Dye', 'https://starbounder.org/Purple_Dye', 'https://starbounder.org/mediawiki/images/9/99/Purple_Dye.png', 8, 12),
    'reddye': ('Red Dye', 'https://starbounder.org/Red_Dye', 'https://starbounder.org/mediawiki/images/c/c1/Red_Dye.png', 8, 12),
    'whitedye': ('White Dye', 'https://starbounder.org/White_Dye', 'https://starbounder.org/mediawiki/images/9/91/White_Dye.png', 8, 12),

    'money': ('Pixel', 'https://starbounder.org/Pixel', 'https://starbounder.org/mediawiki/images/2/21/Pixel.png', 12, 16),

    'syringe': ('Medical Syringe', 'https://starbounder.org/Medical_Syringe', 'https://starbounder.org/mediawiki/images/0/00/Medical_Syringe.png', 7, 15),
    'greenstim': ('Green Stim Pack', 'https://starbounder.org/Green_Stim_Pack', 'https://starbounder.org/mediawiki/images/0/04/Green_stim_pack.png', 7, 14),
    'bluestim': ('Blue Stim Pack', 'https://starbounder.org/Blue_Stim_Pack', 'https://starbounder.org/mediawiki/images/3/3a/Blue-Stim-Pack.png', 7, 14),

    'energyjavelin': ('Energy Javelin', 'https://starbounder.org/Energy_Javelin', 'https://starbounder.org/mediawiki/images/9/92/Energy_Javelin.png', 27, 3),
    'javelin': ('Javelin', 'https://starbounder.org/Javelin', 'https://starbounder.org/mediawiki/images/1/1d/Javelin.png', 27, 3),
    'throwingspear': ('Iron Hunting Spear', 'https://starbounder.org/Iron_Hunting_Spear', 'https://starbounder.org/mediawiki/images/1/19/Iron_Hunting_Spear.png', 16, 5),
    'throwingblock': ('Throwing Block', 'https://starbounder.org/Throwing_Block', 'https://starbounder.org/mediawiki/images/d/d3/Throwing_Block.png', 10, 10),

    'biosample': ("Bio Sample", "https://starbounder.org/Bio_Sample", "https://starbounder.org/mediawiki/images/4/40/Bio_Sample.png", 12, 9),
    'toxicwaste': ("Toxic Waste", "https://starbounder.org/Toxic_Waste", "https://starbounder.org/mediawiki/images/9/94/Toxic_Waste.png", 12, 13),
    'glowfibre': ("Glow Fibre", "https://starbounder.org/Glow_Fibre", "https://starbounder.org/mediawiki/images/f/f8/Glow_Fibre.png", 15, 14),

    'silk': ("Silk", "https://starbounder.org/Silk", "https://starbounder.org/mediawiki/images/8/83/Silk.png", 14, 14),
    'milk': ("Milk", "https://starbounder.org/Milk", "https://starbounder.org/mediawiki/images/9/92/Milk.png", 8, 15),
    'silkfibre': ("Silk Fibre", "https://starbounder.org/Silk_Fibre", "https://starbounder.org/mediawiki/images/9/9f/Silk_Fibre.png", 15, 14),
    'egg': ("Egg", "https://starbounder.org/Egg", "https://starbounder.org/mediawiki/images/2/26/Egg.png", 16, 16),
    'cheese': ("Cheese", "https://starbounder.org/Cheese", "https://starbounder.org/mediawiki/images/a/a5/Cheese.png", 12, 8),
    'fabric': ("Woven Fabric", "https://starbounder.org/Woven_Fabric", "https://starbounder.org/mediawiki/images/d/db/Woven_Fabric.png", 14, 12),
    'nanowrap': ("Nanowrap Bandage", "https://starbounder.org/Nanowrap_Bandage", "https://starbounder.org/mediawiki/images/7/7c/Nanowrap_Bandage.png", 16, 10),
    'alienwoodsap': ("Alien Wood Sap", "https://starbounder.org/Alien_Wood_Sap", "https://starbounder.org/mediawiki/images/9/95/Alien_Wood_Sap.png", 10, 14),

    'cryonicextract': ("Cryonic Extract", "https://starbounder.org/Cryonic_Extract", "https://starbounder.org/mediawiki/images/d/d0/Cryonic_Extract.png", 8, 16),
    'venomsample': ("Venom Sample", "https://starbounder.org/Venom_Sample", "https://starbounder.org/mediawiki/images/3/3d/Venom_Sample.png", 12, 13),
    'phasematter': ("Phase Matter", "https://starbounder.org/Phase_Matter", "https://starbounder.org/mediawiki/images/5/51/Phase_Matter.png", 13, 13),
    'livingroot': ("Living Root", "https://starbounder.org/Living_Root", "https://starbounder.org/mediawiki/images/c/c8/Living_Root.png", 14, 13),
    'staticcell': ("Static Cell", "https://starbounder.org/Static_Cell", "https://starbounder.org/mediawiki/images/6/6a/Static_Cell.png", 9, 14),
    'hardenedcarapace': ("Hardened Carapace", "https://starbounder.org/Hardened_Carapace", "https://starbounder.org/mediawiki/images/f/f2/Hardened_Carapace.png", 14, 10),
    'scorchedcore': ("Scorched Core", "https://starbounder.org/Scorched_Core", "https://starbounder.org/mediawiki/images/b/b1/Scorched_Core.png", 12, 11),

    'platinumdrill': ('Platinum Drill', 'https://starbounder.org/Platinum_Drill', 'https://starbounder.org/mediawiki/images/6/67/Platinum_Drill.png', 24, 11.25),
    'spaceorgan': ('Space Synth', 'https://starbounder.org/Space_Synth', 'https://starbounder.org/mediawiki/images/5/5c/Space_Synth.png', 18, 15),
    'squarewave': ('Square Wave', 'https://starbounder.org/Square_Wave', 'https://starbounder.org/mediawiki/images/1/1b/Square_Wave.png', 18, 15),

    'manipulatormodule': ('Manipulator Module', 'https://starbounder.org/Manipulator_Module', 'https://starbounder.org/mediawiki/images/6/68/Manipulator_Module.png', 10, 16),
    'techcard': ('Tech Card', 'https://starbounder.org/Tech_Card', 'https://starbounder.org/mediawiki/images/6/6f/Tech_Card.png', 14, 10),
    'upgrademodule': ('Upgrade Module', 'https://starbounder.org/Upgrade_Module', 'https://starbounder.org/mediawiki/images/2/2e/Upgrade_Module.png', 16, 15),

    'crystalbackpackback': ("Crystal Backpack", "https://starbounder.org/Crystal_Backpack", "https://starbounder.org/mediawiki/images/9/93/Crystal_Backpack_Icon.png", 16, 16),
    'minerhead': ("Miner's Helmet", "https://starbounder.org/Miner%27s_Helmet", "https://starbounder.org/mediawiki/images/3/3b/Miner%27s_Helmet_Icon.png", 16, 16),
    'minerchest': ("High-Vis Jacket", "https://starbounder.org/High-Vis_Jacket", "https://starbounder.org/mediawiki/images/3/32/High-Vis_Jacket_Icon.png", 16, 16),

    # Objects
    'hivebed': ('Hive Bed', 'https://starbounder.org/Hive_Bed', 'https://starbounder.org/mediawiki/images/3/35/Hive_Bed.png', 18.5, 5.5),
    'hivechair': ('Hive Chair', 'https://starbounder.org/Hive_Chair', 'https://starbounder.org/mediawiki/images/2/2d/Hive_Chair.png', 11.25, 7.5),
    'hivedoor': ('Hive Door', 'https://starbounder.org/Hive_Door', 'https://starbounder.org/mediawiki/images/f/f0/Hive_Door.png', 4.5, 15),
    'hivelamp': ('Hive Lamp', 'https://starbounder.org/Hive_Lamp', 'https://starbounder.org/mediawiki/images/e/e0/Hive_Lamp.png', 5.25, 10.5),
    'hivetable': ('Hive Table', 'https://starbounder.org/Hive_Table', 'https://starbounder.org/mediawiki/images/1/14/Hive_Table.png', 15, 6),

    'crystalbed': ('Crystal Bed', 'https://starbounder.org/Crystal_Bed', 'https://starbounder.org/mediawiki/images/a/a6/Crystal_Bed.png', 18, 9),
    'crystalchair': ('Crystal Chair', 'https://starbounder.org/Crystal_Chair', 'https://starbounder.org/mediawiki/images/1/10/Crystal_Chair.png', 6, 9),
    'crystalchest': ('Crystal Chest', 'https://starbounder.org/Crystal_Chest', 'https://starbounder.org/mediawiki/images/d/de/Crystal_Chest.png', 12, 10.5),
    'crystallamp': ('Crystal Lamp', 'https://starbounder.org/Crystal_Lamp', 'https://starbounder.org/mediawiki/images/0/0b/Crystal_Lamp.png', 8, 12),
    'crystaltable': ('Crystal Table', 'https://starbounder.org/Crystal_Table', 'https://starbounder.org/mediawiki/images/4/48/CrystalTable.png', 15, 6),

    'largecooler1': ('Large Cooler', 'https://starbounder.org/Large_Cooler', 'https://starbounder.org/mediawiki/images/1/10/Large_Cooler.png', 12, 6),
    'tier3light': ('Titanium Light', 'https://starbounder.org/Titanium_Light', 'https://starbounder.org/mediawiki/images/f/f0/Titanium_Light.png', 6, 10.5),
    'tier3chair': ('Titanium Chair', 'https://starbounder.org/Titanium_Chair', 'https://starbounder.org/mediawiki/images/9/9e/Titanium_Chair.png', 9, 8),
    'tier3door': ('Titanium Door', 'https://starbounder.org/Titanium_Door', 'https://starbounder.org/mediawiki/images/1/1c/Titanium_Door.png', 5, 10),
    'tier3switch': ('Titanium Console', 'https://starbounder.org/Titanium_Console', 'https://starbounder.org/mediawiki/images/4/47/Titanium_Console.gif', 8.5, 6),
    'tier3table': ('Titanium Table', 'https://starbounder.org/Titanium_Table', 'https://starbounder.org/mediawiki/images/2/22/Titanium_Table.png', 15, 6),
    'tier3bed': ('Titanium Bed', 'https://starbounder.org/Titanium_Bed', 'https://starbounder.org/mediawiki/images/3/3f/Titanium_Bed.png', 18, 5.25),
    'prismlamp1': ('Prism Magenta Lamp', 'https://starbounder.org/Prism_Magenta_Lamp', 'https://starbounder.org/mediawiki/images/3/3e/Prism_Magenta_Lamp.png', 6, 10.5),
    'prismlamp2': ('Prism Emerald Lamp', 'https://starbounder.org/Prism_Emerald_Lamp', 'https://starbounder.org/mediawiki/images/0/07/Prism_Emerald_Lamp.png', 6, 8),
    'prismlamp3': ('Prism Cyan Lamp', 'https://starbounder.org/Prism_Cyan_Lamp', 'https://starbounder.org/mediawiki/images/9/93/Prism_Cyan_Lamp.png', 6, 10.5),

    'podchest': ('Pod Chest', 'https://starbounder.org/Pod_Chest', 'https://starbounder.org/mediawiki/images/0/00/Pod_Chest.png', 8.75, 5),
    'apextablelamp': ('Green Lamp Pod', 'https://starbounder.org/Green_Lamp_Pod', 'https://starbounder.org/mediawiki/images/f/fd/Green_Lamp_Pod.png', 8, 8),
    'futurelight': ('Cheap Light', 'https://starbounder.org/Cheap_Light', 'https://starbounder.org/mediawiki/images/c/cf/Cheap_Light.png', 6, 9),
    'electricdoor': ('Electrical Barrier', 'https://starbounder.org/Electrical_Barrier', 'https://starbounder.org/mediawiki/images/d/d3/Electrical_Barrier.gif', 3, 15),
    'outpoststandingdesk': ('Standing Desk', 'https://starbounder.org/Standing_Desk', 'https://starbounder.org/mediawiki/images/e/e4/Standing_Desk.png', 6, 6),
    'outposttable': ('Basic Metal Table', 'https://starbounder.org/Basic_Metal_Table', 'https://starbounder.org/mediawiki/images/9/9e/Basic_Metal_Table.png', 17.25, 6),
    'bluelight': ('Blue Light', 'https://starbounder.org/Blue_Light', 'https://starbounder.org/mediawiki/images/f/f9/Blue_Light.png', 6, 0.75),
    'outdoorbench': ("Outdoor Bench", "https://starbounder.org/Outdoor_Bench", "https://starbounder.org/mediawiki/images/5/5d/Outdoor_Bench.png", 24, 6),

    'poptopplush': ("Poptop Plushie", "https://starbounder.org/Poptop_Plushie", "https://starbounder.org/mediawiki/images/b/bd/Poptop_Plushie.png", 12, 11),
    'bearplush': ("Bear Plushie", "https://starbounder.org/Bear_Plushie", "https://starbounder.org/mediawiki/images/f/f5/Bear_Plushie.png", 10.5, 11.5),
    'badgooplush': ("Bad Goo Plushie", "https://starbounder.org/Bad_Goo_Plushie", "https://starbounder.org/mediawiki/images/3/38/Bad_Goo_Plushie.png", 12, 8),
    'mindwurmplush': ("Mindwurm Plushie", "https://starbounder.org/Mindwurm_Plushie", "https://starbounder.org/mediawiki/images/a/a2/Mindwurm_Plushie.png", 12, 12),
    'numiplush': ("Numi Plushie", "https://starbounder.org/Numi_Plushie", "https://starbounder.org/mediawiki/images/e/ef/Numi_Plushie.png", 12, 12),
    'turtleplush': ("Turtle Plushie", "https://starbounder.org/Turtle_Plushie", "https://starbounder.org/mediawiki/images/3/30/Turtle_Plushie.png", 11, 12),
    'plainorbplush': ("Virorb Plushie", "https://starbounder.org/Virorb_Plushie", "https://starbounder.org/mediawiki/images/6/6c/Virorb_Plushie.png", 12, 10),

    'industrialbed': ("Industrial Bed", "https://starbounder.org/Industrial_Bed", "https://starbounder.org/mediawiki/images/8/82/Industrial_Bed.png", 28, 10),
    'industrialcanister': ("Industrial Canister", "https://starbounder.org/Industrial_Canister", "https://starbounder.org/mediawiki/images/1/1a/Industrial_Canister.png", 6, 12),
    'industrialchair': ("Industrial Chair", "https://starbounder.org/Industrial_Chair", "https://starbounder.org/mediawiki/images/c/c4/Industrial_Chair.png", 6, 10),
    'industrialcomputer': ("Industrial Computer", "https://starbounder.org/Industrial_Computer", "https://starbounder.org/mediawiki/images/d/d6/Industrial_Computer.gif", 12, 12),
    'industrialcrate': ("Industrial Crate", "https://starbounder.org/Industrial_Crate", "https://starbounder.org/mediawiki/images/0/07/Industrial_Crate.png", 15, 12),
    'industrialdisplay': ("Industrial Display", "https://starbounder.org/Industrial_Display", "https://starbounder.org/mediawiki/images/b/b8/Industrial_Display.gif", 21, 12),
    'industrialdoor': ("Industrial Door", "https://starbounder.org/Industrial_Door", "https://starbounder.org/mediawiki/images/a/ac/Industrial_Door.png", 6, 15),
    'industriallight': ("Industrial Light", "https://starbounder.org/Industrial_Light", "https://starbounder.org/mediawiki/images/e/ec/Industrial_Light.png", 12, 6),
    'industrialstoragelocker': ("Industrial Storage Locker", "https://starbounder.org/Industrial_Storage_Locker", "https://starbounder.org/mediawiki/images/6/61/Industrial_Storage_Locker.png", 12, 9),
    'industrialtable': ("Industrial Table", "https://starbounder.org/Industrial_Table", "https://starbounder.org/mediawiki/images/b/b6/Industrial_Table.png", 24, 12),

    'giantflowerchest': ('Giant Flower Chest', 'https://starbounder.org/Giant_Flower_Chest', 'https://starbounder.org/mediawiki/images/b/ba/Giant_Flower_Chest.png', 12, 9.75),
    'toxicchest': ('Toxic Chest', 'https://starbounder.org/Toxic_Chest', 'https://starbounder.org/mediawiki/images/c/c4/Toxic-Chest.png', 12, 12),
    'alienchest': ('Alien Chest', 'https://starbounder.org/Alien_Chest', 'https://starbounder.org/mediawiki/images/3/35/Alien_Chest.png', 12, 9.75),
    'techchest': ('Hi-Tech Chest (Blue)', 'https://starbounder.org/Hi-Tech_Chest_(Blue)', 'https://starbounder.org/mediawiki/images/9/9f/Hi-Tech_Chest_%28Blue%29.png', 12, 9),
    'techchest2': ('Hi-Tech Chest (Green)', 'https://starbounder.org/Hi-Tech_Chest_(Green)', 'https://starbounder.org/mediawiki/images/8/88/Hi-Tech_Chest_%28Green%29.png', 12, 9),
    'miningchest': ('Mining Chest', 'https://starbounder.org/Mining_Chest', 'https://starbounder.org/mediawiki/images/4/4f/Mining_Chest.png', 18, 12),
    'slimehide': ('Slime Chest', 'https://starbounder.org/Slime_Chest', 'https://starbounder.org/mediawiki/images/d/da/Slime_Chest.png', 12, 9),
    'rainbowchest': ('Rainbow Chest', 'https://starbounder.org/Rainbow_Chest', 'https://starbounder.org/mediawiki/images/a/a9/Rainbowchest.png', 12, 12),

    # Biome Objects
    'capsulesmall': ('Small Capsule', 'https://starbounder.org/Small_Capsule', 'https://starbounder.org/mediawiki/images/b/b9/Small_Capsule.png', 10, 10),
    'capsulemed': ('Medium Capsule', 'https://starbounder.org/Medium_Capsule', 'https://starbounder.org/mediawiki/images/e/e0/Medium_Capsule.png', 10, 12),
    'capsulebig': ('Large Capsule', 'https://starbounder.org/Large_Capsule', 'https://starbounder.org/mediawiki/images/8/83/Large_Capsule.png', 10, 16),
    'statuspod': ('Status Pod', 'https://starbounder.org/Status_Pod', 'https://starbounder.org/mediawiki/images/d/de/Status_Pod.gif', 8, 16),
    'prismrock1': ('Small Prism Crystal', 'https://starbounder.org/Prism_Shard', 'https://starbounder.org/mediawiki/images/c/c0/Prism_Shard.png', 10, 10),
    'prismrock2': ('Rigid Prism Crystal', 'https://starbounder.org/Prism_Shard', 'https://starbounder.org/mediawiki/images/c/c0/Prism_Shard.png', 10, 10),
    'prismrock3': ('Fragile Prism Crystal', 'https://starbounder.org/Prism_Shard', 'https://starbounder.org/mediawiki/images/c/c0/Prism_Shard.png', 10, 10),
    'flowerblue': ('Blue Flower', 'https://starbounder.org/Blue_Flower', 'https://starbounder.org/mediawiki/images/9/9d/Blue_Flower.png', 10, 16),
    'flowerred': ('Red Flower', 'https://starbounder.org/Red_Flower', 'https://starbounder.org/mediawiki/images/3/31/Red_Flower.png', 8, 16),
    'crystallinebush1': ('Crystalline Bush', 'https://starbounder.org/Crystalline_Bush', 'https://starbounder.org/mediawiki/images/0/0e/Crystalline_Bush.png', 16.5, 12),
    'crystallinebush2': ('Crystalline Bush 2', 'https://starbounder.org/Crystalline_Bush_(2)', 'https://starbounder.org/mediawiki/images/8/8d/Crystalline_Bush2.png', 15, 12),
    'crystallinebush3': ('Crystalline Bush 3', 'https://starbounder.org/Crystalline_Bush_(3)', 'https://starbounder.org/mediawiki/images/6/65/Crystalline_Bush3.png', 12, 12),
    'crystallinebush4': ('Crystalline Bush 4', 'https://starbounder.org/Crystalline_Bush_(4)', 'https://starbounder.org/mediawiki/images/6/65/Crystalline_Bush4.png', 12, 12),
    'crystalcavebush1': ('Crystal Deposit', 'https://starbounder.org/Crystalline_Bush', 'https://starbounder.org/mediawiki/images/archive/0/0e/20151127192824%21Crystalline_Bush.png', 18, 12),
    'crystalcavebush2': ('Crystal Deposit 2', 'https://starbounder.org/Crystalline_Bush_(2)', 'https://starbounder.org/mediawiki/images/archive/8/8d/20151127192816%21Crystalline_Bush2.png', 18, 12),
    'crystalcavebush3': ('Crystal Deposit 3', 'https://starbounder.org/Crystalline_Bush_(3)', 'https://starbounder.org/mediawiki/images/archive/6/65/20151127192810%21Crystalline_Bush3.png', 12, 12),
    'crystalcavebush4': ('Crystal Deposit 4', 'https://starbounder.org/Crystalline_Bush_(4)', 'https://starbounder.org/mediawiki/images/archive/6/65/20151127192803%21Crystalline_Bush4.png', 12, 12),

    'crystalplantseed': ("Crystal Plant Seed", "https://starbounder.org/Crystal_Plant_Seed", "https://starbounder.org/mediawiki/images/0/01/Crystal_Plant_Crop.png", 15, 14),
    'wildcrystalplantseed': ("Crystal Plant Seed", "https://starbounder.org/Crystal_Plant_Seed", "https://starbounder.org/mediawiki/images/0/01/Crystal_Plant_Crop.png", 15, 14),
    'beakseedseed': ("Beakseed Seed", "https://starbounder.org/Beakseed_Seed", "https://starbounder.org/mediawiki/images/c/c6/Beakseed_Crop.png", 6, 12.25),
    'wildbeakseedseed': ("Beakseed Seed", "https://starbounder.org/Beakseed_Seed", "https://starbounder.org/mediawiki/images/c/c6/Beakseed_Crop.png", 6, 12.25),

    'ceilingspike1': ("Ceiling Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'ceilingspike2': ("Ceiling Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'ceilingspike3': ("Ceiling Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'ceilingspike4': ("Ceiling Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'groundspike1': ("Ground Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'groundspike2': ("Ground Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'groundspike3': ("Ground Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'groundspike4': ("Ground Spike", "https://starbounder.org/Bone_Spike", "https://starbounder.org/mediawiki/images/a/a9/Bone_Spike.png", 6, 12),
    'teslaspike': ("Tesla Spike", "https://starbounder.org/Tesla_Spike", "https://starbounder.org/mediawiki/images/b/bf/Tesla_Spike.png", 12, 12),
    'bioshroom1': ("Bioshroom", "https://starbounder.org/Mushroom", "https://starbounder.org/mediawiki/images/8/8c/Mushroom.png", 16, 16),
    'bioshroom2': ("Bioshroom", "https://starbounder.org/Mushroom", "https://starbounder.org/mediawiki/images/8/8c/Mushroom.png", 16, 16),
    'bioshroom3': ("Bioshroom", "https://starbounder.org/Mushroom", "https://starbounder.org/mediawiki/images/8/8c/Mushroom.png", 16, 16),
    'bioshroom4': ("Bioshroom", "https://starbounder.org/Mushroom", "https://starbounder.org/mediawiki/images/8/8c/Mushroom.png", 16, 16),
    'bioshroom5': ("Bioshroom", "https://starbounder.org/Mushroom", "https://starbounder.org/mediawiki/images/8/8c/Mushroom.png", 16, 16),

    # Blocks
    'cloudblock': ("Cloud", "https://starbounder.org/Cloud", "https://starbounder.org/mediawiki/images/d/d2/Cloud.png", 16, 16),
    'obsidian': ("Obsidian", "https://starbounder.org/Obsidian", "https://starbounder.org/mediawiki/images/2/23/Obsidian.png", 10, 10),
    'snow': ('Snow', 'https://starbounder.org/Snow', 'https://starbounder.org/mediawiki/images/4/4e/Snow.png', 10, 10),
    'slush': ('Slush', 'https://starbounder.org/Slush', 'https://starbounder.org/mediawiki/images/6/64/Slush.png', 10, 10),
    'frozenwater': ('Smooth Ice', 'https://starbounder.org/Smooth_Ice', 'https://starbounder.org/mediawiki/images/b/b4/Smooth_Ice.png', 12, 12),
    'ice': ('Ice', 'https://starbounder.org/Ice', 'https://starbounder.org/mediawiki/images/7/77/Ice.png', 10, 10),
    'waste': ('Waste', 'https://starbounder.org/Waste', 'https://starbounder.org/mediawiki/images/1/12/Waste.png', 10, 10),

    'moondust': ("Moondust", "https://starbounder.org/Moondust", "https://starbounder.org/mediawiki/images/f/fc/Moondust.png", 10, 10),
    'moonrock': ("Moonrock", "https://starbounder.org/Moonrock", "https://starbounder.org/mediawiki/images/b/b8/Moonrock.png", 10, 10),
    'moonstone': ("Moonstone", "https://starbounder.org/Moonstone", "https://starbounder.org/mediawiki/images/b/b6/Moonstone.png", 10, 10),
    'rock14': ("Granite Rock", "https://starbounder.org/Granite_Rock", "https://starbounder.org/mediawiki/images/e/eb/Granite_Rock.png", 12, 12),
    'crystalblock': ("Crystal Block", "https://starbounder.org/Crystal_Block", "https://starbounder.org/mediawiki/images/9/93/Crystal_Block.png", 14, 13),

    # Loot tables
    'luminousCaveChestTreasure': ("Luminous Cave Chest Treasure", "https://starbounder.org/Treasure/Biome/Underground#Underground_Luminous_Chest_Treasure", "https://starbounder.org/mediawiki/images/e/e9/Glow_Chest.png", 12, 10.5),
    'crystalChestTreasure': ("Crystal Chest Treasure", "https://starbounder.org/Crystal_Chest", "https://starbounder.org/mediawiki/images/d/de/Crystal_Chest.png", 12, 10.5),
    'luminousCaveTreasure': ("Luminous Cave Treasure", "https://starbounder.org/Treasure/Biome/Underground#Underground_Luminous_Chest_Treasure", "https://starbounder.org/mediawiki/images/e/e9/Glow_Chest.png", 12, 10.5),
    'crystalTreasure': ("Crystal Treasure", "https://starbounder.org/Crystal_Chest", "https://starbounder.org/mediawiki/images/d/de/Crystal_Chest.png", 12, 10.5),

    'weapon': ('Weapon Treasure', 'https://starbounder.org/Treasure#Weapon', 'https://starbounder.org/mediawiki/images/2/20/Weapon_Chest.png', 18, 10.5),
    'costume': ('Costume Treasure', 'https://starbounder.org/Treasure#Costume', 'https://starbounder.org/mediawiki/images/9/93/Crystal_Backpack_Icon.png', 16, 16),
    'tool': ('Instrument Treasure', 'https://starbounder.org/Tool_(treasure)', 'https://starbounder.org/mediawiki/images/6/67/Platinum_Drill.png', 24, 11.25),

    # Grass
    'grass-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),
    'testflower-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),
    'testflower2-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),
    'testflower3-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),
    'testflower4-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),
    'testflower5-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),
    'testflower6-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),
    'testflower7-grass': ('Grass', 'https://starbounder.org/Grass', 'https://starbounder.org/mediawiki/images/e/ef/Grass_Seeds.png', 9, 12),

    # Radio
    'pickupseed': ("I see that you've discovered some seeds. I suggest planting them in some tilled soil, and watering them until they grow. The tools you need can be built at a foraging table.", None, 0, 0),
    'pickupflag': ("I am able to reconfigure the ship's teleporter to teleport directly to the location marked by this flag. Place and interact with the flag to establish a name.", None, 0, 0),
    'pickupcoal': ("You discovered coal! You can turn coal into torches to light your way. The chance of fatal incidents is dramatically increased in the dark. Explore the crafting menu.", None, 0, 0),
    'pickupore': ("You discovered some ore. Ore can be turned into bars using a furnace, bars are useful for crafting a wide range of equipment that may increase your life expectancy.", None, 0, 0),
    'pickupcorefrag': ("You discovered a core fragment! These are useful objects. I estimate that you will require at least 20 of them.", None, 0, 0),
    'pickupplantfibre': ("You discovered some plant fibre. This can be woven into useful fabrics at a spinning wheel.", None, 0, 0),
    'pickupdye': ("You discovered dye. With these you can colour your attire to your liking. You can apply one to any piece of armour or clothing with a right-click.", None, 0, 0),
    'pickupepp': ("You obtained an Enviro Protection Pack (EPP). These specialised devices enable the user to survive in otherwise inhospitable environments. You can also enhance EPPs with augments.", None, 0, 0),
    'pickupaugment': ("You obtained an augment. These modules can provide a wide range of benefits. Install them to an Enviro Protection Pack (EPP) with a right-click.", None, 0, 0),
    'pickupcollar': ("You discovered a collar. When worn by a tamed monster, these collars can provide a wide range of benefits. You can add them to a filled capture pod with a right-click.", None, 0, 0),
}

WIKI_ICONS = {
    '/interface/statuses/nova.png': ("https://starbounder.org/mediawiki/images/6/65/Status_Nova.png", 16, 16),
    '/interface/statuses/swimboost.png': ("https://starbounder.org/mediawiki/images/b/b6/Status_Swim_Boost.png", 16, 16),
    '/interface/statuses/jumpboost.png': ("https://starbounder.org/mediawiki/images/8/85/Status_Jump_Boost_2.png", 16, 16),
}
