# My Enternia Wiki Generator

This folder contains scripts used to generate this wiki based on files from the mod.

## Usage

1. Make sure you have Python 3.8+ installed.
1. Execute `main.py`. It will generate subfolders with files in them.
1. When ready to push to GitHub, move all generated files into root directory.

### Config

To make the scripts work with your mod properly, edit the `config.py` file.
To make the wiki suit your mod better, you'll have to edit the rest of the scripts.

### Supported Features

- supports all basic parameters of all items, objects, effects, weather, biomes, monsters and projectiles.
- has a shared script for all of them, meaning item parameters are also supported for objects, biomes, etc., and vise-versa.
- supports crafting recipes and loot tables.
- supports icons, custom categories, external links.
- converts color highlights in descriptions to links with icons.
- custom parameter `longdescription` is also supported and is displayed after the regular description.
- custom parameter `threat` for weather (or anything else).
- custom parameter `asset` containing path to another json file and is merged into current one if present.
- converts IDs to proper readable names if possible (if no name parameters like `shortdescription`, `title` or `friendlyName` are present).

### TODO

- leveled price

### Known Issues

Can generate pages with same names if they have same names in the mod (or similar names sometimes).  
This is partially because in order to be GitHub Wiki-compatible, all files are named after asset names, and replace all spaces and underscores with dashes, and slashes with `-by-`.
