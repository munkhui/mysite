from django.contrib import admin
from .models import Sensor

class SensorAdmin(admin.ModelAdmin):
    list_display = ["name", "mqtt_topic"]
# Register your models here.
admin.site.register(Sensor,SensorAdmin)
