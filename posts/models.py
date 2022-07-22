from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255, default="")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption = models.CharField(max_length=2200, default="")
    date = models.DateField(null=False, blank=False)
    is_carousel_item = models.BooleanField(default=False, null=False, blank=False)
    location_id = models.CharField(default="", max_length=255)
    MEDIA_TYPE_CHOICES = [
        ('VD', 'VIDEO'),
        ('CR', 'CAROUSEL'),
        ('IM', 'IMAGE'),
    ]
    media_type = models.CharField(max_length=2, choices=MEDIA_TYPE_CHOICES, default='IM')
    STATUS_CHOICES = [
        ('RD', 'Ready'),
        ('UP', 'Uploaded'),
        ('PO', 'Posted'),
        ('ER', 'Error'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RD')
    thumb_offset = models.CharField(max_length=255, default="", null=False, blank=False)
    access_token = models.CharField(max_length=2200, default="", null=False, blank=False)
    ig_user_id = models.CharField(max_length=2200, default="", null=False, blank=False)
    is_posted = models.BooleanField(default=False)


class Photo(models.Model):
    title = models.CharField(max_length=100, default="")
    # photo = models.ImageField(upload_to='posts', null=False)
    url = models.CharField(null=False, blank=False, max_length=2200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
