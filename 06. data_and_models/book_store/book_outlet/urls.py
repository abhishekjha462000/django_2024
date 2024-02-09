from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.index, name = 'all_books'),
    path('books/<int:rating>', views.get_book_by_rating, name = 'rated_book'),
    path('books/delete/<int:rating>', views.delete_book_by_rating)
]
