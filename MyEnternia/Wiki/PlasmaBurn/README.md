# Plasma Burn

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_plasma_burn.png" alt="Plasma Burn icon" loading="lazy" width="auto" height="16px"> **Plasma Burn** is a neutral [effect](https://ceterai.github.io/MyEnternia/Wiki/Effects).

Repeatedly damages you with pure [plasma](https://ceterai.github.io/MyEnternia/Wiki/Tags/Plasma). Having <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_plasma_block.png" alt="icon" width="16" height="16"/> [plasma immunity](https://ceterai.github.io/MyEnternia/Wiki/Alternia#immunity) blocks the effect, <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Immunity icon" loading="lazy" width="16px" height="16px"> [Electric Immunity](https://starbounder.org/Electric_Resistance) minimizes the damage, [Fire Status Immunity](https://ceterai.github.io/MyEnternia/Wiki/FireStatusImmunity) decreases the damage, <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_hevikai.png" alt="Hevikai icon" loading="lazy" width="auto" height="16px"> [Hevikai](https://ceterai.github.io/MyEnternia/Wiki/Hevikai) increases the damage.

## Parameters

Blocking Stat: `plasmaStatusImmunity`  
Default Duration: 4s  
Effect parameters:

- Interval: 1.0
- Health Percentage: 0.03
- Damage Kind: <img src="/damage/ct_plasma.png" alt="Plasma icon" loading="lazy" width="16px" height="16px"> [Plasma](Alternia#damage)
- Animation:
  - Color: `fade=0050c0=0.25`
  - Particles:  `sparks_dense`
  - Lights:  `mid`
- Semi Immunity: <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Status Immunity icon" loading="lazy" width="16px" height="16px"> [Electric Status Immunity](https://starbounder.org/Electric_Resistance)
- Mini Immunity: `fireStatusImmunity`
- Vulnerability: `hevikai`

## Technical Information

- In-game ID: `ct_plasma_burn`
- File: [`/stats/effects/ct_plasma_burn.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_plasma_burn.statuseffect)
