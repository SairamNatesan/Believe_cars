# Generated by Django 4.0.1 on 2024-05-21 03:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_vehiclelisting_owner_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclelisting',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 5, 21, 3, 35, 50, 677826, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
