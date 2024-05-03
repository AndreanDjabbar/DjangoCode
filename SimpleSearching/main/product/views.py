from django.shortcuts import render, redirect
from .models import ProductModel
from .forms import ProductForm

def home(request):
    get_products = ProductModel.objects.all()
    context = {
        "title":"Home",
        "products":get_products
    }
    
    if request.method == "POST":
        search_key = request.POST.get("search")
        searching_data = ProductModel.objects.filter(product_name__icontains=search_key)
        context["searched"] = search_key
        context["result"] = searching_data

    return render(
        request,
        "product/home.html",
        context
    )

def create(request):
    get_form = ProductForm()

    if request.method == "POST":
        get_form = ProductForm(request.POST)
        if get_form.is_valid():
            get_form.save()
            return redirect("product:home")

    context = {
        "title":"Create",
        "forms":get_form
    }
    return render(
        request,
        "product/create.html",
        context
    )