# Generated by Django 3.0.3 on 2020-04-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SLA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_no', models.IntegerField()),
                ('problem_details', models.TextField(blank='False', null='False')),
                ('priority', models.CharField(choices=[('HIGH', 'High'), ('LOW', 'Low'), ('MODERATE', 'Moderate')], max_length=200)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('INITIATED', 'Initiated'), ('IN PROGRESS', 'In Progress'), ('RESOLVED', 'Resolved')], max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'SLA',
            },
        ),
    ]
