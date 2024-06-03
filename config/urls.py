from django.contrib import admin
from django.urls import path
from app.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name="home"),
    path('movie/', movie_list, name='movie_list'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('movie/new/', create_movie, name='create_movie'),
    path('movie/<int:pk>/edit/', update_movie, name='update_movie'),
    path('movie/<int:pk>/delete/', delete_movie, name='delete_movie'),
    path('movie/<str:letter>/', movie_list_by_letter, name='movie_list_by_letter'),
    path("admin/", admin.site.urls),

     path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/profile/', profile, name='profile'),
]
