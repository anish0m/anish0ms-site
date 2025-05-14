from django.shortcuts import render
from django.views import View
from .models import Project

class PortfolioView(View):
    template_name = "portfolio/index.html"

    def get(self, request):
        projects = Project.objects.all().prefetch_related("technologies")
        return render(request, self.template_name, {
            "projects": projects
        })
