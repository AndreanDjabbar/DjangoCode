from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "authentication/",
        include("authentication.urls", namespace="authentication")
    ),
    path(
        "main/",
        include("main.urls", namespace="main")
    ),
    path("", views.login_redirected),
    path('admin/', admin.site.urls),
]
