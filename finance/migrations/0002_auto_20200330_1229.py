# Generated by Django 3.0.4 on 2020-03-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20200330_1229'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='serviceTAG',
            field=models.ManyToManyField(to='services.Service'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='ItemTAG',
            field=models.ManyToManyField(to='services.Item'),
        ),
    ]
