# Generated by Django 2.2.1 on 2020-08-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planId', models.CharField(max_length=30, null=True)),
                ('Type', models.CharField(choices=[('PREPAID', 'Prepaid'), ('POSTPAID', 'Postpaid')], max_length=20, null=True)),
                ('duration', models.CharField(max_length=20, null=True)),
                ('dateOfCreation', models.DateField(null=True)),
                ('validity', models.DateField(null=True)),
                ('billingCycle', models.DateField(null=True)),
                ('dueDate', models.DateField(null=True)),
                ('terms', models.TextField(max_length=250, null=True, verbose_name='PlanTerms')),
            ],
            options={
                'verbose_name_plural': 'plan',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_no', models.CharField(max_length=30, null=True)),
                ('Product_name', models.CharField(max_length=20, null=True)),
                ('cost', models.FloatField()),
                ('Company_name', models.CharField(max_length=20)),
                ('Product_Description', models.TextField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'product',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceId', models.CharField(max_length=50, null=True)),
                ('name_c', models.CharField(max_length=100, null=True, verbose_name='company')),
                ('Type', models.CharField(default='Unknown', max_length=20, null=True, verbose_name='Type')),
                ('description', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
                ('Active', models.BooleanField(default='True')),
            ],
            options={
                'verbose_name_plural': 'Service',
            },
        ),
    ]
