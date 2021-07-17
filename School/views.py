from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'dashboard.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

def contactUs(request):
    return render(request,'contactUs.html')

def policy(request):
    return render(request,'policy.html')
