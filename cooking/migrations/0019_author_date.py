# Generated by Django 3.0.5 on 2020-04-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0018_auto_20200415_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
