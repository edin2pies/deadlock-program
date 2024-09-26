# recommender/forms.py

from django import forms
from .data import original_hero_names

class HeroForm(forms.Form):
    player_hero = forms.ChoiceField(
        choices=[('', 'Select Your Hero')] + [(hero, hero) for hero in sorted(original_hero_names.values())],
        required=True,
        label="Your Hero"
    )
    enemy_heroes = forms.MultipleChoiceField(
        choices=[(hero, hero) for hero in sorted(original_hero_names.values())],
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Enemy Team Heroes"
    )