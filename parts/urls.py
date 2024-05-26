from django.urls import path
from parts.views import PartDetailView

urlpatterns = [
    path('<slug:slug>', PartDetailView.as_view(), name='part-detail-view'),
]
