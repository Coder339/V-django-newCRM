# Generated by Django 3.0.3 on 2020-04-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_remove_invoice_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='Total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
