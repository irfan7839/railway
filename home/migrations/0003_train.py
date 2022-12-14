# Generated by Django 4.1.1 on 2022-09-13 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_coach'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=50)),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('availability_of_seats', models.IntegerField()),
                ('train_date', models.DateField()),
                ('coach_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.coach')),
            ],
        ),
    ]
