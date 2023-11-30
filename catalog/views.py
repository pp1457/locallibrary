from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request) :
    num_books = Book.objects.all().count()

    num_books_haha = Book.objects.all().filter(title='haha').count()

    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()


    context = {
            'num_books': num_books, 
            'num_books_haha': num_books_haha, 
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author
