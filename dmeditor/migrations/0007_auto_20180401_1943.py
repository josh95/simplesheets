# Generated by Django 2.0.3 on 2018-04-01 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmeditor', '0006_auto_20180401_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='levels',
            name='dm_id',
        ),
        migrations.AddField(
            model_name='allies',
            name='dm_id',
            field=models.IntegerField(default=0),
        ),
    ]
