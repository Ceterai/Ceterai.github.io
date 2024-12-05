import config
import load
import md
import db


class Page:

    def __init__(self, file_path: str, lib_cp: load.CockpitLib, lib_cl: load.ChestLib, obj: dict = None):
        self.raw = obj.copy()
        self.wiki: dict[str] = dict(self.get('wiki', {}))
        self.ext = load.ext(file_path)

        self.cat = self.get_cat()
        self.uid = self.get_uid()
        self.wid = self.uid if '-' in self.uid else (f'{self.uid}-{self.cat}')
        self.bid = self.uid if self.ext not in ('bush', 'grass', 'modularstem', 'modularfoliage') else self.wid
        self.rarity = self.get('rarity')
        self.level = self.get('level')
        self.price = self.get_price()
        self.element = self.get_element()
        self.tags = self.get_tags()
        self.pit = lib_cp.weather.get(self.uid, {}) if self.ext == 'weather' else {}
        # Display
        self.name = self.get_name()
        self.desc = get_desc(self.raw)
        self.name_wiki = md.urlf(self.name)
        # Paths and links
        self.file_path_full = file_path
        self.file_path = file_path.replace((config.ROOT_SOURCE), '').replace('\\', '/')
        self.dir_path = '/'.join(self.file_path.split('/')[:-1])
        self.icon = md.icon(get_obj_icon_link(self.raw, self.uid, self.dir_path, self.pit))
        self.link = md.item(self.name, self.name_wiki, self.icon)
        self.file_link = f'{config.ROOT_REPO_FILES}{self.file_path}'.replace(' ', '%20')
        # Connections
        self.chest = lib_cl.get_pools_by_obj(self.uid)
        self.chest_loot_uids = lib_cl.get_pools_by_obj_flat(self.uid)
        self.loot_uids = self.get_loot_uids()
        self.surface = get_placeables(self.get('surfacePlaceables', {}), lib_cl)
        self.caves = get_placeables(self.get('undergroundPlaceables', {}), lib_cl)
        self.abils = {abil: obj.copy() for abil in ('primary', 'alt', 'passive',) if (obj := self.get(abil + 'Ability'))}
        self.upgrades = get_upgrades(self.raw.copy(), self.file_path_full, lib_cp, lib_cl)
        self.list_item_upgrades = [f'{md.list_link(obj.name, self.name_wiki, obj.icon)}\n' for obj in self.upgrades]
        upgs = get_upgrades(self.raw.copy(), self.file_path_full, lib_cp, lib_cl, False)
        self.aliases = get_aliases(self.name, self.name_wiki, self.icon, self.raw, upgs, self.wiki, self.dir_path)
        # Other
        self.smashable = self.get(('smashable', 'smashOnBreak', 'breakDropOptions'))
        self.pickup = self.get_pickup_msgs()
        # Wiki
        self.md = load.md(raw, **(self.get('charCreationTooltip', {}))) if (raw := self.wiki.get('raw')) else ''
        self.cmd = self.wiki.get('md', '')
        self.trivia = self.wiki.get('trivia', [])
        self.banner = md.icon(self.wiki.get('banner'))
        self.parents = self.wiki.get('parents', [])
        self.body = ''

    def get(self, attr_names: list[str]|str, default = None):
        return get(self.raw, attr_names, default)

    def get_uid(self) -> str:
        return self.get(('itemName', 'objectName', 'name', 'type', 'projectileName', 'kind',), '') if self.ext != 'codex' else self.raw['id'] + '-codex'

    def get_name(self) -> str:
        fields = ('shortDescription', 'shortdescription', 'title', 'label', 'friendlyName', 'kind',)
        return md.clean(self.get(fields, '') or self.pit.get('displayName') or md.uid_to_name(self.wid))

    def get_price(self):
        return int(price * (((self.level or 1) / 2) + 0.5)) if (price := self.get('price')) is not None else price

    def get_element(self):
        if element := self.get('elementalType'): return element
        if kind := self.get('damageKind'):
            for el in db.ELEMENTS:
                if el in kind: return el

    def get_tags(self):
        return sorted(tuple(i.lower() for i in set(self.get(('itemTags', 'colonyTags',), []) + [self.rarity, self.element, self.get('race')]) if i))

    def get_cat(self) -> str:
        tags = self.get('itemTags', [])
        cat = self.get('category')
        if cat == 'throwableItem' and 'spawner' in tags: return 'spawner'
        if cat == 'mysteriousReward' and 'loot' in tags: return 'loot'
        if cat == 'mysteriousReward' and 'gsr' in tags: return 'gsr'
        if cat == 'mysteriousReward' and 'set' in tags: return 'set'
        if self.ext == 'codex': return 'codex'
        if self.ext == 'biome': return 'planetarybiome' if self.get('weather') else 'minibiome' if self.get('surfacePlaceables') else 'cavebiome'
        if self.ext == 'statuseffect': return 'statuseffect'
        if self.ext == 'monstertype' and self.get('baseParameters', {}).get('persistent'): return 'othermonster'
        if self.ext == 'monstertype': return self.get('baseParameters', {}).get('statusSettings', {}).get('statusProperties', {}).get('targetMaterialKind', 'organic') + 'monster'
        if self.ext == 'weather': return 'weather'
        if self.ext == 'projectile': return 'projectile'
        if self.ext == 'modularstem': return 'treestem'
        if self.ext == 'modularfoliage': return 'treetop'
        if self.ext == 'bush': return 'bush'
        if self.ext == 'grass': return 'grass'
        if self.ext == 'species': return 'species'
        else: return cat

    def get_pickup_msgs(self):
        msgs: list[str] = self.get('radioMessagesOnPickup', [])
        for v in self.tags:
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

    def get_lore(self, tags, cat, species, tips):
        for tag in tags:
            if tips.lore.alta[tag] and species == 'alta': full += (full, tips.lore.alta[tag], '\n\n')
        for tag in tags:
            if tips.lore.tags[tag]: full += (full, tips.lore.tags[tag], '\n\n')
        for tag in tags:
            if tips.lore.factions[tag]: full += (full, tips.lore.factions[tag], '\n\n')
        if cat and tips.lore.categories[cat]: full += (full, tips.lore.categories[cat], '\n\n')
        if species and tips.lore.species[species]: full += (full, tips.lore.species[species], '\n\n')
        return full

    def get_loot_uids(self):
        loot_uids: dict = (self.get('dropPools') or [{}])[0]
        loot_uids.update({'treasure': self.get('treasure', {}).get('pool', '')})
        loot_uids.update({'harvest': [stage.get('harvestPool', '') for stage in (self.get('stages') or [{}])][-1]})
        loot_uids.update({'smash': self.get('smashDropPool'), 'break': self.get('breakDropPool')})
        return {uid: loot_uids[uid] for uid in loot_uids if loot_uids[uid]}

