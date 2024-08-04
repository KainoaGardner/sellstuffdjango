from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("makeUser", views.makeUser, name="makeUser"),
    path("checkLogin", views.checkLogin, name="checkLogin"),
    path("addItem", views.addItem, name="addItem"),
    path("deleteItem/<id>/", views.deleteItem, name="deleteItem"),
    path("toggleSold/<id>/", views.toggleSold, name="toggleSold"),
]
