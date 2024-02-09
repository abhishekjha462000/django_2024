from django.shortcuts import render
from .models import Book
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

initial_books = [
    Book(title = 'Harry Potter 1', rating = 1, author = 'J.K Rowling', is_bestselling = True),
    Book(title = 'Harry Potter 2', rating = 4, author = 'J.K Rowling', is_bestselling = False),
    Book(title = 'Harry Potter 3', rating = 5, author = 'J.K Rowling', is_bestselling = True),
    Book(title = 'Harry Potter 4', rating = 2, author = 'J.K Rowling', is_bestselling = False),
    Book(title = 'Harry Potter 5', rating = 3, author = 'J.K Rowling', is_bestselling = True),
]

def index(request):
    books_fetched = list(Book.objects.all())

    if len(books_fetched) == 0:
        # This means that we do not have any books in our database at the current moment.
        # we will add all the books in the initial_books array into our database.
        # but first we need to save all the books into our database.
        for book in initial_books:
            book.save() # The save method is used to either save a fresh data into the database or either update an existing data
        
        books_fetched = list(Book.objects.all())
    
    books = [dict(title = book.title, rating = book.rating) for book in books_fetched]

    
    return render(request, 'book_outlet/index.html', {'books':books})

def get_book_by_rating(request, rating):
    if rating not in {1,2,3,4,5}:
        return HttpResponseNotFound('<h1>The rating must be in {1,2,3,4,5}</h1>')
    
    # fetch all the books with rating = rating 
    fetched_book = Book.objects.get(rating = rating)

    book = {
            'title': fetched_book.title,
            'rating' : fetched_book.rating, 
            'best_selling':fetched_book.is_bestselling, 
            'author' : fetched_book.author
            }

    response_data = render_to_string('book_outlet/book_by_rating.html', {'book':book})

    return HttpResponse(response_data)


def delete_book_by_rating(request, rating):

    # first fetch all the books with the given rating
    fetched_books = Book.objects.filter(rating = rating)

    for book in fetched_books:
        book.delete()

    redirected_url = reverse('all_books', args = [])
    return HttpResponseRedirect(redirected_url)