from django.contrib import admin
from django.urls import path, include
import os

urlpatterns = [
    path(os.environ.get('ADMIN_URL', default='admin/'), admin.site.urls),
    path('api/', include('myapp.urls')),
]
