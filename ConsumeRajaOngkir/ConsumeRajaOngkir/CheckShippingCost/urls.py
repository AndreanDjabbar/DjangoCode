from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path(
        "home/",
        views.home_page,
        name="home"
    ),
    path(
        "",
        views.main_root_handler
    )
]