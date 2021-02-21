from django.shortcuts import render, redirect
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
        'urls': urls,
        
    }
    return render(request, 'urlApp/index.html', context)

def delete_URL(request, save_url_id):
    completed_url = ShortenedURL.objects.get(id=save_url_id)
    completed_url.delete()

    return HttpResponseRedirect(reverse('urlApp:index'))

def save_url(request):
    long_url = request.POST['long_url']
    url_code = random_string_creator()
    code = url_code
    shortened_url = ShortenedURL(url = long_url, code = code)
    shortened_url.save()

    return HttpResponseRedirect(reverse('urlApp:index'))




def site_redirect(request, code):
    print(code)
    shortened_url = ShortenedURL.objects.get(code=code)
    shortened_url.counter += 1
    print(shortened_url)
    shortened_url.save()
    return redirect(shortened_url.url)
   

     
    