# Generated by Django 3.0.3 on 2020-05-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0013_auto_20200313_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producercertificate',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
