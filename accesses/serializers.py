from rest_framework import serializers
from .models import Accesses

class AccessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesses
        fields = '__all__'
