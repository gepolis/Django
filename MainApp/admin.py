from django.contrib import admin
from MainApp.models import *


@admin.register(Item)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "count", "brand")

    list_filter = ('brand',)
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ("id","name", "count")
