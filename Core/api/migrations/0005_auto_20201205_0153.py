# Generated by Django 3.0.3 on 2020-12-04 18:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_event_event_device_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_device_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]