# Generated by Django 4.1.5 on 2023-01-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_morphedimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morphedimages',
            name='morphedimage',
            field=models.ImageField(null=True, upload_to='morphed/'),
        ),
    ]