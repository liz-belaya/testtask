from django.conf import settings
from django.db import models
from django.utils import timezone


class Qr(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    campaign = models.CharField(max_length=200)
    sourse =  models.CharField(max_length=200)
    product =  models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    number_of_transitions = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="qr_images/" )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

#    def __str__(self):
#        return self.title
