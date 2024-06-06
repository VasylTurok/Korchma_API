import math

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class DrinkType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Questionnaire(models.Model):
    name = models.CharField(max_length=63)
    comment = models.TextField(blank=True)
    phone = models.CharField(max_length=31)
    site_link = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=63)
    drink_type = models.ForeignKey(
        DrinkType,
        on_delete=models.CASCADE,
        related_name="questionnaires",
        blank=True
    )

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=63)

    @property
    def count_drink(self) -> int:
        return self.drinks.count

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=63)
    logo = models.URLField(blank=True)
    image = models.URLField(blank=True)
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=31, blank=True)
    email = models.CharField(max_length=63, blank=True)
    insta = models.CharField(max_length=63, blank=True)
    fb = models.CharField(max_length=63, blank=True)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="producers"
    )

    def __str__(self):
        return self.name


class Volume(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(unique=True, max_length=63)
    descriptions = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    phone = models.CharField(max_length=31, blank=True)
    site_link = models.CharField(max_length=255, blank=True)
    strength = models.CharField(max_length=63, blank=True)
    taste_parameters = models.CharField(max_length=63, blank=True)
    tastes_together = models.CharField(max_length=63, blank=True)
    isRating = models.BooleanField(default=False)
    volume = models.ForeignKey(
        Volume,
        on_delete=models.CASCADE,
        related_name="drinks"
    )
    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        related_name="drinks",
        default=1
    )
    drink_type = models.ForeignKey(
        DrinkType,
        on_delete=models.CASCADE,
        related_name="drinks"
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="drinks"
    )
    sum_of_marks = models.IntegerField(default=0)
    count_marks = models.IntegerField(default=0)

    @property
    def rating(self) -> float:
        if self.count_marks != 0:
            return round(self.sum_of_marks / self.count_marks, 1)
        return 0.0

    @property
    def count_comments(self) -> int:
        return self.comments.count

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
        related_name="photos",

    )

    def clean(self):
        if self.drink.photos.count() >= 3:
            raise ValidationError("Максимальна кількість фото для напою вже досягнута.")

    def __str__(self):
        return self.image


class Comment(models.Model):
    name = models.CharField(max_length=63)
    email = models.CharField(max_length=63)
    body = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    advantages = models.TextField(blank=True)
    disadvantages = models.TextField(blank=True)
    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.full_clean()
        self.drink.sum_of_marks += self.rating
        self.drink.count_marks += 1
        self.drink.save()
        return super(Comment, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return self.name
