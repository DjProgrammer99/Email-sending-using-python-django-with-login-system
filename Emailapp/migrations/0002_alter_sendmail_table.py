# Generated by Django 4.1.7 on 2023-04-09 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emailapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='sendmail',
            table='email',
        ),
    ]