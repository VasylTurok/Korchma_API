# Generated by Django 5.0.4 on 2024-05-12 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_producer_about_producer_email_producer_fb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='drink_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to='app.drinktype'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='site_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
