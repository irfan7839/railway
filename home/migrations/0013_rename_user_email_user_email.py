# Generated by Django 4.1.1 on 2022-09-26 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_email_user_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='User_email',
            new_name='email',
        ),
    ]
