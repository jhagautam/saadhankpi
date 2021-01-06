# Generated by Django 3.1.4 on 2020-12-31 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_remove_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production_volume',
            name='data_updated',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales_order',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]