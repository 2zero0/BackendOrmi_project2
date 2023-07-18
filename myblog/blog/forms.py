from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category","content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title"}),
            "content": forms.Textarea(attrs={"placeholder": "Enter the content"}),
        }