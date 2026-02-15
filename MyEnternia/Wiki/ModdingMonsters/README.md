> Main page: <img src="https://starbounder.org/mediawiki/images/8/81/Tool_Nav_Icon.png" alt="icon" loading="lazy" width="auto" height="16px"> [Modding](https://ceterai.github.io/MyEnternia/Wiki/Modding)

This page contains technical information regarding monsters added by this mod.

### Effects

Monsters created in this mod can have permanent status effects on them. This is due to a custom **monster builder**.

The builder is located here: [/monsters/ct_ioterash_monster.lua](https://github.com/Ceterai/Enternia/blob/main/monsters/ct_ioterash_monster.lua)

Example: <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/spawners/drones/scout.png" alt="Scout Drone icon" loading="lazy" width="auto" height="16px"> [Scout Drone](https://ceterai.github.io/MyEnternia/Wiki/ScoutDrone)

### Abilities

You may notice that most monsters have fields like `primaryAbility` and `passiveAbility` in their files. This is mainly for use by [Monster Spawners](https://ceterai.github.io/MyEnternia/Wiki/ModdingItems#monster-spawners) for display in tooltips, and for display on the **wiki**.

Example: <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/spawners/drones/scout.png" alt="Scout Drone icon" loading="lazy" width="auto" height="16px"> [Scout Drone](https://ceterai.github.io/MyEnternia/Wiki/ScoutDrone)

### Behavior

Currently there is a WIP alarm behavior in place. It is not used as of right now.

### Ship Pets

Species pets in this mod can make sounds (often) and sing (rarely).

Scripts implementing that:
- [/monsters/alta/pets/drone/petBehavior.lua](https://github.com/Ceterai/Enternia/blob/main/monsters/alta/pets/drone/petBehavior.lua)
- [/monsters/alta/pets/drone/singState.lua](https://github.com/Ceterai/Enternia/blob/main/monsters/alta/pets/drone/singState.lua)
- [/monsters/alta/pets/drone/soundState.lua](https://github.com/Ceterai/Enternia/blob/main/monsters/alta/pets/drone/soundState.lua)
Pet example: Personal Drone
