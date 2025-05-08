from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page-recipes"),
    path("recipes", views.AllRecipesView.as_view(), name="recipes-page"),
    path("recipes/<slug:slug>", views.SingleRecipeView.as_view(), name="recipe-detail-page"),
]