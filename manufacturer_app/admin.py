from django.contrib import admin
from .models import Manufacturer

# Register your models here.
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('m_name','m_phone','m_address','m_details','m_previous_blance','m_date')
  



admin.site.register(Manufacturer, ManufacturerAdmin)