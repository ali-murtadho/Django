from rest_framework import serializers
from . models import padi

class padiSerializers(serializers.Serializer):
    class Meta:
        model = padi
        fields = '__all__'