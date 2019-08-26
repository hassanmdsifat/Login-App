from django.db import models

class Customer(models.Model):
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    phonenumber= models.CharField(max_length=15)
    dob=models.DateTimeField('Date of Birth')
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Order(models.Model):
    placementdate=models.DateField("Placement Date")
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='orders')
    details=models.CharField(max_length=500)