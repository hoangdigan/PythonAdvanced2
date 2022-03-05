from django.db import models

class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    year = models.IntegerField(default=0)
    series = models.CharField(max_length=20)

    def __str__(self):
        return self.manufacturer, self.car_model
