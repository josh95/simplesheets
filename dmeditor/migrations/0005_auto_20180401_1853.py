# Generated by Django 2.0.3 on 2018-04-01 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmeditor', '0004_auto_20180401_1847'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ally',
            new_name='Allies',
        ),
        migrations.RenameModel(
            old_name='item',
            new_name='Items',
        ),
        migrations.RenameModel(
            old_name='level',
            new_name='Levels',
        ),
    ]
