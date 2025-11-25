from django.contrib import admin
from .models import Customer
from .models import ImageUploader

class customAdmin(admin.ModelAdmin):list_display=['cname','cadd','email','phone','unm','pw']

admin.site.register(Customer, customAdmin)
@admin.register(ImageUploader)
class ImageUploaderModelAdmin(admin.ModelAdmin):list_display = ['photo','date']