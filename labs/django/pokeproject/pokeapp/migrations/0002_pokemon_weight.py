# Generated by Django 3.1.6 on 2021-02-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
