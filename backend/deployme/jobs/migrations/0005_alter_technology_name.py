# Generated by Django 5.2 on 2025-05-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_rename_technology_joboffer_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
