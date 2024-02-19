from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("login/", views.login, name="Login"),
    path("checkout/", views.checkout, name="Checkout")
]
