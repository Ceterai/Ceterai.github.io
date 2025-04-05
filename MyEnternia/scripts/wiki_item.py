import json
import toml
from pathlib import Path

import config
import resources as rs
import md
import db
import load
import wiki_generic


class MD:
    PARENTS = '> Main pages: '
    BREAKS = '\nThis object **doesn\'t drop itself** when broken.  \n'
    HANDED = '2-handed '
    LEVEL = ' lvl.{}'
    SOLD = 'Can be sold for *{}* {}.'
    PARENTS = '> Main pages: '

class Page(wiki_generic.Page):
    def __init__(self, path, lib: rs.Library):
        self.raw = toml.load(path)
        self.lib = lib

        self.header = self.get_header()
        self.header = self.get_body()
        self.footer = self.get_footer()
        Path(config.ROOT_TARGET + self.get('wiki').get('fdir')).mkdir(parents=True, exist_ok=True)
        load.dump(self.header+self.footer, '', config.ROOT_TARGET + self.get('wiki').get('fpath'))

    def get(self, attr: str, default = None):
        return self.raw.get(attr, default)

    def meta(self, attr: str, default = None):
        return self.get('meta', {}).get(attr, default)

    def stats(self, attr: str, default = None):
        return self.get('stats', {}).get(attr, default)

    def get_body(self) -> str:
        shield = [
            self.stats.get('baseShieldHealth', 0),
            self.stats.get('minActiveTime', 0.0),
            self.stats.get('cooldownTime', 0.0),
            self.stats.get('knockback', 0),
        ]
        wp.body = wp.body + get_abils_desc(wp, lib, '### ')  # Abilities
        if craftable(wp.ext) and wp.upgrades:  # Upgrades
            wp.body = wp.body + '\n### Item Variants\n\n' + '\n'.join([get_headline(obj, cat, lib, wp) + get_abils_desc(obj, lib, '#### Upgraded ') for obj in wp.upgrades])
        if craftable(wp.ext):  # Crafting
            if (bps := lib.bps.find_recipes_of_obj(wp.uid)) + (uses := lib.bps.find_recipes_that_use_obj(wp.uid)):
                wp.body = wp.body + f'\n### Crafting\n'
                if bps:
                    body = []
                    for bp in bps:
                        body.append(md.ln(', '.join(bp.sources) + f' (takes {bp.dur}s, outputs {wp.icon} {wp.name}{nw(bp.n)}):')
                        + ''.join([find_list_item(obj.uid, lib.obj, n=obj.n, prefix='  ') for obj in bp.input]))
                    wp.body = wp.body + get_expand(''.join(set(body)), 'Can be crafted:', len(set(body)), 3)
                if uses:
                    body = ''.join(get_item_list(tuple(use.uid for use in uses), lib.obj, prefix=''))
                    wp.body = wp.body + get_expand(body, 'Can be used to craft:', len(uses))
            if lbps := wp.get('learnBlueprintsOnPickup', []):
                body = ''.join(get_item_list(lbps, lib.obj, prefix=''))
                wp.body = wp.body + get_expand(body, 'Unlocks following blueprints/recipes on pickup:', len(lbps), 10)
            if bps := lib.bps.find_admin_recipes_of_obj(wp.uid):
                body = []
                for bp in bps:
                    body.extend([md.ln(source) for source in bp.sources_admin])
                wp.body = wp.body + get_expand(''.join(set(body)), 'Can be accquired in cheat/creative crafting tables:', len(set(body)), 0)
        if lootable(wp.ext):  # Loot
            lts = {**lib.loot.find_loot_of_obj(wp.loot_uids), **lib.loot.find_obj_loot_of_obj(wp.raw)}
            loot_sources = get_loot_sources(wp.uid, lib)
            if lts or wp.chest or loot_sources:
                wp.body = wp.body + f'\n### Loot\n'
                if lts or wp.chest:
                    body = ''.join([f'\nContains following **{name}** loot:\n\n' + get_loot_list(lib.loot, lib.obj, lts[name]) for name in lts])
                    for chest in wp.chest:
                        body = body + f'\nContains following `{chest}` treasure:\n\n'
                        for l in wp.chest[chest]:
                            body = body + f'- for planet level **{l}+**:\n'
                            for pool in wp.chest[chest][l]:
                                body = body + f'  - loot pool `{pool}`:\n' + get_loot_list(lib.loot, lib.obj, lib.loot.find_loot_of_obj({l: pool})[l], '    ')
                    wp.body = wp.body + get_expand(body, 'Full list of possible loot:', 0, 0)
                if loot_sources:
                    wp.body = wp.body + get_expand(''.join(loot_sources), 'Can be found as loot in:', len(loot_sources))
        if found := get_biomes(wp.bid, lib):
            wp.body = wp.body + '\n### Found In Biomes\n' + get_expand(''.join(found), 'Can be found in following biomes:', len(found))
        body = (
            md.nm('Shield parameters:', shield[0]),
            md.nm(md.l((
                md.param('health', shield[0]),
                md.param('min time', shield[1]),
                md.param('cooldown', shield[2]),
                md.param('knockback', shield[3]),
            )), shield[0]),
            md.nm(get_stats(self.raw.get('stats', {}), lib, (
                {'statusEffects': {}},
            ))),
            md.nm(get_abils_desc(wp, lib, '### ')),
            md.nm(),
            md.nm(),
            md.nm(),
            md.nm(),
            md.nm(),
        )





        header = (
            md.h1(self.get('name')),
            md.nm(MD.PARENTS + ', '.join([md.replace(i, self.lib.names) for i in self.meta('parents', [])]), self.meta('parents')),
            md.nm(md.icon(self.meta('banner'))),
            md.nm((
                f'{self.get('icon')} **{self.get('name')}** is {rarity}{level} {hand}{element}{self.get('cat')}.',
                MD.SOLD.format(int(self.get('cost', {}).get('pixels')/5), db.link("pixels", *db.WIKI_LINKS["money"][1:])) if self.get('cost', {}).get('pixels') else '',
                md.enrich(self.get('lore'), self.lib.names),
                md.enrich(self.get('long'), self.lib.names),
            )),
            ''.join(tuple(f'{md.nm(h)}{md.nm(md.enrich(self.meta('md')[h], self.lib.names))}' for h in self.meta('md'))) if self.meta('md') and (not self.get('parent')) else '',
        )
        return ''.join(body)

    def get_abils_desc(wp: wiki.Page, lib: rs.Library, prefix: str = '##### ', def_desc: str = 'This ability has no description.  \n'):
        body = ''
        for abil in wp.abils:
            name = f'**{name}**: ' if (name := wp.abils[abil].get('name')) else ''
            body = body + f'\n{prefix}{abil.title()} Ability\n\n{name}{md.enrich(wiki.get_desc(wp.abils[abil]), lib.names) or def_desc}'
        return body

