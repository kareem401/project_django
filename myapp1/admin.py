from django.contrib import admin

from .models import *

admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)
admin.site.register(post)