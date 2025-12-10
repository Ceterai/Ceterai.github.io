# Lira ★★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/spear/ct_lira.png" alt="Lira ★★ icon" loading="lazy" width="auto" height="16px"> **Lira ★★** is a legendary two-handed spear.

**WIP**. Each attack of this spear replenishes your energy.  
This instrument was made as part of a skylight orchestra, an interplanetary music concert performed by arknights. But as with many things, the wielder determines its purpose.

## Ingame

Species descriptions:

- Alta: The secret to playing a stardust lira is obviously having some stardust on you.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Octavia's Wrath

**WIP**. Each hit is more powerful with <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) in your inventory (+0.5%/speck, 120 (+60%) max).  
You can hear harmonical humming coming from this instrument.

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

### Melody Of The Stars

Hold to perform a magical composition using the stardust energy.  
Perhaps this isn't a very intended feature, but a very useful one instead.

Parameters:

- Base Dps: 11
- Fire Time: 0.2
- Energy Usage: 40
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

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_lira`
- Level: `6`
- Power: `4.19`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`instrument`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Instrument), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`musical`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Musical), [`physical`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Physical), [`spear`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Spear), [`stardust`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Stardust), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/spear/ct_lira.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/spear/ct_lira.activeitem)
