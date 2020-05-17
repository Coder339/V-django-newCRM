# Generated by Django 3.0.4 on 2020-05-08 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_company', models.CharField(max_length=20, null=True)),
                ('customer_name', models.CharField(max_length=20, null=True)),
                ('Invoice_number', models.CharField(max_length=30)),
                ('Invoice_date', models.DateField()),
                ('payment_terms', models.TextField(max_length=250, null=True)),
                ('Total', models.FloatField(blank=True, null=True)),
                ('customer', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Customer')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'invoice',
            },
        ),
        migrations.CreateModel(
            name='ServiceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=250, null=True)),
                ('rate', models.FloatField()),
                ('Qty', models.FloatField()),
                ('Discount', models.FloatField()),
                ('Tax', models.FloatField()),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.Invoice')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_company', models.CharField(max_length=50, null=True)),
                ('vendor_name', models.CharField(max_length=50, null=True)),
                ('PO_Number', models.CharField(max_length=50)),
                ('PO_Date', models.DateField()),
                ('Total', models.FloatField(blank=True, null=True)),
                ('Vendor', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Vendor')),
            ],
            options={
                'verbose_name_plural': 'purchaseOrder',
            },
        ),
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=250, null=True)),
                ('rate', models.FloatField()),
                ('Qty', models.FloatField()),
                ('Discount', models.FloatField()),
                ('Tax', models.FloatField()),
                ('PO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.PurchaseOrder')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Product')),
            ],
        ),
    ]
