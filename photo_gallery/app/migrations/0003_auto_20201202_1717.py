# Generated by Django 3.1.3 on 2020-12-02 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_galleryimage_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='title',
        ),
    ]
