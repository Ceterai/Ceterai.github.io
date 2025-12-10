# Vionos Twins

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_enchanted_twins.png" alt="Vionos Twins icon" loading="lazy" width="auto" height="16px"> **Vionos Twins** is an uncommon two-handed cryogenic broadsword.

Someone did the seemingly impossible - used anomaly energy to create a tool. You can sense slight magnetic pulls coming from it.  
This dangerous yet powerful combo doesn't seem to go well with usual alta safety protocols. Still, it might be pretty enticing to some.

Can be upgraded to <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/melee/alta/heavy/ct_enchanted_twins_2.png" alt="Bi-Blade ★ icon" loading="lazy" width="auto" height="16px"> [Bi-Blade ★](https://ceterai.github.io/MyEnternia/Wiki/Bi-Blade) at the Weapon Upgrade Anvil.

## Ingame

Species descriptions:

- Alta: This seems a bit hazardous. I should probably consult with a coordinator first, just in case. Viona anomalies can be pretty dangerous.

Radiomessages on pickup:

- You've just picked up an alta weapon, or an "energy tool", as they call it. According to my database, these usually have an extended set of features. I suggest reading its description.

## Parameters

### Viona Resonation

A sequence of 3 heavy strikes. Hold to perform a [blade charge](https://ceterai.github.io/MyEnternia/Wiki/Weapons#Blade-Charge). Hold in air to [downstab](https://ceterai.github.io/MyEnternia/Wiki/Weapons#Downstab).  
The special resonation creates slight energy vibrations between the twins, providing additional power to each hit.

Parameters:

- Base Dps: 12
- Fire Time: 0.83
- Energy Usage: 32
- Hold Params:
  - Charge Border: `FF33FF88`
  - Damage Config:
    - Damage Source Kind: `icebroadsword`
    - Status Effects:  `frostslow`
    - Ranged:
      - Type: `smallicecloud`
      - Count: 3
      - Params:
        - Speed: 10
      - Inaccuracy: 1.57
      - Offset:  5.0,  -0.85
      - Sound: <img src="https://starbounder.org/mediawiki/images/7/77/Ice.png" alt="Ice icon" loading="lazy" width="10px" height="10px"> [Ice](https://starbounder.org/Ice)
- Damage Config:
  - Base Damage: 22.5
  - Knockback: 40
  - Damage Source Kind: `broadsword`
  - Knockback Mode: `facing`
  - Timeout: 0.5
- Steps: 
- Damage Factor: 1.0
- Energy Factor:
- Knockback: 10.0
- Swoosh: `swoosh1`
- Swoosh Offset Region:  0.75, ,  4.25,  5.0
- Element: `physical`, 
- Damage Factor: 0.4
- Energy Factor:
- Knockback: 5.0
- Swoosh: `swoosh2`
- Swoosh Offset Region:  3.0,  -0.5,  6.5,  2.0
- Element: `physical`, 
- Damage Factor: 1.1
- Energy Factor:
- Knockback: 25.0
- Swoosh: `swoosh3`
- Swoosh Offset Region:  1.5,  -1.0,  5.5,  1.0
- Damage Source Kind: `icebroadsword`
- Status Effects:  `frostslow`

### Resonation

Raises an ice pillar in front of you.  
The impact from this special attack quickly dissipates, as not all viona combinations are able to exist for extended periods of time.

## Sources

Found naturally in containers:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/objects/biome/alterash/viona/chest/icon.png" alt="Enchanted Chest icon" loading="lazy" width="auto" height="16px"> [Enchanted Chest](https://ceterai.github.io/MyEnternia/Wiki/EnchantedChest)

Can be bought from merchants:

- [Alta Agent](https://ceterai.github.io/MyEnternia/Wiki/AltaAgent)
- [Alta Merchant](https://ceterai.github.io/MyEnternia/Wiki/AltaMerchant)
- [Neiteru Archiver](https://ceterai.github.io/MyEnternia/Wiki/NeiteruArchiver)
- [Viona Merchant](https://ceterai.github.io/MyEnternia/Wiki/VionaMerchant)

Can be obtained from special items:

- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/biome/ct_enchanted_loot.png" alt="Enchanted Loot Crate icon" loading="lazy" width="auto" height="16px"> [Enchanted Loot Crate](https://ceterai.github.io/MyEnternia/Wiki/EnchantedLootCrate)
- <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/loot/other/gsr.png" alt="GSR Pod ★★★ icon" loading="lazy" width="auto" height="16px"> [GSR Pod ★★★](https://ceterai.github.io/MyEnternia/Wiki/GSRPod)

Can be obtained via <img src="https://raw.githubusercontent.com/Silverfeelin/Starbound-SpawnableItemPack/master/interface/sip/iconSmall.png" alt="Spawnable Item Pack icon" width="18" height="14"/> [Spawnable Item Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=733665104) or <img src="https://steamuserimages-a.akamaihd.net/ugc/263843960696222713/3EC9A7C005541F7D577EBCB8C5736B4EFC9973D6/" alt="icon" width="8" height="12"/> [Tabula Rasa](https://community.playstarbound.com/resources/the-tabula-rasa.3222/) (if you have any of them installed).

## Technical Information

- In-game ID: `ct_enchanted_twins`
- Level: `4`
- Power: `2.5`
- Rarity: `Uncommon`
- Tags: [`alta`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Alta), [`broadsword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Broadsword), [`enchanted`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Enchanted), [`ice`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Ice), [`melee`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Melee), [`sword`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Sword), [`twinblade`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Twinblade), [`uncommon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Uncommon), [`upgradeableWeapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/UpgradeableWeapon), [`viona`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Viona), [`vionos`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Vionos), [`weapon`](https://ceterai.github.io/MyEnternia/Wiki/Tags/Weapon)
- File: [`/items/active/weapons/melee/alta/heavy/ct_enchanted_twins.activeitem`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/heavy/ct_enchanted_twins.activeitem)
