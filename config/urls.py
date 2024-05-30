from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('movie/', movie_list, name='movie_list'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('movie/new/', create_movie, name='create_movie'),
    path('movie/<int:pk>/edit/', update_movie, name='update_movie'),
    path('movie/<int:pk>/delete/', delete_movie, name='delete_movie'),
    path('movie/<str:letter>/', movie_list_by_letter, name='movie_list_by_letter'),
    path("admin/", admin.site.urls),
]
