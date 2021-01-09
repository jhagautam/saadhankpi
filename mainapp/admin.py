from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(user_firm)
admin.site.register(User, UserAdmin)
admin.site.register(designation)
admin.site.register(product_category)
admin.site.register(product)
admin.site.register(KPIList)
admin.site.register(employee)
admin.site.register(production_volume)
admin.site.register(machines)
admin.site.register(maintenance_cost)
admin.site.register(customer)
admin.site.register(vendor)
admin.site.register(sales_order)
admin.site.register(purchase_order)
admin.site.register(sales_item)
admin.site.register(purchase_item)
admin.site.register(contactus)
