from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def register(request):
    # return HttpResponse('ok')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('blog:post_list')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})