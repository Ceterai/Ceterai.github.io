import toml, json

import config
import md
import db
import load
import resources


class File:
    def __init__(self, root, web, dir, name, ext, link_name, icon):
        self.root = root
        self.web = web.replace(' ', '%20')
        self.name = name.replace(' ', '%20')
        self.ext = ext
        self.file = f'{self.name}.{self.ext}'

        self.rdir = dir.replace(' ', '%20')
        self.fdir = f'{self.web}{self.rdir}'

        self.rpath = f'{self.rdir}/{self.file}'
        self.fpath = f'{self.web}{self.rpath}'

        self.full = f'{self.root}{self.fpath}'
        self.link = md.item(link_name, self.fpath, icon)


class Element:
    def __init__(self, element, name, advantage):
        self.base = element
        self.type = None
        self.strong = None
        self.energy = None
        if element == 'electric':
            if 'puls' in md.mini(name):
                self.type = 'impulse'
                self.strong = 'lightning'
                self.energy = 'ceternia'
            if 'plasm' in md.mini(name) or 'energ' in md.mini(name):
                self.type = 'plasma'
                self.strong = 'fireplasma'
                self.energy = 'alternia'
            if 'ion' in md.mini(name):
                self.type = 'ionic'
                self.strong = 'static'
                self.energy = 'enternia'
        if 'energ' in md.mini(name):
            self.energy = 'alternia'
        self.advantage = advantage


class Spawner:
    def __init__(self, entities, stats):
        self.entities = sorted(tuple(e for e in (set(entities)) if e))
        self.stats = stats
        self.raw = {'entities': self.entities, 'stats': self.stats} if self.entities else None


class Wiki:
    def __init__(self, raw: dict):
        self.raw = raw.copy()
        if 'related' in self.raw:
            self.raw['related'] = json.dumps(self.raw['related'])
        self.banner: str = raw.get('banner')
        self.md: dict[str, str] = raw.get('md')
        self.widgets: dict[str, list[dict[str]]] = raw.get('widgets')
        self.trivia: list[str] = raw.get('trivia')
        self.skip: bool = raw.get('skip')


class Ability:
    def __init__(self, raw: dict):
        raw = raw or {}
        self.name: str = raw.get('name')
        self.lore: str = raw.get('description')
        self.long: str = raw.get('longdescription')
        self.stats: dict[str] = {key: raw[key] for key in raw if key not in ('name', 'description', 'longdescription', 'type', 'class', 'scripts',)}
        if 'stances' in self.stats:
            self.stats.pop('stances')
        if 'steps' in self.stats:
            self.stats.pop('steps')
        if 'lazerParams' in self.stats:
            self.stats.pop('lazerParams')
        if 'lightningChargeLevels' in self.stats:
            self.stats.pop('lightningChargeLevels')
        self.raw = {
            'name': self.name,
            'lore': self.lore,
            'long': self.long,
            'stats': self.stats,
        } if self.name or self.stats else None


class Upgrade:
    def __init__(self, raw: dict, uid: str, uid_suffix: str, toml_path: str, file_name: str, icon: str):
        raw = raw or {}
        self.id: str = uid + (('-' + uid_suffix) if uid_suffix else '')
        self.suffix: str = uid_suffix
        self.name: str = md.star(md.clean(raw.get('shortdescription')))
        self.toml: str = md.item(self.name, toml_path.replace(file_name, md.urlf(self.name) or ''), icon)
        self.value: str = raw.get('chance', 0.1)
        self.raw = {
            'id': self.id,
            'name': self.name,
            'toml': self.toml,
            'value': self.value,
        } if self.name else None


