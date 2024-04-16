from rest_framework import serializers
from . import models

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