from django.contrib import admin

# Register your models here.

from .models import receiveTable, item

admin.site.register(receiveTable)
admin.site.register(item)