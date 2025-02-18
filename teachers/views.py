from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TeachersForm
from .models import teacher

# Create your views here.

def home(request):  
    form = TeachersForm(request.POST)  
    if request.method == 'POST':
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            bio = form.cleaned_data['bio']
            teach = teacher.objects.create(name=name, email=email, phone_number=phone_number, bio=bio)
            return HttpResponse('Well done!!')
    else:
        form = TeachersForm()   
    return render(request, 'teachers/home.html', {'form':form})


def data(request):
    alldata = teacher.objects.all()
    return render(request, 'teachers/alldata.html', {'alldata':alldata})

def update(request,id):
    t = teacher.objects.get(id=id)
    form = TeachersForm(request.POST)
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():
            t.name = form.cleaned_data['name']
            t.email = form.cleaned_data['email']
            t.phone_number = form.cleaned_data['phone_number']
            t.bio = form.cleaned_data['bio']
            t.save()
    else: 
        form = TeachersForm(initial={'name':t.name, 'email':t.email, 'phone_number':t.phone_number, 'bio':t.bio})

    return render(request, 'teachers/update.html',{'form':form})

def delete(request,id):
    if request.method=="POST":
        t = teacher.objects.get(id=id)
        t.delete()

    return HttpResponseRedirect("/home/")

def boottest(request):
    return render(request, 'teachers/boottest.html')