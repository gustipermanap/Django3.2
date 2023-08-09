from django.contrib import admin
from django.urls import path
from . import views
from profil import views as profilViews
from about import views as aboutViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', profilViews.index),  # yang ditambahkan
    path('', views.index),  # yang ditambahkan
    path('index', views.index),
    # path('about/', views.about),
    path('about/', aboutViews.index),  # yang ditambahkan
]
