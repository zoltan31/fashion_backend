from rest_framework import serializers
from builder.models import User, Cloth

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ['id', 'name', 'date_of_purchase', 'style', 'type']