from django import forms
from .models import Comment

# Form for users to Create Comment Under a Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        # to hide label in form
        labels = {
            'content' : '',
        }