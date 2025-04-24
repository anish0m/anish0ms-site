from django.shortcuts import render
from django.views.generic import ListView

from .models import Contents

# Create your views here.


class StartingPageView(ListView):
    template_name = "anish0m/index.html"
    model = Contents
    # ordering = ["-date"]
    context_object_name = "contents"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
