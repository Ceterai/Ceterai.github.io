# Barracuda's Cry ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_barracuda_fin_2.png" alt="Barracuda's Cry ★ icon" loading="lazy" width="auto" height="16px"/> **Barracuda's Cry ★** is a legendary two-handed electric broadsword.

A refined, hardened Barracuda's Fin. With the power of <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"/> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) this thing can do absolute wonders.  
The only things left are the most necessary ones - the hard, refined **pillar bone** and barely visible refined **cuda spikes**. With this size they're now able to resonate, attracting and spreading charged kinetic energy.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_barracuda_fin.png" alt="Barracuda's Fin icon" loading="lazy" width="auto" height="16px"/> [Barracuda's Fin](https://ceterai.github.io/MyEnternia/Wiki/Barracuda'sFin).

## Ingame

Species descriptions:

- Alta: I can use this as a sword. Or a surfing board! But I guess I should take care of the smell first...

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Perfect Strike

A sequence of 4 _(+1)_ heavy strikes. Hold to perform an _Fang Discharge_.  
The fin is pretty heavy, so any of this might take some additional effort.

Parameters:

- Damage Config:
  - Base Damage: 22.5
  - Knockback: 40
  - Damage Source Kind: `broadsword`
  - Knockback Mode: `facing`
  - Timeout: 0.5
- Fire Time: 0.7
- Hold Params:
  - Cooldown Time: 0.8
  - Energy Factor: 1.0
- Energy Usage: 32
- Hold Time Max: 0.35
- Press Params:
  - Flash:
    - Time: 0.15
    - Directives: `fade=FFFFFFFF=0.15`
  - Combo Speed Factor: 0.7
  - Edge Trigger Grace: 0.25
- Downstab Params:
  - Cooldown Time: 0.5
  - Energy Factor: 0.2
  - Hold AIr Control: 60
  - Stab Velocity: -5
  - Bounce Y Velocity: 35
  - Damage Config:
    - Damage Factor: 0.5
    - Damage Source Kind: `spear`
    - Knockback: ,  -35
    - Timeout: 0.2
    - Timeout Group: `primary`
- Base Dps: 12
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
- Class: `KunaiBlast`

### Steelspin

Hold to perform an electric Super Spin Slash.  
The inertia makes it much easier to execute then regular attacks.

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_barracuda_fin-upgrade`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`barracuda`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Barracuda), [`broadsword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Broadsword), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`physical`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Physical), [`sea`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Sea), [`sword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Sword), [`uncommon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Uncommon), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/heavy/ct_barracuda_fin.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/heavy/ct_barracuda_fin.activeitem)
