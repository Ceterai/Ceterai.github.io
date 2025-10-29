# Impulse Rifle NG4

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle.png" alt="Impulse Rifle NG4 icon" loading="lazy" width="auto" height="16px"/> **Impulse Rifle NG4** is an uncommon two-handed electric assault rifle.

A rifled ceternia impulse blaster, mostly used by [alta](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta) security to suppress threats. Relatively harmless.  
This long-range high-precision energy instrument can generate long-lasting impulses, able to travel without losing height.

Can be upgraded to <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle_2.png" alt="Impulse Rifle NG4X ★ icon" loading="lazy" width="auto" height="16px"/> [Impulse Rifle NG4X ★](https://ceterai.github.io/MyEnternia/Wiki/ImpulseRifleNG4X) at the Weapon Upgrade Anvil.

## Ingame

Species descriptions:

- Alta: What a classic. You can see a lot of these held by vardas guarding <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/codex/alta/ebook/security.png" alt="Alta Cities icon" loading="lazy" width="auto" height="16px"/> [alta cities](https://ceterai.github.io/MyEnternia/Wiki/AltaCities).

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Impulse Blast

A standard [impulse](https://ceterai.github.io/MyEnternia/Wiki/Tags/Impulse) blast with high precision.
Firemodes: charge, semiauto.

Parameters:

- Base Dps: 8
- Energy Usage: 32
- Fire Time: 0.8
- Default Fire Type: `charge`
- Fire Types:
  - Charge:
    - Press Type: `blast`
    - Press Params:
      - Type: `ct_impulse_medium`
      - Sound: `primary_press`
      - Inaccuracy: 0.005
    - Hold Type: `blast`
    - Hold Params:
      - Type: `ct_impulse_large`
      - Sound: `primary_hold`
      - Inaccuracy: 0.005
    - Hold Start: `charge`
    - Hold Loop: `charging`
  - Semi:
    - Press Type: `semi`
    - Press Params:
      - Type: `ct_impulse_medium`
      - Count: 2
      - Interval: 0.1
      - Inaccuracy: 0.005
    - Hold Time Max:

### Security Switch

All a security unit needs with a rifle.
Press - change attachments: none, flashlight;
Hold - change firemodes.

Parameters:

- Fire Types:  `charge`,  `semi`
- Attachments:  `none`,  `flashlight`

## Usage

### Crafting

Can be used to craft:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle_mk2.png" alt="Impulse Rifle NG4-2 icon" loading="lazy" width="auto" height="16px"/> [Impulse Rifle NG4-2](https://ceterai.github.io/MyEnternia/Wiki/ImpulseRifleNG4-2)

## Sources

Can be crafted:

- Tier 2 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon2.png) [Alta Crafting Station](https://ceterai.github.io/MyEnternia/Wiki/AltaCraftingStation) (takes 4.5s, outputs <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle.png" alt="Impulse Rifle NG4 icon" loading="lazy" width="auto" height="16px"/> Impulse Rifle NG4 x*1*):
  - <img src="https://starbounder.org/mediawiki/images/9/94/Titanium_Bar.png" alt="Titanium Bar icon" loading="lazy" width="14px" height="13px"/> [Titanium Bar](https://starbounder.org/Titanium_Bar) x*2*
  - <img src="https://starbounder.org/mediawiki/images/0/09/Durasteel_Bar.png" alt="Durasteel Bar icon" loading="lazy" width="14px" height="13px"/> [Durasteel Bar](https://starbounder.org/Durasteel_Bar) x*4*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/produce/ct_yaara_root.png" alt="Yaara Root icon" loading="lazy" width="auto" height="16px"/> [Yaara Root](https://ceterai.github.io/MyEnternia/Wiki/YaaraRoot) x*4*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/energy_cell.png" alt="Energy Cell icon" loading="lazy" width="auto" height="16px"/> [Energy Cell](https://ceterai.github.io/MyEnternia/Wiki/EnergyCell) x*2*

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"/> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_alta_impulse_rifle`
- Power: `2.5`
- Rarity: `Uncommon`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`assaultrifle`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Assaultrifle), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`impulse`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Impulse), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`uncommon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Uncommon), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle.activeitem)
