from rest_framework import routers

from .views import (
    DrinkViewSet,
    DrinkTypeViewSet,
    RegionViewSet,
    VolumeViewSet,
    ProducerViewSet,
    CommentViewSet,
    QuestionnaireViewSet
)

router = routers.DefaultRouter()
router.register("drink", DrinkViewSet)
router.register("drink-type", DrinkTypeViewSet)
router.register("region", RegionViewSet)
router.register("volume", VolumeViewSet)
router.register("producer", ProducerViewSet)
router.register("comment", CommentViewSet)
router.register("questionnaire", QuestionnaireViewSet)


urlpatterns = router.urls

app_name = "app"
