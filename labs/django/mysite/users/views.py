from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from blog.models import Post
from .models import UserProfile
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
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # create a user from the submitted form data
            user = form.save()
            # getting the image that was chosen by the user
            # profile_picture = request.FILES.get('image')
            profile_picture = form.cleaned_data['image']
            # creating a user profile associated with this user and image
            user_profile = UserProfile(user=user, profile_picture=profile_picture)
            user_profile.save()

            messages.success(request, f'Account created for {user.username}!')
            django.contrib.auth.login(request, user)
            return redirect('blog:post_list')
        else:
            return render(request, 'users/register.html', {'form': form})
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
    posts = Post.objects.filter(author = request.user).order_by('-published_date')
    return render(request, 'blog/profile_page.html',{'posts': posts})