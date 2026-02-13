# Mind Field

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_mind.png" alt="Mind Field icon" loading="lazy" width="auto" height="16px"> **Mind Field** is a neutral [effect](https://ceterai.github.io/MyEnternia/Wiki/Effects).

Repeatedly damages enemies around you with Ions, slowing them down. Damage is dependant on your max energy.

Applied by following items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/armors/alta/tier6/ceterai/mindframe/icon.png" alt="C.T. Mindframe ★ icon" loading="lazy" width="auto" height="16px"> [C.T. Mindframe ★](https://ceterai.github.io/MyEnternia/Wiki/C.T.Mindframe)
- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/armors/alta/tier4/elin/helmet/icon.png" alt="Elin Guard Helmet ★ icon" loading="lazy" width="auto" height="16px"> [Elin Guard Helmet ★](https://ceterai.github.io/MyEnternia/Wiki/ElinGuardHelmet)

## Parameters

Blocking Stat: `emiJam`  
Default Duration:  
Effect parameters:

- Animation:
  - Particles:  `sparks`
- Bolt Interval: 0.5
- Damage Clamp: `True`
- Damage Clamp Range:  1,  15
- Damage From Max Energy: `True`
- Damage From Max Energy Percent: 0.05
- Jump Distance: 8
- Projectile: `ct_ionic_small`
- Status Effects:  `frostslow`

## Technical Information

- In-game ID: `ct_mind`
- File: [`/stats/effects/ct_mind.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_mind.statuseffect)
