from django.urls import path
from . import views

urlpatterns = [
    path("external/", views.external_api, name="external")
]