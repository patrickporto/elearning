# Generated by Django 2.0.5 on 2018-05-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0006_chatmessagem_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessagem',
            name='tipo',
            field=models.CharField(default='chat_message', max_length=40),
        ),
    ]
