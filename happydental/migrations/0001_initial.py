# Generated by Django 3.2.18 on 2023-05-01 10:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import happydental.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=150, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['-price'],
                'unique_together': {('service_name', 'price')},
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Please enter a valid phone number,e.g. 123456789. Up to 15 digits allowed.', regex='^\\+?1?\\d{8,15}$')])),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '12:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30')], default='10:00', max_length=30)),
                ('dentist', models.ForeignKey(default=happydental.models.get_default_dentist, on_delete=django.db.models.deletion.CASCADE, to='happydental.dentist')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='happydental.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'date', 'time', 'service')},
            },
        ),
    ]
