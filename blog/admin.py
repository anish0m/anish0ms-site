from django import forms
from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "tags": forms.CheckboxSelectMultiple()
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "post",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)