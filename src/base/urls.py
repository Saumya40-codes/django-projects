from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('index/<str:pk>/', views.index, name='index'),
    path('nav/', views.nav, name='nav'),
    path('createRoom/', views.createRoom, name='createRoom'),
    path('loginUser/',views.userLogin, name='userLogin'),
    path('signup/', views.signUp, name = 'signUp'),
    path('updateRoom/<str:pk>',views.updateRoom, name = 'update'),
    path('deleteRoom/<str:pk>',views.delete,name='delete')
]