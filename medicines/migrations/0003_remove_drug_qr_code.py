# Generated by Django 5.0.6 on 2024-10-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_drug_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='qr_code',
        ),
    ]
