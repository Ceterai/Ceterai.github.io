# Bishyn Cannon ★

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/cannon/ct_bishyn_gun_2.png" alt="Bishyn Cannon ★ icon" loading="lazy" width="auto" height="16px"> **Bishyn Cannon ★** is a legendary two-handed shotgun.

This massive blaster now shoots <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/biome/alterash_prime/bishyn/ct_poison_crystal1/icon.png" alt="icon" loading="lazy" width="auto" height="16px"> [bishyn](https://ceterai.github.io/MyEnternia/Wiki/BishynHalls) crystals encrusted with <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_stardust.png" alt="Stardust icon" loading="lazy" width="auto" height="16px"> [stardust](https://ceterai.github.io/MyEnternia/Wiki/Stardust).

An upgrade for <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/cannon/ct_bishyn_gun.png" alt="Bishyn Gun icon" loading="lazy" width="auto" height="16px"> [Bishyn Gun](https://ceterai.github.io/MyEnternia/Wiki/BishynGun).

## Ingame

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Bishyn Barrage

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/biome/alterash_prime/bishyn/ct_poison_crystal1/icon.png" alt="icon" loading="lazy" width="auto" height="16px"> [Bishyn](https://ceterai.github.io/MyEnternia/Wiki/BishynHalls) crystals are poisonous - they deal physical damage while applying special effects. Press to burst with shards, hold for a shard discharge.

Parameters:

- Base Dps: 8
- Energy Usage: 32
- Fire Time: 0.9
- Hold Params:
  - Count: 12
  - Inaccuracy: 1.81
  - Type: `ct_bishyn_shard`
- Hold Type: `clouds`
- Press Params:
  - Inaccuracy: 0.18
  - Params:
    - Knockback: 20
    - Time To Live: 5.0
  - Type: `ct_bishyn_shard`
- Press Type: `burst`

### Bishyn Discharge

A powerful poisonous discharge - press for a shotgun-like burst of poison, hold to launch a proximity mine.

Parameters:

- Base Dps: 8
- Energy Usage: 36
- Fire Time: 0.9
- Hold Params:
  - Inaccuracy: 0.01
  - Type: `poisonproximitymine`
- Hold Type: `blast`
- Press Params:
  - Count: 3
  - Inaccuracy: 0.11
  - Params:
    - Knockback: 20
    - Time To Live: 5.0
  - Type: `acidsweep`
- Press Type: `burst`

## Sources

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_bishyn_gun-upgrade`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`bishyn`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Bishyn), [`cannon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Cannon), [`crystal`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Crystal), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`minelauncher`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Minelauncher), [`physical`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Physical), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`rare`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rare), [`shotgun`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Shotgun), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/cannon/ct_bishyn_gun.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/cannon/ct_bishyn_gun.activeitem)
