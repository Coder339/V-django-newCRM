# Generated by Django 3.0.3 on 2020-04-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_invoice_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Total',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
