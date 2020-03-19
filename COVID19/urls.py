from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from stats.views import get_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
