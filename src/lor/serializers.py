from rest_framework import serializers
from .models import Pers



class PersSerializer(serializers.Serializer):
    
    photo = serializers.ImageField(default=None)
    lor = serializers.CharField()
    fraction = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=30)
    character = serializers.StringRelatedField()
    
    
    def create(self, validated_data):
        return Pers.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.lor = validated_data.get('lor', instance.lor)
        instance.fraction = validated_data.get('fraction', instance.fraction)
        instance.name = validated_data.get('name', instance.name)
        instance.character = validated_data.get('character', instance.character)
        instance.save()
        return instance