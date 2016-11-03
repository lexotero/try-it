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


class SocialProfiles(models.Model):
    website = models.URLField(blank=True)
    twitter_profile = models.CharField(max_length=255, blank=True)
    facebook_profile = models.CharField(max_length=255, blank=True)
    linked_in_profile = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class Company(BaseModel, SocialProfiles):
    name = models.CharField(max_length=255, unique=True)

    description = HTMLField(blank=True)

    def __str__(self):
        return self.name


class Speaker(BaseModel, SocialProfiles):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    bio = HTMLField(blank=True)
    company = models.ForeignKey(Company, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class ActivityFormat(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = HTMLField(blank=True)

    def __str__(self):
        return self.name


class Activity(BaseModel):
    title = models.CharField(max_length=255)
    description = HTMLField(blank=True)
    format = models.ForeignKey(ActivityFormat)
    tags = models.ManyToManyField(Tag)

    speakers = models.ManyToManyField(Speaker)
    companies = models.ManyToManyField(Company)

    edition = models.ForeignKey(Edition)
    track = models.ForeignKey(Track, blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.title
