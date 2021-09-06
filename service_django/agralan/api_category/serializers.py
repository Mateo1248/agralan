from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    id = serializers.ReadOnlyField()
    name = serializers.CharField(required = True)

    class Meta:
        model = Category
        fields = '__all__'