from rest_framework import serializers
from .models import Information
import os
import json


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id','country', 'csirt', 'web', 'flag', 'country_code']
        extra_kwargs = {
            'flag': {'read_only': True},
            'country_code': {'read_only': True}
        }
    
    def validate(self, data):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'country.json')
        with open(file_path, 'r') as file:
            data_list = json.load(file)
        user_country = data['country'].lower()
        matching_country = next((item for item  in data_list if item["country"].lower() == user_country), None)
        if not matching_country:
            raise serializers.ValidationError({'country': 'Please enter a valid country'})
        
        return data