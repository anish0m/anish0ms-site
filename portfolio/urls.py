from django.urls import path
from . import views

urlpatterns = [
    path("", name="portfolio"),# views.StartingPageView.as_view(), 
]