# Generated by Django 3.1.6 on 2021-02-09 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Priority', to='ToDo_app.priority'),
        ),
    ]
