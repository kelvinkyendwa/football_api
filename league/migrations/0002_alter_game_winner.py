# Generated by Django 3.2.9 on 2021-11-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
