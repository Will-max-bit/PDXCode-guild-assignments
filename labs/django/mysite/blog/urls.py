from django.urls import path
from . import views
from .views import BlogPostLike

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new',),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/delete', views.post_delete, name='post_delete'),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name='blogpost_like')
    
    
    
]
