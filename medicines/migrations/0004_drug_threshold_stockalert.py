# Generated by Django 5.0.6 on 2024-07-14 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0003_alter_drug_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='threshold',
            field=models.IntegerField(default=10),
        ),
        migrations.CreateModel(
            name='StockAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=255)),
                ('viewed', models.BooleanField(default=False)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.drug')),
            ],
        ),
    ]