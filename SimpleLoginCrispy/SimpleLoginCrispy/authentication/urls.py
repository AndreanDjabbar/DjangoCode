from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path(
        "logout-page",
        views.logout_page,
        name="logout"
    ),
    path(
        "Register-page/",
        views.register_page,
        name="register"
    ),
    path(
        "login-page/",
        views.login_page,
        name="login"
    )
]