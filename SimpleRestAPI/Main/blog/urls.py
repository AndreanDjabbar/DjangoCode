from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path(
        "django-api-home/<int:data_id>/",
        views.json_detail,
        name="json_detail"
    ),
    path(
        "json-api-home/",
        views.json_api_home,
        name="json_api_home"
    ),
    path(
        "django-api-home/",
        views.django_api_home,
        name="django_api_home"
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
        views.blog_redirect
    )
]