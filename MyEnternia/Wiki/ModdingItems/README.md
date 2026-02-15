> Main page: <img src="https://starbounder.org/mediawiki/images/8/81/Tool_Nav_Icon.png" alt="icon" loading="lazy" width="auto" height="16px"> [Modding](https://ceterai.github.io/MyEnternia/Wiki/Modding)

This page contains modding information about <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/generic/crafting/alta/energy_cell.png" alt="icon" loading="lazy" width="auto" height="16px"> [items](https://ceterai.github.io/MyEnternia/Wiki/Items) added by this mod, including item builders, item scripts, weapon abilities, etc.
- Items
-   - Item Builder Parameters
- Weapons
-   - Weapon Builder Parameters
-   - Abilities
- Objects
-   - Object Builder Parameters
-   - Object Logic
-     - Switch Logic
-   - Saplings
- Consumable Items
-   - Consumable Builder Parameters
-   - Variants
- Monster Spawners
-   - Spawner Builder Parameters
-   - Spawner Logic
-     - Spawner Projectile
> Note: Read more about item and object build scripts here: [Alta Item Builders](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/README.md)

## Items

Most items in this mod use a custom item builder. It extracts as much information as possible from an asset and calculates params and tooltips based on them.

It is currently used for:
- [Crafting Materials & Cooking Ingredients](Generic-Items)
- [Epp Augments & Pet Collars](Enhancement-Items)
- [Active Items (Weapons, Shields, Loot Items)](Active-Items)
- [Clothing](Clothing)
- [Codexes](Codexes)
The builder is located here: [`/items/buildscripts/alta/item.lua`](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/item.lua)

Refer to the builder file for more documentation.

### Item Builder Parameters

More info: [Alta Item Builders - Items](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/README.md#items)

All listed parameters are optional.

<table><thead><tr><th>Parameter</th><th>Default</th><th>Description</th></tr></thead><tbody>

<tr><td>`level`</td><td>1</td><td>Item level. Will not be overridden by custom levels if `fixedLevel` is set to `true`.</td></tr>

<tr><td>`price`</td><td>0</td><td>Can be fixed if `fixedPrice` is `true`, or level-dependant.</td></tr>

<tr><td>`race`</td><td>`nil`</td><td>Will be displayed in a tooltip if set.</td></tr>

<tr><td>`fixedLevel`</td><td>`true`</td><td>Prevents the level param from being overwritten with custom values.</td></tr>

<tr><td>`fixedPrice`</td><td>`false`</td><td>If false, the price will be calculated based on level using `itemLevelPriceMultiplier` calc function.</td></tr>

<tr><td>`damageLevelMultiplier`</td><td>1.0</td><td>Calculates based on item level using the `weaponDamageLevelMultiplier` calc function.</td></tr>

<tr><td>`elementalType`</td><td>`"physical"`</td><td>Can match any existing element, just like with original Starbound weapons. If set, replaces the `<elementalType>` patterns in asset's data.</td></tr>

<tr><td>`primaryAbility`</td><td>`nil`</td><td>Primary ability, supports `elementalConfig`. Not used by majority of items.</td></tr>

<tr><td>`altAbility`</td><td>`nil`</td><td>Special ability, supports `elementalConfig`. Not used by majority of items.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`palette`</td><td>`nil`</td><td>Used for color swaps like with original Starbound weapons.</td></tr>

<tr><td>`colorIndex`</td><td>1</td><td>Used for color swaps like with original Starbound weapons.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`baseDps` or `primaryAbility.baseDps`</td><td>0</td><td>Item's DPS. If set, will be displayed in some tooltips.</td></tr>

<tr><td>`fireTime` or `primaryAbility.fireTime`</td><td>0.0</td><td>Item's general Fire Rate. If set, will be displayed in some tooltips.</td></tr>

<tr><td>`energyUsage` or `primaryAbility.energyUsage`</td><td>0</td><td>Item's general Energy Usage. If set, will be displayed in some tooltips.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`baseShieldHealth`</td><td>0.0</td><td>Item's leveled Shield Health. If set, will be displayed in some tooltips.</td></tr>

<tr><td>`cooldownTime`</td><td>0</td><td>Item's general Cooldown Time. If set, will be displayed in some tooltips.</td></tr>

<tr><td>`knockback`</td><td>0</td><td>Item's general Knockback. If set, will be displayed in some tooltips.</td></tr>

<tr><td>`minActiveTime`</td><td>0</td><td>Item's general Min Time. If set, will be displayed in some tooltips.</td></tr>

<tr><td>`perfectBlockTime`</td><td>0</td><td>Item's general Parry Time. If set, will be displayed in some tooltips.</td></tr>

<tr><td>`forceWalk`</td><td>`false`</td><td>Item's general "Heaviness" determinator, used in shields to determine whether it will force you to walk when raise. Not currently displayed.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`primaryAbility.name`</td><td>`"unknown"`</td><td>Primary ability name for tooltips.</td></tr>

<tr><td>`primaryAbility.description`</td><td>`""`</td><td>Primary ability description for tooltips.</td></tr>

<tr><td>`altAbility.name`</td><td>`"unknown"`</td><td>Special ability name for tooltips. If not set, tries to use the ability default first, and only then the default mentioned here.</td></tr>

<tr><td>`altAbility.description`</td><td>`""`</td><td>Special ability description for tooltips.</td></tr>

<tr><td>`passiveAbility.name`</td><td>`"unknown"`</td><td>Passive ability name for tooltips. Will replace Special if set.</td></tr>

<tr><td>`passiveAbility.description`</td><td>`""`</td><td>Passive ability description for tooltips. Will replace Special if set.</td></tr>

<tr><td>`upgradeParameters`</td><td>`nil`</td><td>For upgrades: [Weapons: Upgrades](https://ceterai.github.io/MyEnternia/Wiki/AltaWeaponry#upgrades).</td></tr>

<tr><td>`upgradeParameters.shortdescription`</td><td>`nil`</td><td>Upgrade name for tooltips.</td></tr>

</tbody></table>

## Weapons

> Main page: <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/blaster/ct_alta_scout_blaster.png" alt="icon" loading="lazy" width="auto" height="16px"> [Weapons](https://ceterai.github.io/MyEnternia/Wiki/Weapons)

Most <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/weapons/ranged/alta/blaster/ct_alta_scout_blaster.png" alt="icon" loading="lazy" width="auto" height="16px"> [weapons and shields](https://ceterai.github.io/MyEnternia/Wiki/Weapons) in this mod use a custom item builder, custom logic and custom abilities.

The builder used is the same mentioned in the previous section.

### Weapon Builder Parameters

Weapons and shields support the same parameters as in [Supported Item Parameters](#supported-item-parameters).

### Abilities

Used custom weapon scripts and abilities can be found here:

Weapon Base:
- [`/items/active/weapons/ct_alta_weapon.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ct_alta_weapon.lua)
Melee Bases:
- [`/items/active/weapons/melee/alta/melee.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/melee.lua)
- [`/items/active/weapons/melee/alta/enhanced.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/enhanced.lua)
- [`/items/active/weapons/melee/alta/special.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/melee/alta/special.lua)
Ranged Bases:
- [`/items/active/weapons/ranged/alta/ranged.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/ranged.lua)
- [`/items/active/weapons/ranged/alta/rifle.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/rifle.lua)
Special Ranged Abilities:
- [`/items/active/weapons/ranged/alta/abils/chakram/chakram.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/abils/chakram/chakram.lua)
- [`/items/active/weapons/ranged/alta/abils/grapple/grapple.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/abils/grapple/grapple.lua)
- [`/items/active/weapons/ranged/alta/abils/orbs/orbs.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/weapons/ranged/alta/abils/orbs/orbs.lua)
Read more about supported weapon abilities: [Weapon Mechanics](https://ceterai.github.io/MyEnternia/Wiki/AltaWeaponry#mechanics)

## Objects

Most objects in this mod use a custom item builder. It enhances the item builder mantioned above.

The builder is located here: [`/items/buildscripts/alta/object.lua`](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/object.lua)

### Object Builder Parameters

More info: [Alta Item Builders - Objects](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/README.md#objects)

All listed parameters are optional.

<table><thead><tr><th>Parameter</th><th>Default</th><th>Description</th></tr></thead><tbody>

<tr><td>Item Builder Params</td><td>-</td><td>All parameters mentioned in the **Supported Item Parameters** section.</td></tr>

<tr><td>`smashOnBreak` or `smashable`</td><td>`false`</td><td>If set, displays tooltip note "This object doesn't drop itself when broken/smashed!"</td></tr>

<tr><td>`slotCount`</td><td>`nil`</td><td>If set, displays in a tooltip.</td></tr>

<tr><td>`lightColor`</td><td>`nil`</td><td>If set, displays the color in a form of a star in a tooltip.</td></tr>

<tr><td>`colonyTags`</td><td>[]</td><td>If set, displays in a tooltip.</td></tr>

<tr><td>`health`</td><td>1.0</td><td>Displays in a tooltip, multiplied by 10.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`touchDamage.baseDamage` or `touchDamage.damage` or `touchDamage.power` or `baseDamage` or `damage` or `power`</td><td>`nil`</td><td>If set, displays in a tooltip.</td></tr>

<tr><td>`touchDamage.fireTime` or `fireTime`</td><td>`nil`</td><td>If set, displays in a tooltip.</td></tr>

<tr><td>`touchDamage.energyUsage` or `energyUsage`</td><td>`nil`</td><td>If set, displays in a tooltip.</td></tr>

<tr><td>`touchDamage.knockback` or `knockback`</td><td>`nil`</td><td>If set, displays in a tooltip.</td></tr>

</tbody></table>

### Object Logic

Some objects use scripts to function, with a lot of them using custom scripts made for this mod.

#### Switch Logic

Most switch-like and light-like objects in the mod use a single custom script with many parameters.

This script can be found here: [`/objects/alta/switch.lua`](https://github.com/Ceterai/Enternia/blob/main/objects/alta/switch.lua)

### Saplings

More info: [Alta Item Builders - Saplings](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/README.md#saplings)

## Consumable Items

Consumable items like Food, Medicine, etc. in this mod use a custom item builder. It enhances the original **buildfood.lua**.

The builder is located here: [`/items/buildscripts/alta/consumable.lua`](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/consumable.lua)

### Consumable Builder Parameters

More info: [Alta Item Builders - Consumables](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/README.md#consumables)

All listed parameters are optional.

<table><thead><tr><th>Parameter</th><th>Default</th><th>Description</th></tr></thead><tbody>

<tr><td>Item Builder Params</td><td>-</td><td>All parameters mentioned in the **Supported Item Parameters** section.</td></tr>

<tr><td>`fixedPrice`</td><td>`true`</td><td>Unlike for other items, this value is true by default.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`rotConfig`</td><td>[`"/items/generic/food/ct_ionic_rotting.config"`](https://github.com/Ceterai/Enternia/blob/main/items/generic/food/ct_ionic_rotting.config)</td><td>Path to rotting config, if used.</td></tr>

<tr><td>`timeToRot`</td><td>`nil`</td><td>If set, sets fixed max rotting time without multipliers.</td></tr>

<tr><td>`rottingMultiplier`</td><td>1.0</td><td>If `timeToRot` isn't set, this is used to dynamically determine those parameters.</td></tr>

<tr><td>`foodValue`</td><td>`nil`</td><td>If set, displays in a tooltip.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`variants`</td><td>[]</td><td>If set, displays in a tooltip. If the item has an aging spript attached, this might be used to turn the item into one of possible variants.</td></tr>

</tbody></table>

### Variants

Consumable items that have a `variants` parameter set and use an aging scripted called [`/items/generic/food/ct_food_aging.lua`](https://github.com/Ceterai/Enternia/blob/main/items/generic/food/ct_food_aging.lua) have a chance to turn into one of the variants shortly after crafting.

This is mainly used for the <img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/codex/alta/ebook/crystalline_prime.png" alt="Perfect Cooking icon" loading="lazy" width="auto" height="16px"> [Perfect Cooking](https://ceterai.github.io/MyEnternia/Wiki/PerfectCooking) mechanic.

## Monster Spawners

<img src="https://raw.githubusercontent.com/Ceterai/Enternia/main/items/active/alta/spawners/drones/companion.png" alt="icon" loading="lazy" width="auto" height="16px"> [Monster Spawners](https://ceterai.github.io/MyEnternia/Wiki/Spawners) in this mod use a custom item builder.

The builder is located here: [`/items/buildscripts/alta/spawner.lua`](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/spawner.lua)

### Spawner Builder Parameters

More info: [Alta Item Builders - Spawners](https://github.com/Ceterai/Enternia/blob/main/items/buildscripts/alta/README.md#spawners)

All listed parameters are optional except for `asset`.

<table><thead><tr><th>Parameter</th><th>Default</th><th>Description</th></tr></thead><tbody>

<tr><td>Item Builder Params</td><td>-</td><td>All parameters mentioned in the **Supported Item Parameters** section.</td></tr>

<tr><td colspan="3"></td></tr>

<tr><td>`asset`</td><td>`nil`</td><td>Path to the `.monstertype` file to load config from.</td></tr>

<tr><td>`subtitle`</td><td>`Tool`</td><td>An item subtitle displayed in the tooltip.</td></tr>

<tr><td>`pets`</td><td>`nil`</td><td>If set, a random monster is selected from this list.</td></tr>

</tbody></table>

### Spawner Logic

The logic is similar to how [Capture Pods](https://starbounder.org/Capture_Pod) work - on use, a monster spawner releases a creature contained within it.

The file with the logic is located here: [`/items/active/alta/spawner.lua`](https://github.com/Ceterai/Enternia/blob/main/items/active/alta/spawner.lua)

#### Spawner Projectile

Activating a monster spawner item involves throwing a special projectile containing custom logic.

This logic can be found here: [`/projectiles/spawner/ct_monster_spawner.lua`](https://github.com/Ceterai/Enternia/blob/main/projectiles/spawner/ct_monster_spawner.lua)
