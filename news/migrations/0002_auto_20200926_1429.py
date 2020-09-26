# Generated by Django 3.1.1 on 2020-09-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
