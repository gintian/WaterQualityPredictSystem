# Generated by Django 2.0.1 on 2018-01-26 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WQPS', '0002_auto_20180126_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waterqualityrecord',
            name='CODMn',
        ),
    ]
