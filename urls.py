from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

try:
    from django.conf.urls import url, include

    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
    ]
except ImproperlyConfigured:
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
