"""
URL configuration for villa project.
"""
from django.contrib import admin
from django.urls import path
from villApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path('regis/', views.regis, name='regis'),
    path("login/", views.login, name='login'),
    path("userdtl", views.userdtl, name='userdtl'),
    path("contact/", views.contact, name='contact'),
    path("why/", views.why, name='why'),
    path("shop/", views.shop, name='shop'),
    path("cart/", views.cart, name='cart'),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name='add_to_cart'),
    path("remove_from_cart/<int:cart_item_id>/", views.remove_from_cart, name='remove_from_cart'),
    path("add_product/", views.add_product, name='add_product'),
    path("checkout/", views.checkout, name='checkout'),
    path("testimonial/", views.testimonial, name='testimonial'),
    path("upload/", views.upload_image, name='upload_image'),
    path('delete_image/<int:id>/', views.delete_image, name='delete_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
