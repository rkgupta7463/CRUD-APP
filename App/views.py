from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.
# super user id: crud , pass: C@1234


def home(request):
    request.session['name'] = 'Rishu'
    if 'name' in request.session:
        request.session.modified = True
        fm = StudentInfoForm()
        viewdb = StudentDB.objects.all()
        if request.method == "POST":
            fm = StudentInfoForm(request.POST)
            if fm.is_valid:
                name = request.POST['sname']
                email = request.POST['semail']
                Phone = request.POST['phone']
                Brnach = request.POST['Branch']
                College = request.POST['college']

                dbsave = StudentDB(sname=name, semail=email,
                                   phone=Phone, Branch=Brnach, college=College)
                dbsave.save()
                fm = StudentInfoForm()
                messages.success(request, "Your list have created!")
        else:
            fm = StudentInfoForm()
        context = {
            'form': fm,
            'viewdb': viewdb
        }
        return render(request, 'home.html', context)
    else:
        return HttpResponse("Your session has expired........!")

# update function


def update(request, uid):
    if request.method == 'POST':
        pi = StudentDB.objects.get(id=uid)
        updata = StudentInfoForm(request.POST, instance=pi)
        if updata.is_valid:
            updata.save()
            return redirect('home')
    else:
        pi = StudentDB.objects.get(id=uid)
        updata = StudentInfoForm(instance=pi)

    return render(request, 'update.html', {'updateform': updata})

# delete function

def delete(request,pk):
    member = StudentDB.objects.get(id=pk)
    member.delete()
    messages.success(request,"Data Deleted!")
    return redirect("home")

