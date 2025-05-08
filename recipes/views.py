from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = "recipes/index.html"
    model = Recipe
    ordering = ["-date"]
    context_object_name = "recipes"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]

        return data


class AllRecipesView(ListView):
    template_name = "recipes/all-recipes.html"
    model = Recipe
    ordering = ["-date"]
    context_object_name = "all_recipes"


class SingleRecipeView(View):
    def get(self, request, slug):
        recipe = Recipe.objects.get(slug=slug)

        context = {
            "recipe": recipe,
            "search_filters": recipe.search_filter.all(),
            "comment_form": CommentForm(),
            "comments": recipe.comments.all().order_by("-id"),
        }
        return render(request, "recipes/recipe-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        recipe = Recipe.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()

            return HttpResponseRedirect(reverse("book-detail-page", args=[slug]))

        context = {
            "recipe": recipe,
            "search_filters": recipe.search_filter.all(),
            "comment_form": comment_form,
            "comments": recipe.comments.all(),
        }

        return render(request, "recipes/recipe-detail.html", context)