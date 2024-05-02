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
    comments = CommentSerializer(many=True, read_only=True)
    region = RegionSerializer(many=False, read_only=True)
    volume = VolumeSerializer(many=False, read_only=True)
    drink_type = DrinkTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Drink
        fields = (
            "id",
            "name",
            "descriptions",
            "price",
            "phone",
            "site_link",
            "strength",
            "taste_parameters",
            "tastes_together",
            "isRating",
            "rating",
            "volume",
            "drink_type",
            "region",
            "comments"
        )
