# Generated by Django 4.2.8 on 2023-12-21 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0005_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(default='ABC123', on_delete=django.db.models.deletion.CASCADE, to='hms.department'),
        ),
    ]
