# Generated by Django 5.0.2 on 2024-03-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_customer_address_customer_city_customer_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='surname',
        ),
    ]
