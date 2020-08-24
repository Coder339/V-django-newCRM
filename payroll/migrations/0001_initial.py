# Generated by Django 2.2.1 on 2020-08-24 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, null=True)),
                ('packageId', models.CharField(max_length=20, null=True)),
                ('salary', models.IntegerField()),
                ('dateOfPayment', models.DateField(null=True)),
                ('modeOfPayment', models.CharField(max_length=10)),
                ('unpaid_leaves_allowed', models.PositiveIntegerField()),
                ('paid_leaves_allowed', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=100, null=True)),
                ('empId', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.EmployeeProfile')),
            ],
            options={
                'verbose_name_plural': 'employeeSalary',
            },
        ),
        migrations.CreateModel(
            name='MonthlySalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaryMonth', models.DateField(null=True)),
                ('unpaid_leaves', models.PositiveIntegerField(null=True)),
                ('paid_leaves', models.PositiveIntegerField(null=True)),
                ('activeDays', models.PositiveIntegerField()),
                ('workingDays', models.PositiveIntegerField()),
                ('total_Salary_Amount', models.PositiveIntegerField()),
                ('EmpId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.EmployeeProfile')),
                ('salaryId', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='payroll.EmployeePackage')),
            ],
            options={
                'verbose_name_plural': 'monthlySalary',
            },
        ),
    ]
