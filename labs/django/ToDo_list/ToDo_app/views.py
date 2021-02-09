from django.shortcuts import render
from django.http import HttpResponse
from .models import Priority, ToDoItem
from datetime import datetime
# Create your views here.

dummy_items = ['dummy item 1','dummy item 2','dummy item 3','dummy item 4',]


def index(request):
    items = ToDoItem.objects.order_by('created_date')
    context = {
        'items': items
    }
    return render(request, 'ToDo_app/index.html', context)

def save_todo_item(request):
    print(request.POST)
    priority = request.POST['Priority']
    # 
    text = request.POST['text']
    created_date = datetime
    to_do_item = ToDoItem(text = text, created_date = created_date)
    to_do_item.save()


    return HttpResponse('ok')