# Generated by Django 4.1.1 on 2022-09-27 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='berth_no',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='coach_type',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='no_of_passengers',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='status',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='train_no',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user_id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='chart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='chart_tickets', to='home.seat_chart'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='dest',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dest_ticket', to='home.station'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='dest_schedule',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dest_schedule_tickets', to='home.schedule'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='fare',
            field=models.IntegerField(null=True, verbose_name='Fare'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='passenger',
            field=models.CharField(default='', max_length=20, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='source',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='source_ticket', to='home.station'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='source_schedule',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='source_schedule_tickets', to='home.schedule'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='train',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='train_tickets', to='home.train'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='type',
            field=models.CharField(default='', max_length=2, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='home.user'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]