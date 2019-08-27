from rest_framework import serializers
from .models import Customer,Order
from . import logic


'''class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'''


class customerSerializer(serializers.Serializer):
    firstname=serializers.CharField(label="firstname",max_length=50,required=False,validators=[logic.validateserializerName])
    lastname=serializers.CharField(max_length=50,required=False,validators=[logic.validateserializerName])
    email=serializers.EmailField(max_length=100,required=False,validators=[logic.validateserializerEmail])
    phonenumber=serializers.CharField(max_length=15,required=False,validators=[logic.validateserializerPhone])
    address=serializers.CharField(max_length=200,required=False)
    dob=serializers.DateTimeField(read_only=True,required=False)

    def update(self, instance, validated_data):
       instance.firstname=validated_data.get('firstname',instance.firstname)
       instance.lastname=validated_data.get('lastname',instance.lastname)
       instance.phonenumber=validated_data.get('phonenumber',instance.phonenumber)
       instance.address=validated_data.get('address',instance.address)
       instance.save()
       return instance


class AddCustomerserializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=50, validators=[logic.validateserializerName])
    lastname = serializers.CharField(max_length=50, validators=[logic.validateserializerName])
    email = serializers.EmailField(max_length=100, validators=[logic.validateserializerEmail_two])
    phonenumber = serializers.CharField(max_length=15, validators=[logic.validateserializerPhone])
    address = serializers.CharField(max_length=200)
    dob = serializers.DateField()

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

