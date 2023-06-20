from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):

    # Extrae los registros usando objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Libros disponibles (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Crea y retorna una página HTML
    return render(request, 'index.html', context=context)