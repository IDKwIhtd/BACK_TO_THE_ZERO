from django.urls import path
from django.urls import include
from . import views

urlpatterns =[
 path('', views.users, name="users"),
    path('profile/<str:username>/', views.profile, name="profile"),
]