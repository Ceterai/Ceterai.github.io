# Overcharged Air

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_overcharged_air.png" alt="Overcharged Air icon" loading="lazy" width="auto" height="16px"/> **Overcharged Air** is a neutral [effect](https://ceterai.github.io/MyEnternia/Wiki/Effects).

Quickly degrades your energy. Once out of energy, damages you repeatedly with [plasma](https://ceterai.github.io/MyEnternia/Wiki/Tags/Plasma) strikes.  
Having <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Immunity icon" loading="lazy" width="16px" height="16px"/> [Electric Immunity](https://starbounder.org/Electric_Resistance) minimizes negative effects, while <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_plasma_block.png" alt="icon" width="16" height="16"/> [plasma immunity](https://ceterai.github.io/MyEnternia/Wiki/Alternia#immunity) blocks the effect completely.

## Parameters

Blocking Stat: `plasmaStatusImmunity`  
Default Duration: 5s  
Effect parameters:

- Animation:
  - Directives: `fade=5000c0=0.25`
  - Particles:  `sparks`,  `ember`
- Movement Modifiers:
  - Speed Modifier: 0.6
  - Air Jump Modifier: 0.6
- Cooldown: 2.0
- Energy Cost: 40
- Damage: 80
- Semi Immunity: <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Status Immunity icon" loading="lazy" width="16px" height="16px"/> [Electric Status Immunity](https://starbounder.org/Electric_Resistance)
- Radio Message: `ct_overcharged_air_msg`
- Radio Message Immune: `ct_overcharged_air_immune_msg`
- Poison Resistance: -0.1
- Electric Resistance: -0.2

## Technical Information

- In-game ID: `ct_overcharged_air`
- File: [`/stats/effects/ct_overcharged_air.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_overcharged_air.statuseffect)
