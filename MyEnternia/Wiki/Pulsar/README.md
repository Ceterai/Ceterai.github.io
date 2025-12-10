# Pulsar

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/cannon/ct_pulsar.png" alt="Pulsar icon" loading="lazy" width="auto" height="16px"/> **Pulsar** is a legendary two-handed electric shotgun.

An [impulse](https://ceterai.github.io/MyEnternia/Wiki/Tags/Impulse) cannon made for heavy defensive combat. Covers the area in pulse blasts or charges up an Impulse Bomb.

## Ingame

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Pulsar Charge

Creates semiauto bursts of [Impulse Charges](https://ceterai.github.io/MyEnternia/Wiki/ImpulseCharges) using <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/damage/ct_impulse.png" alt="icon" width="16" height="16"/> [ceternia](https://ceterai.github.io/MyEnternia/Wiki/Ceternia) energy.

Parameters:

- Base Dps: 8
- Energy Usage: 32
- Fire Time: 0.65
- Press Type: `semi`
- Press Params:
  - Type: `ct_impulse_medium`
  - Inaccuracy: 0.04
  - Params:
    - Knockback: 20
    - Time To Live: 5.0
- Hold Time Min: 0.9
- Hold Time Max:

### Twin Pulse

Generates syncronized Twin Impulses with different power.
Press - launch a Twin Impulse;
Hold - shotgun burst of Twin Impulses.

Parameters:

- Base Dps: 10
- Energy Usage: 40
- Fire Time: 0.9
- Press Type: `rocket`
- Press Params:
  - Type: `ct_impulse_large`
- Hold Type: `burst`
- Hold Params:
  - Type: `ct_impulse_large`
  - Inaccuracy: 0.21
  - Count: 3

## Sources

Can be crafted:

- Tier 4 ![ ](https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/alta/crafting/crafting_station/icon4.png) [Alta Crafting Station](https://ceterai.github.io/MyEnternia/Wiki/AltaCraftingStation) (takes 5.5s, outputs <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/cannon/ct_pulsar.png" alt="Pulsar icon" loading="lazy" width="auto" height="16px"/> Pulsar x*1*):
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/phosicore.png" alt="Phosicore icon" loading="lazy" width="auto" height="16px"/> [Phosicore](https://ceterai.github.io/MyEnternia/Wiki/Phosicore) x*6*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/cetersphere.png" alt="Ceter-Sphere icon" loading="lazy" width="auto" height="16px"/> [Ceter-Sphere](https://ceterai.github.io/MyEnternia/Wiki/Ceter-Sphere) x*1*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/bion.png" alt="Bion Compound icon" loading="lazy" width="auto" height="16px"/> [Bion Compound](https://ceterai.github.io/MyEnternia/Wiki/BionCompound) x*2*
  - <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/eds.png" alt="EDS Armor icon" loading="lazy" width="auto" height="16px"/> [EDS Armor](https://ceterai.github.io/MyEnternia/Wiki/EDSArmor) x*2*

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"/> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_pulsar`
- Level: `6`
- Power: `3.5`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`cannon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Cannon), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`elite`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Elite), [`impulse`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Impulse), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`shotgun`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Shotgun), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/cannon/ct_pulsar.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/cannon/ct_pulsar.activeitem)
