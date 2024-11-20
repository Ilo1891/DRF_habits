# Generated by Django 5.0.6 on 2024-06-27 19:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("habits", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="select user",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="habits",
                to=settings.AUTH_USER_MODEL,
                verbose_name="owner",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="related_habit",
            field=models.ForeignKey(
                blank=True,
                help_text="select related_habit",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="habits.habit",
                verbose_name="related_habit",
            ),
        ),
    ]