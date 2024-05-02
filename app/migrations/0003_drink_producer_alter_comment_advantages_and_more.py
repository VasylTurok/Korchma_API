# Generated by Django 5.0.4 on 2024-05-02 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_drink_israting'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='producer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='app.producer'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='advantages',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='disadvantages',
            field=models.TextField(blank=True),
        ),
    ]