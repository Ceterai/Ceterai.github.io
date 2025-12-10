# Winged Halberd ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/spear/ct_winged_halberd.png" alt="Winged Halberd ★ icon" loading="lazy" width="auto" height="16px"> **Winged Halberd ★** is a legendary two-handed spear.

**WIP**. An instrument used by legendary eva [altas](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta).  
Its "wing" is an aerodynamic blade made of stardust and a hardened [dianid](https://ceterai.github.io/MyEnternia/Wiki/dianid) compound.

## Ingame

Species descriptions:

- Alta: It's so easy to hold and swing with! Better not hurt anyone on accident.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Ark Flight

**WIP**. A sequence of 4 (+1) light strikes. Hold to perform a Super Heavy Slash. Each hit is more powerful with <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) in your inventory (+0.5%/speck, 120 (+60%) max).  
Enters a charged state every 5 (-5) seconds, making next 5 (+1) hits deal bonus electric damage.  
This smooth flow of circular swings helps you stay in balance regardless of you position. The halberd also has an in-built impulse compensator to account for the electric busrts.

Parameters:

- Fire Time: 0.6
- Base Dps: 12
- Damage Config:
  - Damage Source Kind: `<elementalType>spear`
  - Knockback Mode: `aim`
  - Knockback: 10
  - Timeout Group: `primary`
- Hold Damage Multiplier: 0.1
- Hold Damage Config:
  - Timeout Group: `hold`
  - Timeout: 0.5

### Aeroflux

Performs a spear flurry.  
A quick elemental superhit performed with an electric halberd.

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_winged_halberd`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`eva`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Eva), [`halberd`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Halberd), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`physical`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Physical), [`spear`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Spear), [`stardust`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Stardust), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/spear/ct_winged_halberd.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/spear/ct_winged_halberd.activeitem)
