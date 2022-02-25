# Generated by Django 3.2.6 on 2022-01-25 09:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_alter_medicine_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0004_threadmodel_messagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('total_price', models.IntegerField(null=True)),
                ('payment_method', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Esewa', 'Esewa'), ('Khalti', 'Khalti')], max_length=200, null=True)),
                ('payment_status', models.BooleanField(blank=True, default=False, null=True)),
                ('contact_no', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(10)])),
                ('contact_address', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.medicine')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]