# Ionic Shock

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_ionic_shock.png" alt="Ionic Shock icon" loading="lazy" width="auto" height="16px"> **Ionic Shock** is a neutral [effect](https://ceterai.github.io/MyEnternia/Wiki/Effects).

Repeatedly damages you with [ionic](https://ceterai.github.io/MyEnternia/Wiki/Enternia#damage) electricity. Having <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_ionicblockade.png" alt="icon" loading="lazy" width="auto" height="16px"> [Ionic Immunity](https://ceterai.github.io/MyEnternia/Wiki/Enternia#immunity) blocks the effect, <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Immunity icon" loading="lazy" width="16px" height="16px"> [Electric Immunity](https://starbounder.org/Electric_Resistance) minimizes the damage, <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_hevikai.png" alt="Hevikai icon" loading="lazy" width="auto" height="16px"> [Hevikai](https://ceterai.github.io/MyEnternia/Wiki/Hevikai) increases the damage.

Applied by following weather:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/interface/cockpit/weather/ct_ionic_rain.png" alt="Ionic Rain icon" loading="lazy" width="auto" height="16px"> [Ionic Rain](https://ceterai.github.io/MyEnternia/Wiki/IonicRain)
- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/interface/cockpit/weather/ct_ionic_storm.png" alt="Ionic Storm icon" loading="lazy" width="auto" height="16px"> [Ionic Storm](https://ceterai.github.io/MyEnternia/Wiki/IonicStorm)

## Parameters

Blocking Stat: `ionicStatusImmunity`  
Default Duration: 2.5s  
Effect parameters:

- Animation:
  - Directives: `fade=5000c0=0.25`
  - Lights:  `dim`
  - Particles:  `sparks_dense`
- Damage Clamp Range:  2,  8
- Damage Kind: <img src="/damage/ct_ionic.png" alt="Ionic icon" loading="lazy" width="16px" height="16px"> [Ionic](Enternia#damage)
- Health Percentage: 0.04
- Interval: 1.4
- Jump Distance: 8
- Semi Immunity: <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Status Immunity icon" loading="lazy" width="16px" height="16px"> [Electric Status Immunity](https://starbounder.org/Electric_Resistance)
- Vulnerability: `hevikai`

## Technical Information

- In-game ID: `ct_ionic_shock`
- File: [`/stats/effects/ct_ionic_shock.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_ionic_shock.statuseffect)
