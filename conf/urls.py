from django.contrib import admin
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
