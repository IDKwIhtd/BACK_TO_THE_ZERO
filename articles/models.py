from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Custom User Model을 참조
        on_delete=models.SET_NULL,  # 작성자가 삭제되면 author_id가 NULL로 설정됨
        related_name="articles",  # User 입장에서 Article에 접근할 때 사용할 이름
        null=True,  # author_id 필드가 NULL 값을 허용하도록 설정
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # Custom User Model을 참조
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
