from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from .models import (
    Drink,
    DrinkType,
    Producer,
    Volume,
    Region,
    Comment,
    Photo,
    Questionnaire
)


# TODO добавити кількість випивки в регіоні
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            "id",
            "name",
            "count_drink"
        )


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
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
    producer = ProducerSerializer(many=False, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

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
            "count_comments",
            "isRating",
            "rating",
            "producer",
            "volume",
            "drink_type",
            "region",
            "comments",
            "photos"
        )


class DrinkListSerializer(DrinkSerializer):
    class Meta:
        model = Drink
        fields = (
            "id",
            "name",
            "descriptions",
            "price",
            "count_comments",
            "isRating",
            "rating",
            "producer",
            "volume",
            "drink_type",
            "region",
            "photos"
        )
