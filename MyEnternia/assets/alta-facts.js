// Random Alta Fact Generator
(function() {
    'use strict';

    const altaFacts = [
        // Tenants
        { text: "Alta tenants pay rent in crystals and prism shards instead of pixels — because they are more common among altas then pixels.", icon: "🏠", category: "Tenants" },
        { text: "There are 187 tenant types in the mod, and some of them are cosplaying stuff from the human world — including altas dressed as bananas, sharks, dinosaurs, and pirates 🍌🦈🦕🏴‍☠️", icon: "🏠", category: "Tenants" },

        // NPCs
        { text: "Among the 176 alta NPC types, there are dedicated cosplay NPCs — yes, you can have a banana girl move into your colony.", icon: "🧑‍🔬", category: "NPCs" },

        // Monsters
        { text: "Alta robotics include everything from combat drones to a fully functional waiter bot — and yes, an alta Roomba that just... roombas around. 🧹", icon: "👾", category: "Monsters" },
        { text: "The mod has about 120 monster types total, and 32+ of those are alta-built robots organized into drone and droid classes!", icon: "👾", category: "Monsters" },

        // Critters
        { text: "There are 48 critter species across alta planets, including a flower that hunts (the Hunter Flower) and the Koyscream — a frog whose name tells you exactly what it does. 🐸💀", icon: "🦗", category: "Critters" },
        { text: "36 critters + 12 bugs = 48 little guys!", icon: "🦗", category: "Critters" },

        // Biomes
        { text: "'Orbital Strike' is classified as a weather type on Enterash planets. Yes, the weather forecast is literally artillery from orbit.", icon: "🌍", category: "Biomes" },
        { text: "The mod adds 43 unique biomes across planets like Alterash and Alterash Prime!", icon: "🌍", category: "Biomes" },

        // Items
        { text: "Altas have their own cola (Tsay Cola) and energy drink (VMAX) — because even a highly advanced alien civilization needs energy to get through the day.", icon: "⚔️", category: "Items" },
        { text: "The mod adds 354+ active items, and a full tier 0–4 progression system — where tier 4 weapons are literally powered by condensed dream energy.", icon: "⚔️", category: "Items" },

        // Codex Entries
        { text: "There are 102 codex entries documenting alta civilization — and they come in three formats: Datamasses (digital), Ebooks (electronic readers), and Paper (yes, altas still use paper sometimes).", icon: "📖", category: "Codex" },

        // Objects
        { text: "The mod adds 846 placeable objects to the game — from alta crafting stations to decorative furniture. That's more objects than some entire mods have files.", icon: "🏗️", category: "Objects" },

        // Alkey Language
        { text: "In the Alkey language, the word 'corgi' means 'literature.' No relation to the dog. Probably. 📚🐕", icon: "🗣️", category: "Alkey" },
        { text: "Altas count in hexadecimal — their word for 16 is 'ales,' literally meaning 'the 10 of altas.' Because who needs base-10 when you're a superior civilization?", icon: "🗣️", category: "Alkey" },
        { text: "The Alkey dictionary has ~400 words. The word 'altamisu' means 'alta soup' — and yes, it sounds like tiramisu on purpose.", icon: "🗣️", category: "Alkey" },
        { text: "'MECA' stands for Mira + Elin + Celestia + Alliana — the four Alta Mothers. It's also just a really cool acronym.", icon: "🗣️", category: "Alkey" },

        // Alta Orgs & Companies
        { text: "The alta fashion brand Perizhad dominates so completely that when one helmet turned out NOT to be designed by them, the product description literally says: 'Wait, what? This helmet wasn't designed by Perizhad. Wow.' >>:3", icon: "🏢", category: "Orgs & Companies" },
        { text: "Altas have their own IKEA — a furniture company called Unika that makes office furniture from refined poison crystals (bishyn). The extracted poison particles? They use them as polish for that 'pretty gloss' finish. ✨", icon: "🏢", category: "Orgs & Companies" },
        { text: "Ortan Ti is an alta beverage company that produces Tsay-Cola and Gheanade (a soda made from liquid crystal). Meanwhile, Vitai Ordis makes V-Max — an alta energy drink. Yes, this civilization has brand rivalries. 🥤", icon: "🏢", category: "Orgs & Companies" },

        // Characters
        { text: "Mira, the first-ever alta, is technically not even organic — she's an AI in an android body. The first alta body was actually built as her prototype, and every alta since was grown from that blueprint!", icon: "👤", category: "Characters" },
        { text: "Celestia, one of the four Alta Mothers, isn't actually an alta at all — she's an all-powerful stardust being. But altas consider her one of theirs anyway, because that's just how altas roll. 💙", icon: "👤", category: "Characters" },
        { text: "The word 'MECA' (the leadership council) isn't just a cool name — it's literally the initials of the four Alta Mothers: Mira, Elin, Celestia, and Alliana. And yes, there's also a cake named after Alliana. 🎂", icon: "👤", category: "Characters" },

        // Botanics
        { text: "The Alta Botanics Guide describes exactly 5 types of farming: Terraponics, Hydroponics, Ecoponics, Thermoponics, and Omniponics. There are also 8 dedicated plant-related professions — altas take their gardening very seriously.", icon: "🌿", category: "Botanics" },
        { text: "According to alta botanics, tonna fruit is 'botanically speaking, a nut.' Some things are universal even in space. 🥜", icon: "🌿", category: "Botanics" },

        // Yaara
        { text: "Yaara megaplants grow so large they develop their own ecosystems, complete with unique flora, fauna, and humanoid plant guardians called Yaara Keepers. The main diplomatic issue between altas and keepers? Altas keep trying to pour blue fire (alternia energy) on the groves. 🔥🌿", icon: "🌱", category: "Yaara" },
        { text: "There's a 'sacred yaara frog' called a Yaafrog, and you can carve Yaajacks (jack-o-lanterns) from yaara melons that glow orange during Ceternity (the alta Halloween)! 🐸🎃", icon: "🌱", category: "Yaara" },

        // Rainbow Wood
        { text: "Vionora — the alta name for rainbow wood trees — are palm-like trees that only grow on viona-infested riversides and need to be at least 50% submerged in liquid. The word literally means 'viona tree' in Alkey, and 'spectro' is the alta word for rainbow! 🌈", icon: "🌈", category: "Rainbow Wood" },

        // Corfals
        { text: "CorFals (Correctional Facilities) are basically alta daycare-hospital-rehabilitation combos. Every single alta starts life in one after being grown in Elin Gardens. Caretakers read to them, cook for them, and use a treat called 'shokka' as a pacifier method for 'very energetic unbehaving altas.' >~<", icon: "🏥", category: "Corfals" },
        { text: "The sonaveil pie recipe 'varies between alta cities, corfals, and colonies, each adding their own cherished touches' — so corfals have signature pie recipes. That's adorable. 🥧", icon: "🏥", category: "Corfals" },

        // Energy Tools
        { text: "Altas don't call their weapons 'weapons' — they call them 'energy tools,' because of course a research-obsessed civilization would rebrand swords and blasters as scientific instruments. As a glitch traveller points out: 'Their terminology for weapons reveals their scientific perspective.'", icon: "⚡", category: "Energy Tools" },
        { text: "The plasmasword is described as 'an energy tool to all energy tools' — the alta equivalent of calling something the tool of all tools. It's also the 'visit card of alta gladiators,' meaning gladiators exist and they fight with plasma swords! ⚔️✨", icon: "⚡", category: "Energy Tools" },
    ];

    // Generate random fact
    function generateFact() {
        return altaFacts[Math.floor(Math.random() * altaFacts.length)];
    }

    // Replace <!-- alta fact --> placeholder
    function replaceFactPlaceholder(fact) {
        const placeholder = document.body.innerHTML;
        if (placeholder.includes('<!-- alta fact -->')) {
            const factHTML = `
                <div class="alta-fact-box">
                    <div class="fact-content">
                        <div class="fact-icon">${fact.icon}</div>
                        <div class="fact-body">
                            <div class="fact-category">${fact.category}</div>
                            <div class="fact-text">${fact.text}</div>
                        </div>
                        <button class="fact-refresh" title="New fact" onclick="window.refreshAltaFact()">⟳</button>
                    </div>
                </div>
            `;
            document.body.innerHTML = placeholder.replace('<!-- alta fact -->', factHTML);
        }
    }

    // Refresh fact function
    window.refreshAltaFact = function() {
        const fact = generateFact();
        const factIcon = document.querySelector('.alta-fact-box .fact-icon');
        const factCategory = document.querySelector('.alta-fact-box .fact-category');
        const factText = document.querySelector('.alta-fact-box .fact-text');
        if (factIcon && factCategory && factText) {
            factIcon.textContent = fact.icon;
            factCategory.textContent = fact.category;
            factText.textContent = fact.text;
        }
    };

    // Initialize
    function init() {
        if (!document.body.innerHTML.includes('<!-- alta fact -->')) return;

        const fact = generateFact();
        replaceFactPlaceholder(fact);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
