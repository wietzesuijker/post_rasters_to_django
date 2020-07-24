# Generated by Django 3.0.4 on 2020-06-24 08:10

from django.db import migrations, models
import drf_and_image_uploads.apps.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200623_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='raster',
            field=models.ImageField(blank=True, upload_to=drf_and_image_uploads.apps.accounts.models.upload_to, verbose_name='Raster'),
        ),
    ]