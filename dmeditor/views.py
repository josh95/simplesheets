from django.shortcuts import render, redirect
from django.http import HttpResponse
from dmeditor.models import *
from django.utils import timezone
# Create your views here.

def index(request):
    context = {"purpose":"Used by the DM to input info about artifacts and allies the players will encounter"}
    dm_id = request.GET.get('dm_id')
    if dm_id is None:
        dm_id = 0 #we use this as a catch all.
    request.session['dm_id'] = dm_id 

    #find all allies
    allAllies = []
    for ally in Allies.objects.filter(dm_id=dm_id):
        allAllies.append({"name": ally.ally_name,
                          "image": ally.img_url,
                          "id": ally.ally_id
            })
    
    #find most recent allies
    context["allies"] = allAllies
    recentAllies = allAllies[:5]
    context["recentallies"] = recentAllies


    allitems = []
    for item in Items.objects.filter(dm_id=dm_id):
        allitems.append({
                "name": item.item_name,
                "image": item.img_url,
                "id": item.item_id
            })
    context["items"] = allitems
    context["recentitems"] = allitems[:5] 
        
    return render(request, "dmeditor_main.html", context)

def allyEditor(request):
    try:
        dm_id = request.session['dm_id']
    except:
        #user opened a new session and went directly to ally edit, need to redirect to main page
        return redirect("../")
    
    allyID = request.GET.get('param')
    if not allyID is None:
        ##editting existing entry, need to load existing inputs
        ally = Allies.objects.get(ally_id=allyID)
        levels = []
        for level in Levels.objects.filter(ally_id=allyID):
            levels.append(level.description)
        if ally.dm_id == int(dm_id):
            context = {"dm_id" : dm_id,
                       "edit": ally.ally_id,
                       "maxLevel":len(levels),
                       "levels": levels,
                       "name": ally.ally_name,
                       "personality": ally.personality,
                       "description": ally.description,
                       "imgurl": ally.img_url}
        else:
            return redirect("../?dm_id=" + str(dm_id))
    else:
        ##creating a new entry
        context = {"dm_id" : dm_id,
                   "maxLevel":3,
                   "levels": ["blah blah", "blah", "more stuff"]}
    return render(request, "allyeditor.html", context)


def submitAlly(request):
    name = request.POST['name']
    personality = request.POST['personality']
    traits = request.POST.getlist('traits')
    imgurl = request.POST['imgurl']
    description = request.POST['description']
    #levels = request.POST.get('level')
    levels = request.POST.getlist('level')
    edittingid = request.POST['edittingID'] #only set if editting existing ally, None otherwise
    if edittingid:
        newally = Allies(ally_name= name,
               description = description,
               personality = str(personality),
               traits = str(traits),
               last_edit = timezone.now(),
               img_url = imgurl,
               dm_id = request.session['dm_id'],
               ally_id = edittingid)
        
    else:
        newally = Allies(ally_name= name,
                       description = description,
                       personality = str(personality),
                       traits = str(traits),
                       last_edit = timezone.now(),
                       img_url = imgurl,
                       dm_id = request.session['dm_id'])
    newally.save()
    
    Levels.objects.filter(ally_id=newally.ally_id).delete()
    
    for counter, thislevel in enumerate(levels):
        newlevel = Levels(ally_id = newally.ally_id,
                         description = thislevel,
                         level = counter)
        newlevel.save()

    return render(request, "submit.html", {"dm_id":request.session['dm_id']})


def itemEditor(request):
    try:
        dm_id = request.session['dm_id']
    except:
        #user opened a new session and went directly to item edit, need to redirect to main page
        return redirect("../")

    itemID = request.GET.get('param')
    if not itemID is None:
        ##editting existing entry, need to load existing inputs
        item = Items.objects.get(item_id=itemID)
        if item.dm_id == int(dm_id):
            context = {"dm_id" : dm_id,
                       "edit": item.item_id,
                       "name": item.item_name,
                       "description": item.description,
                       "imgurl": item.img_url}
        else:
            return redirect("../?dm_id=" + str(dm_id))
    else:
        ##creating a new entry
        context = {"dm_id" : dm_id}
    return render(request, "itemeditor.html", context)
    
def submitItem(request):

    item = Items()

    edittingid = request.POST['edittingID'] #only set if editting existing item, None otherwise
    if edittingid:
        newitem = Items(item_name= request.POST['name'],
               description = request.POST['description'],
               last_edit = timezone.now(),
               img_url = request.POST['imgurl'],
               dm_id = request.session['dm_id'],
               item_id = edittingid)
        
    else:
        newitem = Items(item_name= request.POST['name'],
               description = request.POST['description'],
               last_edit = timezone.now(),
               img_url = request.POST['imgurl'],
               dm_id = request.session['dm_id'])
    newitem.save()
    return render(request, "submit.html", {"dm_id":request.session['dm_id']})
