# Generated by Django 3.0.3 on 2020-04-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20200407_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='ea_delivery_accepted',
        ),
        migrations.AddField(
            model_name='lot',
            name='ea_delivery_status',
            field=models.CharField(choices=[('N', 'N/A'), ('A', 'Accepté'), ('AS', 'Accepté sous réserve'), ('R', 'Refusé')], default='N/A', max_length=64),
        ),
    ]