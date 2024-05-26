from django.urls import path
from pages.views import AboutView

# from django_parts.catalogs.views import CatalogView

urlpatterns = [
    path("about", AboutView.as_view(), name='about'),
]
