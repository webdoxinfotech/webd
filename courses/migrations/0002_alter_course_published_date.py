# Generated by Django 4.1.7 on 2023-05-20 04:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]