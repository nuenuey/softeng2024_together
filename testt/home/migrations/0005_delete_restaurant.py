# Generated by Django 4.1 on 2024-12-21 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_restaurant"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Restaurant",
        ),
    ]