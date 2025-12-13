# Bi-Blade ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_enchanted_twins_2.png" alt="Bi-Blade ★ icon" loading="lazy" width="auto" height="16px"> **Bi-Blade ★** is a legendary two-handed electric broadsword.

A weapon that combines different energies into one, long, powerful paired blade.  
You can feel slight pressure if you put your hand between the blades. If you move it slowly, you will feel how gravity is wavering from side to side, sliding from end to end, as if some kind of uneven surface.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_enchanted_twins.png" alt="Vionos Twins icon" loading="lazy" width="auto" height="16px"> [Vionos Twins](https://ceterai.github.io/MyEnternia/Wiki/VionosTwins).

## Ingame

Species descriptions:

- Alta: This seems a bit hazardous. I should probably consult with a coordinator first, just in case. Viona anomalies can be pretty dangerous.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Dual Resonation

A sequence of 4 (+1) heavy strikes. Hold to perform a [blade charge](https://ceterai.github.io/MyEnternia/Wiki/Weapons#Blade-Charge). Hold in air to [downstab](https://ceterai.github.io/MyEnternia/Wiki/Weapons#Downstab)  
Full resonation engaged! A perfect viona anomaly to rule them all.

Parameters:

- Base Dps: 12
- Steps: 
- Damage Factor: 1.0
- Energy Factor:
- Knockback: 20.0
- Swoosh: `swoosh1`
- Swoosh Offset:  0.75, ,  4.25,  5.0
- Element: `physical`, 
- Damage Factor: 0.6
- Energy Factor:
- Knockback: 15.0
- Swoosh: `swoosh2`
- Swoosh Offset:  3.0,  -0.5,  6.5,  2.0
- Element: `physical`, 
- Damage Factor: 1.2
- Energy Factor:
- Knockback: 25.0
- Swoosh: `swoosh3`
- Swoosh Offset:  1.5,  -1.0,  5.5,  1.0
- Damage Source Kind: `icebroadsword`
- Status Effects:  `frostslow`, 
- Damage Factor: 1.6
- Energy Factor:
- Knockback: 35.0
- Swoosh: `swoosh1`
- Swoosh Offset:  3.0,  -0.5,  6.5,  2.0
- Damage Source Kind: `icebroadsword`
- Status Effects:  `frostslow`
- Swoosh Sound: `primary_hold`
- Ranged:
  - Type: `smallicecloud`
  - Count: 3
  - Params:
    - Speed: 5
  - Inaccuracy: 1.57
  - Offset:  5.0,  -0.85
  - Sound: <img src="https://starbounder.org/mediawiki/images/7/77/Ice.png" alt="Ice icon" loading="lazy" width="10px" height="10px"> [Ice](https://starbounder.org/Ice)
- Damage Config:
  - Base Damage: 22.5
  - Knockback: 40
  - Damage Source Kind: `broadsword`
  - Knockback Mode: `facing`
  - Timeout: 0.5
- Energy Usage: 32
- Hold Params:
  - Charge Border: `FF33FF88`
  - Damage Config:
    - Status Effects:  `frostslow`
    - Ranged:
      - Count: 5
      - Params:
        - Speed: 15
      - Inaccuracy: 1.57
      - Type: `smallicecloud`
      - Sound: <img src="https://starbounder.org/mediawiki/images/7/77/Ice.png" alt="Ice icon" loading="lazy" width="10px" height="10px"> [Ice](https://starbounder.org/Ice)
      - Offset:  5.0,  -0.85
    - Damage Source Kind: `icebroadsword`
- Fire Time: 0.93

### Enchanted Resonation

Raises an electric pillar in front of you.  
With increased power comes increased gravity of the situation you're in, and increased risk of sudden mini-anomalies, or **miazmas**.

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_enchanted_twins-upgrade`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`broadsword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Broadsword), [`electric`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Electric), [`enchanted`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Enchanted), [`ice`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ice), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`sword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Sword), [`twinblade`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Twinblade), [`uncommon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Uncommon), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`viona`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Viona), [`vionos`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Vionos), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/heavy/ct_enchanted_twins.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/heavy/ct_enchanted_twins.activeitem)
