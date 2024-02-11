from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User, Group

def home_redirect(request):
    return redirect("main:home")

def home(request):
    get_users = User.objects.exclude(
        is_superuser=True
    )
    # Get all user which not superuser
    users = {}
    for user in get_users:
        users[user.username] = user.groups.all()[0]
    # Take all user's username and role
    context = {
        "title":"Home",
        "users":users,
    }
    return render(
        request,
        "main/home.html",
        context
    )

def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            default_group = Group.objects.get(name="CommonUser")
            user.groups.add(default_group)
            # Put CommonUser role for new user
            return redirect("main:home")
    else:
        form = UserForm()

    context = {
        "title":"Create",
        "forms":form
    }
    return render(
        request,
        "main/create.html",
        context
    )

def management(request):
    get_users = User.objects.all()
    # Get all users data
    if request.method == "POST":
        selected_users = request.POST.getlist("targets[]")
        # Get all selected users from input forms in management.html
        selected_role = request.POST["role"]
        # Get selected role from input forms in management.html
        selected_role = Group.objects.get(
            name=selected_role
        )
        # Get group which named selected role
        for user_id in selected_users:
            user = User.objects.get(id=user_id)
            user.groups.clear()
            # Clear user's role
            user.groups.add(selected_role)
            # Add new role for the user
            if str(selected_role) == "Staff":
                user.is_staff = True
                # Add staff status to user
            else:
                user.is_staff = False
        user.save()
        return redirect("main:home")
        
    context = {
        "title":"Management",
        "users":get_users
    }
    return render(
        request,
        "main/management.html",
        context
    )