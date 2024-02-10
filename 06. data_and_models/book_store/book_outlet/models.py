from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# We need to create migrations and then migrate them
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    author = models.CharField(max_length=100, null = True)
    is_bestselling = models.BooleanField(default = False)


    def get_book_url(self):
        redirect_path = reverse('rated_book', args = [self.rating])
        return redirect_path

    def __str__(self):
        return f"{self.title}({self.rating})"
