from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'px-5  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'Email Address'}))
    first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'Fist Name'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 py-2 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50  w-full bg-rose-50 border border-gray-300 text-gray-900  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'Last Name'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 px-5 py-2 focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg w-full block mb-2 text-sm font-medium text-gray-900 dark:text-black'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted dark:text-white"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = ' bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 px-5 py-2 focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg  w-full block mb-2 text-sm font-medium text-gray-900 dark:text-black'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="w-full form-text text-muted small dark:text-white"><li><small>Your password can\'t be too similar to your other personal information.</small></li><li> <small>Your password must contain at least 8 characters. </small></li><li> <small>Your password can\'t be a commonly used password.</small> </li><li> <small>Your password can\'t be entirely numeric. </small></li></ul> <br /> '

        self.fields['password2'].widget.attrs['class'] = 'bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50  px-5 py-2 focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg  w-full block mb-2 text-sm font-medium text-gray-900 dark:text-black'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted dark:text-white"><small>Enter the same password as before, for verification.</small></span>'



class AddRecordForm(forms.ModelForm):
    first_name= forms.CharField(required=False ,label="First Name",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-white','placeholder':'Jhon','required':True}))
    last_name= forms.CharField(required=False,label="Last Name",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'Doe','required':True  }))
    age=forms.IntegerField(required=False ,label="Age",widget=forms.NumberInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'27' ,'required':True  }))

    address= forms.CharField(required=False ,label="Address",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'#8, Quid Street' ,'required':True  }))
    city= forms.CharField( required=False ,label="City",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'Springfield'  ,'required':True  }))
    state=forms.CharField(  required=False ,label="State",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'Illionis' ,'required':True  }))
    zipcode= forms.CharField( required=False , label="Zipcode",max_length=100,widget=forms.TextInput(attrs={'class':'px-5 bg-rose-50 border border-gray-300 text-gray-900  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full  focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'62629' ,'required':True  }))


    email=forms.EmailField( required=False ,  label="Email",widget=forms.TextInput(attrs={'class':'px-5  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'jhon@doe.us'}))
    phone=forms.CharField( required=False  ,label="Phone Number",widget=forms.TextInput(attrs={'class':'px-5  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'+1-212-456-7890'}))

    is_true=forms.CharField(required=False  ,  label="Diagosis",widget=forms.TextInput(attrs={'class':'px-5  bg-rose-50 border border-gray-300 text-gray-900 py-2 w-full focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg block mb-2 text-sm font-medium text-gray-900 dark:text-black','placeholder':'Unspecified'}))



    image=   forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': False,'required': True }))


    medical_history=  forms.FileField(required=False,   widget=forms.ClearableFileInput(attrs={'multiple': False, 'required':True }))

    genatic_information=   forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': False, 'required':True  }))

    lab_results=  forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': False, 'required':True  }))
    radiology_results=  forms.FileField(required=False,  widget=forms.ClearableFileInput(attrs={'multiple': False, 'required':True  }))
    clinical_results=  forms.FileField(required=False,  widget=forms.ClearableFileInput(attrs={'multiple': False, 'required':True }))


    class Meta:
        model=Record
        exclude=('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



