# Generated by Django 4.1 on 2024-12-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_delete_restaurant"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField()),
                ("operating_hours", models.TextField()),
                ("main_menu", models.TextField()),
                ("description", models.TextField()),
            ],
        ),
    ]