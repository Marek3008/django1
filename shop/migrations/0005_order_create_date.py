# Generated by Django 4.2.7 on 2023-12-15 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='create_Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
