# Generated by Django 3.2.9 on 2022-01-02 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211231_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='DoctorProfile',
        ),
        migrations.DeleteModel(
            name='PatientProfile',
        ),
    ]
