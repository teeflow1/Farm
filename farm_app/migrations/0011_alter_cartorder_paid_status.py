# Generated by Django 4.2.3 on 2023-07-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0010_alter_productimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='paid_status',
            field=models.BooleanField(default=True),
        ),
    ]
