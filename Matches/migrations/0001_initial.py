# Generated by Django 2.2.16 on 2020-11-24 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Riders', '0006_auto_20201011_0919'),
        ('Teams', '0004_team_stadium'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_points', models.IntegerField()),
                ('guest_team_points', models.IntegerField()),
                ('date', models.DateField()),
                ('guest_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_team', to='Teams.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='Teams.Team')),
            ],
            options={
                'ordering': ['date'],
                'unique_together': {('home_team', 'guest_team', 'date')},
            },
        ),
        migrations.CreateModel(
            name='MatchPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_run', models.CharField(max_length=2)),
                ('second_run', models.CharField(max_length=2)),
                ('third_run', models.CharField(max_length=2)),
                ('fourth_run', models.CharField(max_length=2)),
                ('fifth_run', models.CharField(max_length=2)),
                ('sixth_run', models.CharField(max_length=2)),
                ('seventh_run', models.CharField(max_length=2)),
                ('joker_rider', models.IntegerField()),
                ('runs', models.CharField(max_length=2)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Matches.Match')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Riders.Rider')),
            ],
            options={
                'unique_together': {('rider', 'match')},
            },
        ),
    ]
