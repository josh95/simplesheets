# Generated by Django 2.0.3 on 2018-04-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmeditor', '0012_auto_20180402_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ally_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_id', models.IntegerField(default=0)),
                ('ally_id', models.IntegerField(default=0)),
                ('ally_level', models.IntegerField(default=0)),
                ('player_notes', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Item_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(default=0)),
                ('sheet_id', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]
