# Generated by Django 3.1.4 on 2020-12-31 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20201231_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(default='Name', max_length=10),
            preserve_default=False,
        ),
    ]
