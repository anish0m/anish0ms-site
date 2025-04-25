from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

# Create your views here.


class StartingPageView(ListView):
    template_name = "bookstore/index.html"
    model = Book
    ordering = ["-date"]
    context_object_name = "books"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]

        return data