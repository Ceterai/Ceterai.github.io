import config
import load
import wiki
import db


class Item:

    def __init__(self, item: dict|list|str):
        try:
            if type(item) == dict:  # Always the case with recipes, but not always with loot
                self._parse(str(item['item']), int(item.get('count', 1)), dict(item.get('parameters', {})))
            elif type(item) == list:
                self._parse(str(item[0]), int(item[1] if len(item) > 1 else 1), dict(item[2] if len(item) > 2 else {}))
            else:
                self._parse(str(item), 1, {})
            self.raw = item
        except Exception as e:
            print(f'Can\'t parse item descriptor: {item}')
            raise e

    def _parse(self, uid: str, n: int, params: dict):
        self.uid = uid
        self.n = n
        self.params = params


class Recipe:

    def __init__(self, recipe: dict):
        try:
            self.raw_input = tuple(recipe['input'])
            self.raw_output = dict(recipe['output'])
            self.input = tuple(Item(entry) for entry in self.raw_input)
            self.output = Item(self.raw_output)
            self.tags = tuple(recipe.get('groups', []))
            self.dur = float(dur) if '.' in str(dur := recipe.get('duration', 0.0)) else int(dur)
            self.sources_admin = self._get_sources(db.RECIPE_SOURCES_ADMIN)
            self.sources = self._get_sources(db.RECIPE_SOURCES)
            if not (self.sources_admin + self.sources):
                self.sources = ['Other Crafting Tables']
            if not self.output.params:
                self.sources_admin.append(db.RECIPE_SIP)
            self.raw = recipe
            # Output shortcuts
            self.uid = self.output.uid
            self.n = self.output.n
            self.params = self.output.params
        except Exception as e:
            print(f'Can\'t parse recipe: {recipe}')
            raise e

    def _get_sources(self, source_lib: dict[str, list[str]]) -> list[str]:
        sources = []
        for source in source_lib:
            for tag in self.tags:
                if tag in source_lib[source]:
                    sources.append(source)
                    break
        return sources


class RecipeLib:

    def __init__(self):
        self.raw = load.json_in_dirs(load.dirs(config.RECIPE_PATHS))
        self.recipes = tuple(Recipe(recipe) for recipe in self.raw)
        print(f'- Generated {len(self.recipes)} recipes')

    def find_recipes_of_obj(self, uid: str):
        result: list[Recipe] = []
        for recipe in self.recipes:
            if recipe.sources and uid == recipe.uid:
                result.append(recipe)
        return result

    def find_admin_recipes_of_obj(self, uid: str):
        result: list[Recipe] = []
        for recipe in self.recipes:
            if recipe.sources_admin and uid == recipe.uid:
                result.append(recipe)
        return result

    def find_recipes_that_use_obj(self, uid: str):
        result: list[Recipe] = []
        for recipe in self.recipes:
            for input_obj in recipe.input:
                if uid == input_obj.uid and not self.is_already_added(result, recipe):
                    result.append(recipe)
        return result

    def is_already_added(self, queue: list[Recipe], recipe: Recipe):
        for old in queue:
            if old.uid == recipe.uid:
                return True
        return False


class LootEntry(Item):

    def __init__(self, loot_entry: dict, weight_default=0.0):
        self.is_pool = bool(loot_entry.get('pool'))
        self.weight = str(loot_entry.get('weight', weight_default))
        super().__init__(loot_entry.get('item') or loot_entry.get('pool'))
        self.raw = loot_entry


class Loot:

    def __init__(self, loot: list):
        try:
            self.level = int(loot[0])
            self.values = dict(loot[1])
            self.pool_raw: tuple[dict] = tuple(self.values.get('pool', []))
            self.fill_raw: tuple[dict] = tuple(self.values.get('fill', []))
            self.pool = tuple(LootEntry(pool) for pool in self.pool_raw)
            self.fill = tuple(LootEntry(fill, 'always present') for fill in self.fill_raw)
            self.all = self.pool + self.fill
            self.rounds: tuple[tuple[float, int]] = tuple(self.values.get('poolRounds', []))
            self.raw = loot
        except Exception as e:
            print(f'Can\'t parse loot table: {loot}')
            raise e


