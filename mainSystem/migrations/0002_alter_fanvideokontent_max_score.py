# Generated by Django 5.0 on 2024-10-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanvideokontent',
            name='max_score',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
