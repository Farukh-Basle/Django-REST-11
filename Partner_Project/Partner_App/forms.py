
from django import  forms

class EmployeeForm(forms.Form):
    eno = forms.IntegerField()
    ename = forms.CharField()
    salary = forms.DecimalField()
