# Generated by Django 3.0.2 on 2020-01-24 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platformuser',
            name='entity',
        ),
        migrations.AddField(
            model_name='platformuser',
            name='user_type',
            field=models.CharField(choices=[('Producteur', 'Producteur'), ('Opérateur', 'Opérateur'), ('Administrateur', 'Administrateur')], default='Producteur', max_length=64),
        ),
        migrations.CreateModel(
            name='PlatformUserRights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Entity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Right',
                'verbose_name_plural': 'Users Rights',
                'db_table': 'users_rights',
            },
        ),
    ]