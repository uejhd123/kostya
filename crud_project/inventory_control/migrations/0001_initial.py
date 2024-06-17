# Generated by Django 5.0.6 on 2024-05-30 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TotalSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SaleToCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mfg', models.DateField()),
                ('exp', models.DateField()),
                ('sold_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               to='inventory_control.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mfg', models.DateField()),
                ('exp', models.DateField()),
                ('quantity', models.IntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product',
                                                  to='inventory_control.productdescription')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                to='inventory_control.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='ExpiredProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mfg', models.DateField()),
                ('exp', models.DateField()),
                ('quantity', models.IntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='expired_product',
                    to='inventory_control.productdescription')),
                ('warehouse', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='inventory_control.warehouse')),
            ],
        ),
    ]