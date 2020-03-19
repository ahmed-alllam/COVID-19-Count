from django.contrib import admin

from core.models import LocationModel


class LocationAdmin(admin.ModelAdmin):
    """admin for location models"""
    list_display = ('country', 'country_code', 'confirmed')


admin.site.register(LocationModel, LocationAdmin)
