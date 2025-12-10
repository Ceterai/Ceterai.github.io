# Impulse Rifle NG4X ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle_2.png" alt="Impulse Rifle NG4X ★ icon" loading="lazy" width="auto" height="16px"> **Impulse Rifle NG4X ★** is a legendary two-handed electric assault rifle.

An NG4 with added laser pointer and scope, as well as increased firerate and precision due to the use of <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) energy.  
This long-range high-precision energy instrument can generate long-lasting impulses, able to travel without losing height.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle.png" alt="Impulse Rifle NG4 icon" loading="lazy" width="auto" height="16px"> [Impulse Rifle NG4](https://ceterai.github.io/MyEnternia/Wiki/ImpulseRifleNG4).

## Ingame

Species descriptions:

- Alta: I don't think I've ever seen this model before. I assume it's custom made.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Impulse Blast

A standard [impulse](https://ceterai.github.io/MyEnternia/Wiki/Tags/Impulse) blast with high precision.
Firemodes: charge, semiauto.

Parameters:

- Fire Time: 0.7
- Base Dps: 6
- Default Fire Type: `charge`
- Fire Types:
  - Semi:
    - Hold Time Max:
    - Press Params:
      - Type: `ct_impulse_medium`
      - Interval: 0.1
      - Count: 2
      - Inaccuracy: 0.001
    - Press Type: `semi`
  - Charge:
    - Hold Start: `charge`
    - Hold Type: `blast`
    - Hold Params:
      - Type: `ct_impulse_large`
      - Sound: `primary_hold`
      - Inaccuracy: 0.001
    - Press Params:
      - Type: `ct_impulse_medium`
      - Sound: `primary_press`
      - Inaccuracy: 0.001
    - Hold Loop: `charging`
    - Press Type: `blast`
- Energy Usage: 32

### Security Switch

All a security unit needs with a rifle.
Press - change attachments: none, flashlight;
Hold - change firemodes.

Parameters:

- Attachments:  `none`,  `laser`,  `flashlight`
- Fire Types:  `charge`,  `semi`

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_alta_impulse_rifle-upgrade`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`assaultrifle`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Assaultrifle), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`impulse`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Impulse), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`uncommon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Uncommon), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/rifle/ct_alta_impulse_rifle.activeitem)
