from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'rating')
    list_display = ('author', 'is_bestselling', 'title')

admin.site.register(Book, BookAdmin)