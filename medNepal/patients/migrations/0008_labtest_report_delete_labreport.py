# Generated by Django 4.0.1 on 2022-01-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_labreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtest',
            name='report',
            field=models.FileField(null=True, upload_to='static/patientLabreport'),
        ),
        migrations.DeleteModel(
            name='Labreport',
        ),
    ]
