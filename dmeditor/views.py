from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {"purpose":"Used by the DM to input info about artifacts and allies the players will encounter"}

    #find most recent allies
    recentAllies = [{"name": "bee girl", "image": "url"},
                    {"name": "slime girl", "image": "url"},
                    {"name": "holstaur girl", "image": "url"}]
    context["allies"] = recentAllies
    return render(request, "dmeditor_main.html", context)

def allyEditor(request):
    allyID = request.GET.get('param')
    
    if not allyID is None:
        ##fetch existing data
        pass
    else:
        context = {"maxLevel":3, "levels": ["blah blah", "blah", "more stuff"]}
    return render(request, "allyeditor.html", context)


def submitAlly(request):
    name = request.POST['name']
    print(name)
    return render(request, "submit.html")
