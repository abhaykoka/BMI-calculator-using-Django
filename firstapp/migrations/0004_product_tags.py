# Generated by Django 4.2.3 on 2023-08-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_product_tag_delete_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='firstapp.tag'),
        ),
    ]
