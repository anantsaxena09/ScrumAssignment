# Generated by Django 5.0.2 on 2024-02-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='status',
            field=models.CharField(choices=[('married', 'Married'), ('single', 'Single')], default='single', max_length=10),
        ),
    ]
