# Generated by Django 3.0.4 on 2020-04-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20200402_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productentry',
            name='Discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productentry',
            name='Qty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productentry',
            name='Tax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='serviceentry',
            name='Discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='serviceentry',
            name='Qty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='serviceentry',
            name='Tax',
            field=models.FloatField(),
        ),
    ]
