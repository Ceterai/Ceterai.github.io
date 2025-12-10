# Plasma Rifle NG5

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle.png" alt="Plasma Rifle NG5 icon" loading="lazy" width="auto" height="16px"/> **Plasma Rifle NG5** is a rare two-handed electric assault rifle.

A rifled alternia [plasma](https://ceterai.github.io/MyEnternia/Wiki/Tags/Plasma) blaster, mostly used by combat and elite [alta](https://ceterai.github.io/MyEnternia/Wiki/Alta) forces.  
Its heavy casing contains a lot of isolation and enough space for a proper _rapid plasma generator_.

Can be upgraded to <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle_2.png" alt="Plasma Rifle NG5X ★ icon" loading="lazy" width="auto" height="16px"/> [Plasma Rifle NG5X ★](https://ceterai.github.io/MyEnternia/Wiki/PlasmaRifleNG5X) at the Weapon Upgrade Anvil.

## Ingame

Species descriptions:

- Alta: Remember when main NG models went plasmic? I remember. I think.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Plasma Blast

A standard [plasma](https://ceterai.github.io/MyEnternia/Wiki/Tags/Plasma) discharger.
Firemodes: auto, semiauto, single.

Parameters:

- Base Dps: 8
- Fire Time: 0.1
- Energy Usage: 32
- Burst Params:
  - Count: 3
  - Interval: 0.1
- Default Fire Type: `auto`
- Fire Types:
  - Auto:
    - Press Type: `blast`
    - Press Params:
      - Type: `ct_plasma_medium`
      - Sound: `auto`
    - Hold Time Max:
  - Semi:
    - Press Type: `semi`
    - Press Params:
      - Type: `ct_plasma_medium`
      - Count: 3
      - Interval: 0.1
    - Hold Time Max:
  - Single:
    - Press Type: `blast`
    - Press Params:
      - Type: `ct_plasma_medium`
      - Fire Time: 0.45
      - Inaccuracy: 0.02
    - Hold Time Max:

### Combat Switch

A combat-specific set of functions.
Press - launch a <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/throwables/ct_plasma_nade.png" alt="Plasma Nade icon" loading="lazy" width="auto" height="16px"/> [Plasma Nade](https://ceterai.github.io/MyEnternia/Wiki/PlasmaNade);
Hold - change firemodes.

Parameters:

- Base Dps: 8
- Energy Usage: 36
- Fire Time: 0.8
- Press Type: `nade`
- Press Params:
  - Type: `ct_plasma_nade_charge`
- Hold Firemodes: `True`
- Fire Types:  `auto`,  `semi`,  `single`

## Sources

Can be crafted:

- Tier 3 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon3.png) [Alta Crafting Station](https://ceterai.github.io/MyEnternia/Wiki/AltaCraftingStation) (takes 5s, outputs <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle.png" alt="Plasma Rifle NG5 icon" loading="lazy" width="auto" height="16px"/> Plasma Rifle NG5 x*1*):
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/phosicore.png" alt="Phosicore icon" loading="lazy" width="auto" height="16px"/> [Phosicore](https://ceterai.github.io/MyEnternia/Wiki/Phosicore) x*6*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/bion.png" alt="Bion Compound icon" loading="lazy" width="auto" height="16px"/> [Bion Compound](https://ceterai.github.io/MyEnternia/Wiki/BionCompound) x*3*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/eds.png" alt="EDS Armor icon" loading="lazy" width="auto" height="16px"/> [EDS Armor](https://ceterai.github.io/MyEnternia/Wiki/EDSArmor) x*3*

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"/> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_alta_plasma_rifle`
- Level: `5`
- Power: `3.0`
- Rarity: `Rare`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`assaultrifle`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Assaultrifle), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`plasma`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Plasma), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`rare`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rare), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle.activeitem)
