import wiki
import resources as rs
import md
import db


class MD:
    PARENTS = '> Main pages: '
    BREAKS = '\nThis object **doesn\'t drop itself** when broken.  \n'
    PARENTS = '> Main pages: '
    PARENTS = '> Main pages: '
    PARENTS = '> Main pages: '
    PARENTS = '> Main pages: '


def get_body(wp: wiki.Page, lib: rs.Library, cat: str) -> str:
    if wp.md:
        wp.body = md.enrich(wp.md, lib.names)
        return wp.body
    wp.body = get_headline(wp, cat, lib)
    if wp.banner: wp.body = md.n(wp.banner) + wp.body
    if wp.parents: wp.body = md.n(MD.PARENTS + ', '.join([md.replace(i, lib.names) for i in wp.parents])) + wp.body
    if (shield := [wp.get('baseShieldHealth', 0), wp.get('minActiveTime', 0.0), wp.get('cooldownTime', 0.0), wp.get('knockback', 0)])[0]:
        wp.body = wp.body + f'\nShield parameters:\n\n- health: {shield[0]}\n- min time: {shield[1]}\n- cooldown: {shield[2]}\n- knockback: {shield[3]}\n'
    wp.body = wp.body + get_stats(wp.raw, lib, (
        {'blockingStat': {}, 'defaultDuration': {'metric': 's'}, 'effectConfig': {'name': 'Effect parameters'}},  # Effect params
        {'statusEffects': {}},
    ))
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
    # Other
    wp.body = wp.body + f'\n### Technical Information\n\n'
    if craftable(wp.ext): wp.body = wp.body + f'Tags: `{"` `".join(wp.tags)}`  \n'
    if wp.level: wp.body = wp.body + f'Level: {wp.level}  \n'
    if race := wp.get('race'): wp.body = wp.body + f'Race: {md.item(race.title(), db.RACES[race]) if race in db.RACES else race.title()}  \n'
    if wp.loot_uids: wp.body = wp.body + f'Loot table ID(s): `{"` `".join(wp.loot_uids.values())}`  \n'
    wp.body = wp.body + f'In-game ID: `{wp.uid}`  \n'
    wp.body = wp.body + f'File path (GitHub link): [`{wp.file_path}`]({wp.file_link})  \n'
    if wp.trivia: wp.body = wp.body + '\n### Trivia\n\n' + ';\n'.join(['- ' + md.enrich(t, lib.names) for t in wp.trivia]) + '.\n'
    if wp.wiki.get('related') or wp.wiki.get('images'):
        wp.body = wp.body + '\n---\n'
    if rel := wp.wiki.get('related', {}):
        wp.body = wp.body + '\n## Related Resources\n'
        for item in rel:
            wp.body = wp.body + f'\n{item}\n' + (get_related(i,lib) if type(i:=rel[item])==list else ''.join(tuple(f'\n{i2}\n{get_related(i[i2],lib)}' for i2 in i)))
    if imgs := wp.wiki.get('images', []):
        wp.body = wp.body + '\n## Related Images\n\n' + ' '.join([md.icon(img) for img in imgs]) + '\n'
    wp.body = wp.body.replace('\n\n\n\n', '\n\n').replace('\n  \n', '\n\n').replace('\n\n\n', '\n\n').replace(': \n', ':\n')
    return wp.body

def get_headline(wp: wiki.Page, cat: str, lib: rs.Library, parent_wp: wiki.Page = None) -> str:
    element = db.ELEMENTS[e] + ' ' if (e := wp.element) else ''
    hand = '' if (h := wp.get('twoHanded')) is None else ('2-handed ' if h else '1-handed ')
    rarity = db.RARITIES[wp.rarity] if wp.rarity else 'a'
    level = f' lvl.{wp.level}' if wp.level else ''
    headline = f'{wp.icon} **{wp.name}** is {rarity}{level} {hand}{element}{cat}.  \n'
    price = f'Can be sold for *{int(wp.price/5)}* {db.link("pixels", *db.WIKI_LINKS["money"][1:])}.  \n' if wp.price else ''
    mds = ''.join(tuple(f'\n{h}\n\n{md.enrich(wp.cmd[h], lib.names)}\n' for h in wp.cmd)) if wp.cmd and (not parent_wp or parent_wp.cmd != wp.cmd) else ''
    return f'{headline}{price}{md.enrich(wp.desc, lib.names)}{get_races(wp, lib, parent_wp)}{mds}{get_pickup(wp, lib, parent_wp)}'

def get_abils_desc(wp: wiki.Page, lib: rs.Library, prefix: str = '##### ', def_desc: str = 'This ability has no description.  \n'):
    body = ''
    for abil in wp.abils:
        name = f'**{name}**: ' if (name := wp.abils[abil].get('name')) else ''
        body = body + f'\n{prefix}{abil.title()} Ability\n\n{name}{md.enrich(wiki.get_desc(wp.abils[abil]), lib.names) or def_desc}'
    return body

def get_related(l, lib: rs.Library):
    return '\n' + ''.join(tuple((md_any(i, lib.full) if type(i) == str else ''.join(tuple('  ' + md_any(j, lib.full) for j in i))) for i in l))

def get_races(wp: wiki.Page, lib: rs.Library, original_wp: wiki.Page = None):
    obj: dict[str] = wp.raw.copy()
    if races := [(k1, k2) for k1, k2 in [(key.replace('Description', ''), obj[key]) for key in obj if 'Description' in key] if k1 in db.RACES]:
        body = get_expand(''.join(f'- {md.item(k1.title(), db.RACES[k1])}: {md.enrich(k2, lib.names)}\n' for k1, k2 in races), 'Race descriptions:', len(races))
        if not original_wp or get_races(original_wp, lib) != body:
            return body
    return ''

def get_pickup(wp: wiki.Page, lib: rs.Library, original_wp: wiki.Page = None):
    if msgs := wp.pickup:
        body = get_expand(''.join(md_any(m, {**lib.uids, **lib.names}, True, True, lib.radios) for m in msgs), 'Pickup Messages:', len(msgs), 0)
        if not original_wp:
            return body
    return ''

def md_any(s, sources: dict, *args, **kwargs):
    return md.ln(md.replace(s, sources, *args, **kwargs))

def nw(n: int = None, w: str = None, p=' '):
    return (f'{p}x*{n}*' if n else '') + (f' (weight: {w})' if w else '')

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

def lootable(ext):
    return ext not in ('projectile', 'biome', 'statuseffect', 'weather', 'bush', 'grass')

def craftable(ext):
    return lootable(ext) and ext not in ('monstertype', 'modularstem', 'modularfoliage')
