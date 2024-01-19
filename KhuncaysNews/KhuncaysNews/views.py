from django.shortcuts import redirect

def start(request):
    return redirect("news:home")