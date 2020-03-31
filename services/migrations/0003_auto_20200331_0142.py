# Generated by Django 3.0.3 on 2020-03-30 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20200331_0138'),
        ('services', '0002_addproductentry_addserviceentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='invoice',
        ),
        migrations.AddField(
            model_name='addproductentry',
            name='PO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.PurchaseOrder'),
        ),
        migrations.AddField(
            model_name='addserviceentry',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.Invoice'),
        ),
    ]
