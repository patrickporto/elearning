# Generated by Django 2.0.5 on 2018-05-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20180504_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
