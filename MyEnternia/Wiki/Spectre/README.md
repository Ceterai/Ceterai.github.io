# Spectre

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_spectre.png" alt="Spectre icon" loading="lazy" width="auto" height="16px"/> **Spectre** is a legendary two-handed poisonous hammer.

A powerful battle axe. Its razor is made out of <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"/> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) energy and can change its polarity on a whim.  
These energy swaps, while spectacular, are quite unstable. Therefore, the Spectre tends to suffer from elemental offsets, where some of its abilities might get the element change with a certain delay.

## Ingame

Species descriptions:

- Alta: A tool that uses spectral projection and stardust to manifest energy in form of spectral elemental analogs. No idea what I've just said.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Spectral Tear

A sequence of 3 heavy strikes. Each strike changes the element. Hold to create a [Traveling Slash](https://ceterai.github.io/MyEnternia/Wiki/TravelingSlash). Hold in air to [Downstab](https://ceterai.github.io/MyEnternia/Wiki/Downstab). Each hit is more powerful with <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"/> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) in your inventory (+0.5%/speck, 120 (+60%) max).  
The element changes are affecting the _Spectral Tear_ immediately, but might take time to spread onto [Spectral Wave](https://ceterai.github.io/MyEnternia/Wiki/SpectralWave) as well.

Parameters:

- Class: `TravelingSlash`
- Base Dps: 12
- Fire Time: 1.2
- Energy Usage: 32
- Damage Config:
  - Item Bonus:
    - Type: <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"/> [Stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust)
    - Damage Factor: 0.005
    - Max: 120
- Switch Element Config: 
- Element: `fire`
- Sprite: `/items/active/weapons/melee/alta/heavy/ct_spectre_2.png`, 
- Element: `electric`
- Sprite: `/items/active/weapons/melee/alta/heavy/ct_spectre_3.png`, 
- Element: `poison`
- Sprite: `/items/active/weapons/melee/alta/heavy/ct_spectre.png`
- Steps: 
- Damage Factor: 1.0
- Energy Factor:
- Knockback: 10.0
- Swoosh: `swoosh1`
- Swoosh Offset:  0.75, ,  4.25,  5.0, 
- Damage Factor: 1.4
- Energy Factor:
- Knockback: 5.0
- Swoosh: `swoosh2`
- Swoosh Offset:  3.0,  -0.5,  6.5,  2.0, 
- Damage Factor: 0.6
- Energy Factor:
- Knockback: 25.0
- Swoosh: `swoosh3`
- Swoosh Offset:  1.5,  -1.0,  5.5,  1.0

### Spectral Wave

Launches an elemental shockwave. The element is affected by the main ability, but needs a reset to go in action.  
This ability creates a vertical spectral projection that imitates a pillar of elemental matter. It requires a significant amount of energy to do so.

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"/> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_spectre`
- Power: `3.5`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`axe`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Axe), [`battleaxe`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Battleaxe), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`poison`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Poison), [`stardust`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Stardust), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/heavy/ct_spectre.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/heavy/ct_spectre.activeitem)
