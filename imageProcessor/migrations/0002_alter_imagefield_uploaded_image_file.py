# Generated by Django 4.2.5 on 2023-09-27 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("imageProcessor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagefield",
            name="uploaded_image_file",
            field=models.ImageField(
                upload_to="images/",
                validators=[django.core.validators.validate_image_file_extension],
            ),
        ),
    ]