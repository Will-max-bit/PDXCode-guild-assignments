# Generated by Django 3.1.6 on 2021-02-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_app', '0002_auto_20210208_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
