from django.contrib import admin
from django import forms
from .models import Project, Technology

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "technologies": forms.CheckboxSelectMultiple()
        }

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ("title", "filter_tag",)
    list_filter = ("filter_tag", "technologies",)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)
