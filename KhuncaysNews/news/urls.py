from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path(
        "post/<slug:slug_name>",
        views.post,
        name="post"
    ),
    path(
        "category/<str:category>",
        views.category_post,
        name="category"
    ),
    path(
        "delete/<int:delete_id>",
        views.delete,
        name="delete"
    ),
    path(
        "update/<int:update_id>",
        views.update,
        name="update"
    ),
    path(
        "add",
        views.add,
        name="add"
    ),
    path(
        "profile",
        views.profile,
        name="profile"
    ),
    path(
        "",
        views.home,
        name="home"
    )
]