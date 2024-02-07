from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="authentication:login")
def home(request):
    context = {
        "title":"Home"
    }
    return render(
        request,
        "main/home.html",
        context
    )