from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "blog/",
        include("blog.urls", namespace="blog")
    ),
    path("", views.blog_redirect),
    path('admin/', admin.site.urls),
]
