from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Recipe

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
        }
        return render(request, "recipes/recipe-detail.html", context)

    def post(self, request, slug):
        recipe = Recipe.objects.get(slug=slug)

        context = {
            "recipe": recipe,
            "search_filters": recipe.search_filter.all(),
        }

        return render(request, "recipes/recipe-detail.html", context)