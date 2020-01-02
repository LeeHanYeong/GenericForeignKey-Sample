from django.db import models


class SitePartition(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name