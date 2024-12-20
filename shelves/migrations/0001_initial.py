# Generated by Django 5.0.6 on 2024-10-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='نام')),
                ('location', models.CharField(max_length=100, verbose_name='موقعیت')),
                ('capacity', models.IntegerField(verbose_name='تعداد')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
            options={
                'verbose_name': 'قفسه',
                'verbose_name_plural': 'قفسه ها',
            },
        ),
    ]
