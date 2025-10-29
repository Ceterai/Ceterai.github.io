# Tsyntex Prime ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/blaster/ct_tsyntex_2.png" alt="Tsyntex Prime ★ icon" loading="lazy" width="auto" height="16px"/> **Tsyntex Prime ★** is a legendary one-handed poisonous pistol.

A pristine model of original tsyntex blaster with its power enhanced by <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"/> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust).  
It feels a little heavier than usual, but part of that can be attributed to a different material used for casing and some of the blaster's insides.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/blaster/ct_tsyntex.png" alt="Tsyntex icon" loading="lazy" width="auto" height="16px"/> [Tsyntex](https://ceterai.github.io/MyEnternia/Wiki/Tsyntex).

## Ingame

Species descriptions:

- Alta: Let me liquify some annoying drois with this. Or is it liquidate? Liquinade? Yeah, that's it.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Ultimate Gheablast

Semiauto [impulse](https://ceterai.github.io/MyEnternia/Wiki/Tags/Impulse) bursts on press (+1 blast per burst), or 2x [gheatsyn charges](https://ceterai.github.io/MyEnternia/Wiki/gheatsyncharges) on hold (40% faster charge). The hold damage increases by 0.2% for every <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/throwables/ct_gheatsyn_shard.png" alt="Gheatsyn Shard icon" loading="lazy" width="auto" height="16px"/> [gheatsyn shard](https://ceterai.github.io/MyEnternia/Wiki/GheatsynShard) in inventory (max 300 or 60%).  
Now packing a special accelerator module ran on stardust, it speeds up tsyntex significantly, improving overall performace of this tool.

Parameters:

- Fire Time: 0.1
- Hold Type: `semi`
- Hold Params:
  - Count: 2
  - Inaccuracy: 0.01
  - Item Bonus:
    - Type: <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/throwables/ct_gheatsyn_shard.png" alt="Gheatsyn Shard icon" loading="lazy" width="auto" height="16px"/> [Gheatsyn Shard](https://ceterai.github.io/MyEnternia/Wiki/GheatsynShard)
    - Damage Factor: 0.002
    - Max: 300
  - Type: `ct_gheatsyn_charge`
- Press Params:
  - Count: 4
  - Inaccuracy: 0.04
  - Type: `ct_impulse_small`
- Hold Time Max: 0.45
- Base Dps: 4
- Energy Usage: 16
- Press Type: `semi`

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_tsyntex-upgrade`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`blaster`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Blaster), [`ghearun`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ghearun), [`gheatsyn`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Gheatsyn), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`pistol`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Pistol), [`poison`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Poison), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`rare`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rare), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/blaster/ct_tsyntex.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/blaster/ct_tsyntex.activeitem)
