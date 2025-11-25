from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer
from pokedex.forms import PokemonForm
from pokedex.forms import TrainerForm
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

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

def ver_entrenadores(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainers})

@login_required
def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html', {'form' : form})

@login_required
def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    
    return render(request, 'trainer_form.html', {'form' : form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    
    return render(request, 'pokemon_form.html', {'form' : form})

@login_required
def edit_trainer(request, trainer_id):
    entrenador = Trainer.objects.get(id = trainer_id)
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=entrenador)
    
    return render(request, 'trainer_form.html', {'form' : form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def delete_trainer(request, trainer_id):
    entrenador = Trainer.objects.get(id = trainer_id)
    entrenador.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = "login_form.html"