# Generated by Django 4.2 on 2023-04-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lor', '0005_alter_pers_character_alter_pers_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pers',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='static/images'),
        ),
    ]
