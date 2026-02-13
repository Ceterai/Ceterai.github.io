# Venomous Warper

<img src="https://raw.githubusercontent.com/wiki/Ceterai/Enternia/images/icons/ct_tool_mimic-warper.png" alt="Venomous Warper icon" loading="lazy" width="auto" height="16px"> **Venomous Warper** is a legendary two-handed poisonous unique weapon.

A full on creature that you can wear on your hand. Be careful - its tentacles are pretty venomous...

Can be upgraded to <img src="https://raw.githubusercontent.com/wiki/Ceterai/Enternia/images/icons/ct_tool_mimic-warper-upgrade.png" alt="Toxiwarper ★ icon" loading="lazy" width="auto" height="16px"> [Toxiwarper ★](https://ceterai.github.io/MyEnternia/Wiki/Toxiwarper) at the Weapon Upgrade Anvil.

## Ingame

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.
- Beware of the warped items you just acquired. Warped is a form of wild growth found mainly on alterash planets, that tends to spread uncontrollably and contaminate everything in its path.  
Warped things can be bioluminescent, but they also tend to be quite venomous too. I wouldn't recommend testing your luck.

## Parameters

### Venomous Kiss

Exposes its tentacles one by one, each touch equally dangerous.

Parameters:

- Base Dps: 6.0
- Chain:
  - End Segment Image: `/items/active/weapons/other/tentaclegun/wormend.png`
  - Segment Image: `/items/active/weapons/other/tentaclegun/wormsegment.png`
  - Segment Size: 1.0
  - Taper: 0.5
- Energy Usage: 40
- Fire Time: 0.2
- Guide Projectiles: `True`
- Inaccuracy: 0.01
- Max Length: 20
- Max Projectiles: 10
- Projectile Parameters:
  - Knockback: 5
  - Speed: 40
  - Time To Live: 10
- Projectile Type: `invisibletentaclefist`

### Tentacle Burst

Alternative ability of the item, activated with right mouse button.

Parameters:

- Base Dps: 8.0
- Chain:
  - End Segment Image: `/items/active/weapons/other/tentaclegun/wormend.png`
  - Segment Image: `/items/active/weapons/other/tentaclegun/wormsegment.png`
  - Segment Size: 1.0
  - Taper: 0.5
- Energy Usage: 28
- Fire Sound: `altFire`
- Fire Time: 2.0
- Guide Projectiles:
- Inaccuracy: 3.14
- Max Projectiles: 20
- Projectile Count: 20
- Projectile Parameters:
  - Bounces: 4
  - Ignore Terrain:
  - Knockback: 40
  - Knockback Directional: `True`
  - Min Velocity: 10
  - Speed: 20
  - Time To Live: 10
- Projectile Tracks User: `True`
- Projectile Type: `invisibletentaclefistnosound`

## Sources

Can be obtained via <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have it installed).

## Technical Information

- In-game ID: `ct_tool_mimic-warper`
- Level: `5`
- Power: `3.0`
- Rarity: `Legendary`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`legendary`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Legendary), [`poison`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Poison), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`warped`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Warped), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/buildscripts/ct_mimics/tool.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/ct_mimics/tool.activeitem)
