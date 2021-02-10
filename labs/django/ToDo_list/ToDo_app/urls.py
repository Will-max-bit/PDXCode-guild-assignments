from django.urls import path
from . import views

app_name = 'ToDo_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('save_todo_item/', views.save_todo_item, name='save_todo_item' ),
    path('completed_todo/<int:text_id>', views.completed_todo, name='completed_todo'),
    path('delete_item/<int:completed_todo_id>', views.delete_item, name='delete_item')
]