# CREATE OBJ

def build(file_path: str, lib_cp: load.CockpitLib, lib_cl: load.ChestLib, obj: dict = None):
    raw_base = obj.copy() if obj else load.json(file_path)
    raw_asset = load.json(raw_base.get('asset'))
    raw_codex = raw_base.get('itemConfig', {})
    raw = {**raw_base, **raw_asset, **raw_codex}
    wiki: dict[str] = get(raw, 'wiki', {})
    if not wiki.get('skip'):
        return Page(file_path, lib_cp, lib_cl, {**raw, **(wiki.get('override', {}))})

def get(raw: dict, attr_names: list[str]|str, default = None):
    attr_names = (attr_names,) if type(attr_names) == str else attr_names
    for name in attr_names:
        if raw.get(name):
            return raw[name]
    return default

def get_desc(raw: dict) -> str:
    return ''.join(tuple((f'{d}  \n' if (d := get(raw, (key,), '')) else d) for key in ('description', 'longdescription',)))

def get_obj_icon_link(obj: dict, uid: str, file_path_relative: str, pit: dict = {}) -> str:
    icon = (obj.get('icon') or obj.get('inventoryIcon') or obj.get('damageKindImage') or pit.get('icon') or '').split(':')[0]
    if not icon:
        if obj.get('shape'): icon = f'{file_path_relative}/saplingicon.png'
        elif not obj.get('category'): return icon
        else: icon = uid + '.png'
    return get_icon_link(icon, file_path_relative)

