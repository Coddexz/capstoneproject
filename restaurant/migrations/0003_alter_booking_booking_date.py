# Generated by Django 4.2.1 on 2023-05-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_booking_booking_date_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
