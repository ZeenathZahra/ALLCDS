from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
import os
#import tensorflow
#from tensorflow import keras

class Prata():
  def __init__(self,batch_size,img_height,img_width):
    self.batch_size=batch_size
    self.img_height=img_height
    self.img_width=img_width

  def load_data(self,path):
    train_ds= tensorflow.keras.utils.image_dataset_from_directory(
        path,
        seed=123,
        image_size=(self.img_height, self.img_width),
        batch_size=self.batch_size)
    AUTOTUNE = tensorflow.data.AUTOTUNE
    return train_ds.cache().prefetch(buffer_size=AUTOTUNE)


class Uzta():
  def __init__(self,path):
    self.path=path

  def unzip(self):
    zipfile.ZipFile(self.path,'r').extractall()

class Prometheus():
  def __init__(self,model_dir):
    self.model_dir=model_dir

  def infer(self,dataset):
    model = tensorflow.keras.models.load_model(self.model_dir)
    return "HEM" if model.predict(dataset)[0][0]>0.5 else "ALL"





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

def up_precord(request,pk):
    if request.user.is_authenticated:
        currect_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST  or None, request.FILES or None,instance=currect_record)
        if form.is_valid():
            dpath='/home/ahmed/lab/ALLCDS/Nexus/media/images/'+forms.cleaned_data['image']
            mpath='/home/ahmed/lab/ALLCDS/Nexus/allcds/model/weights/content/wb'
            object=Uzta(dpath).unzip()
            new = Prata(32,180,180).load_data(dpath[:-4])
            whatever=prometheus(mpath)
            form.cleaned_data['is_true']=whatever.infer(new)
            form.save()
            messages.success(request,"Record Updated" )
            return redirect('home')
        return render(request,'up_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to view this page")
        return redirect('home')


