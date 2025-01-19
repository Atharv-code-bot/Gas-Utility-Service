from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')  # Display the relevant columns (adjust as needed)
    list_editable = ('status',)  # Make the 'status' field editable in the list view

    # Optional: Add filters or search functionality if needed
    list_filter = ('status',)  # Filter by status
    search_fields = ('customer__username', 'customer__email')  # Search by customer username or email
