# Generated by Django 5.0.4 on 2024-04-25 14:30

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, unique=True)),
                ('descriptions', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('phone', models.CharField(max_length=31)),
                ('site_link', models.CharField(blank=True, max_length=255)),
                ('strength', models.CharField(blank=True, max_length=63)),
                ('taste_parameters', models.CharField(blank=True, max_length=63)),
                ('tastes_together', models.CharField(blank=True, max_length=63)),
                ('sum_of_marks', models.IntegerField(default=0)),
                ('count_marks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DrinkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('email', models.CharField(max_length=63)),
                ('body', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('advantages', models.TextField()),
                ('disadvantages', models.TextField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.drink')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='drink_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='app.drinktype'),
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('comment', models.TextField()),
                ('phone', models.CharField(max_length=31)),
                ('site_link', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=63)),
                ('drink_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to='app.drinktype')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='app.region'),
        ),
        migrations.AddField(
            model_name='drink',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='app.volume'),
        ),
    ]
