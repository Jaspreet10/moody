from rest_framework import serializers
from ml.models import Sentiments

class mlSerializer(serializers.Serializer):
    compound = serializers.DecimalField(max_digits=19, decimal_places=10)
    neg = serializers.DecimalField(max_digits=19, decimal_places=10)
    neu = serializers.DecimalField(max_digits=19, decimal_places=10)
    pos = serializers.DecimalField(max_digits=19, decimal_places=10)
    
    def create(self, validated_data):
        return Sentiments.objects.create(**validated_data)
