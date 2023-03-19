from django.urls import path

from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("<int:id>",views.index, name="index"),
    path("cart",views.cart,name="cart"),
]