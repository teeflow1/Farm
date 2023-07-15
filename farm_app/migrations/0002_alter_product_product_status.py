# Generated by Django 4.2.3 on 2023-07-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'Processing'), ('disabled', 'Shipped'), ('rejected', 'Rejected'), ('published', 'Delivered')], default='In Review', max_length=10),
        ),
    ]