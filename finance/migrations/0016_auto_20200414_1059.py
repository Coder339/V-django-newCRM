# Generated by Django 3.0.3 on 2020-04-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0015_productentry_serviceentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
