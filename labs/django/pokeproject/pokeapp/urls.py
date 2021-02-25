from django.urls import path
from . import views


app_name = 'pokeapp'
urlpatterns = [
    path('', views.load_pokemon, name='load_pokemon')
]
