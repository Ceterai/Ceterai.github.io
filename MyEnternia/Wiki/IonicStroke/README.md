# Ionic Stroke

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_ionic_stroke.png" alt="Ionic Stroke icon" loading="lazy" width="auto" height="16px"> **Ionic Stroke** is a neutral [effect](https://ceterai.github.io/MyEnternia/Wiki/Effects).

Quickly degrades your energy. Once out of energy, damages you repeatedly with <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/damage/ct_ionic.png" alt="icon" width="16" height="16"/> [enternia](https://ceterai.github.io/MyEnternia/Wiki/Enternia) electricity.

Applied by following weather:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/interface/cockpit/weather/ct_ionic_peak.png" alt="Ionic Peak icon" loading="lazy" width="auto" height="16px"> [Ionic Peak](https://ceterai.github.io/MyEnternia/Wiki/IonicPeak)

## Parameters

Blocking Stat: `ionicStatusImmunity`  
Default Duration: 5s  
Effect parameters:

- Animation:
  - Particles:  `sparks`,  `ember`
- Movement Modifiers:
  - Speed Modifier: 0.6
  - Air Jump Modifier: 0.6
- Cooldown: 2.0
- Energy Cost: 40
- Damage: 80
- Semi Immunity: <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Status Immunity icon" loading="lazy" width="16px" height="16px"> [Electric Status Immunity](https://starbounder.org/Electric_Resistance)
- Poison Resistance: -0.1
- Electric Resistance: -0.2

## Technical Information

- In-game ID: `ct_ionic_stroke`
- File: [`/stats/effects/ct_ionic_stroke.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_ionic_stroke.statuseffect)
