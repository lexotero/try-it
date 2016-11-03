import datetime

from django.db import models
from tinymce.models import HTMLField

from tryit.models import BaseModel


class Edition(BaseModel):
    name = models.CharField(
        max_length=255,
        default=datetime.date.today().year,
        unique=True
    )

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    description = HTMLField(blank=True)

    def __str__(self):
        return self.name


class Speaker(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    bio = HTMLField(blank=True)
    company = models.ForeignKey(Company)

    website = models.URLField(blank=True)
    twitter_profile = models.CharField(max_length=255, blank=True)
    facebook_profile = models.CharField(max_length=255, blank=True)
    linked_in_profile = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey(Company, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
