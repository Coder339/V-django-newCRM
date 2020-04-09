# Generated by Django 3.0.3 on 2020-04-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business_opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email_id', models.EmailField(default='', max_length=100)),
                ('phone_no', models.CharField(default='', max_length=100)),
                ('additional_contact', models.CharField(default='', max_length=300, null='False')),
                ('details', models.CharField(max_length=300, null='False', verbose_name='')),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
                ('followup_date', models.DateField()),
                ('upload_documents', models.FileField(default='', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Business Opportunity',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
                ('owner', models.CharField(max_length=100)),
                ('team_lead', models.CharField(max_length=100)),
                ('task_assigned', models.CharField(default='', max_length=300)),
                ('project_status', models.CharField(choices=[('PLANNING', 'Planning'), ('DEVELOPMENT', 'Development'), ('TESTING', 'Testing'), ('DEPLOYMENT', 'Deployment'), ('COMPLETED', 'Completed')], default='', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=300, null='False')),
                ('task', models.CharField(max_length=300, null='False')),
                ('update', models.CharField(max_length=300, null='False')),
            ],
            options={
                'verbose_name_plural': 'Employee Report',
            },
        ),
    ]
