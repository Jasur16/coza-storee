# Generated by Django 4.1.1 on 2022-09-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistorymodel',
            name='products',
            field=models.ManyToManyField(to='shop.productmodel'),
        ),
    ]
