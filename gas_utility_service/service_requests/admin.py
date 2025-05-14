from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceReuqestAdmin(admin.ModelAdmin):
    list_display = ('customer','service_type','status','created_at')
    list_filter = ('status','service_type')

# Register your models here.
