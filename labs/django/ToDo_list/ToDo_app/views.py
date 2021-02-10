from django.shortcuts import render
from django.http import HttpResponse
from .models import Priority, ToDoItem
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.




def index(request):
    items = ToDoItem.objects.filter(completed=False).order_by('created_date')
    priorities = Priority.objects.all()
    completed_todos = ToDoItem.objects.filter(completed=True).order_by('created_date')
    # print(completed_todos)
    context = {
        'items': items,
        'priorities': priorities,
        'completed_todos': completed_todos,
    }
    return render(request, 'ToDo_app/index.html', context)

def save_todo_item(request):
    print(request.POST)
    priority_id = request.POST['priority_id']
    priorities = Priority.objects.get(id=priority_id)
    text = request.POST['text']
    created_date = timezone.now()
    to_do_item = ToDoItem(text = text, created_date = created_date, priority = priorities)
    to_do_item.save()

    return HttpResponseRedirect(reverse('ToDo_app:index'))

def delete_item(request, completed_todo_id):
    items_completed = ToDoItem.objects.get(id=completed_todo_id)
    # print(items_completed)
    items_completed.delete()

    return HttpResponseRedirect(reverse('ToDo_app:index'))



def completed_todo(request, text_id):
    item = ToDoItem.objects.get(id=text_id)
    item.completed = True
    item.save()
    # print(item)
    return HttpResponseRedirect(reverse('ToDo_app:index'))


def delete_all(request):
    # completed_items = completed_todo(request, text_id)
    completed_todos = ToDoItem.objects.filter(completed=True)
    completed_todos.delete()
    print(completed_todos)
    print('this is a marker')
    return HttpResponseRedirect(reverse('ToDo_app:index'))