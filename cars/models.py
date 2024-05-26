from django.db import models
from manufacturers.models import Manufacturer
from parts.models import Part

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=64)
    parts = models.ManyToManyField(Part)

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"
