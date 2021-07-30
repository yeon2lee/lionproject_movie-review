from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['post_title','movie_title','author','body','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']