def get_related(l, lib: rs.Library):
    return '\n' + ''.join(tuple((md_any(i, lib.full) if type(i) == str else ''.join(tuple('  ' + md_any(j, lib.full) for j in i))) for i in l))

def md_any(s, sources: dict, *args, **kwargs):
    return md.ln(md.replace(s, sources, *args, **kwargs))

def lootable(ext):
    return ext not in ('projectile', 'biome', 'statuseffect', 'weather', 'bush', 'grass')



lib = rs.Library()
for item_path in load.filepaths_in_dirs(load.dirs(('items',), config.ROOT_TARGET + config.ROOT_TARGET_TOML)):
    Page(item_path, lib)

def get_list_item(uid: str, obj: wiki.Page = None, n: int = None, w: str = None, prefix='  '):
    return prefix + md.ln((obj.link if obj else (db.link(*(db.WIKI_LINKS[uid])) if uid in db.WIKI_LINKS else md.qs(uid))) + nw(n, w))

def find_list_item(uid: str, obj_lib: list[wiki.Page], **kwargs):
    return get_list_item(uid, rs.find_obj(uid, obj_lib), **kwargs)

def get_item_list(uids: list[str], obj_lib: list[wiki.Page], **kwargs):
    all_results = tuple(rs.find_obj(uid, obj_lib) or uid for uid in uids)
    items = rs.sort(tuple(item for item in all_results if type(item) != str))
    uids = sorted(tuple(item for item in all_results if type(item) == str))
    return tuple(get_list_item(item.uid, item, **kwargs) for item in items) + tuple(get_list_item(uid, **kwargs) for uid in uids)

