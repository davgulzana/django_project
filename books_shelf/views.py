from django.shortcuts import render
from books_shelf.models import Book, Author


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_shelf/books_list.html', {
            'books': books
        }
    )

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'books_shelf/authors_list.html', {
            'authors': authors
        }
    )

def filter_by_author(request, pk):
    book = Book.objects.get(pk=pk)
    # filtered_author = Author.objects.filter(id=book.author)
    authors_books = Book.objects.filter(author=book.author)
    return render(request, 'books_shelf/filtered_books.html', {'filtered_books': authors_books})