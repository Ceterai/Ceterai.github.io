import shutil
import time
import config
import load
import resources
import md
from wiki import Page
from body import get_body


# TIMER


class Timer:
    def __init__(self):
        self.start = time.time()
        self.last = self.start
        self.last2 = self.last
    def check(self, last=None, new=None):
        return round((new or time.time()) - (last or self.last), 1)
    def tick(self):
        new = time.time()
        elapsed = self.check(self.last, new)
        self.last = new
        self.last2 = new
        return elapsed
    def tick2(self):
        new = time.time()
        elapsed = self.check(self.last2, new)
        self.last2 = new
        return elapsed
    def total(self):
        return self.check(self.start)


# INFRASTRUCTURE


def write_objs(cat_objs: list[Page], path: str, cat: str, lib: resources.Library):
    item_list = []
    for obj in cat_objs:
        item_list.append(md.ln(obj.link))
        item_list.extend([f'  {link}' for link in obj.list_item_upgrades])
        with load.open_page(path, md.filename(obj.name_wiki)) as save:
            save.writelines(get_body(obj, lib, cat))
    return item_list


def generate(subdirs=False):
    timer = Timer()
    print(f'Initializing library...')
    lib = resources.Library()
    print(f'Initialized library in {timer.tick()}s...')

    if subdirs:
        print(f'Creating subfolders...')
        for main_cat in config.CATEGORIES:
            path = load.os.path.join(config.ROOT_TARGET, main_cat)
            if not load.os.path.exists(path): load.os.makedirs(path)

    print(f'Creating pages...')
    for main_cat in lib.obj_dict:
        total = lib.get_total(main_cat, lib.obj_dict)
        with load.open_page(main_cat if subdirs else None, md.filename(md.up(main_cat))) as all_save:
            if len(lib.obj_dict[main_cat]) > 1:
                all_save.write(f'The mod adds a total of {total} {main_cat}.\n\n## Navigation\n\n')
                if total < 200:
                    for super_cat in lib.obj_dict[main_cat]:
                        all_save.write(f'{md.list_link(md.up(md.safe(super_cat)), md.urlf(main_cat) + "#" + md.urlf(super_cat))}\n')
                        for cat in lib.obj_dict[main_cat][super_cat]:
                            if len(lib.obj_dict[main_cat][super_cat][cat]):
                                cat_link = md.safe(f'{md.many(config.flat_cats[cat])}')
                                cat_icon = lib.obj_dict[main_cat][super_cat][cat][0].icon
                                all_save.write(f'  {md.list_link(md.up(cat_link), md.urlf(main_cat) + "#" + md.urlf(cat_link), cat_icon)}\n')
                    for super_cat in lib.obj_dict[main_cat]:
                        cats_objs = lib.obj_dict[main_cat][super_cat]
                        all_save.write(f'\n## {md.up(md.safe(super_cat))}\n\n')
                        all_save.write(f'There are {lib.get_subtotal(cats_objs)} entries in this category.\n')
                        for cat in cats_objs:
                            if len(cats_objs[cat]):
                                all_save.write(f'\n### {md.up(md.many(config.flat_cats[cat]))}\n\n')
                                all_save.write(f'The mod adds a total of {len(cats_objs[cat])} {md.many(config.flat_cats[cat])}:\n\n')
                                cat_link = md.safe(config.flat_cats[cat])
                                cat_link = md.item(cat_link, md.urlf(main_cat) + "#" + md.urlf(md.many(cat_link)))
                                all_save.writelines(write_objs(cats_objs[cat], main_cat if subdirs else None, cat_link, lib))
                        print(f'- Created all {super_cat} in {timer.tick2()}s...')
                else:
                    for super_cat in lib.obj_dict[main_cat]:
                        all_save.write(f'{md.list_link(md.up(md.safe(super_cat)), md.urlf(super_cat))}\n')
                        for cat in lib.obj_dict[main_cat][super_cat]:
                            if len(lib.obj_dict[main_cat][super_cat][cat]):
                                cat_link = md.safe(f'{md.many(config.flat_cats[cat])}')
                                cat_icon = lib.obj_dict[main_cat][super_cat][cat][0].icon
                                all_save.write(f'  {md.list_link(md.up(cat_link), md.urlf(super_cat) + "#" + md.urlf(cat_link), cat_icon)} ({len(lib.obj_dict[main_cat][super_cat][cat])} {main_cat})\n')
                    for super_cat in lib.obj_dict[main_cat]:
                        cats_objs = lib.obj_dict[main_cat][super_cat]
                        with load.open_page(main_cat if subdirs else None, md.filename(md.up(super_cat))) as cat_save:
                            cat_save.write(f'> Main page: {md.build_item(main_cat)}\n\n')
                            cat_save.write(f'The mod adds a total of {lib.get_subtotal(cats_objs)} {super_cat}.\n')
                            for cat in cats_objs:
                                if len(cats_objs[cat]):
                                    cat_save.write(f'\n## {md.up(md.many(config.flat_cats[cat]))}\n\n')
                                    cat_save.write(f'The mod adds a total of {len(cats_objs[cat])} {md.many(config.flat_cats[cat])}:\n\n')
                                    cat_link = md.safe(config.flat_cats[cat])
                                    cat_link = md.item(cat_link, md.urlf(super_cat) + "#" + md.urlf(md.many(cat_link)))
                                    cat_save.writelines(write_objs(cats_objs[cat], main_cat if subdirs else None, cat_link, lib))
                        print(f'- Created all {super_cat} in {timer.tick2()}s...')
            else:
                for super_cat in lib.obj_dict[main_cat]:
                    cats_objs = lib.obj_dict[main_cat][super_cat]
                    if total < 200:
                        if len(cats_objs) > 1:
                            all_save.write(f'The mod adds a total of {total} {main_cat}.\n')
                        for cat in cats_objs:
                            if len(cats_objs[cat]):
                                if len(cats_objs) > 1:
                                    all_save.write(f'\n## {md.up(md.many(config.flat_cats[cat]))}\n\n')
                                    all_save.write(f'The mod adds a total of {len(cats_objs[cat])} {md.many(config.flat_cats[cat])}:\n\n')
                                else:
                                    all_save.write(f'The mod adds a total of {total} {main_cat}.\n')
                                cat_link = md.safe(config.flat_cats[cat])
                                cat_link = md.item(cat_link, md.urlf(main_cat))
                                all_save.writelines(write_objs(cats_objs[cat], main_cat if subdirs else None, cat_link, lib))
                    else:
                        all_save.write(f'The mod adds a total of {total} {main_cat}.\n\n## Navigation\n\n')
                        for cat in cats_objs:
                            if len(cats_objs[cat]):
                                cat_link = md.safe(f'{md.many(config.flat_cats[cat])}')
                                cat_icon = lib.obj_dict[main_cat][super_cat][cat][0].icon
                                all_save.write(f'{md.list_link(md.up(cat_link), md.urlf(cat_link), cat_icon)} ({len(cats_objs[cat])} {main_cat})\n')
                                with load.open_page(main_cat if subdirs else None, md.filename(md.up(cat_link))) as cat_save:
                                    cat_save.write(f'> Main page: {md.build_item(main_cat)}\n\n')
                                    cat_save.write(f'The mod adds a total of {len(cats_objs[cat])} {cat_link}:\n\n')
                                    cat_link = md.safe(config.flat_cats[cat])
                                    cat_link = md.item(cat_link, md.up(md.urlf(md.many(cat_link))))
                                    cat_save.writelines(write_objs(cats_objs[cat], main_cat if subdirs else None, cat_link, lib))
        print(f'Created all {main_cat} ({total}) in {timer.tick()}s...')
    # Pasting manually written pages on top of generated ones
    pages = load.os.path.join(config.ROOT_TARGET, 'raw', 'manual')
    mds = [load.os.path.join(pages, f) for f in load.os.listdir(pages) if f[-3:] == '.md']
    for f in mds:
        shutil.copy(f, config.ROOT_TARGET)
    print(f'Copied manual pages ({len(mds)}) in {timer.tick()}s...')
    # Pasting manually written pages on top of generated ones 2
    pages = load.os.path.join(config.ROOT_SOURCE, '.meta', 'wiki', 'manual')
    mds = [load.os.path.join(pages, f) for f in load.os.listdir(pages) if f[-3:] == '.md']
    for f in mds:
        with load.open_page(None, load.get_filename(f)) as mdf:
            mdf.write(md.enrich(load.md(f, ''), lib.names))
    print(f'Copied semi-manual pages ({len(mds)}) in {timer.tick()}s...')
    print(f'Done in {timer.total()}s.')
    """
    print(f'Creating homepage...')
    with load.open_page('', 'Home.md') as home:
        home.write(f'# {config.MOD_NAME}\n\nWelcome to the mod wiki! Here you can find all information and lore related to it.\n\n## Navigation\n\n<table> <tbody valign="top">\n<tr valign="middle">')
        for main_cat in objs:
            home.write(f'<th>\n\n{md.item(md.up(md.safe(main_cat)), md.urlf(main_cat))}\n</th>')
        home.write(f'</tr>\n<tr>')
        for main_cat in objs:
            home.write(f'<td>\n\n')
            if len(objs[main_cat]) > 1:
                for super_cat in objs[main_cat]:
                    if total < 200:
                        home.write(f'{md.list_link(md.up(md.safe(super_cat)), md.urlf(main_cat) + "#" + md.urlf(super_cat))}\n')
                    else:
                        home.write(f'{md.list_link(md.up(md.safe(super_cat)), md.urlf(super_cat))}\n')
                    for cat in objs[main_cat][super_cat]:
                        if len(objs[main_cat][super_cat][cat]):
                            cat_link = md.safe(f'{md.many(config.flat_cats[cat])}')
                            cat_icon = objs[main_cat][super_cat][cat][0].icon
                            if total < 200:
                                home.write(f'  {md.list_link(md.up(cat_link), md.urlf(main_cat) + "#" + md.urlf(cat_link), cat_icon)}\n')
                            else:
                                home.write(f'  {md.list_link(md.up(cat_link), md.urlf(super_cat) + "#" + md.urlf(cat_link), cat_icon)}\n')
            else:
                for super_cat in objs[main_cat]:
                    cats_objs = objs[main_cat][super_cat]
                    for cat in cats_objs:
                        if len(cats_objs[cat]):
                            cat_link = md.safe(f'{md.many(config.flat_cats[cat])}')
                            cat_icon = objs[main_cat][super_cat][cat][0].icon
                            if total < 200:
                                home.write(f'{md.list_link(md.up(cat_link), md.urlf(main_cat) + "#" + md.urlf(cat_link), cat_icon)}\n')
                            else:
                                home.write(f'{md.list_link(md.up(cat_link), md.urlf(cat_link), cat_icon)}\n')
            home.write(f'\n</td>')
    """

def compile():
    pages = load.os.path.join(config.ROOT_TARGET, 'pages')
    paths = [r[0] for r in list(load.os.walk(config.ROOT_TARGET))]
    for path in paths:
        mds = [load.os.path.join(path, f) for f in load.os.listdir(path) if f[-3:] == '.md']
        for f in mds:
            # shutil.copy(f, pages + f.replace(path, ''))
            pass

# compile() MOVES FILES!!!
generate()
