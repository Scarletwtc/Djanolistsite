from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList, DeleteList
# Create your views here.

def index(response, id):
    ls = TodoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False 

                    item.save()       
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) >2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid");       
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})

def home(response):
     return render(response, "main/home.html", {}) 

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST) 

        if form.is_valid():
            n= form.cleaned_data['name']
            t = TodoList(name=n)
            t.save()
            response.user.todolist.add(t)
           
        return HttpResponseRedirect("/%i" %t.id)
    else:     
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})

def delete(response):
    if response.method == "POST":
        list_id = response.POST.get("list_to_delete")
        try:
            list_to_delete = TodoList.objects.get(id=list_id)
            if list_to_delete in response.user.todolist.all():
                list_to_delete.delete()
                response.user.todolist.remove(list_to_delete)
        except TodoList.DoesNotExist:
            pass
    return HttpResponseRedirect("/view")