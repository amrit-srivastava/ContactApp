from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView


app_name = "user"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="register"),
    path("", LoginView.as_view(template_name="user/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="user/logout.html"), name="logout"
    ),
]
