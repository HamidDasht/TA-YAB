# Generated by Django 3.1.1 on 2021-06-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach_main', '0005_reply_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
