# Generated by Django 3.0.3 on 2020-03-12 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_lot_matiere_premiere2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='matiere_premiere2',
            new_name='biocarburant',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='volume2',
        ),
    ]
