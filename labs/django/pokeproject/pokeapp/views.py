from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, Http404, HttpResponse
from .models import Pokemon
import json
from django.core.paginator import Paginator
from django.views.generic.list import ListView

# Create your views here.

class PokeList(ListView):
    paginate_by = 2
    model = Pokemon




def load_pokemon(request):
    # return HttpResponse('ok')

    pokemon_all = Pokemon.objects.all()
    paginator = Paginator(pokemon_all, 25)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(page_number)
    return render(request, 'pokeapp/index.html', {'pokemon_all': pokemon_all, 'page_obj': page_obj })