from rest_framework import serializers 
from django.conf import settings  
from .models import Invoice  

class InvoiceSerializer(serializers.ModelSerializer):     
    class Meta:         
        model = Invoice  
        exclude = ['user', ]
