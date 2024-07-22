from django.urls import path, include
from recomend import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.doLogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path("song/<int:id>/", views.song),
    path('search_suggestions/', views.search_suggestions)
]