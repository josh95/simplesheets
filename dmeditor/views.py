from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {"purpose":"Used by the DM to input info about artifacts and allies the players will encounter"}
    return render(request, "dmeditor_main.html", context)
