# Generated by Django 4.1.7 on 2023-07-01 04:37

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='image',
            field=models.ImageField(default='reviews/reviews.png', upload_to=courses.models.Reviews.path_and_rename),
        ),
    ]
