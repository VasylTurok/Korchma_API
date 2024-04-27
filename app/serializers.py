from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from .models import (
    Drink,
    Questionnaire,
    DrinkType,
    Producer,
    Volume,
    Region,
    Comment
)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = "__all__"


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class DrinkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkType
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = "__all__"
