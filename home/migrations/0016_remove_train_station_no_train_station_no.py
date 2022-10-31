# Generated by Django 4.1.1 on 2022-09-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_station_train_no_train_station_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='station_no',
        ),
        migrations.AddField(
            model_name='train',
            name='station_no',
            field=models.ManyToManyField(to='home.station'),
        ),
    ]