from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('items/',views.items_list),
    path('items/<str:brand>',views.items_brand_list),
    path('item/<int:id>',views.item_page),
    path('admin/', admin.site.urls),
]
