# EDS Cannonsword ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_eds_claymore_2.png" alt="EDS Cannonsword ★ icon" loading="lazy" width="auto" height="16px"> **EDS Cannonsword ★** is a legendary two-handed broadsword.

This weapon is now a powerful device that can hold any threat back, no matter how far away it is.  
The enhanced CDR is now able to launch powerful [EDS rockets](https://ceterai.github.io/MyEnternia/Wiki/EDSrockets) at the targets. Packed with the _Litera-7_ homing system, it's able to find it target after a charge.

_Centar Thruster_ is what causing the weapon to propell forward, with the use of mentioned rockets as push charges.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_eds_claymore.png" alt="EDS Claymore icon" loading="lazy" width="auto" height="16px"> [EDS Claymore](https://ceterai.github.io/MyEnternia/Wiki/EDSClaymore).

## Ingame

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.
- The item you've just picked up seems to have visual EDS markings on it. EDS is an alta formation focused on protecting altas from all possible threats, and thus all related items and objects often reflect that goal in their characteristics.  
Unfortunately, it seems like EDS's automated defence system went out of control recently, so I'd suggest avoiding contact with still active facilities.

## Parameters

### Bastion Stand

A sequence of 4 _(+1)_ heavy strikes. Hold to perform a [rising slash](https://ceterai.github.io/MyEnternia/Wiki/Weapons#Rising-Slash). Hold in air to [downstab](https://ceterai.github.io/MyEnternia/Wiki/Weapons#Downstab).

Parameters:

- Steps: 
- Damage Factor: 1.0
- Energy Factor:
- Knockback: 20.0
- Swoosh: `swoosh1`
- Swoosh Offset:  0.75, ,  4.25,  5.0, 
- Damage Factor: 0.6
- Energy Factor:
- Knockback: 15.0
- Swoosh: `swoosh2`
- Swoosh Offset:  3.0,  -0.5,  6.5,  2.0, 
- Damage Factor: 1.2
- Energy Factor:
- Knockback: 25.0
- Swoosh: `swoosh3`
- Swoosh Offset:  1.5,  -1.0,  5.5,  1.0, 
- Damage Factor: 1.6
- Energy Factor:
- Knockback: 35.0
- Swoosh: `swoosh1`
- Swoosh Offset:  3.0,  -0.5,  6.5,  2.0
- Swoosh Sound: `primary_hold`
- Energy Usage: 32
- Fire Time: 1.1
- Hold Params:
  - Cooldown Time: 0.2
  - Energy Factor: 1.0
- Base Dps: 12

### Elerune CDR Barrage

Launches stabilizing Ion Rockets that deal electric damage. _Press for 1 or hold for 3._

Parameters:

- Hold Type: `blast`
- Press Type: `blast`
- Energy Usage: 36
- Press Params:
  - Type: `ct_ionic_large`
  - Inaccuracy:
  - Params:
    - Time To Live: 5.0
  - Offset:  -0.45,  5.0
- Fire Time: 1.2
- Hold Params:
  - Interval: 0.1
  - Count: 3
  - Params:
    - Time To Live: 5.0
    - Knockback: 15
  - Type: `ct_ionic_large`
  - Offset:  -0.75,  5.0
- Base Dps: 9

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_eds_claymore-upgrade`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`broadsword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Broadsword), [`eds`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Eds), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`physical`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Physical), [`rare`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rare), [`sword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Sword), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/heavy/ct_eds_claymore.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/heavy/ct_eds_claymore.activeitem)
