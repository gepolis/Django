from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    desc = models.CharField(max_length=255)
    cost = models.PositiveIntegerField(default=1000)
    imgurl = models.CharField(max_length=255)