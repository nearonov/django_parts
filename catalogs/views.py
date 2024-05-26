from django.views.generic import ListView, TemplateView
from manufacturers.models import Manufacturer
from cars.models import Car
from categories.models import Category
from parts.models import Part

class CatalogView(ListView):
    model = Manufacturer
    context_object_name = "manufacturers"
    template_name = "catalogs/catalog.html"


class CatalogCarsView(ListView):
    context_object_name = "cars"
    template_name = "catalogs/catalog_cars.html"

    def get_queryset(self):
        qs = Car.objects.filter(manufacturer=self.kwargs["manufacturer"])
        return qs

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["manufacturer"] = self.kwargs["manufacturer"]
        return context


class CatalogCategoriesView(ListView):
    context_object_name = "categories"
    model = Category
    template_name = "catalogs/catalog_categories.html"

    # def get_queryset(self):
    #     qs = Category.objects.all()
    #     return qs

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["manufacturer"] = self.kwargs["manufacturer"]
        context["car"] = self.kwargs["car"]
        # context["category"] = self.kwargs["category"]
        return context

class CatalogPartsView(ListView):
    context_object_name = "parts"
    template_name = "catalogs/catalog_parts.html"

    def get_queryset(self):
        try:
            # car = Car.objects.get(id=self.kwargs["car"])
            car = Car.objects.get(id=self.kwargs["car"])
        except Exception:
            raise Exception
        qs = car.parts.filter(category=self.kwargs["category"])

        return qs


class IndexView(TemplateView):
    template_name = "catalogs/index.html"

