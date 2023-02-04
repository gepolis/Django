from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    desc = models.CharField(max_length=255)
    cost = models.PositiveIntegerField(default=1000)
    imgurl = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pk} {self.brand}   {self.name}"
class Cart(models.Model):
    item = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    user = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{Item.objects.get(pk=self.pk).name}({self.count})"