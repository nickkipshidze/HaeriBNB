from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.SignupUser.as_view(), name="signup"),
    path("login", views.LoginUser.as_view(), name="login"),
    path("profile", views.CurrentUser.as_view(), name="profile")
]