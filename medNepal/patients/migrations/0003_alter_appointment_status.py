# Generated by Django 3.2.9 on 2022-01-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]