# Generated by Django 2.2.1 on 2019-07-30 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_auto_20190730_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
