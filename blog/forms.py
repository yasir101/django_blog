from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget = CKEditor5Widget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']