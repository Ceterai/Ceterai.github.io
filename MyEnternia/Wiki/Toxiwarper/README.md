# Toxiwarper ★

<img src="https://raw.githubusercontent.com/wiki/Ceterai/Enternia/images/icons/ct_tool_mimic-warper-upgrade.png" alt="Toxiwarper ★ icon" loading="lazy" width="auto" height="16px"> **Toxiwarper ★** is a legendary two-handed poisonous unique weapon.

A full on creature that you can wear on your hand. Be careful - its tentacles are pretty venomous...

An upgrade for <img src="https://raw.githubusercontent.com/wiki/Ceterai/Enternia/images/icons/ct_tool_mimic-warper.png" alt="Venomous Warper icon" loading="lazy" width="auto" height="16px"> [Venomous Warper](https://ceterai.github.io/MyEnternia/Wiki/VenomousWarper).

## Ingame

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.
- Beware of the warped items you just acquired. Warped is a form of wild growth found mainly on alterash planets, that tends to spread uncontrollably and contaminate everything in its path.  
Warped things can be bioluminescent, but they also tend to be quite venomous too. I wouldn't recommend testing your luck.

## Parameters

### Primary Ability

Main ability of the item, activated with left mouse button.

Parameters:

- Projectile Parameters:
  - Knockback: 5
  - Speed: 40
  - Time To Live: 10
- Chain:
  - Taper: 0.5
  - Segment Image: `/items/active/weapons/other/tentaclegun/wormsegment.png`
  - End Segment Image: `/items/active/weapons/other/tentaclegun/wormend.png`
  - Segment Size: 1.0
- Energy Usage: 40
- Inaccuracy: 0.01
- Guide Projectiles: `True`
- Max Projectiles: 10
- Base Dps: 6.0
- Max Length: 20
- Fire Time: 0.2
- Projectile Type: `invisibletentaclefist`

### Secondary Ability

Alternative ability of the item, activated with right mouse button.

Parameters:

- Chain:
  - Taper: 0.5
  - Segment Image: `/items/active/weapons/other/tentaclegun/wormsegment.png`
  - End Segment Image: `/items/active/weapons/other/tentaclegun/wormend.png`
  - Segment Size: 1.0
- Guide Projectiles:
- Base Dps: 8.0
- Fire Time: 2.0
- Max Projectiles: 20
- Energy Usage: 28
- Inaccuracy: 3.14
- Fire Sound: `altFire`
- Projectile Count: 20
- Projectile Type: `invisibletentaclefistnosound`
- Projectile Tracks User: `True`
- Projectile Parameters:
  - Knockback: 40
  - Knockback Directional: `True`
  - Speed: 20
  - Ignore Terrain:
  - Bounces: 4
  - Time To Live: 10
  - Min Velocity: 10

## Sources

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_tool_mimic-warper-upgrade`
- Level: `6`
- Power: `3.85`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`poison`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Poison), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`warped`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Warped), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/buildscripts/ct_mimics/tool.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/ct_mimics/tool.activeitem)
