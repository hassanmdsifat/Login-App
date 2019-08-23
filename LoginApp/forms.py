from django import forms
from .models import Customer

all_customer=Customer.objects.all()
class LoginForm(forms.Form):
    Email=forms.EmailField(label="Email",max_length=50)
    Password=forms.CharField(label="Password",max_length=50)


class RegisterUser(forms.Form):
    FirstName=forms.CharField(label="First Name",max_length=50)
    LastName=forms.CharField(label="Last Name",max_length=50)
    Email=forms.EmailField(label="Email",max_length=50)
    Password1=forms.CharField(label="Password",max_length=50)
    Password2= forms.CharField(label="Repeat Password", max_length=50)


class addCustomer(forms.Form):
    firstname=forms.CharField(label="First Name",max_length=50)
    lastname=forms.CharField(label="Last Name",max_length=50)
    email=forms.EmailField(label="Email",max_length=100)
    phone=forms.CharField(label="Phone",max_length=15)
    dob=forms.DateTimeField(label="Date Of Birth")
    address=forms.CharField(label="Address",max_length=200)
