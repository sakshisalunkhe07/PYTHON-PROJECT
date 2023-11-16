from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")
def course(request): 
    return redirect("https://www.cdac.in/index.aspx?id=ActsCourses")
def login(request): 
    return redirect("https://cdac.in/candidatelogin")
def contact(request): 
    return redirect("https://cdac.in/index.aspx?id=contact")
