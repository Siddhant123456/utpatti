# Generated by Django 3.2.9 on 2021-11-12 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_delete_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CropReview',
        ),
    ]