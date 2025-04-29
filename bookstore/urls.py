from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page-bookstore"),
    path("books", views.AllBooksView.as_view(), name="books-page"),
    path("books/<slug:slug>", views.SingleBookView.as_view(), name="book-detail-page"),
]