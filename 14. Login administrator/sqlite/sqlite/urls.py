from django.contrib import admin
from django.urls import path
from .views import index, v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', v1),
    path('index',index),
]

