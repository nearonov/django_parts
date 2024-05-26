from django.db import models
from core.models import BaseModels


class Article(BaseModels):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
