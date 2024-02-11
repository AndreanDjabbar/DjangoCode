from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path(
        "management/",
        views.management,
        name="management"
    ),
    path(
        "create/",
        views.create,
        name="create"
    ),
    path(
        "home/",
        views.home,
        name="home"
    ),
    path(
        "",
        views.home_redirect
    ),
]