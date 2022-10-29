# Generated by Django 4.0.3 on 2022-10-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='amount',
            field=models.FloatField(blank=True, db_column='wallet_amount', default=5000.0, null=True, verbose_name='User wallet amount'),
        ),
    ]
