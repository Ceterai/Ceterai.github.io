import re
import db

def star(s: str) -> str:
    return s.replace('', '★').replace('оЂ¤', '★').replace('«', '❤') if s else s

def safe(s: str) -> str:
    return star(s).replace(': ', ' ').replace(':_', ' ').replace(':', ' ').replace(':-', ' ').replace('/', ' by ').replace('★', '').replace('❤', '').rstrip() if s else s

def up(s: str) -> str:
    return ' '.join([word if word == word.upper() else word.capitalize() for word in s.split(' ')]) if s else s

def urlf(s: str) -> str:
    return safe(s).replace(' ', '-').replace('_', '-').replace('"', '') if s else s

def filename(s: str) -> str:
    return f'{urlf(s)}.md'

def icon(s: str|list) -> str:
    return (f'![ ]({s})' if type(s) == str else db.img(*s)) if s else ''

def qs(s: str) -> str:
    return f'`{s}`' if s else ''

def n(s: str = '') -> str:
    return f'{s}\n\n' if s else ''

# Blocks

def nm(s: str|list[str] = '', condition: bool = True) -> str:
    if type(s) in (list, tuple):
        s = '  \n'.join([s1 for s1 in s if s1])
    return f'\n{s}\n' if s and condition else ''

def param(s: str = '', val: str = '', condition: bool = True) -> str:
    return f'{s}: {val}' if s and val and condition else ''

def loop(func, strs: list[str], delim: str = ' ') -> str:
    return delim.join(tuple(func(s) for s in strs or [] if s))

def h1(s: str = '', condition: bool = True) -> str:
    return nm(f'# {s}') if s and condition else ''

def h2(s: str = '', condition: bool = True) -> str:
    return nm(f'## {s}') if s and condition else ''

def h3(s: str = '', condition: bool = True) -> str:
    return nm(f'### {s}') if s and condition else ''

def h4(s: str = '', condition: bool = True) -> str:
    return nm(f'#### {s}') if s and condition else ''

def line(condition: bool = True) -> str:
    return nm('---') if condition else ''

# Lists

def li(s: str) -> str:
    return f'- {s}'

def ln(s: str) -> str:
    return f'{li(s)}\n'

def l(lst: list) -> str:
    return ''.join([ln(s) for s in lst])

def many(s: str) -> str:
    return '' if not s else (s + 'es' if s[-1] == 's' or s[-1] == 'h' else (s[:-1] + 'ies' if s[-1] == 'y' else s + 's'))

def item(name: str, link: str, icon: str = None) -> str:
    return (f'{icon} ' if icon else '') + (f'[[ {name}|{link} ]]' if link[0] != '/' and link[:8] != 'https://' and link[:7] != 'http://' else f'[{name}]({link})')

def list_link(name: str, link: str, icon: str = None) -> str:
    return li(item(name, link, icon))

def build_item(name: str, icon: str = None) -> str:
    return item(up(safe(name)), urlf(name), icon)

def build_list_link(name: str, icon: str = None) -> str:
    return li(build_item(name, icon))

def mini(s: str) -> str:
    return safe(s).replace('★', '').replace('❤', '').lower().replace('\'', '').replace(' ', '').replace('-', '').replace('.', '').replace('_', '').replace('"', '')

def compare(s1: str, s2: str) -> str:
    return mini(s1) == mini(s2)

def full_compare(s1: str, s2: str) -> str:
    return (compare(s1, s2) or compare(many(s1), s2) or compare(s1, many(s2)))

def uid_to_name(s: str) -> str:
    s = s[3:] if s[:3] == 'ct_' else s
    return up(s.replace('_', ' ').replace('-', ' '))

def camel_to_name(s: str) -> str:
    return re.sub(r'([A-Z])', r' \1', s).capitalize()

def clean(s: str, l: str = '', r: str = '') -> str:
    return safe(re.sub(r'(\^[^\s\;\^]*\;)([^\;\^]*)(\^reset\;)', l + r'\2' + r, s)) if s else s

def enrich(s: str, link_lib: dict) -> str:
    segments = re.sub(
        r'(\^(?!reset|#ff8888|#88ff88|gray|green|orange|yellow|cyan|red)[^\s\;\^]*\;)([^\;\^]*)(\^(?=reset|#ff8888|#88ff88|gray|green|orange|yellow|cyan|red)[^\s\;\^]*\;)',
        r'^!sep;\2^!end;^!sep;',
        s
    ).split('^!sep;') if s else ''
    for i in range(len(segments)):
        if '^!end;' in segments[i]:
            segments[i] = replace(segments[i][:-6], link_lib)
    s = star(''.join(segments))
    s = re.sub(r'(\^(?=#ff8888|#88ff88|green|yellow|red)[^\s\;\^]*\;)([^\;\^]*)(\^reset\;)', r'**\2**', s)
    s = re.sub(r'(\^(?=gray)[^\s\;\^]*\;)([^\;\^]*)(\^reset\;)', r'*\2*', s)
    s = re.sub(r'(\^(?=orange|cyan)[^\s\;\^]*\;)([^\;\^]*)(\^reset\;)', r'\2', s)
    return re.sub(r'(\^[^\s\;\^]*\;)', '', s)

def replace(s: str, link_lib: dict, uid=False, no_dmg=False, custom=None) -> str:
    l = lambda s1, s2: s1.title() if uid else s2
    c = compare if uid else full_compare
    def search(old_s, objs, found_f):
        for r in objs:
            if c(r, old_s):
                return found_f(r)

    if not uid:
        s = star(s)
        if s2 := search(s, db.RACES, lambda r: item(l(r, s), db.RACES[r])): return s2
        if s2 := search(s, db.PAGES, lambda r: item(l(r, s), r, icon(db.PAGES[r]))): return s2
    if not no_dmg:
        if s2 := search(s, db.ELEMENTS, lambda r: db.ELEMENTS[r]): return s2
    if s2 := search(s, db.ALIASES, lambda r: item(l(r, s), db.ALIASES[r], icon(db.ICONS.get(r)))): return s2
    if s2 := search(s, link_lib, lambda r: item(((link_lib[r][2] if len(link_lib[r]) > 2 else r) if uid else s), link_lib[r][0], link_lib[r][1])): return s2
    if s2 := search(s, db.WIKI_LINKS, lambda r: db.link(l(db.WIKI_LINKS[r][0], s), db.WIKI_LINKS[r][1], *db.WIKI_LINKS[r][2:])): return s2
    if custom:
        if s2 := search(s, custom, lambda r: enrich(custom[r], link_lib)): return s2
    return qs(s) if uid else item(s, urlf(s))
