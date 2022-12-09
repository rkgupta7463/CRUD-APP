from django import forms
from .models import *

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=StudentDB
        fields=['sname','semail','phone','Branch','college']
        labels={'sname':'Name','semail':'Email', 'phone':'Phone','Branch':'Branch','college':'College'}
        widgets={'sname':forms.TextInput(attrs={'class':'form-control'}), 'semail':forms.EmailInput(attrs={'class':'form-control'}), 'phone':forms.NumberInput(attrs={'class':'form-control'}), 'Branch':forms.TextInput(attrs={'class':'form-control'}),'college':forms.TextInput(attrs={'class':'form-control'})}
