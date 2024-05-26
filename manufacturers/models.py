from django.db import models
from core.models import BaseModels


class Manufacturer(BaseModels):
    name = models.CharField(max_length=64, default="Manufacturer")
    description = models.TextField

    def __str__(self) -> str:
        return f"{self.name} "

