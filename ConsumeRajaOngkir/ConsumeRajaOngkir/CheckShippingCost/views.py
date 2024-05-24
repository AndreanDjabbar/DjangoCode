from django.shortcuts import render, redirect
from .shippingCost import get_sources, get_services

def main_root_handler(request):
    return redirect("main:home")

def check_province(province_input):
    provinces = get_sources("https://api.rajaongkir.com/starter/province")
    for province in provinces["rajaongkir"]["results"]:
        if province["province"].lower() == province_input.lower():
            return province["province_id"]
    return False

def check_city(city_input, province_input):
    cities = get_sources("https://api.rajaongkir.com/starter/city")
    for city in cities["rajaongkir"]["results"]:
        if city["city_name"].lower() == city_input.lower() and city["province"].lower() == province_input.lower():
            return city["city_id"]
    return False

def check_service(origin_id, destination_id, weight, courier):
    services = get_services("https://api.rajaongkir.com/starter/cost", origin_id, destination_id, weight, courier)
    return services["rajaongkir"]["results"]

def home_page(request):
    origin_province_err = origin_city_err = destination_province_err = destination_city_err = weight_err = ""
    
    if request.method == "POST":
        origin_province = request.POST.get("origin-province")
        origin_city = request.POST.get("origin-city")
        destination_province = request.POST.get("destination-province")
        destination_city = request.POST.get("destination-city")
        weight = request.POST.get("weight")
        courier = request.POST.get("courier")
        courier = courier.lower()

        if not check_province(origin_province):
            origin_province_err = "Origin Province is not found"
        
        origin_id = check_city(origin_city, origin_province)

        if not origin_id:
            origin_city_err = "Origin City is not found"

        if not check_province(destination_province):
            destination_province_err = "Destination is Province not found"
        
        destination_id = check_city(destination_city, destination_province)

        if not destination_id:
            destination_city_err = "Destination is City not found"

        if not weight:
            weight_err = "Weight is required"

        if origin_province_err == "" and origin_city_err == "" and destination_province_err == "" and destination_city_err == "" and weight_err == "":
            services = check_service(origin_id, destination_id, weight, courier)
            detail_services = services[0]["costs"]

            context = {
                "title":"Detail",
                "origin_province":origin_province,
                "origin_city":origin_city,
                "destination_province":destination_province,
                "destination_city":destination_city,
                "name":services[0]["name"],
                "detail_services" : detail_services
            }
            return render(
                request,
                "main/detail.html",
                context
            )

    context = {
        "title":"Home",
        "origin_province_err":origin_province_err,
        "origin_city_err":origin_city_err,
        "destination_province_err":destination_province_err,
        "destination_city_err":destination_city_err
    }

    return render(
        request,
        "main/home.html",
        context
    )