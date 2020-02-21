from django.urls import path
from books_shelf.views import books_list, authors_list, filter_by_author

urlpatterns = [
    path('books/', books_list, name='books'),
    path('authors/', authors_list, name='authors'),
    path('filterbyauthor/<int:pk>', filter_by_author, name='filter_by_author')
]