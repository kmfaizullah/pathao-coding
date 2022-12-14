# Generated by Django 4.0.3 on 2022-10-29 11:51

from django.db import migrations, models
import uuid


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
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('user_name', models.CharField(db_column='user_name', max_length=255, unique=True, verbose_name='User Name')),
                ('password', models.CharField(db_column='password', max_length=150, verbose_name='Password')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is Superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
        ),
    ]
