from django.contrib import admin
from .models import Patient, Package, Staff, CarePlan, Reports


admin.site.register(Patient)
admin.site.register(Package)
admin.site.register(Staff)
admin.site.register(CarePlan)
admin.site.register(Reports)