from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.utils import timezone
import os
from uuid import uuid4
from pathlib import Path
from django.contrib.contenttypes.fields import GenericRelation


class Subject(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'images'
        ext = filename.split('.')[-1]
        name = Path(filename).stem
        # get filename
        if instance.pk:
            filename = '{}-{}.{}'.format(name,instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}-{}.{}'.format(name,uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(default="images/default.jpg", upload_to=path_and_rename)
    slug = models.SlugField(default="", null=False)

class Course(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'images'
        ext = filename.split('.')[-1]
        name = Path(filename).stem
        # get filename
        if instance.pk:
            filename = '{}-{}.{}'.format(name,instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}-{}.{}'.format(name,uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    text = RichTextUploadingField()
    image = models.ImageField(default="images/default.jpg", upload_to=path_and_rename)
    slug = models.SlugField(default="", null=False)
    published_date = models.DateTimeField(default=timezone.now)
    subjects = models.ManyToManyField(Subject, related_name="courses")
    seo_keywords = models.CharField(max_length=90, null=True, blank=True)
    seo_meta_desc = models.CharField(max_length=160, null=True, blank=True)

class Reviews(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'reviews'
        ext = filename.split('.')[-1]
        name = Path(filename).stem
        # get filename
        if instance.pk:
            filename = '{}-{}.{}'.format(name,instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}-{}.{}'.format(name,uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)


    name = models.CharField(max_length=50)
    review = models.TextField()
    profession = models.CharField(max_length=100)
    image = models.ImageField(default="reviews/review.png", upload_to=path_and_rename)
    active = models.BooleanField(default=False)


class Certificate(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'certificate'
        ext = filename.split('.')[-1]
        name = Path(filename).stem
        # get filename
        if instance.pk:
            filename = '{}-{}.{}'.format(name,instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}-{}.{}'.format(name,uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    student_name = models.CharField(max_length=80)
    course_name = models.CharField(max_length=255)
    ref_id = models.CharField(max_length=20)
    certificate = models.FileField(upload_to=path_and_rename, default="certificate/certificate.png", validators=[FileExtensionValidator(allowed_extensions=["pdf"])])