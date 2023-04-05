from rest_framework import serializers
from .models import Pers



class PersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pers
        fields = ('photo','name', 'lor')