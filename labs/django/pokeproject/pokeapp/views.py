from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, Http404, HttpResponse
from .models import Pokemon
# Create your views here.


def load_pokemon(request):
    # return HttpResponse('ok')
    pokemon_all = Pokemon.objects.all()
    return render(request, 'pokeapp/index.html', {'pokemon_all': pokemon_all})