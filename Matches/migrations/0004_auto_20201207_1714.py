# Generated by Django 2.2.16 on 2020-12-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matches', '0003_auto_20201124_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='guest_team_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]