def get_loot_list(lib: rs.LootLib, obj_lib: list[wiki.Page], loot_tables: rs.LootTable, prefix=''):
    result = ''
    for loot in loot_tables.entries:
        rounds = ', '.join([nw(f[1], f[0], '') for f in loot.rounds])
        result = result + prefix + f'- for level **{loot.level}+**' + (f' (pool rounds: {rounds})' if rounds else '') + ':\n'
        for f in loot.all:
            if f.is_pool and f.uid in lib.tables:
                result = result + prefix + f'- loot pool `{f.uid}`{nw(f.n, f.weight)}:\n' + get_loot_list(lib, obj_lib, lib.tables[f.uid], prefix + '  ')
            else:
                result = result + prefix + get_list_item(f.uid, rs.find_obj(f.uid, obj_lib, lib, f.is_pool), f.n, f.weight, '')
    return result

def get_stat_val(stat, lib: rs.Library, metric: str = '', no_dmg=False):
    if type(stat) in (int, float):
        return str(stat) + ((metric) if metric.replace(' ', '') else '')
    if type(stat) == dict:
        return '\n\n' + ''.join([get_stat_desc(stat, lib, stat_name, metric='  ', prefix=metric+'- ', no_dmg=no_dmg) for stat_name in stat])
    if type(stat) == str:
        return md.replace(stat, {**lib.uids, **lib.names}, True, no_dmg, lib.radios)
    if type(stat) == list:
        return ', '.join([get_stat_val(s, lib, no_dmg=no_dmg) for s in [stat[i] for i in range(len(stat)) if i == stat.index(stat[i])]])
    return md.qs(str(stat))

def get_stat_desc(obj: dict, lib: rs.Library, stat_name: str, name: str = None, metric: str = '', prefix: str = '', no_dmg=False, non_empty=False):
    return f'{prefix}{name or md.camel_to_name(stat_name)}: {get_stat_val(stat, lib, metric, no_dmg)}  \n' if empty(stat := obj.get(stat_name), non_empty) else ''

def get_stats(obj: dict, lib: rs.Library, stat_groups: list[dict[str, dict[str, str]]], body=''):
    for stat_group in stat_groups:
        if tuple(True for stat in stat_group if obj.get(stat) != None):
            body = body + '\n' + ''.join([get_stat_desc(obj, lib, stat, **(stat_group[stat])) for stat in stat_group])
    return body

def get_placeable_item(objs: list[str], lib: rs.Library):
    return ', '.join(rs.unique([md.replace(obj, {**lib.wids, **lib.uids}, True) for obj in sorted(set(objs))]))

def get_biome_spawns(obj: wiki.Page) -> list[str]:
    return obj.surface.get('all', []) + obj.caves.get('all', [])

def get_biome_sources(source_types: list[str]):
    result = []
    if 'biome' in source_types:
        result.append('spawns in the biome')
    if 'chest' in source_types:
        result.append('found in chests')
    if 'drop' in source_types or ('loot' in source_types and not 'chest' in source_types):
        result.append('drops from objects')
    return result

def get_biomes(uid: str, lib: rs.Library):
    sources = lib.loot.get_loot_sources(uid, lib.obj, True)
    sources_per_uid = sources.uid_sources
    sources_per_uid[uid] = sources_per_uid.get(uid, []) + ['biome']
    result = []
    for obj in lib.obj:
        placeables = get_biome_spawns(obj)
        if placeables:
            sources_msg = []
            for obj_uid in sources.obj_uids + [uid]:
                if obj_uid in placeables:
                    sources_msg.extend(get_biome_sources(sources_per_uid[obj_uid]))
            if sources_msg:
                result.append(md.ln(obj.link + (' - ' + ', '.join(set(sources_msg))) if sources_msg else ''))
    return result

def get_loot_sources(uid, lib: rs.Library):
    sources = lib.loot.get_loot_sources(uid, lib.obj, True)
    return tuple(get_list_item(uid, prefix='') for uid in sources.uids) + tuple(get_list_item('', obj, prefix='') for obj in sources.all_objs)

def get_expand(body: str, head: str, n: int, min_n=5):
    return f'\n{head}\n\n{body}' if n < min_n else f'\n<details><summary>{head} (Expand {n or "many"} items)</summary>\n\n{body}\n</details>\n'

def empty(val, non_empty: bool):
    return bool(val) if non_empty else (val != None)
