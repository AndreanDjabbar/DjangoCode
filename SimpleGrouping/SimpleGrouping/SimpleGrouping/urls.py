from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "main/",
        include("main.urls", namespace="main")
    ),
    path(
        "",
        views.main_redirect
    ),
    path('admin/', admin.site.urls),
]
