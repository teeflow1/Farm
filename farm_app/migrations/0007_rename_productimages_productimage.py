# Generated by Django 4.2.3 on 2023-07-15 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0006_alter_product_product_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
    ]