class ItemExtractor():

    def __init__(self, file_path: str, pit: load.CockpitLib, chests: load.ChestLib, radio: load.RadioLib, bps: resources.RecipeLib, loot: resources.LootLib, child: str = None):
        self.raw = load.json(file_path)
        self.uid = self.get('itemName')

        self.cat = self.get_cat()
        self.type = self.get_type()

        self.file_path_full = file_path.replace('\\', '/')
        self.file_path = self.file_path_full.replace((config.ROOT_SOURCE), '')
        self.dir_path = '/'.join(self.file_path.split('/')[:-1])
        self.file_name = '.'.join(self.file_path.split('/')[-1].split('.')[:-1])
        self.file_ext = self.file_path.split('/')[-1].split('.')[-1]
        self.file_link = f'{config.ROOT_REPO_FILES}{self.file_path}'.replace(' ', '%20')
        self.repo = File('', config.ROOT_REPO_FILES, self.dir_path, self.file_name, self.file_ext, md.qs(self.file_path), None)

        self.name = md.star(md.clean(self.get('shortdescription')))
        self.icon = md.icon(self.get_obj_icon_link())

        self.urlf = md.urlf(md.clean(self.get('shortdescription')))
        self.toml = File(config.ROOT_TARGET, config.ROOT_TARGET_TOML, '/items', self.urlf, 'toml', self.name, self.icon)
        self.wiki = File(config.ROOT_TARGET, config.ROOT_TARGET_WIKI, f'/items/{self.cat}', self.urlf, 'md', self.name, self.icon)
        self.meta = Wiki(self.get('wiki', {}))

        self.parent = Upgrade({}, '', None, self.toml.fpath, self.toml.name, self.icon)
        if child:
            self.parent = Upgrade(self.raw.copy(), self.uid, None, self.toml.fpath, self.toml.name, self.icon)
            if child == 'upgrade':
                self.uid = self.uid + '-upgrade'
                self.raw = {**self.raw, **self.get('upgradeParameters')}
                self.raw.pop('upgradeParameters')
            else:
                self.uid = self.uid + '-' + child
                self.raw = {**self.raw, **self.get('presets')[child]}
                self.raw.pop('presets')
            self.name = md.star(md.clean(self.get('shortdescription')))
            self.icon = md.icon(self.get_obj_icon_link())
            self.urlf = md.urlf(md.clean(self.get('shortdescription')))
            self.toml = File(config.ROOT_TARGET, config.ROOT_TARGET_TOML, '/items', self.urlf, 'toml', self.name, self.icon)

        self.type2: str = self.get('builder')
        if self.type2:
            self.type2 = self.type2.split('/')[-1].split('.')[0]
            defaults = load.json('/items/buildscripts/alta/defaults.config')
            self.defaults = {
                **defaults.get('default'),
                **defaults.get(self.type2, defaults.get('species').get('default').get(self.get('category'), {})),
                **defaults.get(self.type2, defaults.get('species').get(self.get('race', 'generic'), {}).get(self.get('category'), {})),
            }
            self.raw = {**self.defaults, **self.raw}

        # self.chest = chests.get_pools_by_obj(self.uid)
        # self.chest_loot_uids = chests.get_pools_by_obj_flat(self.uid)
        self.pickup = {uid: radio.msgs[uid] for uid in self.get_pickup_msgs() if uid in radio.msgs}
        self.element = Element(self.get('elemtentalType'), self.get('shortdescription'), None)
        self.spawner = Spawner(
            set(self.get('pats', []) + [self.get('pet')]),
            {**self.get('baseParameters', {}), **{'damageTeam': self.get('damageTeam', {})},}
        )

        self.level = self.get('level', 0)
        self.tier = self.get_tier()
        self.rarity = self.get_rarity()

        self.anvil = Upgrade(self.get('upgradeParameters'), self.uid, 'upgrade', self.toml.fpath, self.toml.name, self.icon)
        if self.anvil.raw:
            ItemExtractor(file_path, pit, chests, radio, bps, loot, 'upgrade').save()
        self.perfect = self.get('variants', [])
        self.cooking = [
            Upgrade(self.get('presets', {}).get(variant, {}), self.uid, variant, self.toml.fpath, self.toml.name, self.icon) for variant in self.perfect if type(variant) == str
        ]
        for variant in self.cooking:
            if variant.raw:
                ItemExtractor(file_path, pit, chests, radio, bps, loot, variant.suffix).save()
        self.loot = self.get_loot_uids()

    def get_loot_uids(self):
        pool_uid = self.get('treasure', {}).get('pool')
        level = self.get('treasure', {}).get('level')
        return {'treasure': pool_uid, 'level': level or self.level} if pool_uid else {}

    def get(self, attr: str, default = None):
        return self.raw.get(attr, default)

    def get_cat(self) -> str:
        tags = self.get('itemTags', [])
        cat = self.get('category')
        if cat == 'throwableItem' and 'monster_egg' in tags: return 'monster_egg'
        if cat == 'throwableItem' and 'droid' in tags: return 'droid_deployer'
        if cat == 'throwableItem' and 'drone' in tags: return 'drone_deployer'
        if cat == 'throwableItem' and 'android' in tags: return 'android_deployer'
        if cat == 'throwableItem' and 'spawner' in tags: return 'spawner'
        if cat == 'throwableItem': return 'throwable'
        if cat == 'mysteriousReward' and 'loot' in tags: return 'loot'
        if cat == 'mysteriousReward' and 'gsr' in tags: return 'gsr'
        if cat == 'mysteriousReward' and 'set' in tags: return 'set'
        if cat == 'mysteriousReward': return 'reward'
        if cat == 'preparedFood': return 'dish'
        if cat == 'craftingMaterial': return 'resource'
        if cat == 'clothingDye': return 'dye'
        if cat == 'cookingIngredient': return 'ingredient'
        if cat == 'shield' and 'shielder' in tags: return 'shielder'
        if cat == 'medicine' and 'enhancer' in tags: return 'enhancer'
        if cat == 'A.I. Chip': return 'ai'
        if cat == 'headwear': return 'head_clothing'
        if cat == 'chestwear': return 'body_clothing'
        if cat == 'legwear': return 'legs_clothing'
        if cat == 'backwear': return 'back_clothing'
        if cat == 'headarmour': return 'head_armor'
        if cat == 'chestarmour': return 'body_armor'
        if cat == 'legarmour': return 'legs_armor'
        if cat == 'enviroProtectionPack': return 'back_armor'
        if cat == 'eppAugment': return 'augment'
        if cat == 'petCollar': return 'collar'
        if cat == 'assaultRifle': return 'ar'
        if cat == 'sniperRifle': return 'sniper'
        if cat == 'uniqueWeapon': return 'weapon'
        if cat == 'machinePistol': return 'smg'
        if cat == 'rocketLauncher': return 'rocket_launcher'
        if cat == 'grenadeLauncher': return 'grenade_launcher'
        else: return cat

    def get_type(self) -> str:
        tags = self.get('itemTags', [])
        cat = self.get('category')
        if 'scanner' in tags: return 'device'
        if 'energy_source' in tags: return 'energy_source'
        if 'data_source' in tags: return 'data_source'
        if cat == 'throwableItem' and 'monster_egg' in tags: return 'egg'
        if cat == 'throwableItem' and 'droid' in tags: return 'robotics'
        if cat == 'throwableItem' and 'drone' in tags: return 'robotics'
        if cat == 'throwableItem' and 'android' in tags: return 'robotics'
        if cat == 'throwableItem' and 'spawner' in tags: return 'egg'
        if cat == 'throwableItem' and 'nade' in tags: return 'nade'
        if cat == 'throwableItem': return 'equipment'
        if cat == 'mysteriousReward' and 'loot' in tags: return 'container'
        if cat == 'mysteriousReward' and 'gsr' in tags: return 'container'
        if cat == 'mysteriousReward' and 'set' in tags: return 'equipment'
        if cat == 'mysteriousReward': return 'reward'
        if cat == 'preparedFood': return 'cooking'
        if cat == 'food': return 'cooking'
        if cat == 'cookingIngredient': return 'cooking'
        if cat == 'craftingMaterial': return 'resource'
        if cat == 'clothingDye': return 'dye'
        if cat == 'shield' and 'shielder' in tags: return 'shielder'
        if cat == 'medicine' and 'enhancer' in tags: return 'enhancer'
        if cat == 'A.I. Chip': return 'data_source'
        if cat == 'eppAugment': return 'data_source'
        if cat == 'petCollar': return 'accessory'
        else: return cat

    def get_tags(self, tags=[]):
        return sorted(tuple(i.lower() for i in set(self.get('itemTags', []) + tags) if i and i != 'upgradeableWeapon'))

    def get_pickup_msgs(self):
        tags = self.get('itemTags', [])
        msgs: list[str] = self.get('radioMessagesOnPickup', [])
        for v in tags:
            if v == 'gsr': msgs.append('ct_gsr_msg')
            if v == 'set': msgs.append('ct_set_msg')
            if v == 'loot': msgs.append('ct_loot_crate_msg')
            if v == 'datamass': msgs.append('ct_datamass_msg')
            if v == 'ebook': msgs.append('ct_ebook_msg')
            if v == 'faradea': msgs.append('ct_faradea_msg')
            if v == 'haven': msgs.append('ct_haven_msg')
            if v == 'warped': msgs.append('ct_warped_msg')
            if v == 'eds': msgs.append('ct_eds_msg')
            if v == 'shield': msgs.append('ct_alta_shield_msg')
            if v == 'weapon': msgs.append('ct_alta_weapon_msg')
            if v == 'energy_shielder': msgs.append('ct_energy_shielder_msg')
            if v == 'drone' or v == 'droid': msgs.append('ct_robot_spawner_msg')
        return sorted(set(msgs))

    def get_cost(self):
        return self.get('price', 0)

    def get_cost_pixels(self):
        return int(self.get_cost() * ((self.level / 2) + 0.5) + (round(self.get_cost() / 100) * 10 * self.rarity))

    def get_cost_gold(self):
        return self.get_cost_pixels() * 2

    def get_cost_credits(self):
        return int(self.get_cost() / 2.5 * ((self.tier / 2) + 0.5) + (round(self.get_cost() / 100) * 10 * self.rarity))

    def get_cost_stardust(self):
        return int(self.get_cost_credits() / 1.6)

    def get_cost_essence(self):
        return int(self.get_cost() * (self.level + 0.5))

    def get_tier(self):
        return 0 if self.level < 3 else (self.level - 2)

    def get_rarity(self):
        return self.get('shortdescription', '').count('')

    def get_obj_icon_link(self) -> str:
        icon = self.get('inventoryIcon', '').split(':')[0]
        if not icon:
            if self.get('shape'): icon = f'{self.dir_path}/saplingicon.png'
            else: icon = self.get('itemName') + '.png'
        return self.get_icon_link(icon)

    def get_icon_link(self, icon: str) -> str:
        if icon in db.WIKI_ICONS: return db.WIKI_ICONS[icon]
        if icon[0] != '/': icon = f'{self.dir_path}/{icon}'
        return f'{config.ROOT_REPO}{icon}'.replace(' ', '_')

    def save(self):
        output = {
            'id': self.uid,
            'base': 'item',
            'cat': self.cat,
            'type': self.type,
            'tags': self.get_tags([self.cat, self.type]),

            'name': self.name,
            'lore': md.star(self.get('description')),
            'long': md.star(self.get('longdescription')),

            'species': self.get('race', 'generic'),
            'level': self.level,
            'rarity': self.rarity,
            'rarity_sb': list(db.RARITIES)[0 if self.level < 3 else (1 if self.level < 5 else (2 if self.level < 6 else (3 if self.level < 8 else 4)))],
            'tier': self.tier,

            'inspect': {
                'alta': md.star(self.get('altaDescription')),
                'apex': md.star(self.get('apexDescription')),
                'avian': md.star(self.get('avianDescription')),
                'floran': md.star(self.get('floranDescription')),
                'glitch': md.star(self.get('glitchDescription')),
                'human': md.star(self.get('humanDescription')),
                'hylotl': md.star(self.get('hylotlDescription')),
                'novakid': md.star(self.get('novakidDescription')),
            },
            'pickup': self.pickup,
            'scanner': [],
            'cost': {
                'gold': self.get_cost_gold(),
                'pixels': self.get_cost_pixels(),
                'credits': self.get_cost_credits(),
                'stardust': self.get_cost_stardust(),
                'essence': self.get_cost_essence(),
            },
            'element': {
                'base': self.element.base,
                'type': self.element.type,
                'strong': self.element.strong,
                'energy': self.element.energy,
                'advantage': self.element.advantage,
            },
            'upgrades': {
                'anvil': self.anvil.raw,
                'station': {
                    'id': '',
                    'name': '',
                    'link': '',
                    'cost': 0,
                },
                'cooking': [variant.raw for variant in self.cooking if variant.raw],
                'random': [
                    {
                        'id': '',
                        'name': '',
                        'link': '',
                        'chance': 0,
                    },
                ],
            },
            'parent': self.parent.raw,
            'abilities': {
                'primary': Ability(self.get('primaryAbility')).raw,
                'secondary': Ability(self.get('altAbility')).raw,
                'passive': Ability(self.get('passiveAbility')).raw,
            },
            # 'item': {
            #     'handedness': self.get('twoHanded'),
            #     "spawner" : {
            #         "entities" : self.get('pats', []) + [self.get('pet', '')],
            #         "stats" : {**self.get('baseParameters', {}), **{'damageTeam': self.get('damageTeam', {})},}
            #     },
            # },
            # 'object': {
            #     'smashable': self.get('smashable', False),
            #     'loungeable': self.get('objectType') == 'loungeable',
            #     'droppable': not bool(self.get('smashable') or self.get('smashOnBreak') or self.get('breakDropOptions')),
            #     'slots': self.get('slotCount', 0),
            #     'health': self.get('smashable', 1) * 10,
            #     "spawner" : {
            #         "entities" : self.get('spawner', {}).get('monsterTypes', []),
            #         "stats" : self.get('spawner', {}).get('monsterParams', {}),
            #         "stock" : self.get('spawner', {}).get('stock', 0),
            #         "frequency" : self.get('spawner', {}).get('frequency', 0),
            #         "trigger" : self.get('spawner', {}).get('trigger', ''),
            #         "outOfSight" : self.get('spawner', {}).get('outOfSight', False)
            #     },
            #     'chests': self.chest,
            #     'loot': self.chest_loot_uids,
            # },
            'stats': {
                'handedness': self.get('twoHanded'),
                "spawner" : self.spawner.raw,
            },
            'effects': [],
            'loot': self.loot,

            'repo': {
                'ext': self.repo.ext,
                'name': self.repo.file,
                'rdir': self.repo.rdir,
                'rpath': self.repo.rpath,
                'fdir': self.repo.fdir,
                'fpath': self.repo.fpath,
                'link': self.repo.link,
            },
            'assets': {
                'ext': self.toml.ext,
                'name': self.toml.file,
                'rdir': self.toml.rdir,
                'rpath': self.toml.rpath,
                'fdir': self.toml.fdir,
                'fpath': self.toml.fpath,
                'link': self.toml.link,
            },
            'wiki': {
                'ext': self.wiki.ext,
                'name': self.wiki.file,
                'rdir': self.wiki.rdir,
                'rpath': self.wiki.rpath,
                'fdir': self.wiki.fdir,
                'fpath': self.wiki.fpath,
                'link': self.wiki.link.replace('.md', ''),
            },
            'meta': self.meta.raw,
            'icon': self.icon,
        }
        if not self.meta.skip:
            toml.dump(output, open(self.toml.full, 'w', encoding="utf-8"))



