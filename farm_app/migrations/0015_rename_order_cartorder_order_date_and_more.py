# Generated by Django 4.2.3 on 2023-07-28 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0014_rename_order_date_cartorder_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='order',
            new_name='order_date',
        ),
        migrations.RenameField(
            model_name='cartorder',
            old_name='paid_status_order',
            new_name='paid_status',
        ),
    ]
