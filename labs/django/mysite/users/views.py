from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from blog.models import Post
import django.contrib.auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.


def logout_user(request):
    logout(request)
    return redirect('blog:post_list')



def register(request):
    # return HttpResponse('ok')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            image = request.Files.get('image', None)
            user = User.objects.get(username=username)
            messages.success(request, f'Account created for {username}!')
            django.contrib.auth.login(request, user, image)
        return redirect('blog:post_list')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect('blog:post_list')
        else:
            messages.info(request, 'Invalid username or password')
    return render(request, 'users/login.html', {})

def profile_page(request):
    posts = Post.objects.filter(author = request.user)
    return render(request, 'blog/profile_page.html',{'posts': posts})