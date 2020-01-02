from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Location(models.Model):
    """
    장소를 나타내는 모델
    어떤 장소를 가리키는지는 content_object필드를 사용
        이 필드를 사용해서 Merchant, SitePartition, User등... 어디든 연결된다
        제약이 필요하다면 clean()이나 save()에 제약사항 정의 필요
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{cls} - {name}'.format(
            cls=self.content_object.__class__.__name__,
            name=self.content_object.name[:10],
        )


class DeviceItem(models.Model):
    cur_location_history = models.OneToOneField(
        'LocationHistory', on_delete=models.CASCADE,
        blank=True, null=True,
    )

    def __str__(self):
        return f'DeviceItem (pk: {self.pk}, Location: {self.cur_location_history})'


class LocationHistory(models.Model):
    device_item = models.ForeignKey(DeviceItem, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
