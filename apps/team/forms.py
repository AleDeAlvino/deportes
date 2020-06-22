from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # Formularios para registrar un alumno
    class Meta:
        model = Student
        exclude = ('liberado',)
        labels = {
            'team':''
        }
        widgets ={
            'team' : forms.NumberInput(attrs={'hidden':True})
        }