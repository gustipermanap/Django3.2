from django.contrib import admin
from django.urls import path, include  # yang di tambahkan
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spp/', include('spp.urls')),  # yang ditambahkan
    path('', views.index),
    path('index', views.index),
]
