from django.shortcuts import render,redirect
from . import util
import re
import random
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,entry):
    return render(request, "encyclopedia/entry.html",{
       
        "entry" : entry.capitalize(),
        "content" :  markdown2.markdown(util.get_entry(entry))
    })

def search(request):
    print(request.GET["q"])
    print(util.list_entries())
    query = request.GET["q"].lower()
    lower_list = []
    for a in util.list_entries():
        lower_list.append(a.lower())
    if query in lower_list:
        return redirect('/'+query)
    search_list = []
    for b in lower_list:
        print(re.search(query,b))
        if re.search(query,b):
            search_list.append(b.capitalize())
            print(search_list)
    return render(request, "encyclopedia/search.html",{
        "list": search_list
    })

def new(request):
    return render(request, "encyclopedia/newpage.html" )

def created(request):
    curr_title = request.GET["title"]
    curr_content = request.GET["txtarea"]
    lower_list = []
    for a in util.list_entries():
        lower_list.append(a.lower())
    for r in lower_list:
        if r == curr_title.lower():
            return render(request,"encyclopedia/error.html")
    util.save_entry(curr_title,curr_content)
    # IF ELSE LAGAO TO CHK IF ALREADY EXISTS
    return render(request,"encyclopedia/entry.html",{
    #     "entry" : curr_title,
    #     "content" : curr_content
        "entry" : curr_title.capitalize(),
        "content" :  markdown2.markdown(util.get_entry(curr_title))
    })
    # entry(request, curr_title)

def edit(request,title_tbc):
    curr_title = title_tbc
    curr_content = util.get_entry(curr_title)
    return render(request, "encyclopedia/edit.html",{
        "title_tbc" : curr_title,
        "content_tbc" : curr_content
    })

def randompage(request):
    mylist = util.list_entries()
    randentry = random.choice(mylist)
    print(randentry)
    return redirect('/'+randentry)

def save(request):
    etitle = request.POST["title"]
    econtent = request.POST["txtarea"]
    util.save_entry(etitle,econtent)
    return redirect("/" + etitle)