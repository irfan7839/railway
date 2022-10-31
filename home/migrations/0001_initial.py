# Generated by Django 4.1.1 on 2022-09-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('adhar_no', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField(default=0)),
                ('mobile_no', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=50)),
                ('security_ques', models.CharField(default='', max_length=50)),
                ('security_ans', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
