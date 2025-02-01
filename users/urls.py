from django.urls import path
from django.urls import include
from . import views

app_name="users"
urlpatterns =[
    path('', views.users, name="users"),
    path('profile/<str:username>/', views.profile, name="profile"),
    path('hello/', views.hello, name="hello")
]