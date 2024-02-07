from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "main/",
        include("main.urls", namespace="main")
    ),
    path(
        "authentication/",
        include("authentication.urls", namespace="authentication")
    ),
    path("", views.login_redirected),
    path('admin/', admin.site.urls),
]
