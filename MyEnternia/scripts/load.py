import os
import pyjson5
import re

import config


def single_root(file_path: str, root=config.ROOT_SOURCE) -> str:
    return root + file_path.replace(root, '')


def text(file_path: str, root=config.ROOT_SOURCE) -> str:
    if file_path:
        with open(single_root(file_path, root), encoding='utf-8') as fp:
            return ''.join(fp.readlines())
    return ''

def json(file_path: str, root=config.ROOT_SOURCE) -> dict[str]:
    if raw := text(file_path, root):
        lines = re.sub(r'((?<!:)\/\/.*)\n', r'\n', raw).replace('\n', '  ')
        return pyjson5.loads(lines)
    return {}

def md(file_path: str, root=config.ROOT_SOURCE, **kwargs) -> str:
    if md := text(file_path, root):
        for arg in kwargs:
            md = md.replace('<%%' + arg + '%%>', kwargs[arg])
        return md
    return ''

def ext_is_allowed(name: str, skipped_exts=tuple()) -> bool:
    return '.' in name and ext(name) not in (config.SKIPPED_EXTS + skipped_exts)

def dirs(roots: list[str], source: str = config.ROOT_SOURCE) -> list[str]:
    dir_paths = []
    for path in roots:
        dir_paths.extend([r[0] for r in list(os.walk(source + '/' + path))])
    return dir_paths

def filepaths_in_dir(dir_path: str, skipped_exts=tuple()) -> list[str]:
    return [os.path.join(dir_path, fn) for fn in os.listdir(dir_path) if ext_is_allowed(fn, skipped_exts)]

def filepaths_in_dirs(dir_paths: list[str], skipped_exts=tuple()) -> list[str]:
    filepath_list = []
    for dir_path in dir_paths:
        filepath_list.extend(filepaths_in_dir(dir_path, skipped_exts))
    return filepath_list

def json_in_dir(dir_path: str, skipped_exts=tuple()) -> list[dict]:
    return [json(fp) for fp in filepaths_in_dir(dir_path, skipped_exts)]

def json_in_dirs(dir_paths: list[str], skipped_exts=tuple()) -> list[dict]:
    obj_list = []
    for dir_path in dir_paths:
        obj_list.extend(json_in_dir(dir_path, skipped_exts))
    return obj_list

# Write

def open_page(path: str, filename: str):
    return open(os.path.join(config.ROOT_TARGET, path or '', filename), 'w', encoding="utf-8")

def dump(body: str, path: str, filename: str):
    with open_page(path, filename) as save:
        save.write(body)

def ext(path: str):
    return path.split('.')[-1]

def get_filename(path: str):
    return os.path.basename(path)

def get_name(path: str):
    return '.'.join(get_filename(path).split('.')[:-1])

def get_patches(obj):
    if len(obj) > 0 and type(obj[0]) == list:
        return obj[0]
    return obj


# Patches


def merge_patches(source: dict, dest: dict):
    for k, v in source.items():
        if isinstance(v, dict):
            node = dest.setdefault(k, {})
            merge_patches(v, node)
        elif isinstance(v, list):
            dest.setdefault(k, [])
            dest[k].extend(v)
        else:
            dest[k] = v
    return dest


def decode_patch_list(patch_list):
    obj: dict[str] = {}
    for patch in patch_list:
        op: str = patch['op']
        if op in ('add', 'replace', ):
            path: str = patch['path']
            value: str = patch['value']
            path = path[1:].split('/')
            for i in range(len(path)-1, -1, -1):
                if path[i] == '-':
                    value = [value]
                else:
                    value = {path[i]: value}
            obj = merge_patches(value, obj)
    return obj


class AbstractLib:

    def get_tables(self, paths: list[str]):
        raw: dict[str] = {}
        for path in paths:
            if path.endswith(f'{self.ext}.patch'):
                patch_list = json(path)
                raw.update(decode_patch_list(patch_list))
            elif ext(path) == self.ext:
                obj = json(path)
                raw.update(obj)
        return raw

    def get_path(self, patch: dict) -> str:
        return patch.get('path', '')

    def get_pathname(self, patch: dict) -> str:
        return self.get_path(patch).replace('/', '')

    def get_value(self, patch: dict, default={}) -> dict:
        return patch.get('value', default)


class CockpitLib(AbstractLib):

    def __init__(self):
        self.patches = get_patches(json(config.COCKPIT_CONFIG))
        self.tables = self.get_all_tables()
        self.weather = self.get_weather()
        print(f'- Generated {len(self.weather)} weather entries')

    def is_weather(self, path: str):
        return path[:17] == '/displayWeathers/'

    def get_all_tables(self):
        tables: dict[str] = {}
        for patch in self.patches:
            tables.update({self.get_path(patch): self.get_value(patch)})
        return tables

    def get_weather(self):
        return { k.replace('/displayWeathers/', ''): self.tables[k] for k in self.tables if self.is_weather(k)}


class ChestLib(AbstractLib):

    def __init__(self):
        self.ext = 'treasurechests'
        self.tables: dict[str, list[dict]] = self.get_tables(filepaths_in_dirs(dirs(config.LOOT_PATHS)))
        print(f'- Generated {len(self.tables)} chests')

    def get_loot(self):
        return { k: { { r.get('minimumLevel'): r.get('treasurePool') } for r in self.tables[k] } for k in self.tables }

    def get_objs_per_chest(self):
        result = {}
        for k in self.tables:
            chests = []
            for r in self.tables[k]:
                chests.extend(r.get('containers'))
            result.update({k: chests})
        return result

    def get_objs_flat(self):
        chests = []
        for r in (k := self.get_objs_per_chest()):
            chests.extend(k[r])
        return chests

    def get_chests_per_obj(self):
        result = {}
        for k in self.tables:
            for r in self.tables[k]:
                for c in r.get('containers'):
                    result[c] = result.get(c, []) + [k]
        return result

    def get_pools_per_obj(self):
        result: dict[str, dict[str, dict[str, list[str]]]] = {}
        for k in self.tables:
            for r in self.tables[k]:
                for c in r.get('containers'):
                    result[c] = result.get(c, {})
                    result[c][k] = result[c].get(k, {})
                    result[c][k][r.get('minimumLevel')] = result[c][k].get(r.get('minimumLevel'), [])
                    result[c][k][r.get('minimumLevel')] = result[c][k][r.get('minimumLevel')] + [r.get('treasurePool')]
        return result

    def get_objs_by_chest(self, chest_uid: str) -> list[str]:
        return self.get_objs_per_chest().get(chest_uid, [])

    def get_pools_by_obj(self, uid: str):
        return self.get_pools_per_obj().get(uid, {})

    def get_pools_by_obj_flat(self, uid: str):
        result: list[str] = []
        pools = self.get_pools_by_obj(uid)
        for chest_uid in pools:
            for level in pools[chest_uid]:
                result.extend(pools[chest_uid][level])
        return result


class RadioLib(AbstractLib):

    def __init__(self):
        self.ext = 'radiomessages'
        self.tables: dict[str, dict] = self.get_tables(filepaths_in_dirs(dirs(config.RADIO_PATHS)))
        self.msgs = {table: self.tables[table]['text'] for table in self.tables}
        print(f'- Generated {len(self.tables)} radio messages')
