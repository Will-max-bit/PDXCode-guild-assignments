from django.shortcuts import render
from django.http import HttpResponse
from .models import Twit
from users.models import User 


def index(request):
    twits = Twit.objects.all()

    return render(request, 'tweeterapp/index.html', {'twits': twits})
