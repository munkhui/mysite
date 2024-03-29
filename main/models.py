from django.db import models

# Create your models here.

class Sensor(models.Model):
    name=models.CharField(max_length = 30)
    photo=models.ImageField(blank=True, null=True)
    mqtt_topic=models.CharField(max_length=30)

    def __str__(self):
        return self.name


