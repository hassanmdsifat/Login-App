# Generated by Django 2.2.4 on 2019-08-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0004_auto_20190822_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
    ]