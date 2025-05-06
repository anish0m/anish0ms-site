from django.shortcuts import render
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