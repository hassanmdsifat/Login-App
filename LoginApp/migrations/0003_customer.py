# Generated by Django 2.2.4 on 2019-08-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LoginApp', '0002_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phonenumber', models.CharField(max_length=15)),
                ('dob', models.DateTimeField()),
            ],
        ),
    ]