class LootTable:

    def __init__(self, loot_list: list):
        try:
            self.entries_raw = tuple(loot for loot in loot_list if type(loot) == list)
            self.entries = tuple(Loot(loot) for loot in self.entries_raw)
            self.raw = loot_list
        except Exception as e:
            print(f'Can\'t parse loot list: {loot_list}')
            raise e


class LootLib(load.AbstractLib):

    def __init__(self):
        try:
            self.ext = 'treasurepools'
            self.tables_raw = self.get_tables(load.filepaths_in_dirs(load.dirs(config.LOOT_PATHS)))
            self.tables = {str(key): LootTable(self.tables_raw[key]) for key in self.tables_raw}
            self.tables = {key: self.tables[key] for key in self.tables if self.tables[key].entries}
            print(f'- Generated {len(self.tables)} loot tables ({len(self.tables_raw)} entries total found, including chests)')
        except Exception as e:
            print(f'Can\'t parse loot library: {self.tables}')
            raise e

    def find_loot_of_obj(self, loot_uids: dict[str, str]):
        result: dict[str, LootTable] = {}
        for name in loot_uids:
            for table_uid in self.tables:
                if loot_uids[name] == table_uid:
                    result[name] = self.tables[table_uid]
        return result

    def find_obj_loot_of_obj(self, obj: dict):
        result: dict[str, LootTable] = {}
        for i, option in enumerate(self.get_drop_options(obj)):
            result.update({f'drop option {i + 1}': LootTable([[0, {'pool': [{'weight':1.0,'item':[item.uid, item.n]} for item in option]}]])})
        return result

    def find_loot_that_drops_obj(self, obj_uid: str) -> list[str]:
        result = []
        for table in self.tables:
            for loot in self.tables[table].entries:
                source_uid = None
                for f in loot.all:
                    if obj_uid == f.uid:
                        source_uid = table
                        break
                if source_uid:
                    result.append(source_uid)
                    break
        return result

    def find_objs_that_drop_obj(self, obj_uid: str, obj_lib: list[wiki.Page], use_bid=False) -> list[str]:
        result = []
        for obj in obj_lib:
            for option in self.get_drop_options(obj.raw):
                if self.find_first_option(obj_uid, option):
                    result.append(obj.bid if use_bid else obj.uid)
                    break
        return result

    def find_first_option(self, uid: str, items: list[Item]):
        for item in items:
            if uid == item.uid:
                return item.uid

    def find_pool_uids_of_obj(self, loot_uids: list[str]):
        result = []
        for loot_uid in loot_uids:
            if loot_uid in self.tables:
                for loot in self.tables[loot_uid].entries:
                    for f in loot.all:
                        if f.is_pool and f.uid in self.tables:
                            result.extend(self.find_pool_uids_of_obj([f.uid]))
        return list(set(result + loot_uids))

    def get_drop_options_raw(self, obj: dict) -> list[list]:
        return obj.get('breakDropOptions', []) + obj.get('smashDropOptions', []) + dict(obj.get('dropConfig', {})).get('drops', [])

    def get_drop_options(self, obj: dict):
        return tuple(tuple(Item(item) for item in option) for option in self.get_drop_options_raw(obj))

    def get_loot_sources(self, uid: str, obj_lib: list[wiki.Page], use_bid=False):
        loot_sources = self.find_loot_that_drops_obj(uid)
        loot_sources_objects = self.find_objs_that_drop_obj(uid, obj_lib, use_bid)
        uids = {'loot': [], 'drop': [], 'chest': [], 'uids': []}
        for item_uid in set(loot_sources + loot_sources_objects):
            item_objs = {'loot': [], 'drop': [], 'chest': []}
            if item_uid in loot_sources:
                item_objs['loot'].extend(find_objs(item_uid, obj_lib, self, is_pool=True))
                item_objs['chest'].extend(find_objs(item_uid, obj_lib, self, is_chest=True))
            if item_uid in loot_sources_objects:
                item_objs['drop'].extend(find_objs(item_uid, obj_lib))
            if not item_objs['loot'] and not item_objs['drop'] and not item_objs['chest']:
                uids['uids'].append(item_uid)
            else:
                uids['loot'].extend(item_objs['loot'])
                uids['chest'].extend(item_objs['chest'])
                uids['drop'].extend(item_objs['drop'])
        return FilterResult(uids)


