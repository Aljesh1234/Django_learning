from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['services'] = Services.objects.all()
    views['Feedbacks'] = Feedback.objects.all()
    return render(request,'index.html',views)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request,'contact.html')
def portfolio(request):
    return render(request,'portfolio.html')
def price(request):
    return render(request,'price.html')
def services(request):
    views = {}
    views['new_service'] = Services.objects.all()

    return render(request,'services.html',views)