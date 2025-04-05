import json
import toml
from pathlib import Path

import config
import resources as rs
import md
import db
import load


class MD:
    PARENTS = '> Main pages: '
    BREAKS = '\nThis object **doesn\'t drop itself** when broken.  \n'
    HANDED = '2-handed '
    LEVEL = ' lvl.{}'
    SOLD = 'Can be sold for *{}* {}.'
    PARENTS = '> Main pages: '

class Page():
    def __init__(self, path, lib: rs.Library):
        self.raw = toml.load(path)
        self.lib = lib

        self.header = self.get_header()
        self.footer = self.get_footer()
        Path(config.ROOT_TARGET + self.get('wiki').get('fdir')).mkdir(parents=True, exist_ok=True)
        load.dump(self.header+self.footer, '', config.ROOT_TARGET + self.get('wiki').get('fpath'))

    def get(self, attr: str, default = None):
        return self.raw.get(attr, default)

    def meta(self, attr: str, default = None):
        return self.get('meta').get(attr, default)

    def get_header(self) -> str:
        element = db.ELEMENTS[e] + ' ' if (e := self.get('element', {}).get('base')) else ''
        hand = MD.HANDED if self.get('handedness') else ''
        rarity = db.RARITIES[self.get('rarity_sb')] if self.get('rarity_sb') else 'a'
        level = MD.LEVEL.format(self.get('level')) if self.get('level') else ''
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
        return ''.join(header)[1:]

    def get_footer(self) -> str:
        footer = (
            md.h3('Technical Information'),
            md.nm((
                md.param('Tags', md.loop(md.qs, self.get('tags')), craftable(self.get('repo').get('ext'))),
                md.param('Level', self.get('level')),
                md.param('Species', md.item(race.title(), db.RACES[race]) if (race := self.get('species')) in db.RACES else race.title()),
                md.param('In-game ID', md.qs(self.get('id'))),
                md.param('File path (GitHub link)', self.get('repo', {}).get('link')),
            )),
            md.h3('Trivia', self.meta('trivia')),
            md.nm(';\n'.join(['- ' + md.enrich(t, self.lib.names) for t in self.meta('trivia', [])]) + '.\n', self.meta('trivia')),
            md.line(self.meta('related') or self.meta('images')),
            md.h2('Related Resources', self.meta('related')),
            md.nm(self.get_related(json.loads(self.meta('related', '{}')))),
            md.h2('Related Images', self.meta('images')),
            md.nm(md.loop(md.icon, self.meta('images'))),
        )
        return ''.join(footer)
    
    def get_related(self, rel):
        rels = []
        for item in rel or []:
            rels.append(md.nm(item) + (get_related(i,self.lib) if type(i:=rel[item])==list else ''.join(tuple(md.nm(i2) + get_related(i[i2],self.lib) for i2 in i))))
        return ''.join(rels)

def get_related(l, lib: rs.Library):
    return '\n' + ''.join(tuple((md_any(i, lib.full) if type(i) == str else ''.join(tuple('  ' + md_any(j, lib.full) for j in i))) for i in l))

def md_any(s, sources: dict, *args, **kwargs):
    return md.ln(md.replace(s, sources, *args, **kwargs))

def lootable(ext):
    return ext not in ('projectile', 'biome', 'statuseffect', 'weather', 'bush', 'grass')

def craftable(ext):
    return lootable(ext) and ext not in ('monstertype', 'modularstem', 'modularfoliage')



lib = rs.Library()
for item_path in load.filepaths_in_dirs(load.dirs(('items',), config.ROOT_TARGET + config.ROOT_TARGET_TOML)):
    Page(item_path, lib)
