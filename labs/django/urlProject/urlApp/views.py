from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import ShortenedURL
from django.urls import reverse
import random
import string


def random_string_creator():
    chars = list(string.ascii_letters + string.digits)
    y = 0
    x = 6
    out_lst = []
    while y < x:
        out_lst.append(random.choice(chars))
        y +=1
    url_code = "".join(out_lst)
    return url_code


# Create your views here.
def index(request):
    urls = ShortenedURL.objects.all()
    context = {
        'message': 'URL App!!!!',
        'urls': urls,
    }
    return render(request, 'urlApp/index.html', context)

def shortener(request):
    pass

def save_url(request):
    long_url = request.POST['long_url']
    url_code = random_string_creator()
    code = url_code
    shortened_url = ShortenedURL(url = long_url, code = code)
    shortened_url.save()

    return HttpResponseRedirect(reverse('urlApp:index'))

def counting(request):
    pass


def redirect(request, code):
    code = ShortenedURL.objects.get(code=code)
    url = str(code)
    # counter += 1
    # print(counter)
    return HttpResponseRedirect(url)

     
    