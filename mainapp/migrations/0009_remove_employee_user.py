# Generated by Django 3.1.4 on 2020-12-31 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_employee_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]