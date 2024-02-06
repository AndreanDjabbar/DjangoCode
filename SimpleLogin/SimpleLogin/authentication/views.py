from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound

def login_page(request):
    context = {
        "title":"Login"
    }

    if request.user.is_authenticated:
        # Checking is user authenticated or not
        return redirect("main:home")
    
    user = LoginForm(request.POST or None)
    # Check request.POST is available or not
    # If available, request.POST will be used
    # If not, None will be used

    if request.method == "POST":
        if user.is_valid():
            # check user is valid or not
            username = user.cleaned_data["username"]
            #  Get username
            password = user.cleaned_data["password"]
            # Get password
            user = authenticate(
                username=username,
                password=password
            )
            #  Checking user is exist or not
            if user is not None:
                login(request, user)
                # Login if user is exist
                return redirect("main:home")
            else:
                error_message = "User Not Found Please Register or Try to Input a Correct Username or Password"
                context["error"] = error_message
                # Return error message if user is not exist

    context["forms"] = user
    return render(
        request,
        "authentication/login.html",
        context
    )

def register_page(request):
    context = {
        "title":"Register"
    }

    if request.user.is_authenticated:
        # Checking is user authenticated or not
        return redirect("main:home")

    user = RegisterForm(request.POST or None)
    # Check request.POST is available or not
    # If available, request.POST will be used
    # If not, None will be used
    if request.method == "POST":
        if user.is_valid():
            # check user is valid or not
            user.save()
            # Save user
            return redirect("authentication:login")
            # redirect to authentication/login-page
    context["forms"] = user
    return render(
        request,
        "authentication/register.html",
        context
    )

@login_required(login_url="authentication:login")
# Make Sure you are is login before access this logout feature
def logout_page(request):
    logout(request)
    # Logout
    return redirect("main:home")
    # Redirect to main/home page