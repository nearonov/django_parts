from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('catalog/', include('catalogs.urls')),
    path('parts/', include('parts.urls')),
    path('', include('pages.urls')),
    path('', include('articles.urls')),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
