from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
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

def create(request):
    cities = City.objects.all()
    context = {
        'cities': cities
    }
    return render(request,'contactapp/create.html', context)

def save_contact(request):
    print(request.POST)
    # extract form data into local variables
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    notes = request.POST['notes']
    city_id = request.POST['city_id']
    existing_city = City.objects.get(id=city_id)
    contact = Contact(first_name = first_name, middle_name=middle_name, last_name=last_name, email =email, phone_number = phone_number, notes = notes, city = existing_city  )
    # create instance of model using data
    contact.save()
    #save the model to the database 
    
    #redirect back to index page
    return HttpResponseRedirect(reverse('contactapp:index'))
    # return render(request, 'contactapp/index.html')
    # return HttpResponse(dict(test))