from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms 
from .models import Profile



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']     
        widgets ={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),

        } 







class StudentForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['education','city','gender','course','photo']  
        widgets = {
          
            'education': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'course' : forms.Select(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
        }

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['education','city','gender','course','photo']
        widgets = {
            'education': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'course' : forms.Select(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
        }