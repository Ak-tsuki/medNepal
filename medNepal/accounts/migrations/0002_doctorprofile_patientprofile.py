# Generated by Django 3.2.9 on 2021-12-31 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('profile_pic', models.FileField(default='static/default_user.png', upload_to='static/profile')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('departmentName', models.CharField(choices=[('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'), ('WednCritical Care Medicine Specialistsesday', 'WednCritical Care Medicine Specialistsesday'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Gastroenterologists', 'Gastroenterologists')], max_length=100)),
                ('hospitalName', models.CharField(max_length=200)),
                ('profile_pic', models.FileField(default='static/default_user.png', upload_to='static/profile')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
