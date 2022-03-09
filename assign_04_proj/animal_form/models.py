from django.db import models

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name