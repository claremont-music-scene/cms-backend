# Generated by Django 3.1.1 on 2020-09-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0002_auto_20200909_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='address_full',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]