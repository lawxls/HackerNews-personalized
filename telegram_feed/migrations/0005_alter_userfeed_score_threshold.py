# Generated by Django 4.1 on 2022-11-18 00:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("telegram_feed", "0004_alter_userfeed_score_threshold"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfeed",
            name="score_threshold",
            field=models.PositiveSmallIntegerField(
                default=1,
                validators=[django.core.validators.MaxValueValidator(10000)],
                verbose_name="Threshold to pass for a story to be sent",
            ),
        ),
    ]
