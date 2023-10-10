
from django.db.models import fields
from rest_framework import serializers
from .models import customerDetails
 
class customerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = customerDetails
        fields = ('id','name', 'email','PhoneNumber')