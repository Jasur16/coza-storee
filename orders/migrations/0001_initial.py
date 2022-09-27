# Generated by Django 4.1.1 on 2022-09-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('gmail', models.EmailField(max_length=254, null=True)),
                ('comment', models.TextField(null=True)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'history',
                'verbose_name_plural': 'histories',
            },
        ),
    ]
