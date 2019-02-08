# Generated by Django 2.1.5 on 2019-02-02 03:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driverRegister', '0002_remove_driver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_plate_num',
            field=models.CharField(default='default value', max_length=264),
        ),
        migrations.AlterField(
            model_name='driver',
            name='max_num_passengers',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='driver',
            name='type',
            field=models.CharField(choices=[('1', 'Type1'), ('2', 'Type2'), ('3', 'Type3')], default='1', max_length=1),
        ),
    ]