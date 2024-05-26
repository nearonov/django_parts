from django.urls import path
from articles.views import ArticleDetailView

# from django_parts.catalogs.views import CatalogView

urlpatterns = [
    path("<slug:slug>/", ArticleDetailView.as_view(), name='article_detail'),
]

