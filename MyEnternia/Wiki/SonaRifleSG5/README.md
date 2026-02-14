# Sona Rifle SG5

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_sona_rifle.png" alt="Sona Rifle SG5 icon" loading="lazy" width="auto" height="16px"> **Sona Rifle SG5** is a rare two-handed cryogenic assault rifle.

A rifled cryo energy blaster, mostly used by [sona soldiers](https://ceterai.github.io/MyEnternia/Wiki/SonaSoldier) operating in <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/biome/ct_sona_loot.png" alt="Tavriya icon" loading="lazy" width="auto" height="16px"> [tavriya](https://ceterai.github.io/MyEnternia/Wiki/Tavriya).  
Its compact cryogenic core is able to produce energy blasts at different rates, allowing for multiple firemodes.

Can be upgraded to <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/rifle/ct_alta_sona_rifle_2.png" alt="Sona Rifle SG5X ★ icon" loading="lazy" width="auto" height="16px"> [Sona Rifle SG5X ★](https://ceterai.github.io/MyEnternia/Wiki/SonaRifleSG5X) at the Weapon Upgrade Anvil.

## Ingame

Species descriptions:

- Alta: A very useful thing to have one you when its exceptionally hot outside. Like right now.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Cryo Blast

Phosicore of this weapon can produce sona energy.  
Firemodes: burst, auto, charge.  
Letting it hold on the charge mode will produce a cryoplasma rocket and launch it at a decent speed.

Parameters:

- Base Dps: 8
- Default Fire Type: `burst`
- Energy Usage: 32
- Fire Time: 0.15
- Fire Types:
  - Auto:
    - Hold Time Max:
    - Press Params:
      - Type: `iceplasma`
    - Press Type: `blast`
  - Burst:
    - Hold Time Max:
    - Press Params:
      - Count: 3
      - Fire Time: 0.65
      - Sound: `primary_hold`
      - Type: `iceplasma`
    - Press Type: `burst`
  - Charge:
    - Hold Params:
      - Type: `iceplasmarocket`
    - Hold Type: `rocket`
    - Press Params:
      - Type: `iceplasma`
    - Press Type: `blast`

### Tactical Cryonics

A set of functions for tavriya environments.  
Press - launch an Ice Cloud Nade;  
Hold - change firemodes.  
Works especially well against targets vulnerable to low temperatures.

Parameters:

- Base Dps: 8
- Energy Usage: 36
- Fire Time: 0.5
- Fire Types:  `auto`,  `charge`,  `burst`
- Hold Firemodes: `True`
- Press Params:
  - Type: `icecloudgrenade`
- Press Type: `nade`

## Sources

Found naturally in containers:

- `icechest`
- `icespherechest`

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)
- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/biome/ct_sona_loot.png" alt="Sona Loot Crate icon" loading="lazy" width="auto" height="16px"> [Sona Loot Crate](https://ceterai.github.io/MyEnternia/Wiki/SonaLootCrate)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_alta_sona_rifle`
- Level: `5`
- Power: `3.0`
- Rarity: `Rare`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`assaultrifle`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Assaultrifle), [`ice`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ice), [`ranged`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ranged), [`rare`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Rare), [`sona`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Sona), [`tavriya`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Tavriya), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/ranged/alta/rifle/ct_alta_sona_rifle.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/rifle/ct_alta_sona_rifle.activeitem)
