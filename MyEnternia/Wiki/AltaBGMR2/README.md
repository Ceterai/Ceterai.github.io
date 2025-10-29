# Alta BGMR2

> Source: [Alta Consumables Builder](https://github.com/Ceterai/Enternia/tree/main/items/buildscripts/alta/consumable.lua)

**Alta Bromatology, Gastronomy & Medicine Regulation M2** (ABGMR2) is the official alta food balancing and quality control system introduced in update 2.3.4e. This regulatory framework ensures all consumable items in alta cuisine maintain consistent standards for nutritional value, preservation, and effect potency.

**Core Principles:**

- **Power Scaling** - Food effects scale with item level/tier for consistent progression
- **Rot-to-Effect Balance** - Tradeoff between preservation time and beneficial effect duration
- **Effect Stacking** - Multiple effects (positive, negative, emotional) interact dynamically
- **Food Value Calculation** - Standardized hunger restoration based on ingredients and preparation

**System Parameters:**

- **Good Effects** - Beneficial status effects scaled by power and duration
- **Bad Effects** - 5-second negative effects that increase good effect duration
- **Mood Effects** - Emotional status effects (Happy, Inspired, Passionate, etc.) that slightly reduce good effect time
- **Rot Ratio** - Configurable balance between preservation time and effect potency (1.0 = 50/50 split)

**Aging Categories:**

The system classifies food freshness into granular stages:

- **Fermenting** - Up to 30 minutes (intentional fermentation process)
- **Fresh** - Up to 8 hours (optimal consumption window)
- **Preserved** - Up to 2 weeks (extended shelf life)
- **Unexpirable** - Up to 256 years (near-permanent preservation)

This system replaced earlier inconsistent food mechanics and now governs all 214+ alta prepared food recipes and 225+ total food-related items in the mod.
