from django.shortcuts import render, redirect
from .forms import DataForm
from django.http import JsonResponse
from .models import DataModel
from .serializers import DataSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

def blog_redirect(request):
    return redirect("blog:home")

def home(request):
    context = {
        "title":"Home"
    }
    return render(
        request,
        "blog/home.html",
        context
    )

def create(request):
    if request.method == "POST":
        get_forms = DataForm(request.POST)
        if get_forms.is_valid():
            get_forms.save()
            return redirect("blog:home")
    else:
        get_forms = DataForm()

    context = {
        "title":"Create",
        "forms":get_forms
    }
    return render(
        request,
        "blog/create.html",
        context
    )

@api_view(["GET", "POST"])
def django_api_home(request):
    context = {}
    if request.method == "GET":
        get_all_data = DataModel.objects.all()
        serializer = DataSerializer(
            get_all_data,
            many=True
        )
        data_json = {
            "items":serializer.data
        } 
        return Response(data_json)
    
    elif request.method == "POST":
        get_serializer = DataSerializer(
            data=request.data
        )
        if get_serializer.is_valid():
            DataModel.objects.create(
                **get_serializer.validated_data
            )
            return Response(
                get_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                get_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
@api_view(["GET", "PUT", "DELETE"])
def json_detail(request, data_id):
    try:
        get_data = DataModel.objects.get(
            id=data_id
        )
    except:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == "GET":
        serializer = DataSerializer(get_data)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = DataSerializer(
            get_data,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    elif request.method == "DELETE":
        get_data.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(["GET"])
def json_api_home(request):
    context = {}
    if request.method == "GET":
        get_all_data = DataModel.objects.all()
        serializer = DataSerializer(
            get_all_data,
            many=True
        )
        format = {
            "indent":4
        }
        data_json = {
            "items":serializer.data
        }
        return JsonResponse(
            data_json,
            json_dumps_params=format,
            safe=False
        )