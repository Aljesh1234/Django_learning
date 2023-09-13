from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['services'] = Services.objects.all()
    views['Feedbackitems'] = Feedback.objects.all()
    return render(request,'index.html',views)

def about(request):
    views = {}
    views['skills'] = Skills.objects.all()
    return render(request, 'about.html',views)


# def contact(request):
#     views = {}
#     views ['viewing_contact'] =

def contact(request):
    views = {}
    views['viewing_contact'] = SiteInfo.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        views['message'] = "The form is submitted"
        return render(request,'contact.html',views)
    return render(request,'contact.html',views)

# def contact(request):
#     views = {}
#     views['contact_page'] = SiteInfo.objects.all()
#     return render(request,'contact.html',views)



def portfolio(request):
    return render(request,'portfolio.html',)

# def price(request):
#     return render(request,'price.html')

def services(request):
    views = {}
    views['new_service'] = Services.objects.all()
    return render(request,'services.html',views)

def price(request):
    views = {}
    views['PriceOf_Items'] = Price.objects.all()
    return render(request,'price.html',views)

