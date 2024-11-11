# Generated by Django 5.0.6 on 2024-10-26 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0004_delete_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationShelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='نام')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
            options={
                'verbose_name': 'موفعیت قفسه',
                'verbose_name_plural': 'موفعیت قفسه ها',
            },
        ),
        migrations.AlterField(
            model_name='shelf',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelfs', to='shelves.locationshelf', verbose_name='موقعیت'),
        ),
    ]