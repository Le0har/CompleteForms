from rest_framework import serializers
from forms.models import Form
import re


class FormSerializer(serializers.ModelSerializer): 
    phone = serializers.CharField(max_length=16, min_length=12)

    class Meta:
        model = Form
        fields = ('name', 'email', 'phone', 'data', 'text')
        read_only_fields = ['name', 'email', 'phone', 'data', 'text']
        extra_kwargs = {
            'name': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'data': {'required': False},
            'text': {'required': False}
            }
        
    def validate_phone(self, phone):
        if not re.match(r'^\+7\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{2}\s?[0-9]{2}$', phone):
            raise serializers.ValidationError('Invalid phone number format.')
        return phone