# Haven Chaos ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/cannon/ct_haven_storm_2.png" alt="Haven Chaos ★ icon" loading="lazy" width="auto" height="16px"> **Haven Chaos ★** is a legendary two-handed poisonous rocket launcher.

A powerful generator of haven toxins, now enhanced with <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust) energy.

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/cannon/ct_haven_storm.png" alt="Haven Storm icon" loading="lazy" width="auto" height="16px"> [Haven Storm](https://ceterai.github.io/MyEnternia/Wiki/HavenStorm).

## Ingame

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.
- The item you just got seems to have come for alterash haven - flowery areas on alterash planets that tend to have higher levels of toxicity than surrounding nature. Although it equals to toxicity levels on most green planets, it's not a usual sight here, so I would recommend being careful.

## Parameters

### Toxin Core

The poisonous generator of this cannon makes it spread toxic plasma on activation.

Parameters:

- Base Dps: 8
- Energy Usage: 32
- Fire Time: 0.1
- Hold Time Max:
- Press Params:
  - Type: `poisonplasma`
  - Inaccuracy: 0.11
  - Params:
    - Knockback: 5
    - Time To Live: 5.0
- Press Type: `blast`

### Ex-Pollinator

This cannon is able to accumulate so much energy it can create toxin clouds.
Press to release toxins around you;
Hold to charge a slow powerful cloud.

Parameters:

- Base Dps: 8
- Energy Usage: 40
- Fire Time: 0.9
- Hold Params:
  - Type: `largepoisoncloud`
  - Inaccuracy:
  - Params:
    - Knockback: 5
    - Time To Live: 8.0
    - Speed: 15.0
- Hold Type: `blast`
- Press Params:
  - Type: `smallpoisoncloud`
- Press Type: `clouds`

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_haven_storm-upgrade`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`cannon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Cannon), [`gasthrower`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Gasthrower), [`haven`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Haven), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`poison`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Poison), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`rare`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rare), [`rocketlauncher`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rocketlauncher), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/cannon/ct_haven_storm.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/cannon/ct_haven_storm.activeitem)