class FilterResult:

    def __init__(self, data: dict):
        self.loot: tuple[wiki.Page] = tuple(data['loot'])
        self.drop: tuple[wiki.Page] = tuple(data['drop'])
        self.chest: tuple[wiki.Page] = tuple(data['chest'])
        self.uids: tuple[str] = tuple(sorted(data['uids']))

    @property
    def all_objs(self):
        return sort(unique(self.loot + self.drop + self.chest))

    @property
    def obj_uids(self) -> list[str]:
        return sorted(tuple(obj.uid for obj in self.all_objs)) + sorted(tuple(obj.wid for obj in self.all_objs))

    @property
    def all_uids(self) -> list[str]:
        return sorted(list(set(self.uids + self.obj_uids)))

    @property
    def uid_sources(self):
        sources = {}
        for page in self.loot:
            sources.update({page.bid: sources.get(page.bid, []) + ['loot']})
        for page in self.drop:
            sources.update({page.bid: sources.get(page.bid, []) + ['drop']})
        for page in self.chest:
            sources.update({page.bid: sources.get(page.bid, []) + ['chest']})
        for s in self.uids:
            sources.update({s: sources.get(s, []) + ['uids']})
        return sources


class Library:

    def __init__(self):
        self.cockpit = load.CockpitLib()
        self.chests = load.ChestLib()
        self.bps = RecipeLib()
        self.loot = LootLib()
        self.radios = load.RadioLib().tables
        self.names = {}
        self.uids = {}
        self.tags = {}
        self.wids = {}
        # self.obj = self.gen_obj_list()
        # for obj in self.obj:
        #     self.names.update(obj.aliases)
        #     self.uids.update({obj.uid: (obj.name_wiki, obj.icon, obj.name)})
        #     self.wids.update({obj.wid: (obj.name_wiki, obj.icon, obj.name)})
        #     for tag in obj.tags:
        #         self.tags[tag] = self.tags[tag] + 1 if self.tags.get(tag) else 1
        # self.obj_dict = self.gen_obj_dict()
        # self.obj.reverse()
        # self.names.update(self.gen_names())
        self.tags = dict(sorted(self.tags.items()))
        self.names = dict(sorted(self.names.items()))
        self.uids = dict(sorted(self.uids.items()))
        self.wids = dict(sorted(self.wids.items()))
        self.full = {**self.names, **self.uids}
        # [print(l, names[l]) for l in names]
        # [print(l, self.tags[l]) for l in self.tags]

    def get_total(self, main_cat: str, objs: dict):
        return sum([self.get_subtotal(objs[main_cat][super_cat]) for super_cat in objs[main_cat]])


    def get_subtotal(self, cats_objs: dict):
        return sum([len(cats_objs[cat]) for cat in cats_objs])

    def gen_obj_list(self) -> list[wiki.Page]:
        print(f'- Creating page objects...')
        paths = load.filepaths_in_dirs(load.dirs(config.PATHS), ('patch', 'md'))
        obj_lib: list[wiki.Page] = [wiki.build(fp, self.cockpit, self.chests) for fp in paths]
        print(f'  - Loaded {len(obj_lib)} potential page objects...')
        obj_lib = [p for p in obj_lib if p]
        print(f'  - Filtered out empty, {len(obj_lib)} page objects left...')
        obj_lib.sort(key=lambda x: x.name_wiki)
        print(f'  - Sorted page objects...')
        print(f'  - Filled links...')
        return obj_lib

    def gen_obj_dict(self) -> list[wiki.Page]:
        print(f'- Categorizing page objects...')
        objs: dict[str, dict[str, dict[str, list[wiki.Page]]]] = {}
        for main_cat in config.CATEGORIES:
            objs[main_cat] = objs.get(main_cat, {})
            for super_cat in config.CATEGORIES[main_cat]:
                objs[main_cat][super_cat] = objs[main_cat].get(super_cat, {})
                for cat in config.CATEGORIES[main_cat][super_cat]:
                    objs[main_cat][super_cat][cat] = [obj for obj in self.obj if obj.cat == cat and obj.name]
        return objs

    def gen_names(self) -> dict[list]:
        print(f'- Creating aliases...')
        links = {}
        for main_cat in self.obj_dict:
                links.update({wiki.md.up(main_cat): (wiki.md.up(main_cat), None)})
                total = self.get_total(main_cat, self.obj_dict)
                if len(self.obj_dict[main_cat]) > 1:
                    if total < 200:
                        for super_cat in self.obj_dict[main_cat]:
                            links.update({wiki.md.up(wiki.md.safe(super_cat)): (wiki.md.urlf(main_cat) + "#" + wiki.md.urlf(super_cat), None)})
                            for cat in self.obj_dict[main_cat][super_cat]:
                                cat_link = wiki.md.safe(wiki.md.many(config.flat_cats[cat]))
                                links.update({wiki.md.up(cat_link): (wiki.md.urlf(main_cat) + "#" + wiki.md.urlf(cat_link), None)})
                    else:
                        for super_cat in self.obj_dict[main_cat]:
                            links.update({wiki.md.up(wiki.md.safe(super_cat)): (wiki.md.urlf(super_cat), None)})
                            for cat in self.obj_dict[main_cat][super_cat]:
                                cat_link = wiki.md.safe(wiki.md.many(config.flat_cats[cat]))
                                links.update({wiki.md.up(cat_link): (wiki.md.urlf(super_cat) + "#" + wiki.md.urlf(cat_link), None)})
                else:
                    for super_cat in self.obj_dict[main_cat]:
                        cats_objs = self.obj_dict[main_cat][super_cat]
                        if total < 200:
                            for cat in cats_objs:
                                cat_link = wiki.md.safe(wiki.md.many(config.flat_cats[cat]))
                                links.update({wiki.md.up(cat_link): (wiki.md.urlf(main_cat + "#" + cat_link), None)})
                        else:
                            for cat in cats_objs:
                                cat_link = wiki.md.safe(wiki.md.many(config.flat_cats[cat]))
                                links.update({wiki.md.up(cat_link): (wiki.md.urlf(cat_link), None)})
        return links


def find_objs(uid: str, obj_lib: list[wiki.Page], loot_lib: LootLib=None, is_pool=False, first=False, is_chest=False):
    objs = []
    for obj in obj_lib:
        if (
            (not is_pool and obj.bid == uid) or
            (is_pool and uid in loot_lib.find_pool_uids_of_obj(list(obj.loot_uids.values()))) or
            (is_chest and uid in loot_lib.find_pool_uids_of_obj(obj.chest_loot_uids))
        ):
            objs.append(obj)
            if first:
                break
    return sort(unique(objs))

def find_obj(uid, obj_lib: list[wiki.Page], loot_lib: LootLib=None, is_pool=False):
    objs = find_objs(uid, obj_lib, loot_lib, is_pool=is_pool, first=True)
    return objs[0] if objs else None

def unique(objs: list[wiki.Page]):
    seen = set()
    seen_add = seen.add
    return [x for x in objs if not (x in seen or seen_add(x))]

def sort(objs: list[wiki.Page]):
    return sorted(objs, key=lambda x: x.name_wiki)
