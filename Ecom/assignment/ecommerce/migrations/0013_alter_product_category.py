# Generated by Django 5.0.2 on 2024-02-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_rename_orders_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Clothing', 'Clothing')], max_length=20),
        ),
    ]