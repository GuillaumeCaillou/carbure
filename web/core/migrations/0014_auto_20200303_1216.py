# Generated by Django 3.0.3 on 2020-03-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200303_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matierepremiere',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
