# Generated by Django 4.0.1 on 2022-02-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_alter_medicine_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_image', models.FileField(null=True, upload_to='static/images')),
                ('article_title', models.CharField(max_length=200)),
                ('article_brief', models.TextField()),
                ('article_sub_brief', models.TextField()),
            ],
        ),
    ]