# recommender/views.py

from django.shortcuts import render
from .data import hero_counters, preferred_items, original_hero_names, get_counter_items_ordered, prioritize_items, hero_stats_growth
from .forms import HeroForm
import re

def home(request):
    return render(request, 'recommender/home.html')

def hero_stats(request):
    hero_stats_data = hero_stats_growth  # Ensure this is correctly imported from data.py
    selected_hero = request.GET.get('hero', 'abrams')  # Default to 'abrams' if no hero selected
    selected_level = int(request.GET.get('level', 1))  # Default to level 1 if no level selected

    # Calculate stats based on selected hero and level
    if selected_hero in hero_stats_data:
        base_health = hero_stats_data[selected_hero]['base_health']
        health_growth = hero_stats_data[selected_hero]['health_growth']
        base_damage = hero_stats_data[selected_hero]['base_damage']
        damage_growth = hero_stats_data[selected_hero]['damage_growth']
        base_light = hero_stats_data[selected_hero]['base_light']
        light_growth = hero_stats_data[selected_hero]['light_growth']
        base_heavy = hero_stats_data[selected_hero]['base_heavy']
        heavy_growth = hero_stats_data[selected_hero]['heavy_growth']

        # Calculate current stats
        current_health = base_health + (health_growth * (selected_level - 1))
        current_damage = base_damage + (damage_growth * (selected_level - 1))
        current_light = base_light + (light_growth * (selected_level - 1))
        current_heavy = base_heavy + (heavy_growth * (selected_level -1))

        # Create a dictionary for template rendering
        hero_stats = {
            'name': selected_hero,
            'base_health': base_health,
            'current_health': current_health,
            'base_damage': base_damage,
            'current_damage': current_damage,
            'base_light': base_light,
            'current_light': current_light,
            'base_heavy': base_heavy,
            'current_heavy': current_heavy,
            'level': selected_level
        }
    else:
        hero_stats = {}

    # Create a list of levels from 1 to 10
    levels = list(range(1, 15))  # This creates a list of levels [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, 'recommender/hero_stats.html', {
        'hero_stats': hero_stats,
        'hero_names': hero_stats_data.keys(),  # Pass available hero names
        'selected_hero': selected_hero,
        'selected_level': selected_level,
        'levels': levels  # Pass the levels list to the template
    })

def item_recommender(request):
    error_message = None
    player_hero = None
    preferred_sorted = []
    remaining_sorted = []

    if request.method == 'POST':
        player_hero = request.POST.get('player_hero')
        enemy_heroes = request.POST.getlist('enemy_heroes')
        print("Player Hero:", player_hero)
        print("Enemy Heroes:", enemy_heroes)

        if not player_hero:
            error_message = "Please select your hero."
        elif not enemy_heroes:
            error_message = "Please select at least one enemy hero."
        else:
            # Clean and process player hero
            cleaned_player_hero = re.sub(r'[^a-zA-Z]', '', player_hero).lower()
            player_preferred = preferred_items.get(cleaned_player_hero, [])

            # Get counter items
            counter_items_sorted = get_counter_items_ordered(enemy_heroes)
            counter_items_dict = {item: details for item, details in counter_items_sorted}

            # Prioritize items
            preferred_sorted, remaining_sorted = prioritize_items(player_preferred, counter_items_dict)

            # Render results.html with the recommended items
            return render(request, 'recommender/results.html', {
                'player_hero': player_hero,
                'preferred_sorted': preferred_sorted,
                'remaining_sorted': remaining_sorted
            })

    return render(request, 'recommender/item_recommender.html', {
        'heroes': sorted(original_hero_names.values()),
        'error': error_message,
        'player_hero': player_hero,
        'preferred_sorted': preferred_sorted,
        'remaining_sorted': remaining_sorted,
    })