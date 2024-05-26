from django.urls import path
from catalogs.views import CatalogView, IndexView, CatalogCarsView, CatalogCategoriesView, CatalogPartsView

# from django_parts.catalogs.views import CatalogView

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('cars/<manufacturer>', CatalogCarsView.as_view(), name='catalog-cars-view'),
    path('cars/<manufacturer>/<car>', CatalogCategoriesView.as_view(), name='catalog-categories-view'),
    path('cars/<manufacturer>/<car>/<category>', CatalogPartsView.as_view(), name='catalog-parts-detail-view'),
    path('index/', IndexView.as_view(), name='index'),
]
