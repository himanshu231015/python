from django.contrib import admin
from .models import Customer

class customAdmin(admin.ModelAdmin):list_display=['cname','cadd','email','phone','unm','pw']

admin.site.register(Customer, customAdmin)
