from django.contrib import admin
from .models import Pokemon
from .models import Trainer
# Register your models here.
@admin.register(Pokemon, Trainer)
class PokemonAdmin(admin.ModelAdmin):
    pass

