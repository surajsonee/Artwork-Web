# Generated by Django 3.2.9 on 2021-12-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211214_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fulfilment',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
