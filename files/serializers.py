from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Upload


class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Upload
        fields = ['name', 'object', 'created_at', 'updated_at', 'user']
        depth = 0
