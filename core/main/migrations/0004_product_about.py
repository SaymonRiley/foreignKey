# Generated by Django 4.2.7 on 2023-11-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.TextField(null=True, verbose_name='About Product'),
        ),
    ]
