from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    YOUR_CHOICES = [
    ("국내여행", "국내여행"),
    ("해외여행", "해외여행"),
    ("먹방여행", "먹방여행"),
    ("자연여행", "자연여행"),
    ("액티비티", "액티비티"),
    ]
    category = forms.ChoiceField(choices=YOUR_CHOICES)

    class Meta:
        model = Post
        fields = ["title", "category","content"]
        
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title"}),
            "content": forms.Textarea(attrs={"placeholder": "Enter the content"}),
        }