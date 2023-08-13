from django.contrib import admin
from django.urls import path
# from . views import products, customer
from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('products/', products),
#     path('customer/', customer),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.products),
    path('customer/', views.customer),
    path('dashboard/', views.dashboard),
    path('main/', views.main),
    path('navbar/', views.navbar),
    path('status/', views.status),
]
