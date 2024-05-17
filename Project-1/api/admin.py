from django.contrib import admin
from api.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(Service, ServiceAdmin)
