# Generated by Django 5.0.2 on 2024-02-16 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_alter_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
    ]
