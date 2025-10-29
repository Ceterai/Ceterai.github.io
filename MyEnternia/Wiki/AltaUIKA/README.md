# Alta UIKA

> Source: [Alta Consumables Builder](https://github.com/Ceterai/Enternia/tree/main/data/alta_database.json)

**Alta Universal Information & Knowledge Accumulation** (UIKA) is the central alta database system introduced in version 2.3.4e - a comprehensive generated JSON document containing information about all items in the mod.

**System Purpose:**

- **Item Acquisition Data** - Documents how to obtain every item (crafting, loot, discovery)
- **Usage Information** - Records what items can be used for (recipes, applications)
- **Real-Time Access** - Allows in-game items to query information without on-the-spot calculations
- **Wiki Generation** - Provides structured data for automated documentation generation

**Technical Implementation:**

- **Location** - Stored at `/data/alta_database.json`
- **Format** - Structured JSON with indexed item relationships
- **Update System** - Automatically regenerated when mod content changes
- **Query Optimization** - Pre-calculated data reduces in-game processing overhead

UIKA serves as the foundation for both in-game knowledge systems (Scanner, Datacenter) and external documentation tools, ensuring consistency across all information sources about alta civilization and technology.
