# Generated by Django 5.0.1 on 2024-03-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_hostel_hostelimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='contact',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
