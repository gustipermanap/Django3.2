from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # yang ditambahkan


def tentang(request):  # yang ditambahkan
    return HttpResponse('Halaman Tentang')  # yang ditambahkan


def index(request):  # yang ditambahkan
    return HttpResponse('hallo')  # yang ditambahkan


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tentang/', tentang),  # yang ditambahkan
    path('index', index),  # yang ditambahkan
]
