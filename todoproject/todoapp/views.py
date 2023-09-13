from django.shortcuts import render, redirect

from .forms import todoform
from .models import task


# Create your views here.
def sample(request):
    return render(request,'sample.html')


def home(request):
    det = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        tasks=task(name=name,priority=priority,date=date)
        tasks.save()
    return render(request,'home.html',{'det':det})


# def details(request):
#     det = task.objects.all()
#     return render(request,'details.html',{'det':det})


def delete(request,taskid):
    tasks=task.objects.get(id=taskid)
    if request.method=='POST':
        tasks.delete()
        return redirect('/')

    return render(request,'delete.html')


def update(request,id):
    tasks=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=tasks)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request,'edit.html',{'f':f,'tasks':tasks})

