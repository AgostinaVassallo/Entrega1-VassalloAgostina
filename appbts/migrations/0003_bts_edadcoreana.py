# Generated by Django 4.1.3 on 2023-01-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbts', '0002_army_alter_bts_integrantes_alter_coreasur_soft_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='bts',
            name='edadcoreana',
            field=models.IntegerField(default=''),
        ),
    ]
