# Generated by Django 3.0.4 on 2020-04-02 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20200402_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='plan',
            new_name='duration',
        ),
    ]
