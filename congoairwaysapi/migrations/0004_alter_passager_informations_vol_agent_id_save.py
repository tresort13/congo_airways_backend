# Generated by Django 4.0.5 on 2022-06-24 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('congoairwaysapi', '0003_manifest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passager_informations_vol',
            name='agent_id_save',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]