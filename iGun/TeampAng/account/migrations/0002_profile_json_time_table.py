# Generated by Django 3.0.6 on 2020-05-29 12:37

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='json_time_table',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
