from django.shortcuts import render
from django.views import View

# Create your views here.
class PortfolioView(View):
    template_name = "portfolio/index.html"
    # model = Contents
    # ordering = ["-date"]
    # context_object_name = "contents"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset