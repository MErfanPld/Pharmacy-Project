# Generated by Django 5.0.6 on 2024-10-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0002_shelf_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, verbose_name='موقعیت انبار')),
                ('capacity', models.IntegerField(verbose_name='ظرفیت انبار')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
        ),
    ]