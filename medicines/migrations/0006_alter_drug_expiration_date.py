# Generated by Django 5.0.6 on 2024-07-15 13:04

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0005_delete_stockalert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiration_date',
            field=django_jalali.db.models.jDateField(verbose_name='تاریخ انقضا'),
        ),
    ]
