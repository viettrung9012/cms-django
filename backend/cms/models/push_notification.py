"""Model for Push Notifications
"""
from django.db import models
from django.utils import timezone

from .region import Region
from .language import Language


class PushNotification(models.Model):
    """Class representing the Push Notification base model

    Args:
        models : Databas model inherit from the standard django models
    """
    region = models.ForeignKey(Region, related_name='push_notifications', on_delete=models.CASCADE)
    channel = models.CharField(max_length=60)
    draft = models.BooleanField(default=True)
    sent_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # pylint does not recognize the related name as attribute
        # pylint: disable=E1101
        if self.translations.exists():
            return self.translations.first().title
        return ""

    class Meta:
        default_permissions = ()
        permissions = (
            ('view_push_notifications', 'Can view push notification'),
            ('edit_push_notifications', 'Can edit push notification'),
            ('send_push_notifications', 'Can send push notification'),
        )


class PushNotificationTranslation(models.Model):
    """Class representing the Translation of a Push Notification

    Args:
        models : Database model inherit from the standard django models
    """
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    push_notification = models.ForeignKey(PushNotification, related_name='translations', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        default_permissions = ()
