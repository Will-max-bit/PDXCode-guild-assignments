# Generated by Django 3.1.6 on 2021-02-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0002_pokemon_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='url',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
