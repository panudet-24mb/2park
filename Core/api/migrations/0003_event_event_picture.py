# Generated by Django 3.0.3 on 2020-12-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201204_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_picture',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
