from django import forms
from users.models import *


class Registerform(forms.Form):
    username = forms.CharField(label='User Name', max_length=20)
    password = forms.CharField(label='Password', max_length=12)
    confirm = forms.CharField(label='Confirm', max_length=12)
    username.widget.attrs['class'] = 'form-control form-control-user '
    password.widget.attrs['class'] = 'form-control form-control-user '
    confirm.widget.attrs['class'] = 'form-control form-control-user '


class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

