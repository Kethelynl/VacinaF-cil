# Generated by Django 5.1.2 on 2024-10-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vaccines",
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
                ("name_vacinne", models.CharField(max_length=100)),
                ("description", models.TimeField()),
                ("age_group", models.CharField(max_length=50)),
                ("doses", models.IntegerField()),
            ],
        ),
    ]
