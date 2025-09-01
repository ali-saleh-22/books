from django.urls import path
from appbooks.views import *

urlpatterns = [
    path("", index, name="appbooks.index"),
    path("all-books/", all_books, name="appbooks.all_books"),
    path("show/book-<str:slug>/", show_book, name="appbooks.show_book"),
    path(
        "category/<str:slug>/", all_category_books, name="appbooks.all_category_books"
    ),
    path("booK/search/", search, name="search"),
    path("book/<str:slug>/view/", view_pdf, name="view_pdf"),
    # path("download/<int:id>/", download_book, name="download_book"),
]
