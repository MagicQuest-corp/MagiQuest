# Generated by Django 5.0.4 on 2024-05-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_missions_mission'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/profiles'),
        ),
    ]
