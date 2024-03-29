# Generated by Django 2.2.3 on 2019-09-11 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_agreement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreement',
            old_name='state',
            new_name='condition',
        ),
        migrations.RemoveField(
            model_name='agreement',
            name='mileage_in',
        ),
        migrations.AlterField(
            model_name='agreement',
            name='payment_freq',
            field=models.CharField(choices=[('W', 'Weekly (7 Days)'), ('BW', 'Bi-Weekly (14 Days)'), ('M', 'Monthly (30 Days)'), ('BM', 'Bi-Monthly (60 Days)')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='term',
            field=models.CharField(choices=[('W', 'Weekly (7 Days)'), ('BW', 'Bi-Weekly (14 Days)'), ('M', 'Monthly (30 Days)'), ('BM', 'Bi-Monthly (60 Days)')], default='M', max_length=2),
        ),
    ]
