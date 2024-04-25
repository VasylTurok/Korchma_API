from django.contrib import admin

from .models import (
    Drink,
    Questionnaire,
    DrinkType,
    Producer,
    Volume,
    Region,
    Comment
)


admin.site.register(Drink)
admin.site.register(Questionnaire)
admin.site.register(DrinkType)
admin.site.register(Producer)
admin.site.register(Volume)
admin.site.register(Region)
admin.site.register(Comment)
