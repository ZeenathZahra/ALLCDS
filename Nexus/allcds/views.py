from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.
def records(request):
    records=Record.objects.all()

    return render(request,'records.html',{'records':records})

def home(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # Authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In")
            return redirect('home')
        else:
            messages.success(request,"Error, Try again...")
            return redirect('home')
    else:
        return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')


def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login(, user)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Successfully registed.")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{'form':form})



def precord(request,pk):
    if request.user.is_authenticated:
        patient_record=Record.objects.get(id=pk)
        return render(request,'pat_records.html',{'patient_record':patient_record})
    else:
        messages.success(request,"You must be logged in to view this page")
        return redirect('home')


def del_precord(request,pk):
    if request.user.is_authenticated:

        delete = Record.objects.get(id=pk)
        delete.delete()
        messages.success(request,"Deleted")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in to view this page")
        return redirect('home')


def add_precord(request):

    form=AddRecordForm(request.POST , request.FILES)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record Added")
                return redirect('home')

        return render(request,'add_records.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to view this page")
        return redirect('home')


