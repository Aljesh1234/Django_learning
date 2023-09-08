from django.urls import path
from .views import *




urlpatterns =[
    path("",home),
    path("about/",about),
    path("contact/",contact),
    path("portfolio/",portfolio),
    path("price/",price),
    path("services/",services)
]