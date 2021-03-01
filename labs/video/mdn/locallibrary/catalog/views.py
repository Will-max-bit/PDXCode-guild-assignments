from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_availble':num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', content_type=context)