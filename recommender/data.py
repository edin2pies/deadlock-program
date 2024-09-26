# recommender/data.py

import re
from collections import defaultdict

# Dictionary of heroes and their counter items
hero_counters = {
    "abrams": ["Decay", "Toxic Bullets", "Healbane"],
    "bebop": ["Debuff Remover", "Ethereal Shift", "Warp Stone", "Reactive Barrier"],
    "dynamo": ["Reactive Barrier", "Rescue Beam", "Soul Rebirth"],
    "grey talon": ["Debuff Remover", "Ethereal Shift", "Knockdown"],
    "haze": ["Warp Stone", "Return Fire", "Metal Skin"],
    "infernus": ["Debuff Reducer", "Debuff Remover", "Slowing Hex"],
    "ivy": ["Super Stamina", "Warp Stone", "Silence Glyph"],
    "kelvin": ["Super Stamina", "Ethereal Shift"],
    "lady geist": ["Silencer", "Silence Glyph"],
    "lash": ["Slowing Hex", "Silence Glyph", "Ethereal Shift"],
    "mcginnis": ["Superior Stamina", "Monster Rounds"],
    "mo_krill": ["Reactive Barrier", "Slowing Hex", "Silence Glyph"],
    "paradox": ["Ethereal Shift"],
    "pocket": ["Debuff Reducer", "Debuff Remover", "Silence Glyph"],
    "seven": ["Knockdown"],
    "shiv": ["Debuff Reducer", "Debuff Remover"],
    "vindicta": ["Superior Stamina", "Debuff Remover", "Ethereal Shift", "Knockdown"],
    "viscous": ["Silence Glyph", "Superior Stamina"],
    "warden": ["Superior Stamina", "Debuff Remover", "Ethereal Shift", "Slowing Hex"],
    "wraith": ["Ethereal Shift", "Metal Skin", "Return Fire"],
    "yamato": ["Silence Glyph", "Ethereal Shift"]
}

# Dictionary of player's heroes and their preferred items
preferred_items = {
    "abrams": ["Healing Booster"],
    "bebop": ["Monster Rounds", "Majestic Leap"],
    "dynamo": ["Warp Stone"],
    "grey talon": ["Superior Stamina"],
    "haze": ["Silencer"],
    "infernus": ["Toxic Bullets", "Ethereal Shift"],
    "ivy": ["Monster Rounds", "Rescue Beam"],
    "kelvin": [],
    "lady geist": ["Healbane", "Warp Stone"],
    "lash": ["Superior Stamina", "Monster Rounds"],
    "mcginnis": ["Superior Stamina", "Echo Shard"],
    "mo_krill": ["Fleetfoot"],
    "paradox": ["Warp Stone"],
    "pocket": ["Majestic Leap"],
    "seven": ["Monster Rounds", "Echo Shard"],
    "shiv": ["Debuff Remover"],
    "vindicta": ["Silencer"],
    "viscous": ["Monster Rounds", "Silence Glyph"],
    "warden": ["Monster Rounds", "Fleetfoot"],
    "wraith": ["Monster Rounds", "Silence Glyph"],
    "yamato": ["Healbane"]
}

# Reverse mapping from cleaned hero names to original names for output
original_hero_names = {
    "abrams": "Abrams",
    "bebop": "Bebop",
    "dynamo": "Dynamo",
    "grey talon": "Grey Talon",
    "haze": "Haze",
    "infernus": "Infernus",
    "ivy": "Ivy",
    "kelvin": "Kelvin",
    "lady geist": "Lady Geist",
    "lash": "Lash",
    "mcginnis": "McGinnis",
    "mo_krill": "Mo_Krill",
    "paradox": "Paradox",
    "pocket": "Pocket",
    "seven": "Seven",
    "shiv": "Shiv",
    "vindicta": "Vindicta",
    "viscous": "Viscous",
    "warden": "Warden",
    "wraith": "Wraith",
    "yamato": "Yamato"
}

def clean_hero_input(hero_name):
    # Remove any non-alphabetic characters and convert to lowercase
    cleaned_name = re.sub(r'[^a-zA-Z]', '', hero_name).lower()
    return cleaned_name

def get_counter_items_ordered(enemy_team):
    item_impact = defaultdict(lambda: {"count": 0, "heroes": []})
    
    for hero in enemy_team:
        cleaned_hero = clean_hero_input(hero)
        if cleaned_hero in hero_counters:
            for item in hero_counters[cleaned_hero]:
                item_impact[item]["count"] += 1
                item_impact[item]["heroes"].append(original_hero_names.get(cleaned_hero, hero))
        else:
            print(f"Hero '{hero}' not found in the list.")
    
    sorted_items = sorted(item_impact.items(), key=lambda x: x[1]["count"], reverse=True)
    return sorted_items

def prioritize_items(preferred, counter_items):
    preferred_set = set(preferred)
    prioritized = []
    remaining = []
    
    for item in preferred:
        if item in counter_items:
            prioritized.append((item, counter_items[item]))
    
    for item, details in counter_items.items():
        if item not in preferred_set:
            remaining.append((item, details))
    
    return prioritized, remaining