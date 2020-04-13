# Generated by Django 3.0.3 on 2020-04-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptId', models.CharField(max_length=10)),
                ('dept_name', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'department',
            },
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_holidays_allowed', models.IntegerField()),
                ('package', models.IntegerField()),
                ('Joining_date', models.DateField(null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('isactive', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'staffProfile',
            },
        ),
    ]
