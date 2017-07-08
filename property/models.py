# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Property(models.Model):
    """fields"""

    title = models.CharField('Title', max_length=100, blank=False, null=False)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    city = models.CharField('City', max_length=100, blank=False, null=False)
    state = models.CharField('State', max_length=100, blank=False, null=False)
    id_json = models.CharField('Id', unique=True, max_length=100, blank=False, null=False)
    purpose = models.CharField('Purpose', max_length=50, blank=False, null=False)
    listing_type = models.CharField('Listing Type', max_length=50, blank=False, null=False)
    published_on = models.CharField('Published On', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Imoveis"

    def __unicode__(self):
        return unicode(self.name)
