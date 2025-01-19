# customers/admin.py
from django.contrib import admin
from .models import Customer  # Ensure this line imports the correct model

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username',)  # Display relevant fields
