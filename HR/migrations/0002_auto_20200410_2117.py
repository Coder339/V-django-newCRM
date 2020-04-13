# Generated by Django 3.0.3 on 2020-04-10 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payroll', '0001_initial'),
        ('HR', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='EmpId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.EmployeeProfile'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HR.Department'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='packageId',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='payroll.EmployeePackage'),
        ),
    ]
