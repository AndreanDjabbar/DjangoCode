from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_handler(request):
    return redirect("main:home")

urlpatterns = [
    path(
        "main/",
        include("CheckShippingCost.urls", namespace="main")
    ),
    path("", root_handler),
    path('admin/', admin.site.urls),
]
