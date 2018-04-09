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
    dm_id = Player.objects.get(player_id = int(player_id)).dm_id
    allAllies = []
    for ally in Allies.objects.filter(dm_id = dm_id):
        allAllies.append({
            "name": ally.ally_name,
            "image" : ally.img_url,
            "description" : ally.description,
            "id": ally.ally_id})
    allItems = []
    for item in Items.objects.filter(dm_id=dm_id):
        allItems.append({
                "name": item.item_name,
                "image" : item.img_url,
                "description" : item.description,
                "importance" : item.importance,
                "id": item.item_id
            })
    
    context = {"playerID" :player_id, "allAllies": allAllies, "allItems": allItems}
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

def saveChanges(request):
    data = json.loads(request.POST["payload"])
    print(data)
    success = [1,2,3]
    return HttpResponse(success, content_type="application/json")

def getLevels(request):
    allyID = int(request.GET.get('allyID'))
    level = int(request.GET.get('level')) -1
    levelList = []
    for item in Levels.objects.filter(level__lte = level, ally_id = allyID):
        levelList.append(item.description)
    return HttpResponse(json.dumps(levelList), content_type="application/json")

def getAllyDeets(request):
    allyID = int(request.GET.get('allyID'))
    ally = Allies.objects.get(ally_id = allyID)
    return HttpResponse(json.dumps({"imgurl": ally.img_url, "description":ally.description}), content_type="application/json")

def getItemDeets(request):
    itemID = int(request.GET.get('itemID'))
    item = Items.objects.get(item_id = itemID)
    return HttpResponse(json.dumps({"imgurl": item.img_url, "description":item.description}), content_type="application/json")
    
    
