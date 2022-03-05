from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name