from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Avg

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_books": books.count(),
        "avg_rating":books.aggregate(Avg("rating"))
    })

def book_detail(request, slug_url):
    book = get_object_or_404(Book,slug=slug_url)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller":book.is_bestselling
    })
