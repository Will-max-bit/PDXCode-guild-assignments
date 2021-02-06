from django.urls import path
from . import views

app_name = 'contactapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    # localhost:8000/contactapp/detail/5/
    path('detail/<int:contact_id>/', views.detail, name='detail'),
]