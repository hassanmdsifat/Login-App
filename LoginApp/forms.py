from django import forms
from .models import Customer
from .logic import validatePhone,validateEmail,validateName
all_customer=Customer.objects.all()
class LoginForm(forms.Form):
    Email=forms.EmailField(label="Email",max_length=50)
    Password=forms.CharField(label="Password",max_length=50)


class RegisterUser(forms.Form):
    FirstName=forms.CharField(label="First Name",max_length=50,required=True)
    LastName=forms.CharField(label="Last Name",max_length=50)
    Email=forms.EmailField(label="Email",max_length=50)
    Password1=forms.CharField(label="Password",max_length=50)
    Password2= forms.CharField(label="Repeat Password", max_length=50)


class addCustomer(forms.Form):
    firstname=forms.CharField(label="First Name",max_length=50,validators=[validateName])
    lastname=forms.CharField(label="Last Name",max_length=50,validators=[validateName])
    email=forms.EmailField(label="Email",max_length=100,validators=[validateEmail])
    phone=forms.CharField(label="Phone",max_length=15,validators=[validatePhone])
    dob=forms.DateTimeField(label="Date Of Birth")
    address=forms.CharField(label="Address",max_length=200)

class editCustomer(forms.Form):
    firstname=forms.CharField(label="First Name",max_length=50,validators=[validateName])
    lastname=forms.CharField(label="Last Name",max_length=50,validators=[validateName])
    email=forms.EmailField(label="Email",max_length=100)
    phone=forms.CharField(label="Phone",max_length=15,validators=[validatePhone])
    dob=forms.DateTimeField(label="Date Of Birth")
    address=forms.CharField(label="Address",max_length=200)
