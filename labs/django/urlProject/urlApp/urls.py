from django.urls import path
from . import views


app_name = 'urlApp'
urlpatterns = [
    path('save_url', views.save_url, name='save_url'),
    path('<str:code>/', views.site_redirect, name='redirect'),
    path('delete/<int:save_url_id>/', views.delete_URL, name='delete_url'),
    path('', views.index, name='index'),
]
