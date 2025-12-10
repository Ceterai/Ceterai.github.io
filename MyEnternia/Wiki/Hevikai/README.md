# Hevikai

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_hevikai.png" alt="Hevikai icon" loading="lazy" width="auto" height="16px"> **Hevikai** is a neutral [effect](https://ceterai.github.io/MyEnternia/Wiki/Effects).

A disease-like immunity issue found in <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/ct_alternia_shard.png" alt="icon" width="16" height="16"/> [hevika](https://ceterai.github.io/MyEnternia/Wiki/Hevika) areas, that can cause various creatures to start slowly produce plasma in their body. To most organisms this process could be lethal.  
To some this might lead to an increase in energy and power in exchange for sanity, however, the end is usually the same as always.  
Read more about the disease: <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/codex/alta/datamass/hevika.png" alt="icon" width="16" height="16"/> [hevikai incident](https://ceterai.github.io/MyEnternia/Wiki/Hevika#hevikai-incident)

Important notes:

- to block this effect, try to not get a <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_hevikai_strike.png" alt="Hevikai Strike icon" loading="lazy" width="auto" height="16px"> [Hevikai Strike](https://ceterai.github.io/MyEnternia/Wiki/HevikaiStrike) twice in a row.
- If you got sick with Hevikai, use the <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/other/ct_hevikai_antidote.png" alt="Hevikai Antidote ★★ icon" loading="lazy" width="auto" height="16px"> [Hevikai Antidote](https://ceterai.github.io/MyEnternia/Wiki/HevikaiAntidote) to cure it in time.
- having <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/stats/effects/ct_plasma_block.png" alt="icon" width="16" height="16"/> [plasma immunity](https://ceterai.github.io/MyEnternia/Wiki/Alternia#immunity) increases the time you have by x2.
- hevikai strips you of <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Immunity icon" loading="lazy" width="16px" height="16px"> [Electric Immunity](https://starbounder.org/Electric_Resistance) (if you have it) and decreases your <img src="https://starbounder.org/mediawiki/images/4/42/Status_Electric_Resistance.png" alt="Electric Resistance icon" loading="lazy" width="16px" height="16px"> [electric resistance](https://starbounder.org/Electric_Resistance) by 20%.

This effect might come in use to be able to survive on [Enterash Prime](https://ceterai.github.io/MyEnternia/Wiki/Tags/EnterashPrime).  
This effect can be artificially induced using a <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/other/ct_hevikai_stim.png" alt="Hevikai Stim Pack icon" loading="lazy" width="auto" height="16px"> [Hevikai Stim Pack](https://ceterai.github.io/MyEnternia/Wiki/HevikaiStimPack).

Applied by following items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/other/ct_hevikai_stim.png" alt="Hevikai Stim Pack icon" loading="lazy" width="auto" height="16px"> [Hevikai Stim Pack](https://ceterai.github.io/MyEnternia/Wiki/HevikaiStimPack)

## Parameters

Blocking Stat: `hevikaiStatusImmunity`  
Default Duration: 600s  
Effect parameters:

- Animation:
  - Particles:  `ember`
- Semi Immunity: `plasmaStatusImmunity`
- Radio Message: `ct_hevikai_msg`
- Electric Resistance: -0.2
- Remove Electric Status Immunity: `True`

## Technical Information

- In-game ID: `ct_hevikai`
- File: [`/stats/effects/ct_hevikai.statuseffect`](https://github.com/Ceterai/Enternia/blob/main/stats/effects/ct_hevikai.statuseffect)
