from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

class NoteSerializer(serializers.ModelSerializer):  
    class Meta:
        model = models.Note
        fields = '__all__'
    
    def update(self, instance, validated_data):
        validated_data.pop('created_at', None)
        return super().update(instance, validated_data)

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kategori
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('created_at', None)
        return super().update(instance, validated_data)