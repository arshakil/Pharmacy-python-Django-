from django.contrib import admin

from .models import Category, Medicine, Unit, MedicineType

# Register your models here.


admin.site.register(Category)
admin.site.register(MedicineType)
admin.site.register(Unit)
admin.site.register(Medicine)