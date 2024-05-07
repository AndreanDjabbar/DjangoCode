from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductModel
from .cart import Cart
from django.core.paginator import Paginator
from django.http import JsonResponse

def product_root_handler(request):
    return redirect("product:home")

def home(request):
    cart = Cart(request)
    paginator = Paginator(
        ProductModel.objects.filter(product_stock__gt=0),  # Filter products with stock greater than 0
        4
    )
    page = request.GET.get("page")
    get_products = paginator.get_page(page)
    
    context = {
        "title":"Home",
        "products":get_products,
        "products_amount":len(get_products),
    }
    return render(
        request,
        "product/home.html",
        context
    )

def cart(request):
    cart = Cart(request)
    quantities = cart.get_quantities()
    cart_products = cart.get_products()
    # print(cart_products)
    totals = cart.get_totals()
    context = {
        "title":"Cart",
        "cart_products":cart_products,
        "quantities":quantities,
        "totals":totals
    }
    return render(
        request,
        "product/cart.html",
        context
    )

def product_detail(request, product_id):
    get_product = ProductModel.objects.get(id=product_id)
    context = {
        "title":"Product Detail",
        "product":get_product
    }
    return render(
        request,
        "product/detail.html",
        context
    )

def cart_add(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity")) 
        product = get_object_or_404(ProductModel, id=product_id)
        cart.add(product=product, quantity=product_quantity)

        cart_quantity = cart.__len__()

        response = JsonResponse({
            "Product Name":product.product_name,
            "product_id":product.id,
            "quantity":cart_quantity
        })
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        print(product_id)
        product_quantity = int(request.POST.get("product_quantity")) 
        cart.update(product=product_id, quantity=product_quantity)
        response = JsonResponse({"Quantity":product_quantity})
        return response
        # return redirect("product:cart")

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        cart.delete(product=product_id)
        response = JsonResponse({"Product":product_id})
        return response
    
def checkout(request):
    cart = Cart(request)
    cart.checkout()
    return redirect("product:cart")

