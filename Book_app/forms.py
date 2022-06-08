
from tkinter import Widget
from django.core import validators
from django import forms
from .models import User

class  Stud_reg(forms.ModelForm):
    class Meta:
        # class Meta:
        model = User
        fields = "__all__"    # all fiels are covered hear no need to create seprate fields
    
        Widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}) ,
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'}),
            
            
            
         }