from django.shortcuts import render,get_object_or_404
from .forms import LoginForm,RegisterUser,addCustomer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .logic import validatePhone
from .models import Customer,Order
from django.utils import timezone

def index(request):
    if request.user.is_authenticated:
        return render(request, "LoginApp/dashboard.html")
    return render(request,"LoginApp/index.html",{})

def login(request):
    newform=LoginForm()
    error=[]
    if request.user.is_authenticated:
        return render(request,"LoginApp/dashboard.html")
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
          email=form.cleaned_data["Email"]
          password=form.cleaned_data["Password"]
          print(email,password)
          user=authenticate(request, username=email, password=password)
          print(user)
          if user is not None:
              auth_login(request,user)
              return HttpResponseRedirect(reverse("LoginApp:dashboard"))
          else:
              error.append("User Does not Exist!!")
    context={
        "form":newform,
        "error":error,
    }
    return render(request,"LoginApp/login.html",context)

def register(request):
    if request.user.is_authenticated:
        return render(request,"LoginApp/dashboard.html",{})
    newform=RegisterUser()
    error=[]
    if request.method=="POST":
        newform=RegisterUser(request.POST)
        if newform.is_valid():
            firstname=newform.cleaned_data["FirstName"]
            lastname=newform.cleaned_data["LastName"]
            email=newform.cleaned_data["Email"]
            password=newform.cleaned_data["Password1"]
            rpassword=newform.cleaned_data["Password2"]
            if password!=rpassword:
                error.append("Password and Repeat Password doesn't match")
            checkUser= User.objects.filter(username=email)
            if len(checkUser)==0:
                user = User()
                user.username = email
                user.first_name = firstname
                user.last_name = lastname
                user.email = email
                user.set_password(password)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Registered Successfully')
                return HttpResponseRedirect(reverse('LoginApp:login'))
            else:
                error.append("User Already Exist")
        else:
            error.append("Fill out the form properly")
    context={
        "form":newform,
        "errormessage":error
    }
    return render(request,"LoginApp/register.html",context)

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,"LoginApp/dashboard.html",{})
    else:
        return render(request,"LoginApp/index.html",{})


def logout(request):
    auth_logout(request)
    return render(request,"LoginApp/index.html",{})


def addcustomer(request):
    if request.user.is_authenticated:
        customerform=addCustomer()
        context = {
            'form': customerform
        }
        if request.method=="POST":
            customerform=addCustomer(request.POST)
            if customerform.is_valid():
                cnt=0
                firstname=customerform.cleaned_data["firstname"]
                lastname=customerform.cleaned_data["lastname"]
                phone=customerform.cleaned_data["phone"]
                email=customerform.cleaned_data["email"]
                dob=customerform.cleaned_data["dob"]
                address=customerform.cleaned_data["address"]
                firstname=firstname.lstrip()
                lastname = lastname.lstrip()
                email=email.lstrip()
                address=address.lstrip()
                if not validatePhone(phone):
                    messages.add_message(request, messages.ERROR, 'Not a valid Number')
                    cnt=1
                if len(Customer.objects.filter(email=email)):
                    messages.add_message(request,messages.ERROR,"User Already Exist!!!")
                    cnt=1
                if cnt==0:
                    q= Customer(firstname=firstname,lastname=lastname,email=email,phonenumber=phone,dob=dob,address=address)
                    q.save()
                    return HttpResponseRedirect(reverse("LoginApp:showcustomerlist"))
                else:
                    return render(request, "LoginApp/addcustomer.html", context)

        return render(request,"LoginApp/addcustomer.html",context)
    else:
        return render(request,"LoginApp/index.html",{})



def showAllCustomer(request):
    if request.user.is_authenticated:
        AllCustomer=Customer.objects.all()
        context={
            'customerlist':AllCustomer,
        }
        return render(request,"LoginApp/customerlist.html",context)
    else:
        return render(request,"LoginApp/index.html",{})


def deletecustomer(request,c_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Customer,pk=c_id)
        question.delete()
        AllCustomer = Customer.objects.all()
        context = {
            'customerlist': AllCustomer,
        }
        return render(request,"LoginApp/customerlist.html",context)
    else:
        return render(request,"LoginApp/index.html",{})


def editcustomer(request,c_id):
    if not request.user.is_authenticated:
        return render(request,"LoginApp/index.html",{})
    else:
        customer= get_object_or_404(Customer, pk=c_id)
        form=addCustomer()
        context = {
            'form': form,
            'customer': customer,
        }
        if request.method=="POST":
            newform=addCustomer(request.POST)
            if newform.is_valid():
                firstname=newform.cleaned_data["firstname"]
                firstname=firstname.lstrip()
                lastname = newform.cleaned_data["lastname"]
                lastname=lastname.lstrip()
                email=newform.cleaned_data["email"]
                email=email.lstrip()
                phone=newform.cleaned_data["phone"]
                phone=phone.lstrip()
                address=newform.cleaned_data["address"]
                address=address.lstrip()
                if firstname==customer.firstname and lastname==customer.lastname and phone==customer.phonenumber and email==customer.email and address==customer.address:
                    messages.add_message(request, messages.ERROR, "Nothing Changed!!!")
                    return render(request,"LoginApp/editcustomer.html",context)
                else:
                    cnt=0
                    if validatePhone(phone):
                        customer.firstname=firstname
                        customer.lastname=lastname
                        customer.phonenumber=phone
                        customer.address=address
                        customer.save()
                        messages.add_message(request, messages.ERROR, "Edited Successfully!!!")
                        return HttpResponseRedirect(reverse("LoginApp:showcustomerlist"))

                    else:
                        messages.add_message(request, messages.ERROR, "Phone Number not valid!!!")
                        return render(request, "LoginApp/editcustomer.html", context)
        return render(request,"LoginApp/editcustomer.html",context)


def addorder(request):
    if request.user.is_authenticated:
        all_user=Customer.objects.all()
        context={
            'customerlist':all_user,
        }
        if request.method=="POST":
            order_details=request.POST["details"]
            cid=request.POST["cid"]
            get_customer=get_object_or_404(Customer,pk=cid)
            order=Order(placementdate=timezone.now(),customer=get_customer,details=order_details)
            order.save()
            return HttpResponseRedirect(reverse("LoginApp:showorderlist"))

        else:
            return render(request,"LoginApp/addorder.html",context)
    else:
        return render(request,"LoginApp/index.html",{})


def allorder(request):
    if request.user.is_authenticated:
        get_all_order=Order.objects.all().order_by("-id")
        context={
            'orderlist':get_all_order
        }
        return render(request,"LoginApp/orderlist.html",context)
    else:
        return render(request,"LoginApp/index.html",{})\


def deleteorder(request,o_id):
    if request.user.is_authenticated:
        get_order=get_object_or_404(Order,pk=o_id)
        get_order.delete()
        messages.add_message(request,messages.SUCCESS,"Order Deleted Successfully")
        return HttpResponseRedirect(reverse("LoginApp:showorderlist"))
    else:
        return render(request,"LoginApp/index.html",{})