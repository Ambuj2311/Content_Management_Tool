from django.shortcuts import render
from .forms import contentform
from .models import content
from django.http import HttpResponseRedirect

def show(request):
    if request.method=="POST":
        form= contentform(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            form = contentform()     
    else:
        
        form = contentform()  
    records=content.objects.all()
    return render(request,'create.html',{'form':form,'records':records})


def deleterecord(request,id):
    
    stdId= content.objects.get(pk=id)
    stdId.delete()
    return HttpResponseRedirect('/')

def updaterecord(request,id):
    if request.method=="POST":   
        stdId=content.objects.get(pk=id)
        form=contentform(request.POST,request.FILES,instance=stdId)
        if form.is_valid():
            form.save()
          
        
    else:
        stdId=content.objects.get(pk=id)
        form=contentform(instance=stdId)
    
    
    return render(request,'update.html',{'form':form})
