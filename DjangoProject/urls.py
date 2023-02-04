from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="index"),
    path('cart',views.cart,name="cart"),
    path('about/',views.about,name="about"),
    path('items/',views.items_list, name="items"),
    path('items/<str:brand>',views.items_brand_list),
    path('item/<int:id>',views.item_page),
    path('admin/', admin.site.urls, name="adm"),
    path("register", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request,name="logout"),
    path("item/add/<int:item>", views.add_item,name="add_item"),
    path("test/",views.test,name="test")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
