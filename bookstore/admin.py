from django import forms
from django.contrib import admin

from .models import SubBook, Book, Author, Tag

# Register your models here.

class SubBookInline(admin.TabularInline):
    model = SubBook
    extra = 1
    fields = ("title", "description")
class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "tags": forms.CheckboxSelectMultiple()
        }
class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [SubBookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Tag)  