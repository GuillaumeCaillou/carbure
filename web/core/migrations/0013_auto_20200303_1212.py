# Generated by Django 3.0.3 on 2020-03-03 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200226_1541'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FiliereProduction',
            new_name='MatierePremiere',
        ),
        migrations.AlterModelOptions(
            name='matierepremiere',
            options={'verbose_name': 'Matiere Premiere', 'verbose_name_plural': 'Matieres Premieres'},
        ),
        migrations.RenameField(
            model_name='lot',
            old_name='filiere_production',
            new_name='matiere_premiere',
        ),
        migrations.AlterModelTable(
            name='matierepremiere',
            table='matieres_premieres',
        ),
    ]