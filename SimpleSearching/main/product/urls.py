from django.urls import path
from .views import *

app_name = "product"

urlpatterns = [
    path(
        "home/",
        home,
        name="home"
    ),
    path(
        "create/",
        create,
        name="create"
    ),
]