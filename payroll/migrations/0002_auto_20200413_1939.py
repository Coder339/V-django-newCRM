# Generated by Django 3.0.3 on 2020-04-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlysalary',
            name='paid_leaves',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='monthlysalary',
            name='unpaid_leaves',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
