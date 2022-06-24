# from Trainee import forms
# from .models import Course, Trainee

from django import forms
from .models import Course,Trainee


class Traineeform(forms.Form):
    name = forms.CharField(label='User Name  :', max_length=50)
    nid = forms.CharField(label='natonal_num :', max_length=12)
    courses = forms.ModelChoiceField(Course.objects.all())
    # courses = forms.ChoiceField(widget=forms.Select, choices=Course.objects.all(), required=False, help_text="Courses")


class List(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'

class TraineeUpdate(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'
