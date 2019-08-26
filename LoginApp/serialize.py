from rest_framework import serializers
from .models import Customer,Order


'''class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'''

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class customerSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    firstname=serializers.CharField(max_length=50)
    lastname=serializers.CharField(max_length=50)
    email=serializers.EmailField(max_length=100)
    phonenumber=serializers.CharField(max_length=15)
    address=serializers.CharField(max_length=200)
    dob=serializers.DateTimeField()

    def create(self):
        pass



