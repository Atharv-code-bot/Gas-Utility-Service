from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    list_editable = ('status',)

    list_filter = ('status',)
    search_fields = ('customer__username', 'customer__email')
