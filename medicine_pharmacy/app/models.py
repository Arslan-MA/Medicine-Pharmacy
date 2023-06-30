from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=80)
    location = models.IntegerField()
    margin = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.location} - {self.margin}"


class Medicine(models.Model):
    name = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    quantity = models.IntegerField()
    pharmacy = models.ManyToManyField(Pharmacy)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.quantity}"
