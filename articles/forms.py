from django import forms
from django.db import models
from .models import Comment
from articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ("author",)
        # exclude ["title"]

    # 앞은 데이터베이스에 저장될 값, 뒤는 사용자에게 보여질 값
    # GENRE_CHOICES = [
    #     ("technoloty", "Technology"),
    #     ("life", "Life"),
    #     ("hobby", "Hobby"),
    # ]

    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)
    # genre = forms.ChoiceField(choices=GENRE_CHOICES)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article", "author")
