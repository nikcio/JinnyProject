# Generated by Django 3.0.5 on 2020-04-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0006_auto_20200414_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='type',
        ),
        migrations.RemoveField(
            model_name='title',
            name='type',
        ),
        migrations.AddField(
            model_name='description',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='title',
            name='title',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pagetype',
            name='descriptions',
            field=models.ManyToManyField(blank=True, to='cooking.Description'),
        ),
        migrations.AlterField(
            model_name='pagetype',
            name='titles',
            field=models.ManyToManyField(blank=True, to='cooking.Title'),
        ),
    ]
