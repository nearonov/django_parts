from django.db import models
from core.models import BaseModels
from manufacturers.models import Manufacturer
from categories.models import Category


class Part(BaseModels):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name}{self.code}"

    def save(self, *args, **kwargs) -> None:
        self.slug = self.code
        return super().save(*args, **kwargs)
