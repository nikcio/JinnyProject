# Generated by Django 3.0.5 on 2020-04-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0008_description_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='title',
            field=models.CharField(default='title', max_length=255, null=True),
        ),
    ]
