# Generated by Django 4.2.8 on 2023-12-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0004_remove_doctor_doctor_id_remove_patient_patient_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(default='ABC123', max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]