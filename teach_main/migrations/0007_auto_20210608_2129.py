# Generated by Django 3.1.1 on 2021-06-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach_main', '0006_auto_20210608_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
