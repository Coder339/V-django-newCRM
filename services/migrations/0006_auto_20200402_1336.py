# Generated by Django 3.0.4 on 2020-04-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20200402_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rate',
            new_name='cost',
        ),
    ]
