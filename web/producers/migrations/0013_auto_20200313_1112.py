# Generated by Django 3.0.3 on 2020-03-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0012_auto_20200313_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productionsiteinput',
            name='eligible_double_comptage',
        ),
        migrations.AddField(
            model_name='productionsite',
            name='eligible_dc',
            field=models.BooleanField(default=False),
        ),
    ]