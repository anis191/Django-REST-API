# Generated by Django 5.1.7 on 2025-05-23 02:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ratings',
            field=models.PositiveIntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
