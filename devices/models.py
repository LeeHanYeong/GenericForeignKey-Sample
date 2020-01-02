from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Location(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # def __str__(self):
    #     return '{cls} - {name}'.format(
    #         cls=self.content_type
    #     )


class DeviceItem(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'DeviceItem (pk: {self.pk}, Location: {self.location})'
