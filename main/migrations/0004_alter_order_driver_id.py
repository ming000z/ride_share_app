# Generated by Django 4.1.5 on 2023-02-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver_id',
            field=models.IntegerField(default=None),
        ),
    ]