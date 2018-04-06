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
            "description" : sheet.description,
            "id": sheet.sheet_id})
            
    context["sheets"] = character_sheets
    context["player"] = player_name
    return render(request, "sheets_main.html", context)

def index(request):
    #takes user to login page
    return render(request, "login.html")

def sheetEditor(request):
    try:
        player_id = request.session['player_id']
    except:
        return redirect("../sheetMain")

    sheet_id = request.GET.get('sheetID')
    
    context = {"playerID" :player_id}
    if sheet_id is None:
        #new sheet
        return render(request, "charsheet.html", context)
    else:
        sheet = Sheets.objects.get(sheet_id = sheet_id)
        context['sheetID'] = sheet.sheet_id
        context['charName'] = sheet.character_name
        context['imgurl'] = sheet.img_url
        context['description'] = sheet.description
        return render(request, "charsheet.html", context)

def checkUser(request):
    try:
        player_id = Player.objects.get(player_name = request.POST['user']).player_id
    except:
        pass
    return HttpResponse(player_id, content_type="application/json")
