from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer

def index(request):
    #pokemones
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    context = {
        'pokemons': pokemons,
        'trainers': trainers,
    }
    return HttpResponse(template.render(context, request))


def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def entrenador(request, trainer_id):
    entrenador = Trainer.objects.get(id = trainer_id)
    template = loader.get_template('display_trainers.html')
    context = {
        'Trainer': entrenador,
    }
    return HttpResponse(template.render(context, request))