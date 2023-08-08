from django.contrib import admin
from django.urls import path
from .view import index, tentang  # yang ditambahkan


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tentang/', tentang),  # yang ditambahkan
    path('index', index),  # yang ditambahkan
]
