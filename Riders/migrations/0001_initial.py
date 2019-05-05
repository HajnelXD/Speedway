# Generated by Django 2.2 on 2019-05-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['last_name'],
                'unique_together': {('last_name', 'first_name')},
            },
        ),
    ]