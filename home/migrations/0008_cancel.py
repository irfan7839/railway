# Generated by Django 4.1.1 on 2022-09-13 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_passenger_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.passenger')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]
