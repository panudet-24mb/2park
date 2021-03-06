# Generated by Django 3.0.3 on 2020-12-05 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201205_0153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.RenameField(
            model_name='user_has_car',
            old_name='user',
            new_name='Users',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_citizen_id',
            new_name='users_citizen_id',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_firstname',
            new_name='users_firstname',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_id',
            new_name='users_id',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_lastname',
            new_name='users_lastname',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_mobile',
            new_name='users_mobile',
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
