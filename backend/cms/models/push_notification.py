from django.db import models
from django.utils import timezone

from .site import Site
from .language import Language


class PushNotification(models.Model):
    site = models.ForeignKey(Site)
    channel = models.CharField(max_length=60)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)


class PushNotificationTranslation(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    language = models.ForeignKey(Language)
    push_notification = models.ForeignKey(PushNotification)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
