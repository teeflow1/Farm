# Generated by Django 4.2.3 on 2023-07-15 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0002_alter_product_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farm_app.farmer'),
        ),
    ]
