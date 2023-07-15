# Generated by Django 4.1.7 on 2023-07-01 04:57

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_reviews_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='image',
            field=models.ImageField(default='reviews/review.png', upload_to=courses.models.Reviews.path_and_rename),
        ),
    ]