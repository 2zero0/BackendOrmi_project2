from django import forms
from .models import Post, Comment

# 게시글
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
        fields = ["title", "category","content", "image"]
        
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title"}),
            "content": forms.Textarea(attrs={"placeholder": "Enter the content"}),
        }


# 댓글
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": "3", "cols": "35"})}