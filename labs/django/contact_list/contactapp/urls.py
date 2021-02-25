from django.urls import path
from . import views

app_name = 'contactapp'
urlpatterns = [
    path('', views.index, name='index'),
    # localhost:8000/contactapp/detail/5/
    path('detail/<int:contact_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('savecontact/', views.save_contact, name='savecontact')
]