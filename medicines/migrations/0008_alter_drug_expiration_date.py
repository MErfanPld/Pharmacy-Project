# Generated by Django 5.0.6 on 2024-07-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0007_alter_drug_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiration_date',
            field=models.CharField(max_length=255, verbose_name='تاریخ انقضا'),
        ),
    ]