# Generated by Django 3.0.3 on 2020-04-10 15:47

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('SUPER USER', 'super user'), ('MANAGER', 'manager'), ('HR', 'hr'), ('STAFF', 'staff')], default='unknown', max_length=20, null=True, verbose_name='user role')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_Name', models.CharField(max_length=150, null=True)),
                ('company_Address1', models.CharField(max_length=150, null=True)),
                ('company_Address2', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('zip_code', models.CharField(max_length=150, null=True)),
                ('country', models.CharField(max_length=150, null=True)),
                ('company_Phone', models.CharField(max_length=150, null=True)),
                ('company_EmailId', models.CharField(max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'company',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email_id', models.CharField(max_length=150, null=True)),
                ('govt_id', models.CharField(choices=[('driving license', 'DRIVING LICENSE'), ('passport', 'PASSPORT'), ('aadhar', 'AADHAR CARD'), ('other', 'OTHER')], max_length=150, null=True)),
                ('id_no', models.CharField(max_length=150, null=True, unique=True, verbose_name='')),
                ('p_id1', models.CharField(max_length=150, null=True, verbose_name='PersonalID')),
                ('p_id_link', models.CharField(max_length=500, null=True, unique=True, verbose_name='')),
                ('contact', models.CharField(max_length=20, null=True, verbose_name='PhoneNo.')),
                ('address_1', models.CharField(max_length=150, null=True)),
                ('address_2', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('state', models.CharField(max_length=150, null=True)),
                ('country', models.CharField(max_length=150, null=True)),
                ('zip_code', models.CharField(max_length=150, null=True)),
                ('company_Name', models.CharField(max_length=150, null=True)),
                ('company_Address1', models.CharField(max_length=150, null=True)),
                ('company_Address2', models.CharField(max_length=150, null=True)),
                ('company_Phone', models.CharField(max_length=150, null=True)),
                ('company_EmailId', models.CharField(max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'vendor',
            },
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email_id', models.EmailField(max_length=150, null=True)),
                ('dob', models.DateField()),
                ('contact', models.CharField(max_length=20, null=True, verbose_name='PhoneNo.')),
                ('address_1', models.CharField(max_length=150, null=True)),
                ('address_2', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('state', models.CharField(max_length=150, null=True)),
                ('country', models.CharField(max_length=150, null=True)),
                ('zip_code', models.CharField(max_length=150, null=True)),
                ('govt_id', models.CharField(choices=[('driving license', 'DRIVING LICENSE'), ('passport', 'PASSPORT'), ('aadhar', 'AADHAR CARD'), ('other', 'OTHER')], max_length=150, null=True)),
                ('id_no', models.CharField(max_length=150, null=True, unique=True, verbose_name='')),
                ('employee_id', models.CharField(max_length=50, null=True, unique=True)),
                ('p_id1', models.CharField(max_length=150, null=True, verbose_name='PersonalID')),
                ('p_id2', models.CharField(max_length=500, null=True, unique=True, verbose_name='')),
                ('position', models.CharField(max_length=150, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('hr', models.BooleanField(default=False)),
                ('manager', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email_id', models.CharField(max_length=150, null=True)),
                ('govt_id', models.CharField(choices=[('driving license', 'DRIVING LICENSE'), ('passport', 'PASSPORT'), ('aadhar', 'AADHAR CARD'), ('other', 'OTHER')], max_length=150, null=True)),
                ('id_no', models.CharField(max_length=150, null=True, unique=True, verbose_name='')),
                ('p_id1', models.CharField(max_length=150, null=True, verbose_name='PersonalID')),
                ('p_id_link', models.CharField(max_length=500, null=True, unique=True, verbose_name='')),
                ('contact', models.CharField(max_length=20, null=True, verbose_name='PhoneNo.')),
                ('address_1', models.CharField(max_length=150, null=True)),
                ('address_2', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('state', models.CharField(max_length=150, null=True)),
                ('country', models.CharField(max_length=150, null=True)),
                ('zip_code', models.CharField(max_length=150, null=True)),
                ('createdBy', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='authentication.EmployeeProfile')),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
    ]
