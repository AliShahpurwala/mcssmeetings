# Generated by Django 3.1.1 on 2020-09-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meetingHeader',
            field=models.CharField(default='', max_length=255),
        ),
    ]
