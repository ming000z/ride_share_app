# Generated by Django 4.1.5 on 2023-02-03 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_order_driver_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rider_id',
            field=models.IntegerField(default=None),
        ),
    ]