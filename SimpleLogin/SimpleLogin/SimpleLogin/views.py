from django.shortcuts import redirect

def login_redirected(request):
    return redirect("authentication:login")