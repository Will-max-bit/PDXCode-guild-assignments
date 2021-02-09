from django.urls import path
from . import views

app_name = 'ToDo_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('Save_todo/', views.save_todo_item, name='save_todo_item' )
]
