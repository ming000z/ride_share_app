# Generated by Django 4.1.5 on 2023-02-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_order_rider_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver_id',
            field=models.IntegerField(default=None, null=True),
        ),
    ]