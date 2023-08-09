from django.contrib import admin
from django.urls import path, include  # yang ditambahkan
from . import views  # yang ditambahkan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),  # yang ditambahkan
    path('', views.index),  # yang ditambahkan
    path('index', views.index,)  # yang ditambahkan
]
