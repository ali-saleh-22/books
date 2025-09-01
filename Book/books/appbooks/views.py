from django.shortcuts import render, get_object_or_404
from appbooks.models import Book, Category
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
import os


# Create your views here.
def index(request):
    recommended_books = Book.objects.all().filter(recommended_books=True)
    ficition_books = Book.objects.all().filter(ficition_books=True)
    business_books = Book.objects.all().filter(business_books=True)

    return render(
        request,
        "appbooks/index.html",
        {
            "recommended_books": recommended_books,
            "ficition_books": ficition_books,
            "business_books": business_books,
        },
    )


def all_books(request):
    books = Book.objects.all()
    return render(request, "appbooks/all_books.html", {"books": books})


@login_required()
def show_book(request, slug):
    book = get_object_or_404(Book, slug=slug)

    book_categories = book.category.all()
    similar_books = (
        Book.objects.all()
        .filter(category__in=book_categories)
        .exclude(id=book.id)
        .distinct()
    )

    return render(
        request,
        "appbooks/show_book.html",
        {"book": book, "similar_books": similar_books},
    )


def all_category_books(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, "appbooks/all_category_books.html", {"category": category})


def search(request):
    book = request.GET.get("book")
    results = Book.objects.all().filter(title__contains=book)
    return render(request, "appbooks/search.html", {"results": results})


def view_pdf(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "appbooks/view_pdf.html", {"book": book})


# def download_book(request, id):
#     book = get_object_or_404(Book, id=id)
#     file_path = book.pdf.path
#     return FileResponse(
#         open(file_path, "rb"), as_attachment=True, filename=os.path.basename(file_path)
#     )
