from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["recipe"]
        labels = {
            "user_name": "Your Name",
            "rating": "Your Email",
            "text": "Your Comment"
        }
