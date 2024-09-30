# recommender/data.py

import re
from collections import defaultdict

# Dictionary of heroes and their counter items
hero_counters = {
    "abrams": ["Decay", "Toxic Bullets", "Healbane"],
    "bebop": ["Debuff Remover", "Ethereal Shift", "Warp Stone", "Reactive Barrier"],
    "dynamo": ["Reactive Barrier", "Rescue Beam", "Soul Rebirth"],
    "greytalon": ["Debuff Remover", "Ethereal Shift", "Knockdown"],
    "haze": ["Warp Stone", "Return Fire", "Metal Skin"],
    "infernus": ["Debuff Reducer", "Debuff Remover", "Slowing Hex"],
    "ivy": ["Super Stamina", "Warp Stone", "Silence Glyph"],
    "kelvin": ["Super Stamina", "Ethereal Shift"],
    "ladygeist": ["Silencer", "Silence Glyph"],
    "lash": ["Slowing Hex", "Silence Glyph", "Ethereal Shift"],
    "mcginnis": ["Superior Stamina", "Monster Rounds"],
    "mokrill": ["Reactive Barrier", "Slowing Hex", "Silence Glyph"],
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
    "greytalon": ["Superior Stamina"],
    "haze": ["Silencer"],
    "infernus": ["Toxic Bullets", "Ethereal Shift"],
    "ivy": ["Monster Rounds", "Rescue Beam"],
    "kelvin": [],
    "ladygeist": ["Healbane", "Warp Stone"],
    "lash": ["Superior Stamina", "Monster Rounds"],
    "mcginnis": ["Superior Stamina", "Echo Shard"],
    "mokrill": ["Fleetfoot"],
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
    "greytalon": "Grey Talon",
    "haze": "Haze",
    "infernus": "Infernus",
    "ivy": "Ivy",
    "kelvin": "Kelvin",
    "ladygeist": "Lady Geist",
    "lash": "Lash",
    "mcginnis": "McGinnis",
    "mokrill": "Mo & Krill",
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

hero_stats_growth = {
    "abrams": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "bebop": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "dynamo": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "grey talon": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "haze": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "infernus": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "ivy": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "kelvin": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "lady geist": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "lash": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "mcGinnis": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "mo & krill": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "paradox": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "pocket": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "seven": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "shiv": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "vindicta": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "viscous": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "warden": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "wraith": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    "yamato": {"base_health": 600, "health_growth": 32, "base_damage": 20, "damage_growth": 2, "base_light": 63, "light_growth": 3.4, "base_heavy": 116, "heavy_growth": 3.4},
    # Add other heroes with their respective growth values
}