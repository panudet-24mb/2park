# Generated by Django 3.0.3 on 2020-12-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_event_event_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_device_uuid',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]