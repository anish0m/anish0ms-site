from django.shortcuts import render
from django.views import View
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


class SingleBookView(View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)

        context = {
            "book": book,
            "book_tags": book.tags.all(),
            # "comment_form": CommentForm(),
            # "comments": book.comments.all().order_by("-id"),
        }
        return render(request, "bookstore/book-detail.html", context)

    def book(self, request, slug):
        # comment_form = CommentForm(request.book)
        book = Book.objects.get(slug=slug)

        # if comment_form.is_valid():
        #     comment = comment_form.save(commit=False)
        #     comment.book = book
        #     comment.save()

        #     return HttpResponseRedirect(reverse("book-detail-page", args=[slug]))

        context = {
            "book": book,
            "book_tags": book.tags.all(),
            # "comment_form": comment_form,
            # "comments": book.comments.all(),
        }

        return render(request, "bookstore/book-detail.html", context)