from rest_framework import serializers
from .models import Referal

class ReferalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referal
        fields = '__all__'
