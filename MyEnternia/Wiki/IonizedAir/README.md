# Ionized Air

Slowly degrades your energy. Once out of energy, damages you repeatedly with [ionic](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ionic) strikes.  
While in water, damages you regardless and twice as fast.

## Parameters

Blocking Stat: `ionicStatusImmunity`  
Default Duration: 5s  
Effect parameters:

- Animation:
  - Particles:  `ember`
- Movement Modifiers:
  - Speed Modifier: 1.4
  - Air Jump Modifier: 1.4
- Cooldown: 2.0
- Energy Cost: 10
- Damage: 20
- Full Immunity: <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Status Immunity icon" loading="lazy" width="16px" height="16px"/> [Electric Status Immunity](https://starbounder.org/Electric_Resistance)
- Radio Message: `ct_ionized_air_msg`
- Radio Message Immune: `ct_ionized_air_immune_msg`
- Liquid I D: 1
- Liquid Movement Modifiers:
  - Speed Modifier: 1.4
  - Air Jump Modifier: 1.4
- Liquid Cooldown: 1.0
- Liquid Damage: 10
- Liquid Damage Kind: <img src="/damage/ct_ionic.png" alt="Ionic icon" loading="lazy" width="16px" height="16px"/> [Ionic](Enternia#damage)
- Electric Resistance: -0.1

## Technical Information

- In-game ID: `ct_ionized_air`
- File: [`/stats/effects/ct_ionized_air.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_ionized_air.statuseffect)
