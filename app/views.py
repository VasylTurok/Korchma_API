from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from .models import (
    Drink,
    Questionnaire,
    DrinkType,
    Producer,
    Volume,
    Region,
    Comment
)

from .serializers import (
    DrinkSerializer,
    DrinkTypeSerializer,
    ProducerSerializer,
    VolumeSerializer,
    RegionSerializer,
    CommentSerializer,
    DrinkListSerializer
)


class Pagination(PageNumberPagination):
    page_size = 9
    max_page_size = 100


class DrinkViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Drink.objects.prefetch_related(
        "volume", "drink_type", "region", "comments"
    )

    def get_serializer_class(self):
        if self.action == "list":
            return DrinkListSerializer
        return self.serializer_class

    serializer_class = DrinkSerializer
    # pagination_class = Pagination


class DrinkTypeViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = DrinkType.objects.all()
    serializer_class = DrinkTypeSerializer


class ProducerViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class VolumeViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer


class RegionViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CommentViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
