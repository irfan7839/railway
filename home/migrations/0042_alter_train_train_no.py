# Generated by Django 4.1.1 on 2022-10-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='train_no',
            field=models.IntegerField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
