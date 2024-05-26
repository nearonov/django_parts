from django.contrib import admin
from parts.models import Part

# admin.site.register(Part)


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("code",)}