FULL = {
    'id': '',
    'base': '',  # 'item', 'creature', 'projectile', 'biome', 'species', 'object', 'plant'
    'cat': '',
    'type': '',
    'tags': [],

    'name': '',
    'lore': '',
    'long': '',

    'species': '',
    'level': '',
    'class': '',

    'inspect': {
        'alta': '',
    },
    'pickup': [
    ],
    'scanner': {
    },
    'cost': {
        'gold': 0,
        'pixels': 0,
        'credits': 0,
        'stardust': 0,
        'essence': 0,
    },
    'element': {
        'base': '',
        'type': '',
        'strong': '',
        'advantage': '',
    },
    'upgrades': {
        'anvil': {
            'id': '',
            'name': '',
            'link': '',
            'cost': 0,
        },
        'station': {
            'id': '',
            'name': '',
            'link': '',
            'cost': 0,
        },
        'cooking': {
            'id': '',
            'name': '',
            'link': '',
            'chance': 0,
        },
        'random': [
            {
                'id': '',
                'name': '',
                'link': '',
                'chance': 0,
            },
        ],
    },
    'abilities': {
        'primary': {
            'name': '',
            'desc': '',
            'long': '',
            'lore': '',
            'stats': {
            },
        },
        'secondary': {
            'name': '',
            'desc': '',
            'long': '',
            'lore': '',
            'stats': {
            },
        },
        'passive': {
            'name': '',
            'desc': '',
            'long': '',
            'lore': '',
            'stats': {
            },
        },
    },
    'object': {
        'smashable': False,
        'loungeable': False,
        'droppable': False,
        'slots': 0,
    },
    'stats': [],
    'effects': [],

    'repo': {
        'dir': '',
        'name': '',
        'path': '',
        'link': '',
    },
    'icon': '',
}


co = load.CockpitLib()
ch = load.ChestLib()
ra = load.RadioLib()
bps = resources.RecipeLib()
loot = resources.LootLib()
for item_path in load.filepaths_in_dirs(load.dirs(('items',)), ('patch', 'md', 'object')):
    ItemExtractor(item_path, co, ch, ra, bps, loot).save()
