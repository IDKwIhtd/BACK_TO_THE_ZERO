from django.urls import path
from django.urls.conf import include
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.articles, name="articles"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    # path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/update/", views.update, name="update"),
    # path('new/', views.new, name = "new"),
    path("<int:pk>/delete_image/", views.delete_image, name="delete_image"),
    path("create/", views.create, name="create"),
    path("hello/", views.hello, name="hello"),
    path("data-throw/", views.data_throw, name="throw"),
    path("data-catch/", views.data_catch, name="catch"),
    path("index2/", views.index2, name="index2"),
    path("<int:pk>/comment_create/", views.comment_create, name="comment_create"),
    path("comment/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
]
