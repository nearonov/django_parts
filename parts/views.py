from django.views.generic import DetailView
from parts.models import Part


class PartDetailView(DetailView):
    model = Part
    context_object_name = 'part'
    template_name = "parts/detail.html"
