from django.urls import path
from . import views


app_name = 'urlApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_url', views.save_url, name='save_url'),
    path('redirect/<str:code>', views.redirect, name='redirect'),
    path('urlApp:delete_URL', views.delete_URL, name='delete_URL')
]
