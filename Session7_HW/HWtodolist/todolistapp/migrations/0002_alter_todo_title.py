# Generated by Django 4.0.3 on 2022-04-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
