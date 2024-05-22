# Generated by Django 4.0.1 on 2024-05-22 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_vehiclelisting_additional_image1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclelisting',
            name='insurance_type',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='vehiclelisting',
            name='insurance_validity',
            field=models.DateField(default=datetime.date(2024, 5, 22)),
        ),
        migrations.AddField(
            model_name='vehiclelisting',
            name='mobile_number',
            field=models.CharField(default='Not provided', max_length=15),
        ),
        migrations.AddField(
            model_name='vehiclelisting',
            name='num_owners',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='vehiclelisting',
            name='registration_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehiclelisting',
            name='rto',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='vehiclelisting',
            name='seller_name',
            field=models.CharField(default='Not provided', max_length=100),
        ),
        migrations.AddField(
            model_name='vehiclelisting',
            name='transmission',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
