# Generated by Django 4.1.1 on 2022-09-29 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_passenger_passenger_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='passenger',
            field=models.ForeignKey(default='', max_length=20, on_delete=django.db.models.deletion.CASCADE, to='home.passenger'),
        ),
    ]