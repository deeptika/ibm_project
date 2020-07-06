#creating ModelForm here
from django import forms 
from .models import User

class UserForm(forms.ModelForm): 
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    contact_number = forms.RegexField(regex=r'^[6-9]\d{9}$')
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email', 'contact_number']
