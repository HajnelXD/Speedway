# Generated by Django 2.2 on 2019-05-04 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Teams.Team')),
                ('years_in_ekstraliga', models.ManyToManyField(to='Teams.Year')),
            ],
        ),
    ]
