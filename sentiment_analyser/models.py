from django.db import models
from phone_field import PhoneField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100, help_text = "First name")
    last_name = models.CharField(max_length = 100, help_text = "Last name")
    email = models.EmailField(blank = True, help_text = "Email ID")
    contact_number = PhoneField(blank = True, help_text = 'Phone Number')
