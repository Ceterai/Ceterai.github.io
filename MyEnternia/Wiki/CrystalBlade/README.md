# Crystal Blade ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/light/ct_calin_sword_2.png" alt="Crystal Blade ★ icon" loading="lazy" width="auto" height="16px"/> **Crystal Blade ★** is a legendary one-handed shortsword.

A [calin](https://ceterai.github.io/MyEnternia/Wiki/Tags/Calin) sword made out of refined crystals and <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"/> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust). Seems like it's quickly gathering the energy around it...  
The now one-sided blade is structured to put all the force on the impacting side, including alternative indent patterns.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/light/ct_calin_sword.png" alt="Calin Sword icon" loading="lazy" width="auto" height="16px"/> [Calin Sword](https://ceterai.github.io/MyEnternia/Wiki/CalinSword).

## Ingame

Species descriptions:

- Alta: A simple yet sturdy alta creation. I like how it shines with the enrgy bursts from the inside. Maybe this is the so-called **cal-core** mastered to perfection?

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Crystal Might

A sequence of 4 (+1) light strikes. Hold to perform a [Trail Dash](https://ceterai.github.io/MyEnternia/Wiki/TrailDash). Hold in air to [Downstab](https://ceterai.github.io/MyEnternia/Wiki/Downstab).  
Enters a charged state every 5 (-5) seconds, making next 5 (+1) hits deal bonus [electric](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric) damage.  
The new energy flow is able to concentrate faster, building up at the impact rim.

Parameters:

- Damage Config:
  - Damage Source Kind: `shortsword`
  - Timeout: 0.5
- Fire Time: 0.625
- Base Dps: 6
- Steps: 
- Damage Factor: 1.0
- Energy Factor:
- Knockback: 10.0
- Swoosh: `swoosh_small1`
- Swoosh Offset:  -1.0,  -0.25,  2.5,  2.0
- Swoosh Sound: `primary_press`, 
- Damage Factor: 0.6
- Energy Factor:
- Knockback: 20.0
- Swoosh: `swoosh_small2`
- Swoosh Offset: ,  -0.5,  2.5,  1.0
- Swoosh Sound: `primary_press2`, 
- Damage Factor: 1.4
- Energy Factor:
- Knockback: 10.0
- Swoosh: `swoosh_small2`
- Swoosh Offset: ,  -0.25,  2.5,  1.0
- Swoosh Sound: `primary_press`, 
- Damage Factor: 1.3
- Energy Factor:
- Knockback: 25.0
- Swoosh: `swoosh_small1`
- Swoosh Offset:  -0.5,  -0.75,  2.0,  1.5
- Swoosh Sound: `primary_press`
- Class: `TrailDash`

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_calin_sword-upgrade`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`calin`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Calin), [`crystal`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Crystal), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`physical`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Physical), [`shortsword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Shortsword), [`sword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Sword), [`uncommon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Uncommon), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/light/ct_calin_sword.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/light/ct_calin_sword.activeitem)
