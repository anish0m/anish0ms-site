from django import forms
from django.contrib import admin

from .models import Procedure, Ingredients, Recipe, SearchFilter

# Register your models here.

class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 1
    fields = ("name", "amount")

class ProcedureInline(admin.TabularInline):
    model = Procedure
    extra = 1
    fields = ("step",)
class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {
            "search_filter": forms.CheckboxSelectMultiple()
        }
class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    list_filter = ("search_filter", "date",)
    list_display = ("title", "date",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [IngredientsInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(SearchFilter)  