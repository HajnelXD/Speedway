# Generated by Django 2.2.16 on 2020-12-21 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0004_team_stadium'),
        ('Matches', '0005_matchpoints_bonuses'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchpoints',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Teams.Team'),
            preserve_default=False,
        ),
    ]