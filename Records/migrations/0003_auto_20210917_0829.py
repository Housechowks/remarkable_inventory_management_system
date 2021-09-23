# Generated by Django 3.2.6 on 2021-09-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0002_auto_20210901_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='total_price',
            new_name='total_amount',
        ),
        migrations.AlterField(
            model_name='position',
            name='tonnages',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
