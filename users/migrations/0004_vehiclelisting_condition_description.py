# Generated by Django 4.0.1 on 2024-05-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_vehiclelisting_star_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclelisting',
            name='condition_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
