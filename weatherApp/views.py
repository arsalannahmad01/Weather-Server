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
    
    api_url = f"https://api.weatherapi.com/v1/current.json?key=a6c3d3462f894fc18bd162511232508&q={location}&aqi=yes"
    try:
        response = requests.get(api_url)
        response_data = response.json()

        print(response_data)
        
        print(response_data["current"]["condition"]["text"])
        return JsonResponse({"weather":response_data["current"]["condition"]["text"], "temprature":response_data["current"]["temp_c"], "humidity":response_data["current"]["humidity"]})
    except Exception as e:
        return JsonResponse({"error": "Error 500"}, status=500)
