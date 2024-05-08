# Generated by Django 5.0.3 on 2024-05-07 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_order',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.order'),
        ),
        migrations.AddField(
            model_name='products_order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
        migrations.AddField(
            model_name='products_restaurant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
        migrations.AddField(
            model_name='products_restaurant',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant'),
        ),
    ]
