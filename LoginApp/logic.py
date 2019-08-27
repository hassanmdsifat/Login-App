from django import forms
from .models import Customer
from rest_framework import serializers
from django.contrib import messages

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


def validateserializerName(value):
    if is_num(value):
        raise serializers.ValidationError("Name can not contain numbers!!!")

def validateserializerPhone(value):
    if len(value) < 11 or len(value) > 13:
        raise serializers.ValidationError("Invalid Phone Number")
    if not value.isnumeric():
        raise serializers.ValidationError("Invalid Phone Number!!!")

def validateserializerEmail(value):
    tmp=Customer.objects.filter(email=value)
    if len(tmp) and tmp.email!=value:
        raise serializers.ValidationError("Email Already Exist!!!")

def validateserializerEmail_two(value):
    tmp = Customer.objects.filter(email=value)
    if len(tmp)>0:
        raise serializers.ValidationError("Email Already Exist!!!")