from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        # verbose_name = "Categories"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        # return f"{self.name}"
        return self.name
