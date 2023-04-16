from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('index/<str:pk>/', views.index, name='index'),
    path('nav/', views.nav, name='nav'),
]