def get_icon_link(icon: str, file_path_relative: str) -> str:
    if icon in db.WIKI_ICONS: return db.WIKI_ICONS[icon]
    icon = icon if icon[0] == '/' else f'{file_path_relative}/{icon}'
    return f'{config.ROOT_REPO}{icon}'.replace(' ', '_')

def get_upgrades(obj: dict, path: str, cp, cl, skip=True):
    return get_children('upgradeParameters', obj, path, cp, cl, skip=skip) + get_children('presets', obj, path, cp, cl, True, skip=skip)

def get_children(key: str, obj: dict, path: str, lib_cp, lib_cl, multi = False, skip = True):
    presets = obj.get(key, {}) if multi else ({'0': upg} if (upg := obj.get(key)) else {})
    cs = [get_child(obj, path, key, presets[p], lib_cp, lib_cl) for p in presets]
    return [c for c in cs if not skip or not c.wiki.get('skip')]

def get_child(obj: dict, file_path: str, child_params: str, child_params_obj: dict, lib_cp: load.CockpitLib, lib_cl: load.ChestLib):
    new_obj = {**(obj.copy())}
    for key in child_params_obj:
        if new_obj.get(key) and type(new_obj[key]) == dict and child_params_obj[key] != None:
            new_obj[key].update(child_params_obj[key])
        else:
            new_obj[key] = child_params_obj[key]
    new_obj.pop(child_params)
    if child_params == 'upgradeParameters':
        new_obj['level'] = 6
    return Page(file_path, lib_cp, lib_cl, new_obj)

def get_placeables(obj: dict, lib_cl: load.ChestLib):
    items: list[dict[str]] = obj.get('items', [])
    objects = []
    bushes = []
    grasses = []
    treetops = []
    treestems = []
    treasure = []
    for item in items:
        if 'objectSets' in item:
            for obj_set in item['objectSets']:
                for obj in obj_set.get('pool', []):
                    objects.append(obj[1])
        if 'bushes' in item:
            for bush in item['bushes']:
                if bush: bushes.append(bush.get('name') + '-bush')
        if 'grasses' in item:
            for grass in item['grasses']:
                if grass: grasses.append(grass + '-grass')
        if 'treeFoliageList' in item:
            for grass in item['treeFoliageList']:
                if grass: treetops.append(grass + '-treetop')
        if 'treeStemList' in item:
            for grass in item['treeStemList']:
                if grass: treestems.append(grass + '-treestem')
        if 'treasureBoxSets' in item:
            for grass in item['treasureBoxSets']:
                for chest in lib_cl.get_objs_by_chest(grass):
                    treasure.append(chest)
    return {
        'objects': objects,
        'bushes': bushes,
        'grasses': grasses,
        'treetops': treetops,
        'treestems': treestems,
        'treasure': treasure,
        'all': objects + bushes + grasses + treetops + treestems + treasure,
    }

def get_aliases(name: str, name_wiki: str, icon: str, obj: dict, upgrades: list[Page], wiki: dict, dirp: str):
    aliases = {name: (name_wiki, icon), **{obj.name: (name_wiki, obj.icon) for obj in upgrades}}
    if alkey := obj.get('alkey'): aliases.update({alkey: (name_wiki, icon)})
    for a in (als := wiki.get('aliases', {})):
        icn = als[a].get('icon')
        anchor = (('#' + anc) if (anc := als[a].get('anchor')) else '')
        if icn == 'none':
            aliases.update({a: (name_wiki + anchor, None)})
        elif (size := als[a].get('icon_size')):
            aliases.update({a: (name_wiki + anchor, md.icon((icn, *size),))})
        else:
            aliases.update({a: (name_wiki + anchor, (md.icon(get_icon_link(icn, dirp)) if icn else icon))})
    return aliases
