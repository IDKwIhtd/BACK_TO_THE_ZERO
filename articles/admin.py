from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


# admin.site.register(Article)
