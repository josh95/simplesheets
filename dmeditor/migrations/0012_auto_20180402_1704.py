# Generated by Django 2.0.3 on 2018-04-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmeditor', '0011_auto_20180402_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheets',
            name='description',
            field=models.CharField(default='poop', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheets',
            name='img_url',
            field=models.CharField(default='oop', max_length=300),
            preserve_default=False,
        ),
    ]
