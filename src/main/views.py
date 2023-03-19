from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDolist , Item
from .forms import CreateNewList
# Create your views here.


def home(response):
   return render(response ,"main/home.html")

def index(response,id):
    ls = ToDolist.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if(response.POST.get("c"+str(item.id)) == "clicked"):
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newitem"):
            txt = response.POST.get("item")

            if len(txt) > 2:
                ls.item_set.create(text=txt,complete = False)
            else:
                print("len less than 2")    

    return render(response,"main/base.html",{"ls":ls})

def cart(response):
    return render(response ,"main/cart.html")
