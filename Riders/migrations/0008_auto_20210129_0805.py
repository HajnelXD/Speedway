# Generated by Django 2.2.16 on 2021-01-29 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Riders', '0007_rider_rider_photo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rider',
            old_name='rider_photo_name',
            new_name='rider_photo',
        ),
    ]