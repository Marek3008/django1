# Generated by Django 4.2.7 on 2024-04-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0005_student_cislo_domu_student_obec_student_psc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='datum_narodenia',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='ucitel',
            name='datum_narodenia',
            field=models.DateField(null=True),
        ),
    ]
