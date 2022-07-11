from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("addbook", views.addbook, name="addbook"),
     path("addtocart", views.addtocart, name="addtocart"),
     path("deleteelement", views.deleteelement, name="deleteelement"),
     path("cart", views.cart, name="cart"),
     path("bookadd", views.bookadd, name="bookadd"),
     path("search", views.searchbook, name="searchbook"),
 ]