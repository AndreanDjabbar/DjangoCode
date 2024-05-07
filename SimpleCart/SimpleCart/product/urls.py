from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path(
        "checkout",
        views.checkout,
        name="checkout"
    ),
    path(
        "cart/add",
        views.cart_add,
        name="cart_add"
    ),
    path(
        "cart/update",
        views.cart_update,
        name="cart_update"
    ),
    path(
        "cart/delete",
        views.cart_delete,
        name="cart_delete"
    ),
    path(
        "detail/<int:product_id>",
        views.product_detail,
        name="detail"
    ),
    path(
        "home/",
        views.home,
        name="home"
    ),
    path(
        "cart/",
        views.cart,
        name="cart"
    ),
    path(
        "",
        views.product_root_handler
    )
]