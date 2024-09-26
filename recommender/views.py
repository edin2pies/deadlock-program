# recommender/views.py

from django.shortcuts import render
from .data import hero_counters, preferred_items, original_hero_names, get_counter_items_ordered, prioritize_items
from .forms import HeroForm
import re

def home(request):
    return render(request, 'recommender/home.html')

def home(request):
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

    return render(request, 'recommender/home.html', {
        'heroes': sorted(original_hero_names.values()),
        'error': error_message,
        'player_hero': player_hero,
        'preferred_sorted': preferred_sorted,
        'remaining_sorted': remaining_sorted,
    })
