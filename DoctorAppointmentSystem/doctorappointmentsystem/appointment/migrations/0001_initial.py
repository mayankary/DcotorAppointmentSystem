# Generated by Django 5.0.1 on 2024-02-19 05:16

import appointment.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('D', 'Doctor'), ('C', 'Customer')], default='C', max_length=1, verbose_name='Type')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Gender')),
                ('prifile_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('phone_no', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Mobile number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['last_name'],
            },
            bases=('appointment.user',),
            managers=[
                ('objects', appointment.models.CustomerManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('specialization', models.CharField(max_length=50, verbose_name='Specialization')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('experience', models.CharField(max_length=50, verbose_name='Experience')),
                ('fee', models.IntegerField(verbose_name='Fee')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Approve')),
            ],
            options={
                'ordering': ['specialization', 'last_name'],
            },
            bases=('appointment.user',),
            managers=[
                ('objects', appointment.models.DoctorManager()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=200, verbose_name='Review')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('date', models.DateField(verbose_name='Date')),
                ('is_cancelled', models.BooleanField(default=False, verbose_name='Cancelled')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.customer')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
            options={
                'ordering': ['start_time', '-date'],
            },
        ),
    ]
