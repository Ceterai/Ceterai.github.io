# Phase Cannon ★★★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/heavy/ct_phase_cannon.png" alt="Phase Cannon ★★★ icon" loading="lazy" width="auto" height="16px"> **Phase Cannon ★★★** is a legendary two-handed electric unique weapon.

The eternal heat produced by this mysterious artifact can cause small phase states with charged <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) energy.  
The counterpart to that is the size and overall mass of this tool - it might be a bit too hard to hold it up without an exoskeleton...

## Ingame

Species descriptions:

- Alta: Okay, NOW we're talking.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Phasebeam

A powerful beam of <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) energy, able to polarize everything in its path.  
A powerful generator is able to produce a continous stream while using a relatively small amount of energy.

Parameters:

- Base Dps: 12
- Fire Time: 0.2
- Energy Usage: 44
- Damage Config:
  - Damage Source Kind: `plasma`
  - Knockback: 2
- Beam Length: 50
- Chain:
  - Start Offset: 
  - Segment Image: `/items/active/weapons/ranged/unrand/neolaserlauncher/beam.png`
  - End Segment Image: `/items/active/weapons/ranged/unrand/neolaserlauncher/beam.png`
  - Segment Size: 1.0
  - Overdraw Length:
  - Taper:
  - Jitter: 0.125
  - Waveform:
    - Frequency: 1.0
    - Amplitude: 0.25
    - Movement:
  - Fullbright: `True`
  - Light:  249,  21,  207

### Phase Charge

Charges up a sphere and launches it forward at a low speed.  
This sphere is a point of concentrated energy, able to exist for a prolonged periods of time.

Parameters:

- Base Dps: 12
- Fire Time: 0.9
- Energy Usage: 48
- Press Type: `blast`
- Press Params:
  - Type: `chargeshotsmall`
  - Inaccuracy:
  - Params:
    - Speed: 20
    - Knockback:
    - Time To Live: 5.0
- Hold Type: `clouds`
- Hold Params:
  - Type: `chargeshotlarge`
  - Inaccuracy:
  - Count: 1
  - Params:
    - Speed: 10
    - Knockback:
    - Time To Live: 5.0

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_phase_cannon`
- Level: `6`
- Power: `4.54`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`stardust`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Stardust), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/heavy/ct_phase_cannon.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/heavy/ct_phase_cannon.activeitem)
