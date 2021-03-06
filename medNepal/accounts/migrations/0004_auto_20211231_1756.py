# Generated by Django 3.2.9 on 2021-12-31 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211231_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='profile_pic',
            field=models.FileField(default='static/default_user.png', upload_to='static/doctorProfile'),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile_pic',
            field=models.FileField(default='static/default_user.png', upload_to='static/patientProfile'),
        ),
    ]
