from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('index/<str:pk>/', views.index, name='index'),
    path('nav/', views.nav, name='nav'),
    path('createRoom/', views.createRoom, name='createRoom'),
    path('signup/', views.signUp, name = 'signUp'),
    path('updateRoom/<str:pk>',views.updateRoom, name = 'update'),
    path('deleteRoom/<str:pk>',views.delete,name='delete'),
    path('test/',views.testIt,name='test'),
    path('update_test/', views.test_update, name= 'testUpdate'),
    path('topic_new/', views.createTopic,name='topic_new'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logoutUser'),
]