# Generated by Django 4.0.5 on 2022-07-01 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congoairwaysapi', '0015_passager_informations_vol_avion_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passager_informations_vol',
            name='vol_info',
        ),
    ]