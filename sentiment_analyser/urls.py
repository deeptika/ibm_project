from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('form/', views.form, name = 'form'),
    path('about/', views.about, name = 'about'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
]