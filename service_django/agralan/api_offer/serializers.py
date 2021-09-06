from rest_framework import serializers
from .models import Offer


class CategorySerializer(serializers.ModelSerializer):
    
    id = serializers.ReadOnlyField()
    title = serializers.CharField(
        required = True,
        max_length = 50
    )
    description = serializers.CharField(
        required = True,
        max_length = 1000
    )
    price = serializers.DecimalField(
        required = True,
        max_digits = 10,
        decimal_places = 2
    )
    created_at = serializers.DateTimeField(
        read_only = True
    )


    class Meta:
        model = Offer
        fields = '__all__'