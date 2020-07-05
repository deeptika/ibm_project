#creating ModelForm here
from django import forms 
from .models import User

class UserForm(forms.ModelForm): 
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    class Meta: 
        model = User
        fields = "__all__"
