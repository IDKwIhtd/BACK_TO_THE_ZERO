from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class User(AbstractUser):
#     pass  # 기본 User 모델을 변경하지 않더라도 확장성을 높일 수 있음


class User(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # 기본 'user_set' 이름 대신 변경
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",  # 기본 'user_permissions' 이름 대신 변경
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
