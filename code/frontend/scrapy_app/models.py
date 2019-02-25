from django.db import models
from djongo.models import ObjectIdField


class Vehicles(models.Model):
    _id = ObjectIdField()
    estimated_price = models.IntegerField()
    car_name = models.CharField(max_length=100)
    miles = models.CharField(max_length=500)
    vin = models.CharField(max_length=500)
    body = models.CharField(max_length=500)
    primary_damage = models.CharField(max_length=500)
    secondary_damage = models.CharField(max_length=500)
    start_code = models.CharField(max_length=500)
    key_fob = models.CharField(max_length=500)
    airbags = models.CharField(max_length=500)
    car_image = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    value_est = models.FloatField()

    class Meta:
        db_table = "scrapy_items"
