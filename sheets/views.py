from django.shortcuts import render
from django.http import HttpResponse
from dmeditor.models import *
import json

def sheetMain(request):
    context = {}
    player_id = request.POST.get('player_id')
    #find all sheets
    if player_id is None:
        player_id = 0
    request.session['player_id'] = player_id
    player_name = Player.objects.get(player_id = int(player_id)).player_name
        
    character_sheets = []

    for sheet in Sheets.objects.filter(player_id = player_id):
        character_sheets.append({
            "name": sheet.character_name,
            "image" : sheet.img_url,
            "description" : sheet.description})
            
    context["sheets"] = character_sheets
    context["player"] = player_name
    return render(request, "sheets_main.html", context)

def index(request):
    #takes user to login page
    return render(request, "login.html")

def sheetEditor(request):
    context = {}

    return render(request, "charsheet.html", context)

def checkUser(request):
    try:
        player_id = Player.objects.get(player_name = request.POST['user']).player_id
        print(player_id)
    except:
        pass
    return HttpResponse(player_id, content_type="application/json")
