from django.contrib import admin
from django.urls import path
from . import views
from profil import views as profilViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', profilViews.index),  # yang ditambahkan
    path('', views.index),  # yang ditambahkan
    path('index', views.index),
    path('about/', views.about),
]
