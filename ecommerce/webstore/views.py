from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'webstore/index.html')
def details(request):
    return render(request,'webstore/details.html')
def contact(request):
    return render(request,'webstore/contact.html')