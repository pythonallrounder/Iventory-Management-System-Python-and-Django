from django import forms
from .models import *

class laptopform(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type','price','status','issue')


class desktopform(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type','price','status','issue')
        

class mobileform(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type','price','status','issue')        