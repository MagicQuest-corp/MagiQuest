# Generated by Django 5.0.4 on 2024-05-17 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_users_remove_mission_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
