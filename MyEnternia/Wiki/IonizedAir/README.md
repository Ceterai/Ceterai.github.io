# Ionized Air

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_ionized_air.png" alt="Ionized Air icon" loading="lazy" width="auto" height="16px"> **Ionized Air** is a neutral [effect](https://ceterai.github.io/MyEnternia/Wiki/Effects).

Slowly degrades your energy. Once out of energy, damages you repeatedly with [ionic](https://ceterai.github.io/MyEnternia/Wiki/Enternia#damage) strikes.  
While in water, damages you regardless and twice as fast.

## Parameters

Blocking Stat: `ionicStatusImmunity`  
Default Duration: 5s  
Effect parameters:

- Animation:
  - Particles:  `ember`
- Cooldown: 2.0
- Damage: 20
- Electric Resistance: -0.1
- Energy Cost: 10
- Full Immunity: <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Status Immunity icon" loading="lazy" width="16px" height="16px"> [Electric Status Immunity](https://starbounder.org/Electric_Resistance)
- Liquid Cooldown: 1.0
- Liquid Damage: 10
- Liquid Damage Kind: <img src="/damage/ct_ionic.png" alt="Ionic icon" loading="lazy" width="16px" height="16px"> [Ionic](Enternia#damage)
- Liquid I D: 1
- Liquid Movement Modifiers:
  - Air Jump Modifier: 1.4
  - Speed Modifier: 1.4
- Movement Modifiers:
  - Air Jump Modifier: 1.4
  - Speed Modifier: 1.4
- Radio Message: `ct_ionized_air_msg`
- Radio Message Immune: `ct_ionized_air_immune_msg`

## Technical Information

- In-game ID: `ct_ionized_air`
- File: [`/stats/effects/ct_ionized_air.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_ionized_air.statuseffect)
