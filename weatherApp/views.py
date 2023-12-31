# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, Arsalan. We are here. what are you doing")

import requests
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View

def external_api(request):
    # URL of the external API you want to call

    location = request.GET.get('location')

    if not location:
        return HttpResponseBadRequest("Missing 'location' parameter.")
    
    api_url = f"https://api.weatherapi.com/v1/current.json?key=a6c3d3462f894fc18bd162511232508&q={location}&aqi=no"
    try:
        response = requests.get(api_url)
        response_data = response.json()

        return JsonResponse({"icon":response_data["current"]["condition"]["icon"], "weather":response_data["current"]["condition"]["text"], "temprature":response_data["current"]["temp_c"], "feelslike": response_data["current"]["feelslike_c"], "humidity":response_data["current"]["humidity"], "city":response_data["location"]["name"], "country":response_data["location"]["country"]})
    except Exception as e:
        return JsonResponse({"error": response_data["error"]["message"]}, status=500)
