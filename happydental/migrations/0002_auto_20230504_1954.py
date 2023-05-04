# Generated by Django 3.2.10 on 2023-05-04 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('happydental', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('user', 'dentist', 'date', 'time', 'service')},
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happydental.dentist')),
            ],
            options={
                'unique_together': {('dentist', 'date', 'time')},
            },
        ),
    ]
