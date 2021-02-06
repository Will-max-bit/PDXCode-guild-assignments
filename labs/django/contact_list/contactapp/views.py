from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Contact

# Create your views here.

def index(request):
    contact_people = Contact.objects.order_by('last_name') 
    context = {
        'contact_people': contact_people,
    }
    
    return render(request, 'contactapp/index.html', context)

def detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {
        'contact': contact,
    }
    return render(request, 'contactapp/detail.html', context)
    # return HttpResponse("You're looking at contact wtih id " + str(contact_id))

