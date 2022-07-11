from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.login_view, name="Login"),
    path("login",views.authenticates,name="authenticates"),
    path("profile",views.profile,name="profile"),
    
    path("register",views.createUser,name="createuser"),
    path("logout", views.logout_view, name="logout")
]
