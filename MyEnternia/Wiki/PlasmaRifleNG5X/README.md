# Plasma Rifle NG5X ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle_2.png" alt="Plasma Rifle NG5X ★ icon" loading="lazy" width="auto" height="16px"> **Plasma Rifle NG5X ★** is a legendary two-handed electric assault rifle.

This improved NG5 model has enhanced energy capacity due to the use of <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust).  
The integrated crystal acts as an energy booster, and the updated rapid generator allows for longer high loads.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle.png" alt="Plasma Rifle NG5 icon" loading="lazy" width="auto" height="16px"> [Plasma Rifle NG5](https://ceterai.github.io/MyEnternia/Wiki/PlasmaRifleNG5).

## Ingame

Species descriptions:

- Alta: These are sometimes attached to heavy machinery as an in-place defence mechanism.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Plasma Blast

A standard [plasma](https://ceterai.github.io/MyEnternia/Wiki/Alternia#damage) discharger.
Firemodes: auto, semiauto, single.

Parameters:

- Base Dps: 8
- Burst Params:
  - Count: 3
  - Interval: 0.1
- Default Fire Type: `auto`
- Energy Usage: 32
- Fire Time: 0.1
- Fire Types:
  - Auto:
    - Hold Time Max:
    - Press Params:
      - Sound: `auto`
      - Type: `ct_plasma_medium`
    - Press Type: `blast`
  - Semi:
    - Hold Time Max:
    - Press Params:
      - Count: 3
      - Interval: 0.1
      - Type: `ct_plasma_medium`
    - Press Type: `semi`
  - Single:
    - Hold Time Max:
    - Press Params:
      - Fire Time: 0.45
      - Inaccuracy: 0.02
      - Type: `ct_plasma_medium`
    - Press Type: `blast`

### Combat Switch

A combat-specific set of functions.
Press - launch a <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/throwables/ct_plasma_nade.png" alt="Plasma Nade icon" loading="lazy" width="auto" height="16px"> [Plasma Nade](https://ceterai.github.io/MyEnternia/Wiki/PlasmaNade);
Hold - change firemodes.

Parameters:

- Base Dps: 8
- Energy Usage: 36
- Fire Time: 0.8
- Fire Types:  `auto`,  `semi`,  `single`
- Hold Firemodes: `True`
- Press Params:
  - Type: `ct_plasma_nade_charge`
- Press Type: `nade`

## Sources

Can be crafted:

- Tier 2 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/upgrade_station/icon2.png) [Alta Upgrade Station](https://ceterai.github.io/MyEnternia/Wiki/AltaUpgradeStation) (takes 0.0s, outputs <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle_2.png" alt="Plasma Rifle NG5X ★ icon" loading="lazy" width="auto" height="16px"> Plasma Rifle NG5X ★ x*1*):
  - `spaceplasmarifle` x*1*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/throwables/ct_gheatsyn_shard.png" alt="Gheatsyn Shard icon" loading="lazy" width="auto" height="16px"> [Gheatsyn Shard](https://ceterai.github.io/MyEnternia/Wiki/GheatsynShard) x*1780*

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_alta_plasma_rifle-upgrade`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`assaultrifle`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Assaultrifle), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`plasma`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Plasma), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`rare`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rare), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/rifle/ct_alta_plasma_rifle.activeitem)
