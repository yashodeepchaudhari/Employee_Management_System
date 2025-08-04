from django import forms
from .models import ADD_EMP


class ADD_EMPFORM(forms.ModelForm):
    class Meta:
        model = ADD_EMP
        fields = ['empid','name', 'contact', 'email', 'age', 'gender','dept']