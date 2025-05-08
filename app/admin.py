from django.contrib import admin
from .models import CustomUser, Package  # Import Month model

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name')
    ordering = ('email',)

  
class PackageAdmin(admin.ModelAdmin):
    list_display = ('place', 'country', 'state', 'price', 'days', 'nights', 'is_active', 'is_trending', 'display_months')
    list_filter = ('is_active', 'is_trending', 'months')
    search_fields = ('place', 'country', 'state')

    # Custom method to display months in admin panel
    def display_months(self, obj):
        return ', '.join([dict(Package.MONTH_CHOICES).get(month, month) for month in obj.months])
    display_months.short_description = 'Months Available'

# Register the model with the custom admin
admin.site.register(Package, PackageAdmin)