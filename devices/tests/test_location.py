import random

from django.test import TestCase
from model_bakery import baker

from devices.models import Location, DeviceItem, LocationHistory
from factories.models import Factory
from members.models import User
from merchants.models import Merchant
from sites.models import SitePartition


class LocationTest(TestCase):
    def test_location(self):
        # 임의의 Merchant, SitePartition, Factory, User를 생성
        merchant = baker.make(Merchant)
        site_partition = baker.make(SitePartition)
        factory = baker.make(Factory)
        user = baker.make(User)

        # 위에서 생성한 객체들과 연결되는 Location객체들 생성
        location_merchant = baker.make(Location, content_object=merchant)
        location_site_partition = baker.make(Location, content_object=site_partition)
        location_factory = baker.make(Location, content_object=factory)
        location_user = baker.make(Location, content_object=user)
        locations = (
            location_merchant,
            location_site_partition,
            location_factory,
            location_user,
        )

        # 특정 DeviceItem생성
        di = baker.make(DeviceItem)

        # di에 10개의 LocationHistory를 생성
        last_history = None
        for i in range(10):
            location = random.choice(locations)
            lh = baker.make(LocationHistory, device_item=di, location=location)
            last_history = lh
            di.cur_location_history = lh
            di.save()

        self.assertEqual(di.locationhistory_set.count(), 10)
        self.assertEqual(di.cur_location_history, last_history)
