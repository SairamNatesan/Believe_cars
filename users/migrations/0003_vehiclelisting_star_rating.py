# Generated by Django 4.0.1 on 2024-05-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_vehiclelisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclelisting',
            name='star_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
