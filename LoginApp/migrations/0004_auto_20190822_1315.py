# Generated by Django 2.2.4 on 2019-08-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='dob',
            field=models.DateTimeField(verbose_name='Date of Birth'),
        ),
    ]
