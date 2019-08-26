from django import forms
from .models import Customer

def is_num(value):
    for val in value:
        if val.isnumeric():
            return True
    else:
        return False

def validatePhone(value):
    if len(value) < 11 or len(value) > 13:
        raise forms.ValidationError("Invalid Phone Number")
    if not value.isnumeric():
        raise forms.ValidationError("Invalid Phone Number!!!")


def validateEmail(value):
    if len(Customer.objects.filter(email=value)):
        raise forms.ValidationError("Email Already Exist!!!")

def validateName(value):
    if is_num(value):
        raise forms.ValidationError("Name can not contain numbers!!!")