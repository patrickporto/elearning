# Generated by Django 2.0.5 on 2018-05-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0005_duvida'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessagem',
            name='tipo',
            field=models.CharField(default='conversa', max_length=40),
        ),
    ]