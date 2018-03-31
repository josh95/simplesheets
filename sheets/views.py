from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    player = request.GET.get('player')
    player_id = request.GET.get('player_id')
    #find all sheets 
    character_sheets= [{"name": "Majik Markees", "image": "http://mgewiki.com/images/thumb/4/4f/Grizzly_0.jpg/300px-Grizzly_0.jpg", "description": ""},
                    {"name": "Jack the Lumberjack", "image": "url", "description": ""}]
    context["sheets"] = character_sheets
    return render(request, "sheets_main.html", context)

def sheetEditor(request):
    context = {}

    return render(request, "charsheet.html", context)
