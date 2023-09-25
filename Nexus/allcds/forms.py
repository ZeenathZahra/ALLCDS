from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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


