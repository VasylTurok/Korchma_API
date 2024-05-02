import math

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class DrinkType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Questionnaire(models.Model):
    name = models.CharField(max_length=63)
    comment = models.TextField()
    phone = models.CharField(max_length=31)
    site_link = models.CharField(max_length=255)
    email = models.CharField(max_length=63)
    drink_type = models.ForeignKey(
        DrinkType,
        on_delete=models.CASCADE,
        related_name="questionnaires"
    )

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Volume(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(unique=True, max_length=63)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=31)
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
            return self.sum_of_marks / self.count_marks
        return 0

    @property
    def count_comments(self) -> int:
        return self.comments.count

    def __str__(self):
        return self.name


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
