from django.shortcuts import render
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def index(request):
    objs = TodoItem.objects.all()
    context = {'objs':objs}
    return render(request,'index.html',context=context)

def addtodo(request):
    c = request.POST['content']
    new_obj = TodoItem(todo_item = c)
    new_obj.save()
    return HttpResponseRedirect("/todoapp/")

def deleteitem(request,id):
    obj = TodoItem.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect("/todoapp/")