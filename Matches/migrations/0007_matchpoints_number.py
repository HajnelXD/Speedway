# Generated by Django 2.2.16 on 2020-12-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matches', '0006_matchpoints_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchpoints',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
