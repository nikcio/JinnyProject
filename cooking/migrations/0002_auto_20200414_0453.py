# Generated by Django 3.0.5 on 2020-04-14 02:53

import cooking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=cooking.models.get_recipe_image, verbose_name='Image'),
        ),
    ]
