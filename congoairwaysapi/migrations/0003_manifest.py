# Generated by Django 4.0.5 on 2022-06-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congoairwaysapi', '0002_passager_informations_vol_agent_id_save'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manifest', models.FileField(upload_to='files')),
                ('date_heure_envoie', models.DateTimeField(auto_now_add=True)),
                ('date_envoie', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
