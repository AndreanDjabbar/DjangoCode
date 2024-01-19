from django.shortcuts import render, redirect
from .models import NewsModel
from .forms import NewsForm

def home(request):
    models = NewsModel.objects.all()
    categories = NewsModel.objects.values("category").distinct()
    format = {
        "title":"Home",
        "all_data":models,
        "categories":categories
    }
    return render(request, "news/home.html", format)

def add(request):
    forms = NewsForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return redirect("news:home")
    format = {
        "title":"Add News",
        "forms":forms
    }
    return render(request, "news/add.html", format)

def post(request, slug_name):
    get_data = NewsModel.objects.get(slug__iexact=slug_name)
    format = {
        "title":slug_name,
        "data":get_data
    }
    return render(request, "news/post.html", format)

def update(request, update_id):
    data_target = NewsModel.objects.get(id=update_id)
    current_data = data_target.__dict__
    forms = NewsForm(
        request.POST or None,
        initial=current_data,
        instance=data_target
    )
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return redirect("news:home")
    format = {
        "title":"Update News",
        "forms":forms,
        "data":data_target
    }
    return render(request, "news/update.html", format)

def delete(request, delete_id):
    data_target = NewsModel.objects.get(id=delete_id).delete()
    return redirect("news:home")

def category_post(request, category):
    data_filtered = NewsModel.objects.filter(category__iexact=category)
    format = {
        "title":category,
        "all_data":data_filtered
    }
    return render(request, "news/category_post.html", format)

def profile(request):
    return render(request, "news/profile.html")