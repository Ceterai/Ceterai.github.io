def link(name: str, url: str, img: str, w: int = 16, h: int = 16):
    return f'<img src="{img}" width="{w}" height="{h}"/> [{name}]({url})'
def lnk(name: str, img: str, w: int = 16, h: int = 16):
    source = 'https://starbounder.org/'
    return f'<img src="{img}" width="{w}" height="{h}"/> [{name}]({source}{name.replace(" ", "_")})'
# <img src="([^\s]*)" width="([^\s]*)" height="([^\s]*)"\/> \[(.*)\]\(([^\s]*)\)'
# {link("$4", "$5", "$1", $2, $3)}'

MOD_NAME = 'My Enternia'

CATEGORIES = {
    'monsters': {
        'monster list': {
            'organicmonster': 'organic monster',
            'roboticmonster': 'robotic monster',
            'othermonster': 'persistent creature',
        },
    },
    'projectiles': {
        'projectile list': {
            'projectile': 'projectile',
        },
    },
    'plants': {
        'plant list': {
            'bush': 'bush',
            'grass': 'grass',
            'sapling': 'tree',
            'treetop': 'foliage',
            'treestem': 'stem',
        },
    },
    'items': {
        'generic items': {
            'craftingMaterial': 'crafting material',
            'cookingIngredient': 'cooking ingredient',
        },
        'enhancement items': {
            'eppAugment': 'EPP augment',
            'petCollar': 'pet collar',
        },
        'consumable items': {
            'food': 'food item',
            'medicine': 'medicine item',
            'preparedFood': 'prepared food item',
            'drink': 'drink',
        },
        'throwable items': {
            'throwableItem': 'throwable item',
            'spawner': 'monster spawner',  # Custom Category Example
        },
        'loot items': {
            'mysteriousReward': 'reward item',
            'loot': 'loot crate item',  # Custom Category Example
            'gsr': 'special loot pod',  # Custom Category Example
            'set': 'equipment set',  # Custom Category Example
        },
        'active items': {
            'shield': 'shield',

            'uniqueWeapon': 'unique weapon',
            'shotgun': 'shotgun',
            'rocketLauncher': 'rocket launcher',
            'grenadeLauncher': 'grenade launcher',
            'sniperRifle': 'sniper rifle',
            'machinePistol': 'machine pistol',
            'assaultRifle': 'assault rifle',
            'pistol': 'pistol',
            'chakram' : 'chakram',
            'boomerang' : 'boomerang',
            'toy' : 'toy',
            'tool' : 'tool',

            'spear': 'spear',
            'broadsword': 'broadsword',
            'shortsword': 'shortsword',
            'axe': 'axe',
            'whip': 'whip',
        },
        'clothing': {
            'chestarmour': 'chest armor',
            'headarmour': 'head armor',
            'legarmour': 'leg armor',
            'chestwear': 'chestwear',
            'headwear': 'headwear',
            'legwear': 'legwear',
            'backwear': 'backwear',
            'enviroProtectionPack': 'EPP',
        },
        'codexes': {
            'codex': 'codex item',
        },
    },
    'objects': {
        'object list': {
            'decorative': 'decorative object',
            'furniture': 'furniture object',
            'storage': 'storage object',
            'fridgeStorage': 'fridge',
            'light': 'light',
            'door': 'door',
            'wire': 'wired object',
            'crafting': 'crafting object',
            'teleporter': 'teleporter',
            'teleportMarker': 'teleportation marker',
            'actionFigure': 'action figure',
            'breakable': 'breakable',
            'trap': 'trap',
            'seed': 'farmable',
            'sapling': 'sapling',
            'other': 'other',
        },
    },
    'status effects': {
        'status effect list': {
            'statuseffect': 'status effect',
        },
    },
    'biomes': {
        'biome list': {
            'planetarybiome': 'planetary biome',
            'minibiome': 'minibiome',
            'cavebiome': 'cave minibiome',
        },
    },
    'weather': {
        'weather list': {
            'weather': 'weather type',
        },
    },
    'species': {
        'species list': {
            'species': 'specie',
        },
    },
}
flat_cats: dict[str, str] = {}
for m in CATEGORIES:
    for s in CATEGORIES[m]:
        flat_cats.update(CATEGORIES[m][s])

PATHS = [
    'monsters',
    'projectiles',
    'plants',
    'stats',
    'codex',
    'biomes',
    'weather',
    'objects',
    'items',
    'species',
]

LOOT_PATHS = [
    'treasure',
]

RECIPE_PATHS = [
    'recipes',
]

CHEST_PATHS = [
    'treasure',
]

RADIO_PATHS = [
    'radiomessages',
]

ROOT_SOURCE = 'D://Apps/Steam/steamapps/common/Starbound/mods/Enternia'
ROOT_TARGET = 'D://Dev/GitHub/Pages'
ROOT_TARGET_DND = '/MyEnternia/DnD'
ROOT_TARGET_WIKI = '/MyEnternia/Wiki'
ROOT_TARGET_TOML = '/MyEnternia/assets'
ROOT_REPO = 'https://raw.githubusercontent.com/Ceterai/Enternia/main'
ROOT_REPO_FILES = 'https://github.com/Ceterai/Enternia/blob/main'
COCKPIT_CONFIG = '/interface/cockpit/cockpit.config.patch'  # Custom Path Example
SKIPPED_EXTS = (
    'weaponability',
    'monsterpart',
    'animation',
    'parallax',
    'frames',
    'config',
    'png',
    'lua',
    'txt',
    'raceeffect',
    'default',
)
