from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

from plotly.offline import plot
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px

import tensorflow
import pandas
from tensorflow import keras

import os
import random
import zipfile
from pathlib import Path


# pending diagnosis
# user activity

class Prata():
  def __init__(self,batch_size,img_height,img_width):
    self.batch_size=batch_size
    self.img_height=img_height
    self.img_width=img_width

  def load_data(self,path):
    train_ds= tensorflow.keras.utils.image_dataset_from_directory(
        path,
        seed=42,
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
    model = tensorflow.keras.saving.load_model(self.model_dir,compile=True)
    print(sum (model.predict(dataset))/len(model.predict(dataset)))
    return "HEM" if sum (model.predict(dataset))/len(model.predict(dataset))>0.5 else "ALL"

class Statistics():
    def __init__(self,records):
        self.length = len(records)
        self.patients = len([i.is_true for i in records if i.is_true=='ALL'])
        self.new_patients = random.randint(1,len(records))




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
        records=Record.objects.all()
        merecat=Statistics(records)
        frame = pandas.DataFrame({'id':[i.id for i in records],'date':[i.created_At for i in records],'diagnosis':[i.is_true for i in records]})
        frame['date'] = pandas.to_datetime(frame['date'])
        custom_colors = {'HEM': '#FF9999', 'ALL': '#EF4444'}
        figr=px.pie(frame, names='diagnosis', title='Ratio',color='diagnosis',color_discrete_map=custom_colors)
        figl=px.line(frame, x='date', color='diagnosis', title='Diagnosis Over Time')
        figbr=go.Figure(data=[go.Table(
            header=dict(values=list(frame.columns),
                    fill_color='#FF9999',
                    align='left'),
                    cells=dict(values=[frame.id,frame.date,frame.diagnosis],
                    fill_color='lavender',
                    align='left'))])
        filtered_frame = frame[frame['diagnosis']=='Unspecified']
        figbl=go.Figure(data=[go.Table(
            header=dict(values=['ID','Status'],
                    fill_color='#FF9999',
                    align='left'),
                    cells=dict(values=[filtered_frame.id,filtered_frame.diagnosis],
                    fill_color='lavender',
                    align='left'))])

        
        plotly_plot_objr = plot({'data': figr}, output_type='div')
        plotly_plot_objl = plot({'data': figl}, output_type='div')
        plotly_plot_objbr = plot({'data': figbr}, output_type='div')
        plotly_plot_objbl = plot({'data': figbl}, output_type='div')
        


        return render(request,'home.html',{'stats':merecat,'frame':frame,'target':plotly_plot_objr,'target1':plotly_plot_objl,'target2':plotly_plot_objbr,'target3':plotly_plot_objbl})


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
            BASE_DIR = Path(__file__).resolve().parent.parent
            dpath=str(BASE_DIR)+"\\media\\images\\"+str(form.cleaned_data['image']).replace('/','\\')
            mpath=str(BASE_DIR)+"\\allcds\\model\\weights\\content\\"
            zipfile.ZipFile(dpath,'r').extractall(dpath[:-4]+"\\")
            new = Prata(32,180,180).load_data(dpath[:-4])
            whatever=Prometheus(mpath)
            form.instance.is_true=whatever.infer(new)
            form.save()
            messages.success(request,"Record Updated" )
            return redirect('home')
        return render(request,'up_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to view this page")
        return redirect('home')


