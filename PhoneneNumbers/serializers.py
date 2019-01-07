from .models import Client
from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    phone = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Client` instance, given the validated data.
        """
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Client` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance